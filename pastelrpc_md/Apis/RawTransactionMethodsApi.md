# RawTransactionMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRawTransactionCreaterawtransactionPost**](RawTransactionMethodsApi.md#createRawTransactionCreaterawtransactionPost) | **POST** /createrawtransaction | Create a raw transaction |
| [**decodeRawTransactionDecoderawtransactionPost**](RawTransactionMethodsApi.md#decodeRawTransactionDecoderawtransactionPost) | **POST** /decoderawtransaction | Decode a raw transaction |
| [**fundRawTransactionFundrawtransactionPost**](RawTransactionMethodsApi.md#fundRawTransactionFundrawtransactionPost) | **POST** /fundrawtransaction | Add inputs to a transaction |
| [**getRawChangeAddressGetrawchangeaddressGet**](RawTransactionMethodsApi.md#getRawChangeAddressGetrawchangeaddressGet) | **GET** /getrawchangeaddress | Get a new Pastel address for receiving change |
| [**getRawTransactionGetrawtransactionPost**](RawTransactionMethodsApi.md#getRawTransactionGetrawtransactionPost) | **POST** /getrawtransaction | Get the raw transaction data |
| [**getTxOutProofGettxoutproofGet**](RawTransactionMethodsApi.md#getTxOutProofGettxoutproofGet) | **GET** /gettxoutproof | Get proof of transaction inclusion in a block |
| [**sendFromSendfromPost**](RawTransactionMethodsApi.md#sendFromSendfromPost) | **POST** /sendfrom | Send amount from an account to a Pastel address |
| [**sendManySendmanyPost**](RawTransactionMethodsApi.md#sendManySendmanyPost) | **POST** /sendmany | Send multiple transactions |
| [**sendRawTransactionSendrawtransactionPost**](RawTransactionMethodsApi.md#sendRawTransactionSendrawtransactionPost) | **POST** /sendrawtransaction | Submit a raw transaction to the network |
| [**signRawTransactionSignrawtransactionPost**](RawTransactionMethodsApi.md#signRawTransactionSignrawtransactionPost) | **POST** /signrawtransaction | Sign a raw transaction |
| [**zMergetoaddressZMergetoaddressPost**](RawTransactionMethodsApi.md#zMergetoaddressZMergetoaddressPost) | **POST** /z_mergetoaddress | Merge multiple UTXOs and notes into a single UTXO or note |
| [**zSendManyZSendmanyPost**](RawTransactionMethodsApi.md#zSendManyZSendmanyPost) | **POST** /z_sendmany | Send multiple times to multiple recipients |


<a name="createRawTransactionCreaterawtransactionPost"></a>
# **createRawTransactionCreaterawtransactionPost**
> CreateRawTransactionResponse createRawTransactionCreaterawtransactionPost(CreateRawTransactionRequest)

Create a raw transaction

    Create a transaction spending the given inputs and sending to the given addresses.  ### Description - This endpoint creates a hex-encoded raw transaction that spends the given inputs and sends to the specified addresses. - The transaction&#39;s inputs are not signed, and it is not stored in the wallet or transmitted to the network.  ### Input Parameters - &#x60;transactions&#x60;: A list of transaction inputs, each containing:     - &#x60;txid&#x60;: The transaction id.     - &#x60;vout&#x60;: The output number.     - &#x60;sequence&#x60;: (Optional) The sequence number. - &#x60;addresses&#x60;: A dictionary with addresses as keys and amounts as values. - &#x60;locktime&#x60;: (Optional) Raw locktime. Non-0 value also activates inputs. - &#x60;expiryheight&#x60;: (Optional) Expiry height of transaction (if Overwinter is active).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [{\&quot;txid\&quot;: \&quot;myid\&quot;, \&quot;vout\&quot;: 0}],     \&quot;addresses\&quot;: {\&quot;address\&quot;: 0.01},     \&quot;locktime\&quot;: 0,     \&quot;expiryheight\&quot;: 1000 } &#x60;&#x60;&#x60;  ### Response - Returns a hex string of the transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction\&quot;: \&quot;hex-encoded-transaction\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateRawTransactionRequest** | [**CreateRawTransactionRequest**](../Models/CreateRawTransactionRequest.md)|  | |

### Return type

[**CreateRawTransactionResponse**](../Models/CreateRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="decodeRawTransactionDecoderawtransactionPost"></a>
# **decodeRawTransactionDecoderawtransactionPost**
> DecodeRawTransactionResponse decodeRawTransactionDecoderawtransactionPost(DecodeRawTransactionRequest)

Decode a raw transaction

    Decode a serialized, hex-encoded transaction and return a JSON object representing it.  ### Description - This endpoint decodes a raw, serialized, hex-encoded transaction and provides detailed information about it.  ### Input Parameters - &#x60;hexstring&#x60; (string, required): The hex-encoded transaction string to decode.  ### Example Request - &#x60;POST /decoderawtransaction&#x60; with body &#x60;{\&quot;hexstring\&quot;: \&quot;hex-encoded-string\&quot;}&#x60;  ### Response - Returns a JSON object containing detailed information about the transaction, including &#x60;txid&#x60;, &#x60;size&#x60;, &#x60;overwintered&#x60; flag, &#x60;version&#x60;, &#x60;locktime&#x60;, &#x60;vin&#x60;, and &#x60;vout&#x60; fields.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;id\&quot;,     \&quot;size\&quot;: n,     \&quot;overwintered\&quot;: true,     \&quot;version\&quot;: n,     \&quot;versiongroupid\&quot;: \&quot;hex\&quot;,     \&quot;locktime\&quot;: ttt,     \&quot;expiryheight\&quot;: n,     \&quot;vin\&quot;: [         {             \&quot;txid\&quot;: \&quot;id\&quot;,             \&quot;vout\&quot;: n,             \&quot;scriptSig\&quot;: {                 \&quot;asm\&quot;: \&quot;asm\&quot;,                 \&quot;hex\&quot;: \&quot;hex\&quot;             },             \&quot;sequence\&quot;: n         }     ],     \&quot;vout\&quot;: [         {             \&quot;value\&quot;: x.xxx,             \&quot;n\&quot;: n,             \&quot;scriptPubKey\&quot;: {                 \&quot;asm\&quot;: \&quot;asm\&quot;,                 \&quot;hex\&quot;: \&quot;hex\&quot;,                 \&quot;reqSigs\&quot;: n,                 \&quot;type\&quot;: \&quot;pubkeyhash\&quot;,                 \&quot;addresses\&quot;: [                     \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;                 ]             }         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;hexstring&#x60; parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for debugging transactions and understanding their structure.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DecodeRawTransactionRequest** | [**DecodeRawTransactionRequest**](../Models/DecodeRawTransactionRequest.md)|  | |

### Return type

[**DecodeRawTransactionResponse**](../Models/DecodeRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="fundRawTransactionFundrawtransactionPost"></a>
# **fundRawTransactionFundrawtransactionPost**
> FundRawTransactionResponse fundRawTransactionFundrawtransactionPost(FundRawTransactionRequest)

Add inputs to a transaction

    Add inputs to a transaction until it has enough in value to meet its out value.  ### Description - This endpoint adds inputs to a raw transaction represented by a hex string. It ensures the transaction has enough value to meet its output value. - It will not modify existing inputs and will add one change output to the outputs. - Note that inputs which were signed may need to be re-signed after completion since inputs/outputs have been added. - The inputs added by this method will not be signed; use &#x60;signrawtransaction&#x60; for that.  ### Input Parameters - &#x60;hexstring&#x60;: A string representing the raw transaction in hexadecimal format.  ### Example Request - &#x60;POST /fundrawtransaction&#x60; with JSON body &#x60;{\&quot;hexstring\&quot;: \&quot;rawtransactionhex\&quot;}&#x60;  ### Response - Returns a JSON object containing the resulting raw transaction, the fee added, and the position of the added change output.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;fundedtransactionhex\&quot;,     \&quot;fee\&quot;: 0.0012,     \&quot;changepos\&quot;: 1 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;hexstring&#x60; parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is part of the transaction creation process, typically followed by &#x60;signrawtransaction&#x60; and &#x60;sendrawtransaction&#x60;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **FundRawTransactionRequest** | [**FundRawTransactionRequest**](../Models/FundRawTransactionRequest.md)|  | |

### Return type

[**FundRawTransactionResponse**](../Models/FundRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getRawChangeAddressGetrawchangeaddressGet"></a>
# **getRawChangeAddressGetrawchangeaddressGet**
> oas_any_type_not_mapped getRawChangeAddressGetrawchangeaddressGet()

Get a new Pastel address for receiving change

    Get a new Pastel address for receiving change. This is for use with raw transactions, NOT for normal use.  ### Description - This endpoint generates and returns a new Pastel address that can be used for receiving change in raw transactions. - It is important to note that this address should not be used for regular transactions.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getrawchangeaddress&#x60;  ### Response - Returns a string representing the new Pastel address.  ### Example Response &#x60;&#x60;&#x60;json \&quot;mnX4Ph6uhz2ez5y9Yb9hWPiPH5G9Wp2VWJ\&quot; &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - RPC_WALLET_KEYPOOL_RAN_OUT: Error message if the keypool has run out. In this case, the &#x60;keypoolrefill&#x60; RPC method should be called first.  ### Note - This address should only be used for change in raw transactions and not for general transaction purposes.

### Parameters
This endpoint does not need any parameter.

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getRawTransactionGetrawtransactionPost"></a>
# **getRawTransactionGetrawtransactionPost**
> oas_any_type_not_mapped getRawTransactionGetrawtransactionPost(GetRawTransactionRequest)

Get the raw transaction data

    Get the raw transaction data for a given transaction id.  ### Description - This endpoint returns the raw transaction data based on the given transaction ID. - If &#x60;verbose&#x60; is 0 or not set, it returns a string that is serialized, hex-encoded data for the transaction. - If &#x60;verbose&#x60; is non-zero, it returns a JSON object with detailed information about the transaction.  ### Input Parameters - &#x60;txid&#x60; (string, required): The transaction id. - &#x60;verbose&#x60; (int, optional, default&#x3D;0): If 0, return a string, otherwise return a JSON object. - &#x60;blockhash&#x60; (string, optional): The block hash to look for the transaction in.  ### Example Request - &#x60;POST /getrawtransaction&#x60; with JSON body &#x60;{\&quot;txid\&quot;: \&quot;mytxid\&quot;, \&quot;verbose\&quot;: 1}&#x60;  ### Response - Depending on the &#x60;verbose&#x60; parameter, either a string or a JSON object with detailed transaction information.  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetRawTransactionRequest** | [**GetRawTransactionRequest**](../Models/GetRawTransactionRequest.md)|  | |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getTxOutProofGettxoutproofGet"></a>
# **getTxOutProofGettxoutproofGet**
> GetTxOutProofResponse getTxOutProofGettxoutproofGet(body, block\_hash)

Get proof of transaction inclusion in a block

    Get a hex-encoded proof that one or more transactions were included in a block.  ### Description - This endpoint returns a serialized, hex-encoded data for the proof that specified transaction(s) were included in a block. - By default, this function only works if there is an unspent output in the UTXO for these transactions. To make it always work, maintain a transaction index with the -txindex command line option, or specify the block hash manually.  ### Input Parameters - &#x60;txids&#x60;: A list of transaction IDs to filter. - &#x60;block_hash&#x60; (Optional): The hash of the block in which to look for the transactions.  ### Example Request - &#x60;GET /gettxoutproof?txids&#x3D;[\&quot;txid1\&quot;,\&quot;txid2\&quot;]&amp;block_hash&#x3D;00000000abc123&#x60;  ### Response - Returns a string that is a serialized, hex-encoded data for the proof.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;data\&quot;: \&quot;serialized-hex-encoded-proof-data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure that the transaction index is maintained for accurate results.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **body** | **oas_any_type_not_mapped**|  | |
| **block\_hash** | [**Block_Hash**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**GetTxOutProofResponse**](../Models/GetTxOutProofResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendFromSendfromPost"></a>
# **sendFromSendfromPost**
> SendFromResponse sendFromSendfromPost(fromaccount, tozcashaddress, amount, minconf, comment, comment\_to)

Send amount from an account to a Pastel address

    Send an amount from an account to a specified Pastel address.                ### Description - This endpoint is a deprecated method (use sendtoaddress) for sending an amount from an account to a Pastel address. The amount is a real number and is rounded to the nearest 0.00000001.  ### Input Parameters - &#x60;fromaccount&#x60;: (string, required) Must be set to the empty string \&quot;\&quot; to represent the default account. Any other string will result in an error. - &#x60;tozcashaddress&#x60;: (string, required) The Pastel address to send funds to. - &#x60;amount&#x60;: (numeric, required) The amount in PSL. - &#x60;minconf&#x60;: (numeric, optional, default&#x3D;1) Only use funds with at least this many confirmations. - &#x60;comment&#x60;: (string, optional) A comment for the transaction, stored in your wallet. - &#x60;comment_to&#x60;: (string, optional) A comment to store the name of the person/organization to which you&#39;re sending the transaction, stored in your wallet.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaccount\&quot;: \&quot;\&quot;,     \&quot;tozcashaddress\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;amount\&quot;: 0.01,     \&quot;minconf\&quot;: 1,     \&quot;comment\&quot;: \&quot;donation\&quot;,     \&quot;comment_to\&quot;: \&quot;seans outpost\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;transactionid1234567890\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Invalid request parameters. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s recommended to use &#x60;sendtoaddress&#x60; instead of this deprecated method.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fromaccount** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **tozcashaddress** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **amount** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **comment** | [**Comment**](../Models/.md)|  | [optional] [default to null] |
| **comment\_to** | [**Comment_To**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**SendFromResponse**](../Models/SendFromResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="sendManySendmanyPost"></a>
# **sendManySendmanyPost**
> SendManyResponse sendManySendmanyPost(SendManyRequest)

Send multiple transactions

    Send multiple times. Amounts are decimal numbers with at most 8 digits of precision.  ### Description - This endpoint sends multiple transactions to multiple addresses.  ### Input Parameters - &#x60;from_account&#x60;: MUST be set to the empty string \&quot;\&quot; to represent the default account. Any other string will result in an error. - &#x60;amounts&#x60;: A JSON object with addresses and amounts. - &#x60;min_conf&#x60;: Optional, minimum number of confirmations. Default is 1. - &#x60;comment&#x60;: Optional, a comment for the transaction. - &#x60;subtract_fee_from_amount&#x60;: Optional, a list of addresses from which the fee will be subtracted. - &#x60;change_address&#x60;: Optional, the destination address for the change. Can be \&quot;original\&quot;, \&quot;new\&quot;, or a specific Pastel t-address.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;from_account\&quot;: \&quot;\&quot;,     \&quot;amounts\&quot;: {         \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;: 0.01     },     \&quot;min_conf\&quot;: 1,     \&quot;comment\&quot;: \&quot;Test transaction\&quot;,     \&quot;subtract_fee_from_amount\&quot;: [\&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;],     \&quot;change_address\&quot;: \&quot;original\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;transaction_id_here\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendManyRequest** | [**SendManyRequest**](../Models/SendManyRequest.md)|  | |

### Return type

[**SendManyResponse**](../Models/SendManyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendRawTransactionSendrawtransactionPost"></a>
# **sendRawTransactionSendrawtransactionPost**
> SendRawTransactionResponse sendRawTransactionSendrawtransactionPost(SendRawTransactionRequest)

Submit a raw transaction to the network

    Submit a raw transaction (serialized, hex-encoded) to the local node and network.  ### Description - This endpoint is used to submit a serialized, hex-encoded transaction to the network. - It can be used in combination with &#x60;createrawtransaction&#x60; and &#x60;signrawtransaction&#x60; calls.  ### Input Parameters - &#x60;hexstring&#x60; (string, required): The hex string of the raw transaction. - &#x60;allowhighfees&#x60; (boolean, optional, default&#x3D;false): Allow high fees.  ### Example Request - &#x60;POST /sendrawtransaction&#x60; with JSON body:  &#x60;&#x60;&#x60;json {     \&quot;hexstring\&quot;: \&quot;signedhex\&quot;,     \&quot;allowhighfees\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction hash.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tx_hash\&quot;: \&quot;transactionhashinhex\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendRawTransactionRequest** | [**SendRawTransactionRequest**](../Models/SendRawTransactionRequest.md)|  | |

### Return type

[**SendRawTransactionResponse**](../Models/SendRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signRawTransactionSignrawtransactionPost"></a>
# **signRawTransactionSignrawtransactionPost**
> SignRawTransactionResponse signRawTransactionSignrawtransactionPost(SignRawTransactionRequest)

Sign a raw transaction

    Sign inputs for a raw transaction (serialized, hex-encoded).  ### Description - This endpoint signs the inputs of a given raw transaction.  ### Input Parameters - &#x60;hexstring&#x60;: The transaction hex string. - &#x60;prevtxs&#x60;: An optional array of previous dependent transaction outputs. - &#x60;privatekeys&#x60;: An optional array of base58-encoded private keys for signing. - &#x60;sighashtype&#x60;: The signature hash type (default is \&quot;ALL\&quot;). - &#x60;branchid&#x60;: An optional consensus branch ID for signing.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;hexstring\&quot;: \&quot;01000000...\&quot;,     \&quot;prevtxs\&quot;: [{\&quot;txid\&quot;: \&quot;0123abcd...\&quot;, \&quot;vout\&quot;: 0, \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;, \&quot;amount\&quot;: 0.1}],     \&quot;privatekeys\&quot;: [\&quot;5J1m2B...\&quot;, \&quot;5Hs2R...\&quot;],     \&quot;sighashtype\&quot;: \&quot;ALL\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns the signed transaction in hex format, along with a flag indicating if the transaction has a complete set of signatures.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;01000000...\&quot;,     \&quot;complete\&quot;: true,     \&quot;errors\&quot;: [] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint is used for manually signing raw transactions before broadcasting them to the network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SignRawTransactionRequest** | [**SignRawTransactionRequest**](../Models/SignRawTransactionRequest.md)|  | |

### Return type

[**SignRawTransactionResponse**](../Models/SignRawTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zMergetoaddressZMergetoaddressPost"></a>
# **zMergetoaddressZMergetoaddressPost**
> MergeToAddressResponse zMergetoaddressZMergetoaddressPost(MergeToAddressRequest)

Merge multiple UTXOs and notes into a single UTXO or note

    Merge multiple UTXOs and notes into a single UTXO or note.  ### Description - This endpoint merges multiple UTXOs and notes into a single UTXO or note. Coinbase UTXOs are ignored; use &#x60;z_shieldcoinbase&#x60; to combine those into a single note. - It&#39;s an asynchronous operation, and UTXOs selected for merging will be locked. If there is an error, they are unlocked. - The number of UTXOs and notes selected for merging can be limited by the caller.  ### Input Parameters - &#x60;fromaddresses&#x60;: List of addresses. Special strings \&quot;ANY_TADDR\&quot; and \&quot;ANY_SAPLING\&quot; can be used. - &#x60;toaddress&#x60;: The address to send the funds to. - &#x60;fee&#x60;: Optional fee amount to attach to this transaction. - &#x60;transparent_limit&#x60;: Optional limit on the number of UTXOs to merge. - &#x60;shielded_limit&#x60;: Optional limit on the number of notes to merge. - &#x60;memo&#x60;: Optional memo, encoded as hex, applicable only for zaddr.  ### Example Request &#x60;&#x60;&#x60;json {   \&quot;fromaddresses\&quot;: [\&quot;ANY_SAPLING\&quot;, \&quot;t1XYZ\&quot;],   \&quot;toaddress\&quot;: \&quot;t1ABC\&quot;,   \&quot;fee\&quot;: 0.001,   \&quot;transparent_limit\&quot;: 50,   \&quot;shielded_limit\&quot;: 200,   \&quot;memo\&quot;: \&quot;48656c6c6f\&quot; } &#x60;&#x60;&#x60;  ### Response - Detailed information about the merge operation, including the number of UTXOs and notes merged, remaining ones, and the operation ID.  ### Possible Errors - HTTP 400: Bad Request for invalid parameters. - HTTP 500: Internal Server Error for processing issues.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MergeToAddressRequest** | [**MergeToAddressRequest**](../Models/MergeToAddressRequest.md)|  | |

### Return type

[**MergeToAddressResponse**](../Models/MergeToAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zSendManyZSendmanyPost"></a>
# **zSendManyZSendmanyPost**
> SendManyResponse zSendManyZSendmanyPost(SendManyRequest)

Send multiple times to multiple recipients

    Send multiple times to multiple recipients. This endpoint allows for sending transactions to multiple addresses.  ### Description - Allows for sending specified amounts to multiple taddr or zaddr addresses from a single fromaddress.  ### Input Parameters - &#x60;SendManyRequest&#x60;: A JSON object containing the sending address, a list of recipient addresses with amounts and optional memos, minimum confirmations, and an optional fee.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;fromaddress\&quot;: \&quot;t1XYZ...\&quot;,     \&quot;amounts\&quot;: [         {\&quot;address\&quot;: \&quot;t1ABC...\&quot;, \&quot;amount\&quot;: 0.1, \&quot;memo\&quot;: \&quot;Optional memo\&quot;},         {\&quot;address\&quot;: \&quot;t1DEF...\&quot;, \&quot;amount\&quot;: 0.2}     ],     \&quot;minconf\&quot;: 1,     \&quot;fee\&quot;: 0.0001 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the operation ID of the send operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operationid\&quot;: \&quot;opid-1234567890abcdef\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for creating complex transactions involving multiple recipients.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendManyRequest** | [**SendManyRequest**](../Models/SendManyRequest.md)|  | |

### Return type

[**SendManyResponse**](../Models/SendManyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

