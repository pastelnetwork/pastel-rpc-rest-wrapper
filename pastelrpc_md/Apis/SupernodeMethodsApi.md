# SupernodeMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**executeMasternodeCommandMasternodeCommandPost**](SupernodeMethodsApi.md#executeMasternodeCommandMasternodeCommandPost) | **POST** /masternode/command | Execute masternode related actions |
| [**initializeMasternodeMasternodeInitPost**](SupernodeMethodsApi.md#initializeMasternodeMasternodeInitPost) | **POST** /masternode/init | Initialize masternode |
| [**listMasternodeOutputsMasternodeOutputsGet**](SupernodeMethodsApi.md#listMasternodeOutputsMasternodeOutputsGet) | **GET** /masternode/outputs | List masternode outputs |
| [**masternodeBroadcastMasternodebroadcastPost**](SupernodeMethodsApi.md#masternodeBroadcastMasternodebroadcastPost) | **POST** /masternodebroadcast | Create and relay masternode broadcast messages |
| [**masternodeClearCacheMasternodeClearCachePost**](SupernodeMethodsApi.md#masternodeClearCacheMasternodeClearCachePost) | **POST** /masternode/clear-cache | Clear Masternode Cache Items |
| [**masternodeMakeConfMasternodeMakeConfPost**](SupernodeMethodsApi.md#masternodeMakeConfMasternodeMakeConfPost) | **POST** /masternode/make_conf | Create Masternode Configuration |
| [**masternodeMessageMasternodeMessagePost**](SupernodeMethodsApi.md#masternodeMessageMasternodeMessagePost) | **POST** /masternode/message | Interact with Masternode messages |
| [**masternodePoseBanScoreMasternodePoseBanScorePost**](SupernodeMethodsApi.md#masternodePoseBanScoreMasternodePoseBanScorePost) | **POST** /masternode_pose_ban_score | Manage MasterNode PoSe Ban Score |
| [**masternodelistMasternodelistGet**](SupernodeMethodsApi.md#masternodelistMasternodelistGet) | **GET** /masternodelist | Get a list of masternodes in different modes |


<a name="executeMasternodeCommandMasternodeCommandPost"></a>
# **executeMasternodeCommandMasternodeCommandPost**
> Response_Execute_Masternode_Command_Masternode_Command_Post executeMasternodeCommandMasternodeCommandPost(MasternodeCommandRequest)

Execute masternode related actions

    Execute various masternode related actions based on the provided command.  ### Description - This endpoint allows for executing different masternode related commands such as count, current, winner, genkey, and others.  ### Input Parameters - &#x60;command&#x60;: The masternode command to execute. - &#x60;additional_args&#x60;: Additional arguments required for specific commands.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;count\&quot;,     \&quot;additional_args\&quot;: {\&quot;count_type\&quot;: \&quot;enabled\&quot;} } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result based on the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;count\&quot;: 150 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the command or additional arguments are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeCommandRequest** | [**MasternodeCommandRequest**](../Models/MasternodeCommandRequest.md)|  | |

### Return type

[**Response_Execute_Masternode_Command_Masternode_Command_Post**](../Models/Response_Execute_Masternode_Command_Masternode_Command_Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="initializeMasternodeMasternodeInitPost"></a>
# **initializeMasternodeMasternodeInitPost**
> MasternodeInitResponse initializeMasternodeMasternodeInitPost(MasternodeInitRequest)

Initialize masternode

    Initialize masternode with existing outpoint (collateral txid &amp; index).  ### Description - Initializes a masternode with the provided collateral from the local wallet.    Generates new Pastel ID, registers mnid, and generates masternode private key.  ### Input Parameters - &#x60;passphrase&#x60;: Passphrase for new PastelID. - &#x60;txid&#x60;: ID of transaction with the collateral amount. - &#x60;index&#x60;: Index in the transaction with the collateral amount.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;secure-passphrase\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 4 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the generated and registered Pastel ID and other key details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;mnid\&quot;: \&quot;Generated and registered Pastel ID\&quot;,     \&quot;legRoastKey\&quot;: \&quot;Generated and registered LegRoast private key\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;outIndex\&quot;: 4,     \&quot;privKey\&quot;: \&quot;Generated masternode private key\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeInitRequest** | [**MasternodeInitRequest**](../Models/MasternodeInitRequest.md)|  | |

### Return type

[**MasternodeInitResponse**](../Models/MasternodeInitResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listMasternodeOutputsMasternodeOutputsGet"></a>
# **listMasternodeOutputsMasternodeOutputsGet**
> MasternodeOutputsResponse listMasternodeOutputsMasternodeOutputsGet()

List masternode outputs

    List masternode outputs (collateral txid+index).  ### Description - This endpoint lists possible coin candidates for masternode collateral,    including transaction ID and index of each output.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /masternode/outputs&#x60;  ### Response - Returns a JSON object containing the masternode outputs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;outputs\&quot;: {         \&quot;txid1\&quot;: \&quot;index1\&quot;,         \&quot;txid2\&quot;: \&quot;index2\&quot;,         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**MasternodeOutputsResponse**](../Models/MasternodeOutputsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="masternodeBroadcastMasternodebroadcastPost"></a>
# **masternodeBroadcastMasternodebroadcastPost**
> MasternodeBroadcastResponse masternodeBroadcastMasternodebroadcastPost(MasternodeBroadcastRequest)

Create and relay masternode broadcast messages

    Set of commands to create and relay masternode broadcast messages.  ### Description - This endpoint is used for creating and relaying masternode broadcast messages. It supports multiple commands for different operations related to masternode broadcasts.  ### Input Parameters - &#x60;command&#x60;: (String) The command to execute. Available commands: create-alias, create-all, decode, relay. - &#x60;parameters&#x60;: (String, Optional) Additional parameters based on the command. - &#x60;fast&#x60;: (Boolean, Optional) If set to true, uses a fast method for the &#39;relay&#39; command.  ### Example Request - &#x60;POST /masternodebroadcast&#x60; with JSON body &#x60;{\&quot;command\&quot;: \&quot;create-alias\&quot;, \&quot;parameters\&quot;: \&quot;aliasName\&quot;}&#x60;  ### Response - Returns a JSON object containing details of the operation based on the command executed.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;overall\&quot;: \&quot;Successfully created broadcast messages for 1 masternodes, failed to create 0, total 1\&quot;,     \&quot;detail\&quot;: [         {             \&quot;outpoint\&quot;: \&quot;0000000000000000000000000000000000000000000000000000000000000000-1\&quot;,             \&quot;addr\&quot;: \&quot;127.0.0.1:9933\&quot;,             \&quot;error_message\&quot;: null         }     ],     \&quot;hex\&quot;: \&quot;0100000000abcdef...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Depending on the command, the response structure may vary.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeBroadcastRequest** | [**MasternodeBroadcastRequest**](../Models/MasternodeBroadcastRequest.md)|  | |

### Return type

[**MasternodeBroadcastResponse**](../Models/MasternodeBroadcastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodeClearCacheMasternodeClearCachePost"></a>
# **masternodeClearCacheMasternodeClearCachePost**
> MasternodeClearCacheResponse masternodeClearCacheMasternodeClearCachePost(cache\_item)

Clear Masternode Cache Items

    Clear specific Masternode cache items.   ### Description - This endpoint clears specific cache items related to Masternodes in the network. The cache items include the masternode list, seen masternodes, recovery cache, asked masternode cache, and historical top masternodes cache.  ### Input Parameters - &#x60;cache_item&#x60;: A string specifying the cache item to clear. Possible values are &#39;all&#39;, &#39;mns&#39;, &#39;seen&#39;, &#39;recovery&#39;, &#39;asked&#39;, &#39;top-mns&#39;.  ### Example Request - &#x60;POST /masternode/clear-cache&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;cache_item\&quot;: \&quot;mns\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the status of the cache clearing operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;Cache cleared successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if an invalid cache item is provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is primarily used for network maintenance and troubleshooting.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cache\_item** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**MasternodeClearCacheResponse**](../Models/MasternodeClearCacheResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="masternodeMakeConfMasternodeMakeConfPost"></a>
# **masternodeMakeConfMasternodeMakeConfPost**
> MasternodeMakeConfResponse masternodeMakeConfMasternodeMakeConfPost(MasternodeMakeConfRequest)

Create Masternode Configuration

    Create masternode configuration in JSON format.   ### Description - Generates MasterNode Private Key (mnPrivKey) and registers MasterNode PastelID (extKey). - If collateral txid and index are not provided, searches for the first available non-locked outpoint with the correct amount (1000000 PSL).  ### Input Parameters - &#x60;alias&#x60;: Local alias (name) of the Master Node. - &#x60;mn_address&#x60;: The address and port of the Master Node&#39;s cNode. - &#x60;ext_address&#x60;: The address and port of the Master Node&#39;s Storage Layer. - &#x60;ext_p2p&#x60;: The address and port of the Master Node&#39;s Kademlia point. - &#x60;passphrase&#x60;: Passphrase for new Pastel ID. - &#x60;txid&#x60;: (Optional) ID of transaction with the collateral amount. - &#x60;index&#x60;: (Optional) Index in the transaction with the collateral amount.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;alias\&quot;: \&quot;myMN\&quot;,     \&quot;mn_address\&quot;: \&quot;127.0.0.1:9933\&quot;,     \&quot;ext_address\&quot;: \&quot;127.0.0.1:4444\&quot;,     \&quot;ext_p2p\&quot;: \&quot;127.0.0.1:5545\&quot;,     \&quot;passphrase\&quot;: \&quot;securepassphrase\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 4 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the Masternode configuration details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;alias\&quot;: \&quot;myMN\&quot;,     \&quot;config\&quot;: {         \&quot;mn_address\&quot;: \&quot;127.0.0.1:9933\&quot;,         \&quot;ext_address\&quot;: \&quot;127.0.0.1:4444\&quot;,         \&quot;ext_p2p\&quot;: \&quot;127.0.0.1:5545\&quot;,         \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,         \&quot;out_index\&quot;: \&quot;4\&quot;,         \&quot;mn_priv_key\&quot;: \&quot;generatedPrivateKey\&quot;,         \&quot;ext_key\&quot;: \&quot;generatedPastelID\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used for setting up new Masternodes on the network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeMakeConfRequest** | [**MasternodeMakeConfRequest**](../Models/MasternodeMakeConfRequest.md)|  | |

### Return type

[**MasternodeMakeConfResponse**](../Models/MasternodeMakeConfResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodeMessageMasternodeMessagePost"></a>
# **masternodeMessageMasternodeMessagePost**
> MasternodeMessageResponse masternodeMessageMasternodeMessagePost(MasternodeMessageRequest)

Interact with Masternode messages

    Allows sending, listing, printing, and signing messages using Masternode.  ### Description - This endpoint interacts with Masternode messages based on the specified operation.  ### Input Parameters - &#x60;operation&#x60;: The operation to perform (&#x60;send&#x60;, &#x60;list&#x60;, &#x60;print&#x60;, &#x60;sign&#x60;). - &#x60;pub_key&#x60;: The Masternode public key (required for &#x60;send&#x60; operation). - &#x60;message&#x60;: The message text (required for &#x60;send&#x60; and &#x60;sign&#x60; operations). - &#x60;message_id&#x60;: The message ID (required for &#x60;print&#x60; operation). - &#x60;additional_param&#x60;: Additional parameter (optional, used in &#x60;sign&#x60; operation).  ### Example Request - &#x60;POST /masternode/message&#x60;  ### Response - Returns a JSON object containing the result of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Success\&quot;,     \&quot;signature\&quot;: \&quot;abc123\&quot;,     \&quot;pubkey\&quot;: \&quot;def456\&quot;,     \&quot;messages\&quot;: {\&quot;msg1\&quot;: \&quot;Message content\&quot;} } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasternodeMessageRequest** | [**MasternodeMessageRequest**](../Models/MasternodeMessageRequest.md)|  | |

### Return type

[**MasternodeMessageResponse**](../Models/MasternodeMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodePoseBanScoreMasternodePoseBanScorePost"></a>
# **masternodePoseBanScoreMasternodePoseBanScorePost**
> MasterNodePoseBanScoreResponse masternodePoseBanScoreMasternodePoseBanScorePost(MasterNodePoseBanScoreRequest)

Manage MasterNode PoSe Ban Score

    Manage the Proof-Of-Service (PoSe) ban score for a MasterNode.  ### Description - This endpoint allows getting or incrementing the PoSe ban score of a specified MasterNode. - The MasterNode is identified by the transaction ID (txid) and index of its collateral transaction.  ### Input Parameters - &#x60;command&#x60;: The operation to perform - \&quot;get\&quot; to retrieve the current score or \&quot;increment\&quot; to increase it. - &#x60;txid&#x60;: The transaction ID of the MasterNode&#39;s collateral transaction. - &#x60;index&#x60;: The index of the collateral output in the transaction.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;get\&quot;,     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 1 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the MasterNode&#39;s PoSe ban score, ban status, and ban height if applicable.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726\&quot;,     \&quot;index\&quot;: 1,     \&quot;pose_ban_score\&quot;: 10,     \&quot;pose_banned\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MasterNodePoseBanScoreRequest** | [**MasterNodePoseBanScoreRequest**](../Models/MasterNodePoseBanScoreRequest.md)|  | |

### Return type

[**MasterNodePoseBanScoreResponse**](../Models/MasterNodePoseBanScoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="masternodelistMasternodelistGet"></a>
# **masternodelistMasternodelistGet**
> MasternodeListResponse masternodelistMasternodelistGet(mode, filter, allnodes)

Get a list of masternodes in different modes

    Get a list of masternodes in different modes.  ### Description - Retrieves information about masternodes based on the specified mode. Each mode provides different types of data about the masternodes.  ### Input Parameters - &#x60;mode&#x60; (string, optional): The mode to run the list in. Defaults to &#39;status&#39;. Available modes:   - &#x60;activeseconds&#x60;: Number of seconds the masternode has been recognized as enabled.   - &#x60;addr&#x60;: IP address associated with a masternode.   - &#x60;full&#x60;: Info in the format &#39;status protocol payee lastseen activeseconds lastpaidtime lastpaidblock IP&#39;.   - &#x60;info&#x60;: Info in the format &#39;status protocol payee lastseen activeseconds sentinelversion sentinelstate IP&#39;.   - &#x60;lastpaidblock&#x60;: The last block height a node was paid on the network.   - &#x60;lastpaidtime&#x60;: The last time a node was paid on the network.   - &#x60;lastseen&#x60;: Timestamp of when a masternode was last seen on the network.   - &#x60;payee&#x60;: Pastel address associated with a masternode.   - &#x60;protocol&#x60;: Protocol of a masternode.   - &#x60;pubkey&#x60;: Masternode (not collateral) public key.   - &#x60;rank&#x60;: Rank of a masternode based on current block.   - &#x60;status&#x60;: Masternode status (e.g., ENABLED, EXPIRED).   - &#x60;extra&#x60;: PASTEL data associated with the masternode. - &#x60;filter&#x60; (string, optional): Filter results. Partial match by outpoint by default in all modes, additional matches in some modes are also available. - &#x60;allnodes&#x60; (string, optional): Force to show all masternodes including expired NEW_START_REQUIRED.  ### Example Request - &#x60;GET /masternodelist?mode&#x3D;full&amp;filter&#x3D;192.168.0.1&#x60;  ### Response - Depending on the mode, returns a JSON object containing various information about masternodes.  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to status] |
| **filter** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to ] |
| **allnodes** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to ] |

### Return type

[**MasternodeListResponse**](../Models/MasternodeListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

