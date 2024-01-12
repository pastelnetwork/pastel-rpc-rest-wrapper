import service_functions
from logger_config import setup_logger
from service_functions import get_local_rpc_settings_func
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, Field
from json import JSONEncoder
from datetime import datetime
from typing import Optional, List, Dict, Any, Union
logger = setup_logger()

# RPC Client Dependency
async def get_rpc_connection():
    rpc_host, rpc_port, rpc_user, rpc_password, other_flags = get_local_rpc_settings_func() 
    return service_functions.AsyncAuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

router = APIRouter()

tags_metadata = [
    {"name": "High-Level Methods", "description": "Endpoints that are not actually part of the Pastel RPC API, but operate at a higher level of abstraction."},
    {"name": "OpenAPI Methods", "description": "Endpoints that are interact with both the Pastel RPC API and also the Walletnode API to get information on Sense and Cascade."},
    {"name": "Blockchain Methods", "description": "Endpoints for retrieving blockchain data"},
    {"name": "Mining Methods", "description": "Endpoints for retrieving mining data"},
    {"name": "Ticket Methods", "description": "Endpoints for retrieving blockchain ticket data"},
    {"name": "Supernode Methods", "description": "Endpoints for retrieving Supernode data"},
    {"name": "Network Methods", "description": "Endpoints for retrieving network data"},
    {"name": "Raw Transaction Methods", "description": "Endpoints for working with raw transactions"},
    {"name": "Utility Methods", "description": "Endpoints for various utility functions"},
    {"name": "Control Methods", "description": "Endpoints for various control methods"},
]

class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

# Define the request/response models:

class GetBestBlockHashResponse(BaseModel):
    block_hash: str

class PingResponse(BaseModel):
    success: bool    

class NodeAddressInfo(BaseModel):
    address: str
    connected: str  # 'inbound', 'outbound', or 'false'

class AddedNodeInfo(BaseModel):
    addednode: str
    connected: bool
    addresses: List[NodeAddressInfo]

class GetAddedNodeInfoResponse(BaseModel):
    nodes: List[AddedNodeInfo]
    
class GetConnectionCountResponse(BaseModel):
    connection_count: int

class SendToAddressRequest(BaseModel):
    address: str
    amount: float
    comment: Optional[str] = None
    comment_to: Optional[str] = None    

class PeerInfo(BaseModel):
    id: int
    addr: str
    addrlocal: Optional[str]
    services: str
    lastsend: int
    lastrecv: int
    bytessent: int
    bytesrecv: int
    conntime: int
    timeoffset: int
    pingtime: float
    pingwait: Optional[float]
    version: int
    subver: str
    inbound: bool
    startingheight: int
    banscore: Optional[int]
    synced_headers: Optional[int]
    synced_blocks: Optional[int]
    inflight: Optional[List[int]]
    whitelisted: bool

class GetPeerInfoResponse(BaseModel):
    peers: List[PeerInfo]

class AddNodeRequest(BaseModel):
    node: str
    command: str

class AddNodeResponse(BaseModel):
    result: Optional[str] = None

class DisconnectNodeRequest(BaseModel):
    node: str

class DisconnectNodeResponse(BaseModel):
    status: str

class GetNetTotalsResponse(BaseModel):
    totalbytesrecv: int
    totalbytessent: int
    timemillis: int
    
class NetworkInfo(BaseModel):
    name: str
    limited: bool
    reachable: bool
    proxy: str
    proxy_randomize_credentials: bool

class GetNetworksInfoResponse(BaseModel):
    networks: List[NetworkInfo]
    
class GetDeprecationInfoResponse(BaseModel):
    version: int
    subversion: str
    deprecationheight: int
    
class SetBanRequest(BaseModel):
    ip_subnet: str
    command: str
    bantime: Optional[int] = None
    absolute: Optional[bool] = False

class SetBanResponse(BaseModel):
    result: str = "Success"    

class NetworkInfo(BaseModel):
    name: str
    limited: bool
    reachable: bool
    proxy: str

class LocalAddressInfo(BaseModel):
    address: str
    port: int
    score: int

class GetNetworkInfoResponse(BaseModel):
    version: int
    subversion: str
    protocolversion: int
    localservices: str
    timeoffset: int
    connections: int
    networks: List[NetworkInfo]
    relayfee: float
    localaddresses: List[LocalAddressInfo]
    warnings: str    
    
class BannedAddress(BaseModel):
    address: str
    banned_until: int

class ListBannedResponse(BaseModel):
    banned_addresses: list[BannedAddress]    
    
class GetInfoResponse(BaseModel):
    version: int
    protocolversion: int
    walletversion: Optional[int]
    balance: Optional[float]
    blocks: int
    timeoffset: int
    connections: int
    proxy: Optional[str]
    difficulty: float
    testnet: bool
    keypoololdest: Optional[int]
    keypoolsize: Optional[int]
    unlocked_until: Optional[int]
    paytxfee: Optional[float]
    relayfee: float
    errors: str
    
class ValidateAddressResponse(BaseModel):
    isvalid: bool
    address: Optional[str] = None
    scriptPubKey: Optional[str] = None
    ismine: Optional[bool] = None
    iswatchonly: Optional[bool] = None
    isscript: Optional[bool] = None
    pubkey: Optional[str] = None
    iscompressed: Optional[bool] = None
    account: Optional[str] = None

class ValidateAddressRequest(BaseModel):
    t_address: str

class ZAddressQuery(BaseModel):
    zaddr: str
        
class ZValidateAddressResponse(BaseModel):
    isvalid: bool
    address: Optional[str]
    type: Optional[str]
    ismine: Optional[bool]
    payingkey: Optional[str]
    transmissionkey: Optional[str]
    diversifier: Optional[str]
    diversifiedtransmissionkey: Optional[str]

class CreateMultisigRequest(BaseModel):
    nrequired: int
    keys: List[str]

class CreateMultisigResponse(BaseModel):
    address: str
    redeemScript: str

class VerifyMessageRequest(BaseModel):
    t_address: str
    signature: str
    message: str

class VerifyMessageResponse(BaseModel):
    is_verified: bool

class MempoolDelta(BaseModel):
    address: str
    txid: str
    index: int
    patoshis: int
    timestamp: int
    prevtxid: Optional[str] = None
    prevout: Optional[int] = None

class GetAddressMempoolResponse(BaseModel):
    deltas: List[MempoolDelta]
    
class MemoryInfo(BaseModel):
    used: int
    free: int
    total: int
    locked: int
    chunks_used: int
    chunks_free: int

class GetMemoryInfoResponse(BaseModel):
    locked: MemoryInfo

class ImportPrivKeyResponse(BaseModel):
    address: str
    
class ImportAddressRequest(BaseModel):
    address: str
    label: Optional[str] = ""
    rescan: Optional[bool] = True

class ImportAddressResponse(BaseModel):
    result: Optional[str] = None
    error: Optional[str] = None    
    
class ZImportWalletResponse(BaseModel):
    success: bool
    message: str
        
class ImportWalletResponse(BaseModel):
    message: str
        
class DumpPrivKeyRequest(BaseModel):
    t_addr: str

class DumpPrivKeyResponse(BaseModel):
    key: str        
        
class ExportWalletResponse(BaseModel):
    path: str        
        
class DumpWalletResponse(BaseModel):
    path: str
        
class ZImportKeyResponse(BaseModel):
    type: str
    address: str
    
class ZImportViewingKeyRequest(BaseModel):
    vkey: str
    rescan: Optional[str] = "whenkeyisnew"
    start_height: Optional[int] = 0

class ZImportViewingKeyResponse(BaseModel):
    type: str
    address: str            
        
class ZExportKeyRequest(BaseModel):
    zaddr: str

class ZExportKeyResponse(BaseModel):
    key: str
        
class ZExportViewingKeyResponse(BaseModel):
    viewing_key: str        
        
class GetNetworkSolpsRequest(BaseModel):
    blocks: Optional[int] = 120
    height: Optional[int] = -1

class GetNetworkSolpsResponse(BaseModel):
    solutions_per_second: float
        
class GetLocalSolpsResponse(BaseModel):
    sols_per_second: float        
        
class RefreshMiningMnidInfoResponse(BaseModel):
    mnids: List[str]        
        
class GetGenerateResponse(BaseModel):
    is_generating: bool

class GenerateBlocksRequest(BaseModel):
    num_blocks: int
    pastel_id: Optional[str] = None

class GenerateBlocksResponse(BaseModel):
    block_hashes: List[str]
    
class SetGenerateRequest(BaseModel):
    generate: bool
    genproclimit: Optional[int] = -1

class SetGenerateResponse(BaseModel):
    message: str
    
class PrioritiseTransactionRequest(BaseModel):
    txid: str
    priority_delta: float
    fee_delta: int

class PrioritiseTransactionResponse(BaseModel):
    result: bool

class GetMiningInfoResponse(BaseModel):
    blocks: int
    currentblocksize: int
    currentblocktx: int
    difficulty: float
    errors: str
    generate: bool
    genproclimit: int
    localsolps: float
    networksolps: int
    pooledtx: int
    testnet: bool
    chain: str
    
class GetBlockTemplateRequest(BaseModel):
    jsonrequestobject: Optional[str] = None

class Transaction(BaseModel):
    data: str
    hash: str
    depends: List[int]
    fee: int
    sigops: int
    required: Optional[bool]

class CoinbaseTxn(BaseModel):
    data: str
    hash: str
    depends: List[int]
    fee: int
    sigops: int
    required: bool

class GetBlockTemplateResponse(BaseModel):
    capabilities: List[str]
    version: int
    previousblockhash: str
    finalsaplingroothash: str
    transactions: List[Transaction]
    coinbasetxn: Optional[CoinbaseTxn]
    target: str
    mintime: int
    mutable: List[str]
    noncerange: str
    sigoplimit: int
    sizelimit: int
    curtime: int
    bits: str
    height: int
    masternodeinfo: dict
    governanceinfo: dict    
    
class SubmitBlockRequest(BaseModel):
    hexdata: str
    jsonparametersobject: Optional[dict] = None

class SubmitBlockResponse(BaseModel):
    result: str    
    
class EstimateFeeResponse(BaseModel):
    estimated_fee_per_kb: float
    
class GetBlockSubsidyResponse(BaseModel):
    miner: float
    masternode: float
    governance: float
    
class GetNextBlockSubsidyResponse(BaseModel):
    miner: float
    masternode: float
    governance: Optional[float] = None  # Optional, as it may not always be present

class GenerateReportResponse(BaseModel):
    # Define the fields expected in the response. 
    # This is a placeholder structure, modify it according to the actual response structure of 'generate_report'
    report_data: dict
    
class TicketsGetRequest(BaseModel):
    txid: str
    decode_properties: Optional[bool] = False

class TicketProperty(BaseModel):
    key: str
    value: str

class TicketsGetResponse(BaseModel):
    ticket: Dict[str, Any]  # Replace 'Any' with more specific types if possible
    
class TicketInfo(BaseModel):
    ticket_data: dict

class TicketsFindByLabelResponse(BaseModel):
    tickets: list[TicketInfo]
    
class GetFeeScheduleResponse(BaseModel):
    fee_deflator_factor: float
    pastelid_registration_fee: float
    username_registration_fee: float
    username_change_fee: float    
    
class ChaindataStoreRequest(BaseModel):
    data: str

class ChaindataStoreResponse(BaseModel):
    txid: str
    rawtx: str

class ChaindataRetrieveRequest(BaseModel):
    txid: str

class ChaindataRetrieveResponse(BaseModel):
    data: str

class TicketsResponse(BaseModel):
    result: str  # Assuming the result is a string; adjust the type based on actual response
    
class GetBlockCountResponse(BaseModel):
    block_count: int
    
class GetDifficultyResponse(BaseModel):
    difficulty: float

class GetRawMemPoolResponse(BaseModel):
    transaction_ids: List[str] = Field(..., example=["txid1", "txid2", "txid3"])

class VerboseMemPoolTransaction(BaseModel):
    size: int
    fee: float
    time: int
    height: int
    startingpriority: float
    currentpriority: float
    depends: List[str]

class GetRawMemPoolVerboseResponse(BaseModel):
    transactions: Dict[str, VerboseMemPoolTransaction]    
    
class GetBlockHeaderResponseVerbose(BaseModel):
    hash: str
    confirmations: int
    height: int
    version: int
    merkleroot: str
    finalsaplingroot: str
    time: int
    nonce: int
    bits: str
    difficulty: float
    previousblockhash: str
    nextblockhash: str
    pastelid: Optional[str]
    prevMerkleRootSignature: Optional[str]

class GetBlockHeaderResponseNonVerbose(BaseModel):
    data: str
    
class GetBlockHashRequest(BaseModel):
    index: int

class GetBlockHashResponse(BaseModel):
    hash: str        
    
# Response models for different verbosity levels
class TransactionID(BaseModel):
    transactionid: str

class BlockResponseVerbosity0(BaseModel):
    data: str

class BlockResponseVerbosity1(BaseModel):
    hash: str
    confirmations: int
    size: int
    height: int
    version: int
    merkleroot: str
    finalsaplingroot: Optional[str]
    pastelid: Optional[str]
    prevMerkleRootSignature: Optional[str]
    tx: List[TransactionID]
    time: int
    nonce: int
    bits: str
    difficulty: float
    previousblockhash: Optional[str]
    nextblockhash: Optional[str]

class ScriptSig(BaseModel):
    asm: str
    hex: str

class Vin(BaseModel):
    txid: str
    vout: int
    scriptSig: ScriptSig
    sequence: int

class ScriptPubKey(BaseModel):
    asm: str
    hex: str
    reqSigs: Optional[int]
    type: str
    addresses: List[str]

class Vout(BaseModel):
    value: float
    n: int
    scriptPubKey: ScriptPubKey

class TransactionDetail(BaseModel):
    in_active_chain: Optional[bool]
    hex: str = Field(..., description="The serialized, hex-encoded data for txid")
    txid: str = Field(..., description="The transaction id")
    version: int = Field(..., description="The version")
    locktime: int = Field(..., description="The lock time")
    expiryheight: Optional[int] = Field(None, description="The block height after which the transaction expires")
    vin: List[Vin] = Field(..., description="List of transaction inputs")
    vout: List[Vout] = Field(..., description="List of transaction outputs")
    blockhash: Optional[str] = Field(None, description="The block hash")
    confirmations: Optional[int] = Field(None, description="The number of confirmations")
    time: Optional[int] = Field(None, description="The transaction time in seconds since epoch (Jan 1 1970 GMT)")
    blocktime: Optional[int] = Field(None, description="The block time in seconds since epoch (Jan 1 1970 GMT)")


class BlockResponseVerbosity2(BlockResponseVerbosity1):
    tx: List[TransactionDetail]  # Override with detailed transaction information

# Combined response model to handle all verbosity levels
class GetBlockResponse(BaseModel):
    response: Union[BlockResponseVerbosity0, BlockResponseVerbosity1, BlockResponseVerbosity2]
    
class GetTxOutSetInfoResponse(BaseModel):
    height: int
    bestblock: str
    transactions: int
    txouts: int
    bytes_serialized: int
    hash_serialized: str
    total_amount: float
    
class GetTxOutResponse(BaseModel):
    bestblock: str
    confirmations: int
    value: float
    valuePat: int
    scriptPubKey: dict
    version: int
    coinbase: bool  
    
class VerifyChainRequest(BaseModel):
    checklevel: Optional[int] = 3
    numblocks: Optional[int] = 288

class VerifyChainResponse(BaseModel):
    verified: bool
      
class ChainTip(BaseModel):
    height: int
    hash: str
    branchlen: int
    status: str

class GetChainTipsResponse(BaseModel):
    tips: List[ChainTip]

class GetMempoolInfoResponse(BaseModel):
    size: int
    bytes: int
    usage: int
    
class SoftFork(BaseModel):
    id: str
    version: int
    enforce: dict
    reject: dict

class Upgrade(BaseModel):
    name: str
    activationheight: int
    status: str
    info: str

class Consensus(BaseModel):
    chaintip: str
    nextblock: str

class BlockchainInfoResponse(BaseModel):
    chain: str
    blocks: int
    headers: int
    bestblockhash: str
    difficulty: float
    verificationprogress: float
    chainwork: str
    commitments: int
    softforks: list[SoftFork]
    upgrades: dict[str, Upgrade]
    consensus: Consensus
    pruned: Optional[bool]
    pruneheight: Optional[int]
    
class ReconsiderBlockRequest(BaseModel):
    hash: str

class ReconsiderBlockResponse(BaseModel):
    success: bool
    message: str    
    
class InvalidateBlockResponse(BaseModel):
    success: bool
    message: Optional[str]
    
class InputDetail(BaseModel):
    address: str
    patoshis: int
    index: int
    prevtxid: str
    prevout: int

class OutputDetail(BaseModel):
    address: str
    patoshis: int
    index: int

class DeltaDetail(BaseModel):
    txid: str
    index: int
    inputs: list[InputDetail]
    outputs: list[OutputDetail]

class GetBlockDeltasResponse(BaseModel):
    hash: str
    confirmations: int
    size: int
    height: int
    version: int
    merkleroot: str
    deltas: list[DeltaDetail]
    time: int
    mediantime: int
    nonce: str
    bits: str
    difficulty: float
    chainwork: str
    previousblockhash: Optional[str]
    nextblockhash: Optional[str]
    
class GetRawTransactionRequest(BaseModel):
    txid: str
    verbose: Optional[int] = 0
    blockhash: Optional[str] = None

class GetRawTransactionResponse(BaseModel):
    in_active_chain: Optional[bool]
    hex: str
    txid: str
    version: int
    locktime: int
    expiryheight: Optional[int]
    vin: List[Vin]
    vout: List[Vout]
    blockhash: Optional[str]
    confirmations: int
    time: int
    blocktime: int
    
class GetTxOutProofResponse(BaseModel):
    data: str        
    
class TransactionInput(BaseModel):
    txid: str
    vout: int
    sequence: Optional[int] = None

class AddressAmount(BaseModel):
    address: str
    amount: float

class CreateRawTransactionRequest(BaseModel):
    transactions: List[TransactionInput]
    addresses: Dict[str, float]
    locktime: Optional[int] = 0
    expiryheight: Optional[int] = None

class CreateRawTransactionResponse(BaseModel):
    transaction: str
    
class DecodeRawTransactionResponse(BaseModel):
    txid: str
    size: int
    overwintered: bool
    version: int
    versiongroupid: Optional[str] = None
    locktime: int
    expiryheight: Optional[int] = None
    vin: List[Vin]
    vout: List[Vout]

class DecodeRawTransactionRequest(BaseModel):
    hexstring: str    
    
class DecodeScriptResponse(BaseModel):
    asm: str
    hex: str
    type: str
    reqSigs: int
    addresses: List[str]
    p2sh: str

class DecodeScriptRequest(BaseModel):
    hex: str
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
        
@router.get("/getbestblockhash",
            response_model=GetBestBlockHashResponse,
            tags=["Blockchain Methods"],
            summary="Get the hash of the best block",
            description="""Get the hash of the best (tip) block in the longest blockchain. 

### Description
- This endpoint returns the hash of the latest block added to the Pastel blockchain, representing the most current and up-to-date state of the network.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getbestblockhash`

### Response
- Returns a JSON object containing the hash of the best block in hexadecimal format.

### Example Response
```json
{
    "block_hash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Primarily used by blockchain explorers and wallets to identify the current end of the blockchain.""",
            response_description="Hex-encoded hash of the best block")
async def get_best_block_hash(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    block_hash = await rpc_connection.getbestblockhash()
    return GetBestBlockHashResponse(block_hash=block_hash)



@router.get("/ping",
            response_model=PingResponse,
            tags=["Utility Methods"],
            summary="Send a ping to all nodes",
            description="""Request a ping to be sent to all other nodes, measuring ping time.

### Description
- This endpoint triggers a ping to all nodes in the network. It's used to measure the ping time and network responsiveness.
- The ping time and wait time results are available in the `getpeerinfo` response, under `pingtime` and `pingwait` fields, represented in decimal seconds.
- The ping command is queued with other commands, so it measures the total processing backlog, not just the network latency.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /ping`

### Response
- Returns a JSON object indicating whether the ping request was successfully queued.

### Example Response
```json
{
    "success": true
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for network diagnostics and monitoring the responsiveness of the network.""",
            response_description="Indicates whether the ping request was successful")
async def ping(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    try:
        await rpc_connection.ping()
        return PingResponse(success=True)
    except Exception as e:
        logger.error(f"Ping request failed: {e}")
        return PingResponse(success=False)
    
    

@router.get("/getaddednodeinfo",
            response_model=GetAddedNodeInfoResponse,
            tags=["Network Methods"],
            summary="Get information about added nodes",
            description="""Get information about the given added node or all added nodes.

### Description
- This endpoint returns information about nodes that have been added using the `addnode` RPC command. 
- It can return information about all added nodes or a specific node, if specified.

### Input Parameters
- `dns`: A boolean value indicating whether detailed information is required.
- `node`: (Optional) The specific node to get information about.

### Example Request
- `GET /getaddednodeinfo?dns=true&node=192.168.0.201`

### Response
- Returns a JSON object containing information about added nodes.

### Example Response
```json
{
    "nodes": [
        {
            "addednode": "192.168.0.201",
            "connected": true,
            "addresses": [
                {
                    "address": "192.168.0.201:9933",
                    "connected": "outbound"
                }
            ]
        }
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Information about added nodes")
async def get_added_node_info(dns: bool, node: Optional[str] = None, 
                              rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getaddednodeinfo(dns, node)
    return GetAddedNodeInfoResponse(nodes=response)


@router.get("/getconnectioncount",
            response_model=GetConnectionCountResponse,
            tags=["Network Methods"],
            summary="Get the number of connections to other nodes",
            description="""Get the number of connections to other nodes in the Pastel network.

### Description
- This endpoint returns the total number of connections that the node has to other nodes in the network. It's an indicator of the node's connectivity and participation in the network.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getconnectioncount`

### Response
- Returns a JSON object containing the total number of connections.

### Example Response
```json
{
    "connection_count": 15
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for network diagnostics and monitoring the node's network activity.""",
            response_description="The total number of connections to other nodes")
async def get_connection_count(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    connection_count = await rpc_connection.getconnectioncount()
    return GetConnectionCountResponse(connection_count=connection_count)



@router.get("/getpeerinfo",
            response_model=GetPeerInfoResponse,
            tags=["Network Methods"],
            summary="Get data about each connected network node",
            description="""Get data about each connected network node as a json array of objects.

### Description
- This endpoint returns detailed information about each peer connected to the Pastel network.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getpeerinfo`

### Response
- Returns a JSON array containing information about each connected network node.

### Example Response
```json
{
    "peers": [
        {
            "id": 1,
            "addr": "host:port",
            "addrlocal": "ip:port",
            "services": "xxxxxxxxxxxxxxxx",
            "lastsend": 1617704837,
            "lastrecv": 1617704837,
            ...
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for network diagnostics and analysis.""",
            response_description="Information about each connected network node")
async def get_peer_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    peer_info_data = await rpc_connection.getpeerinfo()
    return GetPeerInfoResponse(peers=peer_info_data)



@router.post("/addnode",
            response_model=AddNodeResponse,
            tags=["Network Methods"],
            summary="Add, remove, or try a connection to a node",
            description="""Attempt to add or remove a node from the addnode list, or try a connection to a node once.

### Description
- This endpoint manages nodes in the addnode list. It can add a node to the list, remove a node from the list, or try a connection to a node once.
- The 'node' parameter specifies the node (IP address and port), and the 'command' parameter specifies the action to be taken ('add', 'remove', or 'onetry').

### Input Parameters
- `node` (string, required): The node's address in the format `IP:port`.
- `command` (string, required): The command to execute, which can be 'add', 'remove', or 'onetry'.

### Example Request
```json
{
    "node": "192.168.0.6:9933",
    "command": "onetry"
}
```

### Response
- Returns a success message or null if the command is executed successfully.

### Example Response
```json
{
    "result": "Node added successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this method cautiously as it can modify the node's peer connections.""",
            response_description="Result of the addnode command")
async def add_node(request: AddNodeRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.addnode(request.node, request.command)
    return AddNodeResponse(result=result)




@router.post("/disconnectnode",
             response_model=DisconnectNodeResponse,
             tags=["Control Methods"],
             summary="Disconnect from a specified node",
             description="""Disconnect immediately from a specified node in the Pastel network.

### Description
- This endpoint allows for immediate disconnection from a specified node. It's useful for network management and control.

### Input Parameters
- `node`: The IP address and port of the node to disconnect from, in the format "IP:PORT".

### Example Request
```json
{
    "node": "192.168.0.6:9933"
}
```

### Response
- Returns a JSON object indicating the status of the disconnection.

### Example Response
```json
{
    "status": "Node disconnected successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this endpoint with caution as it modifies the network connections of the Pastel node.""",
             response_description="Status of the disconnection operation")
async def disconnect_node(request: DisconnectNodeRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.disconnectnode(request.node)
    return DisconnectNodeResponse(status="Node disconnected successfully")



@router.get("/getnettotals",
            response_model=GetNetTotalsResponse,
            tags=["Network Methods"],
            summary="Get network traffic information",
            description="""Get information about network traffic, including total bytes received, total bytes sent, and current time.

### Description
- This endpoint returns statistics about the network traffic, including the total number of bytes received and sent by the node since startup, as well as the current time in milliseconds.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getnettotals`

### Response
- Returns a JSON object containing the network traffic statistics.

### Example Response
```json
{
    "totalbytesrecv": 123456,
    "totalbytessent": 654321,
    "timemillis": 1627891234567
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for monitoring and diagnostics of the node's network activity.""",
            response_description="Network traffic statistics")
async def get_net_totals(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    net_totals = await rpc_connection.getnettotals()
    return GetNetTotalsResponse(**net_totals)



@router.get("/getnetworksinfo",
            response_model=GetNetworksInfoResponse,
            tags=["Network Methods"],
            summary="Get information about all the networks",
            description="""Get detailed information about all the networks known to the node.

### Description
- This endpoint provides information about each network that the node is aware of. It includes details like the network's name, its accessibility status, and any associated proxy settings.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getnetworksinfo`

### Response
- Returns a JSON array of objects, each representing a network with its specific details.

### Example Response
```json
{
    "networks": [
        {
            "name": "ipv4",
            "limited": false,
            "reachable": true,
            "proxy": "192.168.1.1:9050",
            "proxy_randomize_credentials": true
        },
        {
            "name": "ipv6",
            "limited": false,
            "reachable": true,
            "proxy": "",
            "proxy_randomize_credentials": false
        }
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for network diagnostics and for understanding the node's perspective of the network topology.""",
            response_description="Details about each network known to the node")
async def get_networks_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    networks = await rpc_connection.getnetworksinfo()
    return GetNetworksInfoResponse(networks=networks)



@router.get("/getdeprecationinfo",
            response_model=GetDeprecationInfoResponse,
            tags=["Control Methods"],
            summary="Get deprecation information of the current version",
            description="""Get information about the deprecation of the current server version. 

### Description
- This endpoint returns an object containing details about the current server version, its subversion, and the block height at which this version will deprecate and shut down. This endpoint is applicable only on mainnet.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getdeprecationinfo`

### Response
- Returns a JSON object containing the server version, subversion, and deprecation block height.

### Example Response
```json
{
    "version": 5000500,
    "subversion": "/MagicBean:5.0.5[-v]/",
    "deprecationheight": 100000
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is typically used for software maintenance and upgrade planning.""",
            response_description="Information about the deprecation of the current server version")
async def get_deprecation_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    deprecation_info = await rpc_connection.getdeprecationinfo()
    return GetDeprecationInfoResponse(**deprecation_info)



@router.get("/getnetworkinfo",
            response_model=GetNetworkInfoResponse,
            tags=["Network Methods"],
            summary="Get various state info regarding P2P networking",
            description="""Get an object containing various state information regarding P2P networking.

### Description
- This endpoint returns an object containing various state information regarding the P2P networking of the Pastel node.
- It provides details like server version, protocol version, connections, and network information.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getnetworkinfo`

### Response
- Returns a JSON object containing various state info regarding P2P networking.

### Example Response
```json
{
    "version": 5000000,
    "subversion": "/MagicBean:5.0.0[-v]/",
    "protocolversion": 170013,
    "localservices": "000000000000040d",
    "timeoffset": 0,
    "connections": 10,
    "networks": [
        {
            "name": "ipv4",
            "limited": false,
            "reachable": true,
            "proxy": ""
        }
    ],
    "relayfee": 0.00001000,
    "localaddresses": [
        {
            "address": "123.45.67.89",
            "port": 8333,
            "score": 1
        }
    ],
    "warnings": ""
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Various state info regarding P2P networking")
async def get_network_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getnetworkinfo()
    return response




@router.post("/setban", 
             response_model=SetBanResponse, 
             tags=["Control Methods"],
             summary="Add or Remove an IP/Subnet from the Ban List",
             description="""Add or remove an IP/Subnet from the banned list.

### Description
- This endpoint attempts to add or remove an IP/Subnet from the banned list of the node.

### Input Parameters
- `ip_subnet`: The IP/Subnet with an optional netmask (default is /32 = single IP).
- `command`: 'add' to add to the list, 'remove' to remove from the list.
- `bantime`: (Optional) Time in seconds for how long the IP is banned. 0 or empty uses the default time of 24 hours.
- `absolute`: (Optional) If true, `bantime` is an absolute timestamp since epoch (Jan 1 1970 GMT).

### Example Request
```json
{
    "ip_subnet": "192.168.0.6",
    "command": "add",
    "bantime": 86400,
    "absolute": false
}
```

### Response
- Returns a success message upon successful addition or removal.

### Example Response
```json
{
    "result": "Success"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this endpoint with caution as it affects the node's network connections.""",
             response_description="Result of the setban operation")
async def set_ban(request: SetBanRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Convert request to the format expected by the RPC method
    params = [request.ip_subnet, request.command]
    if request.bantime is not None:
        params.append(request.bantime)
    if request.absolute:
        params.append(request.absolute)
    # Call the RPC method
    await rpc_connection.setban(*params)
    return SetBanResponse()



@router.get("/listbanned",
            response_model=ListBannedResponse,
            tags=["Network Methods"],
            summary="List all banned IPs/Subnets",
            description="""List all banned IPs/Subnets in the network.

### Description
- This endpoint retrieves a list of all IP addresses and subnets that have been banned from the network.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /listbanned`

### Response
- Returns a JSON array of objects, each containing the banned address and the timestamp until which it is banned.

### Example Response
```json
{
    "banned_addresses": [
        {
            "address": "192.168.1.0/24",
            "banned_until": 1625097600
        },
        {
            "address": "10.0.0.5",
            "banned_until": 1625098000
        }
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for network administrators and developers to audit and manage network access.""",
            response_description="List of banned IP addresses and subnets")
async def list_banned(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    banned_data = await rpc_connection.listbanned()
    return ListBannedResponse(banned_addresses=banned_data)



@router.get("/getinfo",
            response_model=GetInfoResponse,
            tags=["Control Methods"],
            summary="Get various state info",
            description="""Get an object containing various state info about the Pastel server.

### Description
- This endpoint provides information about the server's state, including wallet balance, block count, connections, and other relevant details.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getinfo`

### Response
- Returns a JSON object containing various state information of the server.

### Example Response
```json
{
  "version": 50000,
  "protocolversion": 70015,
  "walletversion": 60000,
  "balance": 15.0,
  "blocks": 120987,
  "timeoffset": 0,
  "connections": 8,
  "proxy": "127.0.0.1:9050",
  "difficulty": 1.23456789,
  "testnet": false,
  "keypoololdest": 1577836800,
  "keypoolsize": 1000,
  "unlocked_until": 1596240000,
  "paytxfee": 0.0001,
  "relayfee": 0.00001,
  "errors": "Warning: unknown new rules activated (versionbit 28)"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for getting a quick overview of the state of the server and its wallet.""",
            response_description="Various state information of the Pastel server")
async def get_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    info = await rpc_connection.getinfo()
    return GetInfoResponse(**info)



@router.post("/validateaddress",
             response_model=ValidateAddressResponse,
             tags=["Utility Methods"],
             summary="Validate a Pastel address",
             description="""Validate a given Pastel transparent address.

### Description
- This endpoint validates a specified Pastel transparent address and returns detailed information about it.

### Input Parameters
- `t_address`: The Pastel transparent address to validate.

### Example Request
```json
{
    "t_address": "1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc"
}
```

### Response
- Returns a JSON object containing various details about the address if it is valid. If the address is not valid, only the `isvalid` field is returned.

### Example Response
```json
{
    "isvalid": true,
    "address": "1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc",
    "scriptPubKey": "76a914...",
    "ismine": true,
    "iswatchonly": false,
    "isscript": false,
    "pubkey": "02...",
    "iscompressed": true,
    "account": ""
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Provides detailed information about a Pastel address, including ownership and script information.""",
             response_description="Details about the validated Pastel address")
async def validate_address(request: ValidateAddressRequest,
                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.validateaddress(request.t_address)
    return ValidateAddressResponse(**response)




@router.get("/z_validateaddress",
            response_model=ZValidateAddressResponse,
            tags=["Utility Methods"],
            summary="Validate a Z address",
            description="""Validate the given Z address and return information about it.

### Description
- This endpoint validates a Z address and returns various details about it, including its validity, type, and ownership.

### Input Parameters
- `zaddr`: The Z address to validate.

### Example Request
- `GET /z_validateaddress?zaddr=PzWcy67ygestjagHaFZxjWxmawMeShmQWNPE8FNJp23pQS2twecwps5223ajUtN7iihxR4MmLDFQ19heHkBx5AKaDooS6aQ`

### Response
- Returns a JSON object with information about the Z address.

### Example Response
```json
{
    "isvalid": true,
    "address": "PzWcy67y...",
    "type": "sapling",
    "ismine": false,
    ...
}
```

### Possible Errors
- HTTP 400: Bad Request if the address format is incorrect.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is used to verify the details and ownership of a Z address.""",
            response_description="Information about the Z address")
async def z_validate_address(query: ZAddressQuery, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.z_validateaddress(query.zaddr)
    return ZValidateAddressResponse(**result)



@router.post("/createmultisig",
            response_model=CreateMultisigResponse,
            tags=["Utility Methods"],
            summary="Create a multisig address",
            description="""Creates a multi-signature address with n signatures of m keys required.

### Description
- This endpoint creates a multi-signature address requiring a specified number of signatures from a set of provided keys.
- It returns the new multisig address and the hex-encoded redemption script.

### Input Parameters
- `nrequired`: The number of required signatures out of the n keys or addresses.
- `keys`: A list of Pastel addresses or hex-encoded public keys.

### Example Request
- `POST /createmultisig`
```json
{
    "nrequired": 2,
    "keys": ["Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY", "Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY"]
}
```

### Response
- Returns a JSON object containing the multisig address and the hex-encoded redemption script.

### Example Response
```json
{
    "address": "multisigaddress",
    "redeemScript": "script"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="The new multisig address and redemption script")
async def create_multisig(request: CreateMultisigRequest, 
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.createmultisig(request.nrequired, request.keys)
    return CreateMultisigResponse(address=result['address'], redeemScript=result['redeemScript'])




@router.post("/verifymessage",
             response_model=VerifyMessageResponse,
             tags=["Utility Methods"],
             summary="Verify a signed message",
             description="""Verify a signed message using a Pastel transparent address, a signature, and the message itself.

### Description
- Verifies a message signature against a given Pastel transparent address.

### Input Parameters
- `t_address`: The Pastel transparent address used for the signature.
- `signature`: The signature provided by the signer in base 64 encoding.
- `message`: The message that was signed.

### Example Request
```json
{
    "t_address": "Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY",
    "signature": "signature_in_base64",
    "message": "my message"
}
```

### Response
- Returns a boolean indicating if the signature is verified.

### Example Response
```json
{
    "is_verified": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the inputs are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for validating the authenticity of messages signed with a Pastel address.""",
             response_description="Result of the signature verification")
async def verify_message(request: VerifyMessageRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    is_verified = await rpc_connection.verifymessage(request.t_address, request.signature, request.message)
    return VerifyMessageResponse(is_verified=is_verified)



@router.get("/getaddressmempool",
            response_model=GetAddressMempoolResponse,
            tags=["Address Index Methods"],
            summary="Get all mempool deltas for an address",
            description="""Retrieve all mempool deltas for a specified address.

### Description
- This endpoint returns all mempool deltas (transaction differences) for a given address.
- It's useful for tracking the unconfirmed transactions involving a specific address.

### Input Parameters
- `addresses`: A list of base58check encoded addresses.

### Example Request
- `GET /getaddressmempool?addresses=["tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp"]`

### Response
- Returns a JSON array of objects, each representing a mempool delta for the given address(es).

### Example Response
```json
[
    {
        "address": "tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp",
        "txid": "txid123",
        "index": 1,
        "patoshis": 5000000,
        "timestamp": 1617184000,
        "prevtxid": "txid456",
        "prevout": 0
    }
]
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="List of mempool deltas for the specified address(es)")
async def get_address_mempool(addresses: List[str], 
                              rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getaddressmempool({"addresses": addresses})
    return GetAddressMempoolResponse(deltas=response)




@router.get("/getmemoryinfo",
            response_model=GetMemoryInfoResponse,
            tags=["Utility Methods"],
            summary="Get memory usage information",
            description="""Get detailed information about memory usage by the Pastel node. 

### Description
- This endpoint returns information about the memory usage, including details about used and free memory, total memory managed, amount of memory locked, and the number of chunks used and free.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getmemoryinfo`

### Response
- Returns a JSON object containing detailed memory usage information.

### Example Response
```json
{
    "locked": {
        "used": 123456,
        "free": 654321,
        "total": 1000000,
        "locked": 500000,
        "chunks_used": 20,
        "chunks_free": 80
    }
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for monitoring the memory performance and health of the Pastel node.""",
            response_description="Detailed memory usage information")
async def get_memory_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    memory_info = await rpc_connection.getmemoryinfo()
    return GetMemoryInfoResponse(**memory_info)



@router.post("/importprivkey",
             response_model=ImportPrivKeyResponse,
             tags=["Wallet Methods"],
             summary="Import a private key",
             description="""Import a private key into the wallet.

### Description
- Adds a Zcash-format private key to your wallet, allowing the wallet to use funds associated with the key's address.

### Input Parameters
- `zcashprivkey`: The Zcash private key to be imported (required).
- `label`: An optional label for the address (optional, default empty string).
- `rescan`: A boolean indicating whether the wallet should be rescanned for transactions after importing the key (optional, default true).

### Example Request
```json
{
    "zcashprivkey": "mykey",
    "label": "testing",
    "rescan": false
}
```

### Response
- Returns the address associated with the imported private key.

### Example Response
```json
{
    "address": "t1XYZabc123..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Importing a private key can take minutes if rescan is true.""",
             response_description="Address associated with the imported private key")
async def import_priv_key(zcashprivkey: str, label: Optional[str] = "", rescan: bool = True, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    address = await rpc_connection.importprivkey(zcashprivkey, label, rescan)
    return ImportPrivKeyResponse(address=address)



@router.post("/importaddress",
             response_model=ImportAddressResponse,
             tags=["Wallet Methods"],
             summary="Import an address",
             description="""Import an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend.

### Description
- This endpoint adds an address or script to your wallet as a watch-only address. This means you can see incoming transactions to it, but not spend its funds.
- The `rescan` option will rescan the wallet for transactions, but this can be time-consuming.

### Input Parameters
- `address`: The address to import.
- `label`: An optional label for the address.
- `rescan`: A boolean indicating whether to rescan the wallet for transactions. Default is true.

### Example Request
```json
{
    "address": "myaddress",
    "label": "testing",
    "rescan": false
}
```

### Response
- Returns `null` on successful addition of the address. In case of an error, an error message is returned.

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this endpoint with caution as rescanning can take a considerable amount of time.""",
             response_description="Result of the address import")
async def import_address(request: ImportAddressRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.importaddress(request.address, request.label, request.rescan)
    return ImportAddressResponse(result=result)




@router.post("/z_importwallet",
             response_model=ZImportWalletResponse,
             tags=["Utility Methods"],
             summary="Import keys from a wallet export file",
             description="""Imports taddr and zaddr keys from a wallet export file. This is typically used after using `z_exportwallet`.

### Description
- Allows for the importation of taddr and zaddr keys from a previously exported wallet file.

### Input Parameters
- `filename`: The path to the wallet file that needs to be imported.

### Example Request
- `POST /z_importwallet` with payload:
```json
{
    "filename": "path/to/exportdir/nameofbackup"
}
```

### Response
- Returns a JSON object indicating the success or failure of the import operation.

### Example Response
```json
{
    "success": true,
    "message": "Wallet imported successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the filename parameter is missing or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Ensure the path to the wallet file is correct and accessible.""",
             response_description="Status of the import wallet operation")
async def z_import_wallet(filename: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.z_importwallet(filename)
    return ZImportWalletResponse(success=True, message="Wallet imported successfully")




@router.post("/importwallet",
             response_model=ImportWalletResponse,
             tags=["Wallet Methods"],
             summary="Import a wallet from a dump file",
             description="""Import taddr keys from a wallet dump file.

### Description
- This endpoint imports taddr keys from a specified wallet dump file. This is useful for restoring a wallet from a backup.

### Input Parameters
- `filename`: The path to the wallet dump file to be imported.

### Example Request
```json
{
    "filename": "path/to/exportdir/nameofbackup"
}
```

### Response
- Returns a confirmation message upon successful import.

### Example Response
```json
{
    "message": "Wallet imported successfully"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Ensure that the wallet dump file exists at the specified path before calling this endpoint.""",
             response_description="Confirmation of wallet import")
async def import_wallet(filename: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.importwallet(filename)
    return ImportWalletResponse(message="Wallet imported successfully")



@router.get("/dumpprivkey",
            response_model=DumpPrivKeyResponse,
            tags=["Utility Methods"],
            summary="Reveal the private key for a given address",
            description="""Reveals the private key corresponding to the specified transparent address.

### Description
- This endpoint is used to retrieve the private key associated with a given transparent address. 
- It's important to handle the output with care as the private key controls access to the assets held in the address.

### Input Parameters
- `t_addr`: The transparent address for which the private key is to be revealed.

### Example Request
- `GET /dumpprivkey?t_addr=myaddress`

### Response
- Returns a JSON object containing the private key in a string format.

### Example Response
```json
{
    "key": "5J1m2B2K5m3..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the address is invalid or not specified.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The output should be kept secure as it provides complete control over the assets in the address.""",
            response_description="The private key associated with the given address")
async def dump_priv_key(request: DumpPrivKeyRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    key = await rpc_connection.dumpprivkey(request.t_addr)
    return DumpPrivKeyResponse(key=key)



@router.post("/z_exportwallet",
             response_model=ExportWalletResponse,
             tags=["Wallet Methods"],
             summary="Export wallet keys",
             description="""Export all wallet keys, for taddr and zaddr, in a human-readable format.

### Description
- Exports all wallet keys, including both transparent (taddr) and shielded (zaddr) addresses, to a specified file. Overwriting an existing file is not permitted.

### Input Parameters
- `filename`: A string representing the filename to which the wallet keys will be exported. The file will be saved in the folder set by the `pasteld -exportdir` option.

### Example Request
```json
{
    "filename": "my_wallet_export"
}
```

### Response
- Returns a JSON object containing the full path of the destination file where the wallet keys are exported.

### Example Response
```json
{
    "path": "/path/to/exported/file/my_wallet_export"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.

### Note
- Use this endpoint to backup wallet keys securely.""",
             response_description="Path of the exported wallet file")
async def z_export_wallet(filename: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    export_path = await rpc_connection.z_exportwallet(filename)
    return ExportWalletResponse(path=export_path)



@router.post("/dumpwallet",
             response_model=DumpWalletResponse,
             tags=["Wallet Methods"],
             summary="Dump wallet keys",
             description="""Dumps taddr wallet keys in a human-readable format.

### Description
- Dumps transparent address (taddr) wallet keys to a specified file. Overwriting an existing file is not permitted.

### Input Parameters
- `filename`: A string representing the filename to which the wallet keys will be dumped. The file will be saved in the folder set by the `pasteld -exportdir` option.

### Example Request
```json
{
    "filename": "my_wallet_dump"
}
```

### Response
- Returns a JSON object containing the full path of the destination file where the wallet keys are dumped.

### Example Response
```json
{
    "path": "/path/to/dumped/file/my_wallet_dump"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.

### Note
- Use this endpoint for transparent address wallet key backups.""",
             response_description="Path of the dumped wallet file")
async def dump_wallet(filename: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    dump_path = await rpc_connection.dumpwallet(filename)
    return DumpWalletResponse(path=dump_path)



@router.get("/z_importkey",
            response_model=ZImportKeyResponse,
            tags=["Wallet Methods"],
            summary="Import a Z key into the wallet",
            description="""Imports a Z key (as returned by z_exportkey) to your wallet.

### Description
- Adds a Z key to your wallet and optionally rescans the wallet for transactions.

### Input Parameters
- `zkey`: The Z key to be imported (required).
- `rescan`: Option to rescan the wallet for transactions - can be "yes", "no", or "whenkeyisnew" (optional, default="whenkeyisnew").
- `start_height`: Block height to start rescan from (optional, default=0).

### Example Request
- `GET /z_importkey?zkey=mykey&rescan=yes&start_height=30000`

### Response
- Returns a JSON object containing the type and address corresponding to the imported spending key.

### Example Response
```json
{
    "type": "sapling",
    "address": "ps1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

### Possible Errors
- HTTP 400: Bad Request if input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Importing a key can take minutes to complete if rescan is true. The call will block until the rescan is complete.""",
            response_description="Information about the imported Z key")
async def z_import_key(zkey: str, rescan: Optional[str] = "whenkeyisnew", start_height: Optional[int] = 0, 
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.z_importkey(zkey, rescan, start_height)
    return ZImportKeyResponse(type=response["type"], address=response["address"])



@router.post("/z_importviewingkey",
             response_model=ZImportViewingKeyResponse,
             tags=["Utility Methods"],
             summary="Import a viewing key into the wallet",
             description="""Import a viewing key into your wallet.

### Description
- This endpoint adds a viewing key (as returned by z_exportviewingkey) to your wallet. It allows you to track transactions associated with the viewing key's address.

### Input Parameters
- `vkey`: The viewing key to be imported.
- `rescan`: Rescan option for the wallet transactions. Can be "yes", "no", or "whenkeyisnew".
- `start_height`: The block height from which to start the rescan.

### Example Request
- `POST /z_importviewingkey` with JSON body:
```json
{
    "vkey": "your_viewing_key",
    "rescan": "yes",
    "start_height": 30000
}
```

### Response
- Returns a JSON object containing the type and address corresponding to the imported viewing key.

### Example Response
```json
{
    "type": "sapling",
    "address": "pastel_address"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- Specific errors for invalid viewing key or if the key already exists in the wallet.""",
             response_description="Details of the imported viewing key")
async def z_import_viewing_key(request: ZImportViewingKeyRequest,
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.z_importviewingkey(request.vkey, request.rescan, request.start_height)
    return ZImportViewingKeyResponse(type=result["type"], address=result["address"])



@router.post("/z_exportkey",
             response_model=ZExportKeyResponse,
             tags=["Utility Methods"],
             summary="Reveal the private key corresponding to a z-address",
             description="""Reveals the private key corresponding to the specified z-address.

### Description
- This endpoint is used to extract the private key associated with a given z-address.
- The private key can then be used for various purposes, including wallet backup and migration.

### Input Parameters
- `zaddr`: A string representing the z-address for which the private key is required.

### Example Request
- `POST /z_exportkey`
  ```json
  {
      "zaddr": "myzaddress"
  }
  ```

### Response
- Returns a JSON object containing the private key associated with the specified z-address.

### Example Response
```json
{
    "key": "5Jxxxxx..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the z-address is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this endpoint cautiously as exposing private keys can lead to security risks.""",
             response_description="The private key corresponding to the provided z-address")
async def z_export_key(request: ZExportKeyRequest, 
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    key = await rpc_connection.z_exportkey(request.zaddr)
    return ZExportKeyResponse(key=key)



@router.get("/z_exportviewingkey",
            response_model=ZExportViewingKeyResponse,
            tags=["Utility Methods"],
            summary="Export the viewing key for a Z-address",
            description="""Export the viewing key for a specified Z-address (zaddr).

### Description
- This endpoint reveals the viewing key corresponding to a given Z-address. 
- The key can then be used with the `z_importviewingkey` method.

### Input Parameters
- `zaddr`: A string representing the Z-address for which the viewing key is requested.

### Example Request
- `GET /z_exportviewingkey?zaddr=myaddress`

### Response
- Returns a JSON object containing the viewing key for the specified Z-address.

### Example Response
```json
{
    "viewing_key": "Zivk..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the Z-address is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The returned viewing key allows viewing the transaction details associated with the Z-address.""",
            response_description="Viewing key for the specified Z-address")
async def z_export_viewing_key(zaddr: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    viewing_key = await rpc_connection.z_exportviewingkey(zaddr)
    return ZExportViewingKeyResponse(viewing_key=viewing_key)



@router.get("/getnetworksolps",
            response_model=GetNetworkSolpsResponse,
            tags=["Mining Methods"],
            summary="Get estimated network solutions per second",
            description="""Get the estimated network solutions per second based on the last n blocks.

### Description
- This endpoint estimates the network's solutions per second based on the last specified number of blocks. 
- You can override the number of blocks to consider, or use -1 to specify the blocks over the difficulty averaging window.
- You can also provide a block height to estimate the network speed at the time when that specific block was found.

### Input Parameters
- `blocks` (int, optional, default=120): The number of blocks to consider, or -1 for blocks over the difficulty averaging window.
- `height` (int, optional, default=-1): The block height for estimating the network speed.

### Example Request
- `GET /getnetworksolps?blocks=100&height=5000`

### Response
- Returns a JSON object containing the estimated solutions per second.

### Example Response
```json
{
    "solutions_per_second": 1234567.89
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Estimated network solutions per second")
async def get_network_solps(request: GetNetworkSolpsRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    solutions_per_second = await rpc_connection.getnetworksolps(request.blocks, request.height)
    return GetNetworkSolpsResponse(solutions_per_second=solutions_per_second)




@router.get("/getlocalsolps",
            response_model=GetLocalSolpsResponse,
            tags=["Mining Methods"],
            summary="Get average local solutions per second",
            description="""Get the average local solutions per second since this node was started. 

### Description
- This endpoint returns the average number of solutions per second that the local node has been generating since it was started. This metric is an indicator of the mining or hashing power of the local node.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getlocalsolps`

### Response
- Returns a JSON object containing the average solutions per second.

### Example Response
```json
{
    "sols_per_second": 123.456
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This information is typically shown on the metrics screen of the node, if enabled.""",
            response_description="Average solutions per second since node start")
async def get_local_solps(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    sols_per_second = await rpc_connection.getlocalsolps()
    return GetLocalSolpsResponse(sols_per_second=sols_per_second)


@router.get("/refreshminingmnidinfo",
            response_model=RefreshMiningMnidInfoResponse,
            tags=["Mining Methods"],
            summary="Refresh mining MNID information",
            description="""Refreshes the mining information (MNIDs) from the pastel.conf file.

### Description
- This endpoint refreshes the list of Masternode IDs (MNIDs) used for mining, as specified in the pastel.conf file. It is useful for updating the mining configuration without restarting the node.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /refreshminingmnidinfo`

### Response
- Returns a JSON array containing the list of refreshed MNIDs.

### Example Response
```json
{
    "mnids": ["mnid1", "mnid2", "mnid3"]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in refreshing the MNID information.

### Note
- This endpoint is particularly useful for miners who need to update their Masternode IDs dynamically.""",
            response_description="List of refreshed Masternode IDs (MNIDs)")
async def refresh_mining_mnid_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    mnids = await rpc_connection.refreshminingmnidinfo()
    return RefreshMiningMnidInfoResponse(mnids=mnids)



@router.get("/getgenerate",
            response_model=GetGenerateResponse,
            tags=["Mining Methods"],
            summary="Check if the server is set to generate coins",
            description="""Check if the server is currently set to generate coins.

### Description
- This endpoint checks the server's coin generation status, which indicates whether the server is set to mine new coins.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getgenerate`

### Response
- Returns a JSON object indicating whether the server is set to generate coins.

### Example Response
```json
{
    "is_generating": false
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The coin generation status is controlled by the `-gen` command line argument or the `gen` setting in `pastel.conf`. It can also be modified using the `setgenerate` call.""",
            response_description="Coin generation status of the server")
async def get_generate(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    is_generating = await rpc_connection.getgenerate()
    return GetGenerateResponse(is_generating=is_generating)




@router.post("/generate",
             response_model=GenerateBlocksResponse,
             tags=["Mining Methods"],
             summary="Mine blocks immediately",
             description="""Mine a specified number of blocks immediately on the regtest network.

### Description
- This endpoint mines a given number of blocks instantly and returns their hashes. Only available on the regtest network.

### Input Parameters
- `num_blocks`: The number of blocks to generate immediately.
- `pastel_id`: (Optional) The Pastel ID eligible to mine the block.

### Example Request
```json
{
    "num_blocks": 11,
    "pastel_id": "pastelid_example"
}
```

### Response
- Returns an array of hashes of the blocks generated.

### Example Response
```json
{
    "block_hashes": [
        "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
        ...
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 403: Forbidden if the method is used outside the regtest network.

### Note
- This method is primarily used for testing and development purposes on the regtest network.""",
             response_description="Array of block hashes generated")
async def generate_blocks(request: GenerateBlocksRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    block_hashes = await rpc_connection.generate(request.num_blocks, request.pastel_id)
    return GenerateBlocksResponse(block_hashes=block_hashes)




@router.post("/setgenerate",
             response_model=SetGenerateResponse,
             tags=["Mining Methods"],
             summary="Set generation on or off",
             description="""Set 'generate' true or false to turn generation on or off. 
             Generation is limited to 'genproclimit' processors, -1 is unlimited. 
             See the getgenerate call for the current setting.

             ### Description
             - This endpoint allows turning on or off the generation (mining) process in the Pastel network. 
             - It controls the number of processors to be used for generation.

             ### Input Parameters
             - `generate` (boolean, required): Set to true to turn on generation, off to turn off.
             - `genproclimit` (numeric, optional): Set the processor limit for when generation is on. Can be -1 for unlimited.

             ### Example Request
             ```json
             {
                 "generate": true,
                 "genproclimit": 1
             }
             ```

             ### Response
             - Returns a message indicating successful change of generation setting.

             ### Example Response
             ```json
             {
                 "message": "Generation setting updated successfully"
             }
             ```

             ### Possible Errors
             - HTTP 400: Bad Request if the parameters are invalid.
             - HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Message indicating the status of generation setting update")
async def set_generate(request: SetGenerateRequest,
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.setgenerate(request.generate, request.genproclimit)
    return SetGenerateResponse(message="Generation setting updated successfully")



@router.post("/prioritisetransaction",
             response_model=PrioritiseTransactionResponse,
             tags=["Mining Methods"],
             summary="Prioritise a transaction for mining",
             description="""Accepts the transaction into mined blocks at a higher (or lower) priority.

### Description
- This endpoint allows modifying the priority of a transaction in the mining queue.
- It is useful for influencing the selection algorithm for transaction inclusion in upcoming blocks.

### Input Parameters
- `txid` (str): The transaction ID to be prioritised.
- `priority_delta` (float): The priority to add or subtract. This alters how the transaction selection algorithm views the transaction's priority.
- `fee_delta` (int): The fee value in patoshis to add (or subtract, if negative). It's a virtual change, affecting only the selection algorithm, not the actual transaction fee.

### Example Request
```json
POST /prioritisetransaction
Content-Type: application/json

{
    "txid": "123abc",
    "priority_delta": 0.0,
    "fee_delta": 10000
}
```

### Response
- Returns a JSON object indicating whether the operation was successful.

### Example Response
```json
{
    "result": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is particularly relevant for miners and services that require transaction prioritisation.""",
             response_description="Indicates whether the transaction was successfully prioritised")
async def prioritise_transaction(request: PrioritiseTransactionRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.prioritisetransaction(request.txid, request.priority_delta, request.fee_delta)
    return PrioritiseTransactionResponse(result=result)




@router.get("/getmininginfo",
            response_model=GetMiningInfoResponse,
            tags=["Mining Methods"],
            summary="Get mining-related information",
            description="""Retrieve mining-related information from the blockchain.

### Description
- Returns a JSON object containing various details about the state of mining on the Pastel blockchain, such as the current block, block size, transactions, difficulty, and network solution rate.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getmininginfo`

### Response
- Returns a JSON object containing detailed mining information.

### Example Response
```json
{
    "blocks": 100,
    "currentblocksize": 1000,
    "currentblocktx": 10,
    "difficulty": 1.23456789,
    "errors": "None",
    "generate": false,
    "genproclimit": -1,
    "localsolps": 2.345678,
    "networksolps": 1234567,
    "pooledtx": 5,
    "testnet": false,
    "chain": "main"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for miners and network analysts to understand the current mining environment and network health.""",
            response_description="Detailed mining information of the Pastel blockchain")
async def get_mining_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    mining_info = await rpc_connection.getmininginfo()
    return GetMiningInfoResponse(**mining_info)



@router.post("/getblocktemplate",
             response_model=GetBlockTemplateResponse,
             tags=["Mining Methods"],
             summary="Get data needed to construct a block to work on",
             description="""Get data needed to construct a block to work on.

### Description
- This endpoint returns data necessary for constructing a block. It's primarily used by miners.
- The method supports a 'template' mode for requesting block template data and a 'proposal' mode for submitting a block proposal.

### Input Parameters
- `jsonrequestobject` (string, optional): A JSON object specifying request details.

### Example Request
- `POST /getblocktemplate {"jsonrequestobject": "{\"mode\":\"template\"}"}`

### Response
- Returns a JSON object with details required to construct a block, including transactions to include, block version, target, and more.

### Example Response
```json
{
    "capabilities": ["proposal"],
    "version": 4,
    "previousblockhash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
    ...
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Detailed specification can be found at https://en.bitcoin.it/wiki/BIP_0022.""",
             response_description="Data required for block construction")
async def get_block_template(request: GetBlockTemplateRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getblocktemplate(request.jsonrequestobject)
    return GetBlockTemplateResponse(**response)



@router.post("/submitblock",
             response_model=SubmitBlockResponse,
             tags=["Blockchain Methods"],
             summary="Submit a new block to the network",
             description="""Attempt to submit a new block to the network.

### Description
- This endpoint attempts to submit a new block to the blockchain. 
- The 'jsonparametersobject' parameter is currently ignored.

### Input Parameters
- `hexdata`: Hex-encoded block data to submit.
- `jsonparametersobject`: Optional JSON object of parameters.

### Request JSON Format
```json
{
    "hexdata": "blockdata",
    "jsonparametersobject": {"workid": "id"}
}
```

### Response
- Returns the result of the block submission.

### Example Response
```json
{
    "result": "duplicate" // or "duplicate-invalid", "duplicate-inconclusive", "inconclusive", "rejected"
}
```

### Possible Errors
- HTTP 400: Bad Request if there are issues with the block data.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The block submission process follows the specification outlined in BIP 0022.""",
             response_description="Result of the block submission")
async def submit_block(request: SubmitBlockRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.submitblock(request.hexdata, request.jsonparametersobject)
    return SubmitBlockResponse(result=result)



@router.get("/estimatepriority",
            response_model=float,
            tags=["Utility Methods"],
            summary="Estimate the transaction priority for zero-fee confirmation",
            description="""Estimate the approximate priority a zero-fee transaction needs to begin confirmation within a specified number of blocks.

### Description
- This endpoint estimates the priority that a zero-fee transaction needs to start confirming within a certain number of blocks.
- It's useful for determining the priority required for a transaction to be included in a block without incurring fees.

### Input Parameters
- `nblocks`: The number of blocks within which the transaction should begin confirmation.

### Example Request
- `GET /estimatepriority?nblocks=6`

### Response
- Returns a numeric value representing the estimated priority.

### Example Response
```json
3.4567
```

### Possible Errors
- HTTP 400: Bad Request if the `nblocks` parameter is not a valid number.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Returns `-1.0` if not enough transactions and blocks have been observed to make an estimate.""",
            response_description="Estimated priority for zero-fee transaction confirmation")
async def estimate_priority(nblocks: int, 
                            rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if nblocks < 1:
        logger.error("nblocks must be at least 1")
    estimated_priority = await rpc_connection.estimatepriority(nblocks)
    return estimated_priority


@router.get("/estimatefee",
            response_model=EstimateFeeResponse,
            tags=["Blockchain Methods"],
            summary="Estimate the transaction fee per kilobyte",
            description="""Estimate the approximate fee per kilobyte needed for a transaction to begin confirmation within a specified number of blocks. 

### Description
- This endpoint provides an estimate of the fee per kilobyte for a transaction to be confirmed within a specified number of blocks.

### Input Parameters
- `nblocks`: The number of blocks within which the transaction should begin confirmation.

### Example Request
- `GET /estimatefee?nblocks=6`

### Response
- Returns a JSON object containing the estimated fee per kilobyte.

### Example Response
```json
{
    "estimated_fee_per_kb": 0.0001
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- A return value of -1.0 indicates insufficient data to make an estimate.""",
            response_description="Estimated fee per kilobyte")
async def estimate_fee(nblocks: int, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if nblocks < 1:
         logger.error("nblocks must be at least 1")
    estimated_fee = await rpc_connection.estimatefee(nblocks)
    return EstimateFeeResponse(estimated_fee_per_kb=estimated_fee)



@router.get("/getblocksubsidy",
            response_model=GetBlockSubsidyResponse,
            tags=["Mining Methods"],
            summary="Get block subsidy reward information",
            description="""Get the block subsidy reward for a given block height, considering the mining slow start.

### Description
- This endpoint returns the block subsidy reward, which includes the mining reward, masternode reward, and governance reward for the specified block height.
- If the height is not provided, the subsidy for the current height of the chain is returned.

### Input Parameters
- `height`: (Optional, numeric) The block height. Defaults to the current height if not provided.

### Example Request
- `GET /getblocksubsidy?height=1000`

### Response
- Returns a JSON object containing the subsidy rewards in each category.

### Example Response
```json
{
    "miner": 12.345,
    "masternode": 3.210,
    "governance": 1.050
}
```

### Possible Errors
- HTTP 400: Bad Request if the block height is out of range or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for understanding the distribution of rewards in the blockchain at a given height.""",
            response_description="Block subsidy reward details")
async def get_block_subsidy(height: Optional[int] = None, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getblocksubsidy(height)
    return GetBlockSubsidyResponse(**response)



@router.get("/getnextblocksubsidy",
            response_model=GetNextBlockSubsidyResponse,
            tags=["Blockchain Methods"],
            summary="Get subsidy rewards for the next block",
            description="""Get the block subsidy rewards of the next block in the Pastel blockchain.

### Description
- This endpoint returns the subsidy rewards for the next block, including the amounts for the miner, masternode, and governance.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getnextblocksubsidy`

### Response
- Returns a JSON object containing the subsidy rewards for the next block.

### Example Response
```json
{
    "miner": 12.5,
    "masternode": 6.25,
    "governance": 1.25
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint provides crucial information for understanding the reward distribution in the upcoming block.""",
            response_description="Subsidy rewards for the next block")
async def get_next_block_subsidy(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    subsidy_info = await rpc_connection.getnextblocksubsidy()
    return GetNextBlockSubsidyResponse(**subsidy_info)




@router.get("/generate-report/{report_name}",
            response_model=GenerateReportResponse,
            tags=["Utility Methods"],
            summary="Generate various reports",
            description="""Generate various reports from the Pastel Network. 

### Description
- This endpoint generates different types of reports based on the Pastel Network's blockchain data.

### Input Parameters
- `report_name`: The name of the report to generate. Currently supported: 'fees-and-burn'.

### Example Request
- `GET /generate-report/fees-and-burn`

### Response
- Returns a JSON object containing the generated report data.

### Example Response
```json
{
    "report_data": {
        // Example report data here
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the report name is not supported.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for analysis and insight into various aspects of the Pastel Network.""",
            response_description="Generated report data")
async def generate_report(report_name: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if report_name not in ["fees-and-burn"]:
        raise logger.error("Report name not supported")
    report_data = await rpc_connection.generate_report(report_name)
    return GenerateReportResponse(report_data=report_data)



@router.get("/tickets/get",
            response_model=TicketsGetResponse,
            tags=["Ticket Methods"],
            summary="Get a Pastel ticket by transaction ID",
            description="""Get any Pastel ticket by its transaction ID (txid).

### Description
- This endpoint retrieves a specific Pastel ticket based on its transaction ID.
- It optionally decodes the ticket properties if 'decode_properties' is set to true.

### Input Parameters
- `txid`: The transaction ID of the ticket.
- `decode_properties`: (Optional) Boolean flag to decode ticket properties, default is false.

### Example Request
- `GET /tickets/get?txid=bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726&decode_properties=true`

### Response
- Returns a JSON object containing the ticket information.

### Example Response
```json
{
    "ticket": {
        "property1": "value1",
        "property2": "value2",
        // Other ticket properties
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
            response_description="Information about the specified Pastel ticket")
async def tickets_get(request: TicketsGetRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_get(request.txid, request.decode_properties)
    return TicketsGetResponse(ticket=response)



@router.get("/tickets/findbylabel/{ticket_type}/{label}",
            response_model=TicketsFindByLabelResponse,
            tags=["Ticket Methods"],
            summary="Find tickets by label",
            description="""Find various types of Pastel tickets by label.

### Description
- This endpoint searches for different types of Pastel tickets (like NFT, collection, or action registration tickets) using a specific label.

### Input Parameters
- `ticket_type`: The type of ticket to search for (nft, action, collection).
- `label`: The label used for ticket search.

### Example Request
- `GET /tickets/findbylabel/nft/someLabel`

### Response
- Returns a JSON object containing a list of tickets that match the given label.

### Example Response
```json
{
    "tickets": [
        {"ticket_data": {"ticket_field1": "value1", "ticket_field2": "value2"}},
        {"ticket_data": {"ticket_field1": "value3", "ticket_field2": "value4"}}
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the ticket type is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this endpoint to search for tickets by their labels across different ticket types.""",
            response_description="List of tickets matching the label")
async def tickets_find_by_label(ticket_type: str, label: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    ticket_type = ticket_type.lower()
    if ticket_type not in ['nft', 'collection', 'action']:
        raise logger.error("Invalid ticket type")
    tickets = await rpc_connection.tickets_findbylabel(ticket_type, label)
    return TicketsFindByLabelResponse(tickets=[TicketInfo(ticket_data=ticket) for ticket in tickets])



@router.get("/getfeeschedule",
            response_model=GetFeeScheduleResponse,
            tags=["Utility Methods"],
            summary="Get the current fee schedule",
            description="""Get the current fee schedule including the chain deflation rate and related fees.

### Description
- This endpoint returns the current fee schedule of the network, which includes various fees associated with operations like PastelID registration, username registration, and username change.
- It also provides the fee deflator factor, which is used to adjust fees based on the chain deflation rate.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getfeeschedule`

### Response
- Returns a JSON object containing the current fee schedule.

### Example Response
```json
{
    "fee_deflator_factor": 1.5,
    "pastelid_registration_fee": 100.0,
    "username_registration_fee": 50.0,
    "username_change_fee": 20.0
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This information is crucial for users and applications that interact with the network, especially for those involving registrations and updates.""",
            response_description="The current fee schedule of the network")
async def get_fee_schedule(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    fee_schedule = await rpc_connection.getfeeschedule()
    return GetFeeScheduleResponse(**fee_schedule)



@router.get("/tickets/{command}", 
            response_model=TicketsResponse, 
            tags=["Ticket Methods"],
            summary="Execute Pastel Ticket Commands",
            description="""Execute various commands related to Pastel tickets.

### Description
- This endpoint allows for the execution of various commands related to Pastel tickets such as registering, activating, finding, listing, and getting tickets.

### Input Parameters
- `command`: The Pastel ticket command to execute. Available commands include register, activate, find, findbylabel, list, get, and tools.

### Example Request
- `GET /tickets/register`

### Response
- Returns the result of the executed command.

### Example Response
```json
{
    "result": "Result of the executed command"
}
```

### Possible Errors
- HTTP 400: Bad Request if the command is not recognized.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The functionality of this endpoint depends on the specific command executed.""",
            response_description="Result of the Pastel ticket command")
async def tickets(command: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.tickets(command)
    return TicketsResponse(result=result)





@router.post("/chaindata/store",
             response_model=ChaindataStoreResponse,
             tags=["Utility Methods"],
             summary="Store data in the blockchain",
             description="""Store data in the blockchain. If successful, returns the transaction ID and raw transaction data.

### Description
- This endpoint stores provided data into the blockchain using a P2FMS transaction.
- The maximum size of the data is 4KB.

### Input Parameters
- `data`: The data to be stored in the blockchain.

### Example Request
- `POST /chaindata/store` with JSON payload `{"data": "<your-data>"}`

### Response
- Returns a JSON object containing the transaction ID (`txid`) and the raw transaction data (`rawtx`).

### Example Response
```json
{
    "txid": "example-txid",
    "rawtx": "example-rawtx"
}
```

### Possible Errors
- HTTP 400: Bad Request if the data is not provided, is empty, or exceeds 4KB.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The data stored can later be retrieved using the 'retrieve' command with the returned `txid`.""",
             response_description="Transaction ID and raw transaction data of the stored data")
async def store_chaindata(request: ChaindataStoreRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Ensure data size constraints
    if len(request.data) == 0:
        raise logger.error("No data provided")
    if len(request.data) > 4096:
        raise  logger.error("The data is too big. 4KB is Max")
    response = await rpc_connection.chaindata("store", request.data)
    return ChaindataStoreResponse(**response)




@router.post("/chaindata/retrieve",
             response_model=ChaindataRetrieveResponse,
             tags=["Utility Methods"],
             summary="Retrieve data from the blockchain",
             description="""Retrieve data from the blockchain by transaction ID (`txid`).

### Description
- This endpoint retrieves data from the blockchain that was stored using the 'store' command and associated with the provided `txid`.

### Input Parameters
- `txid`: The transaction ID of the data to be retrieved.

### Example Request
- `POST /chaindata/retrieve` with JSON payload `{"txid": "example-txid"}`

### Response
- Returns a JSON object containing the retrieved data.

### Example Response
```json
{
    "data": "retrieved data"
}
```

### Possible Errors
- HTTP 400: Bad Request if the `txid` is not provided or is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Retrieved data from the blockchain")
async def retrieve_chaindata(request: ChaindataRetrieveRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.chaindata("retrieve", request.txid)
    return ChaindataRetrieveResponse(data=response)




@router.get("/getblockcount",
            response_model=GetBlockCountResponse,
            tags=["Blockchain Methods"],
            summary="Get the current block count",
            description="""Get the number of blocks in the best valid block chain.

### Description
- This endpoint returns the current block count in the blockchain, which is the number of blocks in the longest valid blockchain.
- It reflects the height of the blockchain and is useful for tracking the growth of the blockchain over time.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getblockcount`

### Response
- Returns a JSON object containing the current block count as a numeric value.

### Example Response
```json
{
    "block_count": 650000
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This is a commonly used method for blockchain explorers, wallets, and other tools that need to know the current height of the blockchain.""",
            response_description="The current block count in the blockchain")
async def get_block_count(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    block_count = await rpc_connection.getblockcount()
    return GetBlockCountResponse(block_count=block_count)



@router.get("/getdifficulty",
            response_model=GetDifficultyResponse,
            tags=["Mining Methods"],
            summary="Get the current proof-of-work difficulty",
            description="""Get the current proof-of-work difficulty as a multiple of the minimum difficulty.

### Description
- This endpoint returns the current network difficulty for proof-of-work. It's a measure of how difficult it is to find a new block compared to the easiest it can ever be.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getdifficulty`

### Response
- Returns a JSON object containing the current proof-of-work difficulty as a numeric value.

### Example Response
```json
{
    "difficulty": 874.625
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This information is particularly useful for miners and analysts interested in the network's mining difficulty.""",
            response_description="The current proof-of-work difficulty")
async def get_difficulty(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    difficulty = await rpc_connection.getdifficulty()
    return GetDifficultyResponse(difficulty=difficulty)



@router.get("/getrawmempool",
            tags=["Blockchain Methods"],
            summary="Get all transaction IDs in memory pool",
            description="""Get the transaction IDs in the memory pool. 

### Description
- Returns all transaction IDs in the memory pool as an array of strings or a detailed JSON object.

### Input Parameters
- `verbose`: (boolean, optional, default=false) Set to true for a detailed JSON object, false for an array of transaction IDs.

### Example Request
- `GET /getrawmempool?verbose=false`

### Response
- For `verbose=false`, returns an array of transaction IDs.
- For `verbose=true`, returns a detailed JSON object with information about each transaction.

### Example Response for `verbose=false`
```json
{
    "transaction_ids": ["txid1", "txid2", "txid3"]
}
```

### Example Response for `verbose=true`
```json
{
    "transactions": {
        "txid1": {
            "size": 250,
            "fee": 0.0001,
            "time": 1617184000,
            "height": 675000,
            "startingpriority": 1000000,
            "currentpriority": 1200000,
            "depends": ["txidA", "txidB"]
        },
        ...
    }
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for retrieving detailed information about transactions in the mempool.""",
            response_description="Transaction IDs or detailed transaction info from the mempool")
async def get_raw_mempool(verbose: Optional[bool] = False, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.getrawmempool(verbose)
    if verbose:
        return GetRawMemPoolVerboseResponse(transactions=result)
    else:
        return GetRawMemPoolResponse(transaction_ids=result)
    
    
    
    
@router.get("/getblockheader/{block_hash}",
            tags=["Blockchain Methods"],
            summary="Get information about a block header",
            description="""Retrieve information about a block header by its hash.

### Description
- Returns either detailed information about the block header or its serialized, hex-encoded data, based on the 'verbose' flag.

### Input Parameters
- `block_hash`: The hash of the block.
- `verbose`: Boolean flag to determine the response format. Defaults to true.

### Example Request
- `GET /getblockheader/00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09?verbose=true`

### Response
- If verbose is true, returns a JSON object with detailed block header information.
- If verbose is false, returns a JSON object with serialized, hex-encoded block header data.

### Example Response
- If verbose is true:
```json
{
  "hash": "hash",
  "confirmations": 5,
  "height": 123456,
  ...
}
```
- If verbose is false:
```json
{
  "data": "hex-encoded data"
}
```

### Possible Errors
- HTTP 404: Block not found.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Block header information based on verbosity")
async def get_block_header(block_hash: str, verbose: bool = True, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getblockheader(block_hash, verbose)
    if verbose:
        return GetBlockHeaderResponseVerbose(**response)
    else:
        return GetBlockHeaderResponseNonVerbose(data=response)
    
    
    
@router.get("/getblockhash",
            response_model=GetBlockHashResponse,
            tags=["Blockchain Methods"],
            summary="Get the hash of a block at a specific index",
            description="""Get the hash of a block in the best-block-chain at the provided index.

### Description
- This endpoint returns the hash of the block at a given index in the blockchain. The index refers to the height of the block in the blockchain.

### Input Parameters
- `index` (int, required): The block index (height) in the blockchain.

### Example Request
- `GET /getblockhash?index=1000`

### Response
- Returns a JSON object containing the hash of the block at the specified index.

### Example Response
```json
{
    "hash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e"
}
```

### Possible Errors
- HTTP 400: Bad Request if the index parameter is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- It's important to ensure the block index is within the valid range of the blockchain.""",
            response_description="Hex-encoded hash of the block at the specified index")
async def get_block_hash(request: GetBlockHashRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    block_hash = await rpc_connection.getblockhash(request.index)
    return GetBlockHashResponse(hash=block_hash)


        
@router.get("/getblock",
            response_model=GetBlockResponse,
            tags=["Blockchain Methods"],
            summary="Get block data",
            description="""Get data of a specific block in the Pastel blockchain. 

### Description
- Depending on the verbosity level, this endpoint returns different details about the specified block.

### Input Parameters
- `block_identifier`: The block hash or height.
- `verbosity`: (Optional) Verbosity level (0, 1, or 2). Defaults to 1.

### Example Request
- `GET /getblock?block_identifier="00000000febc373a..."&verbosity=1`

### Response
- Depending on the verbosity, the response structure varies. Refer to the Pydantic models for details.

### Example Response (verbosity = 1)
```json
{
    "hash": "00000000febc373a...",
    "confirmations": 10,
    "size": 800,
    "height": 12800,
    ...
}
```

### Possible Errors
- HTTP 400: Invalid parameters.
- HTTP 404: Block not found.
- HTTP 500: Internal Server Error.

### Note
- Used for detailed blockchain exploration and data analysis.""",
            response_description="Block data in specified format based on verbosity level")
async def get_block(
    block_identifier: str,
    verbosity: int = Query(1, ge=0, le=2), 
    rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)
):
    block_data = await rpc_connection.getblock(block_identifier, verbosity)
    # Depending on verbosity, parse and return the appropriate response model
    if verbosity == 0:
        return GetBlockResponse(response=BlockResponseVerbosity0(data=block_data))
    elif verbosity == 1:
        return GetBlockResponse(response=BlockResponseVerbosity1(**block_data))
    else:
        # Assuming `blockToJSON` returns a dict with detailed transaction info
        return GetBlockResponse(response=BlockResponseVerbosity2(**block_data))
    



@router.get("/gettxoutsetinfo",
            response_model=GetTxOutSetInfoResponse,
            tags=["Blockchain Methods"],
            summary="Get statistics about the unspent transaction output set",
            description="""Returns statistics about the unspent transaction output set.

### Description
- This endpoint provides detailed information about the state of the unspent transaction output set. It's useful for getting a snapshot of the blockchain's UTXO set at the current moment.
- Note: This call may take some time due to the calculations involved.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /gettxoutsetinfo`

### Response
- Returns a JSON object containing various statistics about the UTXO set.

### Example Response
```json
{
    "height": 650000,
    "bestblock": "0000000000000000000c6da2c440...",
    "transactions": 2500000,
    "txouts": 5000000,
    "bytes_serialized": 300000000,
    "hash_serialized": "3e9cc7000...",
    "total_amount": 18446744.07370955
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is particularly useful for analysis and understanding the overall state of the blockchain.""",
            response_description="Statistics about the unspent transaction output set")
async def get_tx_out_set_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    txoutset_info = await rpc_connection.gettxoutsetinfo()
    return GetTxOutSetInfoResponse(**txoutset_info)            



@router.get("/verifychain",
            response_model=VerifyChainResponse,
            tags=["Blockchain Methods"],
            summary="Verify the blockchain database",
            description="""Verifies the integrity of the blockchain database.

### Description
- This endpoint performs checks on the blockchain database to verify its integrity. 
- It allows specification of the thoroughness of the verification and the number of blocks to check.

### Input Parameters
- `checklevel`: (Optional) An integer between 0 and 4, indicating the thoroughness of the block verification (default is 3).
- `numblocks`: (Optional) The number of blocks to check. Default is 288, with 0 indicating all blocks.

### Example Request
- `GET /verifychain?checklevel=3&numblocks=288`

### Response
- Returns a JSON object containing the result of the verification as a boolean value.

### Example Response
```json
{
    "verified": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are out of the expected range.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is important for network administrators and developers for diagnostics and ensuring the integrity of the blockchain data.""",
            response_description="Result of the blockchain database verification")
async def verify_chain(request: VerifyChainRequest, 
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.verifychain(request.checklevel, request.numblocks)
    return VerifyChainResponse(verified=result)




@router.get("/gettxout",
            response_model=GetTxOutResponse,
            tags=["Blockchain Methods"],
            summary="Get details about an unspent transaction output",
            description="""Get details about an unspent transaction output. 

### Description
- This endpoint returns detailed information about an unspent transaction output (UTXO) from the Pastel blockchain.

### Input Parameters
- `txid`: (string, required) The transaction id.
- `n`: (int, required) The output number (vout) of the transaction.
- `includemempool`: (bool, optional) Whether to include the mempool. Defaults to True.

### Example Request
- `GET /gettxout?txid=<txid>&n=1&includemempool=true`

### Response
- Returns a JSON object containing details of the specified unspent transaction output.

### Example Response
```json
{
    "bestblock": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
    "confirmations": 10,
    "value": 12.34,
    "valuePat": 1234000000,
    "scriptPubKey": {
        "asm": "code",
        "hex": "hex",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": ["address1", "address2"]
    },
    "version": 2,
    "coinbase": false
}
```

### Possible Errors
- HTTP 404: Not Found if the specified transaction output is not found or is already spent.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for verifying the existence and details of specific transaction outputs.""",
            response_description="Details of the unspent transaction output")
async def get_tx_out(txid: str, n: int, includemempool: Optional[bool] = True, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    txout_info = await rpc_connection.gettxout(txid, n, includemempool)
    if txout_info is None:
        raise logger.error("Transaction output not found or already spent.")
    return GetTxOutResponse(**txout_info)




@router.get("/getchaintips",
            response_model=GetChainTipsResponse,
            tags=["Blockchain Methods"],
            summary="Get information about all known chain tips",
            description="""Return information about all known tips in the block tree, including the main chain as well as orphaned branches.

### Description
- This endpoint provides details about all known chain tips in the block tree. This includes information about the main chain and any orphaned or detached branches.
- The response includes the height, hash, branch length, and status for each chain tip.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getchaintips`

### Response
- Returns a JSON array of objects, each representing a chain tip with its associated details.

### Example Response
```json
{
    "tips": [
        {
            "height": 123456,
            "hash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
            "branchlen": 0,
            "status": "active"
        },
        {
            "height": 123455,
            "hash": "00000000000000000007abc8d2b16cd689bd44e2f7f8f36b7e4f938b8b9c6f4f",
            "branchlen": 1,
            "status": "valid-fork"
        }
    ]
}
```

### Possible Status Values
1. `invalid`: Contains at least one invalid block.
2. `headers-only`: Not all blocks are available, but the headers are valid.
3. `valid-headers`: All blocks are available but were never fully validated.
4. `valid-fork`: Fully validated but not part of the active chain.
5. `active`: Part of the active main chain.

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for understanding the structure and different branches of the blockchain.""",
            response_description="List of all known chain tips in the block tree")
async def get_chain_tips(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    tips = await rpc_connection.getchaintips()
    return GetChainTipsResponse(tips=tips)




@router.get("/getmempoolinfo",
            response_model=GetMempoolInfoResponse,
            tags=["Utility Methods"],
            summary="Get active state of the TX memory pool",
            description="""Returns details on the active state of the TX memory pool.

### Description
- This endpoint provides information about the current state of the transaction memory pool. 
- It includes details such as the total number of transactions in the pool, the sum of all transaction sizes, and the total memory usage of the mempool.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getmempoolinfo`

### Response
- Returns a JSON object containing details about the transaction memory pool.

### Example Response
```json
{
    "size": 45,
    "bytes": 123456,
    "usage": 98765
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for understanding the load and capacity of the transaction memory pool.""",
            response_description="Details of the transaction memory pool")
async def get_mempool_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    mempool_info = await rpc_connection.getmempoolinfo()
    return GetMempoolInfoResponse(size=mempool_info['size'], bytes=mempool_info['bytes'], usage=mempool_info['usage'])




@router.get("/getblockchaininfo",
            response_model=BlockchainInfoResponse,
            tags=["Blockchain Methods"],
            summary="Get blockchain information",
            description="""Get detailed information about the state of the blockchain. 

### Description
- This endpoint returns various state info regarding blockchain processing.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getblockchaininfo`

### Response
- Returns a JSON object containing detailed information about the blockchain.

### Example Response
```json
{
    "chain": "main",
    "blocks": 680000,
    "headers": 680000,
    "bestblockhash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
    "difficulty": 19298087186262.61,
    "verificationprogress": 0.999998,
    "chainwork": "0000000000000000000000000000000000000000014d1e4fe926a7b5e76e7c6e",
    "commitments": 289431,
    "softforks": [
        {
            "id": "bip34",
            "version": 2,
            "enforce": {"status": true, "found": 1000, "required": 750, "window": 1000},
            "reject": {"status": true, "found": 1000, "required": 950, "window": 1000}
        }
        // Include other softforks as needed
    ],
    "upgrades": {
        "upgrade1": {
            "name": "example_upgrade",
            "activationheight": 123456,
            "status": "active",
            "info": "Additional information"
        }
        // Include other upgrades as needed
    },
    "consensus": {
        "chaintip": "abcd1234",
        "nextblock": "efgh5678"
    },
    "pruned": false,
    "pruneheight": 12345
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for obtaining a variety of data about the blockchain's current state and history.""",
            response_description="Detailed state info regarding block chain processing")
async def get_blockchain_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    blockchain_info = await rpc_connection.getblockchaininfo()
    return BlockchainInfoResponse(**blockchain_info)



@router.post("/reconsiderblock",
             response_model=ReconsiderBlockResponse,
             tags=["Blockchain Methods"],
             summary="Reconsider a previously invalidated block",
             description="""Removes invalidity status of a block and its descendants, reconsider them for activation.

### Description
- This endpoint is used to undo the effects of `invalidateblock`.
- It reconsiders a block that was previously marked as invalid along with all its descendants.

### Input Parameters
- `hash`: (string, required) The hash of the block to reconsider.

### Example Request
- `POST /reconsiderblock {"hash": "blockhash"}`

### Response
- Returns a JSON object indicating the success or failure of the operation.

### Example Response
```json
{
    "success": true,
    "message": "Block and its descendants reconsidered successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the block hash is invalid or missing.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this method with caution as it affects the blockchain state.""",
             response_description="Status of the reconsideration operation")
async def reconsider_block(request: ReconsiderBlockRequest, 
                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    try:
        await rpc_connection.reconsiderblock(request.hash)
        return ReconsiderBlockResponse(success=True, message="Block and its descendants reconsidered successfully")
    except Exception as e:
        return ReconsiderBlockResponse(success=False, message=str(e))
    
    


@router.post("/invalidateblock",
             response_model=InvalidateBlockResponse,
             tags=["Blockchain Methods"],
             summary="Mark a block as permanently invalid",
             description="""Mark a block as permanently invalid, as if it violated a consensus rule.

### Description
- This endpoint marks a specific block in the blockchain as invalid. This operation is irreversible and treats the block as though it has violated a consensus rule.

### Input Parameters
- `block_hash`: The hash of the block to mark as invalid.

### Example Request
```json
POST /invalidateblock
{
    "block_hash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e"
}
```

### Response
- Returns a JSON object indicating the success or failure of the operation.

### Example Response
```json
{
    "success": true,
    "message": "Block marked as invalid"
}
```

### Possible Errors
- HTTP 400: Bad Request if the block hash is not provided or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This is a critical operation and should be used with caution. Invalidating a block can have significant implications on the blockchain state.""",
             response_description="Result of the invalidate block operation")
async def invalidate_block(block_hash: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    try:
        await rpc_connection.invalidateblock(block_hash)
        return InvalidateBlockResponse(success=True, message="Block marked as invalid")
    except Exception as e:
        return InvalidateBlockResponse(success=False, message=str(e))    
    
    
    
    
@router.get("/getblockdeltas/{block_hash}",
            response_model=GetBlockDeltasResponse,
            tags=["Blockchain Methods"],
            summary="Get block deltas",
            description="""Retrieve detailed information about inputs and outputs of all transactions in a block.

### Description
- This endpoint returns detailed information about each transaction in the specified block, including inputs and outputs.

### Input Parameters
- `block_hash`: The hash of the block for which information is requested.

### Example Request
- `GET /getblockdeltas/00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b`

### Response
- Returns a JSON object containing detailed information about the block and its transactions.

### Example Response
```json
{
    "hash": "00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b",
    "confirmations": 10,
    "size": 190,
    ...
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 404: Not Found if the specified block hash does not exist.

### Note
- This endpoint requires the 'insightexplorer' mode to be enabled on the Pastel node.""",
            response_description="Detailed information about the block and its transactions")
async def get_block_deltas(block_hash: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getblockdeltas(block_hash)
    return GetBlockDeltasResponse(**response)




@router.post("/getrawtransaction",
             tags=["Raw Transaction Methods"],
             summary="Get the raw transaction data",
             description="""Get the raw transaction data for a given transaction id.

### Description
- This endpoint returns the raw transaction data based on the given transaction ID.
- If `verbose` is 0 or not set, it returns a string that is serialized, hex-encoded data for the transaction.
- If `verbose` is non-zero, it returns a JSON object with detailed information about the transaction.

### Input Parameters
- `txid` (string, required): The transaction id.
- `verbose` (int, optional, default=0): If 0, return a string, otherwise return a JSON object.
- `blockhash` (string, optional): The block hash to look for the transaction in.

### Example Request
- `POST /getrawtransaction` with JSON body `{"txid": "mytxid", "verbose": 1}`

### Response
- Depending on the `verbose` parameter, either a string or a JSON object with detailed transaction information.

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Raw transaction data in string or JSON format")
async def get_raw_transaction(request: GetRawTransactionRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getrawtransaction(request.txid, request.verbose, request.blockhash)
    if request.verbose:
        # Parse the response to match the GetRawTransactionResponse model
        return GetRawTransactionResponse(**response)
    else:
        return {"hex": response}
    
    

@router.get("/gettxoutproof",
            response_model=GetTxOutProofResponse,
            tags=["Raw Transaction Methods"],
            summary="Get proof of transaction inclusion in a block",
            description="""Get a hex-encoded proof that one or more transactions were included in a block.

### Description
- This endpoint returns a serialized, hex-encoded data for the proof that specified transaction(s) were included in a block.
- By default, this function only works if there is an unspent output in the UTXO for these transactions. To make it always work, maintain a transaction index with the -txindex command line option, or specify the block hash manually.

### Input Parameters
- `txids`: A list of transaction IDs to filter.
- `block_hash` (Optional): The hash of the block in which to look for the transactions.

### Example Request
- `GET /gettxoutproof?txids=["txid1","txid2"]&block_hash=00000000abc123`

### Response
- Returns a string that is a serialized, hex-encoded data for the proof.

### Example Response
```json
{
    "data": "serialized-hex-encoded-proof-data"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Ensure that the transaction index is maintained for accurate results.""",
            response_description="Serialized, hex-encoded proof data")
async def get_tx_out_proof(txids: List[str], block_hash: Optional[str] = None,
                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    proof_data = await rpc_connection.gettxoutproof(txids, block_hash)
    return GetTxOutProofResponse(data=proof_data)    




@router.post("/createrawtransaction",
             response_model=CreateRawTransactionResponse,
             tags=["Raw Transaction Methods"],
             summary="Create a raw transaction",
             description="""Create a transaction spending the given inputs and sending to the given addresses.

### Description
- This endpoint creates a hex-encoded raw transaction that spends the given inputs and sends to the specified addresses.
- The transaction's inputs are not signed, and it is not stored in the wallet or transmitted to the network.

### Input Parameters
- `transactions`: A list of transaction inputs, each containing:
    - `txid`: The transaction id.
    - `vout`: The output number.
    - `sequence`: (Optional) The sequence number.
- `addresses`: A dictionary with addresses as keys and amounts as values.
- `locktime`: (Optional) Raw locktime. Non-0 value also activates inputs.
- `expiryheight`: (Optional) Expiry height of transaction (if Overwinter is active).

### Example Request
```json
{
    "transactions": [{"txid": "myid", "vout": 0}],
    "addresses": {"address": 0.01},
    "locktime": 0,
    "expiryheight": 1000
}
```

### Response
- Returns a hex string of the transaction.

### Example Response
```json
{
    "transaction": "hex-encoded-transaction"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Hex-encoded raw transaction")
async def create_raw_transaction(request: CreateRawTransactionRequest, 
                                 rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Your logic to call the RPC method and return the response
    transaction_hex = await rpc_connection.createrawtransaction(request.transactions, request.addresses, request.locktime, request.expiryheight)
    return CreateRawTransactionResponse(transaction=transaction_hex)




@router.post("/decoderawtransaction",
             response_model=DecodeRawTransactionResponse,
             tags=["Raw Transaction Methods"],
             summary="Decode a raw transaction",
             description="""Decode a serialized, hex-encoded transaction and return a JSON object representing it.

### Description
- This endpoint decodes a raw, serialized, hex-encoded transaction and provides detailed information about it.

### Input Parameters
- `hexstring` (string, required): The hex-encoded transaction string to decode.

### Example Request
- `POST /decoderawtransaction` with body `{"hexstring": "hex-encoded-string"}`

### Response
- Returns a JSON object containing detailed information about the transaction, including `txid`, `size`, `overwintered` flag, `version`, `locktime`, `vin`, and `vout` fields.

### Example Response
```json
{
    "txid": "id",
    "size": n,
    "overwintered": true,
    "version": n,
    "versiongroupid": "hex",
    "locktime": ttt,
    "expiryheight": n,
    "vin": [
        {
            "txid": "id",
            "vout": n,
            "scriptSig": {
                "asm": "asm",
                "hex": "hex"
            },
            "sequence": n
        }
    ],
    "vout": [
        {
            "value": x.xxx,
            "n": n,
            "scriptPubKey": {
                "asm": "asm",
                "hex": "hex",
                "reqSigs": n,
                "type": "pubkeyhash",
                "addresses": [
                    "Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY"
                ]
            }
        }
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the `hexstring` parameter is invalid or missing.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for debugging transactions and understanding their structure.""",
             response_description="Detailed information about the decoded transaction")
async def decode_raw_transaction(request: DecodeRawTransactionRequest, 
                                 rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.decoderawtransaction(request.hexstring)
    return DecodeRawTransactionResponse(**result)




@router.post("/decodescript",
             response_model=DecodeScriptResponse,
             tags=["Utility Methods"],
             summary="Decode a hex-encoded script",
             description="""Decode a hex-encoded script.

### Description
- This endpoint decodes a hex-encoded script and returns detailed information about it.

### Input Parameters
- `hex`: A string representing the hex-encoded script.

### Example Request
```json
{
    "hex": "hexstring"
}
```

### Response
- Returns a JSON object containing details about the script, such as its assembly representation, type, required signatures, associated addresses, and P2SH.

### Example Response
```json
{
    "asm": "asm",
    "hex": "hex",
    "type": "type",
    "reqSigs": 1,
    "addresses": ["address1", "address2"],
    "p2sh": "address"
}
```

### Possible Errors
- HTTP 400: Bad Request if the hex parameter is invalid or missing.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Decoded script information")
async def decode_script(request: DecodeScriptRequest,
                        rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.decodescript(request.hex)
    return DecodeScriptResponse(**response)