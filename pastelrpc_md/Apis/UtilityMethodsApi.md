# UtilityMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMultisigAddressAddmultisigaddressPost**](UtilityMethodsApi.md#addMultisigAddressAddmultisigaddressPost) | **POST** /addmultisigaddress | Add a multisignature address |
| [**backupWalletBackupwalletPost**](UtilityMethodsApi.md#backupWalletBackupwalletPost) | **POST** /backupwallet | Backup the wallet to a destination |
| [**createMultisigCreatemultisigPost**](UtilityMethodsApi.md#createMultisigCreatemultisigPost) | **POST** /createmultisig | Create a multisig address |
| [**decodeScriptDecodescriptPost**](UtilityMethodsApi.md#decodeScriptDecodescriptPost) | **POST** /decodescript | Decode a hex-encoded script |
| [**estimatePriorityEstimatepriorityGet**](UtilityMethodsApi.md#estimatePriorityEstimatepriorityGet) | **GET** /estimatepriority | Estimate the transaction priority for zero-fee confirmation |
| [**generatePastelIdNewkeyPastelidNewkeyPost**](UtilityMethodsApi.md#generatePastelIdNewkeyPastelidNewkeyPost) | **POST** /pastelid/newkey | Generate new Pastel ID and keys |
| [**generateReportGenerateReportReportNameGet**](UtilityMethodsApi.md#generateReportGenerateReportReportNameGet) | **GET** /generate-report/{report_name} | Generate various reports |
| [**getActionFeesStoragefeeGetactionfeesGet**](UtilityMethodsApi.md#getActionFeesStoragefeeGetactionfeesGet) | **GET** /storagefee/getactionfees | Get action fees based on data size |
| [**getAddressMempoolGetaddressmempoolGet**](UtilityMethodsApi.md#getAddressMempoolGetaddressmempoolGet) | **GET** /getaddressmempool | Get all mempool deltas for an address |
| [**getFeeScheduleGetfeescheduleGet**](UtilityMethodsApi.md#getFeeScheduleGetfeescheduleGet) | **GET** /getfeeschedule | Get the current fee schedule |
| [**getMemoryInfoGetmemoryinfoGet**](UtilityMethodsApi.md#getMemoryInfoGetmemoryinfoGet) | **GET** /getmemoryinfo | Get memory usage information |
| [**getMempoolInfoGetmempoolinfoGet**](UtilityMethodsApi.md#getMempoolInfoGetmempoolinfoGet) | **GET** /getmempoolinfo | Get active state of the TX memory pool |
| [**getNewAddressGetnewaddressGet**](UtilityMethodsApi.md#getNewAddressGetnewaddressGet) | **GET** /getnewaddress | Generate a new Pastel address |
| [**getStorageFeeGetFeeStoragefeeGetfeeGet**](UtilityMethodsApi.md#getStorageFeeGetFeeStoragefeeGetfeeGet) | **GET** /storagefee/getfee | Get the storage fee |
| [**getStorageFeesStoragefeeGetfeesGet**](UtilityMethodsApi.md#getStorageFeesStoragefeeGetfeesGet) | **GET** /storagefee/getfees | Get the current storage fees |
| [**getWalletInfoGetwalletinfoGet**](UtilityMethodsApi.md#getWalletInfoGetwalletinfoGet) | **GET** /getwalletinfo | Get wallet state information |
| [**governanceActionGovernancePost**](UtilityMethodsApi.md#governanceActionGovernancePost) | **POST** /governance | Cast a vote or list governance tickets |
| [**pastelidNewkeyPastelidNewkeyPost**](UtilityMethodsApi.md#pastelidNewkeyPastelidNewkeyPost) | **POST** /pastelid_newkey | Generate new Pastel ID and associated keys |
| [**pastelidPasswdPastelidPasswdPost**](UtilityMethodsApi.md#pastelidPasswdPastelidPasswdPost) | **POST** /pastelid/passwd | Change passphrase for PastelID secure container |
| [**pastelidSignFilePastelidSignfilePost**](UtilityMethodsApi.md#pastelidSignFilePastelidSignfilePost) | **POST** /pastelid/signfile | Sign a file with a Pastel ID |
| [**pastelidVerifyFilePastelidVerifyFilePost**](UtilityMethodsApi.md#pastelidVerifyFilePastelidVerifyFilePost) | **POST** /pastelid/verify-file | Verify a file&#39;s signature with a Pastel ID |
| [**pastelidVerifyPastelidVerifyPost**](UtilityMethodsApi.md#pastelidVerifyPastelidVerifyPost) | **POST** /pastelid/verify | Verify a signature with PastelID |
| [**pingPingGet**](UtilityMethodsApi.md#pingPingGet) | **GET** /ping | Send a ping to all nodes |
| [**resendWalletTransactionsResendwallettransactionsPost**](UtilityMethodsApi.md#resendWalletTransactionsResendwallettransactionsPost) | **POST** /resendwallettransactions | Re-broadcast unconfirmed wallet transactions |
| [**retrieveChaindataChaindataRetrievePost**](UtilityMethodsApi.md#retrieveChaindataChaindataRetrievePost) | **POST** /chaindata/retrieve | Retrieve data from the blockchain |
| [**scanForMissingTxsScanformissingtxsPost**](UtilityMethodsApi.md#scanForMissingTxsScanformissingtxsPost) | **POST** /scanformissingtxs | Scan for missing transactions |
| [**sendToAddressSendtoaddressPost**](UtilityMethodsApi.md#sendToAddressSendtoaddressPost) | **POST** /sendtoaddress | Send an amount to a given address |
| [**setTxFeeSettxfeePost**](UtilityMethodsApi.md#setTxFeeSettxfeePost) | **POST** /settxfee | Set the transaction fee per kB |
| [**signMessageSignmessagePost**](UtilityMethodsApi.md#signMessageSignmessagePost) | **POST** /signmessage | Sign a message with the private key of a t-addr |
| [**signWithPastelIdPastelidSignPost**](UtilityMethodsApi.md#signWithPastelIdPastelidSignPost) | **POST** /pastelid/sign | Sign a text with Pastel ID |
| [**storeChaindataChaindataStorePost**](UtilityMethodsApi.md#storeChaindataChaindataStorePost) | **POST** /chaindata/store | Store data in the blockchain |
| [**validateAddressValidateaddressPost**](UtilityMethodsApi.md#validateAddressValidateaddressPost) | **POST** /validateaddress | Validate a Pastel address |
| [**verifyMessageVerifymessagePost**](UtilityMethodsApi.md#verifyMessageVerifymessagePost) | **POST** /verifymessage | Verify a signed message |
| [**zGetNotesCountZGetnotescountGet**](UtilityMethodsApi.md#zGetNotesCountZGetnotescountGet) | **GET** /z_getnotescount | Get the count of sapling notes in the wallet |
| [**zGetOperationStatusZGetoperationstatusGet**](UtilityMethodsApi.md#zGetOperationStatusZGetoperationstatusGet) | **GET** /z_getoperationstatus | Get the status of asynchronous operations |
| [**zListReceivedByAddressZListreceivedbyaddressGet**](UtilityMethodsApi.md#zListReceivedByAddressZListreceivedbyaddressGet) | **GET** /z_listreceivedbyaddress | List amounts received by a z-address |
| [**zValidateAddressZValidateaddressGet**](UtilityMethodsApi.md#zValidateAddressZValidateaddressGet) | **GET** /z_validateaddress | Validate a Z address |
| [**zcBenchmarkZcbenchmarkPost**](UtilityMethodsApi.md#zcBenchmarkZcbenchmarkPost) | **POST** /zcbenchmark | Runs a benchmark of the selected type |


<a name="addMultisigAddressAddmultisigaddressPost"></a>
# **addMultisigAddressAddmultisigaddressPost**
> AddMultisigAddressResponse addMultisigAddressAddmultisigaddressPost(AddMultisigAddressRequest)

Add a multisignature address

    Add a nrequired-to-sign multisignature address to the wallet.                              Each key is a Pastel address or hex-encoded public key.  ### Description - This endpoint adds a multisignature address to the wallet which requires a specified number of signatures to authorize a transaction. - Each key in the &#x60;keysobject&#x60; list can be either a Pastel address or a hex-encoded public key.  ### Input Parameters - &#x60;nrequired&#x60; (int): The number of required signatures out of the n keys or addresses. - &#x60;keysobject&#x60; (List[str]): A list of Pastel addresses or hex-encoded public keys. - &#x60;account&#x60; (str, optional): DEPRECATED. Must be set to an empty string \&quot;\&quot; for the default account. Any other string will result in an error.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nrequired\&quot;: 2,     \&quot;keysobject\&quot;: [\&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;, \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;],     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the newly created Pastel address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;pZc4pUvczxNG1Sfh5Zx3n2fuFjGjTDbB4qu\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **AddMultisigAddressRequest** | [**AddMultisigAddressRequest**](../Models/AddMultisigAddressRequest.md)|  | |

### Return type

[**AddMultisigAddressResponse**](../Models/AddMultisigAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="backupWalletBackupwalletPost"></a>
# **backupWalletBackupwalletPost**
> BackupWalletResponse backupWalletBackupwalletPost(BackupWalletRequest)

Backup the wallet to a destination

    Backup the wallet.dat file to a specified destination filename.  ### Description - Safely copies the wallet.dat file to the specified destination. The destination is a filename and should be saved in the directory set by the &#x60;-exportdir&#x60; option.  ### Input Parameters - &#x60;destination&#x60;: (string, required) The destination filename.  ### Example Request - &#x60;POST /backupwallet&#x60; with JSON body &#x60;{\&quot;destination\&quot;: \&quot;backupdata\&quot;}&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet was backed up.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/backup/backupdata\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the destination filename is invalid or not provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request, such as if the &#x60;-exportdir&#x60; option is not set or the wallet backup fails.  ### Note - It&#39;s crucial to regularly backup your wallet to prevent loss of funds in case of system failures.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **BackupWalletRequest** | [**BackupWalletRequest**](../Models/BackupWalletRequest.md)|  | |

### Return type

[**BackupWalletResponse**](../Models/BackupWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createMultisigCreatemultisigPost"></a>
# **createMultisigCreatemultisigPost**
> CreateMultisigResponse createMultisigCreatemultisigPost(CreateMultisigRequest)

Create a multisig address

    Creates a multi-signature address with n signatures of m keys required.  ### Description - This endpoint creates a multi-signature address requiring a specified number of signatures from a set of provided keys. - It returns the new multisig address and the hex-encoded redemption script.  ### Input Parameters - &#x60;nrequired&#x60;: The number of required signatures out of the n keys or addresses. - &#x60;keys&#x60;: A list of Pastel addresses or hex-encoded public keys.  ### Example Request - &#x60;POST /createmultisig&#x60; &#x60;&#x60;&#x60;json {     \&quot;nrequired\&quot;: 2,     \&quot;keys\&quot;: [\&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;, \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the multisig address and the hex-encoded redemption script.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;multisigaddress\&quot;,     \&quot;redeemScript\&quot;: \&quot;script\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **CreateMultisigRequest** | [**CreateMultisigRequest**](../Models/CreateMultisigRequest.md)|  | |

### Return type

[**CreateMultisigResponse**](../Models/CreateMultisigResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="decodeScriptDecodescriptPost"></a>
# **decodeScriptDecodescriptPost**
> DecodeScriptResponse decodeScriptDecodescriptPost(DecodeScriptRequest)

Decode a hex-encoded script

    Decode a hex-encoded script.  ### Description - This endpoint decodes a hex-encoded script and returns detailed information about it.  ### Input Parameters - &#x60;hex&#x60;: A string representing the hex-encoded script.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;hex\&quot;: \&quot;hexstring\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details about the script, such as its assembly representation, type, required signatures, associated addresses, and P2SH.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;asm\&quot;: \&quot;asm\&quot;,     \&quot;hex\&quot;: \&quot;hex\&quot;,     \&quot;type\&quot;: \&quot;type\&quot;,     \&quot;reqSigs\&quot;: 1,     \&quot;addresses\&quot;: [\&quot;address1\&quot;, \&quot;address2\&quot;],     \&quot;p2sh\&quot;: \&quot;address\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the hex parameter is invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DecodeScriptRequest** | [**DecodeScriptRequest**](../Models/DecodeScriptRequest.md)|  | |

### Return type

[**DecodeScriptResponse**](../Models/DecodeScriptResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="estimatePriorityEstimatepriorityGet"></a>
# **estimatePriorityEstimatepriorityGet**
> BigDecimal estimatePriorityEstimatepriorityGet(nblocks)

Estimate the transaction priority for zero-fee confirmation

    Estimate the approximate priority a zero-fee transaction needs to begin confirmation within a specified number of blocks.  ### Description - This endpoint estimates the priority that a zero-fee transaction needs to start confirming within a certain number of blocks. - It&#39;s useful for determining the priority required for a transaction to be included in a block without incurring fees.  ### Input Parameters - &#x60;nblocks&#x60;: The number of blocks within which the transaction should begin confirmation.  ### Example Request - &#x60;GET /estimatepriority?nblocks&#x3D;6&#x60;  ### Response - Returns a numeric value representing the estimated priority.  ### Example Response &#x60;&#x60;&#x60;json 3.4567 &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;nblocks&#x60; parameter is not a valid number. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Returns &#x60;-1.0&#x60; if not enough transactions and blocks have been observed to make an estimate.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **nblocks** | **Integer**|  | [default to null] |

### Return type

**BigDecimal**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="generatePastelIdNewkeyPastelidNewkeyPost"></a>
# **generatePastelIdNewkeyPastelidNewkeyPost**
> PastelIDNewKeyResponse generatePastelIdNewkeyPastelidNewkeyPost(PastelIDNewKeyRequest)

Generate new Pastel ID and keys

    Generate a new Pastel ID and associated keys (EdDSA448 and LegRoast signing keys).  ### Description - This endpoint generates a new Pastel ID and associated keys using the specified passphrase for encryption.  ### Input Parameters - &#x60;passphrase&#x60;: A string passphrase used to encrypt the key file.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;your_secure_passphrase\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the Pastel ID and public key in base58-encoded format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;pastel_id\&quot;: \&quot;paxxxxxxxxxxxxxxxxxxxxxx\&quot;,     \&quot;public_key\&quot;: \&quot;pubxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDNewKeyRequest** | [**PastelIDNewKeyRequest**](../Models/PastelIDNewKeyRequest.md)|  | |

### Return type

[**PastelIDNewKeyResponse**](../Models/PastelIDNewKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="generateReportGenerateReportReportNameGet"></a>
# **generateReportGenerateReportReportNameGet**
> GenerateReportResponse generateReportGenerateReportReportNameGet(report\_name)

Generate various reports

    Generate various reports from the Pastel Network.   ### Description - This endpoint generates different types of reports based on the Pastel Network&#39;s blockchain data.  ### Input Parameters - &#x60;report_name&#x60;: The name of the report to generate. Currently supported: &#39;fees-and-burn&#39;.  ### Example Request - &#x60;GET /generate-report/fees-and-burn&#x60;  ### Response - Returns a JSON object containing the generated report data.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;report_data\&quot;: {         // Example report data here     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the report name is not supported. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for analysis and insight into various aspects of the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **report\_name** | **String**|  | [default to null] |

### Return type

[**GenerateReportResponse**](../Models/GenerateReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getActionFeesStoragefeeGetactionfeesGet"></a>
# **getActionFeesStoragefeeGetactionfeesGet**
> GetActionFeesResponse getActionFeesStoragefeeGetactionfeesGet(data\_size, height)

Get action fees based on data size

    Get action fees based on data size.  ### Description - This endpoint calculates the action fees based on the given data size in MB.  ### Input Parameters - &#x60;data_size&#x60;: (Required) Data size in MB. - &#x60;height&#x60;: (Optional) Block height to get action fees for.  ### Example Request - &#x60;GET /storagefee/getactionfees?data_size&#x3D;10&amp;height&#x3D;12345&#x60;  ### Response - Returns a JSON object containing action fees for different actions based on the data size.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;datasize\&quot;: 10,     \&quot;height\&quot;: 12345,     \&quot;fee_deflator_factor\&quot;: 1.5,     \&quot;action_fees\&quot;: {         \&quot;actionTypeFee\&quot;: 200,         \&quot;actionTypeFeePat\&quot;: 200000,         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **data\_size** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **height** | [**Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**GetActionFeesResponse**](../Models/GetActionFeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAddressMempoolGetaddressmempoolGet"></a>
# **getAddressMempoolGetaddressmempoolGet**
> GetAddressMempoolResponse getAddressMempoolGetaddressmempoolGet(request\_body)

Get all mempool deltas for an address

    Retrieve all mempool deltas for a specified address.  ### Description - This endpoint returns all mempool deltas (transaction differences) for a given address. - It&#39;s useful for tracking the unconfirmed transactions involving a specific address.  ### Input Parameters - &#x60;addresses&#x60;: A list of base58check encoded addresses.  ### Example Request - &#x60;GET /getaddressmempool?addresses&#x3D;[\&quot;tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing a mempool delta for the given address(es).  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;address\&quot;: \&quot;tPp3pfmLi57S8qoccfWnn2o4tXyoQ23wVSp\&quot;,         \&quot;txid\&quot;: \&quot;txid123\&quot;,         \&quot;index\&quot;: 1,         \&quot;patoshis\&quot;: 5000000,         \&quot;timestamp\&quot;: 1617184000,         \&quot;prevtxid\&quot;: \&quot;txid456\&quot;,         \&quot;prevout\&quot;: 0     } ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **request\_body** | [**List**](../Models/string.md)|  | |

### Return type

[**GetAddressMempoolResponse**](../Models/GetAddressMempoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getFeeScheduleGetfeescheduleGet"></a>
# **getFeeScheduleGetfeescheduleGet**
> GetFeeScheduleResponse getFeeScheduleGetfeescheduleGet()

Get the current fee schedule

    Get the current fee schedule including the chain deflation rate and related fees.  ### Description - This endpoint returns the current fee schedule of the network, which includes various fees associated with operations like PastelID registration, username registration, and username change. - It also provides the fee deflator factor, which is used to adjust fees based on the chain deflation rate.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getfeeschedule&#x60;  ### Response - Returns a JSON object containing the current fee schedule.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;fee_deflator_factor\&quot;: 1.5,     \&quot;pastelid_registration_fee\&quot;: 100.0,     \&quot;username_registration_fee\&quot;: 50.0,     \&quot;username_change_fee\&quot;: 20.0 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This information is crucial for users and applications that interact with the network, especially for those involving registrations and updates.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFeeScheduleResponse**](../Models/GetFeeScheduleResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMemoryInfoGetmemoryinfoGet"></a>
# **getMemoryInfoGetmemoryinfoGet**
> GetMemoryInfoResponse getMemoryInfoGetmemoryinfoGet()

Get memory usage information

    Get detailed information about memory usage by the Pastel node.   ### Description - This endpoint returns information about the memory usage, including details about used and free memory, total memory managed, amount of memory locked, and the number of chunks used and free.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmemoryinfo&#x60;  ### Response - Returns a JSON object containing detailed memory usage information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;locked\&quot;: {         \&quot;used\&quot;: 123456,         \&quot;free\&quot;: 654321,         \&quot;total\&quot;: 1000000,         \&quot;locked\&quot;: 500000,         \&quot;chunks_used\&quot;: 20,         \&quot;chunks_free\&quot;: 80     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for monitoring the memory performance and health of the Pastel node.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMemoryInfoResponse**](../Models/GetMemoryInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMempoolInfoGetmempoolinfoGet"></a>
# **getMempoolInfoGetmempoolinfoGet**
> GetMempoolInfoResponse getMempoolInfoGetmempoolinfoGet()

Get active state of the TX memory pool

    Returns details on the active state of the TX memory pool.  ### Description - This endpoint provides information about the current state of the transaction memory pool.  - It includes details such as the total number of transactions in the pool, the sum of all transaction sizes, and the total memory usage of the mempool.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getmempoolinfo&#x60;  ### Response - Returns a JSON object containing details about the transaction memory pool.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;size\&quot;: 45,     \&quot;bytes\&quot;: 123456,     \&quot;usage\&quot;: 98765 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for understanding the load and capacity of the transaction memory pool.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMempoolInfoResponse**](../Models/GetMempoolInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNewAddressGetnewaddressGet"></a>
# **getNewAddressGetnewaddressGet**
> GetNewAddressResponse getNewAddressGetnewaddressGet(account)

Generate a new Pastel address

    Generate a new Pastel address for receiving payments.  ### Description - This endpoint creates a new Pastel address which can be used to receive payments. - The new address is automatically associated with the default account.  ### Input Parameters - &#x60;account&#x60;: (string, optional) DEPRECATED. The account name for the address. It must be the empty string &#x60;\&quot;\&quot;&#x60; for the default account. Any other value will result in an error.  ### Example Request - &#x60;GET /getnewaddress?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON object containing the new Pastel address in string format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;pZb7J2fg9BpM1Kj3n3FjR5Bn25S55hKx2x\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The generated address is added to the wallet and can be used immediately for receiving funds.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**Account**](../Models/.md)|  | [optional] [default to ] |

### Return type

[**GetNewAddressResponse**](../Models/GetNewAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStorageFeeGetFeeStoragefeeGetfeeGet"></a>
# **getStorageFeeGetFeeStoragefeeGetfeeGet**
> StorageFeeGetFeeResponse getStorageFeeGetFeeStoragefeeGetfeeGet(fee\_type, is\_local, height)

Get the storage fee

    Get the current storage fee based on the specified fee type and blockchain height.  ### Description - This endpoint returns the current storage fee based on the given fee type, optional local/global flag, and blockchain height.  ### Input Parameters - &#x60;fee_type&#x60;: The type of fee to retrieve (e.g., \&quot;nftTicketFee\&quot;). - &#x60;is_local&#x60;: (Optional) A boolean to specify if the fee is local or global. Defaults to &#x60;False&#x60;. - &#x60;height&#x60;: (Optional) The blockchain height for which to retrieve the fee. If not provided, the current height is used.  ### Example Request - &#x60;GET /storagefee/getfee?fee_type&#x3D;nftTicketFee&amp;is_local&#x3D;true&amp;height&#x3D;100000&#x60;  ### Response - Returns a JSON object containing the storage fee, fee in &#39;pat&#39; units, blockchain height, and chain deflator factor.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;fee\&quot;: 0.002,     \&quot;fee_pat\&quot;: 200000,     \&quot;height\&quot;: 100000,     \&quot;chain_deflator_factor\&quot;: 1.5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used to determine the current storage fee for various operations on the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fee\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **is\_local** | [**Is_Local**](../Models/.md)|  | [optional] [default to false] |
| **height** | [**Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**StorageFeeGetFeeResponse**](../Models/StorageFeeGetFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStorageFeesStoragefeeGetfeesGet"></a>
# **getStorageFeesStoragefeeGetfeesGet**
> GetFeesResponse getStorageFeesStoragefeeGetfeesGet()

Get the current storage fees

    Get the current storage fees adjusted by the network median and local factors.  ### Description - This endpoint returns the current storage fees based on the network&#39;s median fee and local fee for various actions. - The fees are adjusted by a fee deflator factor, which is based on the blockchain&#39;s state.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /storagefee/getfees&#x60;  ### Response - Returns a JSON object containing storage fees for different actions.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;height\&quot;: 12345,     \&quot;chain_deflator_factor\&quot;: 1.5,     \&quot;fees\&quot;: {         \&quot;actionName\&quot;: {             \&quot;fee\&quot;: 100,             \&quot;fee_pat\&quot;: 100000         },         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFeesResponse**](../Models/GetFeesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getWalletInfoGetwalletinfoGet"></a>
# **getWalletInfoGetwalletinfoGet**
> WalletInfoResponse getWalletInfoGetwalletinfoGet()

Get wallet state information

    Returns an object containing various wallet state info.  ### Description - This endpoint provides information about the wallet, including balances, transaction count, key pool size, and other relevant data.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getwalletinfo&#x60;  ### Response - Returns a JSON object containing detailed information about the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;walletversion\&quot;: 169900,     \&quot;balance\&quot;: 0.015,     \&quot;unconfirmed_balance\&quot;: 0.0,     \&quot;immature_balance\&quot;: 0.0,     \&quot;txcount\&quot;: 2,     \&quot;keypoololdest\&quot;: 1600000000,     \&quot;keypoolsize\&quot;: 1000,     \&quot;unlocked_until\&quot;: null,     \&quot;paytxfee\&quot;: 0.00001,     \&quot;seedfp\&quot;: \&quot;d1f1a9fc\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**WalletInfoResponse**](../Models/WalletInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="governanceActionGovernancePost"></a>
# **governanceActionGovernancePost**
> Response_Governance_Action_Governance_Post governanceActionGovernancePost(mode, subcommand, body)

Cast a vote or list governance tickets

    Perform governance-related actions such as voting for tickets or listing tickets/winners.  ### Description - This endpoint allows casting votes for governance tickets or listing all governance tickets or winners.  ### Input Parameters - &#x60;mode&#x60;: &#39;ticket&#39; or &#39;list&#39; to specify the action. - &#x60;subcommand&#x60;: Depending on the mode, additional parameters for the action.  ### Example Request - &#x60;POST /governance&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;mode\&quot;: \&quot;ticket\&quot;,       \&quot;subcommand\&quot;: \&quot;add\&quot;,       \&quot;parameters\&quot;: [\&quot;address\&quot;, 10, \&quot;note\&quot;, \&quot;yes\&quot;]   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the governance action.  ### Example Response   &#x60;&#x60;&#x60;json   {       \&quot;result\&quot;: \&quot;success\&quot;,       \&quot;ticketId\&quot;: \&quot;ticket_id_here\&quot;   }   &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for participating in the governance of the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **mode** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **subcommand** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **body** | **oas_any_type_not_mapped**|  | |

### Return type

[**Response_Governance_Action_Governance_Post**](../Models/Response_Governance_Action_Governance_Post.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidNewkeyPastelidNewkeyPost"></a>
# **pastelidNewkeyPastelidNewkeyPost**
> PastelIDNewKeyResponse pastelidNewkeyPastelidNewkeyPost(PastelIDNewKeyRequest)

Generate new Pastel ID and associated keys

    Generate a new Pastel ID and associated keys (EdDSA448) and LegRoast signing keys.  ### Description - This endpoint generates a new Pastel ID, which is a unique identifier for a user or entity on the Pastel network. - The endpoint also generates associated cryptographic keys using EdDSA448 and LegRoast algorithms. - The generated Pastel ID is base58-encoded.  ### Input Parameters - &#x60;passphrase&#x60;: A passphrase used for generating the new key. It cannot be empty.  ### Example Request - &#x60;POST /pastelid_newkey&#x60; with JSON body &#x60;{\&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;}&#x60;  ### Response - Returns a JSON object containing the newly generated Pastel ID and LegRoast key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;base58EncodedPastelID\&quot;,     \&quot;legroast\&quot;: \&quot;base58EncodedLegRoastKey\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the passphrase is empty or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This function is essential for user registration and identity management within the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDNewKeyRequest** | [**PastelIDNewKeyRequest**](../Models/PastelIDNewKeyRequest.md)|  | |

### Return type

[**PastelIDNewKeyResponse**](../Models/PastelIDNewKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidPasswdPastelidPasswdPost"></a>
# **pastelidPasswdPastelidPasswdPost**
> PastelIDPasswdResponse pastelidPasswdPastelidPasswdPost(PastelIDPasswdRequest)

Change passphrase for PastelID secure container

    Change the passphrase used to encrypt the secure container associated with the PastelID.  ### Description - This endpoint is used to update the passphrase of the secure container for a given PastelID. - The secure container is encrypted, and this operation changes its encryption passphrase.  ### Input Parameters - &#x60;pastelid&#x60;: The PastelID for which the passphrase needs to be changed. - &#x60;old_passphrase&#x60;: The current passphrase of the secure container. - &#x60;new_passphrase&#x60;: The new passphrase to set for the secure container.  ### Example Request &#x60;&#x60;&#x60;json POST /pastelid/passwd {     \&quot;pastelid\&quot;: \&quot;jX9NfXhvnUJwDzB2z0wh\&quot;,     \&quot;old_passphrase\&quot;: \&quot;currentpass\&quot;,     \&quot;new_passphrase\&quot;: \&quot;newpass\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or missing. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDPasswdRequest** | [**PastelIDPasswdRequest**](../Models/PastelIDPasswdRequest.md)|  | |

### Return type

[**PastelIDPasswdResponse**](../Models/PastelIDPasswdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidSignFilePastelidSignfilePost"></a>
# **pastelidSignFilePastelidSignfilePost**
> PastelIDSignFileResponse pastelidSignFilePastelidSignfilePost(PastelIDSignFileRequest)

Sign a file with a Pastel ID

    Sign a file with the internally stored private key associated with a Pastel ID.  ### Description - This endpoint allows users to sign a file using their Pastel ID. The file is specified by its path, and the signature is generated using the private key associated with the given Pastel ID. - Supported algorithms are &#39;ed448&#39; (default) and &#39;legroast&#39;.  ### Input Parameters - &#x60;file_path&#x60;: Path to the file that needs to be signed. - &#x60;pastel_id&#x60;: The Pastel ID to use for signing. - &#x60;passphrase&#x60;: The passphrase for the private key. - &#x60;algorithm&#x60;: (Optional) The algorithm to use for signing, either &#39;ed448&#39; or &#39;legroast&#39;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;file_path\&quot;: \&quot;/path/to/file\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYWV...\&quot;,     \&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the signature of the file.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;HJG98uFomw...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The private key must be stored internally and associated with the specified Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDSignFileRequest** | [**PastelIDSignFileRequest**](../Models/PastelIDSignFileRequest.md)|  | |

### Return type

[**PastelIDSignFileResponse**](../Models/PastelIDSignFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pastelidVerifyFilePastelidVerifyFilePost"></a>
# **pastelidVerifyFilePastelidVerifyFilePost**
> PastelIDVerifyFileResponse pastelidVerifyFilePastelidVerifyFilePost(file\_path, signature, pastelid, algorithm)

Verify a file&#39;s signature with a Pastel ID

    Verify a file&#39;s signature with the private key associated with a Pastel ID.  ### Description - This endpoint verifies the signature of a file using a Pastel ID. It supports two algorithms: ed448 or legroast.  ### Input Parameters - &#x60;file_path&#x60;: Path to the file whose signature needs to be verified. - &#x60;signature&#x60;: The signature string to verify. - &#x60;pastelid&#x60;: The Pastel ID associated with the private key. - &#x60;algorithm&#x60;: (Optional) The algorithm used for signing (ed448 or legroast). Default is ed448.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;file_path\&quot;: \&quot;/path/to/file\&quot;,     \&quot;signature\&quot;: \&quot;signature_string\&quot;,     \&quot;pastelid\&quot;: \&quot;pastel_id_string\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the verification was successful or failed.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verification\&quot;: \&quot;OK\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are missing or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for validating the authenticity of a file using a Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **file\_path** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **signature** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **algorithm** | [**Algorithm**](../Models/.md)|  | [optional] [default to ed448] |

### Return type

[**PastelIDVerifyFileResponse**](../Models/PastelIDVerifyFileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="pastelidVerifyPastelidVerifyPost"></a>
# **pastelidVerifyPastelidVerifyPost**
> PastelIDVerifyResponse pastelidVerifyPastelidVerifyPost(PastelIDVerifyRequest)

Verify a signature with PastelID

    Verify a text&#39;s signature using the private key associated with the PastelID.  ### Description - This endpoint verifies the signature of a given text using the private key associated with a specified PastelID. - It supports two algorithms: &#x60;ed448&#x60; and &#x60;legroast&#x60;.  ### Input Parameters - &#x60;text&#x60;: The text (or base64-encoded text) to be verified. - &#x60;signature&#x60;: The signature of the text. - &#x60;pastelid&#x60;: The PastelID used for verification. - &#x60;algorithm&#x60;: (Optional) The algorithm used for signing (&#x60;ed448&#x60; or &#x60;legroast&#x60;). Default is &#x60;ed448&#x60;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;text\&quot;: \&quot;Hello World\&quot;,     \&quot;signature\&quot;: \&quot;signature123\&quot;,     \&quot;pastelid\&quot;: \&quot;pastelid123\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the verification was successful or not.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;verification\&quot;: \&quot;OK\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Verification failure does not always imply the data or signature is incorrect; it might also indicate an issue with the algorithm used.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDVerifyRequest** | [**PastelIDVerifyRequest**](../Models/PastelIDVerifyRequest.md)|  | |

### Return type

[**PastelIDVerifyResponse**](../Models/PastelIDVerifyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="pingPingGet"></a>
# **pingPingGet**
> PingResponse pingPingGet()

Send a ping to all nodes

    Request a ping to be sent to all other nodes, measuring ping time.  ### Description - This endpoint triggers a ping to all nodes in the network. It&#39;s used to measure the ping time and network responsiveness. - The ping time and wait time results are available in the &#x60;getpeerinfo&#x60; response, under &#x60;pingtime&#x60; and &#x60;pingwait&#x60; fields, represented in decimal seconds. - The ping command is queued with other commands, so it measures the total processing backlog, not just the network latency.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /ping&#x60;  ### Response - Returns a JSON object indicating whether the ping request was successfully queued.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and monitoring the responsiveness of the network.

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](../Models/PingResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="resendWalletTransactionsResendwallettransactionsPost"></a>
# **resendWalletTransactionsResendwallettransactionsPost**
> ResendWalletTransactionsResponse resendWalletTransactionsResendwallettransactionsPost()

Re-broadcast unconfirmed wallet transactions

    Immediately re-broadcast unconfirmed wallet transactions to all peers.  ### Description - This endpoint is intended primarily for testing. It forces the immediate re-broadcast of unconfirmed transactions from the wallet to all peers. - The wallet code periodically re-broadcasts transactions automatically, so this method is typically unnecessary in production environments.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;POST /resendwallettransactions&#x60;  ### Response - Returns a JSON object containing an array of transaction IDs that were re-broadcast.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_ids\&quot;: [\&quot;txid1\&quot;, \&quot;txid2\&quot;, \&quot;txid3\&quot;] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method with caution, as it is primarily for testing purposes and may affect network performance if used excessively.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResendWalletTransactionsResponse**](../Models/ResendWalletTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="retrieveChaindataChaindataRetrievePost"></a>
# **retrieveChaindataChaindataRetrievePost**
> ChaindataRetrieveResponse retrieveChaindataChaindataRetrievePost(ChaindataRetrieveRequest)

Retrieve data from the blockchain

    Retrieve data from the blockchain by transaction ID (&#x60;txid&#x60;).  ### Description - This endpoint retrieves data from the blockchain that was stored using the &#39;store&#39; command and associated with the provided &#x60;txid&#x60;.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the data to be retrieved.  ### Example Request - &#x60;POST /chaindata/retrieve&#x60; with JSON payload &#x60;{\&quot;txid\&quot;: \&quot;example-txid\&quot;}&#x60;  ### Response - Returns a JSON object containing the retrieved data.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;data\&quot;: \&quot;retrieved data\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;txid&#x60; is not provided or is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ChaindataRetrieveRequest** | [**ChaindataRetrieveRequest**](../Models/ChaindataRetrieveRequest.md)|  | |

### Return type

[**ChaindataRetrieveResponse**](../Models/ChaindataRetrieveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="scanForMissingTxsScanformissingtxsPost"></a>
# **scanForMissingTxsScanformissingtxsPost**
> ScanForMissingTxsResponse scanForMissingTxsScanformissingtxsPost(ScanForMissingTxsRequest)

Scan for missing transactions

    Scan the wallet for missing transactions starting from a specified block height.  ### Description - This endpoint scans the wallet for transactions that might be missing, starting from a given block height. It helps in ensuring the wallet&#39;s transaction history is complete and up-to-date.  ### Input Parameters - &#x60;starting_height&#x60;: (numeric, required) The block height from which to start scanning for missing transactions.  ### Example Request - &#x60;POST /scanformissingtxs&#x60; with payload &#x60;{\&quot;starting_height\&quot;: 100000}&#x60;  ### Response - Returns a JSON object containing a list of transaction IDs for transactions that are missing in the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;missing_txs\&quot;: [         \&quot;missing_transaction1_txid\&quot;,         \&quot;missing_transaction2_txid\&quot;         // ... more transaction IDs ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the &#x60;starting_height&#x60; is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for wallet recovery and maintenance purposes.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ScanForMissingTxsRequest** | [**ScanForMissingTxsRequest**](../Models/ScanForMissingTxsRequest.md)|  | |

### Return type

[**ScanForMissingTxsResponse**](../Models/ScanForMissingTxsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="sendToAddressSendtoaddressPost"></a>
# **sendToAddressSendtoaddressPost**
> SendToAddressResponse sendToAddressSendtoaddressPost(SendToAddressRequest)

Send an amount to a given address

    Send an amount to a given address. The amount is a real and is rounded to the nearest 0.00000001.  ### Description - Send Pastel to a specified address with optional comments and fee deduction options. - By default, the change is sent to the original address unless specified otherwise.  ### Input Parameters - &#x60;t_address&#x60; (string, required): The Pastel address to send to. - &#x60;amount&#x60; (numeric, required): The amount in Pastel to send. e.g., 0.1 - &#x60;comment&#x60; (string, optional): A comment for transaction record-keeping, not part of the transaction. - &#x60;comment_to&#x60; (string, optional): A comment about the recipient, for record-keeping. - &#x60;subtract_fee_from_amount&#x60; (boolean, optional, default&#x3D;false): If true, the fee is deducted from the amount being sent. - &#x60;change_address&#x60; (string, optional, default&#x3D;\&quot;original\&quot;): Address for sending the change. Can be \&quot;original\&quot;, \&quot;new\&quot;, or a specific Pastel t-address.  ### Example Request - &#x60;POST /sendtoaddress&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;amount\&quot;: 0.1,     \&quot;comment\&quot;: \&quot;donation\&quot;,     \&quot;comment_to\&quot;: \&quot;seans outpost\&quot;,     \&quot;subtract_fee_from_amount\&quot;: true,     \&quot;change_address\&quot;: \&quot;new\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns the transaction ID of the completed transaction.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transaction_id\&quot;: \&quot;b6a19f8fb228edf47e93a2b3d3ad8b1b4f7d8eac4fc0f3c6d3e2c463d7b9fc6f\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SendToAddressRequest** | [**SendToAddressRequest**](../Models/SendToAddressRequest.md)|  | |

### Return type

[**SendToAddressResponse**](../Models/SendToAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setTxFeeSettxfeePost"></a>
# **setTxFeeSettxfeePost**
> SetTxFeeResponse setTxFeeSettxfeePost(SetTxFeeRequest)

Set the transaction fee per kB

    Set the transaction fee per kilobyte for transactions.  ### Description - This endpoint allows setting the transaction fee per kilobyte that will be used for future transactions.  ### Input Parameters - &#x60;amount&#x60;: (numeric, required) The transaction fee in [currency]/kB rounded to the nearest 0.00000001.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;amount\&quot;: 0.00001 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating whether the transaction fee was successfully set.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetTxFeeRequest** | [**SetTxFeeRequest**](../Models/SetTxFeeRequest.md)|  | |

### Return type

[**SetTxFeeResponse**](../Models/SetTxFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signMessageSignmessagePost"></a>
# **signMessageSignmessagePost**
> SignMessageResponse signMessageSignmessagePost(SignMessageRequest)

Sign a message with the private key of a t-addr

    Sign a message using the private key of a transparent address (t-addr).  ### Description - This endpoint allows you to sign a message with the private key of a specified transparent address.  - It&#39;s commonly used for proving ownership of a specific address.  ### Input Parameters - &#x60;t_addr&#x60;: (string, required) The transparent address to use for the private key. - &#x60;message&#x60;: (string, required) The message to create a signature of.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_addr\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;message\&quot;: \&quot;my message\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the base 64 encoded signature of the message.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;H6sliPZjFfS36emU8XThY6UvZHxY...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or the address is not correct. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The address must be a valid t-addr and the wallet must be unlocked for this operation.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SignMessageRequest** | [**SignMessageRequest**](../Models/SignMessageRequest.md)|  | |

### Return type

[**SignMessageResponse**](../Models/SignMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="signWithPastelIdPastelidSignPost"></a>
# **signWithPastelIdPastelidSignPost**
> PastelIDSignResponse signWithPastelIdPastelidSignPost(PastelIDSignRequest)

Sign a text with Pastel ID

    Sign a text using the private key associated with a Pastel ID.  ### Description - Signs a provided text using the private key corresponding to the specified Pastel ID.  ### Input Parameters - &#x60;text&#x60;: The text to be signed. - &#x60;pastel_id&#x60;: The Pastel ID used for signing. - &#x60;passphrase&#x60;: The passphrase for the private key. - &#x60;algorithm&#x60;: (Optional) The signing algorithm, either &#39;ed448&#39; (default) or &#39;legroast&#39;.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;text\&quot;: \&quot;Example text\&quot;,     \&quot;pastel_id\&quot;: \&quot;pastel_id_example\&quot;,     \&quot;passphrase\&quot;: \&quot;secure_passphrase\&quot;,     \&quot;algorithm\&quot;: \&quot;ed448\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the signature of the text.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;signature\&quot;: \&quot;generated_signature\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PastelIDSignRequest** | [**PastelIDSignRequest**](../Models/PastelIDSignRequest.md)|  | |

### Return type

[**PastelIDSignResponse**](../Models/PastelIDSignResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storeChaindataChaindataStorePost"></a>
# **storeChaindataChaindataStorePost**
> ChaindataStoreResponse storeChaindataChaindataStorePost(ChaindataStoreRequest)

Store data in the blockchain

    Store data in the blockchain. If successful, returns the transaction ID and raw transaction data.  ### Description - This endpoint stores provided data into the blockchain using a P2FMS transaction. - The maximum size of the data is 4KB.  ### Input Parameters - &#x60;data&#x60;: The data to be stored in the blockchain.  ### Example Request - &#x60;POST /chaindata/store&#x60; with JSON payload &#x60;{\&quot;data\&quot;: \&quot;&lt;your-data&gt;\&quot;}&#x60;  ### Response - Returns a JSON object containing the transaction ID (&#x60;txid&#x60;) and the raw transaction data (&#x60;rawtx&#x60;).  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;example-txid\&quot;,     \&quot;rawtx\&quot;: \&quot;example-rawtx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the data is not provided, is empty, or exceeds 4KB. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The data stored can later be retrieved using the &#39;retrieve&#39; command with the returned &#x60;txid&#x60;.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ChaindataStoreRequest** | [**ChaindataStoreRequest**](../Models/ChaindataStoreRequest.md)|  | |

### Return type

[**ChaindataStoreResponse**](../Models/ChaindataStoreResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="validateAddressValidateaddressPost"></a>
# **validateAddressValidateaddressPost**
> ValidateAddressResponse validateAddressValidateaddressPost(ValidateAddressRequest)

Validate a Pastel address

    Validate a given Pastel transparent address.  ### Description - This endpoint validates a specified Pastel transparent address and returns detailed information about it.  ### Input Parameters - &#x60;t_address&#x60;: The Pastel transparent address to validate.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing various details about the address if it is valid. If the address is not valid, only the &#x60;isvalid&#x60; field is returned.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;isvalid\&quot;: true,     \&quot;address\&quot;: \&quot;1PSSGeFHDnKNxiEyFrD1wcEaHr9hrQDDWc\&quot;,     \&quot;scriptPubKey\&quot;: \&quot;76a914...\&quot;,     \&quot;ismine\&quot;: true,     \&quot;iswatchonly\&quot;: false,     \&quot;isscript\&quot;: false,     \&quot;pubkey\&quot;: \&quot;02...\&quot;,     \&quot;iscompressed\&quot;: true,     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Provides detailed information about a Pastel address, including ownership and script information.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ValidateAddressRequest** | [**ValidateAddressRequest**](../Models/ValidateAddressRequest.md)|  | |

### Return type

[**ValidateAddressResponse**](../Models/ValidateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="verifyMessageVerifymessagePost"></a>
# **verifyMessageVerifymessagePost**
> VerifyMessageResponse verifyMessageVerifymessagePost(VerifyMessageRequest)

Verify a signed message

    Verify a signed message using a Pastel transparent address, a signature, and the message itself.  ### Description - Verifies a message signature against a given Pastel transparent address.  ### Input Parameters - &#x60;t_address&#x60;: The Pastel transparent address used for the signature. - &#x60;signature&#x60;: The signature provided by the signer in base 64 encoding. - &#x60;message&#x60;: The message that was signed.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;t_address\&quot;: \&quot;Ptor9ydHJuGpNWFAX3ZTu3bXevEhCaDVrsY\&quot;,     \&quot;signature\&quot;: \&quot;signature_in_base64\&quot;,     \&quot;message\&quot;: \&quot;my message\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a boolean indicating if the signature is verified.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;is_verified\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the inputs are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for validating the authenticity of messages signed with a Pastel address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **VerifyMessageRequest** | [**VerifyMessageRequest**](../Models/VerifyMessageRequest.md)|  | |

### Return type

[**VerifyMessageResponse**](../Models/VerifyMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zGetNotesCountZGetnotescountGet"></a>
# **zGetNotesCountZGetnotescountGet**
> ZGetNotesCountResponse zGetNotesCountZGetnotescountGet(minconf)

Get the count of sapling notes in the wallet

    Get the count of sapling notes in the wallet.  ### Description - This endpoint returns the number of sapling notes available in the wallet. - It includes notes in transactions confirmed at least a specified number of times.  ### Input Parameters - &#x60;minconf&#x60;: (Optional, numeric) Only include notes in transactions confirmed at least this many times. Default is 1.  ### Example Request - &#x60;GET /z_getnotescount?minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing the count of sapling notes in the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;sapling\&quot;: 5 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for assessing the number of sapling notes held in the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |

### Return type

[**ZGetNotesCountResponse**](../Models/ZGetNotesCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetOperationStatusZGetoperationstatusGet"></a>
# **zGetOperationStatusZGetoperationstatusGet**
> GetOperationStatusResponse zGetOperationStatusZGetoperationstatusGet(Operation\_Ids\_1)

Get the status of asynchronous operations

    Get the status and any associated results or errors for asynchronous operations.  ### Description - This endpoint returns the status and any results or error data for asynchronous operations, such as those initiated by the &#x60;z_sendmany&#x60; or &#x60;z_shieldcoinbase&#x60; methods. - Operations will remain in memory even after completion.  ### Input Parameters - &#x60;operation_ids&#x60;: (Optional) A list of operation IDs to query. If not provided, information about all operations known to the node is returned.  ### Example Request - &#x60;GET /z_getoperationstatus?operation_ids&#x3D;[\&quot;opid-1a2b3c\&quot;, \&quot;opid-4d5e6f\&quot;]&#x60;  ### Response - Returns a JSON array of objects, each representing the status of an operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;operations\&quot;: [         {             \&quot;id\&quot;: \&quot;opid-1a2b3c\&quot;,             \&quot;status\&quot;: \&quot;success\&quot;,             \&quot;creation_time\&quot;: 1617754083,             \&quot;method\&quot;: \&quot;z_sendmany\&quot;,             \&quot;params\&quot;: { ... },             \&quot;result\&quot;: { ... },             \&quot;error\&quot;: null,             \&quot;execution_secs\&quot;: 2.345,             \&quot;method_finished\&quot;: true         },         {             \&quot;id\&quot;: \&quot;opid-4d5e6f\&quot;,             \&quot;status\&quot;: \&quot;executing\&quot;,             \&quot;creation_time\&quot;: 1617754090,             \&quot;method\&quot;: \&quot;z_shieldcoinbase\&quot;,             \&quot;params\&quot;: { ... },             \&quot;result\&quot;: null,             \&quot;error\&quot;: null,             \&quot;execution_secs\&quot;: null,             \&quot;method_finished\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the provided operation IDs are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for tracking the progress and outcome of operations that do not provide immediate results.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **Operation\_Ids\_1** | [**Operation_Ids_1**](../Models/Operation_Ids_1.md)|  | [optional] |

### Return type

[**GetOperationStatusResponse**](../Models/GetOperationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zListReceivedByAddressZListreceivedbyaddressGet"></a>
# **zListReceivedByAddressZListreceivedbyaddressGet**
> ZListReceivedByAddressResponse zListReceivedByAddressZListreceivedbyaddressGet(ZListReceivedByAddressRequest)

List amounts received by a z-address

    List amounts received by a z-address belonging to the node&#39;s wallet.  ### Description - This endpoint returns a list of amounts received by a specified z-address.  - It includes various details about each received note, such as the transaction ID, amount, confirmations, and more.  ### Input Parameters - &#x60;address&#x60; (string): The z-address to query. - &#x60;minconf&#x60; (numeric, optional, default&#x3D;1): Minimum number of confirmations for a transaction to be included.  ### Example Request - &#x60;GET /z_listreceivedbyaddress?address&#x3D;&lt;z-address&gt;&amp;minconf&#x3D;1&#x60;  ### Response - Returns a JSON object containing a list of received notes, each with detailed information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;notes\&quot;: [         {             \&quot;txid\&quot;: \&quot;example-txid\&quot;,             \&quot;amount\&quot;: 1.23,             \&quot;amountPat\&quot;: 123,             \&quot;memo\&quot;: \&quot;hex-string\&quot;,             \&quot;confirmations\&quot;: 10,             \&quot;blockheight\&quot;: 100000,             \&quot;blockindex\&quot;: 1,             \&quot;blocktime\&quot;: 1609459200,             \&quot;change\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZListReceivedByAddressRequest** | [**ZListReceivedByAddressRequest**](../Models/ZListReceivedByAddressRequest.md)|  | |

### Return type

[**ZListReceivedByAddressResponse**](../Models/ZListReceivedByAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zValidateAddressZValidateaddressGet"></a>
# **zValidateAddressZValidateaddressGet**
> ZValidateAddressResponse zValidateAddressZValidateaddressGet(ZAddressQuery)

Validate a Z address

    Validate the given Z address and return information about it.  ### Description - This endpoint validates a Z address and returns various details about it, including its validity, type, and ownership.  ### Input Parameters - &#x60;zaddr&#x60;: The Z address to validate.  ### Example Request - &#x60;GET /z_validateaddress?zaddr&#x3D;PzWcy67ygestjagHaFZxjWxmawMeShmQWNPE8FNJp23pQS2twecwps5223ajUtN7iihxR4MmLDFQ19heHkBx5AKaDooS6aQ&#x60;  ### Response - Returns a JSON object with information about the Z address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;isvalid\&quot;: true,     \&quot;address\&quot;: \&quot;PzWcy67y...\&quot;,     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;ismine\&quot;: false,     ... } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address format is incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to verify the details and ownership of a Z address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZAddressQuery** | [**ZAddressQuery**](../Models/ZAddressQuery.md)|  | |

### Return type

[**ZValidateAddressResponse**](../Models/ZValidateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zcBenchmarkZcbenchmarkPost"></a>
# **zcBenchmarkZcbenchmarkPost**
> ZCBenchmarkResponse zcBenchmarkZcbenchmarkPost(ZCBenchmarkRequest)

Runs a benchmark of the selected type

    Runs a benchmark of the selected type &#x60;samplecount&#x60; times, returning the running times of each sample.  ### Description - This endpoint runs a specified benchmark multiple times and returns the running time for each iteration.  - It&#39;s useful for performance testing various operations on the Pastel blockchain.  ### Input Parameters - &#x60;benchmarktype&#x60;: The type of benchmark to run. - &#x60;samplecount&#x60;: The number of times to run the benchmark. - &#x60;extra_param&#x60;: Optional additional parameter, depending on the benchmark type.  ### Example Request &#x60;&#x60;&#x60;json {   \&quot;benchmarktype\&quot;: \&quot;solveequihash\&quot;,   \&quot;samplecount\&quot;: 5,   \&quot;extra_param\&quot;: 2 } &#x60;&#x60;&#x60;  ### Response - Returns a list of objects, each containing the &#x60;runningtime&#x60; for a benchmark sample.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;results\&quot;: [         {\&quot;runningtime\&quot;: 0.12},         {\&quot;runningtime\&quot;: 0.11},         {\&quot;runningtime\&quot;: 0.13},         {\&quot;runningtime\&quot;: 0.12},         {\&quot;runningtime\&quot;: 0.12}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZCBenchmarkRequest** | [**ZCBenchmarkRequest**](../Models/ZCBenchmarkRequest.md)|  | |

### Return type

[**ZCBenchmarkResponse**](../Models/ZCBenchmarkResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

