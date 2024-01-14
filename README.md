# Pastel Network RPC API Wrapper

## Overview

This project is a complete FastAPI REST API wrapper for the Pastel Network's `pasteld`, similar to `bitcoind`, providing a user-friendly interface to interact with the Pastel blockchain. It exposes all RPC methods with thorough documentation, making it easier for developers to integrate Pastel blockchain functionalities into various applications.

## Features

- **Comprehensive Coverage**: Includes all RPC methods available in the `pasteld`.
- **Asynchronous Support**: Utilizes FastAPI and async calls for efficient network communication.
- **Detailed Documentation**: Each endpoint is documented with descriptions, parameters, example requests, and responses.
- **Logging and Error Handling**: Features robust logging and error management for reliable operation.
- **Modular Design**: The code is organized into modules for easy maintenance and scalability.

## Installation

To use this API wrapper, you need to have Python installed on your machine. Follow these steps:

1. Clone the repository and install project in venv:
   ```
   git clone https://github.com/pastelnetwork/pastel-rpc-rest-wrapper.git
   cd pastel-rpc-rest-wrapper
   python3 -m venv venv
   source venv/bin/activate
   python3 -m pip install --upgrade pip
   python3 -m pip install wheel
   pip install -r requirements.txt

   ```

   Or, if you want to use PyEnv and Python 3.12:

   ```
   git clone https://github.com/pastelnetwork/pastel-rpc-rest-wrapper.git
   if ! command -v pyenv &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
    source ~/.zshrc
   fi
   cd ~/.pyenv && git pull && cd -
   pyenv install 3.12

   # Setup project with Python 3.12

   cd pastel-rpc-rest-wrapper
   pyenv local 3.12
   python -m venv venv
   source venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install wheel
   pip install -r requirements.txt
   ```

## Getting Started

After installation, you can start the FastAPI server using:

```
python3 main.py
```

This will host the API on `http://localhost:8000` by default.

## Endpoints List

The API categorizes endpoints based on their functionality. Below is a list of available endpoints:

### Blockchain Methods
- `/getbestblockhash`
- `/submitblock`
- `/estimatefee`
- `/getnextblocksubsidy`
- `/getblockcount`
- `/getdifficulty`
- `/getrawmempool`
- `/getblockheader/{block_hash}`
- `/getblockhash`
- `/getblock`
- `/gettxoutsetinfo`
- `/verifychain`
- `/gettxout`
- `/getchaintips`
- `/reconsiderblock`
- `/invalidateblock`
- `/getblockdeltas/{block_hash}`
- `/getblockchaininfo`

### Utility Methods
- `/ping`
- `/validateaddress`
- `/z_validateaddress`
- `/createmultisig`
- `/verifymessage`
- `/getaddressmempool`
- `/getmemoryinfo`
- `/estimatepriority`
- `/generate-report/{report_name}`
- `/getfeeschedule`
- `/decodescript`
- `/getmempoolinfo`
- `/addmultisigaddress`
- `/signmessage`
- `/getreceivedbyaddress`
- `/move`
- `/settxfee`
- `/getwalletinfo`
- `/listlockunspent`
- `/resendwallettransactions`
- `/listunspent`
- `/z_listunspent`
- `/zcbenchmark`
- `/z_listaddresses`
- `/z_listreceivedbyaddress`
- `/z_getbalance/{address}`
- `/z_gettotalbalance`
- `/z_viewtransaction/{txid}`
- `/z_getoperationresult`
- `/z_getoperationstatus`
- `/z_sendmany`
- `/z_shieldcoinbase`
- `/z_mergetoaddress`
- `/z_listoperationids`
- `/z_getnotescount`
- `/

gettxfee/{txid}`
- `/scanformissingtxs`
- `/fixmissingtxs/{starting_height}`
- `/backupwallet`
- `/keypoolrefill`
- `/walletlock`
- `/encryptwallet`
- `/walletpassphrasechange`
- `/lockunspent`

### Network Methods
- `/getaddednodeinfo`
- `/getconnectioncount`
- `/getpeerinfo`
- `/addnode`
- `/disconnectnode`
- `/getnettotals`
- `/getnetworksinfo`
- `/listbanned`
- `/getinfo`

### Control Methods
- `/setban`
- `/getdeprecationinfo`
- `/setaccount`

### Wallet Methods
- `/importprivkey`
- `/importaddress`
- `/z_importwallet`
- `/importwallet`
- `/dumpprivkey

- `/z_exportwallet`
- `/dumpwallet`
- `/z_importkey`
- `/z_importviewingkey`
- `/z_exportkey`
- `/z_exportviewingkey`
- `/getnewaddress`
- `/getaccountaddress`
- `/getrawchangeaddress`
- `/getaccount/{zcashaddress}`
- `/getaddressesbyaccount`
- `/sendtoaddress`
- `/listaddressgroupings`
- `/listaddressamounts`
- `/getreceivedbyaccount`
- `/getbalance`
- `/sendfrom`
- `/sendmany`
- `/listreceivedbyaddress`
- `/listtransactions`
- `/listaccounts`
- `/listsinceblock`
- `/gettransaction/{txid}`
- `/walletpassphrase`

### Mining Methods
- `/getnetworksolps`
- `/getlocalsolps`
- `/refreshminingmnidinfo`
- `/getgenerate`
- `/generate`
- `/setgenerate`
- `/prioritisetransaction`
- `/getmininginfo`
- `/getblocktemplate`
- `/getblocksubsidy`

### Raw Transaction Methods
- `/getrawtransaction`
- `/gettxoutproof`
- `/createrawtransaction`
- `/signrawtransaction`
- `/sendrawtransaction`
- `/fundrawtransaction`
- `/z_mergetoaddress`

### Ticket Methods
- `/tickets/get`
- `/tickets/findbylabel/{ticket_type}/{label}`
- `/tickets/{command}`
- `/tickets/tools/gettotalstoragefee`
- `/tickets/tools/estimatenftstoragefee`
- `/tickets/tools/validateownership`
- `/tickets/tools/searchthumbids`
- `/tickets/tools`
- `/tickets/register/mnid`
- `/tickets/register_id`
- `/tickets/register/nft`
- `/tickets/registercollection`
- `/tickets/register/offer`
- `/tickets/register/accept`
- `/tickets/register/transfer`
- `/tickets/register_royalty`
- `/tickets/register/down`
- `/tickets/register/username`
- `/tickets/register/ethereumaddress`
- `/tickets/register_action`
- `/tickets/list`

### Supernode Methods
- `/masternodelist`
- `/masternode/outputs`
- `/masternode/init`
- `/masternode/make_conf`
- `/masternode/clear-cache`
- `/masternode_pose_ban_score`
- `/masternode/message`
- `/masternode/command`
- `/masternodebroadcast`



## Detailed Overview of Core Components in `service_functions.py`

### `AsyncAuthServiceProxy` Class

- **Purpose**: This class serves as the main client for making asynchronous RPC calls to the Pastel Network's `pasteld` daemon. 
- **Key Features**:
  - **Throttling Requests**: Utilizes an asyncio semaphore (`_semaphore`) to limit the number of concurrent requests, ensuring that the server is not overwhelmed.
  - **Reconnection Logic**: Implements a retry mechanism (`reconnect_amount`) for handling connection failures, with an exponential backoff strategy (`reconnect_timeout`).
  - **HTTP Client Configuration**: Uses `httpx.AsyncClient` for HTTP requests, configured with custom timeout (`request_timeout`) and connection limits.
  - **Basic Authentication**: Constructs an authorization header using Base64 encoding for secure communication with the RPC server.

### `JSONRPCException` Class

- **Purpose**: A custom exception class to handle JSON RPC-specific errors.
- **Implementation**: Captures the error code and message from RPC responses and formats them for easier debugging and logging.

### Configuration Functions

1. **`get_local_rpc_settings_func`**: 
   - Reads the Pastel configuration file (`pastel.conf`) to extract local RPC settings like host, port, and credentials.
   - Parses the file line-by-line, categorizing standard and additional flags for use in establishing RPC connections.

2. **`write_rpc_settings_to_env_file_func`**:
   - Writes RPC configuration settings to a `.env` file, facilitating environment-based configuration management.

3. **`get_remote_rpc_settings_func`**:
   - Returns hardcoded RPC settings for remote connections (used as a fallback or alternative setup).

### Decimal Encoding

- **`EncodeDecimal`**: A utility function to convert `decimal.Decimal` instances to floats. This is necessary for JSON serialization, as JSON does not natively support decimal types.

### Asynchronous RPC Helper Functions

- **Purpose**: These functions (`get_current_pastel_block_height_func`, `get_previous_block_hash_and_merkle_root_func`, etc.) are designed to interact with the Pastel blockchain, retrieving various types of data like block height, transaction details, and node information.
- **Implementation**: Each function leverages the `AsyncAuthServiceProxy` to make async calls to `pasteld`. They serve as building blocks for the API endpoints, abstracting complex RPC calls into simpler, reusable functions.

### Miscellaneous Helper Functions and Classes

- **`MyTimer`**: A context manager class for timing operations, useful for performance monitoring.
- **`check_if_ip_address_is_valid_func`, `get_external_ip_func`**: Functions for IP address validation and retrieval, aiding in network-related operations.

### `check_if_pasteld_is_running_correctly_and_relaunch_if_required_func` Function

- **Purpose**: This function checks whether the `pasteld` daemon is running correctly and restarts it if necessary.
- **Process**:
  1. **Check Pastel Daemon Status**: It tries to fetch the current Pastel block number using `get_current_pastel_block_height_func`. If this operation is successful and the block number is greater than 100,000, it is assumed that `pasteld` is running correctly.
  2. **Error Handling**: In case of an exception (e.g., daemon not responding), an error is logged.
  3. **Restarting Daemon**: If `pasteld` is not running correctly (determined by the block number check or an exception), the function attempts to restart it. It uses the `os.system` command to run `pastelup start walletnode` in a new `tmux` session. This ensures that `pasteld` continues running in the background.
  4. **Logging**: The function logs the output of the restart command and whether `pasteld` was running correctly.

### `install_pasteld_func` Function

- **Purpose**: Installs and configures the Pastel daemon (`pasteld`) and its dependencies.
- **Process**:
  1. **Preparation for Installation**: The function prepares a command string to download `pastelup`, a utility for installing `pasteld`, and sets the necessary permissions.
  2. **Installation Process**:
     - If `pastelup` is already installed, it runs the `pastelup install` command.
     - If not, it downloads `pastelup` and then executes the installation command.
  3. **Network Configuration**: Allows specifying the network name (default is `testnet`). It also modifies the configuration files (`walletnode.yml` and `pastel.conf`) to set up the correct network settings, RPC credentials, and permissions.
  4. **Error Handling**: Logs are generated for each step of the process, capturing success, failure, or any exceptions encountered.
