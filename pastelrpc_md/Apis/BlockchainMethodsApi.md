# BlockchainMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimateFeeEstimatefeeGet**](BlockchainMethodsApi.md#estimateFeeEstimatefeeGet) | **GET** /estimatefee | Estimate the transaction fee per kilobyte |
| [**fixMissingTransactionsFixmissingtxsStartingHeightGet**](BlockchainMethodsApi.md#fixMissingTransactionsFixmissingtxsStartingHeightGet) | **GET** /fixmissingtxs/{starting_height} | Fix Missing Transactions |
| [**getAccountGetaccountZcashaddressGet**](BlockchainMethodsApi.md#getAccountGetaccountZcashaddressGet) | **GET** /getaccount/{zcashaddress} | Get the account associated with a Pastel address |
| [**getBalanceGetbalanceGet**](BlockchainMethodsApi.md#getBalanceGetbalanceGet) | **GET** /getbalance | Get the server&#39;s total available balance |
| [**getBestBlockHashGetbestblockhashGet**](BlockchainMethodsApi.md#getBestBlockHashGetbestblockhashGet) | **GET** /getbestblockhash | Get the hash of the best block |
| [**getBlockCountGetblockcountGet**](BlockchainMethodsApi.md#getBlockCountGetblockcountGet) | **GET** /getblockcount | Get the current block count |
| [**getBlockDeltasGetblockdeltasBlockHashGet**](BlockchainMethodsApi.md#getBlockDeltasGetblockdeltasBlockHashGet) | **GET** /getblockdeltas/{block_hash} | Get block deltas |
| [**getBlockGetblockGet**](BlockchainMethodsApi.md#getBlockGetblockGet) | **GET** /getblock | Get block data |
| [**getBlockHashGetblockhashGet**](BlockchainMethodsApi.md#getBlockHashGetblockhashGet) | **GET** /getblockhash | Get the hash of a block at a specific index |
| [**getBlockHeaderGetblockheaderBlockHashGet**](BlockchainMethodsApi.md#getBlockHeaderGetblockheaderBlockHashGet) | **GET** /getblockheader/{block_hash} | Get information about a block header |
| [**getBlockchainInfoGetblockchaininfoGet**](BlockchainMethodsApi.md#getBlockchainInfoGetblockchaininfoGet) | **GET** /getblockchaininfo | Get blockchain information |
| [**getChainTipsGetchaintipsGet**](BlockchainMethodsApi.md#getChainTipsGetchaintipsGet) | **GET** /getchaintips | Get information about all known chain tips |
| [**getNextBlockSubsidyGetnextblocksubsidyGet**](BlockchainMethodsApi.md#getNextBlockSubsidyGetnextblocksubsidyGet) | **GET** /getnextblocksubsidy | Get subsidy rewards for the next block |
| [**getRawMempoolGetrawmempoolGet**](BlockchainMethodsApi.md#getRawMempoolGetrawmempoolGet) | **GET** /getrawmempool | Get all transaction IDs in memory pool |
| [**getReceivedByAddressGetreceivedbyaddressGet**](BlockchainMethodsApi.md#getReceivedByAddressGetreceivedbyaddressGet) | **GET** /getreceivedbyaddress | Get the total amount received by a Pastel address |
| [**getTransactionGettransactionTxidGet**](BlockchainMethodsApi.md#getTransactionGettransactionTxidGet) | **GET** /gettransaction/{txid} | Get detailed information about a transaction |
| [**getTxOutGettxoutGet**](BlockchainMethodsApi.md#getTxOutGettxoutGet) | **GET** /gettxout | Get details about an unspent transaction output |
| [**getTxOutSetInfoGettxoutsetinfoGet**](BlockchainMethodsApi.md#getTxOutSetInfoGettxoutsetinfoGet) | **GET** /gettxoutsetinfo | Get statistics about the unspent transaction output set |
| [**getTxfeeGettxfeeTxidGet**](BlockchainMethodsApi.md#getTxfeeGettxfeeTxidGet) | **GET** /gettxfee/{txid} | Get transaction fee by txid |
| [**invalidateBlockInvalidateblockPost**](BlockchainMethodsApi.md#invalidateBlockInvalidateblockPost) | **POST** /invalidateblock | Mark a block as permanently invalid |
| [**listAddressGroupingsListaddressgroupingsGet**](BlockchainMethodsApi.md#listAddressGroupingsListaddressgroupingsGet) | **GET** /listaddressgroupings | List groups of addresses with common ownership |
| [**listLockUnspentListlockunspentGet**](BlockchainMethodsApi.md#listLockUnspentListlockunspentGet) | **GET** /listlockunspent | List Temporarily Unspendable Outputs |
| [**listShieldedAddressesZListaddressesGet**](BlockchainMethodsApi.md#listShieldedAddressesZListaddressesGet) | **GET** /z_listaddresses | List Shielded Addresses |
| [**listSinceBlockListsinceblockPost**](BlockchainMethodsApi.md#listSinceBlockListsinceblockPost) | **POST** /listsinceblock | List transactions since a specific block |
| [**listUnspentListunspentGet**](BlockchainMethodsApi.md#listUnspentListunspentGet) | **GET** /listunspent | List Unspent Transaction Outputs |
| [**reconsiderBlockReconsiderblockPost**](BlockchainMethodsApi.md#reconsiderBlockReconsiderblockPost) | **POST** /reconsiderblock | Reconsider a previously invalidated block |
| [**submitBlockSubmitblockPost**](BlockchainMethodsApi.md#submitBlockSubmitblockPost) | **POST** /submitblock | Submit a new block to the network |
| [**verifyChainVerifychainGet**](BlockchainMethodsApi.md#verifyChainVerifychainGet) | **GET** /verifychain | Verify the blockchain database |
| [**zGetBalanceZGetbalanceAddressGet**](BlockchainMethodsApi.md#zGetBalanceZGetbalanceAddressGet) | **GET** /z_getbalance/{address} | Get the balance of an address |
| [**zGetoperationresultZGetoperationresultGet**](BlockchainMethodsApi.md#zGetoperationresultZGetoperationresultGet) | **GET** /z_getoperationresult | Retrieve the result and status of Zcash operations |
| [**zListOperationIdsZListoperationidsGet**](BlockchainMethodsApi.md#zListOperationIdsZListoperationidsGet) | **GET** /z_listoperationids | List Operation IDs |
| [**zListunspentZListunspentGet**](BlockchainMethodsApi.md#zListunspentZListunspentGet) | **GET** /z_listunspent | List unspent shielded notes |
| [**zShieldcoinbaseZShieldcoinbasePost**](BlockchainMethodsApi.md#zShieldcoinbaseZShieldcoinbasePost) | **POST** /z_shieldcoinbase | Shield transparent coinbase funds to a shielded zaddr |
| [**zViewTransactionZViewtransactionTxidGet**](BlockchainMethodsApi.md#zViewTransactionZViewtransactionTxidGet) | **GET** /z_viewtransaction/{txid} | Get detailed shielded information about in-wallet transaction |


<a name="estimateFeeEstimatefeeGet"></a>
# **estimateFeeEstimatefeeGet**
> EstimateFeeResponse estimateFeeEstimatefeeGet(nblocks)

Estimate the transaction fee per kilobyte

    Estimate the approximate fee per kilobyte needed for a transaction to begin confirmation within a specified number of blocks.   ### Description - This endpoint provides an estimate of the fee per kilobyte for a transaction to be confirmed within a specified number of blocks.  ### Input Parameters - &#x60;nblocks&#x60;: The number of blocks within which the transaction should begin confirmation.  ### Example Request - &#x60;GET /estimatefee?nblocks&#x3D;6&#x60;  ### Response - Returns a JSON object containing the estimated fee per kilobyte.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;estimated_fee_per_kb\&quot;: 0.0001 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - A return value of -1.0 indicates insufficient data to make an estimate.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **nblocks** | **Integer**|  | [default to null] |

### Return type

[**EstimateFeeResponse**](../Models/EstimateFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="fixMissingTransactionsFixmissingtxsStartingHeightGet"></a>
# **fixMissingTransactionsFixmissingtxsStartingHeightGet**
> FixMissingTransactionsResponse fixMissingTransactionsFixmissingtxsStartingHeightGet(starting\_height)

Fix Missing Transactions

    Scan for missing transactions in the wallet starting from the given height and add to the wallet all missing transactions found in the blockchain.  ### Description - Scans the blockchain starting from the specified block height for any transactions that are missing in the wallet and adds them.  ### Input Parameters - &#x60;starting_height&#x60;: (integer, required) The block height from which the scan for missing transactions should begin.  ### Example Request - &#x60;GET /fixmissingtxs/100000&#x60;  ### Response - Returns a JSON array of transaction IDs for transactions that were missing in the wallet and have been added.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;missing_transactions\&quot;: [\&quot;missing_transaction1_txid\&quot;, \&quot;missing_transaction2_txid\&quot;, ...] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the starting height is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for wallet recovery and synchronization purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **starting\_height** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**FixMissingTransactionsResponse**](../Models/FixMissingTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAccountGetaccountZcashaddressGet"></a>
# **getAccountGetaccountZcashaddressGet**
> GetAccountResponse getAccountGetaccountZcashaddressGet(zcashaddress)

Get the account associated with a Pastel address

    Retrieve the account name associated with the given Pastel address.   ### Description - This endpoint is used to get the account name linked to a specific Pastel address. It is important to note that this method is marked as deprecated.  ### Input Parameters - &#x60;zcashaddress&#x60;: A string representing the Pastel address for the account lookup.  ### Example Request - &#x60;GET /getaccount/PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n&#x60;  ### Response - Returns a JSON object containing the account name associated with the given Pastel address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;account_name\&quot;: \&quot;exampleAccountName\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is deprecated and might be removed in future versions of the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetAccountResponse**](../Models/GetAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBalanceGetbalanceGet"></a>
# **getBalanceGetbalanceGet**
> GetBalanceResponse getBalanceGetbalanceGet(account, minconf, includeWatchonly)

Get the server&#39;s total available balance

    Get the server&#39;s total available balance.  ### Description - This endpoint returns the total available balance in the server&#39;s wallet. It can be filtered by a minimum number of confirmations and can include balances in watch-only addresses.  ### Input Parameters - &#x60;account&#x60;: (Optional) DEPRECATED. Must be an empty string \&quot;\&quot; or \&quot;*\&quot;, either of which will give the total available balance. Any other string will result in an error. - &#x60;minconf&#x60;: (Optional) Only include transactions confirmed at least this many times. Default is 1. - &#x60;includeWatchonly&#x60;: (Optional) Also include balance in watchonly addresses. Default is false.  ### Example Request - &#x60;GET /getbalance?account&#x3D;*&amp;minconf&#x3D;1&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON object containing the available balance amount.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balance\&quot;: 1000.00 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The account argument is deprecated and should be set to \&quot;\&quot; or \&quot;*\&quot;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**Account_1**](../Models/.md)|  | [optional] [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **includeWatchonly** | [**Includewatchonly**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**GetBalanceResponse**](../Models/GetBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBestBlockHashGetbestblockhashGet"></a>
# **getBestBlockHashGetbestblockhashGet**
> GetBestBlockHashResponse getBestBlockHashGetbestblockhashGet()

Get the hash of the best block

    Get the hash of the best (tip) block in the longest blockchain.   ### Description - This endpoint returns the hash of the latest block added to the Pastel blockchain, representing the most current and up-to-date state of the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getbestblockhash&#x60;  ### Response - Returns a JSON object containing the hash of the best block in hexadecimal format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Primarily used by blockchain explorers and wallets to identify the current end of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBestBlockHashResponse**](../Models/GetBestBlockHashResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockCountGetblockcountGet"></a>
# **getBlockCountGetblockcountGet**
> GetBlockCountResponse getBlockCountGetblockcountGet()

Get the current block count

    Get the number of blocks in the best valid block chain.  ### Description - This endpoint returns the current block count in the blockchain, which is the number of blocks in the longest valid blockchain. - It reflects the height of the blockchain and is useful for tracking the growth of the blockchain over time.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getblockcount&#x60;  ### Response - Returns a JSON object containing the current block count as a numeric value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;block_count\&quot;: 650000 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This is a commonly used method for blockchain explorers, wallets, and other tools that need to know the current height of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBlockCountResponse**](../Models/GetBlockCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockDeltasGetblockdeltasBlockHashGet"></a>
# **getBlockDeltasGetblockdeltasBlockHashGet**
> GetBlockDeltasResponse getBlockDeltasGetblockdeltasBlockHashGet(block\_hash)

Get block deltas

    Retrieve detailed information about inputs and outputs of all transactions in a block.  ### Description - This endpoint returns detailed information about each transaction in the specified block, including inputs and outputs.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block for which information is requested.  ### Example Request - &#x60;GET /getblockdeltas/00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b&#x60;  ### Response - Returns a JSON object containing detailed information about the block and its transactions.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00227e566682aebd6a7a5b772c96d7a999cadaebeaf1ce96f4191a3aad58b00b\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;size\&quot;: 190,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 404: Not Found if the specified block hash does not exist.  ### Note - This endpoint requires the &#39;insightexplorer&#39; mode to be enabled on the Pastel node.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetBlockDeltasResponse**](../Models/GetBlockDeltasResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockGetblockGet"></a>
# **getBlockGetblockGet**
> GetBlockResponse getBlockGetblockGet(block\_identifier, verbosity)

Get block data

    Get data of a specific block in the Pastel blockchain.   ### Description - Depending on the verbosity level, this endpoint returns different details about the specified block.  ### Input Parameters - &#x60;block_identifier&#x60;: The block hash or height. - &#x60;verbosity&#x60;: (Optional) Verbosity level (0, 1, or 2). Defaults to 1.  ### Example Request - &#x60;GET /getblock?block_identifier&#x3D;\&quot;00000000febc373a...\&quot;&amp;verbosity&#x3D;1&#x60;  ### Response - Depending on the verbosity, the response structure varies. Refer to the Pydantic models for details.  ### Example Response (verbosity &#x3D; 1) &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00000000febc373a...\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;size\&quot;: 800,     \&quot;height\&quot;: 12800,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Invalid parameters. - HTTP 404: Block not found. - HTTP 500: Internal Server Error.  ### Note - Used for detailed blockchain exploration and data analysis.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_identifier** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **verbosity** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**GetBlockResponse**](../Models/GetBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockHashGetblockhashGet"></a>
# **getBlockHashGetblockhashGet**
> GetBlockHashResponse getBlockHashGetblockhashGet(GetBlockHashRequest)

Get the hash of a block at a specific index

    Get the hash of a block in the best-block-chain at the provided index.  ### Description - This endpoint returns the hash of the block at a given index in the blockchain. The index refers to the height of the block in the blockchain.  ### Input Parameters - &#x60;index&#x60; (int, required): The block index (height) in the blockchain.  ### Example Request - &#x60;GET /getblockhash?index&#x3D;1000&#x60;  ### Response - Returns a JSON object containing the hash of the block at the specified index.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the index parameter is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s important to ensure the block index is within the valid range of the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetBlockHashRequest** | [**GetBlockHashRequest**](../Models/GetBlockHashRequest.md)|  | |

### Return type

[**GetBlockHashResponse**](../Models/GetBlockHashResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getBlockHeaderGetblockheaderBlockHashGet"></a>
# **getBlockHeaderGetblockheaderBlockHashGet**
> oas_any_type_not_mapped getBlockHeaderGetblockheaderBlockHashGet(block\_hash, verbose)

Get information about a block header

    Retrieve information about a block header by its hash.  ### Description - Returns either detailed information about the block header or its serialized, hex-encoded data, based on the &#39;verbose&#39; flag.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block. - &#x60;verbose&#x60;: Boolean flag to determine the response format. Defaults to true.  ### Example Request - &#x60;GET /getblockheader/00000000c937983704a73af28acdec37b049d214adbda81d7e2a3dd146f6ed09?verbose&#x3D;true&#x60;  ### Response - If verbose is true, returns a JSON object with detailed block header information. - If verbose is false, returns a JSON object with serialized, hex-encoded block header data.  ### Example Response - If verbose is true: &#x60;&#x60;&#x60;json {   \&quot;hash\&quot;: \&quot;hash\&quot;,   \&quot;confirmations\&quot;: 5,   \&quot;height\&quot;: 123456,   ... } &#x60;&#x60;&#x60; - If verbose is false: &#x60;&#x60;&#x60;json {   \&quot;data\&quot;: \&quot;hex-encoded data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 404: Block not found. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | **String**|  | [default to null] |
| **verbose** | **Boolean**|  | [optional] [default to true] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBlockchainInfoGetblockchaininfoGet"></a>
# **getBlockchainInfoGetblockchaininfoGet**
> BlockchainInfoResponse getBlockchainInfoGetblockchaininfoGet()

Get blockchain information

    Get detailed information about the state of the blockchain.   ### Description - This endpoint returns various state info regarding blockchain processing.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getblockchaininfo&#x60;  ### Response - Returns a JSON object containing detailed information about the blockchain.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;chain\&quot;: \&quot;main\&quot;,     \&quot;blocks\&quot;: 680000,     \&quot;headers\&quot;: 680000,     \&quot;bestblockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;difficulty\&quot;: 19298087186262.61,     \&quot;verificationprogress\&quot;: 0.999998,     \&quot;chainwork\&quot;: \&quot;0000000000000000000000000000000000000000014d1e4fe926a7b5e76e7c6e\&quot;,     \&quot;commitments\&quot;: 289431,     \&quot;softforks\&quot;: [         {             \&quot;id\&quot;: \&quot;bip34\&quot;,             \&quot;version\&quot;: 2,             \&quot;enforce\&quot;: {\&quot;status\&quot;: true, \&quot;found\&quot;: 1000, \&quot;required\&quot;: 750, \&quot;window\&quot;: 1000},             \&quot;reject\&quot;: {\&quot;status\&quot;: true, \&quot;found\&quot;: 1000, \&quot;required\&quot;: 950, \&quot;window\&quot;: 1000}         }         // Include other softforks as needed     ],     \&quot;upgrades\&quot;: {         \&quot;upgrade1\&quot;: {             \&quot;name\&quot;: \&quot;example_upgrade\&quot;,             \&quot;activationheight\&quot;: 123456,             \&quot;status\&quot;: \&quot;active\&quot;,             \&quot;info\&quot;: \&quot;Additional information\&quot;         }         // Include other upgrades as needed     },     \&quot;consensus\&quot;: {         \&quot;chaintip\&quot;: \&quot;abcd1234\&quot;,         \&quot;nextblock\&quot;: \&quot;efgh5678\&quot;     },     \&quot;pruned\&quot;: false,     \&quot;pruneheight\&quot;: 12345 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for obtaining a variety of data about the blockchain&#39;s current state and history.

### Parameters
This endpoint does not need any parameter.

### Return type

[**BlockchainInfoResponse**](../Models/BlockchainInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getChainTipsGetchaintipsGet"></a>
# **getChainTipsGetchaintipsGet**
> GetChainTipsResponse getChainTipsGetchaintipsGet()

Get information about all known chain tips

    Return information about all known tips in the block tree, including the main chain as well as orphaned branches.  ### Description - This endpoint provides details about all known chain tips in the block tree. This includes information about the main chain and any orphaned or detached branches. - The response includes the height, hash, branch length, and status for each chain tip.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getchaintips&#x60;  ### Response - Returns a JSON array of objects, each representing a chain tip with its associated details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tips\&quot;: [         {             \&quot;height\&quot;: 123456,             \&quot;hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,             \&quot;branchlen\&quot;: 0,             \&quot;status\&quot;: \&quot;active\&quot;         },         {             \&quot;height\&quot;: 123455,             \&quot;hash\&quot;: \&quot;00000000000000000007abc8d2b16cd689bd44e2f7f8f36b7e4f938b8b9c6f4f\&quot;,             \&quot;branchlen\&quot;: 1,             \&quot;status\&quot;: \&quot;valid-fork\&quot;         }     ] } &#x60;&#x60;&#x60;  ### Possible Status Values 1. &#x60;invalid&#x60;: Contains at least one invalid block. 2. &#x60;headers-only&#x60;: Not all blocks are available, but the headers are valid. 3. &#x60;valid-headers&#x60;: All blocks are available but were never fully validated. 4. &#x60;valid-fork&#x60;: Fully validated but not part of the active chain. 5. &#x60;active&#x60;: Part of the active main chain.  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding the structure and different branches of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetChainTipsResponse**](../Models/GetChainTipsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNextBlockSubsidyGetnextblocksubsidyGet"></a>
# **getNextBlockSubsidyGetnextblocksubsidyGet**
> GetNextBlockSubsidyResponse getNextBlockSubsidyGetnextblocksubsidyGet()

Get subsidy rewards for the next block

    Get the block subsidy rewards of the next block in the Pastel blockchain.  ### Description - This endpoint returns the subsidy rewards for the next block, including the amounts for the miner, masternode, and governance.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnextblocksubsidy&#x60;  ### Response - Returns a JSON object containing the subsidy rewards for the next block.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;miner\&quot;: 12.5,     \&quot;masternode\&quot;: 6.25,     \&quot;governance\&quot;: 1.25 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint provides crucial information for understanding the reward distribution in the upcoming block.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNextBlockSubsidyResponse**](../Models/GetNextBlockSubsidyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRawMempoolGetrawmempoolGet"></a>
# **getRawMempoolGetrawmempoolGet**
> oas_any_type_not_mapped getRawMempoolGetrawmempoolGet(verbose)

Get all transaction IDs in memory pool

    Get the transaction IDs in the memory pool.   ### Description - Returns all transaction IDs in the memory pool as an array of strings or a detailed JSON object.  ### Input Parameters - &#x60;verbose&#x60;: (boolean, optional, default&#x3D;false) Set to true for a detailed JSON object, false for an array of transaction IDs.  ### Example Request - &#x60;GET /getrawmempool?verbose&#x3D;false&#x60;  ### Response - For &#x60;verbose&#x3D;false&#x60;, returns an array of transaction IDs. - For &#x60;verbose&#x3D;true&#x60;, returns a detailed JSON object with information about each transaction.  ### Example Response for &#x60;verbose&#x3D;false&#x60; &#x60;&#x60;&#x60;json {     \&quot;transaction_ids\&quot;: [\&quot;txid1\&quot;, \&quot;txid2\&quot;, \&quot;txid3\&quot;] } &#x60;&#x60;&#x60;  ### Example Response for &#x60;verbose&#x3D;true&#x60; &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: {         \&quot;txid1\&quot;: {             \&quot;size\&quot;: 250,             \&quot;fee\&quot;: 0.0001,             \&quot;time\&quot;: 1617184000,             \&quot;height\&quot;: 675000,             \&quot;startingpriority\&quot;: 1000000,             \&quot;currentpriority\&quot;: 1200000,             \&quot;depends\&quot;: [\&quot;txidA\&quot;, \&quot;txidB\&quot;]         },         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving detailed information about transactions in the mempool.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **verbose** | **Boolean**|  | [optional] [default to null] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getReceivedByAddressGetreceivedbyaddressGet"></a>
# **getReceivedByAddressGetreceivedbyaddressGet**
> GetReceivedByAddressResponse getReceivedByAddressGetreceivedbyaddressGet(zcashaddress, minconf)

Get the total amount received by a Pastel address

    Get the total amount received by the given Pastel address in transactions with at least a specified number of confirmations.  ### Description - This endpoint returns the total amount received by a specific Pastel address in transactions that are confirmed at least a specified number of times.  ### Input Parameters - &#x60;zcashaddress&#x60;: The Pastel address for transactions. - &#x60;minconf&#x60;: (Optional) The minimum number of confirmations for transactions. Defaults to 1.  ### Example Request - &#x60;GET /getreceivedbyaddress?zcashaddress&#x3D;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n&amp;minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing the total amount received at the given address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;total_amount\&quot;: 10.5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or not provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving the total amount received at a particular Pastel address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**GetReceivedByAddressResponse**](../Models/GetReceivedByAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTransactionGettransactionTxidGet"></a>
# **getTransactionGettransactionTxidGet**
> GetTransactionResponse getTransactionGettransactionTxidGet(txid, includeWatchonly)

Get detailed information about a transaction

    Retrieve detailed information about an in-wallet transaction by its ID.  ### Description - Fetches detailed data of a specified transaction from the wallet, including amounts, confirmations, and related addresses.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID to query. - &#x60;includeWatchonly&#x60;: (Optional) Include watch-only addresses in balance calculation and details.  ### Example Request - &#x60;GET /gettransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d&#x60;  ### Response - Returns detailed information about the specified transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;mined\&quot;,     \&quot;amount\&quot;: 10.0,     \&quot;amountPat\&quot;: 10000,     \&quot;confirmations\&quot;: 15,     \&quot;blockhash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;blockindex\&quot;: 1,     \&quot;blocktime\&quot;: 1625097600,     \&quot;txid\&quot;: \&quot;1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d\&quot;,     \&quot;time\&quot;: 1625097600,     \&quot;timereceived\&quot;: 1625097600,     \&quot;details\&quot;: [         {             \&quot;account\&quot;: \&quot;\&quot;,             \&quot;address\&quot;: \&quot;t1Xin4H451oBDwrKcQeY1VGgMWivLs2hhuR\&quot;,             \&quot;category\&quot;: \&quot;receive\&quot;,             \&quot;amount\&quot;: 10.0,             \&quot;amountPat\&quot;: 10000,             \&quot;vout\&quot;: 0         }     ],     \&quot;hex\&quot;: \&quot;010000000...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the transaction ID is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to obtain transaction details for wallet transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**GetTransactionResponse**](../Models/GetTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxOutGettxoutGet"></a>
# **getTxOutGettxoutGet**
> GetTxOutResponse getTxOutGettxoutGet(txid, n, includemempool)

Get details about an unspent transaction output

    Get details about an unspent transaction output.   ### Description - This endpoint returns detailed information about an unspent transaction output (UTXO) from the Pastel blockchain.  ### Input Parameters - &#x60;txid&#x60;: (string, required) The transaction id. - &#x60;n&#x60;: (int, required) The output number (vout) of the transaction. - &#x60;includemempool&#x60;: (bool, optional) Whether to include the mempool. Defaults to True.  ### Example Request - &#x60;GET /gettxout?txid&#x3D;&lt;txid&gt;&amp;n&#x3D;1&amp;includemempool&#x3D;true&#x60;  ### Response - Returns a JSON object containing details of the specified unspent transaction output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;bestblock\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;confirmations\&quot;: 10,     \&quot;value\&quot;: 12.34,     \&quot;valuePat\&quot;: 1234000000,     \&quot;scriptPubKey\&quot;: {         \&quot;asm\&quot;: \&quot;code\&quot;,         \&quot;hex\&quot;: \&quot;hex\&quot;,         \&quot;reqSigs\&quot;: 1,         \&quot;type\&quot;: \&quot;pubkeyhash\&quot;,         \&quot;addresses\&quot;: [\&quot;address1\&quot;, \&quot;address2\&quot;]     },     \&quot;version\&quot;: 2,     \&quot;coinbase\&quot;: false } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 404: Not Found if the specified transaction output is not found or is already spent. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for verifying the existence and details of specific transaction outputs.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **n** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **includemempool** | [**Includemempool**](../Models/.md)|  | [optional] [default to true] |

### Return type

[**GetTxOutResponse**](../Models/GetTxOutResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxOutSetInfoGettxoutsetinfoGet"></a>
# **getTxOutSetInfoGettxoutsetinfoGet**
> GetTxOutSetInfoResponse getTxOutSetInfoGettxoutsetinfoGet()

Get statistics about the unspent transaction output set

    Returns statistics about the unspent transaction output set.  ### Description - This endpoint provides detailed information about the state of the unspent transaction output set. It&#39;s useful for getting a snapshot of the blockchain&#39;s UTXO set at the current moment. - Note: This call may take some time due to the calculations involved.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /gettxoutsetinfo&#x60;  ### Response - Returns a JSON object containing various statistics about the UTXO set.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;height\&quot;: 650000,     \&quot;bestblock\&quot;: \&quot;0000000000000000000c6da2c440...\&quot;,     \&quot;transactions\&quot;: 2500000,     \&quot;txouts\&quot;: 5000000,     \&quot;bytes_serialized\&quot;: 300000000,     \&quot;hash_serialized\&quot;: \&quot;3e9cc7000...\&quot;,     \&quot;total_amount\&quot;: 18446744.07370955 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is particularly useful for analysis and understanding the overall state of the blockchain.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTxOutSetInfoResponse**](../Models/GetTxOutSetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTxfeeGettxfeeTxidGet"></a>
# **getTxfeeGettxfeeTxidGet**
> GetTxfeeResponse getTxfeeGettxfeeTxidGet(txid)

Get transaction fee by txid

    Get the transaction fee for a specific transaction by its transaction ID (txid).  ### Description - This endpoint retrieves the transaction fee for a given transaction ID in the Pastel blockchain.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID for which the transaction fee is requested.  ### Example Request - &#x60;GET /gettxfee/e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4&#x60;  ### Response - Returns a JSON object containing details of the transaction fee.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4\&quot;,     \&quot;height\&quot;: 123456,     \&quot;blockHash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot;,     \&quot;txFeePat\&quot;: 50000,     \&quot;txFee\&quot;: 0.0005 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the txid is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallets and explorers to determine the fee associated with a particular transaction.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetTxfeeResponse**](../Models/GetTxfeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="invalidateBlockInvalidateblockPost"></a>
# **invalidateBlockInvalidateblockPost**
> InvalidateBlockResponse invalidateBlockInvalidateblockPost(block\_hash)

Mark a block as permanently invalid

    Mark a block as permanently invalid, as if it violated a consensus rule.  ### Description - This endpoint marks a specific block in the blockchain as invalid. This operation is irreversible and treats the block as though it has violated a consensus rule.  ### Input Parameters - &#x60;block_hash&#x60;: The hash of the block to mark as invalid.  ### Example Request &#x60;&#x60;&#x60;json POST /invalidateblock {     \&quot;block_hash\&quot;: \&quot;00000000000000000007abd8d2a16cd689ad44e2f7f8f36a7e4f938b8b9c6f3e\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Block marked as invalid\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block hash is not provided or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This is a critical operation and should be used with caution. Invalidating a block can have significant implications on the blockchain state.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **block\_hash** | **String**|  | [default to null] |

### Return type

[**InvalidateBlockResponse**](../Models/InvalidateBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listAddressGroupingsListaddressgroupingsGet"></a>
# **listAddressGroupingsListaddressgroupingsGet**
> AddressGroupingsResponse listAddressGroupingsListaddressgroupingsGet()

List groups of addresses with common ownership

    List groups of addresses which have had their common ownership made public by common use as inputs or as the resulting change in past transactions.  ### Description - This endpoint returns groups of addresses that are grouped together based on their common ownership, which is inferred from their usage in past transactions.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Response - Returns a JSON object containing groups of addresses. Each group is a list of addresses, where each address is represented by its Pastel address, the amount associated with it, and optionally the account name.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;groupings\&quot;: [         [             {\&quot;address\&quot;: \&quot;pasteladdress1\&quot;, \&quot;amount\&quot;: 10.5, \&quot;account\&quot;: \&quot;myaccount\&quot;},             {\&quot;address\&quot;: \&quot;pasteladdress2\&quot;, \&quot;amount\&quot;: 2.3}         ],         [             {\&quot;address\&quot;: \&quot;pasteladdress3\&quot;, \&quot;amount\&quot;: 5.0}         ]     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for understanding wallet organization and for tracking common ownership of addresses.

### Parameters
This endpoint does not need any parameter.

### Return type

[**AddressGroupingsResponse**](../Models/AddressGroupingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listLockUnspentListlockunspentGet"></a>
# **listLockUnspentListlockunspentGet**
> ListLockUnspentResponse listLockUnspentListlockunspentGet()

List Temporarily Unspendable Outputs

    List all temporarily unspendable outputs.  ### Description - This endpoint returns a list of outputs that are temporarily unspendable.  - Useful for viewing transactions that have been locked using the &#x60;lockunspent&#x60; call.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /listlockunspent&#x60;  ### Response - Returns a JSON array containing objects with &#39;txid&#39; and &#39;vout&#39; fields for each temporarily locked output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;lock_unspent_outputs\&quot;: [         {             \&quot;txid\&quot;: \&quot;a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\&quot;,             \&quot;vout\&quot;: 1         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The &#39;txid&#39; represents the transaction id of the locked output, and &#39;vout&#39; is its output index.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListLockUnspentResponse**](../Models/ListLockUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listShieldedAddressesZListaddressesGet"></a>
# **listShieldedAddressesZListaddressesGet**
> ListShieldedAddressesResponse listShieldedAddressesZListaddressesGet(include\_watchonly)

List Shielded Addresses

    List all Sapling shielded addresses belonging to the wallet.  ### Description - This endpoint returns a list of Sapling shielded addresses that are owned by the wallet.  - It can optionally include watch-only addresses.  ### Input Parameters - &#x60;include_watchonly&#x60;: (bool, optional, default&#x3D;false) Set to true to include watch-only addresses.  ### Example Request - &#x60;GET /z_listaddresses?include_watchonly&#x3D;true&#x60;  ### Response - Returns a JSON object containing an array of shielded addresses.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;addresses\&quot;: [\&quot;zs1...address1\&quot;, \&quot;zs1...address2\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for retrieving all shielded addresses associated with the user&#39;s wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **include\_watchonly** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**ListShieldedAddressesResponse**](../Models/ListShieldedAddressesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listSinceBlockListsinceblockPost"></a>
# **listSinceBlockListsinceblockPost**
> ListSinceBlockResponse listSinceBlockListsinceblockPost(ListSinceBlockRequest)

List transactions since a specific block

    List all transactions in blocks since a specified block, or all transactions if no block is specified.  ### Description - This endpoint retrieves all transactions that occurred after a specified block.  - It can be used to update a client with all new transactions if it already knows the old state up to a certain block.  ### Input Parameters - &#x60;blockhash&#x60; (string, optional): The block hash to list transactions since. - &#x60;target_confirmations&#x60; (numeric, optional): The confirmations required, must be 1 or more. - &#x60;include_watchonly&#x60; (bool, optional, default&#x3D;false): Include transactions to watch-only addresses.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;blockhash\&quot;: \&quot;000000000000000bacf66f7497b7dc45ef753ee9a7d38571037cdb1a57f663ad\&quot;,     \&quot;target_confirmations\&quot;: 6,     \&quot;include_watchonly\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with an array of transactions since the specified block and the hash of the last block.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [         {             \&quot;account\&quot;: \&quot;\&quot;,             \&quot;address\&quot;: \&quot;zcashaddress\&quot;,             \&quot;category\&quot;: \&quot;receive\&quot;,             \&quot;amount\&quot;: 10.0,             \&quot;vout\&quot;: 1,             ...         }     ],     \&quot;lastblock\&quot;: \&quot;lastblockhash\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ListSinceBlockRequest** | [**ListSinceBlockRequest**](../Models/ListSinceBlockRequest.md)|  | |

### Return type

[**ListSinceBlockResponse**](../Models/ListSinceBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listUnspentListunspentGet"></a>
# **listUnspentListunspentGet**
> ListUnspentResponse listUnspentListunspentGet(minconf, maxconf, Addresses)

List Unspent Transaction Outputs

    List unspent transaction outputs (UTXOs) with specified confirmations and optionally filtered by addresses.  ### Description - Returns an array of UTXOs with confirmations between the specified minimum and maximum.  ### Input Parameters - &#x60;minconf&#x60;: (Optional) Minimum number of confirmations. Default is 1. - &#x60;maxconf&#x60;: (Optional) Maximum number of confirmations. Default is 9999999. - &#x60;addresses&#x60;: (Optional) A list of Pastel addresses to filter.  ### Example Request - &#x60;GET /listunspent?minconf&#x3D;1&amp;maxconf&#x3D;9999999&#x60;  ### Response - Returns an array of UTXOs with detailed information about each.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;unspent_transactions\&quot;: [         {             \&quot;txid\&quot;: \&quot;12345\&quot;,             \&quot;vout\&quot;: 0,             \&quot;generated\&quot;: false,             \&quot;address\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,             \&quot;account\&quot;: \&quot;account_name\&quot;,             \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;,             \&quot;amount\&quot;: 0.0001,             \&quot;confirmations\&quot;: 10,             \&quot;redeemScript\&quot;: \&quot;abcd...\&quot;,             \&quot;spendable\&quot;: true         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallets and other applications to determine spendable balances.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |
| **maxconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 9999999] |
| **Addresses** | [**Addresses**](../Models/Addresses.md)|  | [optional] |

### Return type

[**ListUnspentResponse**](../Models/ListUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="reconsiderBlockReconsiderblockPost"></a>
# **reconsiderBlockReconsiderblockPost**
> ReconsiderBlockResponse reconsiderBlockReconsiderblockPost(ReconsiderBlockRequest)

Reconsider a previously invalidated block

    Removes invalidity status of a block and its descendants, reconsider them for activation.  ### Description - This endpoint is used to undo the effects of &#x60;invalidateblock&#x60;. - It reconsiders a block that was previously marked as invalid along with all its descendants.  ### Input Parameters - &#x60;hash&#x60;: (string, required) The hash of the block to reconsider.  ### Example Request - &#x60;POST /reconsiderblock {\&quot;hash\&quot;: \&quot;blockhash\&quot;}&#x60;  ### Response - Returns a JSON object indicating the success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Block and its descendants reconsidered successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the block hash is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method with caution as it affects the blockchain state.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ReconsiderBlockRequest** | [**ReconsiderBlockRequest**](../Models/ReconsiderBlockRequest.md)|  | |

### Return type

[**ReconsiderBlockResponse**](../Models/ReconsiderBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="submitBlockSubmitblockPost"></a>
# **submitBlockSubmitblockPost**
> SubmitBlockResponse submitBlockSubmitblockPost(SubmitBlockRequest)

Submit a new block to the network

    Attempt to submit a new block to the network.  ### Description - This endpoint attempts to submit a new block to the blockchain.  - The &#39;jsonparametersobject&#39; parameter is currently ignored.  ### Input Parameters - &#x60;hexdata&#x60;: Hex-encoded block data to submit. - &#x60;jsonparametersobject&#x60;: Optional JSON object of parameters.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;hexdata\&quot;: \&quot;blockdata\&quot;,     \&quot;jsonparametersobject\&quot;: {\&quot;workid\&quot;: \&quot;id\&quot;} } &#x60;&#x60;&#x60;  ### Response - Returns the result of the block submission.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;duplicate\&quot; // or \&quot;duplicate-invalid\&quot;, \&quot;duplicate-inconclusive\&quot;, \&quot;inconclusive\&quot;, \&quot;rejected\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if there are issues with the block data. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The block submission process follows the specification outlined in BIP 0022.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SubmitBlockRequest** | [**SubmitBlockRequest**](../Models/SubmitBlockRequest.md)|  | |

### Return type

[**SubmitBlockResponse**](../Models/SubmitBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="verifyChainVerifychainGet"></a>
# **verifyChainVerifychainGet**
> VerifyChainResponse verifyChainVerifychainGet(VerifyChainRequest)

Verify the blockchain database

    Verifies the integrity of the blockchain database.  ### Description - This endpoint performs checks on the blockchain database to verify its integrity.  - It allows specification of the thoroughness of the verification and the number of blocks to check.  ### Input Parameters - &#x60;checklevel&#x60;: (Optional) An integer between 0 and 4, indicating the thoroughness of the block verification (default is 3). - &#x60;numblocks&#x60;: (Optional) The number of blocks to check. Default is 288, with 0 indicating all blocks.  ### Example Request - &#x60;GET /verifychain?checklevel&#x3D;3&amp;numblocks&#x3D;288&#x60;  ### Response - Returns a JSON object containing the result of the verification as a boolean value.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verified\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are out of the expected range. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is important for network administrators and developers for diagnostics and ensuring the integrity of the blockchain data.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **VerifyChainRequest** | [**VerifyChainRequest**](../Models/VerifyChainRequest.md)|  | |

### Return type

[**VerifyChainResponse**](../Models/VerifyChainResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zGetBalanceZGetbalanceAddressGet"></a>
# **zGetBalanceZGetbalanceAddressGet**
> ZGetBalanceResponse zGetBalanceZGetbalanceAddressGet(address, minconf)

Get the balance of an address

    Get the balance of a transparent or private address in the Pastel blockchain.  ### Description - This endpoint returns the balance of a given t-address or z-address belonging to the node&#39;s wallet.  - CAUTION: If the wallet has only an incoming viewing key for this address, spends cannot be detected, and the returned balance may be larger than the actual balance.  ### Input Parameters - &#x60;address&#x60;: The address for which the balance is requested. It can be a transparent (t-address) or private (z-address). - &#x60;minconf&#x60; (optional): Only include transactions confirmed at least this many times. Default is 1.  ### Example Request - &#x60;GET /z_getbalance/myaddress&#x60; - &#x60;GET /z_getbalance/myaddress?minconf&#x3D;5&#x60;  ### Response - Returns a JSON object containing the balance of the specified address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balance\&quot;: 1234.56 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or does not belong to the node. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Balance is returned in )\&quot; + CURRENCY_UNIT + R\&quot;(. Primarily used to check the amount received by an address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **address** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**ZGetBalanceResponse**](../Models/ZGetBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetoperationresultZGetoperationresultGet"></a>
# **zGetoperationresultZGetoperationresultGet**
> ZGetOperationResultResponse zGetoperationresultZGetoperationresultGet(Operation\_Ids)

Retrieve the result and status of Zcash operations

    Retrieve the result and status of an operation which has finished, and then remove the operation from memory.  ### Description - This endpoint retrieves the results of one or more operations identified by their operation IDs. - It&#39;s primarily used to get the outcome of previously initiated Zcash shielded operations. - The operation is removed from memory after the result is retrieved.  ### Input Parameters - &#x60;operation_ids&#x60;: (Optional) A list of operation ids to query. If not provided, the endpoint examines all operations known to the node.  ### Example Request - &#x60;GET /z_getoperationresult?operation_ids&#x3D;[\&quot;opid-1234\&quot;, \&quot;opid-5678\&quot;]&#x60;  ### Response - Returns a JSON array containing the results of the queried operations.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operation_results\&quot;: [         {             \&quot;id\&quot;: \&quot;opid-1234\&quot;,             \&quot;status\&quot;: \&quot;success\&quot;,             \&quot;creation_time\&quot;: 1622547600,             \&quot;result\&quot;: {                 \&quot;txid\&quot;: \&quot;2f5b0e...\&quot;             },             \&quot;error\&quot;: null,             \&quot;method\&quot;: \&quot;z_sendmany\&quot;,             \&quot;params\&quot;: {                 \&quot;fromaddress\&quot;: \&quot;tm...\&quot;,                 \&quot;amounts\&quot;: [                     {                         \&quot;amount\&quot;: 0.1,                         \&quot;address\&quot;: \&quot;tm...\&quot;                     }                 ]             }         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint is specific to Zcash-based operations and is not applicable to standard Bitcoin transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **Operation\_Ids** | [**Operation_Ids**](../Models/Operation_Ids.md)|  | [optional] |

### Return type

[**ZGetOperationResultResponse**](../Models/ZGetOperationResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zListOperationIdsZListoperationidsGet"></a>
# **zListOperationIdsZListoperationidsGet**
> ZListOperationIdsResponse zListOperationIdsZListoperationidsGet(status)

List Operation IDs

    List all operation IDs currently known to the wallet.  ### Description - This endpoint retrieves a list of operation IDs that are known to the wallet.    It can optionally filter these IDs based on the operation&#39;s state.  ### Input Parameters - &#x60;status&#x60;: (Optional) A string to filter the operation IDs by their state, e.g., \&quot;success\&quot;.  ### Example Request - &#x60;GET /z_listoperationids?status&#x3D;success&#x60;  ### Response - Returns a JSON array containing the operation IDs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operation_ids\&quot;: [\&quot;opid-1\&quot;, \&quot;opid-2\&quot;, \&quot;opid-3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for tracking and managing asynchronous operations performed by the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **status** | [**Status**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**ZListOperationIdsResponse**](../Models/ZListOperationIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zListunspentZListunspentGet"></a>
# **zListunspentZListunspentGet**
> ZListUnspentResponse zListunspentZListunspentGet(minconf, maxconf, includeWatchonly, Addresses\_1)

List unspent shielded notes

    List unspent shielded notes with a specified range of confirmations and optionally filter for specific addresses.  ### Description - Returns an array of unspent shielded notes with a specified range of confirmations. Optionally filters to only include notes sent to specified addresses.  ### Input Parameters - &#x60;minconf&#x60;: Minimum number of confirmations to filter (default&#x3D;1). - &#x60;maxconf&#x60;: Maximum number of confirmations to filter (default&#x3D;9999999). - &#x60;includeWatchonly&#x60;: Whether to include watchonly addresses (default&#x3D;false). - &#x60;addresses&#x60;: Array of Sapling zaddrs to filter on (optional).  ### Example Request - &#x60;GET /z_listunspent?minconf&#x3D;1&amp;maxconf&#x3D;9999999&amp;includeWatchonly&#x3D;false&amp;addresses&#x3D;[\&quot;zaddr1\&quot;, \&quot;zaddr2\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing an unspent shielded note.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;unspent_notes\&quot;: [         {             \&quot;txid\&quot;: \&quot;txid\&quot;,             \&quot;outindex\&quot;: 0,             \&quot;confirmations\&quot;: 10,             \&quot;spendable\&quot;: true,             \&quot;address\&quot;: \&quot;address\&quot;,             \&quot;amount\&quot;: 123.45,             \&quot;memo\&quot;: \&quot;hex_memo\&quot;,             \&quot;change\&quot;: false         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for wallet balance management and transaction preparation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **maxconf** | [**Maxconf**](../Models/.md)|  | [optional] [default to 9999999] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |
| **Addresses\_1** | [**Addresses_1**](../Models/Addresses_1.md)|  | [optional] |

### Return type

[**ZListUnspentResponse**](../Models/ZListUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zShieldcoinbaseZShieldcoinbasePost"></a>
# **zShieldcoinbaseZShieldcoinbasePost**
> ZShieldCoinbaseResponse zShieldcoinbaseZShieldcoinbasePost(ZShieldCoinbaseRequest)

Shield transparent coinbase funds to a shielded zaddr

    Shield transparent coinbase funds by sending them to a shielded z-address.                              This is an asynchronous operation, and UTXOs selected for shielding will be locked.  ### Description - Shields coinbase UTXOs from a transparent address (taddr) to a shielded address (zaddr), locking the UTXOs involved in the process.  ### Input Parameters - &#x60;fromaddress&#x60;: The source transparent address or \&quot;*\&quot; for all taddrs belonging to the wallet. - &#x60;toaddress&#x60;: The destination shielded address. - &#x60;fee&#x60;: (Optional) The fee amount to attach to this transaction. - &#x60;limit&#x60;: (Optional) The maximum number of UTXOs to shield. Set to 0 to shield as many as will fit in the transaction.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaddress\&quot;: \&quot;t1exampleaddress...\&quot;,     \&quot;toaddress\&quot;: \&quot;zs1exampleaddress...\&quot;,     \&quot;fee\&quot;: 0.0001,     \&quot;limit\&quot;: 50 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details about the shielding process including the operation id.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;remainingUTXOs\&quot;: 100,     \&quot;remainingValue\&quot;: 2.5,     \&quot;shieldingUTXOs\&quot;: 50,     \&quot;shieldingValue\&quot;: 1.5,     \&quot;opid\&quot;: \&quot;opid-example-1234\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZShieldCoinbaseRequest** | [**ZShieldCoinbaseRequest**](../Models/ZShieldCoinbaseRequest.md)|  | |

### Return type

[**ZShieldCoinbaseResponse**](../Models/ZShieldCoinbaseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zViewTransactionZViewtransactionTxidGet"></a>
# **zViewTransactionZViewtransactionTxidGet**
> ZViewTransactionResponse zViewTransactionZViewtransactionTxidGet(txid)

Get detailed shielded information about in-wallet transaction

    Retrieve detailed information about a shielded transaction in the wallet.  ### Description - Returns detailed information about a specific in-wallet transaction, including spends and outputs related to shielded addresses.  ### Input Parameters - &#x60;txid&#x60;: The transaction id (string, required).  ### Example Request - &#x60;GET /z_viewtransaction/1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d&#x60;  ### Response - Returns detailed information about the transaction, including spends and outputs.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d\&quot;,     \&quot;spends\&quot;: [...],     \&quot;outputs\&quot;: [...] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 404: Transaction not found or not part of the wallet.  ### Note - This endpoint is used to get detailed information about shielded transactions, particularly for auditing and verification purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**ZViewTransactionResponse**](../Models/ZViewTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

