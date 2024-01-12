import asyncio
import base64
import decimal
import hashlib
import ipaddress
import json
import os
import platform
import statistics
import time
import warnings
from datetime import datetime
import pandas as pd
from httpx import AsyncClient, Limits, Timeout
import urllib.parse as urlparse
from logger_config import setup_logger

# Logger setup
logger = setup_logger()

number_of_cpus = os.cpu_count()
my_os = platform.system()
loop = asyncio.get_event_loop()
warnings.filterwarnings('ignore')

def get_local_rpc_settings_func(directory_with_pastel_conf=os.path.expanduser("~/.pastel/")):
    with open(os.path.join(directory_with_pastel_conf, "pastel.conf"), 'r') as f:
        lines = f.readlines()
    other_flags = {}
    rpchost = '127.0.0.1'
    rpcport = '19932'
    for line in lines:
        if line.startswith('rpcport'):
            value = line.split('=')[1]
            rpcport = value.strip()
        elif line.startswith('rpcuser'):
            value = line.split('=')[1]
            rpcuser = value.strip()
        elif line.startswith('rpcpassword'):
            value = line.split('=')[1]
            rpcpassword = value.strip()
        elif line.startswith('rpchost'):
            pass
        elif line == '\n':
            pass
        else:
            current_flag = line.strip().split('=')[0].strip()
            current_value = line.strip().split('=')[1].strip()
            other_flags[current_flag] = current_value
    return rpchost, rpcport, rpcuser, rpcpassword, other_flags

def write_rpc_settings_to_env_file_func(rpc_host, rpc_port, rpc_user, rpc_password, other_flags):
    with open('.env', 'w') as f:
        f.write(f"RPC_HOST={rpc_host}\n")
        f.write(f"RPC_PORT={rpc_port}\n")
        f.write(f"RPC_USER={rpc_user}\n")
        f.write(f"RPC_PASSWORD={rpc_password}\n")
        for current_flag in other_flags:
            current_value = other_flags[current_flag]
            f.write(f"{current_flag}={current_value}\n")
    return
    
def get_remote_rpc_settings_func():
    rpchost = '45.67.221.205'
    rpcuser = 'IzfUzMZI'
    rpcpassword = 'ku5YhVtKSNWMIYp'
    rpcport = '9932'
    return rpchost, rpcport, rpcuser, rpcpassword    

class JSONRPCException(Exception):
    def __init__(self, rpc_error):
        parent_args = []
        try:
            parent_args.append(rpc_error['message'])
        except Exception as e:
            logger.error(f"Error occurred in JSONRPCException: {e}")
            pass
        Exception.__init__(self, *parent_args)
        self.error = rpc_error
        self.code = rpc_error['code'] if 'code' in rpc_error else None
        self.message = rpc_error['message'] if 'message' in rpc_error else None

    def __str__(self):
        return '%d: %s' % (self.code, self.message)

    def __repr__(self):
        return '<%s \'%s\'>' % (self.__class__.__name__, self)

def EncodeDecimal(o):
    if isinstance(o, decimal.Decimal):
        return float(round(o, 8))
    raise TypeError(repr(o) + " is not JSON serializable")
    
class AsyncAuthServiceProxy:
    max_concurrent_requests = 5000
    _semaphore = asyncio.BoundedSemaphore(max_concurrent_requests)
    def __init__(self, service_url, service_name=None, reconnect_timeout=15, reconnect_amount=2, request_timeout=20):
        self.service_url = service_url
        self.service_name = service_name
        self.url = urlparse.urlparse(service_url)        
        self.client = AsyncClient(timeout=Timeout(request_timeout), limits=Limits(max_connections=200, max_keepalive_connections=10))
        self.id_count = 0
        user = self.url.username
        password = self.url.password
        authpair = f"{user}:{password}".encode('utf-8')
        self.auth_header = b'Basic ' + base64.b64encode(authpair)
        self.reconnect_timeout = reconnect_timeout
        self.reconnect_amount = reconnect_amount
        self.request_timeout = request_timeout

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            raise AttributeError
        if self.service_name is not None:
            name = f"{self.service_name}.{name}"
        return AsyncAuthServiceProxy(self.service_url, name)

    async def __call__(self, *args):
        async with self._semaphore: # Acquire a semaphore
            self.id_count += 1
            postdata = json.dumps({
                'version': '1.1',
                'method': self.service_name,
                'params': args,
                'id': self.id_count
            }, default=EncodeDecimal)
            headers = {
                'Host': self.url.hostname,
                'User-Agent': "AuthServiceProxy/0.1",
                'Authorization': self.auth_header,
                'Content-type': 'application/json'
            }
            for i in range(self.reconnect_amount):
                try:
                    if i > 0:
                        logger.warning(f"Reconnect try #{i+1}")
                        sleep_time = self.reconnect_timeout * (2 ** i)
                        logger.info(f"Waiting for {sleep_time} seconds before retrying.")
                        await asyncio.sleep(sleep_time)
                    response = await self.client.post(
                        self.service_url, headers=headers, data=postdata)
                    break
                except Exception as e:
                    logger.error(f"Error occurred in __call__: {e}")
                    err_msg = f"Failed to connect to {self.url.hostname}:{self.url.port}"
                    rtm = self.reconnect_timeout
                    if rtm:
                        err_msg += f". Waiting {rtm} seconds."
                    logger.exception(err_msg)
            else:
                logger.error("Reconnect tries exceeded.")
                return
            response_json = response.json()
            if response_json['error'] is not None:
                raise JSONRPCException(response_json['error'])
            elif 'result' not in response_json:
                raise JSONRPCException({
                    'code': -343, 'message': 'missing JSON-RPC result'})
            else:
                return response_json['result']
        
async def get_current_pastel_block_height_func():
    global rpc_connection
    best_block_hash = await rpc_connection.getbestblockhash()
    best_block_details = await rpc_connection.getblock(best_block_hash)
    curent_block_height = best_block_details['height']
    return curent_block_height

async def get_previous_block_hash_and_merkle_root_func():
    global rpc_connection
    previous_block_height = await get_current_pastel_block_height_func()
    previous_block_hash = await rpc_connection.getblockhash(previous_block_height)
    previous_block_details = await rpc_connection.getblock(previous_block_hash)
    previous_block_merkle_root = previous_block_details['merkleroot']
    return previous_block_hash, previous_block_merkle_root, previous_block_height

async def get_last_block_data_func():
    global rpc_connection
    current_block_height = await get_current_pastel_block_height_func()
    block_data = await rpc_connection.getblock(str(current_block_height))
    return block_data

async def check_psl_address_balance_func(address_to_check):
    global rpc_connection
    balance_at_address = await rpc_connection.z_getbalance(address_to_check) 
    return balance_at_address

async def get_raw_transaction_func(txid):
    global rpc_connection
    raw_transaction_data = await rpc_connection.getrawtransaction(txid, 1) 
    return raw_transaction_data

async def verify_message_with_pastelid_func(pastelid, message_to_verify, pastelid_signature_on_message) -> str:
    global rpc_connection
    verification_result = await rpc_connection.pastelid('verify', message_to_verify, pastelid_signature_on_message, pastelid, 'ed448')
    return verification_result['verification']

async def check_masternode_top_func():
    global rpc_connection
    masternode_top_command_output = await rpc_connection.masternode('top')
    return masternode_top_command_output

async def check_supernode_list_func():
    global rpc_connection
    masternode_list_full_command_output = await rpc_connection.masternodelist('full')
    masternode_list_rank_command_output = await rpc_connection.masternodelist('rank')
    masternode_list_pubkey_command_output = await rpc_connection.masternodelist('pubkey')
    masternode_list_extra_command_output = await rpc_connection.masternodelist('extra')
    masternode_list_full_df = pd.DataFrame([masternode_list_full_command_output[x].split() for x in masternode_list_full_command_output])
    masternode_list_full_df['txid_vout'] = [x for x in masternode_list_full_command_output]
    masternode_list_full_df.columns = ['supernode_status', 'protocol_version', 'supernode_psl_address', 'lastseentime', 'activeseconds', 'lastpaidtime', 'lastpaidblock', 'ipaddress:port', 'txid_vout']
    masternode_list_full_df.index = masternode_list_full_df['txid_vout']
    masternode_list_full_df.drop(columns=['txid_vout'], inplace=True)
    for current_row in masternode_list_full_df.iterrows():
            current_row_df = pd.DataFrame(current_row[1]).T
            current_txid_vout = current_row_df.index[0]
            current_rank = masternode_list_rank_command_output[current_txid_vout]
            current_pubkey = masternode_list_pubkey_command_output[current_txid_vout]
            current_extra = masternode_list_extra_command_output[current_txid_vout]
            masternode_list_full_df.loc[current_row[0], 'rank'] = current_rank
            masternode_list_full_df.loc[current_row[0], 'pubkey'] = current_pubkey
            masternode_list_full_df.loc[current_row[0], 'extAddress'] = current_extra['extAddress']
            masternode_list_full_df.loc[current_row[0], 'extP2P'] = current_extra['extP2P']
            masternode_list_full_df.loc[current_row[0], 'extKey'] = current_extra['extKey']
    masternode_list_full_df['lastseentime'] = pd.to_datetime(masternode_list_full_df['lastseentime'], unit='s')
    masternode_list_full_df['lastpaidtime'] = pd.to_datetime(masternode_list_full_df['lastpaidtime'], unit='s')
    masternode_list_full_df['activeseconds'] = masternode_list_full_df['activeseconds'].astype(int)
    masternode_list_full_df['lastpaidblock'] = masternode_list_full_df['lastpaidblock'].astype(int)
    masternode_list_full_df['activedays'] = [float(x)/86400.0 for x in masternode_list_full_df['activeseconds'].values.tolist()]
    masternode_list_full_df['rank'] = masternode_list_full_df['rank'].astype(int)
    masternode_list_full_df__json = masternode_list_full_df.to_json(orient='index')
    return masternode_list_full_df__json

async def get_network_storage_fees_func():
    global rpc_connection
    network_median_storage_fee = await rpc_connection.storagefee('getnetworkfee')
    network_median_nft_ticket_fee = await rpc_connection.storagefee('getnftticketfee')
    json_results = {'network_median_storage_fee': network_median_storage_fee, 'network_median_nft_ticket_fee': network_median_nft_ticket_fee}
    return json_results
    
async def get_local_machine_supernode_data_func():
    local_machine_ip = get_external_ip_func()
    supernode_list_full_df = await check_supernode_list_func()
    proper_port_number = statistics.mode([x.split(':')[1] for x in supernode_list_full_df['ipaddress:port'].values.tolist()])
    local_machine_ip_with_proper_port = local_machine_ip + ':' + proper_port_number
    local_machine_supernode_data = supernode_list_full_df[supernode_list_full_df['ipaddress:port'] == local_machine_ip_with_proper_port]
    if len(local_machine_supernode_data) == 0:
        logger.error('Local machine is not a supernode!')
        return 0, 0, 0, 0
    else:
        logger.info('Local machine is a supernode!')
        local_sn_rank = local_machine_supernode_data['rank'].values[0]
        local_sn_pastelid = local_machine_supernode_data['extKey'].values[0]
    return local_machine_supernode_data, local_sn_rank, local_sn_pastelid, local_machine_ip_with_proper_port

async def get_sn_data_from_pastelid_func(specified_pastelid):
    supernode_list_full_df = await check_supernode_list_func()
    specified_machine_supernode_data = supernode_list_full_df[supernode_list_full_df['extKey'] == specified_pastelid]
    if len(specified_machine_supernode_data) == 0:
        logger.error('Specified machine is not a supernode!')
        return pd.DataFrame()
    else:
        return specified_machine_supernode_data

async def get_sn_data_from_sn_pubkey_func(specified_sn_pubkey):
    supernode_list_full_df = await check_supernode_list_func()
    specified_machine_supernode_data = supernode_list_full_df[supernode_list_full_df['pubkey'] == specified_sn_pubkey]
    if len(specified_machine_supernode_data) == 0:
        logger.error('Specified machine is not a supernode!')
        return pd.DataFrame()
    else:
        return specified_machine_supernode_data

def check_if_transparent_psl_address_is_valid_func(pastel_address_string):
    if len(pastel_address_string) == 35 and (pastel_address_string[0:2] == 'Pt'):
        pastel_address_is_valid = 1
    else:
        pastel_address_is_valid = 0
    return pastel_address_is_valid

def check_if_transparent_lsp_address_is_valid_func(pastel_address_string):
    if len(pastel_address_string) == 35 and (pastel_address_string[0:2] == 'tP'):
        pastel_address_is_valid = 1
    else:
        pastel_address_is_valid = 0
    return pastel_address_is_valid

async def get_df_json_from_tickets_list_rpc_response_func(rpc_response):
    tickets_df = pd.DataFrame.from_records([rpc_response[idx]['ticket'] for idx, x in enumerate(rpc_response)])
    tickets_df['txid'] = [rpc_response[idx]['txid'] for idx, x in enumerate(rpc_response)]
    tickets_df['height'] = [rpc_response[idx]['height'] for idx, x in enumerate(rpc_response)]
    tickets_df_json = tickets_df.to_json(orient='index')
    return tickets_df_json

async def get_pastel_blockchain_ticket_func(txid):
    global rpc_connection
    response_json = await rpc_connection.tickets('get', txid )
    if len(response_json) > 0:
        ticket_type_string = response_json['ticket']['type']
        corresponding_reg_ticket_block_height = response_json['height']
        latest_block_height = await get_current_pastel_block_height_func()
        if int(corresponding_reg_ticket_block_height) < 0:
            logger.warning(f'The corresponding reg ticket block height of {corresponding_reg_ticket_block_height} is less than 0!')
        if int(corresponding_reg_ticket_block_height) > int(latest_block_height):
            logger.info(f'The corresponding reg ticket block height of {corresponding_reg_ticket_block_height} is greater than the latest block height of {latest_block_height}!')
        corresponding_reg_ticket_block_info = await rpc_connection.getblock(str(corresponding_reg_ticket_block_height))
        corresponding_reg_ticket_block_timestamp = corresponding_reg_ticket_block_info['time']
        corresponding_reg_ticket_block_timestamp_utc_iso = datetime.utcfromtimestamp(corresponding_reg_ticket_block_timestamp).isoformat()
        response_json['reg_ticket_block_timestamp_utc_iso'] = corresponding_reg_ticket_block_timestamp_utc_iso
        if ticket_type_string == 'nft-reg':
            activation_response_json = await rpc_connection.tickets('find', 'act', txid )
        elif ticket_type_string == 'action-reg':
            activation_response_json = await rpc_connection.tickets('find', 'action-act', txid )
        elif ticket_type_string == 'collection-reg':
            activation_response_json = await rpc_connection.tickets('find', 'collection-act', txid )
        else:
            activation_response_json = f'No activation ticket needed for this ticket type ({ticket_type_string})'
        if len(activation_response_json) > 0:
            response_json['activation_ticket'] = activation_response_json
        else:
            response_json['activation_ticket'] = 'No activation ticket found for this ticket-- check again soon'
        return response_json
    else:
        response_json = 'No ticket found for this txid'
    return response_json

async def get_all_pastel_blockchain_tickets_func(verbose=0):
    if verbose:
        logger.info('Now retrieving all Pastel blockchain tickets...')
    tickets_obj = {}
    list_of_ticket_types = ['id', 'nft', 'offer', 'accept', 'transfer', 'royalty', 'username', 'ethereumaddress', 'action', 'action-act'] # 'collection', 'collection-act'
    for current_ticket_type in list_of_ticket_types:
        if verbose:
            logger.info('Getting ' + current_ticket_type + ' tickets...')
        response = await rpc_connection.tickets('list', current_ticket_type)
        if response is not None and len(response) > 0:
            tickets_obj[current_ticket_type] = await get_df_json_from_tickets_list_rpc_response_func(response)
    return tickets_obj

async def get_usernames_from_pastelid_func(pastelid):
    global rpc_connection
    response = await rpc_connection.tickets('list', 'username')
    list_of_returned_usernames = []
    if response is not None and len(response) > 0:
        for idx, x in enumerate(response):
            if response[idx]['ticket']['pastelID'] == pastelid:
                list_of_returned_usernames.append(response[idx]['ticket']['username'])
    if len(list_of_returned_usernames) > 0:
        if len(list_of_returned_usernames) == 1:
            return list_of_returned_usernames[0]
        else:
            return list_of_returned_usernames
    else:
        return 'Error! No username found for this pastelid'

async def get_pastelid_from_username_func(username):
    global rpc_connection
    response = await rpc_connection.tickets('list', 'username')
    if response is not None and len(response) > 0:
        for idx, x in enumerate(response):
            if response[idx]['ticket']['username'] == username:
                return response[idx]['ticket']['pastelID']
    return 'Error! No pastelid found for this username'

async def testnet_pastelid_file_dispenser_func(password, verbose=0):
    logger.info('Now generating a pastelid...')
    response = await rpc_connection.pastelid('newkey', password)
    pastelid_data = ''
    pastelid_pubkey = ''
    if response is not None and len(response) > 0:
        if 'pastelid' in response:
            logger.info('The pastelid is ' + response['pastelid'])    
            logger.info('Now checking to see if the pastelid file exists...')
            pastelid_pubkey = response['pastelid']
            if os.path.exists('~/.pastel/testnet3/pastelkeys/' + response['pastelid']):
                logger.info('The pastelid file exists!')
                with open('~/.pastel/testnet3/pastelkeys/' + response['pastelid'], 'rb') as f:
                    pastelid_data = f.read()
                    return pastelid_data                     
            else:
                logger.info('The pastelid file does not exist!')
        else:
            logger.error('There was an issue creating the pastelid!')
    return pastelid_pubkey, pastelid_data
    

async def get_all_registration_ticket_txids_corresponding_to_a_collection_ticket_txid_func(collection_ticket_txid: str):
    global rpc_connection
    ticket_dict = await get_pastel_blockchain_ticket_func(collection_ticket_txid)
    ticket_type_string = ticket_dict['ticket']['type']
    if ticket_type_string == 'collection-reg':
        activation_ticket_data = ticket_dict['activation_ticket'] 
        item_type = ticket_dict['ticket']['collection_ticket']['item_type']
    elif ticket_type_string == 'collection-act':
        activation_ticket_data = ticket_dict
        item_type = ''
    else:
        error_string = 'The ticket type is neither collection-reg nor collection-act'
        logger.error(error_string)
        return error_string
    activation_ticket_txid = activation_ticket_data['txid']
    if item_type == 'sense':
        response_json = await rpc_connection.tickets('find', 'action', activation_ticket_txid )
    elif item_type == 'nft':
        response_json = await rpc_connection.tickets('find', 'nft', activation_ticket_txid )
    elif item_type == '':
        try:
            response_json = await rpc_connection.tickets('find', 'action', activation_ticket_txid )
        except Exception as e:
            logger.error(f'Exception occurred while trying to find the activation ticket in the blockchain: {e}')
            try:
                response_json = await rpc_connection.tickets('find', 'nft', activation_ticket_txid )
            except Exception as e:
                response_json = 'Unable to find the activation ticket in the blockchain'
    else:
        response_json = f'The txid given ({collection_ticket_txid}) is not a valid activation ticket txid for a collection ticket'
    return response_json
        

#Misc helper functions:
class MyTimer():
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        runtime = end - self.start
        msg = '({time} seconds to complete)'
        logger.info(msg.format(time=round(runtime, 2)))


def compute_elapsed_time_in_minutes_between_two_datetimes_func(start_datetime, end_datetime):
    time_delta = (end_datetime - start_datetime)
    total_seconds_elapsed = time_delta.total_seconds()
    total_minutes_elapsed = total_seconds_elapsed / 60
    return total_minutes_elapsed


def compute_elapsed_time_in_minutes_since_start_datetime_func(start_datetime):
    end_datetime = datetime.utcnow()
    total_minutes_elapsed = compute_elapsed_time_in_minutes_between_two_datetimes_func(start_datetime, end_datetime)
    return total_minutes_elapsed


def get_sha256_hash_of_input_data_func(input_data_or_string):
    if isinstance(input_data_or_string, str):
        input_data_or_string = input_data_or_string.encode('utf-8')
    sha256_hash_of_input_data = hashlib.sha3_256(input_data_or_string).hexdigest()
    return sha256_hash_of_input_data


def check_if_ip_address_is_valid_func(ip_address_string):
    try:
        _ = ipaddress.ip_address(ip_address_string)
        ip_address_is_valid = 1
    except Exception as e:
        logger.error('Validation Error: ' + str(e))
        ip_address_is_valid = 0
    return ip_address_is_valid


def get_external_ip_func():
    output = os.popen('curl ifconfig.me')
    ip_address = output.read()
    return ip_address


async def check_if_pasteld_is_running_correctly_and_relaunch_if_required_func():
    pasteld_running_correctly = 0
    try:
        current_pastel_block_number = await get_current_pastel_block_height_func()
    except Exception as e:
        logger.error(f"Problem running pastel-cli command: {e}")
        current_pastel_block_number = ''
    if isinstance(current_pastel_block_number, int):
        if current_pastel_block_number > 100000:
            pasteld_running_correctly = 1
            logger.info('Pasteld is running correctly!')
    if pasteld_running_correctly == 0:
        logger.info('Pasteld was not running correctly, trying to restart it...')
        process_output = os.system("cd /home/pastelup/ && tmux new -d ./pastelup start walletnode --development-mode")
        logger.info('Pasteld restart command output: ' + str(process_output))
    return pasteld_running_correctly


def install_pasteld_func(network_name='testnet'):
    install_pastelup_script_command_string = "mkdir ~/pastelup && cd ~/pastelup && wget https://github.com/pastelnetwork/pastelup/releases/download/v2.0.5/pastelup-linux-amd64 && mv pastelup-linux-amd64 pastelup && chmod 755 pastelup"
    command_string = f"cd ~/pastelup && ./pastelup install walletnode -n={network_name} --force -r=latest -p=18.118.218.206,18.116.26.219 && \
                        sed -i -e '/hostname/s/localhost/0.0.0.0/' ~/.pastel/walletnode.yml && \
                        sed -i -e '$arpcbind=0.0.0.0' ~/.pastel/pastel.conf && \
                        sed -i -e '$arpcallowip=172.0.0.0/8' ~/.pastel/pastel.conf && \
                        sed -i -e 's/rpcuser=.*/rpcuser=rpc_user/' ~/.pastel/pastel.conf && \
                        sed -i -e 's/rpcpassword=.*/rpcpassword=rpc_pwd/' ~/.pastel/pastel.conf"
    if os.path.exists('~/pastelup/pastelup'):
        logger.info('Pastelup is already installed!')
        logger.info('Running pastelup install command...')
        try:
            command_result = os.system(command_string)
            if not command_result:
                logger.info('Pastelup install command appears to have run successfully!')
        except Exception as e:
            logger.error(f"Error running pastelup install command! Message: {e}; Command result: {command_result}")
    else:
        logger.info('Pastelup is not installed, trying to install it...')
        try:
            install_result = os.system(install_pastelup_script_command_string)
            if not install_result:
                logger.info('Pastelup installed successfully!')
                logger.info('Running pastelup install command...')
                command_result = os.system(command_string)
            else:
                logger.info(f"Pastelup installation failed! Message: {install_result}") 
        except Exception as e:
            logger.error(f"Error running pastelup install command! Message: {e}; Command result: {install_result}")
    return
            

#_______________________________________________________________


rpc_host, rpc_port, rpc_user, rpc_password, other_flags = get_local_rpc_settings_func()
rpc_connection = AsyncAuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")


