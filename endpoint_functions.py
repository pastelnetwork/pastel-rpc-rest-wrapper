import service_functions
from logger_config import setup_logger
from service_functions import get_local_rpc_settings_func
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel, RootModel, Field, SecretStr
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
    {"name": "Blockchain Methods", "description": "Endpoints for working with blockchain data"},
    {"name": "Mining Methods", "description": "Endpoints for working with mining related operations"},
    {"name": "Ticket Methods", "description": "Endpoints for working with blockchain tickets"},
    {"name": "Supernode Methods", "description": "Endpoints for working with Supernodes"},
    {"name": "Wallet Methods", "description": "Endpoints for working with Wallets"},
    {"name": "Network Methods", "description": "Endpoints for working with network data"},
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
    
class PrevTx(BaseModel):
    txid: str
    vout: int
    scriptPubKey: str
    redeemScript: Optional[str] = None
    amount: float

class SignRawTransactionRequest(BaseModel):
    hexstring: str = Field(..., title="Transaction Hex String")
    prevtxs: Optional[List[PrevTx]] = Field(None, title="Previous Transactions")
    privatekeys: Optional[List[str]] = Field(None, title="Private Keys")
    sighashtype: Optional[str] = Field("ALL", title="Signature Hash Type")
    branchid: Optional[str] = Field(None, title="Consensus Branch ID")

class ErrorObject(BaseModel):
    txid: str
    vout: int
    scriptSig: str
    sequence: int
    error: str

class SignRawTransactionResponse(BaseModel):
    hex: str
    complete: bool
    errors: Optional[List[ErrorObject]]
    
class GetTotalStorageFeeRequest(BaseModel):
    ticket: str
    signatures: str
    pastelid: str
    passphrase: str
    label: str
    fee: int
    imagesize: int

class GetTotalStorageFeeResponse(BaseModel):
    totalstoragefee: int    

class SendRawTransactionRequest(BaseModel):
    hexstring: str
    allowhighfees: Optional[bool] = False

class SendRawTransactionResponse(BaseModel):
    tx_hash: str
    
class EstimateNftStorageFeeResponse(BaseModel):
    estimated_nft_storage_fee_min: int
    estimated_nft_storage_fee_average: int
    estimated_nft_storage_fee_max: int    
    
class ValidateOwnershipRequest(BaseModel):
    item_txid: str
    pastelid: str
    passphrase: str

class ValidateOwnershipResponse(BaseModel):
    type: str
    owns: bool
    txid: str
    transfer: str
    
class FuzzySearch(BaseModel):
    creator: Optional[str] = None
    nft: Optional[str] = None
    series: Optional[str] = None
    keyword: Optional[str] = None
    descr: Optional[str] = None

class SearchJson(BaseModel):
    creator: Optional[str] = None
    blocks: Optional[List[int]] = None
    copies: Optional[List[int]] = None
    rareness_score: Optional[List[int]] = None
    nsfw_score: Optional[List[int]] = None
    fuzzy: Optional[FuzzySearch] = None
    limit: Optional[int] = None

class TicketSearchThumbIdsRequest(BaseModel):
    search_json_base64: str = Field(..., description="Base64-encoded JSON string defining the search criteria.")

class TicketInfo(BaseModel):
    txid: str
    thumbnail_hash: str

class TicketSearchThumbIdsResponse(BaseModel):
    tickets: List[TicketInfo]

class TicketsToolsRequest(BaseModel):
    command: str
    additional_params: Optional[List[str]] = None

class TicketsToolsResponse(BaseModel):
    result: dict

class TicketsRegisterMnidResponse(BaseModel):
    ticket: dict
    height: str
    txid: str
    
class TicketsRegisterIdRequest(BaseModel):
    pastelid: str
    passphrase: str
    address: str

class TicketsRegisterIdResponse(BaseModel):
    ticket: dict
    height: str
    txid: str        
    
class RegisterNFTTicketRequest(BaseModel):
    nft_ticket: str
    signatures: str
    pastelid: str
    passphrase: str
    label: str
    fee: int
    address: Optional[str] = None

class RegisterNFTTicketResponse(BaseModel):
    txid: str
    height: int
    ticket: dict
    
class CollectionTicket(BaseModel):
    collection_ticket_version: int
    collection_name: str
    creator: str
    list_of_pastelids_of_authorized_contributors: List[str]
    blocknum: int
    block_hash: str
    collection_final_allowed_block_height: int
    max_collection_entries: int
    collection_item_copy_count: int
    royalty: float
    green: bool
    app_ticket: dict

class SignatureInfo(BaseModel):
    principal: dict
    mn2: dict
    mn3: dict

class RegisterCollectionTicketRequest(BaseModel):
    collection_ticket: str  # Base64 encoded ticket
    signatures: SignatureInfo
    pastelid: str
    passphrase: str
    label: str
    fee: int
    address: Optional[str] = None

class RegisterCollectionTicketResponse(BaseModel):
    txid: str
    height: int
    ticket: CollectionTicket
    key: str
    label: str
    creator_height: int
    collection_final_allowed_block_height: int
    max_collection_entries: int
    royalty: float
    royalty_address: str
    green: bool
    storage_fee: int
    
class TicketsRegisterOfferRequest(BaseModel):
    txid: str
    price: int
    pastel_id: str
    passphrase: str
    valid_after: Optional[int] = None
    valid_before: Optional[int] = None
    copy_number: Optional[int] = None
    address: Optional[str] = None
    intended_for: Optional[str] = None

class TicketsRegisterOfferResponse(BaseModel):
    ticket: dict
    height: str
    txid: str
    
class RegisterTransferTicketResponse(BaseModel):
    ticket: dict
    height: str
    txid: str

class RegisterTransferTicketRequest(BaseModel):
    offer_txid: str
    accept_txid: str
    pastel_id: str
    passphrase: str
    address: Optional[str] = None

class TicketsRegisterAcceptRequest(BaseModel):
    offer_txid: str
    price: int
    pastel_id: str
    passphrase: str
    address: Optional[str] = None

class TicketsRegisterAcceptResponse(BaseModel):
    ticket: dict
    height: str
    txid: str

class RegisterRoyaltyTicketRequest(BaseModel):
    nft_txid: str
    new_pastelid: str
    old_pastelid: str
    passphrase: str
    address: Optional[str] = None

class RegisterRoyaltyTicketResponse(BaseModel):
    txid: str
    height: int
    ticket: dict    

class TicketsRegisterDownResponse(BaseModel):
    ticket: dict
    height: str
    txid: str

class RegisterUsernameRequest(BaseModel):
    username: str
    pastel_id: str
    passphrase: str
    address: Optional[str] = None

class RegisterUsernameResponse(BaseModel):
    ticket: dict
    height: str
    txid: str

class TicketsRegisterEthereumAddressResponse(BaseModel):
    ticket: dict
    height: str
    txid: str

class TicketsRegisterEthereumAddressRequest(BaseModel):
    ethereum_address: str
    pastel_id: str
    passphrase: str
    address: Optional[str] = None

class ActionTicketRequest(BaseModel):
    action_ticket: str
    signatures: str
    pastelid: str
    passphrase: str
    label: str
    fee: int
    address: Optional[str] = None

class ActionTicketResponse(BaseModel):
    txid: str
    height: int
    ticket: dict

class GovernanceTicketResponse(BaseModel):
    result: str
    ticket_id: Optional[str] = Field(None, alias="ticketId")
    error_message: Optional[str] = Field(None, alias="errorMessage")

class GovernanceTicket(BaseModel):
    id: str
    ticket: str

class GovernanceListResponse(RootModel):
    pass

GovernanceResponse = Union[GovernanceTicketResponse, GovernanceListResponse]
    
class MasternodeBasicInfo(BaseModel):
    status: str
    protocol: int
    payee: str
    lastseen: int
    activeseconds: int
    sentinelversion: str
    sentinelstate: str
    address: str

class MasternodeRankInfo(BaseModel):
    rank: int

class MasternodeFullInfo(MasternodeBasicInfo):
    lastpaidtime: int
    lastpaidblock: int

class MasternodeExtraInfo(BaseModel):
    extAddress: str
    extP2P: str
    extKey: str
    extCfg: str

# The response can be one of several types, depending on the mode.
MasternodeListResponse = Union[Dict[str, MasternodeRankInfo], 
                              Dict[str, MasternodeBasicInfo], 
                              Dict[str, MasternodeFullInfo], 
                              Dict[str, MasternodeExtraInfo]]

class MasternodeOutputsResponse(BaseModel):
    outputs: dict

class MasternodeInitRequest(BaseModel):
    passphrase: str
    txid: str
    index: int

class MasternodeInitResponse(BaseModel):
    mnid: str
    legRoastKey: str
    txid: str
    outIndex: int
    privKey: str

class MasternodeMakeConfRequest(BaseModel):
    alias: str
    mn_address: str
    ext_address: str
    ext_p2p: str
    passphrase: str
    txid: Optional[str] = None
    index: Optional[int] = None

class MasternodeConfig(BaseModel):
    mn_address: str
    ext_address: str
    ext_p2p: str
    txid: str
    out_index: str
    mn_priv_key: str
    ext_key: str

class MasternodeMakeConfResponse(BaseModel):
    alias: str
    config: MasternodeConfig

class MasternodeClearCacheResponse(BaseModel):
    status: str
    
class MasterNodePoseBanScoreRequest(BaseModel):
    command: str  # Either "get" or "increment"
    txid: str
    index: int

class MasterNodePoseBanScoreResponse(BaseModel):
    txid: str
    index: int
    pose_ban_score: int
    pose_banned: bool
    pose_ban_height: Optional[int] = None
    
class MasternodeMessageRequest(BaseModel):
    operation: str
    pub_key: Optional[str] = None
    message: Optional[str] = None
    message_id: Optional[str] = None
    additional_param: Optional[int] = None

class MasternodeMessageResponse(BaseModel):
    result: Optional[str]
    signature: Optional[str]
    pubkey: Optional[str]
    messages: Optional[dict]    

class MasternodeCommandRequest(BaseModel):
    command: str
    additional_args: Optional[dict] = {}

class MasternodeCountResponse(BaseModel):
    count: int

class MasternodeWinnerInfo(BaseModel):
    address: str
    txid: str
    output_index: int
    score: int

class MasternodeWinnersResponse(BaseModel):
    winners: List[MasternodeWinnerInfo]

class MasternodeGenKeyResponse(BaseModel):
    private_key: str

class MasternodeCurrentInfo(BaseModel):
    address: str
    txid: str
    output_index: int
    score: int

class MasternodeStatusResponse(BaseModel):
    status: str
    message: str

class MasternodeInfo(BaseModel):
    address: str
    payee: str
    status: str
    protocol: int

class MasternodeListResponse(BaseModel):
    masternodes: Dict[str, MasternodeInfo]

class MasternodeTopInfo(BaseModel):
    rank: int
    address: str
    payee: str

class MasternodeTopResponse(BaseModel):
    top_masternodes: List[MasternodeTopInfo]

class MasternodePoSeBanScoreResponse(BaseModel):
    txid: str
    index: int
    pose_ban_score: int
    pose_banned: bool
    pose_ban_height: Optional[int] = None

MasternodeCommandResponse = Union[
    MasternodeCountResponse, 
    MasternodeWinnersResponse, 
    MasternodeGenKeyResponse,
    MasternodeCurrentInfo,
    MasternodeStatusResponse,
    MasternodeListResponse,
    MasternodeTopResponse,
    MasternodePoSeBanScoreResponse
]

class TicketFindResponse(BaseModel):
    # Define the structure of the ticket data here. 
    # This is a placeholder structure, modify according to the actual ticket data structure.
    ticket_id: str
    ticket_data: Optional[dict]

FindTicketsResponse = Union[TicketFindResponse, List[TicketFindResponse]]

class GetNewAddressResponse(BaseModel):
    address: str

class GetAccountAddressResponse(BaseModel):
    zcashaddress: str

class GetAccountResponse(BaseModel):
    account_name: str
    
class SetAccountRequest(BaseModel):
    zcashaddress: str
    account: str

class SetAccountResponse(BaseModel):
    success: bool
    message: str    

class SendToAddressRequest(BaseModel):
    t_address: str
    amount: float
    comment: Optional[str] = None
    comment_to: Optional[str] = None
    subtract_fee_from_amount: Optional[bool] = False
    change_address: Optional[str] = "original"

class SendToAddressResponse(BaseModel):
    transaction_id: str

class AddressGrouping(BaseModel):
    address: str
    amount: float
    account: Optional[str] = None

class AddressGroupingsResponse(BaseModel):
    groupings: list[list[AddressGrouping]]

class ListAddressAmountsRequest(BaseModel):
    include_empty: Optional[bool] = False
    ismine_filter: Optional[str] = "all"

    class Config:
        schema_extra = {
            "example": {
                "include_empty": True,
                "ismine_filter": "spendableOnly"
            }
        }

class ListAddressAmountsResponse(BaseModel):
    balances: Dict[str, float]

    class Config:
        schema_extra = {
            "example": {
                "balances": {
                    "t1XYZ...abc": 0.5,
                    "t1ABC...xyz": 1.2
                }
            }
        }

class GetReceivedByAddressResponse(BaseModel):
    total_amount: float

class SignMessageRequest(BaseModel):
    t_addr: str
    message: str

class SignMessageResponse(BaseModel):
    signature: str

class GetBalanceResponse(BaseModel):
    balance: float

class GetReceivedByAccountRequest(BaseModel):
    account: str
    minconf: Optional[int] = 1

class GetReceivedByAccountResponse(BaseModel):
    amount: float

class MoveRequest(BaseModel):
    fromaccount: str
    toaccount: str
    amount: float
    minconf: Optional[int] = 1
    comment: Optional[str] = None

class MoveResponse(BaseModel):
    success: bool
    
class SendFromResponse(BaseModel):
    transaction_id: str
    
class SendManyRequest(BaseModel):
    from_account: str
    amounts: dict[str, float]
    min_conf: Optional[int] = 1
    comment: Optional[str] = None
    subtract_fee_from_amount: Optional[list[str]] = []
    change_address: Optional[str] = "original"

class SendManyResponse(BaseModel):
    transaction_id: str

class AddMultisigAddressRequest(BaseModel):
    nrequired: int
    keysobject: List[str]
    account: Optional[str] = None

class AddMultisigAddressResponse(BaseModel):
    zcashaddress: str

class AddressReceivedInfo(BaseModel):
    involvesWatchonly: Optional[bool]
    address: str
    account: str  # Note: Deprecated
    amount: float
    confirmations: int

class ListTransactionsRequest(BaseModel):
    account: Optional[str] = None
    count: Optional[int] = 10
    from_index: Optional[int] = 0
    include_watch_only: Optional[bool] = False

class TransactionInfo(BaseModel):
    account: Optional[str] = None
    address: Optional[str] = None
    category: str
    amount: float
    vout: Optional[int] = None
    fee: Optional[float] = None
    confirmations: Optional[int] = None
    blockhash: Optional[str] = None
    blockindex: Optional[int] = None
    blocktime: Optional[int] = None
    txid: str
    time: int
    timereceived: Optional[int] = None
    comment: Optional[str] = None
    to: Optional[str] = None
    otheraccount: Optional[str] = None
    size: Optional[int] = None

class ListTransactionsResponse(BaseModel):
    transactions: List[TransactionInfo]

class ListAccountsResponseItem(BaseModel):
    account: str
    balance: float

class ListAccountsResponse(BaseModel):
    accounts: list[ListAccountsResponseItem]
    
class ListSinceBlockRequest(BaseModel):
    blockhash: Optional[str] = None
    target_confirmations: Optional[int] = 1
    include_watchonly: Optional[bool] = False

class ListSinceBlockResponse(BaseModel):
    transactions: List[TransactionInfo]
    lastblock: str    

class TransactionDetail(BaseModel):
    account: Optional[str] = Field(None, description="Deprecated. The account name involved in the transaction.")
    address: str = Field(..., description="The Pastel address involved in the transaction.")
    category: str = Field(..., description="The category, either 'send' or 'receive'.")
    amount: float = Field(..., description="The amount in currency unit.")
    amountPat: int = Field(..., description="The amount in minor currency unit.")
    vout: int = Field(..., description="The vout value.")

class GetTransactionResponse(BaseModel):
    status: str = Field(..., description="The transaction status (mined, waiting, expiringsoon, expired).")
    amount: float = Field(..., description="The transaction amount in currency unit.")
    amountPat: int = Field(..., description="The amount in minor currency unit.")
    confirmations: int = Field(..., description="The number of confirmations.")
    blockhash: Optional[str] = Field(None, description="The block hash.")
    blockindex: Optional[int] = Field(None, description="The block index.")
    blocktime: Optional[int] = Field(None, description="The time in seconds since epoch (1 Jan 1970 GMT).")
    txid: str = Field(..., description="The transaction id.")
    time: int = Field(..., description="The transaction time in seconds since epoch (1 Jan 1970 GMT).")
    timereceived: int = Field(..., description="The time received in seconds since epoch (1 Jan 1970 GMT).")
    details: List[TransactionDetail] = Field(..., description="Details of the transaction.")
    hex: str = Field(..., description="Raw data for transaction.")

class BackupWalletRequest(BaseModel):
    destination: str

class BackupWalletResponse(BaseModel):
    path: str

class WalletPassphraseRequest(BaseModel):
    passphrase: str
    timeout: int

class WalletPassphraseResponse(BaseModel):
    result: Optional[str] = "Wallet unlocked successfully"

class KeypoolRefillRequest(BaseModel):
    newsize: Optional[int] = 100  # Default value as per the RPC method's specification
    
class EncryptWalletResponse(BaseModel):
    message: str

class WalletPassphraseChangeRequest(BaseModel):
    oldpassphrase: str
    newpassphrase: str

class WalletPassphraseChangeResponse(BaseModel):
    result: str

class TransactionOutput(BaseModel):
    txid: str = Field(..., title="Transaction ID", description="The transaction id")
    vout: int = Field(..., ge=0, title="Output Number", description="The output number")

class LockUnspentRequest(BaseModel):
    unlock: bool = Field(..., title="Unlock Flag", description="Whether to unlock (true) or lock (false) the specified transactions")
    transactions: List[TransactionOutput] = Field(..., title="Transactions", description="A list of transaction outputs to lock or unlock")

class LockUnspentResponse(BaseModel):
    success: bool = Field(..., title="Success", description="Whether the command was successful or not")

class SetTxFeeRequest(BaseModel):
    amount: float

class SetTxFeeResponse(BaseModel):
    success: bool

class ListLockUnspentResponseItem(BaseModel):
    txid: str
    vout: int

class ListLockUnspentResponse(BaseModel):
    lock_unspent_outputs: List[ListLockUnspentResponseItem]

class WalletInfoResponse(BaseModel):
    walletversion: int
    balance: float
    unconfirmed_balance: float
    immature_balance: float
    txcount: int
    keypoololdest: int
    keypoolsize: int
    unlocked_until: Optional[int] = None
    paytxfee: float
    seedfp: Optional[str] = None

class ResendWalletTransactionsResponse(BaseModel):
    transaction_ids: List[str]
    
class UnspentTransaction(BaseModel):
    txid: str
    vout: int
    generated: bool
    address: Optional[str]
    account: Optional[str]
    scriptPubKey: str
    amount: float
    confirmations: int
    redeemScript: Optional[str]
    spendable: bool

class ListUnspentResponse(BaseModel):
    unspent_transactions: List[UnspentTransaction]    

class ZListUnspentResponseItem(BaseModel):
    txid: str
    outindex: int
    confirmations: int
    spendable: bool
    address: str
    amount: float
    memo: Optional[str]
    change: Optional[bool]

class ZListUnspentResponse(BaseModel):
    unspent_notes: List[ZListUnspentResponseItem]

class FundRawTransactionRequest(BaseModel):
    hexstring: str

class FundRawTransactionResponse(BaseModel):
    hex: str
    fee: float
    changepos: int

class ZGetNewAddressResponse(BaseModel):
    zcash_address: str

class ZCBenchmarkSampleResult(BaseModel):
    runningtime: float

class ZCBenchmarkRequest(BaseModel):
    benchmarktype: str
    samplecount: int
    extra_param: Optional[int] = None

class ZCBenchmarkResponse(BaseModel):
    results: List[ZCBenchmarkSampleResult]

class ListShieldedAddressesResponse(BaseModel):
    addresses: List[str]

class ZListReceivedByAddressRequest(BaseModel):
    address: str
    minconf: Optional[int] = 1

class ReceivedNoteInfo(BaseModel):
    txid: str
    amount: float
    amountPat: float
    memo: str
    confirmations: int
    blockheight: int
    blockindex: int
    blocktime: int
    jsindex: Optional[int]
    jsoutindex: Optional[int]
    outindex: Optional[int]
    change: bool

class ZListReceivedByAddressResponse(BaseModel):
    notes: List[ReceivedNoteInfo]

class ZGetBalanceResponse(BaseModel):
    balance: float

class ZGetTotalBalanceRequest(BaseModel):
    minconf: Optional[int] = 1
    includeWatchonly: Optional[bool] = False

class ZGetTotalBalanceResponse(BaseModel):
    transparent: float
    private: float
    total: float    
    
class SpendDetail(BaseModel):
    type: str
    spend: Optional[int] = None
    txidPrev: str
    jsPrev: Optional[int] = None
    jsOutputPrev: Optional[int] = None
    outputPrev: Optional[int] = None
    address: str
    value: float
    valuePat: int

class OutputDetail(BaseModel):
    type: str
    output: int
    address: str
    outgoing: bool
    value: float
    valuePat: int
    memo: Optional[str] = None
    memoStr: Optional[str] = None

class ZViewTransactionResponse(BaseModel):
    txid: str
    spends: List[SpendDetail] = []
    outputs: List[OutputDetail] = []
    
class ZOperationResultInfo(BaseModel):
    id: str
    status: str
    creation_time: int
    result: Optional[dict] = None
    error: Optional[dict] = None
    method: str
    params: dict

class ZGetOperationResultResponse(BaseModel):
    operation_results: List[ZOperationResultInfo]
        
class OperationStatusInfo(BaseModel):
    id: str
    status: str
    creation_time: int
    method: str
    params: dict
    result: dict
    error: dict
    execution_secs: Optional[float] = None
    method_finished: bool

class GetOperationStatusResponse(BaseModel):
    operations: List[OperationStatusInfo]

class SendManyRecipient(BaseModel):
    address: str
    amount: float
    memo: Optional[str] = None

class ZShieldCoinbaseRequest(BaseModel):
    fromaddress: str = Field(..., description="The source transparent address or '*' for all taddrs belonging to the wallet.")
    toaddress: str = Field(..., description="The destination shielded address.")
    fee: Optional[float] = Field(default=None, description="The fee amount to attach to this transaction.")
    limit: Optional[int] = Field(default=None, description="The maximum number of UTXOs to shield.")

class ZShieldCoinbaseResponse(BaseModel):
    remainingUTXOs: int
    remainingValue: float
    shieldingUTXOs: int
    shieldingValue: float
    opid: str
    
class MergeToAddressRequest(BaseModel):
    fromaddresses: List[str]
    toaddress: str
    fee: Optional[float] = None
    transparent_limit: Optional[int] = None
    shielded_limit: Optional[int] = None
    memo: Optional[str] = None
    
class MergeToAddressResponse(BaseModel):
    remainingUTXOs: int
    remainingTransparentValue: float
    remainingNotes: int
    remainingShieldedValue: float
    mergingUTXOs: int
    mergingTransparentValue: float
    mergingNotes: int
    mergingShieldedValue: float
    opid: str

class ZListOperationIdsResponse(BaseModel):
    operation_ids: list[str]
    
class ZGetNotesCountResponse(BaseModel):
    sapling: int
    
class GetTxfeeResponse(BaseModel):
    txid: str
    height: Optional[int]
    blockHash: Optional[str]
    txFeePat: int
    txFee: float
    
class ScanForMissingTxsRequest(BaseModel):
    starting_height: int

class ScanForMissingTxsResponse(BaseModel):
    missing_txs: List[str]

class FixMissingTransactionsResponse(BaseModel):
    missing_transactions: List[str]
    
class StorageFeeSetFeeRequest(BaseModel):
    fee_type: str
    new_fee: Optional[int] = None

class StorageFeeSetFeeResponse(BaseModel):
    success: bool

class StorageFeeGetFeeResponse(BaseModel):
    fee: float
    fee_pat: float
    height: int
    chain_deflator_factor: float
    
class StorageFeeInfo(BaseModel):
    fee: int
    fee_pat: int

class GetFeesResponse(BaseModel):
    height: int
    chain_deflator_factor: float
    fees: Dict[str, StorageFeeInfo]

class GetActionFeesResponse(BaseModel):
    datasize: int
    height: int
    fee_deflator_factor: float
    action_fees: Dict[str, StorageFeeInfo]
    
class StorageFeeResponse(BaseModel):
    # Define a general response model. 
    # You might need to adjust this based on the actual structure of your response.
    result: Optional[dict]

class PastelIDNewKeyRequest(BaseModel):
    passphrase: str

class PastelIDNewKeyResponse(BaseModel):
    pastelid: str
    legroast: str
        
class PastelIDImportKeyRequest(BaseModel):
    key: str
    passphrase: Optional[str] = None

class PastelIDImportKeyResponse(BaseModel):
    pastel_id: str
    
class PastelIDListResponse(BaseModel):
    pastel_ids: List[Dict[str, str]]            

class PastelIDSignRequest(BaseModel):
    text: str
    pastel_id: str
    passphrase: str
    algorithm: Optional[str] = None

class PastelIDSignResponse(BaseModel):
    signature: str

class PastelIDSignFileRequest(BaseModel):
    file_path: str
    pastel_id: str
    passphrase: SecretStr
    algorithm: Optional[str] = "ed448"

class PastelIDSignFileResponse(BaseModel):
    signature: str

class PastelIDVerifyRequest(BaseModel):
    text: str
    signature: str
    pastelid: str
    algorithm: Optional[str] = None

class PastelIDVerifyResponse(BaseModel):
    verification: str
    
class PastelIDVerifyFileResponse(BaseModel):
    verification: str    

class PastelIDPasswdRequest(BaseModel):
    pastelid: str
    old_passphrase: str
    new_passphrase: str

class PastelIDPasswdResponse(BaseModel):
    result: str
    
class PastelidSignByKeyRequest(BaseModel):
    text: str
    key: str
    passphrase: str

class PastelidSignByKeyResponse(BaseModel):
    signature: str  # The actual signature of the text signed with the private key

class TicketsListResponse(BaseModel):
    tickets: List[Any]

class MasternodeBroadcastRequest(BaseModel):
    command: str
    parameters: Optional[str] = None
    fast: Optional[bool] = None

class MasternodeStatus(BaseModel):
    outpoint: str
    addr: str
    error_message: Optional[str] = None

class MasternodeBroadcastResponse(BaseModel):
    overall: str
    detail: Optional[List[MasternodeStatus]] = None
    hex: Optional[str] = None

    
            
        
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
            tags=["Utility Methods"],
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
             tags=["Wallet Methods"],
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
            tags=["Wallet Methods"],
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
             tags=["Wallet Methods"],
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
             tags=["Wallet Methods"],
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
            tags=["Wallet Methods"],
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
        logger.error("Report name not supported")
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
        logger.error("Invalid ticket type")
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
        logger.error("No data provided")
    if len(request.data) > 4096:
        logger.error("The data is too big. 4KB is Max")
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
        logger.error("Transaction output not found or already spent.")
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




@router.post("/signrawtransaction", 
             response_model=SignRawTransactionResponse, 
             tags=["Raw Transaction Methods"],
             summary="Sign a raw transaction",
             description="""Sign inputs for a raw transaction (serialized, hex-encoded). 
### Description
- This endpoint signs the inputs of a given raw transaction.

### Input Parameters
- `hexstring`: The transaction hex string.
- `prevtxs`: An optional array of previous dependent transaction outputs.
- `privatekeys`: An optional array of base58-encoded private keys for signing.
- `sighashtype`: The signature hash type (default is "ALL").
- `branchid`: An optional consensus branch ID for signing.

### Example Request
```json
{
    "hexstring": "01000000...",
    "prevtxs": [{"txid": "0123abcd...", "vout": 0, "scriptPubKey": "76a914...", "amount": 0.1}],
    "privatekeys": ["5J1m2B...", "5Hs2R..."],
    "sighashtype": "ALL"
}
```

### Response
- Returns the signed transaction in hex format, along with a flag indicating if the transaction has a complete set of signatures.

### Example Response
```json
{
    "hex": "01000000...",
    "complete": true,
    "errors": []
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The endpoint is used for manually signing raw transactions before broadcasting them to the network.""",
             response_description="The signed raw transaction with details")
async def sign_raw_transaction(request: SignRawTransactionRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.signrawtransaction(
        request.hexstring, 
        request.prevtxs, 
        request.privatekeys, 
        request.sighashtype, 
        request.branchid
    )
    return SignRawTransactionResponse(**result)





@router.post("/tickets/tools/gettotalstoragefee",
             response_model=GetTotalStorageFeeResponse,
             tags=["Ticket Methods"],
             summary="Calculate Total Storage Fee for NFT Registration",
             description="""Calculate the total storage fee for the NFT registration ticket.

### Description
- This endpoint calculates the full storage fee for NFT registration based on the provided ticket details and image size.

### Input Parameters
- `ticket`: Base64 encoded ticket created by the creator.
- `signatures`: Base64 encoded signatures and Pastel IDs of the creator and verifying masternodes.
- `pastelid`: The registering masternode (MN1) Pastel ID.
- `passphrase`: Passphrase for the private key associated with the Pastel ID.
- `label`: Label for the ticket.
- `fee`: Agreed upon storage fee.
- `imagesize`: Size of the image in MB.

### Example Request
```json
{
    "ticket": "ticket-blob",
    "signatures": "{signatures}",
    "pastelid": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "passphrase",
    "label": "label",
    "fee": 100,
    "imagesize": 3
}
```

### Response
- Returns a JSON object containing the total storage fee for the NFT registration.

### Example Response
```json
{
    "totalstoragefee": 500
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used during the NFT registration process to calculate the storage fee.""",
             response_description="Total storage fee for NFT registration")
async def get_total_storage_fee(request: GetTotalStorageFeeRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    rpc_params = [request.ticket, request.signatures, request.pastelid, request.passphrase, request.label, request.fee, request.imagesize]
    total_storage_fee = await rpc_connection.call('tickets', 'tools', 'gettotalstoragefee', *rpc_params)
    return GetTotalStorageFeeResponse(totalstoragefee=total_storage_fee)




@router.post("/sendrawtransaction",
             response_model=SendRawTransactionResponse,
             tags=["Raw Transaction Methods"],
             summary="Submit a raw transaction to the network",
             description="""Submit a raw transaction (serialized, hex-encoded) to the local node and network.

### Description
- This endpoint is used to submit a serialized, hex-encoded transaction to the network.
- It can be used in combination with `createrawtransaction` and `signrawtransaction` calls.

### Input Parameters
- `hexstring` (string, required): The hex string of the raw transaction.
- `allowhighfees` (boolean, optional, default=false): Allow high fees.

### Example Request
- `POST /sendrawtransaction` with JSON body: 
```json
{
    "hexstring": "signedhex",
    "allowhighfees": false
}
```

### Response
- Returns a JSON object containing the transaction hash.

### Example Response
```json
{
    "tx_hash": "transactionhashinhex"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="The transaction hash in hex")
async def send_raw_transaction(request: SendRawTransactionRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    tx_hash = await rpc_connection.sendrawtransaction(request.hexstring, request.allowhighfees)
    return SendRawTransactionResponse(tx_hash=tx_hash)




@router.get("/tickets/tools/estimatenftstoragefee",
            response_model=EstimateNftStorageFeeResponse,
            tags=["Ticket Methods"],
            summary="Estimate storage fee for NFT registration",
            description="""Estimate the storage fee for NFT registration based on the image size. 

### Description
- This endpoint estimates the storage fee in PSL for NFT registration for a given image size.

### Input Parameters
- `image_size_in_mb`: The estimated size of the image in megabytes (MB).

### Example Request
- `GET /tickets/tools/estimatenftstoragefee?image_size_in_mb=3`

### Response
- Returns a JSON object containing the estimated minimum, average, and maximum storage fees for the NFT.

### Example Response
```json
{
    "estimated_nft_storage_fee_min": 100,
    "estimated_nft_storage_fee_average": 150,
    "estimated_nft_storage_fee_max": 200
}
```

### Possible Errors
- HTTP 400: Bad Request if the image size is not provided or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for users and applications to estimate the cost of NFT registration.""",
            response_description="Estimated storage fees for NFT registration")
async def estimate_nft_storage_fee(image_size_in_mb: int, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_tools_estimatenftstoragefee(image_size_in_mb)
    return EstimateNftStorageFeeResponse(**response)




@router.post("/tickets/tools/validateownership",
             response_model=ValidateOwnershipResponse,
             tags=["Ticket Methods"],
             summary="Validate item ownership by Pastel ID",
             description="""Validate item ownership by Pastel ID.

### Description
- This endpoint checks whether the given Pastel ID is the owner of a specified item.
- It returns details of the item, including the type, ownership status, item transaction ID, and transfer ticket transaction ID.

### Input Parameters
- `item_txid` (string, required): The transaction ID of the original NFT registration.
- `pastelid` (string, required): The registered Pastel ID supposed to own the item.
- `passphrase` (string, required): The passphrase to the private key associated with the Pastel ID.

### Example Request
```json
{
    "item_txid": "e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4",
    "pastelid": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "passphrase"
}
```

### Response
- Returns a JSON object with the item type, ownership status, item transaction ID, and transfer ticket transaction ID.

### Example Response
```json
{
    "type": "unknown",
    "owns": false,
    "txid": "",
    "transfer": ""
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is critical for confirming ownership of NFTs and other registered items on the Pastel Network.""",
             response_description="Ownership validation information for the specified item and Pastel ID")
async def validate_ownership(request: ValidateOwnershipRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_tools_validateownership(request.item_txid, request.pastelid, request.passphrase)
    return ValidateOwnershipResponse(**response)





@router.post("/tickets/tools/searchthumbids",
             response_model=TicketSearchThumbIdsResponse,
             tags=["Ticket Methods"],
             summary="Search for NFT registration tickets and thumbnail hash",
             description="""Search for the NFT registration tickets and thumbnail_hash using filters defined by the search_json parameter (Base64-encoded).

### Description
- This endpoint allows searching for NFT registration tickets and associated thumbnail hashes based on various criteria.
- The search criteria are provided as a Base64-encoded JSON string.

### Input Parameters
- `search_json_base64`: A Base64-encoded JSON string defining the search criteria. The JSON structure includes fields like 'creator', 'blocks', 'copies', 'rareness_score', 'nsfw_score', and 'fuzzy' for fuzzy searches.

### Example Request
- `POST /tickets/tools/searchthumbids` with JSON body:
  ```json
  {
      "search_json_base64": "eyJjcmVhdG9yIjogIm1pbmUiLCAiYmxvY2tzIjogWzIwMDAwLDMwMDAwXSwgImNvcGllcyI6IFswLDJdfQ=="
  }
  ```

### Response
- Returns a JSON array of objects with NFT registration ticket "txid" and thumbnail hash.

### Example Response
```json
{
    "tickets": [
        {"txid": "txid_1", "thumbnail_hash": "thumbnail_hash_1"},
        {"txid": "txid_2", "thumbnail_hash": "thumbnail_hash_2"}
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid or if the Base64 decoding fails.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="List of NFT registration tickets and their thumbnail hashes")
async def tickets_tools_searchthumbids(request: TicketSearchThumbIdsRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.tickets_tools_searchthumbids(request.search_json_base64)
    return TicketSearchThumbIdsResponse(tickets=result)




@router.post("/tickets/tools",
            response_model=TicketsToolsResponse,
            tags=["Ticket Methods"],
            summary="Execute various ticket tools commands",
            description="""Execute a set of Pastel ticket tools commands.

### Description
- This endpoint provides a variety of tools related to Pastel tickets, enabling operations like printing trading chains, getting registration tickets by transfer txid, validating usernames and ethereum addresses, and more.

### Input Parameters
- `command` (str, required): The command to be executed.
- `additional_params` (List[str], optional): Additional parameters required for specific commands.

### Example Request
- `POST /tickets/tools` with JSON body:
```json
{
    "command": "printtradingchain",
    "additional_params": ["param1", "param2"]
}
```

### Response
- Returns a JSON object containing the result of the executed command.

### Example Response
```json
{
    "result": {
        "key": "value"
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The specific output and required additional parameters depend on the command executed.""",
            response_description="Result of the executed ticket tool command")
async def tickets_tools(request: TicketsToolsRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.tickets_tools(request.command, request.additional_params)
    return TicketsToolsResponse(result=result)




@router.post("/tickets/register/mnid",
             response_model=TicketsRegisterMnidResponse,
             tags=["Ticket Methods"],
             summary="Register Masternode PastelID",
             description="""Register the identity of the current Masternode into the blockchain. 

### Description
- This endpoint registers the PastelID of the Masternode on the blockchain. It requires an active Masternode.

### Input Parameters
- `pastelid`: The PastelID to register. The PastelID must be generated and stored inside the node.
- `passphrase`: The passphrase to the private key associated with the PastelID.
- `address` (optional): The Pastel blockchain t-address to use for funding the registration.

### Example Request
```json
{
    "pastelid": "jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M",
    "passphrase": "passphrase",
    "address": "P_address"
}
```

### Response
- Returns a JSON object containing the registration details of the Masternode PastelID.

### Example Response
```json
{
    "ticket": {
        "type": "pastelid",
        "pastelID": "jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M",
        "address": "P_address",
        "outpoint": "",
        "timeStamp": "",
        "signature": ""
    },
    "height": "12345",
    "txid": "abcd1234"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Only active Masternodes can register their PastelID.""",
             response_description="Details of the registered Masternode PastelID")
async def tickets_register_mnid(pastelid: str, passphrase: str, address: Optional[str] = None, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets("register", "mnid", pastelid, passphrase, address)
    return TicketsRegisterMnidResponse(**response)





@router.post("/tickets/register_id",
             response_model=TicketsRegisterIdResponse,
             tags=["Ticket Methods"],
             summary="Register Pastel ID identity",
             description="""Register a Pastel ID identity on the Pastel blockchain.

### Description
- This endpoint is used to register a new Pastel ID identity.
- The Pastel ID must be pre-generated and stored inside the node.

### Input Parameters
- `pastelid` (string, required): The Pastel ID. The Pastel ID must be generated and stored inside the node.
- `passphrase` (string, required): The passphrase to the private key associated with the Pastel ID and stored inside the node.
- `address` (string, required): The Pastel blockchain t-address to use for funding the transaction.

### Example Request
```json
{
    "pastelid": "jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M",
    "passphrase": "passphrase",
    "address": "tPmjPqWdUXD68JBTWYBTtqeCDwdFwwRjikg"
}
```

### Response
- Returns a JSON object containing the transaction ID and other details of the registered Pastel ID.

### Example Response
```json
{
    "ticket": {
        "type": "pastelid",
        "pastelID": "jXaShWhN...",
        "address": "tPmjPqWdUXD68...",
        "timeStamp": "2021-04-25T15:30:00",
        "signature": "HwMv...="
    },
    "height": "100000",
    "txid": "3a1b2c3d4e5f6789a0b1c2d3e4f5a678b9c0d1e2f3a4b5c6d7e8f9g0h1i2j3k4"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the registered Pastel ID")
async def tickets_register_id(request: TicketsRegisterIdRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets("register", "id", request.pastelid, request.passphrase, request.address)
    return TicketsRegisterIdResponse(**response)




@router.post("/tickets/register/nft",
             response_model=RegisterNFTTicketResponse,
             tags=["Ticket Methods"],
             summary="Register a new NFT ticket",
             description="""Register a new NFT ticket in the Pastel blockchain.

### Description
- This endpoint registers a new NFT ticket on the Pastel blockchain. It requires authentication via Pastel ID and passphrase.

### Input Parameters
- `nft_ticket`: Base64 encoded NFT ticket created by the creator.
- `signatures`: Signatures and Pastel IDs of the principal and verifying masternodes.
- `pastelid`: The registering masternode's Pastel ID.
- `passphrase`: Passphrase for the Pastel ID private key.
- `label`: Label for the ticket.
- `fee`: Storage fee for the NFT registration.
- `address`: (Optional) Pastel blockchain t-address for funding the registration.

### Example Request
```json
{
    "nft_ticket": "base64-encoded-ticket",
    "signatures": "signatures-json",
    "pastelid": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "passphrase",
    "label": "My NFT",
    "fee": 100,
    "address": "optional-address"
}
```

### Response
- Returns a JSON object with the transaction ID and ticket information.

### Example Response
```json
{
    "txid": "transaction-id",
    "height": 123456,
    "ticket": {
        "type": "nft-reg",
        "nft_ticket": {},
        ...
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used for registering new NFTs on the blockchain.""",
             response_description="Details of the registered NFT ticket")
async def register_nft_ticket(request: RegisterNFTTicketRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_nft(
        request.nft_ticket, request.signatures, request.pastelid,
        request.passphrase, request.label, request.fee,
        request.address
    )
    return RegisterNFTTicketResponse(**response)





@router.post("/tickets/registercollection",
             response_model=RegisterCollectionTicketResponse,
             tags=["Ticket Methods"],
             summary="Register a collection ticket",
             description="""Register a new collection ticket on the Pastel blockchain.

### Description
- This endpoint is used for registering a new collection ticket, representing a collection of NFTs on the Pastel blockchain.
- The ticket includes collection details like name, creator, authorized contributors, and metadata.

### Input Parameters
- `collection_ticket`: Base64 encoded collection ticket.
- `signatures`: Signatures and Pastel IDs of principal and verifying masternodes.
- `pastelid`: The Pastel ID of the registering masternode (MN1).
- `passphrase`: Passphrase for the private key associated with PastelID.
- `label`: A label for the ticket.
- `fee`: Storage fee for registering the ticket.
- `address`: (Optional) Pastel blockchain address for funding the registration.

### Example Request
```json
{
    "collection_ticket": "Base64EncodedTicket",
    "signatures": {
        "principal": {"PastelID": "Signature"},
        "mn2": {"PastelID": "Signature"},
        "mn3": {"PastelID": "Signature"}
    },
    "pastelid": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "yourPassphrase",
    "label": "MyCollection",
    "fee": 100,
    "address": "OptionalAddress"
}
```

### Response
- Returns details of the registered collection ticket including transaction ID, height, and ticket information.

### Example Response
```json
{
    "txid": "TransactionId",
    "height": 123456,
    "ticket": {
        ... // Detailed ticket information
    },
    ... // Other fields
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the registered collection ticket")
async def tickets_register_collection(request: RegisterCollectionTicketRequest,
                                      rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_collection(request.collection_ticket, request.signatures.dict(), 
                                                                request.pastelid, request.passphrase, request.label, 
                                                                request.fee, request.address)
    return RegisterCollectionTicketResponse(**response)





@router.post("/tickets/register/offer",
             response_model=TicketsRegisterOfferResponse,
             tags=["Ticket Methods"],
             summary="Register an offer ticket",
             description="""Register an offer ticket in the Pastel network.

### Description
- Registers an offer ticket on the Pastel network. This is used for offering an NFT for sale, either as the original creator or as the current owner if the NFT has been transferred.

### Input Parameters
- `txid`: The transaction ID of the ticket to offer. This is either the NFT Activation ticket (if the current owner is the original creator) or a Transfer ticket (if the current owner is not the original creator).
- `price`: The offer price in PSL.
- `pastel_id`: The Pastel ID of the current owner. This must be the same Pastel ID used to sign the ticket referred to by `txid`.
- `passphrase`: The passphrase to the private key associated with the creator's Pastel ID.
- `valid_after`: (Optional) The block height after which this offer ticket will become active.
- `valid_before`: (Optional) The block height after which this offer ticket is no longer valid.
- `copy_number`: (Optional) If present, will replace the original not yet accepted Offer ticket with this copy number.
- `address`: (Optional) The Pastel blockchain address to use for funding the registration.
- `intended_for`: (Optional) The Pastel ID of the intended recipient of the offer.

### Example Request
```json
{
    "txid": "txid_value",
    "price": 100000,
    "pastel_id": "pastel_id_value",
    "passphrase": "passphrase_value",
    "valid_after": 0,
    "valid_before": 0,
    "copy_number": 0,
    "address": "address_value",
    "intended_for": "intended_for_value"
}
```

### Response
- Returns a JSON object containing details of the registered offer ticket.

### Example Response
```json
{
    "ticket": {
        "type": "offer",
        "pastelID": "pastel_id_value",
        "txid": "txid_value",
        "copy_number": "0",
        "asked_price": "100000",
        "valid_after": "0",
        "valid_before": "0",
        "signature": "signature_value"
    },
    "height": "block_height_value",
    "txid": "txid_value"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the registered offer ticket")
async def tickets_register_offer(request: TicketsRegisterOfferRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_offer(
        request.txid, request.price, request.pastel_id, request.passphrase, 
        request.valid_after, request.valid_before, request.copy_number, 
        request.address, request.intended_for)
    return response





@router.post("/tickets/register/accept",
             response_model=TicketsRegisterAcceptResponse,
             tags=["Ticket Methods"],
             summary="Register an accept ticket",
             description="""Register an accept ticket for a specific offer on the Pastel network.

### Description
- This endpoint is used to accept an offer for a ticket on the Pastel network.
- It creates an accept ticket that indicates the acceptance of an offer.

### Input Parameters
- `offer_txid`: The transaction ID of the offer ticket to accept.
- `price`: The accepted price in PSL. It should be equal to or more than the asked price in the offer ticket.
- `pastel_id`: The Pastel ID of the new owner.
- `passphrase`: The passphrase to the private key associated with the creator's Pastel ID.
- `address`: (Optional) The Pastel blockchain t-address to use for funding the registration.

### Example Request
```json
{
    "offer_txid": "example_txid",
    "price": 100000,
    "pastel_id": "example_pastel_id",
    "passphrase": "example_passphrase",
    "address": "example_address"
}
```

### Response
- Returns a JSON object containing the ticket details, block height, and transaction ID.

### Example Response
```json
{
    "ticket": {
        "type": "accept",
        "pastelID": "example_pastel_id",
        "offer_txid": "example_txid",
        "price": 100000,
        "signature": "example_signature"
    },
    "height": "example_height",
    "txid": "example_txid"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Details of the registered accept ticket")
async def tickets_register_accept(request: TicketsRegisterAcceptRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_accept(request.offer_txid, request.price, request.pastel_id, request.passphrase, request.address)
    return TicketsRegisterAcceptResponse(**response)




@router.post("/tickets/register/transfer",
             response_model=RegisterTransferTicketResponse,
             tags=["Ticket Methods"],
             summary="Register a transfer ticket",
             description="""Register a transfer ticket in the Pastel network.

### Description
- This endpoint registers a Transfer ticket, completing the transfer of an NFT from one owner to another in a secure manner.

### Input Parameters
- `offer_txid`: The transaction ID of the Offer ticket.
- `accept_txid`: The transaction ID of the Accept ticket.
- `pastel_id`: The Pastel ID of the new owner. Must match the Pastel ID used to sign the Accept ticket.
- `passphrase`: Passphrase of the private key associated with the new owner's Pastel ID.
- `address`: (Optional) The Pastel blockchain t-address to use for funding the registration.

### Request JSON Format
```json
{
    "offer_txid": "offer_transaction_id",
    "accept_txid": "accept_transaction_id",
    "pastel_id": "new_owner_pastel_id",
    "passphrase": "private_key_passphrase",
    "address": "funding_t_address"
}
```

### Response
- Returns a JSON object containing details of the registered transfer ticket.

### Example Response
```json
{
    "ticket": {
        "type": "transfer",
        "pastelID": "new_owner_pastel_id",
        "offer_txid": "offer_transaction_id",
        "accept_txid": "accept_transaction_id",
        "item_txid": "item_transaction_id",
        "registration_txid": "registration_transaction_id",
        "signature": "signature_value"
    },
    "height": "block_height",
    "txid": "transaction_id"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is used to securely transfer ownership of NFTs within the Pastel network.""",
             response_description="Details of the registered transfer ticket")
async def register_transfer_ticket(request: RegisterTransferTicketRequest, 
                                   rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    ticket_data = await rpc_connection.tickets("register", "transfer", 
                                               request.offer_txid, 
                                               request.accept_txid, 
                                               request.pastel_id, 
                                               request.passphrase, 
                                               request.address)
    return RegisterTransferTicketResponse(**ticket_data)





@router.post("/tickets/register_royalty",
             response_model=RegisterRoyaltyTicketResponse,
             tags=["Ticket Methods"],
             summary="Register new change payee of the NFT royalty ticket",
             description="""Register a new change payee of the NFT royalty ticket. If successful, the method returns the transaction ID.

### Description
- This endpoint registers a new recipient for NFT royalty payments, effectively changing the payee.
- It requires the transaction ID of the NFT register ticket, PastelIDs of the new and current royalty recipients, and the passphrase for the old PastelID.

### Input Parameters
- `nft_txid` (string, required): The txid of the NFT register ticket.
- `new_pastelid` (string, required): The PastelID of the new royalty recipient.
- `old_pastelid` (string, required): The PastelID of the current royalty recipient.
- `passphrase` (string, required): The passphrase to the private key associated with 'old-pastelid'.
- `address` (string, optional): The Pastel blockchain t-address for funding the registration.

### Example Request
```json
{
    "nft_txid": "907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440",
    "new_pastelid": "newPastelID123",
    "old_pastelid": "oldPastelID456",
    "passphrase": "yourPassphrase",
    "address": "P_address"
}
```

### Response
- Returns a JSON object containing the details of the registered NFT royalty ticket.

### Example Response
```json
{
    "txid": "generatedTxId",
    "height": 123456,
    "ticket": {
        "type": "nft-royalty",
        "version": 1,
        "pastelID": "oldPastelID456",
        "new_pastelID": "newPastelID123",
        "nft_txid": "907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440",
        "signature": "signatureString"
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the registered NFT royalty ticket")
async def register_royalty_ticket(request: RegisterRoyaltyTicketRequest,
                                  rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_royalty(request.nft_txid, request.new_pastelid, 
                                                             request.old_pastelid, request.passphrase, request.address)
    return RegisterRoyaltyTicketResponse(**response)




@router.post("/tickets/register/down",
             response_model=TicketsRegisterDownResponse,
             tags=["Ticket Methods"],
             summary="Register a Take Down Request Ticket",
             description="""Register a take down request ticket in the Pastel Network.

### Description
- This endpoint registers a take down request ticket, which is a request to take down a piece of content. It returns the transaction ID if successful.

### Input Parameters
- `txid`: The transaction ID.
- `pastelid`: The Pastel ID. Note: Pastel ID must be generated and stored inside the node.
- `passphrase`: The passphrase to the private key associated with the Pastel ID.
- `address`: (Optional) The Pastel blockchain t-address to use for funding the registration.

### Example Request
```json
{
    "txid": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "pastelid": "your_pastel_id",
    "passphrase": "your_passphrase",
    "address": "optional_pastel_address"
}
```

### Response
- Returns a JSON object with the details of the registered take down request ticket.

### Example Response
```json
{
    "ticket": {
        "type": "pastelid",
        "pastelID": "your_pastel_id",
        "timeStamp": "timestamp",
        "signature": "signature"
    },
    "height": "block_height",
    "txid": "transaction_id"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are incorrect.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is used for registering take down requests in the Pastel Network.""",
             response_description="Details of the registered take down request ticket")
async def tickets_register_down(txid: str, pastelid: str, passphrase: str, address: Optional[str] = None, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.tickets("register", "down", txid, pastelid, passphrase, address)
    return TicketsRegisterDownResponse(**result)





@router.post("/tickets/register/username",
             response_model=RegisterUsernameResponse,
             tags=["Ticket Methods"],
             summary="Register a Username Change Request ticket",
             description="""Register a Username Change Request ticket with the specified username and Pastel ID.

### Description
- This endpoint registers a new username change request ticket in the Pastel network.
- The Pastel ID must already exist and be stored in the node.

### Input Parameters
- `username`: The username to be associated with the specified Pastel ID.
- `pastel_id`: The Pastel ID with which the username is to be associated.
- `passphrase`: The passphrase to access the private key associated with the Pastel ID.
- `address`: (Optional) The Pastel blockchain address to fund the registration.

### Example Request
```json
{
    "username": "example_user",
    "pastel_id": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "passphrase",
    "address": "P_address"
}
```

### Response
- Returns a JSON object containing details of the username registration ticket, including the transaction ID.

### Example Response
```json
{
    "ticket": {
        "type": "username",
        "pastelID": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
        "username": "example_user",
        "fee": "0.01",
        "signature": "..."
    },
    "height": "123456",
    "txid": "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is crucial for users who wish to change their username associated with their Pastel ID.""",
             response_description="Details of the registered username change request ticket")
async def register_username(request: RegisterUsernameRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.tickets_register_username(request.username, request.pastel_id, request.passphrase, request.address)
    return RegisterUsernameResponse(ticket=response["ticket"], height=response["height"], txid=response["txid"])





@router.post("/tickets/register/ethereumaddress",
             response_model=TicketsRegisterEthereumAddressResponse,
             tags=["Ticket Methods"],
             summary="Register Ethereum Address Change Request",
             description="""Register an Ethereum Address Change Request ticket.

### Description
- This endpoint registers a change of Ethereum address associated with a given Pastel ID.

### Input Parameters
- `ethereum_address`: The Ethereum address to be mapped with the Pastel ID.
- `pastel_id`: The Pastel ID.
- `passphrase`: The passphrase to the private key associated with the Pastel ID.
- `address` (optional): The Pastel blockchain t-address for funding the registration.

### Example Request
```json
{
    "ethereum_address": "0x863c30dd122a21f815e46ec510777fd3e3398c26",
    "pastel_id": "jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF",
    "passphrase": "passphrase",
    "address": "optional_t_address"
}
```

### Response
- Returns a JSON object containing the details of the registered Ethereum address change request.

### Example Response
```json
{
    "ticket": {
        "type": "ethereumAddress",
        "pastelID": "jXYqZNPj...",
        "ethereumAddress": "0x863c30d...",
        "fee": "0.1",
        "signature": "..."
    },
    "height": "123456",
    "txid": "xyz123abc..."
}
```

### Possible Errors
- HTTP 400: Bad Request if input parameters are incorrect.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Details of the registered Ethereum address change request")
async def tickets_register_ethereum_address(request: TicketsRegisterEthereumAddressRequest,
                                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    params = [request.ethereum_address, request.pastel_id, request.passphrase]
    if request.address:
        params.append(request.address)
    response = await rpc_connection.tickets("register", "ethereumaddress", *params)
    return TicketsRegisterEthereumAddressResponse(**response)





@router.post("/tickets/register_action",
             response_model=ActionTicketResponse,
             tags=["Ticket Methods"],
             summary="Register new Action ticket",
             description="""Register a new Action ticket on the Pastel blockchain.

### Description
- This endpoint is used to register a new Action ticket, supporting action types like 'sense' and 'cascade'.
- The ticket includes details like action type, caller PastelID, block number, and application-specific data.

### Input Parameters
- `action_ticket`: Base64 encoded Action ticket.
- `signatures`: Signatures and Pastel IDs of the principal and verifying masternodes.
- `pastelid`: The Pastel ID of the registering masternode.
- `passphrase`: The passphrase to the private key associated with Pastel ID.
- `label`: A label for the ticket.
- `fee`: The storage fee.
- `address`: (Optional) Pastel blockchain t-address for funding.

### Example Request
```json
{
    "action_ticket": "<encoded-ticket>",
    "signatures": "<signatures-json>",
    "pastelid": "jXYqZNPj...",
    "passphrase": "passphrase",
    "label": "label",
    "fee": 100,
    "address": "P_address"
}
```

### Response
- Returns information about the registered Action ticket including transaction ID, height, and ticket details.

### Example Response
```json
{
    "txid": "transaction_id",
    "height": 123456,
    "ticket": {
        // Ticket details
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the registered Action ticket")
async def register_action_ticket(request: ActionTicketRequest, 
                                 rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Extract parameters from the request
    action_ticket = request.action_ticket
    signatures = request.signatures
    pastelid = request.pastelid
    passphrase = request.passphrase
    label = request.label
    fee = request.fee
    address = request.address

    # Call the RPC method
    response = await rpc_connection.tickets_register_action(action_ticket, signatures, pastelid, passphrase, label, fee, address)

    # Construct and return the response
    return ActionTicketResponse(txid=response['txid'],
                                height=response['height'],
                                ticket=response['ticket'])
    
    
    
    

@router.post("/governance",
             response_model=GovernanceResponse,
             tags=["Utility Methods"],
             summary="Cast a vote or list governance tickets",
             description="""Perform governance-related actions such as voting for tickets or listing tickets/winners.

### Description
- This endpoint allows casting votes for governance tickets or listing all governance tickets or winners.

### Input Parameters
- `mode`: 'ticket' or 'list' to specify the action.
- `subcommand`: Depending on the mode, additional parameters for the action.

### Example Request
- `POST /governance`
  ```json
  {
      "mode": "ticket",
      "subcommand": "add",
      "parameters": ["address", 10, "note", "yes"]
  }
  ```

### Response
- Returns a JSON object containing the result of the governance action.

### Example Response
  ```json
  {
      "result": "success",
      "ticketId": "ticket_id_here"
  }
  ```

### Possible Errors
- HTTP 400: Bad Request if input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used for participating in the governance of the Pastel Network.""")
async def governance_action(mode: str, subcommand: str, parameters: List[Union[str, int]], rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if mode == "ticket":
        # Handle ticket actions
        pass  # Replace with actual implementation
    elif mode == "list":
        # Handle list actions
        pass  # Replace with actual implementation
    else:
        logger.error("Invalid mode specified")    
        
        
        
        
        
@router.get("/masternodelist",
            response_model=MasternodeListResponse,
            tags=["Supernode Methods"],
            summary="Get a list of masternodes in different modes",
            description="""Get a list of masternodes in different modes.

### Description
- Retrieves information about masternodes based on the specified mode. Each mode provides different types of data about the masternodes.

### Input Parameters
- `mode` (string, optional): The mode to run the list in. Defaults to 'status'. Available modes:
  - `activeseconds`: Number of seconds the masternode has been recognized as enabled.
  - `addr`: IP address associated with a masternode.
  - `full`: Info in the format 'status protocol payee lastseen activeseconds lastpaidtime lastpaidblock IP'.
  - `info`: Info in the format 'status protocol payee lastseen activeseconds sentinelversion sentinelstate IP'.
  - `lastpaidblock`: The last block height a node was paid on the network.
  - `lastpaidtime`: The last time a node was paid on the network.
  - `lastseen`: Timestamp of when a masternode was last seen on the network.
  - `payee`: Pastel address associated with a masternode.
  - `protocol`: Protocol of a masternode.
  - `pubkey`: Masternode (not collateral) public key.
  - `rank`: Rank of a masternode based on current block.
  - `status`: Masternode status (e.g., ENABLED, EXPIRED).
  - `extra`: PASTEL data associated with the masternode.
- `filter` (string, optional): Filter results. Partial match by outpoint by default in all modes, additional matches in some modes are also available.
- `allnodes` (string, optional): Force to show all masternodes including expired NEW_START_REQUIRED.

### Example Request
- `GET /masternodelist?mode=full&filter=192.168.0.1`

### Response
- Depending on the mode, returns a JSON object containing various information about masternodes.

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Information about masternodes based on the selected mode")
async def masternodelist(mode: str = "status", filter: str = "", allnodes: str = "",
                         rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.masternodelist(mode, filter, allnodes)
    return response




        
        
@router.get("/masternode/outputs",
            response_model=MasternodeOutputsResponse,
            tags=["Supernode Methods"],
            summary="List masternode outputs",
            description="""List masternode outputs (collateral txid+index).

### Description
- This endpoint lists possible coin candidates for masternode collateral, 
  including transaction ID and index of each output.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /masternode/outputs`

### Response
- Returns a JSON object containing the masternode outputs.

### Example Response
```json
{
    "outputs": {
        "txid1": "index1",
        "txid2": "index2",
        ...
    }
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="List of masternode outputs")
async def list_masternode_outputs(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    outputs = await rpc_connection.masternode_outputs()
    return MasternodeOutputsResponse(outputs=outputs)




        

@router.post("/masternode/init",
             response_model=MasternodeInitResponse,
             tags=["Supernode Methods"],
             summary="Initialize masternode",
             description="""Initialize masternode with existing outpoint (collateral txid & index).

### Description
- Initializes a masternode with the provided collateral from the local wallet. 
  Generates new Pastel ID, registers mnid, and generates masternode private key.

### Input Parameters
- `passphrase`: Passphrase for new PastelID.
- `txid`: ID of transaction with the collateral amount.
- `index`: Index in the transaction with the collateral amount.

### Request JSON Format
```json
{
    "passphrase": "secure-passphrase",
    "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
    "index": 4
}
```

### Response
- Returns a JSON object with the generated and registered Pastel ID and other key details.

### Example Response
```json
{
    "mnid": "Generated and registered Pastel ID",
    "legRoastKey": "Generated and registered LegRoast private key",
    "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
    "outIndex": 4,
    "privKey": "Generated masternode private key"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Masternode initialization details")
async def initialize_masternode(request: MasternodeInitRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.masternode_init(request.passphrase, request.txid, request.index)
    return MasternodeInitResponse(**response)        







@router.post("/masternode/make_conf",
             response_model=MasternodeMakeConfResponse,
             tags=["Supernode Methods"],
             summary="Create Masternode Configuration",
             description="""Create masternode configuration in JSON format. 

### Description
- Generates MasterNode Private Key (mnPrivKey) and registers MasterNode PastelID (extKey).
- If collateral txid and index are not provided, searches for the first available non-locked outpoint with the correct amount (1000000 PSL).

### Input Parameters
- `alias`: Local alias (name) of the Master Node.
- `mn_address`: The address and port of the Master Node's cNode.
- `ext_address`: The address and port of the Master Node's Storage Layer.
- `ext_p2p`: The address and port of the Master Node's Kademlia point.
- `passphrase`: Passphrase for new Pastel ID.
- `txid`: (Optional) ID of transaction with the collateral amount.
- `index`: (Optional) Index in the transaction with the collateral amount.

### Example Request
```json
{
    "alias": "myMN",
    "mn_address": "127.0.0.1:9933",
    "ext_address": "127.0.0.1:4444",
    "ext_p2p": "127.0.0.1:5545",
    "passphrase": "securepassphrase",
    "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
    "index": 4
}
```

### Response
- Returns a JSON object with the Masternode configuration details.

### Example Response
```json
{
    "alias": "myMN",
    "config": {
        "mn_address": "127.0.0.1:9933",
        "ext_address": "127.0.0.1:4444",
        "ext_p2p": "127.0.0.1:5545",
        "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
        "out_index": "4",
        "mn_priv_key": "generatedPrivateKey",
        "ext_key": "generatedPastelID"
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is used for setting up new Masternodes on the network.""",
             response_description="Masternode configuration details in JSON format")
async def masternode_make_conf(request: MasternodeMakeConfRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    masternode_config = await rpc_connection.masternode_make_conf(
        request.alias,
        request.mn_address,
        request.ext_address,
        request.ext_p2p,
        request.passphrase,
        request.txid,
        request.index
    )
    return MasternodeMakeConfResponse(alias=request.alias, config=masternode_config)






@router.post("/masternode/clear-cache",
             response_model=MasternodeClearCacheResponse,
             tags=["Supernode Methods"],
             summary="Clear Masternode Cache Items",
             description="""Clear specific Masternode cache items. 

### Description
- This endpoint clears specific cache items related to Masternodes in the network. The cache items include the masternode list, seen masternodes, recovery cache, asked masternode cache, and historical top masternodes cache.

### Input Parameters
- `cache_item`: A string specifying the cache item to clear. Possible values are 'all', 'mns', 'seen', 'recovery', 'asked', 'top-mns'.

### Example Request
- `POST /masternode/clear-cache`
  ```json
  {
      "cache_item": "mns"
  }
  ```

### Response
- Returns a JSON object indicating the status of the cache clearing operation.

### Example Response
```json
{
    "status": "Cache cleared successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if an invalid cache item is provided.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is primarily used for network maintenance and troubleshooting.""",
             response_description="Status of the cache clearing operation")
async def masternode_clear_cache(cache_item: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if cache_item not in ['all', 'mns', 'seen', 'recovery', 'asked', 'top-mns']:
        logger.error("Invalid cache item specified")
    await rpc_connection.masternode_clear_cache(cache_item)
    return MasternodeClearCacheResponse(status="Cache cleared successfully")






@router.post("/masternode_pose_ban_score",
             response_model=MasterNodePoseBanScoreResponse,
             tags=["Supernode Methods"],
             summary="Manage MasterNode PoSe Ban Score",
             description="""Manage the Proof-Of-Service (PoSe) ban score for a MasterNode.

### Description
- This endpoint allows getting or incrementing the PoSe ban score of a specified MasterNode.
- The MasterNode is identified by the transaction ID (txid) and index of its collateral transaction.

### Input Parameters
- `command`: The operation to perform - "get" to retrieve the current score or "increment" to increase it.
- `txid`: The transaction ID of the MasterNode's collateral transaction.
- `index`: The index of the collateral output in the transaction.

### Example Request
```json
{
    "command": "get",
    "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
    "index": 1
}
```

### Response
- Returns a JSON object containing the MasterNode's PoSe ban score, ban status, and ban height if applicable.

### Example Response
```json
{
    "txid": "bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726",
    "index": 1,
    "pose_ban_score": 10,
    "pose_banned": false
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="PoSe ban score and status of the MasterNode")
async def masternode_pose_ban_score(request: MasterNodePoseBanScoreRequest, 
                                    rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.masternode_pose_ban_score(request.command, request.txid, request.index)
    return MasterNodePoseBanScoreResponse(**result)






@router.post("/masternode/message",
             response_model=MasternodeMessageResponse,
             tags=["Supernode Methods"],
             summary="Interact with Masternode messages",
             description="""Allows sending, listing, printing, and signing messages using Masternode.

### Description
- This endpoint interacts with Masternode messages based on the specified operation.

### Input Parameters
- `operation`: The operation to perform (`send`, `list`, `print`, `sign`).
- `pub_key`: The Masternode public key (required for `send` operation).
- `message`: The message text (required for `send` and `sign` operations).
- `message_id`: The message ID (required for `print` operation).
- `additional_param`: Additional parameter (optional, used in `sign` operation).

### Example Request
- `POST /masternode/message`

### Response
- Returns a JSON object containing the result of the operation.

### Example Response
```json
{
    "result": "Success",
    "signature": "abc123",
    "pubkey": "def456",
    "messages": {"msg1": "Message content"}
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Result of the Masternode message operation")
async def masternode_message(request: MasternodeMessageRequest,
                             rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if request.operation == "send":
        # Logic for sending a message
        return {"result": "Message sent"}
    elif request.operation == "list":
        # Logic for listing messages
        return {"messages": {"msg1": "Message content"}}
    elif request.operation == "print":
        # Logic for printing a message
        return {"result": "Message content"}
    elif request.operation == "sign":
        # Logic for signing a message
        return {"signature": "abc123", "pubkey": "def456"}
    else:
        logger.error("Invalid operation")
        
        



@router.post("/masternode/command",
             response_model=MasternodeCommandResponse,
             tags=["Supernode Methods"],
             summary="Execute masternode related actions",
             description="""Execute various masternode related actions based on the provided command.

### Description
- This endpoint allows for executing different masternode related commands such as count, current, winner, genkey, and others.

### Input Parameters
- `command`: The masternode command to execute.
- `additional_args`: Additional arguments required for specific commands.

### Example Request
```json
{
    "command": "count",
    "additional_args": {"count_type": "enabled"}
}
```

### Response
- Returns a JSON object containing the result based on the executed command.

### Example Response
```json
{
    "count": 150
}
```

### Possible Errors
- HTTP 400: Bad Request if the command or additional arguments are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Result of the masternode command")
async def execute_masternode_command(request: MasternodeCommandRequest, 
                                     rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Implement logic to call the appropriate RPC method based on the command
    if request.command == "count":
        response = await rpc_connection.masternode("count", **request.additional_args)
        return MasternodeCountResponse(count=response)
    elif request.command == "winner":
        # Example logic for 'winner' command
        response = await rpc_connection.masternode("winner", **request.additional_args)
        return MasternodeWinnersResponse(winners=response)
    elif request.command == "genkey":
        # Example logic for 'genkey' command
        response = await rpc_connection.masternode("genkey", **request.additional_args)
        return MasternodeGenKeyResponse(private_key=response)
    # Add other command cases as needed
    else:
        logger.error("Invalid masternode command")
        
        
        


@router.get("/tickets/find",
            response_model=FindTicketsResponse,
            tags=["Ticket Methods"],
            summary="Find Pastel tickets",
            description="""Find various types of Pastel tickets based on a given key.

### Description
- This endpoint searches for different types of Pastel tickets in the blockchain.

### Input Parameters
- `ticket_type`: Type of the ticket to find (e.g., 'id', 'nft', 'act', etc.).
- `key`: The key to use for ticket search.

### Example Request
- `GET /tickets/find?ticket_type=nft&key=exampleKey`

### Response
- Returns a JSON object or an array of objects containing the ticket data.

### Example Response
```json
[
    {
        "ticket_id": "exampleTicketId",
        "ticket_data": {
            "field1": "value1",
            "field2": "value2"
            // ... other ticket data fields
        }
    }
    // ... other tickets
]
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The structure and type of ticket returned depend on the ticket type being searched.""",
            response_description="Ticket data in JSON format")
async def tickets_find(ticket_type: str, key: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    ticket_data = await rpc_connection.tickets_find(ticket_type, key)
    return ticket_data






@router.get("/getnewaddress",
            response_model=GetNewAddressResponse,
            tags=["Utility Methods"],
            summary="Generate a new Pastel address",
            description="""Generate a new Pastel address for receiving payments.

### Description
- This endpoint creates a new Pastel address which can be used to receive payments.
- The new address is automatically associated with the default account.

### Input Parameters
- `account`: (string, optional) DEPRECATED. The account name for the address. It must be the empty string `""` for the default account. Any other value will result in an error.

### Example Request
- `GET /getnewaddress?account=""`

### Response
- Returns a JSON object containing the new Pastel address in string format.

### Example Response
```json
{
    "address": "pZb7J2fg9BpM1Kj3n3FjR5Bn25S55hKx2x"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The generated address is added to the wallet and can be used immediately for receiving funds.""",
            response_description="The new Pastel address")
async def get_new_address(account: Optional[str] = "", 
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    address = await rpc_connection.getnewaddress(account)
    return GetNewAddressResponse(address=address)        





@router.get("/getaccountaddress",
            response_model=GetAccountAddressResponse,
            tags=["Wallet Methods"],
            summary="Get the current Pastel address for receiving payments",
            description="""Get the current Pastel address for receiving payments to a specified account.

### Description
- This endpoint returns the current Pastel address for receiving payments to the specified account. 
- Note: This method is deprecated.

### Input Parameters
- `account`: (string, required) MUST be set to the empty string "" to represent the default account. Passing any other string will result in an error.

### Example Request
- `GET /getaccountaddress?account=""`

### Response
- Returns a JSON object containing the Pastel address for the account.

### Example Response
```json
{
    "zcashaddress": "t1KSLVSVdZD1Cz8TCr7FBG8m5xKwKMBrMT6"
}
```

### Possible Errors
- HTTP 400: Bad Request if an invalid account name is provided.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is deprecated and may be removed in future versions.""",
            response_description="Pastel address for the account")
async def get_account_address(account: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if account != "":
        logger.error("Invalid account name. Account must be an empty string.")
    zcashaddress = await rpc_connection.getaccountaddress(account)
    return GetAccountAddressResponse(zcashaddress=zcashaddress)






@router.get("/getrawchangeaddress",
            response_model=str,
            tags=["Raw Transaction Methods"],
            summary="Get a new Pastel address for receiving change",
            description="""Get a new Pastel address for receiving change. This is for use with raw transactions, NOT for normal use.

### Description
- This endpoint generates and returns a new Pastel address that can be used for receiving change in raw transactions.
- It is important to note that this address should not be used for regular transactions.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getrawchangeaddress`

### Response
- Returns a string representing the new Pastel address.

### Example Response
```json
"mnX4Ph6uhz2ez5y9Yb9hWPiPH5G9Wp2VWJ"
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- RPC_WALLET_KEYPOOL_RAN_OUT: Error message if the keypool has run out. In this case, the `keypoolrefill` RPC method should be called first.

### Note
- This address should only be used for change in raw transactions and not for general transaction purposes.""",
            response_description="The new Pastel address for receiving change")
async def get_raw_change_address(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    new_address = await rpc_connection.getrawchangeaddress()
    return new_address





@router.get("/getaccount/{zcashaddress}", 
            response_model=GetAccountResponse, 
            tags=["Blockchain Methods"],
            summary="Get the account associated with a Pastel address",
            description="""Retrieve the account name associated with the given Pastel address. 

### Description
- This endpoint is used to get the account name linked to a specific Pastel address. It is important to note that this method is marked as deprecated.

### Input Parameters
- `zcashaddress`: A string representing the Pastel address for the account lookup.

### Example Request
- `GET /getaccount/PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n`

### Response
- Returns a JSON object containing the account name associated with the given Pastel address.

### Example Response
```json
{
    "account_name": "exampleAccountName"
}
```

### Possible Errors
- HTTP 400: Bad Request if the address is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is deprecated and might be removed in future versions of the Pastel network.""",
            response_description="Account name associated with the Pastel address")
async def get_account(zcashaddress: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    account_name = await rpc_connection.getaccount(zcashaddress)
    return GetAccountResponse(account_name=account_name)







@router.post("/setaccount",
             response_model=SetAccountResponse,
             tags=["Control Methods"],
             summary="Associate a Pastel address with an account",
             description="""DEPRECATED. Sets the account associated with the given address.

### Description
- This endpoint is used to associate a Pastel address with an account.
- The `account` parameter must be set to an empty string "" to represent the default account. Passing any other string will result in an error.

### Input Parameters
- `zcashaddress` (string, required): The Pastel address to be associated with an account.
- `account` (string, required): The account name. Must be an empty string for the default account.

### Example Request
```json
{
    "zcashaddress": "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n",
    "account": ""
}
```

### Response
- Returns a JSON object indicating success or failure of the operation.

### Example Response
```json
{
    "success": true,
    "message": "Account associated successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Result of the account association operation")
async def set_account(request: SetAccountRequest, 
                      rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    try:
        await rpc_connection.setaccount(request.zcashaddress, request.account)
        return SetAccountResponse(success=True, message="Account associated successfully")
    except Exception as e:
        return SetAccountResponse(success=False, message=str(e))
    
    
    
    
    
@router.get("/getaddressesbyaccount",
            response_model=List[str],
            tags=["Wallet Methods"],
            summary="Get addresses by account",
            description="""Get the list of addresses for the given account.

### Description
- **DEPRECATED**: This endpoint is deprecated and might be removed in future versions. It returns the list of addresses associated with a specified account.
- The account argument must be set to the empty string `""` to represent the default account. Passing any other string will result in an error.

### Input Parameters
- `account`: (string, required) The account name. Must be set to `""` for the default account.

### Example Request
- `GET /getaddressesbyaccount?account=""`

### Response
- Returns a JSON array of strings, each representing a Pastel address associated with the given account.

### Example Response
```json
[
  "paxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "payyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
]
```

### Possible Errors
- HTTP 400: Bad Request if the account parameter is not the empty string.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is primarily used for wallet management and account balance tracking.""",
            response_description="List of Pastel addresses associated with the given account")
async def get_addresses_by_account(account: str, 
                                   rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    addresses = await rpc_connection.getaddressesbyaccount(account)
    return addresses







@router.post("/sendtoaddress",
             response_model=SendToAddressResponse,
             tags=["Utility Methods"],
             summary="Send an amount to a given address",
             description="""Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001.

### Description
- Send Pastel to a specified address with optional comments and fee deduction options.
- By default, the change is sent to the original address unless specified otherwise.

### Input Parameters
- `t_address` (string, required): The Pastel address to send to.
- `amount` (numeric, required): The amount in Pastel to send. e.g., 0.1
- `comment` (string, optional): A comment for transaction record-keeping, not part of the transaction.
- `comment_to` (string, optional): A comment about the recipient, for record-keeping.
- `subtract_fee_from_amount` (boolean, optional, default=false): If true, the fee is deducted from the amount being sent.
- `change_address` (string, optional, default="original"): Address for sending the change. Can be "original", "new", or a specific Pastel t-address.

### Example Request
- `POST /sendtoaddress` with JSON body:
```json
{
    "t_address": "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n",
    "amount": 0.1,
    "comment": "donation",
    "comment_to": "seans outpost",
    "subtract_fee_from_amount": true,
    "change_address": "new"
}
```

### Response
- Returns the transaction ID of the completed transaction.

### Example Response
```json
{
    "transaction_id": "b6a19f8fb228edf47e93a2b3d3ad8b1b4f7d8eac4fc0f3c6d3e2c463d7b9fc6f"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="The transaction ID of the sent transaction")
async def send_to_address(request: SendToAddressRequest,
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.sendtoaddress(request.t_address, request.amount, request.comment, 
                                                  request.comment_to, request.subtract_fee_from_amount, 
                                                  request.change_address)
    return SendToAddressResponse(transaction_id=response)






@router.get("/listaddressgroupings",
            response_model=AddressGroupingsResponse,
            tags=["Blockchain Methods"],
            summary="List groups of addresses with common ownership",
            description="""List groups of addresses which have had their common ownership made public by common use as inputs or as the resulting change in past transactions.

### Description
- This endpoint returns groups of addresses that are grouped together based on their common ownership, which is inferred from their usage in past transactions.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Response
- Returns a JSON object containing groups of addresses. Each group is a list of addresses, where each address is represented by its Pastel address, the amount associated with it, and optionally the account name.

### Example Response
```json
{
    "groupings": [
        [
            {"address": "pasteladdress1", "amount": 10.5, "account": "myaccount"},
            {"address": "pasteladdress2", "amount": 2.3}
        ],
        [
            {"address": "pasteladdress3", "amount": 5.0}
        ]
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for understanding wallet organization and for tracking common ownership of addresses.""",
            response_description="List of address groupings")
async def list_address_groupings(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    groupings = await rpc_connection.listaddressgroupings()
    return AddressGroupingsResponse(groupings=groupings)






@router.get("/listaddressamounts",
            response_model=ListAddressAmountsResponse,
            tags=["Wallet Methods"],
            summary="List balance on each address",
            description="""List the balance on each address in the wallet.

### Description
- This endpoint lists the balances associated with each address in the wallet.
- It allows filtering of addresses based on whether they have a balance and the type of ownership (all, watchOnly, spendableOnly).

### Input Parameters
- `include_empty`: (bool, optional, default=false) Include addresses with empty balances.
- `ismine_filter`: (str, optional, default=all) Filter for "all", "watchOnly", or "spendableOnly" addresses.

### Example Request
- `GET /listaddressamounts?include_empty=true&ismine_filter=spendableOnly`

### Response
- Returns a JSON object with addresses as keys and their corresponding balances as values.

### Example Response
```json
{
    "balances": {
        "t1XYZ...abc": 0.5,
        "t1ABC...xyz": 1.2
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for obtaining an overview of wallet balances distributed across different addresses.""",
            response_description="A dictionary of addresses and their corresponding balances")
async def list_address_amounts(request: ListAddressAmountsRequest = Depends(),
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.listaddressamounts(request.include_empty, request.ismine_filter)
    return ListAddressAmountsResponse(balances=response)






@router.post("/signmessage",
             response_model=SignMessageResponse,
             tags=["Utility Methods"],
             summary="Sign a message with the private key of a t-addr",
             description="""Sign a message using the private key of a transparent address (t-addr).

### Description
- This endpoint allows you to sign a message with the private key of a specified transparent address. 
- It's commonly used for proving ownership of a specific address.

### Input Parameters
- `t_addr`: (string, required) The transparent address to use for the private key.
- `message`: (string, required) The message to create a signature of.

### Example Request
```json
{
    "t_addr": "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n",
    "message": "my message"
}
```

### Response
- Returns a JSON object containing the base 64 encoded signature of the message.

### Example Response
```json
{
    "signature": "H6sliPZjFfS36emU8XThY6UvZHxY..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid or the address is not correct.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The address must be a valid t-addr and the wallet must be unlocked for this operation.""",
             response_description="Base 64 encoded signature of the message")
async def sign_message(request: SignMessageRequest,
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    signature = await rpc_connection.signmessage(request.t_addr, request.message)
    return SignMessageResponse(signature=signature)






@router.get("/getreceivedbyaddress",
            response_model=GetReceivedByAddressResponse,
            tags=["Blockchain Methods"],
            summary="Get the total amount received by a Pastel address",
            description="""Get the total amount received by the given Pastel address in transactions with at least a specified number of confirmations.

### Description
- This endpoint returns the total amount received by a specific Pastel address in transactions that are confirmed at least a specified number of times.

### Input Parameters
- `zcashaddress`: The Pastel address for transactions.
- `minconf`: (Optional) The minimum number of confirmations for transactions. Defaults to 1.

### Example Request
- `GET /getreceivedbyaddress?zcashaddress=PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n&minconf=1`

### Response
- Returns a JSON object containing the total amount received at the given address.

### Example Response
```json
{
    "total_amount": 10.5
}
```

### Possible Errors
- HTTP 400: Bad Request if the address is invalid or not provided.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for retrieving the total amount received at a particular Pastel address.""",
            response_description="Total amount received at the specified Pastel address")
async def get_received_by_address(zcashaddress: str, minconf: Optional[int] = 1, 
                                  rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    total_amount = await rpc_connection.getreceivedbyaddress(zcashaddress, minconf)
    return GetReceivedByAddressResponse(total_amount=total_amount)







@router.get("/getreceivedbyaccount",
            response_model=GetReceivedByAccountResponse,
            tags=["Wallet Methods"],
            summary="Get the total amount received by an account",
            description="""Get the total amount received by addresses with a specified account in transactions with at least a certain number of confirmations.

### Description
- This endpoint returns the total amount received by addresses associated with a given account, considering transactions with at least the specified number of confirmations.
- Note: The 'account' parameter is deprecated and should be set to an empty string "" to represent the default account.

### Input Parameters
- `account` (string, required): Must be set to the empty string "" to represent the default account. Passing any other string will result in an error.
- `minconf` (int, optional, default=1): Only include transactions confirmed at least this many times.

### Example Request
- `GET /getreceivedbyaccount?account=""&minconf=1`

### Response
- Returns the total amount received by the specified account.

### Example Response
```json
{
    "amount": 123.45
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="The total amount received by the specified account")
async def get_received_by_account(request: GetReceivedByAccountRequest, 
                                  rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.getreceivedbyaccount(request.account, request.minconf)
    return GetReceivedByAccountResponse(amount=response)







@router.get("/getbalance",
            response_model=GetBalanceResponse,
            tags=["Blockchain Methods"],
            summary="Get the server's total available balance",
            description="""Get the server's total available balance.

### Description
- This endpoint returns the total available balance in the server's wallet. It can be filtered by a minimum number of confirmations and can include balances in watch-only addresses.

### Input Parameters
- `account`: (Optional) DEPRECATED. Must be an empty string "" or "*", either of which will give the total available balance. Any other string will result in an error.
- `minconf`: (Optional) Only include transactions confirmed at least this many times. Default is 1.
- `includeWatchonly`: (Optional) Also include balance in watchonly addresses. Default is false.

### Example Request
- `GET /getbalance?account=*&minconf=1&includeWatchonly=false`

### Response
- Returns a JSON object containing the available balance amount.

### Example Response
```json
{
    "balance": 1000.00
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The account argument is deprecated and should be set to "" or "*". 
""",
            response_description="Available balance amount")
async def get_balance(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection),
                      account: Optional[str] = None,
                      minconf: Optional[int] = 1,
                      includeWatchonly: Optional[bool] = False):
    balance = await rpc_connection.getbalance(account, minconf, includeWatchonly)
    return GetBalanceResponse(balance=balance)







@router.post("/move",
             response_model=MoveResponse,
             tags=["Control Methods"],
             summary="Move amount from one account to another",
             description="""Move a specified amount from one account in your wallet to another.

### Description
- **DEPRECATED**: This method is deprecated. However, it is still available for use.
- Moves a specified amount from one account in your wallet to another. It is a local operation and does not involve a transaction on the blockchain.

### Input Parameters
- `fromaccount`: (string, required) The account to move funds from. Must be set to the empty string "" to represent the default account.
- `toaccount`: (string, required) The account to move funds to. Must be set to the empty string "" to represent the default account.
- `amount`: (numeric, required) The quantity of currency to move between accounts.
- `minconf`: (numeric, optional, default=1) The minimum number of confirmations for used funds.
- `comment`: (string, optional) An optional comment, stored in the wallet only.

### Example Request
```json
{
    "fromaccount": "",
    "toaccount": "tabby",
    "amount": 0.01,
    "minconf": 1,
    "comment": "Transfer to tabby"
}
```

### Response
- Returns a boolean indicating if the operation was successful.

### Example Response
```json
{
    "success": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is deprecated and might be removed in future versions.""",
             response_description="Indicates whether the move operation was successful")
async def move(request: MoveRequest, 
               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    success = await rpc_connection.move(request.fromaccount, request.toaccount, request.amount, request.minconf, request.comment)
    return MoveResponse(success=success)







@router.post("/sendfrom",
             response_model=SendFromResponse,
             tags=["Raw Transaction Methods"],
             summary="Send amount from an account to a Pastel address",
             description="""Send an amount from an account to a specified Pastel address. 
             
### Description
- This endpoint is a deprecated method (use sendtoaddress) for sending an amount from an account to a Pastel address. The amount is a real number and is rounded to the nearest 0.00000001.

### Input Parameters
- `fromaccount`: (string, required) Must be set to the empty string "" to represent the default account. Any other string will result in an error.
- `tozcashaddress`: (string, required) The Pastel address to send funds to.
- `amount`: (numeric, required) The amount in PSL.
- `minconf`: (numeric, optional, default=1) Only use funds with at least this many confirmations.
- `comment`: (string, optional) A comment for the transaction, stored in your wallet.
- `comment_to`: (string, optional) A comment to store the name of the person/organization to which you're sending the transaction, stored in your wallet.

### Request JSON Format
```json
{
    "fromaccount": "",
    "tozcashaddress": "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n",
    "amount": 0.01,
    "minconf": 1,
    "comment": "donation",
    "comment_to": "seans outpost"
}
```

### Response
- Returns a JSON object containing the transaction ID.

### Example Response
```json
{
    "transaction_id": "transactionid1234567890"
}
```

### Possible Errors
- HTTP 400: Invalid request parameters.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- It's recommended to use `sendtoaddress` instead of this deprecated method.""",
             response_description="Transaction ID of the sent transaction")
async def send_from(
        fromaccount: str,
        tozcashaddress: str,
        amount: float,
        minconf: Optional[int] = 1,
        comment: Optional[str] = None,
        comment_to: Optional[str] = None,
        rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)
    ):
    transaction_id = await rpc_connection.sendfrom(
        fromaccount, tozcashaddress, amount, minconf, comment, comment_to
    )
    return SendFromResponse(transaction_id=transaction_id)







@router.post("/sendmany",
             response_model=SendManyResponse,
             tags=["Raw Transaction Methods"],
             summary="Send multiple transactions",
             description="""Send multiple times. Amounts are decimal numbers with at most 8 digits of precision.

### Description
- This endpoint sends multiple transactions to multiple addresses.

### Input Parameters
- `from_account`: MUST be set to the empty string "" to represent the default account. Any other string will result in an error.
- `amounts`: A JSON object with addresses and amounts.
- `min_conf`: Optional, minimum number of confirmations. Default is 1.
- `comment`: Optional, a comment for the transaction.
- `subtract_fee_from_amount`: Optional, a list of addresses from which the fee will be subtracted.
- `change_address`: Optional, the destination address for the change. Can be "original", "new", or a specific Pastel t-address.

### Example Request
```json
{
    "from_account": "",
    "amounts": {
        "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n": 0.01
    },
    "min_conf": 1,
    "comment": "Test transaction",
    "subtract_fee_from_amount": ["PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n"],
    "change_address": "original"
}
```

### Response
- Returns a JSON object containing the transaction ID.

### Example Response
```json
{
    "transaction_id": "transaction_id_here"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Transaction ID of the sent transactions")
async def send_many(request: SendManyRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Extract parameters from request
    from_account = request.from_account
    amounts = request.amounts
    min_conf = request.min_conf
    comment = request.comment
    subtract_fee_from_amount = request.subtract_fee_from_amount
    change_address = request.change_address

    # Call the RPC method with the extracted parameters
    transaction_id = await rpc_connection.sendmany(from_account, amounts, min_conf, comment, subtract_fee_from_amount, change_address)
    return SendManyResponse(transaction_id=transaction_id)








@router.post("/addmultisigaddress",
             response_model=AddMultisigAddressResponse,
             tags=["Utility Methods"],
             summary="Add a multisignature address",
             description="""Add a nrequired-to-sign multisignature address to the wallet. 
                            Each key is a Pastel address or hex-encoded public key.

### Description
- This endpoint adds a multisignature address to the wallet which requires a specified number of signatures to authorize a transaction.
- Each key in the `keysobject` list can be either a Pastel address or a hex-encoded public key.

### Input Parameters
- `nrequired` (int): The number of required signatures out of the n keys or addresses.
- `keysobject` (List[str]): A list of Pastel addresses or hex-encoded public keys.
- `account` (str, optional): DEPRECATED. Must be set to an empty string "" for the default account. Any other string will result in an error.

### Example Request
```json
{
    "nrequired": 2,
    "keysobject": ["PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n", "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n"],
    "account": ""
}
```

### Response
- Returns a JSON object with the newly created Pastel address.

### Example Response
```json
{
    "zcashaddress": "pZc4pUvczxNG1Sfh5Zx3n2fuFjGjTDbB4qu"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="A Pastel address associated with the keys.")
async def add_multisig_address(request: AddMultisigAddressRequest, 
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    zcashaddress = await rpc_connection.addmultisigaddress(request.nrequired, request.keysobject, request.account)
    return AddMultisigAddressResponse(zcashaddress=zcashaddress)






@router.get("/listreceivedbyaddress",
            response_model=List[AddressReceivedInfo],
            tags=["Wallet Methods"],
            summary="List balances by receiving address",
            description="""List balances by receiving address.

### Description
- This endpoint returns the list of balances associated with each receiving address.

### Input Parameters
- `minconf`: The minimum number of confirmations before payments are included. Default is 1.
- `includeempty`: Whether to include addresses that haven't received any payments. Default is false.
- `includeWatchonly`: Whether to include watchonly addresses (see 'importaddress'). Default is false.

### Example Request
- `GET /listreceivedbyaddress?minconf=1&includeempty=true&includeWatchonly=false`

### Response
- Returns a JSON array with information about each address and its associated balance.

### Example Response
```json
[
    {
        "involvesWatchonly": true,
        "address": "receivingaddress",
        "account": "accountname",
        "amount": 1.234,
        "confirmations": 5
    },
    ...
]
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The `account` field is deprecated and will be removed in future versions.""",
            response_description="List of balances by receiving address")
async def list_received_by_address(minconf: int = 1, includeempty: bool = False, includeWatchonly: bool = False, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.listreceivedbyaddress(minconf, includeempty, includeWatchonly)
    return response






@router.get("/listtransactions",
            response_model=ListTransactionsResponse,
            tags=["Wallet Methods"],
            summary="List recent transactions",
            description="""List up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.

### Description
- This endpoint returns up to 'count' most recent transactions skipping the first 'from' transactions for account 'account'.
- It can include transactions to watch-only addresses if specified.

### Input Parameters
- `account`: (Optional) The account name. Should be "*".
- `count`: (Optional, default=10) The number of transactions to return.
- `from`: (Optional, default=0) The number of transactions to skip.
- `include_watch_only`: (Optional, default=false) Include transactions to watchonly addresses.

### Example Request
- `GET /listtransactions?account=*&count=20&from=100&include_watch_only=true`

### Response
- Returns a list of transaction information.

### Example Response
```json
{
    "transactions": [
        {
            "account": "...",
            "address": "...",
            "category": "...",
            "amount": ...,
            "vout": ...,
            ...
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="A list of recent transactions")
async def list_transactions(request: ListTransactionsRequest, 
                            rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.listtransactions(request.account, request.count, request.from_index, request.include_watch_only)
    return ListTransactionsResponse(transactions=response)






@router.get("/listaccounts",
            response_model=ListAccountsResponse,
            tags=["Wallet Methods"],
            summary="List account balances",
            description="""List the balances of all accounts in the wallet.

### Description
- Returns a list of accounts with their respective balances. Accounts are identified by their names.

### Input Parameters
- `minconf` (optional): Minimum number of confirmations for a transaction to be included.
- `includeWatchonly` (optional): Include balances in watch-only addresses.

### Example Request
- `GET /listaccounts?minconf=1&includeWatchonly=false`

### Response
- Returns a JSON object containing account names and their balances.

### Example Response
```json
{
    "accounts": [
        {"account": "account_name", "balance": 123.45},
        ...
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
            response_description="List of accounts with their balances")
async def list_accounts(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection),
                        minconf: Optional[int] = 1, includeWatchonly: Optional[bool] = False):
    accounts_data = await rpc_connection.listaccounts(minconf, includeWatchonly)
    accounts = []
    for account, balance in accounts_data.items():
        accounts.append(ListAccountsResponseItem(account=account, balance=balance))
    return ListAccountsResponse(accounts=accounts)






@router.post("/listsinceblock",
             response_model=ListSinceBlockResponse,
             tags=["Blockchain Methods"],
             summary="List transactions since a specific block",
             description="""List all transactions in blocks since a specified block, or all transactions if no block is specified.

### Description
- This endpoint retrieves all transactions that occurred after a specified block. 
- It can be used to update a client with all new transactions if it already knows the old state up to a certain block.

### Input Parameters
- `blockhash` (string, optional): The block hash to list transactions since.
- `target_confirmations` (numeric, optional): The confirmations required, must be 1 or more.
- `include_watchonly` (bool, optional, default=false): Include transactions to watch-only addresses.

### Example Request
```json
{
    "blockhash": "000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad",
    "target_confirmations": 6,
    "include_watchonly": false
}
```

### Response
- Returns a JSON object with an array of transactions since the specified block and the hash of the last block.

### Example Response
```json
{
    "transactions": [
        {
            "account": "",
            "address": "zcashaddress",
            "category": "receive",
            "amount": 10.0,
            "vout": 1,
            ...
        }
    ],
    "lastblock": "lastblockhash"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="A list of transactions since the specified block and the last block hash")
async def list_since_block(request: ListSinceBlockRequest, 
                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.listsinceblock(request.blockhash, request.target_confirmations, request.include_watchonly)
    return ListSinceBlockResponse(**response)






@router.post("/backupwallet",
             response_model=BackupWalletResponse,
             tags=["Utility Methods"],
             summary="Backup the wallet to a destination",
             description="""Backup the wallet.dat file to a specified destination filename.

### Description
- Safely copies the wallet.dat file to the specified destination. The destination is a filename and should be saved in the directory set by the `-exportdir` option.

### Input Parameters
- `destination`: (string, required) The destination filename.

### Example Request
- `POST /backupwallet` with JSON body `{"destination": "backupdata"}`

### Response
- Returns a JSON object containing the full path of the destination file where the wallet was backed up.

### Example Response
```json
{
    "path": "/path/to/backup/backupdata"
}
```

### Possible Errors
- HTTP 400: Bad Request if the destination filename is invalid or not provided.
- HTTP 500: Internal Server Error if there's an issue in processing the request, such as if the `-exportdir` option is not set or the wallet backup fails.

### Note
- It's crucial to regularly backup your wallet to prevent loss of funds in case of system failures.""",
             response_description="The full path of the destination file where the wallet was backed up")
async def backup_wallet(request: BackupWalletRequest, 
                        rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    backup_path = await rpc_connection.backupwallet(request.destination)
    return BackupWalletResponse(path=backup_path)





@router.get("/gettransaction/{txid}",
            response_model=GetTransactionResponse,
            tags=["Blockchain Methods"],
            summary="Get detailed information about a transaction",
            description="""Retrieve detailed information about an in-wallet transaction by its ID.

### Description
- Fetches detailed data of a specified transaction from the wallet, including amounts, confirmations, and related addresses.

### Input Parameters
- `txid`: The transaction ID to query.
- `includeWatchonly`: (Optional) Include watch-only addresses in balance calculation and details.

### Example Request
- `GET /gettransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d`

### Response
- Returns detailed information about the specified transaction.

### Example Response
```json
{
    "status": "mined",
    "amount": 10.0,
    "amountPat": 10000,
    "confirmations": 15,
    "blockhash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
    "blockindex": 1,
    "blocktime": 1625097600,
    "txid": "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d",
    "time": 1625097600,
    "timereceived": 1625097600,
    "details": [
        {
            "account": "",
            "address": "t1Xin4H451oBDwrKcQeY1VGgMWivLs2hhuR",
            "category": "receive",
            "amount": 10.0,
            "amountPat": 10000,
            "vout": 0
        }
    ],
    "hex": "010000000..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the transaction ID is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is used to obtain transaction details for wallet transactions.""",
            response_description="Detailed information about the specified transaction")
async def get_transaction(txid: str, includeWatchonly: Optional[bool] = False, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    transaction_data = await rpc_connection.gettransaction(txid, includeWatchonly)
    return GetTransactionResponse(**transaction_data)






@router.post("/walletpassphrase",
             response_model=WalletPassphraseResponse,
             tags=["Control Methods"],
             summary="Unlock the wallet",
             description="""Unlock the wallet with a passphrase for a given duration.

### Description
- Unlocks the wallet for the specified time period, allowing transactions related to private keys, such as sending Pastel. 

### Input Parameters
- `passphrase`: The passphrase used to encrypt the wallet (string, required).
- `timeout`: Duration in seconds to keep the wallet unlocked (integer, required).

### Example Request
```json
{
    "passphrase": "my pass phrase",
    "timeout": 60
}
```

### Response
- Confirmation message indicating successful unlocking of the wallet.

### Example Response
```json
{
    "result": "Wallet unlocked successfully"
}
```

### Possible Errors
- HTTP 400: Incorrect passphrase provided.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 403: Wallet is already unlocked.

### Note
- If the wallet is already unlocked, issuing this command will reset the unlock time.""",
             response_description="Confirmation of wallet unlocking")
async def wallet_passphrase(request: WalletPassphraseRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.walletpassphrase(request.passphrase, request.timeout)
    return WalletPassphraseResponse(result=response if response else "Wallet unlocked successfully")







@router.post("/keypoolrefill",
             tags=["Control Methods"],
             summary="Refill the keypool",
             description="""Refill the keypool to the specified size.

### Description
- This endpoint is used to refill the keypool of the wallet to a new size. The keypool keeps a buffer of keys available for use in transactions. Refilling the keypool is important to maintain anonymity and security.

### Input Parameters
- `newsize`: (Optional, numeric) The new size for the keypool. Default is 100.

### Example Request
- `POST /keypoolrefill` with payload `{"newsize": 150}`

### Response
- This method does not return any specific data, but a successful request indicates that the keypool was refilled successfully.

### Possible Errors
- HTTP 400: Bad Request if the newsize parameter is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- It's recommended to refill the keypool periodically for operational security and efficiency.""",
             response_description="Confirmation that the keypool has been refilled")
async def keypool_refill(request: KeypoolRefillRequest,
                         rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.keypoolrefill(request.newsize)
    return {"message": "Keypool refilled successfully."}





@router.post("/walletlock",
             tags=["Control Methods"],
             summary="Lock the wallet",
             description="""Lock the wallet by removing the encryption key from memory.

### Description
- This endpoint locks the wallet by removing the wallet encryption key from memory. 
- After calling this method, you will need to call `walletpassphrase` again before being able to call any methods which require the wallet to be unlocked.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `POST /walletlock`

### Response
- Returns an empty response on successful execution.

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request or if the wallet is not encrypted.
- HTTP 400: Bad Request if called with an unencrypted wallet.

### Examples:
- Set the passphrase for 2 minutes to perform a transaction:
  - `walletpassphrase "my pass phrase" 120`
- Perform a send (requires passphrase set):
  - `sendtoaddress "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n" 1.0`
- Clear the passphrase since we are done before 2 minutes is up:
  - `walletlock`

### Note
- This is primarily used for security purposes in managing wallet access.""",
             response_description="Empty response on successful wallet lock")
async def walletlock(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.walletlock()
    return "Wallet locked successfully."





@router.post("/encryptwallet",
             response_model=EncryptWalletResponse,
             tags=["Control Methods"],
             summary="Encrypt the wallet with a passphrase",
             description="""Encrypt the wallet with a given passphrase. 
             
             ### Description
             - This endpoint encrypts the wallet with the provided passphrase. It's used for the first time encryption of the wallet. After encryption, any operations that interact with private keys (like sending or signing) will require the passphrase.
             - If the wallet is already encrypted, this operation will fail, and you should use the `walletpassphrasechange` call instead.
             - Note that encrypting the wallet will shutdown the server.

             ### Input Parameters
             - `passphrase`: A string representing the passphrase to encrypt the wallet with. It must be at least 1 character long, but a longer passphrase is recommended for security.

             ### Example Request
             ```json
             {
                 "passphrase": "my secure passphrase"
             }
             ```

             ### Response
             - Returns a message indicating the encryption status and server shutdown.

             ### Example Response
             ```json
             {
                 "message": "wallet encrypted; Pastel server stopping, restart to run with encrypted wallet. The keypool has been flushed, you need to make a new backup."
             }
             ```

             ### Possible Errors
             - HTTP 400: Bad Request if wallet encryption is disabled or the wallet is already encrypted.
             - HTTP 500: Internal Server Error if there's an issue in processing the request.

             ### Note
             - This is a critical operation that changes the state of the wallet and requires server restart.""",
             response_description="Message indicating the encryption status and server shutdown")
async def encrypt_wallet(passphrase: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    if not passphrase:
        logger.error("Passphrase is required and cannot be empty.")
    response = await rpc_connection.encryptwallet(passphrase)
    return EncryptWalletResponse(message=response)





@router.post("/walletpassphrasechange",
             response_model=WalletPassphraseChangeResponse,
             tags=["Control Methods"],
             summary="Change the wallet passphrase",
             description="""Change the wallet passphrase from 'oldpassphrase' to 'newpassphrase'.

### Description
- This endpoint allows for the change of the existing wallet passphrase to a new passphrase. It's essential for maintaining wallet security and should be used with caution.

### Input Parameters
- `oldpassphrase`: The current passphrase of the wallet.
- `newpassphrase`: The new passphrase that will replace the current passphrase.

### Example Request
```json
POST /walletpassphrasechange
{
    "oldpassphrase": "oldpassword123",
    "newpassphrase": "newpassword456"
}
```

### Response
- On successful change, the response is a confirmation message.

### Example Response
```json
{
    "result": "Passphrase changed successfully"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are incorrect or missing.
- HTTP 500: Internal Server Error if there's an issue processing the request or if the old passphrase is incorrect.

### Note
- The wallet needs to be encrypted for this operation to succeed. If the wallet is unencrypted, this method will return an error.""",
             response_description="Confirmation of passphrase change")
async def change_wallet_passphrase(request: WalletPassphraseChangeRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    await rpc_connection.walletpassphrasechange(request.oldpassphrase, request.newpassphrase)
    return WalletPassphraseChangeResponse(result="Passphrase changed successfully")






@router.post("/lockunspent", 
            response_model=LockUnspentResponse, 
            tags=["Control Methods"],
            summary="Lock or unlock unspent transaction outputs",
            description="""Lock or unlock specified transaction outputs.

### Description
- Temporarily lock (unlock=false) or unlock (unlock=true) specified transaction outputs.
- A locked transaction output will not be chosen by automatic coin selection when spending Pastel.
- Locks are stored in memory only and are cleared upon node restart.

### Input Parameters
- `request`: A JSON object containing the unlock flag and a list of transaction outputs to be locked or unlocked.

### Request JSON Format
```json
{
    "unlock": false,
    "transactions": [
        {
            "txid": "a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0",
            "vout": 1
        }
    ]
}
```

### Response
- Returns a JSON object indicating the success of the operation.

### Example Response
```json
{
    "success": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Result of the lock/unlock operation")
async def lock_unspent(request: LockUnspentRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.lockunspent(request.unlock, request.transactions)
    return LockUnspentResponse(success=result)







@router.post("/settxfee",
             response_model=SetTxFeeResponse,
             tags=["Utility Methods"],
             summary="Set the transaction fee per kB",
             description="""Set the transaction fee per kilobyte for transactions.

### Description
- This endpoint allows setting the transaction fee per kilobyte that will be used for future transactions.

### Input Parameters
- `amount`: (numeric, required) The transaction fee in [currency]/kB rounded to the nearest 0.00000001.

### Example Request
```json
{
    "amount": 0.00001
}
```

### Response
- Returns a JSON object indicating whether the transaction fee was successfully set.

### Example Response
```json
{
    "success": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Status of setting the transaction fee")
async def set_tx_fee(request: SetTxFeeRequest, 
                     rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.settxfee(request.amount)
    return SetTxFeeResponse(success=result)







@router.get("/getwalletinfo",
            response_model=WalletInfoResponse,
            tags=["Utility Methods"],
            summary="Get wallet state information",
            description="""Returns an object containing various wallet state info.

### Description
- This endpoint provides information about the wallet, including balances, transaction count, key pool size, and other relevant data.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /getwalletinfo`

### Response
- Returns a JSON object containing detailed information about the wallet.

### Example Response
```json
{
    "walletversion": 169900,
    "balance": 0.015,
    "unconfirmed_balance": 0.0,
    "immature_balance": 0.0,
    "txcount": 2,
    "keypoololdest": 1600000000,
    "keypoolsize": 1000,
    "unlocked_until": null,
    "paytxfee": 0.00001,
    "seedfp": "d1f1a9fc"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Information about the wallet's state")
async def get_wallet_info(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    wallet_info = await rpc_connection.getwalletinfo()
    return WalletInfoResponse(**wallet_info)





@router.get("/listlockunspent",
            response_model=ListLockUnspentResponse,
            tags=["Blockchain Methods"],
            summary="List Temporarily Unspendable Outputs",
            description="""List all temporarily unspendable outputs.

### Description
- This endpoint returns a list of outputs that are temporarily unspendable. 
- Useful for viewing transactions that have been locked using the `lockunspent` call.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /listlockunspent`

### Response
- Returns a JSON array containing objects with 'txid' and 'vout' fields for each temporarily locked output.

### Example Response
```json
{
    "lock_unspent_outputs": [
        {
            "txid": "a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0",
            "vout": 1
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The 'txid' represents the transaction id of the locked output, and 'vout' is its output index.""",
            response_description="List of temporarily unspendable outputs")
async def list_lock_unspent(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    list_lock_unspent_result = await rpc_connection.listlockunspent()
    return ListLockUnspentResponse(lock_unspent_outputs=[ListLockUnspentResponseItem(**item) for item in list_lock_unspent_result])





@router.post("/resendwallettransactions",
            response_model=ResendWalletTransactionsResponse,
            tags=["Utility Methods"],
            summary="Re-broadcast unconfirmed wallet transactions",
            description="""Immediately re-broadcast unconfirmed wallet transactions to all peers.

### Description
- This endpoint is intended primarily for testing. It forces the immediate re-broadcast of unconfirmed transactions from the wallet to all peers.
- The wallet code periodically re-broadcasts transactions automatically, so this method is typically unnecessary in production environments.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `POST /resendwallettransactions`

### Response
- Returns a JSON object containing an array of transaction IDs that were re-broadcast.

### Example Response
```json
{
    "transaction_ids": ["txid1", "txid2", "txid3"]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Use this method with caution, as it is primarily for testing purposes and may affect network performance if used excessively.""",
            response_description="Array of transaction IDs that were re-broadcast")
async def resend_wallet_transactions(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    transaction_ids = await rpc_connection.resendwallettransactions()
    return ResendWalletTransactionsResponse(transaction_ids=transaction_ids)








@router.get("/listunspent",
            response_model=ListUnspentResponse,
            tags=["Blockchain Methods"],
            summary="List Unspent Transaction Outputs",
            description="""List unspent transaction outputs (UTXOs) with specified confirmations and optionally filtered by addresses.

### Description
- Returns an array of UTXOs with confirmations between the specified minimum and maximum.

### Input Parameters
- `minconf`: (Optional) Minimum number of confirmations. Default is 1.
- `maxconf`: (Optional) Maximum number of confirmations. Default is 9999999.
- `addresses`: (Optional) A list of Pastel addresses to filter.

### Example Request
- `GET /listunspent?minconf=1&maxconf=9999999`

### Response
- Returns an array of UTXOs with detailed information about each.

### Example Response
```json
{
    "unspent_transactions": [
        {
            "txid": "12345",
            "vout": 0,
            "generated": false,
            "address": "PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n",
            "account": "account_name",
            "scriptPubKey": "76a914...",
            "amount": 0.0001,
            "confirmations": 10,
            "redeemScript": "abcd...",
            "spendable": true
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for wallets and other applications to determine spendable balances.""",
            response_description="Array of unspent transaction outputs")
async def list_unspent(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection), minconf: int = 1, maxconf: int = 9999999, addresses: Optional[List[str]] = None):
    unspent_transactions = await rpc_connection.listunspent(minconf, maxconf, addresses)
    return ListUnspentResponse(unspent_transactions=unspent_transactions)







@router.get("/z_listunspent",
            response_model=ZListUnspentResponse,
            tags=["Blockchain Methods"],
            summary="List unspent shielded notes",
            description="""List unspent shielded notes with a specified range of confirmations and optionally filter for specific addresses.

### Description
- Returns an array of unspent shielded notes with a specified range of confirmations. Optionally filters to only include notes sent to specified addresses.

### Input Parameters
- `minconf`: Minimum number of confirmations to filter (default=1).
- `maxconf`: Maximum number of confirmations to filter (default=9999999).
- `includeWatchonly`: Whether to include watchonly addresses (default=false).
- `addresses`: Array of Sapling zaddrs to filter on (optional).

### Example Request
- `GET /z_listunspent?minconf=1&maxconf=9999999&includeWatchonly=false&addresses=["zaddr1", "zaddr2"]`

### Response
- Returns a JSON array of objects, each representing an unspent shielded note.

### Example Response
```json
{
    "unspent_notes": [
        {
            "txid": "txid",
            "outindex": 0,
            "confirmations": 10,
            "spendable": true,
            "address": "address",
            "amount": 123.45,
            "memo": "hex_memo",
            "change": false
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used for wallet balance management and transaction preparation.""",
            response_description="List of unspent shielded notes")
async def z_listunspent(minconf: Optional[int] = 1,
                        maxconf: Optional[int] = 9999999,
                        includeWatchonly: Optional[bool] = False,
                        addresses: Optional[List[str]] = None,
                        rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    unspent_notes = await rpc_connection.z_listunspent(minconf, maxconf, includeWatchonly, addresses)
    return ZListUnspentResponse(unspent_notes=unspent_notes)







@router.post("/fundrawtransaction",
             response_model=FundRawTransactionResponse,
             tags=["Raw Transaction Methods"],
             summary="Add inputs to a transaction",
             description="""Add inputs to a transaction until it has enough in value to meet its out value.

### Description
- This endpoint adds inputs to a raw transaction represented by a hex string. It ensures the transaction has enough value to meet its output value.
- It will not modify existing inputs and will add one change output to the outputs.
- Note that inputs which were signed may need to be re-signed after completion since inputs/outputs have been added.
- The inputs added by this method will not be signed; use `signrawtransaction` for that.

### Input Parameters
- `hexstring`: A string representing the raw transaction in hexadecimal format.

### Example Request
- `POST /fundrawtransaction` with JSON body `{"hexstring": "rawtransactionhex"}`

### Response
- Returns a JSON object containing the resulting raw transaction, the fee added, and the position of the added change output.

### Example Response
```json
{
    "hex": "fundedtransactionhex",
    "fee": 0.0012,
    "changepos": 1
}
```

### Possible Errors
- HTTP 400: Bad Request if the `hexstring` parameter is invalid or missing.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This method is part of the transaction creation process, typically followed by `signrawtransaction` and `sendrawtransaction`.""",
             response_description="Information about the funded transaction")
async def fund_raw_transaction(request: FundRawTransactionRequest,
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.fundrawtransaction(request.hexstring)
    return FundRawTransactionResponse(hex=result['hex'], fee=result['fee'], changepos=result['changepos'])






@router.get("/z_getnewaddress",
            response_model=ZGetNewAddressResponse,
            tags=["Wallet Methods"],
            summary="Generate a new shielded address",
            description="""Generate a new shielded address for receiving payments. 

### Description
- This endpoint returns a new shielded (Zcash) Sapling address for receiving payments.

### Input Parameters
- `type`: (Optional) The type of address to generate. Currently, only 'Sapling' type is supported.

### Example Request
- `GET /z_getnewaddress?type=Sapling`

### Response
- Returns a JSON object containing the new shielded Zcash address.

### Example Response
```json
{
    "zcash_address": "zs1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 400: Bad Request if an invalid address type is specified.

### Note
- Used for creating new addresses to receive shielded transactions.""",
            response_description="New shielded Zcash address")
async def z_get_new_address(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection), address_type: Optional[str] = None):
    if address_type not in [None, "Sapling"]:
        logger.error("Invalid address type")
    zcash_address = await rpc_connection.z_getnewaddress(address_type if address_type else "Sapling")
    return ZGetNewAddressResponse(zcash_address=zcash_address)







@router.post("/zcbenchmark",
             response_model=ZCBenchmarkResponse,
             tags=["Utility Methods"],
             summary="Runs a benchmark of the selected type",
             description="""Runs a benchmark of the selected type `samplecount` times, returning the running times of each sample.

### Description
- This endpoint runs a specified benchmark multiple times and returns the running time for each iteration. 
- It's useful for performance testing various operations on the Pastel blockchain.

### Input Parameters
- `benchmarktype`: The type of benchmark to run.
- `samplecount`: The number of times to run the benchmark.
- `extra_param`: Optional additional parameter, depending on the benchmark type.

### Example Request
```json
{
  "benchmarktype": "solveequihash",
  "samplecount": 5,
  "extra_param": 2
}
```

### Response
- Returns a list of objects, each containing the `runningtime` for a benchmark sample.

### Example Response
```json
{
    "results": [
        {"runningtime": 0.12},
        {"runningtime": 0.11},
        {"runningtime": 0.13},
        {"runningtime": 0.12},
        {"runningtime": 0.12}
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="List of running times for each benchmark sample")
async def zc_benchmark(request: ZCBenchmarkRequest, 
                       rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    extra_params = [request.extra_param] if request.extra_param is not None else []
    results = await rpc_connection.zcbenchmark(request.benchmarktype, request.samplecount, *extra_params)
    return ZCBenchmarkResponse(results=[ZCBenchmarkSampleResult(runningtime=result["runningtime"]) for result in results])







@router.get("/z_listaddresses",
            response_model=ListShieldedAddressesResponse,
            tags=["Blockchain Methods"],
            summary="List Shielded Addresses",
            description="""List all Sapling shielded addresses belonging to the wallet.

### Description
- This endpoint returns a list of Sapling shielded addresses that are owned by the wallet. 
- It can optionally include watch-only addresses.

### Input Parameters
- `include_watchonly`: (bool, optional, default=false) Set to true to include watch-only addresses.

### Example Request
- `GET /z_listaddresses?include_watchonly=true`

### Response
- Returns a JSON object containing an array of shielded addresses.

### Example Response
```json
{
    "addresses": ["zs1...address1", "zs1...address2"]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for retrieving all shielded addresses associated with the user's wallet.""",
            response_description="List of shielded addresses")
async def list_shielded_addresses(include_watchonly: bool = False, 
                                  rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    addresses = await rpc_connection.z_listaddresses(include_watchonly)
    return ListShieldedAddressesResponse(addresses=addresses)







@router.get("/z_listreceivedbyaddress",
            response_model=ZListReceivedByAddressResponse,
            tags=["Utility Methods"],
            summary="List amounts received by a z-address",
            description="""List amounts received by a z-address belonging to the node's wallet.

### Description
- This endpoint returns a list of amounts received by a specified z-address. 
- It includes various details about each received note, such as the transaction ID, amount, confirmations, and more.

### Input Parameters
- `address` (string): The z-address to query.
- `minconf` (numeric, optional, default=1): Minimum number of confirmations for a transaction to be included.

### Example Request
- `GET /z_listreceivedbyaddress?address=<z-address>&minconf=1`

### Response
- Returns a JSON object containing a list of received notes, each with detailed information.

### Example Response
```json
{
    "notes": [
        {
            "txid": "example-txid",
            "amount": 1.23,
            "amountPat": 123,
            "memo": "hex-string",
            "confirmations": 10,
            "blockheight": 100000,
            "blockindex": 1,
            "blocktime": 1609459200,
            "change": false
        }
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="List of received notes with detailed information")
async def z_list_received_by_address(request: ZListReceivedByAddressRequest,
                                     rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.z_listreceivedbyaddress(request.address, request.minconf)
    return ZListReceivedByAddressResponse(notes=response)







@router.get("/z_getbalance/{address}",
            response_model=ZGetBalanceResponse,
            tags=["Blockchain Methods"],
            summary="Get the balance of an address",
            description="""Get the balance of a transparent or private address in the Pastel blockchain.

### Description
- This endpoint returns the balance of a given t-address or z-address belonging to the node's wallet. 
- CAUTION: If the wallet has only an incoming viewing key for this address, spends cannot be detected, and the returned balance may be larger than the actual balance.

### Input Parameters
- `address`: The address for which the balance is requested. It can be a transparent (t-address) or private (z-address).
- `minconf` (optional): Only include transactions confirmed at least this many times. Default is 1.

### Example Request
- `GET /z_getbalance/myaddress`
- `GET /z_getbalance/myaddress?minconf=5`

### Response
- Returns a JSON object containing the balance of the specified address.

### Example Response
```json
{
    "balance": 1234.56
}
```

### Possible Errors
- HTTP 400: Bad Request if the address is invalid or does not belong to the node.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Balance is returned in )" + CURRENCY_UNIT + R"(. Primarily used to check the amount received by an address.""",
            response_description="Balance of the specified address")
async def z_get_balance(address: str, minconf: Optional[int] = 1, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    balance = await rpc_connection.z_getbalance(address, minconf)
    return ZGetBalanceResponse(balance=balance)






@router.get("/z_gettotalbalance",
            response_model=ZGetTotalBalanceResponse,
            tags=["Wallet Methods"],
            summary="Get the total balance of both transparent and private funds",
            description="""Get the total value of funds stored in the node's wallet.

### Description
- This endpoint returns the total balance of both transparent and private funds in the node's wallet.
- The balance is calculated based on the specified minimum number of confirmations and can include watchonly addresses.

### Input Parameters
- `minconf` (int, optional, default=1): Only include transactions confirmed at least this many times.
- `includeWatchonly` (bool, optional, default=false): Include balance in watchonly addresses.

### Example Request
- `GET /z_gettotalbalance?minconf=5&includeWatchonly=true`

### Response
- Returns a JSON object containing the total balance of transparent and private funds.

### Example Response
```json
{
    "transparent": 100.0,
    "private": 50.0,
    "total": 150.0
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Balance calculations with watchonly addresses require the corresponding viewing keys.""",
            response_description="Total balance of both transparent and private funds")
async def z_get_total_balance(request: ZGetTotalBalanceRequest, 
                              rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.z_gettotalbalance(request.minconf, request.includeWatchonly)
    return ZGetTotalBalanceResponse(transparent=result["transparent"],
                                    private=result["private"],
                                    total=result["total"])






@router.get("/z_viewtransaction/{txid}",
            response_model=ZViewTransactionResponse,
            tags=["Blockchain Methods"],
            summary="Get detailed shielded information about in-wallet transaction",
            description="""Retrieve detailed information about a shielded transaction in the wallet.

### Description
- Returns detailed information about a specific in-wallet transaction, including spends and outputs related to shielded addresses.

### Input Parameters
- `txid`: The transaction id (string, required).

### Example Request
- `GET /z_viewtransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d`

### Response
- Returns detailed information about the transaction, including spends and outputs.

### Example Response
```json
{
    "txid": "1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d",
    "spends": [...],
    "outputs": [...]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 404: Transaction not found or not part of the wallet.

### Note
- This endpoint is used to get detailed information about shielded transactions, particularly for auditing and verification purposes.""",
            response_description="Detailed information about the shielded transaction")
async def z_view_transaction(txid: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    transaction_info = await rpc_connection.z_viewtransaction(txid)
    return ZViewTransactionResponse(**transaction_info)






@router.get("/z_getoperationresult",
            response_model=ZGetOperationResultResponse,
            tags=["Blockchain Methods"],
            summary="Retrieve the result and status of Zcash operations",
            description="""Retrieve the result and status of an operation which has finished, and then remove the operation from memory.

### Description
- This endpoint retrieves the results of one or more operations identified by their operation IDs.
- It's primarily used to get the outcome of previously initiated Zcash shielded operations.
- The operation is removed from memory after the result is retrieved.

### Input Parameters
- `operation_ids`: (Optional) A list of operation ids to query. If not provided, the endpoint examines all operations known to the node.

### Example Request
- `GET /z_getoperationresult?operation_ids=["opid-1234", "opid-5678"]`

### Response
- Returns a JSON array containing the results of the queried operations.

### Example Response
```json
{
    "operation_results": [
        {
            "id": "opid-1234",
            "status": "success",
            "creation_time": 1622547600,
            "result": {
                "txid": "2f5b0e..."
            },
            "error": null,
            "method": "z_sendmany",
            "params": {
                "fromaddress": "tm...",
                "amounts": [
                    {
                        "amount": 0.1,
                        "address": "tm..."
                    }
                ]
            }
        }
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The endpoint is specific to Zcash-based operations and is not applicable to standard Bitcoin transactions.""",
            response_description="A list of results for the completed Zcash operations")
async def z_getoperationresult(operation_ids: Optional[List[str]] = None,
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    operation_results = await rpc_connection.z_getoperationresult(operation_ids)
    return ZGetOperationResultResponse(operation_results=operation_results)






@router.get("/z_getoperationstatus",
            response_model=GetOperationStatusResponse,
            tags=["Utility Methods"],
            summary="Get the status of asynchronous operations",
            description="""Get the status and any associated results or errors for asynchronous operations.

### Description
- This endpoint returns the status and any results or error data for asynchronous operations, such as those initiated by the `z_sendmany` or `z_shieldcoinbase` methods.
- Operations will remain in memory even after completion.

### Input Parameters
- `operation_ids`: (Optional) A list of operation IDs to query. If not provided, information about all operations known to the node is returned.

### Example Request
- `GET /z_getoperationstatus?operation_ids=["opid-1a2b3c", "opid-4d5e6f"]`

### Response
- Returns a JSON array of objects, each representing the status of an operation.

### Example Response
```json
{
    "operations": [
        {
            "id": "opid-1a2b3c",
            "status": "success",
            "creation_time": 1617754083,
            "method": "z_sendmany",
            "params": { ... },
            "result": { ... },
            "error": null,
            "execution_secs": 2.345,
            "method_finished": true
        },
        {
            "id": "opid-4d5e6f",
            "status": "executing",
            "creation_time": 1617754090,
            "method": "z_shieldcoinbase",
            "params": { ... },
            "result": null,
            "error": null,
            "execution_secs": null,
            "method_finished": false
        }
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the provided operation IDs are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for tracking the progress and outcome of operations that do not provide immediate results.""",
            response_description="Status information about one or more operations")
async def z_get_operation_status(operation_ids: Optional[List[str]] = None, 
                                 rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.z_getoperationstatus(operation_ids)
    return GetOperationStatusResponse(operations=response)







@router.post("/z_sendmany",
             response_model=SendManyResponse,
             tags=["Raw Transaction Methods"],
             summary="Send multiple times to multiple recipients",
             description="""Send multiple times to multiple recipients. This endpoint allows for sending transactions to multiple addresses.

### Description
- Allows for sending specified amounts to multiple taddr or zaddr addresses from a single fromaddress.

### Input Parameters
- `SendManyRequest`: A JSON object containing the sending address, a list of recipient addresses with amounts and optional memos, minimum confirmations, and an optional fee.

### Request JSON Format
```json
{
    "fromaddress": "t1XYZ...",
    "amounts": [
        {"address": "t1ABC...", "amount": 0.1, "memo": "Optional memo"},
        {"address": "t1DEF...", "amount": 0.2}
    ],
    "minconf": 1,
    "fee": 0.0001
}
```

### Response
- Returns a JSON object containing the operation ID of the send operation.

### Example Response
```json
{
    "operationid": "opid-1234567890abcdef"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used for creating complex transactions involving multiple recipients.""",
             response_description="Operation ID of the send operation")
async def z_send_many(request: SendManyRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    operation_id = await rpc_connection.z_sendmany(request.fromaddress, request.amounts, request.minconf, request.fee)
    return SendManyResponse(operationid=operation_id)







@router.post("/z_shieldcoinbase",
             response_model=ZShieldCoinbaseResponse,
             tags=["Blockchain Methods"],
             summary="Shield transparent coinbase funds to a shielded zaddr",
             description="""Shield transparent coinbase funds by sending them to a shielded z-address. 
                            This is an asynchronous operation, and UTXOs selected for shielding will be locked.

### Description
- Shields coinbase UTXOs from a transparent address (taddr) to a shielded address (zaddr), locking the UTXOs involved in the process.

### Input Parameters
- `fromaddress`: The source transparent address or "*" for all taddrs belonging to the wallet.
- `toaddress`: The destination shielded address.
- `fee`: (Optional) The fee amount to attach to this transaction.
- `limit`: (Optional) The maximum number of UTXOs to shield. Set to 0 to shield as many as will fit in the transaction.

### Request JSON Format
```json
{
    "fromaddress": "t1exampleaddress...",
    "toaddress": "zs1exampleaddress...",
    "fee": 0.0001,
    "limit": 50
}
```

### Response
- Returns a JSON object containing details about the shielding process including the operation id.

### Example Response
```json
{
    "remainingUTXOs": 100,
    "remainingValue": 2.5,
    "shieldingUTXOs": 50,
    "shieldingValue": 1.5,
    "opid": "opid-example-1234"
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
             response_description="Details of the coinbase shielding operation")
async def z_shieldcoinbase(request: ZShieldCoinbaseRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Extract data from request body
    fromaddress = request.fromaddress
    toaddress = request.toaddress
    fee = request.fee
    limit = request.limit

    # Call the RPC method
    result = await rpc_connection.z_shieldcoinbase(fromaddress, toaddress, fee, limit)
    return ZShieldCoinbaseResponse(**result)







@router.post("/z_mergetoaddress",
             response_model=MergeToAddressResponse,
             tags=["Raw Transaction Methods"],
             summary="Merge multiple UTXOs and notes into a single UTXO or note",
             description="""Merge multiple UTXOs and notes into a single UTXO or note.

### Description
- This endpoint merges multiple UTXOs and notes into a single UTXO or note. Coinbase UTXOs are ignored; use `z_shieldcoinbase` to combine those into a single note.
- It's an asynchronous operation, and UTXOs selected for merging will be locked. If there is an error, they are unlocked.
- The number of UTXOs and notes selected for merging can be limited by the caller.

### Input Parameters
- `fromaddresses`: List of addresses. Special strings "ANY_TADDR" and "ANY_SAPLING" can be used.
- `toaddress`: The address to send the funds to.
- `fee`: Optional fee amount to attach to this transaction.
- `transparent_limit`: Optional limit on the number of UTXOs to merge.
- `shielded_limit`: Optional limit on the number of notes to merge.
- `memo`: Optional memo, encoded as hex, applicable only for zaddr.

### Example Request
```json
{
  "fromaddresses": ["ANY_SAPLING", "t1XYZ"],
  "toaddress": "t1ABC",
  "fee": 0.001,
  "transparent_limit": 50,
  "shielded_limit": 200,
  "memo": "48656c6c6f"
}
```

### Response
- Detailed information about the merge operation, including the number of UTXOs and notes merged, remaining ones, and the operation ID.

### Possible Errors
- HTTP 400: Bad Request for invalid parameters.
- HTTP 500: Internal Server Error for processing issues.""",
             response_description="Details of the merge operation")
async def z_mergetoaddress(request: MergeToAddressRequest, 
                           rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.z_mergetoaddress(
        request.fromaddresses, 
        request.toaddress, 
        request.fee, 
        request.transparent_limit, 
        request.shielded_limit, 
        request.memo
    )
    return MergeToAddressResponse(**response)





@router.get("/z_listoperationids",
            response_model=ZListOperationIdsResponse,
            tags=["Blockchain Methods"],
            summary="List Operation IDs",
            description="""List all operation IDs currently known to the wallet.

### Description
- This endpoint retrieves a list of operation IDs that are known to the wallet. 
  It can optionally filter these IDs based on the operation's state.

### Input Parameters
- `status`: (Optional) A string to filter the operation IDs by their state, e.g., "success".

### Example Request
- `GET /z_listoperationids?status=success`

### Response
- Returns a JSON array containing the operation IDs.

### Example Response
```json
{
    "operation_ids": ["opid-1", "opid-2", "opid-3"]
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for tracking and managing asynchronous operations performed by the wallet.""",
            response_description="List of operation IDs")
async def z_list_operation_ids(status: Optional[str] = None, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    operation_ids = await rpc_connection.z_listoperationids(status)
    return ZListOperationIdsResponse(operation_ids=operation_ids)






@router.get("/z_getnotescount",
            response_model=ZGetNotesCountResponse,
            tags=["Utility Methods"],
            summary="Get the count of sapling notes in the wallet",
            description="""Get the count of sapling notes in the wallet.

### Description
- This endpoint returns the number of sapling notes available in the wallet.
- It includes notes in transactions confirmed at least a specified number of times.

### Input Parameters
- `minconf`: (Optional, numeric) Only include notes in transactions confirmed at least this many times. Default is 1.

### Example Request
- `GET /z_getnotescount?minconf=1`

### Response
- Returns a JSON object containing the count of sapling notes in the wallet.

### Example Response
```json
{
    "sapling": 5
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for assessing the number of sapling notes held in the wallet.""",
            response_description="The count of sapling notes in the wallet")
async def z_get_notes_count(minconf: int = 1, 
                            rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    notes_count = await rpc_connection.z_getnotescount(minconf)
    return ZGetNotesCountResponse(sapling=notes_count['sapling'])







@router.get("/gettxfee/{txid}", 
            response_model=GetTxfeeResponse, 
            tags=["Blockchain Methods"],
            summary="Get transaction fee by txid",
            description="""Get the transaction fee for a specific transaction by its transaction ID (txid).

### Description
- This endpoint retrieves the transaction fee for a given transaction ID in the Pastel blockchain.

### Input Parameters
- `txid`: The transaction ID for which the transaction fee is requested.

### Example Request
- `GET /gettxfee/e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4`

### Response
- Returns a JSON object containing details of the transaction fee.

### Example Response
```json
{
    "txid": "e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4",
    "height": 123456,
    "blockHash": "00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e",
    "txFeePat": 50000,
    "txFee": 0.0005
}
```

### Possible Errors
- HTTP 400: Bad Request if the txid is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for wallets and explorers to determine the fee associated with a particular transaction.""",
            response_description="Details of the transaction fee for the given txid")
async def get_txfee(txid: str, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    transaction_fee_info = await rpc_connection.gettxfee(txid)
    return GetTxfeeResponse(**transaction_fee_info)






@router.post("/scanformissingtxs",
            response_model=ScanForMissingTxsResponse,
            tags=["Utility Methods"],
            summary="Scan for missing transactions",
            description="""Scan the wallet for missing transactions starting from a specified block height.

### Description
- This endpoint scans the wallet for transactions that might be missing, starting from a given block height. It helps in ensuring the wallet's transaction history is complete and up-to-date.

### Input Parameters
- `starting_height`: (numeric, required) The block height from which to start scanning for missing transactions.

### Example Request
- `POST /scanformissingtxs` with payload `{"starting_height": 100000}`

### Response
- Returns a JSON object containing a list of transaction IDs for transactions that are missing in the wallet.

### Example Response
```json
{
    "missing_txs": [
        "missing_transaction1_txid",
        "missing_transaction2_txid"
        // ... more transaction IDs ...
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the `starting_height` is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Useful for wallet recovery and maintenance purposes.""",
            response_description="List of missing transaction IDs")
async def scan_for_missing_txs(request: ScanForMissingTxsRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    missing_txs = await rpc_connection.scanformissingtxs(request.starting_height)
    return ScanForMissingTxsResponse(missing_txs=missing_txs)






@router.get("/fixmissingtxs/{starting_height}",
            response_model=FixMissingTransactionsResponse,
            tags=["Blockchain Methods"],
            summary="Fix Missing Transactions",
            description="""Scan for missing transactions in the wallet starting from the given height and add to the wallet all missing transactions found in the blockchain.

### Description
- Scans the blockchain starting from the specified block height for any transactions that are missing in the wallet and adds them.

### Input Parameters
- `starting_height`: (integer, required) The block height from which the scan for missing transactions should begin.

### Example Request
- `GET /fixmissingtxs/100000`

### Response
- Returns a JSON array of transaction IDs for transactions that were missing in the wallet and have been added.

### Example Response
```json
{
    "missing_transactions": ["missing_transaction1_txid", "missing_transaction2_txid", ...]
}
```

### Possible Errors
- HTTP 400: Bad Request if the starting height is invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This endpoint is useful for wallet recovery and synchronization purposes.""",
            response_description="List of missing transaction IDs added to the wallet")
async def fix_missing_transactions(starting_height: int, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    missing_txs = await rpc_connection.fixmissingtxs(starting_height)
    return FixMissingTransactionsResponse(missing_transactions=missing_txs)







@router.post("/storagefee/setfee",
             response_model=StorageFeeSetFeeResponse,
             tags=["Control Methods"],
             summary="Set a new fee for a specified fee type",
             description="""Set a new fee for various types of fees in the masternode system.

### Description
- This endpoint allows setting a new fee for storage, ticket, sense-compute, or sense-processing.
- It requires an active masternode to execute.

### Input Parameters
- `fee_type`: The type of fee to set. Valid types are 'storage', 'ticket', 'sense-compute', and 'sense-processing'.
- `new_fee`: (Optional) The new fee amount to set. If not specified, the current fee for the specified type will be maintained.

### Example Request
```json
{
    "fee_type": "storage",
    "new_fee": 100
}
```

### Response
- Returns a JSON object indicating the success of the operation.

### Example Response
```json
{
    "success": true
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid or the fee type is not recognized.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
- HTTP 403: Forbidden if the request is not made by an active masternode.""",
             response_description="Result of setting the new fee")
async def storagefee_setfee(request: StorageFeeSetFeeRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.storagefee_setfee(request.fee_type, request.new_fee)
    return StorageFeeSetFeeResponse(success=result)








@router.get("/storagefee/getfee",
            response_model=StorageFeeGetFeeResponse,
            tags=["Utility Methods"],
            summary="Get the storage fee",
            description="""Get the current storage fee based on the specified fee type and blockchain height.

### Description
- This endpoint returns the current storage fee based on the given fee type, optional local/global flag, and blockchain height.

### Input Parameters
- `fee_type`: The type of fee to retrieve (e.g., "nftTicketFee").
- `is_local`: (Optional) A boolean to specify if the fee is local or global. Defaults to `False`.
- `height`: (Optional) The blockchain height for which to retrieve the fee. If not provided, the current height is used.

### Example Request
- `GET /storagefee/getfee?fee_type=nftTicketFee&is_local=true&height=100000`

### Response
- Returns a JSON object containing the storage fee, fee in 'pat' units, blockchain height, and chain deflator factor.

### Example Response
```json
{
    "fee": 0.002,
    "fee_pat": 200000,
    "height": 100000,
    "chain_deflator_factor": 1.5
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used to determine the current storage fee for various operations on the blockchain.""",
            response_description="Current storage fee details")
async def get_storage_fee_get_fee(fee_type: str, is_local: Optional[bool] = False, height: Optional[int] = None, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    fee_info = await rpc_connection.storagefee_getfee(fee_type, is_local, height)
    return StorageFeeGetFeeResponse(
        fee=fee_info['fee'],
        fee_pat=fee_info['fee_pat'],
        height=fee_info['height'],
        chain_deflator_factor=fee_info['chain_deflator_factor']
    )
    
    
    
    
    
    
@router.get("/storagefee/getfees",
            response_model=GetFeesResponse,
            tags=["Utility Methods"],
            summary="Get the current storage fees",
            description="""Get the current storage fees adjusted by the network median and local factors.

### Description
- This endpoint returns the current storage fees based on the network's median fee and local fee for various actions.
- The fees are adjusted by a fee deflator factor, which is based on the blockchain's state.

### Input Parameters
- None: This endpoint does not require any input parameters.

### Example Request
- `GET /storagefee/getfees`

### Response
- Returns a JSON object containing storage fees for different actions.

### Example Response
```json
{
    "height": 12345,
    "chain_deflator_factor": 1.5,
    "fees": {
        "actionName": {
            "fee": 100,
            "fee_pat": 100000
        },
        ...
    }
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Current storage fees adjusted by network and local factors")
async def get_storage_fees(rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.storagefee_getfees()
    return GetFeesResponse(**response)






@router.get("/storagefee/getactionfees",
            response_model=GetActionFeesResponse,
            tags=["Utility Methods"],
            summary="Get action fees based on data size",
            description="""Get action fees based on data size.

### Description
- This endpoint calculates the action fees based on the given data size in MB.

### Input Parameters
- `data_size`: (Required) Data size in MB.
- `height`: (Optional) Block height to get action fees for.

### Example Request
- `GET /storagefee/getactionfees?data_size=10&height=12345`

### Response
- Returns a JSON object containing action fees for different actions based on the data size.

### Example Response
```json
{
    "datasize": 10,
    "height": 12345,
    "fee_deflator_factor": 1.5,
    "action_fees": {
        "actionTypeFee": 200,
        "actionTypeFeePat": 200000,
        ...
    }
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.""",
            response_description="Action fees based on data size")
async def get_action_fees(data_size: int, height: Optional[int] = None,
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.storagefee_getactionfees(data_size, height)
    return GetActionFeesResponse(**response)    







@router.post("/storagefee",
             response_model=StorageFeeResponse,
             tags=["Control Methods"],
             summary="Interact with Storage Fee and related actions",
             description="""Interact with various Storage Fee and related actions in the Pastel network.

### Description
- This endpoint allows interaction with various aspects of storage fees and related actions.

### Input Parameters
- `command`: The storage fee command to execute.
- `params`: Parameters for the specified command.

### Example Request
```json
{
    "command": "getstoragefee",
    "params": {"is_local": true, "height": 1000}
}
```

### Response
- Returns a JSON object containing the result of the storage fee command.

### Example Response
```json
{
    "result": {
        "storage_fee": "0.001",
        "height": 1000
    }
}
```

### Possible Errors
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Result of the storage fee command")
async def storage_fee(command: str, params: dict, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.storagefee(command, **params)
    return StorageFeeResponse(result=response)







@router.post("/pastelid_newkey",
             response_model=PastelIDNewKeyResponse,
             tags=["Utility Methods"],
             summary="Generate new Pastel ID and associated keys",
             description="""Generate a new Pastel ID and associated keys (EdDSA448) and LegRoast signing keys.

### Description
- This endpoint generates a new Pastel ID, which is a unique identifier for a user or entity on the Pastel network.
- The endpoint also generates associated cryptographic keys using EdDSA448 and LegRoast algorithms.
- The generated Pastel ID is base58-encoded.

### Input Parameters
- `passphrase`: A passphrase used for generating the new key. It cannot be empty.

### Example Request
- `POST /pastelid_newkey` with JSON body `{"passphrase": "your_passphrase"}`

### Response
- Returns a JSON object containing the newly generated Pastel ID and LegRoast key.

### Example Response
```json
{
    "pastelid": "base58EncodedPastelID",
    "legroast": "base58EncodedLegRoastKey"
}
```

### Possible Errors
- HTTP 400: Bad Request if the passphrase is empty or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- This function is essential for user registration and identity management within the Pastel network.""",
             response_description="Newly generated Pastel ID and LegRoast key")
async def pastelid_newkey(request: PastelIDNewKeyRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.pastelid_newkey(request.passphrase)
    return PastelIDNewKeyResponse(pastelid=result['pastelid'], legroast=result['legroast'])






@router.post("/pastelid/sign",
             response_model=PastelIDSignResponse,
             tags=["Utility Methods"],
             summary="Sign a text with Pastel ID",
             description="""Sign a text using the private key associated with a Pastel ID.

### Description
- Signs a provided text using the private key corresponding to the specified Pastel ID.

### Input Parameters
- `text`: The text to be signed.
- `pastel_id`: The Pastel ID used for signing.
- `passphrase`: The passphrase for the private key.
- `algorithm`: (Optional) The signing algorithm, either 'ed448' (default) or 'legroast'.

### Request JSON Format
```json
{
    "text": "Example text",
    "pastel_id": "pastel_id_example",
    "passphrase": "secure_passphrase",
    "algorithm": "ed448"
}
```

### Response
- Returns a JSON object containing the signature of the text.

### Example Response
```json
{
    "signature": "generated_signature"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Signature of the provided text")
async def sign_with_pastel_id(sign_request: PastelIDSignRequest, rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    signature = await rpc_connection.pastelid_sign(
        sign_request.text, 
        sign_request.pastel_id, 
        sign_request.passphrase, 
        sign_request.algorithm
    )
    return PastelIDSignResponse(signature=signature)







@router.post("/pastelid/signfile",
             response_model=PastelIDSignFileResponse,
             tags=["Utility Methods"],
             summary="Sign a file with a Pastel ID",
             description="""Sign a file with the internally stored private key associated with a Pastel ID.

### Description
- This endpoint allows users to sign a file using their Pastel ID. The file is specified by its path, and the signature is generated using the private key associated with the given Pastel ID.
- Supported algorithms are 'ed448' (default) and 'legroast'.

### Input Parameters
- `file_path`: Path to the file that needs to be signed.
- `pastel_id`: The Pastel ID to use for signing.
- `passphrase`: The passphrase for the private key.
- `algorithm`: (Optional) The algorithm to use for signing, either 'ed448' or 'legroast'.

### Example Request
```json
{
    "file_path": "/path/to/file",
    "pastel_id": "jXYWV...",
    "passphrase": "your_passphrase",
    "algorithm": "ed448"
}
```

### Response
- Returns a JSON object containing the signature of the file.

### Example Response
```json
{
    "signature": "HJG98uFomw..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The private key must be stored internally and associated with the specified Pastel ID.""",
             response_description="The signature of the file")
async def pastelid_sign_file(request: PastelIDSignFileRequest, 
                             rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.pastelid_sign_file(request.file_path, 
                                                        request.pastel_id, 
                                                        request.passphrase.get_secret_value(), 
                                                        request.algorithm)
    return PastelIDSignFileResponse(signature=result["signature"])







@router.post("/pastelid/verify",
             response_model=PastelIDVerifyResponse,
             tags=["Utility Methods"],
             summary="Verify a signature with PastelID",
             description="""Verify a text's signature using the private key associated with the PastelID.

### Description
- This endpoint verifies the signature of a given text using the private key associated with a specified PastelID.
- It supports two algorithms: `ed448` and `legroast`.

### Input Parameters
- `text`: The text (or base64-encoded text) to be verified.
- `signature`: The signature of the text.
- `pastelid`: The PastelID used for verification.
- `algorithm`: (Optional) The algorithm used for signing (`ed448` or `legroast`). Default is `ed448`.

### Example Request
```json
{
    "text": "Hello World",
    "signature": "signature123",
    "pastelid": "pastelid123",
    "algorithm": "ed448"
}
```

### Response
- Returns a JSON object indicating whether the verification was successful or not.

### Example Response
```json
{
    "verification": "OK"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Verification failure does not always imply the data or signature is incorrect; it might also indicate an issue with the algorithm used.""",
             response_description="Result of the verification process")
async def pastelid_verify(request: PastelIDVerifyRequest,
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.pastelid_verify(request.text, request.signature, request.pastelid, request.algorithm)
    return PastelIDVerifyResponse(verification="OK" if result else "Failed")






@router.post("/pastelid/verify-file",
             response_model=PastelIDVerifyFileResponse,
             tags=["Utility Methods"],
             summary="Verify a file's signature with a Pastel ID",
             description="""Verify a file's signature with the private key associated with a Pastel ID.

### Description
- This endpoint verifies the signature of a file using a Pastel ID. It supports two algorithms: ed448 or legroast.

### Input Parameters
- `file_path`: Path to the file whose signature needs to be verified.
- `signature`: The signature string to verify.
- `pastelid`: The Pastel ID associated with the private key.
- `algorithm`: (Optional) The algorithm used for signing (ed448 or legroast). Default is ed448.

### Example Request
```json
{
    "file_path": "/path/to/file",
    "signature": "signature_string",
    "pastelid": "pastel_id_string",
    "algorithm": "ed448"
}
```

### Response
- Returns a JSON object indicating whether the verification was successful or failed.

### Example Response
```json
{
    "verification": "OK"
}
```

### Possible Errors
- HTTP 400: Bad Request if input parameters are missing or invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Used for validating the authenticity of a file using a Pastel ID.""",
             response_description="Result of the file verification")
async def pastelid_verify_file(file_path: str, signature: str, pastelid: str, algorithm: Optional[str] = "ed448", rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    result = await rpc_connection.pastelid_verify_file(file_path, signature, pastelid, algorithm)
    return PastelIDVerifyFileResponse(verification=result["verification"])







@router.post("/pastelid/passwd",
            response_model=PastelIDPasswdResponse,
            tags=["Utility Methods"],
            summary="Change passphrase for PastelID secure container",
            description="""Change the passphrase used to encrypt the secure container associated with the PastelID.

### Description
- This endpoint is used to update the passphrase of the secure container for a given PastelID.
- The secure container is encrypted, and this operation changes its encryption passphrase.

### Input Parameters
- `pastelid`: The PastelID for which the passphrase needs to be changed.
- `old_passphrase`: The current passphrase of the secure container.
- `new_passphrase`: The new passphrase to set for the secure container.

### Example Request
```json
POST /pastelid/passwd
{
    "pastelid": "jX9NfXhvnUJwDzB2z0wh",
    "old_passphrase": "currentpass",
    "new_passphrase": "newpass"
}
```

### Response
- Returns a JSON object indicating the success of the operation.

### Example Response
```json
{
    "result": "success"
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid or missing.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
            response_description="Status of the passphrase change operation")
async def pastelid_passwd(request: PastelIDPasswdRequest,
                          rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.pastelid_passwd(request.pastelid, request.old_passphrase, request.new_passphrase)
    return PastelIDPasswdResponse(result=response.result)







@router.post("/pastelid/newkey",
             response_model=PastelIDNewKeyResponse,
             tags=["Utility Methods"],
             summary="Generate new Pastel ID and keys",
             description="""Generate a new Pastel ID and associated keys (EdDSA448 and LegRoast signing keys).

### Description
- This endpoint generates a new Pastel ID and associated keys using the specified passphrase for encryption.

### Input Parameters
- `passphrase`: A string passphrase used to encrypt the key file.

### Example Request
```json
{
    "passphrase": "your_secure_passphrase"
}
```

### Response
- Returns a JSON object containing the Pastel ID and public key in base58-encoded format.

### Example Response
```json
{
    "pastel_id": "paxxxxxxxxxxxxxxxxxxxxxx",
    "public_key": "pubxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

### Possible Errors
- HTTP 400: Bad Request if the input parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.
""",
             response_description="Pastel ID and associated public key")
async def generate_pastel_id_newkey(request: PastelIDNewKeyRequest,
                                    rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    response = await rpc_connection.pastelid("newkey", request.passphrase)
    return PastelIDNewKeyResponse(pastel_id=response['pastel_id'], public_key=response['public_key'])








@router.get("/tickets/list",
            response_model=TicketsListResponse,
            tags=["Ticket Methods"],
            summary="List tickets of a specific type",
            description="""List all tickets of a specific type registered in the system.

### Description
- This endpoint allows querying different types of tickets in the Pastel network, such as PastelID, NFT, and Act tickets. 
- It supports various filters to narrow down the results based on specific criteria.

### Input Parameters
- `ticket_type`: The type of ticket to list. Example: 'id', 'nft', 'act', etc.
- `filter`: Optional filter to apply when listing tickets. Example: 'all', 'active', 'inactive', etc.
- `min_height`: Optional minimum block height for returned tickets.

### Example Request
- `GET /tickets/list?ticket_type=id&filter=all&min_height=250000`

### Response
- Returns a JSON object containing a list of tickets as per the requested type and filters.

### Example Response
```json
{
    "tickets": [
        {
            "ticket_type": "id",
            "ticket_details": {...}
        },
        ...
    ]
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are incorrect.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- The endpoint's flexibility allows for extensive querying capabilities across different ticket types.""",
            response_description="List of tickets as per the requested type and filters")
async def list_tickets(
    ticket_type: str, 
    filter: Optional[str] = None, 
    min_height: Optional[int] = None,
    rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)
):
    tickets = await rpc_connection.tickets_list(ticket_type, filter, min_height)
    return TicketsListResponse(tickets=tickets)







@router.post("/masternodebroadcast",
             response_model=MasternodeBroadcastResponse,
             tags=["Supernode Methods"],
             summary="Create and relay masternode broadcast messages",
             description="""Set of commands to create and relay masternode broadcast messages.

### Description
- This endpoint is used for creating and relaying masternode broadcast messages. It supports multiple commands for different operations related to masternode broadcasts.

### Input Parameters
- `command`: (String) The command to execute. Available commands: create-alias, create-all, decode, relay.
- `parameters`: (String, Optional) Additional parameters based on the command.
- `fast`: (Boolean, Optional) If set to true, uses a fast method for the 'relay' command.

### Example Request
- `POST /masternodebroadcast` with JSON body `{"command": "create-alias", "parameters": "aliasName"}`

### Response
- Returns a JSON object containing details of the operation based on the command executed.

### Example Response
```json
{
    "overall": "Successfully created broadcast messages for 1 masternodes, failed to create 0, total 1",
    "detail": [
        {
            "outpoint": "0000000000000000000000000000000000000000000000000000000000000000-1",
            "addr": "127.0.0.1:9933",
            "error_message": null
        }
    ],
    "hex": "0100000000abcdef..."
}
```

### Possible Errors
- HTTP 400: Bad Request if the parameters are invalid.
- HTTP 500: Internal Server Error if there's an issue in processing the request.

### Note
- Depending on the command, the response structure may vary.""",
             response_description="Details of the masternode broadcast operation")
async def masternode_broadcast(request: MasternodeBroadcastRequest, 
                               rpc_connection: service_functions.AsyncAuthServiceProxy = Depends(get_rpc_connection)):
    # Logic to interact with your RPC class based on the command
    if request.command == "create-alias":
        response = await rpc_connection.masternodebroadcast("create-alias", request.parameters)
    elif request.command == "create-all":
        response = await rpc_connection.masternodebroadcast("create-all")
    elif request.command == "decode":
        response = await rpc_connection.masternodebroadcast("decode", request.parameters)
    elif request.command == "relay":
        response = await rpc_connection.masternodebroadcast("relay", request.parameters, request.fast)
    else:
        logger.error("Invalid command")
    return MasternodeBroadcastResponse(**response)





