# MiningMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**generateBlocksGeneratePost**](MiningMethodsApi.md#generateBlocksGeneratePost) | **POST** /generate | Mine blocks immediately |
| [**getBlockSubsidyGetblocksubsidyGet**](MiningMethodsApi.md#getBlockSubsidyGetblocksubsidyGet) | **GET** /getblocksubsidy | Get block subsidy reward information |
| [**getBlockTemplateGetblocktemplatePost**](MiningMethodsApi.md#getBlockTemplateGetblocktemplatePost) | **POST** /getblocktemplate | Get data needed to construct a block to work on |
| [**getDifficultyGetdifficultyGet**](MiningMethodsApi.md#getDifficultyGetdifficultyGet) | **GET** /getdifficulty | Get the current proof-of-work difficulty |
| [**getGenerateGetgenerateGet**](MiningMethodsApi.md#getGenerateGetgenerateGet) | **GET** /getgenerate | Check if the server is set to generate coins |
| [**getLocalSolpsGetlocalsolpsGet**](MiningMethodsApi.md#getLocalSolpsGetlocalsolpsGet) | **GET** /getlocalsolps | Get average local solutions per second |
| [**getMiningInfoGetmininginfoGet**](MiningMethodsApi.md#getMiningInfoGetmininginfoGet) | **GET** /getmininginfo | Get mining-related information |
| [**getNetworkSolpsGetnetworksolpsGet**](MiningMethodsApi.md#getNetworkSolpsGetnetworksolpsGet) | **GET** /getnetworksolps | Get estimated network solutions per second |
| [**prioritiseTransactionPrioritisetransactionPost**](MiningMethodsApi.md#prioritiseTransactionPrioritisetransactionPost) | **POST** /prioritisetransaction | Prioritise a transaction for mining |
| [**refreshMiningMnidInfoRefreshminingmnidinfoGet**](MiningMethodsApi.md#refreshMiningMnidInfoRefreshminingmnidinfoGet) | **GET** /refreshminingmnidinfo | Refresh mining MNID information |
| [**setGenerateSetgeneratePost**](MiningMethodsApi.md#setGenerateSetgeneratePost) | **POST** /setgenerate | Set generation on or off |


<a name="generateBlocksGeneratePost"></a>
# **generateBlocksGeneratePost**
> GenerateBlocksResponse generateBlocksGeneratePost(GenerateBlocksRequest)

Mine blocks immediately

    Mine a specified number of blocks immediately on the regtest network.  ### Description - This endpoint mines a given number of blocks instantly and returns their hashes. Only available on the regtest network.  ### Input Parameters - &#x60;num_blocks&#x60;: The number of blocks to generate immediately. - &#x60;pastel_id&#x60;: (Optional) The Pastel ID eligible to mine the block.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;num_blocks\&quot;: 11,     \&quot;pastel_id\&quot;: \&quot;pastelid_example\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns an array of hashes of the blocks generated.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_hashes\&quot;: [         \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Forbidden if the method is used outside the regtest network.  ### Note - This method is primarily used for testing and development purposes on the regtest network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GenerateBlocksRequest** | [**GenerateBlocksRequest**](../Models/GenerateBlocksRequest.md)|  | |

### Return type

[**GenerateBlocksResponse**](../Models/GenerateBlocksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getBlockSubsidyGetblocksubsidyGet"></a>
# **getBlockSubsidyGetblocksubsidyGet**
> GetBlockSubsidyResponse getBlockSubsidyGetblocksubsidyGet(height)

Get block subsidy reward information

    Get the block subsidy reward for a given block height, considering the mining slow start.  ### Description - This endpoint returns the block subsidy reward, which includes the mining reward, masternode reward, and governance reward for the specified block height. - If the height is not provided, the subsidy for the current height of the chain is returned.  ### Input Parameters - &#x60;height&#x60;: (Optional, numeric) The block height. Defaults to the current height if not provided.  ### Example Request - &#x60;GET /getblocksubsidy?height&#x3D;1000&#x60;  ### Response - Returns a JSON object containing the subsidy rewards in each category.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;miner\&quot;: 12.345,     \&quot;masternode\&quot;: 3.210,     \&quot;governance\&quot;: 1.050 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block height is out of range or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding the distribution of rewards in the blockchain at a given height.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **height** | **Integer**|  | [optional] [default to null] |

### Return type

[**GetBlockSubsidyResponse**](../Models/GetBlockSubsidyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockTemplateGetblocktemplatePost"></a>
# **getBlockTemplateGetblocktemplatePost**
> GetBlockTemplateResponse getBlockTemplateGetblocktemplatePost(GetBlockTemplateRequest)

Get data needed to construct a block to work on

    Get data needed to construct a block to work on.  ### Description - This endpoint returns data necessary for constructing a block. It&#39;s primarily used by miners. - The method supports a &#39;template&#39; mode for requesting block template data and a &#39;proposal&#39; mode for submitting a block proposal.  ### Input Parameters - &#x60;jsonrequestobject&#x60; (string, optional): A JSON object specifying request details.  ### Example Request - &#x60;POST /getblocktemplate {\&quot;jsonrequestobject\&quot;: \&quot;{\&quot;mode\&quot;:\&quot;template\&quot;}\&quot;}&#x60;  ### Response - Returns a JSON object with details required to construct a block, including transactions to include, block version, target, and more.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;capabilities\&quot;: [\&quot;proposal\&quot;],     \&quot;version\&quot;: 4,     \&quot;previousblockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Detailed specification can be found at https://en.bitcoin.it/wiki/BIP_0022.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetBlockTemplateRequest** | [**GetBlockTemplateRequest**](../Models/GetBlockTemplateRequest.md)|  | |

### Return type

[**GetBlockTemplateResponse**](../Models/GetBlockTemplateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getDifficultyGetdifficultyGet"></a>
# **getDifficultyGetdifficultyGet**
> GetDifficultyResponse getDifficultyGetdifficultyGet()

Get the current proof-of-work difficulty

    Get the current proof-of-work difficulty as a multiple of the minimum difficulty.  ### Description - This endpoint returns the current network difficulty for proof-of-work. It&#39;s a measure of how difficult it is to find a new block compared to the easiest it can ever be.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getdifficulty&#x60;  ### Response - Returns a JSON object containing the current proof-of-work difficulty as a numeric value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;difficulty\&quot;: 874.625 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is particularly useful for miners and analysts interested in the network&#39;s mining difficulty.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDifficultyResponse**](../Models/GetDifficultyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getGenerateGetgenerateGet"></a>
# **getGenerateGetgenerateGet**
> GetGenerateResponse getGenerateGetgenerateGet()

Check if the server is set to generate coins

    Check if the server is currently set to generate coins.  ### Description - This endpoint checks the server&#39;s coin generation status, which indicates whether the server is set to mine new coins.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getgenerate&#x60;  ### Response - Returns a JSON object indicating whether the server is set to generate coins.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;is_generating\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The coin generation status is controlled by the &#x60;-gen&#x60; command line argument or the &#x60;gen&#x60; setting in &#x60;pastel.conf&#x60;. It can also be modified using the &#x60;setgenerate&#x60; call.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetGenerateResponse**](../Models/GetGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getLocalSolpsGetlocalsolpsGet"></a>
# **getLocalSolpsGetlocalsolpsGet**
> GetLocalSolpsResponse getLocalSolpsGetlocalsolpsGet()

Get average local solutions per second

    Get the average local solutions per second since this node was started.   ### Description - This endpoint returns the average number of solutions per second that the local node has been generating since it was started. This metric is an indicator of the mining or hashing power of the local node.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getlocalsolps&#x60;  ### Response - Returns a JSON object containing the average solutions per second.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;sols_per_second\&quot;: 123.456 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is typically shown on the metrics screen of the node, if enabled.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLocalSolpsResponse**](../Models/GetLocalSolpsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMiningInfoGetmininginfoGet"></a>
# **getMiningInfoGetmininginfoGet**
> GetMiningInfoResponse getMiningInfoGetmininginfoGet()

Get mining-related information

    Retrieve mining-related information from the blockchain.  ### Description - Returns a JSON object containing various details about the state of mining on the Pastel blockchain, such as the current block, block size, transactions, difficulty, and network solution rate.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmininginfo&#x60;  ### Response - Returns a JSON object containing detailed mining information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;blocks\&quot;: 100,     \&quot;currentblocksize\&quot;: 1000,     \&quot;currentblocktx\&quot;: 10,     \&quot;difficulty\&quot;: 1.23456789,     \&quot;errors\&quot;: \&quot;None\&quot;,     \&quot;generate\&quot;: false,     \&quot;genproclimit\&quot;: -1,     \&quot;localsolps\&quot;: 2.345678,     \&quot;networksolps\&quot;: 1234567,     \&quot;pooledtx\&quot;: 5,     \&quot;testnet\&quot;: false,     \&quot;chain\&quot;: \&quot;main\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for miners and network analysts to understand the current mining environment and network health.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMiningInfoResponse**](../Models/GetMiningInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetworkSolpsGetnetworksolpsGet"></a>
# **getNetworkSolpsGetnetworksolpsGet**
> GetNetworkSolpsResponse getNetworkSolpsGetnetworksolpsGet(GetNetworkSolpsRequest)

Get estimated network solutions per second

    Get the estimated network solutions per second based on the last n blocks.  ### Description - This endpoint estimates the network&#39;s solutions per second based on the last specified number of blocks.  - You can override the number of blocks to consider, or use -1 to specify the blocks over the difficulty averaging window. - You can also provide a block height to estimate the network speed at the time when that specific block was found.  ### Input Parameters - &#x60;blocks&#x60; (int, optional, default&#x3D;120): The number of blocks to consider, or -1 for blocks over the difficulty averaging window. - &#x60;height&#x60; (int, optional, default&#x3D;-1): The block height for estimating the network speed.  ### Example Request - &#x60;GET /getnetworksolps?blocks&#x3D;100&amp;height&#x3D;5000&#x60;  ### Response - Returns a JSON object containing the estimated solutions per second.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;solutions_per_second\&quot;: 1234567.89 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetNetworkSolpsRequest** | [**GetNetworkSolpsRequest**](../Models/GetNetworkSolpsRequest.md)|  | |

### Return type

[**GetNetworkSolpsResponse**](../Models/GetNetworkSolpsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="prioritiseTransactionPrioritisetransactionPost"></a>
# **prioritiseTransactionPrioritisetransactionPost**
> PrioritiseTransactionResponse prioritiseTransactionPrioritisetransactionPost(PrioritiseTransactionRequest)

Prioritise a transaction for mining

    Accepts the transaction into mined blocks at a higher (or lower) priority.  ### Description - This endpoint allows modifying the priority of a transaction in the mining queue. - It is useful for influencing the selection algorithm for transaction inclusion in upcoming blocks.  ### Input Parameters - &#x60;txid&#x60; (str): The transaction ID to be prioritised. - &#x60;priority_delta&#x60; (float): The priority to add or subtract. This alters how the transaction selection algorithm views the transaction&#39;s priority. - &#x60;fee_delta&#x60; (int): The fee value in patoshis to add (or subtract, if negative). It&#39;s a virtual change, affecting only the selection algorithm, not the actual transaction fee.  ### Example Request &#x60;&#x60;&#x60;json POST /prioritisetransaction Content-Type: application/json  {     \&quot;txid\&quot;: \&quot;123abc\&quot;,     \&quot;priority_delta\&quot;: 0.0,     \&quot;fee_delta\&quot;: 10000 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the operation was successful.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is particularly relevant for miners and services that require transaction prioritisation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PrioritiseTransactionRequest** | [**PrioritiseTransactionRequest**](../Models/PrioritiseTransactionRequest.md)|  | |

### Return type

[**PrioritiseTransactionResponse**](../Models/PrioritiseTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="refreshMiningMnidInfoRefreshminingmnidinfoGet"></a>
# **refreshMiningMnidInfoRefreshminingmnidinfoGet**
> RefreshMiningMnidInfoResponse refreshMiningMnidInfoRefreshminingmnidinfoGet()

Refresh mining MNID information

    Refreshes the mining information (MNIDs) from the pastel.conf file.  ### Description - This endpoint refreshes the list of Masternode IDs (MNIDs) used for mining, as specified in the pastel.conf file. It is useful for updating the mining configuration without restarting the node.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /refreshminingmnidinfo&#x60;  ### Response - Returns a JSON array containing the list of refreshed MNIDs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;mnids\&quot;: [\&quot;mnid1\&quot;, \&quot;mnid2\&quot;, \&quot;mnid3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in refreshing the MNID information.  ### Note - This endpoint is particularly useful for miners who need to update their Masternode IDs dynamically.

### Parameters
This endpoint does not need any parameter.

### Return type

[**RefreshMiningMnidInfoResponse**](../Models/RefreshMiningMnidInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="setGenerateSetgeneratePost"></a>
# **setGenerateSetgeneratePost**
> SetGenerateResponse setGenerateSetgeneratePost(SetGenerateRequest)

Set generation on or off

    Set &#39;generate&#39; true or false to turn generation on or off.               Generation is limited to &#39;genproclimit&#39; processors, -1 is unlimited.               See the getgenerate call for the current setting.               ### Description              - This endpoint allows turning on or off the generation (mining) process in the Pastel network.               - It controls the number of processors to be used for generation.               ### Input Parameters              - &#x60;generate&#x60; (boolean, required): Set to true to turn on generation, off to turn off.              - &#x60;genproclimit&#x60; (numeric, optional): Set the processor limit for when generation is on. Can be -1 for unlimited.               ### Example Request              &#x60;&#x60;&#x60;json              {                  \&quot;generate\&quot;: true,                  \&quot;genproclimit\&quot;: 1              }              &#x60;&#x60;&#x60;               ### Response              - Returns a message indicating successful change of generation setting.               ### Example Response              &#x60;&#x60;&#x60;json              {                  \&quot;message\&quot;: \&quot;Generation setting updated successfully\&quot;              }              &#x60;&#x60;&#x60;               ### Possible Errors              - HTTP 400: Bad Request if the parameters are invalid.              - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetGenerateRequest** | [**SetGenerateRequest**](../Models/SetGenerateRequest.md)|  | |

### Return type

[**SetGenerateResponse**](../Models/SetGenerateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

