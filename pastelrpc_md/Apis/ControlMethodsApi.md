# ControlMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeWalletPassphraseWalletpassphrasechangePost**](ControlMethodsApi.md#changeWalletPassphraseWalletpassphrasechangePost) | **POST** /walletpassphrasechange | Change the wallet passphrase |
| [**disconnectNodeDisconnectnodePost**](ControlMethodsApi.md#disconnectNodeDisconnectnodePost) | **POST** /disconnectnode | Disconnect from a specified node |
| [**encryptWalletEncryptwalletPost**](ControlMethodsApi.md#encryptWalletEncryptwalletPost) | **POST** /encryptwallet | Encrypt the wallet with a passphrase |
| [**getDeprecationInfoGetdeprecationinfoGet**](ControlMethodsApi.md#getDeprecationInfoGetdeprecationinfoGet) | **GET** /getdeprecationinfo | Get deprecation information of the current version |
| [**getInfoGetinfoGet**](ControlMethodsApi.md#getInfoGetinfoGet) | **GET** /getinfo | Get various state info |
| [**keypoolRefillKeypoolrefillPost**](ControlMethodsApi.md#keypoolRefillKeypoolrefillPost) | **POST** /keypoolrefill | Refill the keypool |
| [**lockUnspentLockunspentPost**](ControlMethodsApi.md#lockUnspentLockunspentPost) | **POST** /lockunspent | Lock or unlock unspent transaction outputs |
| [**moveMovePost**](ControlMethodsApi.md#moveMovePost) | **POST** /move | Move amount from one account to another |
| [**setAccountSetaccountPost**](ControlMethodsApi.md#setAccountSetaccountPost) | **POST** /setaccount | Associate a Pastel address with an account |
| [**setBanSetbanPost**](ControlMethodsApi.md#setBanSetbanPost) | **POST** /setban | Add or Remove an IP/Subnet from the Ban List |
| [**storageFeeStoragefeePost**](ControlMethodsApi.md#storageFeeStoragefeePost) | **POST** /storagefee | Interact with Storage Fee and related actions |
| [**storagefeeSetfeeStoragefeeSetfeePost**](ControlMethodsApi.md#storagefeeSetfeeStoragefeeSetfeePost) | **POST** /storagefee/setfee | Set a new fee for a specified fee type |
| [**walletPassphraseWalletpassphrasePost**](ControlMethodsApi.md#walletPassphraseWalletpassphrasePost) | **POST** /walletpassphrase | Unlock the wallet |
| [**walletlockWalletlockPost**](ControlMethodsApi.md#walletlockWalletlockPost) | **POST** /walletlock | Lock the wallet |


<a name="changeWalletPassphraseWalletpassphrasechangePost"></a>
# **changeWalletPassphraseWalletpassphrasechangePost**
> WalletPassphraseChangeResponse changeWalletPassphraseWalletpassphrasechangePost(WalletPassphraseChangeRequest)

Change the wallet passphrase

    Change the wallet passphrase from &#39;oldpassphrase&#39; to &#39;newpassphrase&#39;.  ### Description - This endpoint allows for the change of the existing wallet passphrase to a new passphrase. It&#39;s essential for maintaining wallet security and should be used with caution.  ### Input Parameters - &#x60;oldpassphrase&#x60;: The current passphrase of the wallet. - &#x60;newpassphrase&#x60;: The new passphrase that will replace the current passphrase.  ### Example Request &#x60;&#x60;&#x60;json POST /walletpassphrasechange {     \&quot;oldpassphrase\&quot;: \&quot;oldpassword123\&quot;,     \&quot;newpassphrase\&quot;: \&quot;newpassword456\&quot; } &#x60;&#x60;&#x60;  ### Response - On successful change, the response is a confirmation message.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Passphrase changed successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are incorrect or missing. - HTTP 500: Internal Server Error if there&#39;s an issue processing the request or if the old passphrase is incorrect.  ### Note - The wallet needs to be encrypted for this operation to succeed. If the wallet is unencrypted, this method will return an error.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **WalletPassphraseChangeRequest** | [**WalletPassphraseChangeRequest**](../Models/WalletPassphraseChangeRequest.md)|  | |

### Return type

[**WalletPassphraseChangeResponse**](../Models/WalletPassphraseChangeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="disconnectNodeDisconnectnodePost"></a>
# **disconnectNodeDisconnectnodePost**
> DisconnectNodeResponse disconnectNodeDisconnectnodePost(DisconnectNodeRequest)

Disconnect from a specified node

    Disconnect immediately from a specified node in the Pastel network.  ### Description - This endpoint allows for immediate disconnection from a specified node. It&#39;s useful for network management and control.  ### Input Parameters - &#x60;node&#x60;: The IP address and port of the node to disconnect from, in the format \&quot;IP:PORT\&quot;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;node\&quot;: \&quot;192.168.0.6:9933\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the status of the disconnection.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;status\&quot;: \&quot;Node disconnected successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as it modifies the network connections of the Pastel node.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DisconnectNodeRequest** | [**DisconnectNodeRequest**](../Models/DisconnectNodeRequest.md)|  | |

### Return type

[**DisconnectNodeResponse**](../Models/DisconnectNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="encryptWalletEncryptwalletPost"></a>
# **encryptWalletEncryptwalletPost**
> EncryptWalletResponse encryptWalletEncryptwalletPost(passphrase)

Encrypt the wallet with a passphrase

    Encrypt the wallet with a given passphrase.                             ### Description              - This endpoint encrypts the wallet with the provided passphrase. It&#39;s used for the first time encryption of the wallet. After encryption, any operations that interact with private keys (like sending or signing) will require the passphrase.              - If the wallet is already encrypted, this operation will fail, and you should use the &#x60;walletpassphrasechange&#x60; call instead.              - Note that encrypting the wallet will shutdown the server.               ### Input Parameters              - &#x60;passphrase&#x60;: A string representing the passphrase to encrypt the wallet with. It must be at least 1 character long, but a longer passphrase is recommended for security.               ### Example Request              &#x60;&#x60;&#x60;json              {                  \&quot;passphrase\&quot;: \&quot;my secure passphrase\&quot;              }              &#x60;&#x60;&#x60;               ### Response              - Returns a message indicating the encryption status and server shutdown.               ### Example Response              &#x60;&#x60;&#x60;json              {                  \&quot;message\&quot;: \&quot;wallet encrypted; Pastel server stopping, restart to run with encrypted wallet. The keypool has been flushed, you need to make a new backup.\&quot;              }              &#x60;&#x60;&#x60;               ### Possible Errors              - HTTP 400: Bad Request if wallet encryption is disabled or the wallet is already encrypted.              - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.               ### Note              - This is a critical operation that changes the state of the wallet and requires server restart.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**EncryptWalletResponse**](../Models/EncryptWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getDeprecationInfoGetdeprecationinfoGet"></a>
# **getDeprecationInfoGetdeprecationinfoGet**
> GetDeprecationInfoResponse getDeprecationInfoGetdeprecationinfoGet()

Get deprecation information of the current version

    Get information about the deprecation of the current server version.   ### Description - This endpoint returns an object containing details about the current server version, its subversion, and the block height at which this version will deprecate and shut down. This endpoint is applicable only on mainnet.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getdeprecationinfo&#x60;  ### Response - Returns a JSON object containing the server version, subversion, and deprecation block height.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;version\&quot;: 5000500,     \&quot;subversion\&quot;: \&quot;/MagicBean:5.0.5[-v]/\&quot;,     \&quot;deprecationheight\&quot;: 100000 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is typically used for software maintenance and upgrade planning.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDeprecationInfoResponse**](../Models/GetDeprecationInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getInfoGetinfoGet"></a>
# **getInfoGetinfoGet**
> GetInfoResponse getInfoGetinfoGet()

Get various state info

    Get an object containing various state info about the Pastel server.  ### Description - This endpoint provides information about the server&#39;s state, including wallet balance, block count, connections, and other relevant details.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getinfo&#x60;  ### Response - Returns a JSON object containing various state information of the server.  ### Example Response &#x60;&#x60;&#x60;json {   \&quot;version\&quot;: 50000,   \&quot;protocolversion\&quot;: 70015,   \&quot;walletversion\&quot;: 60000,   \&quot;balance\&quot;: 15.0,   \&quot;blocks\&quot;: 120987,   \&quot;timeoffset\&quot;: 0,   \&quot;connections\&quot;: 8,   \&quot;proxy\&quot;: \&quot;127.0.0.1:9050\&quot;,   \&quot;difficulty\&quot;: 1.23456789,   \&quot;testnet\&quot;: false,   \&quot;keypoololdest\&quot;: 1577836800,   \&quot;keypoolsize\&quot;: 1000,   \&quot;unlocked_until\&quot;: 1596240000,   \&quot;paytxfee\&quot;: 0.0001,   \&quot;relayfee\&quot;: 0.00001,   \&quot;errors\&quot;: \&quot;Warning: unknown new rules activated (versionbit 28)\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for getting a quick overview of the state of the server and its wallet.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInfoResponse**](../Models/GetInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="keypoolRefillKeypoolrefillPost"></a>
# **keypoolRefillKeypoolrefillPost**
> oas_any_type_not_mapped keypoolRefillKeypoolrefillPost(KeypoolRefillRequest)

Refill the keypool

    Refill the keypool to the specified size.  ### Description - This endpoint is used to refill the keypool of the wallet to a new size. The keypool keeps a buffer of keys available for use in transactions. Refilling the keypool is important to maintain anonymity and security.  ### Input Parameters - &#x60;newsize&#x60;: (Optional, numeric) The new size for the keypool. Default is 100.  ### Example Request - &#x60;POST /keypoolrefill&#x60; with payload &#x60;{\&quot;newsize\&quot;: 150}&#x60;  ### Response - This method does not return any specific data, but a successful request indicates that the keypool was refilled successfully.  ### Possible Errors - HTTP 400: Bad Request if the newsize parameter is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - It&#39;s recommended to refill the keypool periodically for operational security and efficiency.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **KeypoolRefillRequest** | [**KeypoolRefillRequest**](../Models/KeypoolRefillRequest.md)|  | |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="lockUnspentLockunspentPost"></a>
# **lockUnspentLockunspentPost**
> LockUnspentResponse lockUnspentLockunspentPost(LockUnspentRequest)

Lock or unlock unspent transaction outputs

    Lock or unlock specified transaction outputs.  ### Description - Temporarily lock (unlock&#x3D;false) or unlock (unlock&#x3D;true) specified transaction outputs. - A locked transaction output will not be chosen by automatic coin selection when spending Pastel. - Locks are stored in memory only and are cleared upon node restart.  ### Input Parameters - &#x60;request&#x60;: A JSON object containing the unlock flag and a list of transaction outputs to be locked or unlocked.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;unlock\&quot;: false,     \&quot;transactions\&quot;: [         {             \&quot;txid\&quot;: \&quot;a08e6907dbbd3d809776dbfc5d82e371b764ed838b5655e72f463568df1aadf0\&quot;,             \&quot;vout\&quot;: 1         }     ] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **LockUnspentRequest** | [**LockUnspentRequest**](../Models/LockUnspentRequest.md)|  | |

### Return type

[**LockUnspentResponse**](../Models/LockUnspentResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="moveMovePost"></a>
# **moveMovePost**
> MoveResponse moveMovePost(MoveRequest)

Move amount from one account to another

    Move a specified amount from one account in your wallet to another.  ### Description - **DEPRECATED**: This method is deprecated. However, it is still available for use. - Moves a specified amount from one account in your wallet to another. It is a local operation and does not involve a transaction on the blockchain.  ### Input Parameters - &#x60;fromaccount&#x60;: (string, required) The account to move funds from. Must be set to the empty string \&quot;\&quot; to represent the default account. - &#x60;toaccount&#x60;: (string, required) The account to move funds to. Must be set to the empty string \&quot;\&quot; to represent the default account. - &#x60;amount&#x60;: (numeric, required) The quantity of currency to move between accounts. - &#x60;minconf&#x60;: (numeric, optional, default&#x3D;1) The minimum number of confirmations for used funds. - &#x60;comment&#x60;: (string, optional) An optional comment, stored in the wallet only.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;fromaccount\&quot;: \&quot;\&quot;,     \&quot;toaccount\&quot;: \&quot;tabby\&quot;,     \&quot;amount\&quot;: 0.01,     \&quot;minconf\&quot;: 1,     \&quot;comment\&quot;: \&quot;Transfer to tabby\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a boolean indicating if the operation was successful.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is deprecated and might be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MoveRequest** | [**MoveRequest**](../Models/MoveRequest.md)|  | |

### Return type

[**MoveResponse**](../Models/MoveResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setAccountSetaccountPost"></a>
# **setAccountSetaccountPost**
> SetAccountResponse setAccountSetaccountPost(SetAccountRequest)

Associate a Pastel address with an account

    DEPRECATED. Sets the account associated with the given address.  ### Description - This endpoint is used to associate a Pastel address with an account. - The &#x60;account&#x60; parameter must be set to an empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error.  ### Input Parameters - &#x60;zcashaddress&#x60; (string, required): The Pastel address to be associated with an account. - &#x60;account&#x60; (string, required): The account name. Must be an empty string for the default account.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot;,     \&quot;account\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating success or failure of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Account associated successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetAccountRequest** | [**SetAccountRequest**](../Models/SetAccountRequest.md)|  | |

### Return type

[**SetAccountResponse**](../Models/SetAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="setBanSetbanPost"></a>
# **setBanSetbanPost**
> SetBanResponse setBanSetbanPost(SetBanRequest)

Add or Remove an IP/Subnet from the Ban List

    Add or remove an IP/Subnet from the banned list.  ### Description - This endpoint attempts to add or remove an IP/Subnet from the banned list of the node.  ### Input Parameters - &#x60;ip_subnet&#x60;: The IP/Subnet with an optional netmask (default is /32 &#x3D; single IP). - &#x60;command&#x60;: &#39;add&#39; to add to the list, &#39;remove&#39; to remove from the list. - &#x60;bantime&#x60;: (Optional) Time in seconds for how long the IP is banned. 0 or empty uses the default time of 24 hours. - &#x60;absolute&#x60;: (Optional) If true, &#x60;bantime&#x60; is an absolute timestamp since epoch (Jan 1 1970 GMT).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ip_subnet\&quot;: \&quot;192.168.0.6\&quot;,     \&quot;command\&quot;: \&quot;add\&quot;,     \&quot;bantime\&quot;: 86400,     \&quot;absolute\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns a success message upon successful addition or removal.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Success\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as it affects the node&#39;s network connections.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **SetBanRequest** | [**SetBanRequest**](../Models/SetBanRequest.md)|  | |

### Return type

[**SetBanResponse**](../Models/SetBanResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storageFeeStoragefeePost"></a>
# **storageFeeStoragefeePost**
> StorageFeeResponse storageFeeStoragefeePost(command, body)

Interact with Storage Fee and related actions

    Interact with various Storage Fee and related actions in the Pastel network.  ### Description - This endpoint allows interaction with various aspects of storage fees and related actions.  ### Input Parameters - &#x60;command&#x60;: The storage fee command to execute. - &#x60;params&#x60;: Parameters for the specified command.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;getstoragefee\&quot;,     \&quot;params\&quot;: {\&quot;is_local\&quot;: true, \&quot;height\&quot;: 1000} } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the storage fee command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: {         \&quot;storage_fee\&quot;: \&quot;0.001\&quot;,         \&quot;height\&quot;: 1000     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **command** | **String**|  | [default to null] |
| **body** | **oas_any_type_not_mapped**|  | |

### Return type

[**StorageFeeResponse**](../Models/StorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="storagefeeSetfeeStoragefeeSetfeePost"></a>
# **storagefeeSetfeeStoragefeeSetfeePost**
> StorageFeeSetFeeResponse storagefeeSetfeeStoragefeeSetfeePost(StorageFeeSetFeeRequest)

Set a new fee for a specified fee type

    Set a new fee for various types of fees in the masternode system.  ### Description - This endpoint allows setting a new fee for storage, ticket, sense-compute, or sense-processing. - It requires an active masternode to execute.  ### Input Parameters - &#x60;fee_type&#x60;: The type of fee to set. Valid types are &#39;storage&#39;, &#39;ticket&#39;, &#39;sense-compute&#39;, and &#39;sense-processing&#39;. - &#x60;new_fee&#x60;: (Optional) The new fee amount to set. If not specified, the current fee for the specified type will be maintained.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;fee_type\&quot;: \&quot;storage\&quot;,     \&quot;new_fee\&quot;: 100 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success of the operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or the fee type is not recognized. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Forbidden if the request is not made by an active masternode.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **StorageFeeSetFeeRequest** | [**StorageFeeSetFeeRequest**](../Models/StorageFeeSetFeeRequest.md)|  | |

### Return type

[**StorageFeeSetFeeResponse**](../Models/StorageFeeSetFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="walletPassphraseWalletpassphrasePost"></a>
# **walletPassphraseWalletpassphrasePost**
> WalletPassphraseResponse walletPassphraseWalletpassphrasePost(WalletPassphraseRequest)

Unlock the wallet

    Unlock the wallet with a passphrase for a given duration.  ### Description - Unlocks the wallet for the specified time period, allowing transactions related to private keys, such as sending Pastel.   ### Input Parameters - &#x60;passphrase&#x60;: The passphrase used to encrypt the wallet (string, required). - &#x60;timeout&#x60;: Duration in seconds to keep the wallet unlocked (integer, required).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;passphrase\&quot;: \&quot;my pass phrase\&quot;,     \&quot;timeout\&quot;: 60 } &#x60;&#x60;&#x60;  ### Response - Confirmation message indicating successful unlocking of the wallet.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Wallet unlocked successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Incorrect passphrase provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 403: Wallet is already unlocked.  ### Note - If the wallet is already unlocked, issuing this command will reset the unlock time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **WalletPassphraseRequest** | [**WalletPassphraseRequest**](../Models/WalletPassphraseRequest.md)|  | |

### Return type

[**WalletPassphraseResponse**](../Models/WalletPassphraseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="walletlockWalletlockPost"></a>
# **walletlockWalletlockPost**
> oas_any_type_not_mapped walletlockWalletlockPost()

Lock the wallet

    Lock the wallet by removing the encryption key from memory.  ### Description - This endpoint locks the wallet by removing the wallet encryption key from memory.  - After calling this method, you will need to call &#x60;walletpassphrase&#x60; again before being able to call any methods which require the wallet to be unlocked.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;POST /walletlock&#x60;  ### Response - Returns an empty response on successful execution.  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request or if the wallet is not encrypted. - HTTP 400: Bad Request if called with an unencrypted wallet.  ### Examples: - Set the passphrase for 2 minutes to perform a transaction:   - &#x60;walletpassphrase \&quot;my pass phrase\&quot; 120&#x60; - Perform a send (requires passphrase set):   - &#x60;sendtoaddress \&quot;PtczsZ91Bt3oDPDQotzUsrx1wjmsFVgf28n\&quot; 1.0&#x60; - Clear the passphrase since we are done before 2 minutes is up:   - &#x60;walletlock&#x60;  ### Note - This is primarily used for security purposes in managing wallet access.

### Parameters
This endpoint does not need any parameter.

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

