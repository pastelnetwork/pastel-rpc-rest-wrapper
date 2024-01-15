# WalletMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dumpPrivKeyDumpprivkeyGet**](WalletMethodsApi.md#dumpPrivKeyDumpprivkeyGet) | **GET** /dumpprivkey | Reveal the private key for a given address |
| [**dumpWalletDumpwalletPost**](WalletMethodsApi.md#dumpWalletDumpwalletPost) | **POST** /dumpwallet | Dump wallet keys |
| [**getAccountAddressGetaccountaddressGet**](WalletMethodsApi.md#getAccountAddressGetaccountaddressGet) | **GET** /getaccountaddress | Get the current Pastel address for receiving payments |
| [**getAddressesByAccountGetaddressesbyaccountGet**](WalletMethodsApi.md#getAddressesByAccountGetaddressesbyaccountGet) | **GET** /getaddressesbyaccount | Get addresses by account |
| [**getReceivedByAccountGetreceivedbyaccountGet**](WalletMethodsApi.md#getReceivedByAccountGetreceivedbyaccountGet) | **GET** /getreceivedbyaccount | Get the total amount received by an account |
| [**importAddressImportaddressPost**](WalletMethodsApi.md#importAddressImportaddressPost) | **POST** /importaddress | Import an address |
| [**importPrivKeyImportprivkeyPost**](WalletMethodsApi.md#importPrivKeyImportprivkeyPost) | **POST** /importprivkey | Import a private key |
| [**importWalletImportwalletPost**](WalletMethodsApi.md#importWalletImportwalletPost) | **POST** /importwallet | Import a wallet from a dump file |
| [**listAccountsListaccountsGet**](WalletMethodsApi.md#listAccountsListaccountsGet) | **GET** /listaccounts | List account balances |
| [**listAddressAmountsListaddressamountsGet**](WalletMethodsApi.md#listAddressAmountsListaddressamountsGet) | **GET** /listaddressamounts | List balance on each address |
| [**listReceivedByAddressListreceivedbyaddressGet**](WalletMethodsApi.md#listReceivedByAddressListreceivedbyaddressGet) | **GET** /listreceivedbyaddress | List balances by receiving address |
| [**listTransactionsListtransactionsGet**](WalletMethodsApi.md#listTransactionsListtransactionsGet) | **GET** /listtransactions | List recent transactions |
| [**zExportKeyZExportkeyPost**](WalletMethodsApi.md#zExportKeyZExportkeyPost) | **POST** /z_exportkey | Reveal the private key corresponding to a z-address |
| [**zExportViewingKeyZExportviewingkeyGet**](WalletMethodsApi.md#zExportViewingKeyZExportviewingkeyGet) | **GET** /z_exportviewingkey | Export the viewing key for a Z-address |
| [**zExportWalletZExportwalletPost**](WalletMethodsApi.md#zExportWalletZExportwalletPost) | **POST** /z_exportwallet | Export wallet keys |
| [**zGetNewAddressZGetnewaddressGet**](WalletMethodsApi.md#zGetNewAddressZGetnewaddressGet) | **GET** /z_getnewaddress | Generate a new shielded address |
| [**zGetTotalBalanceZGettotalbalanceGet**](WalletMethodsApi.md#zGetTotalBalanceZGettotalbalanceGet) | **GET** /z_gettotalbalance | Get the total balance of both transparent and private funds |
| [**zImportKeyZImportkeyGet**](WalletMethodsApi.md#zImportKeyZImportkeyGet) | **GET** /z_importkey | Import a Z key into the wallet |
| [**zImportViewingKeyZImportviewingkeyPost**](WalletMethodsApi.md#zImportViewingKeyZImportviewingkeyPost) | **POST** /z_importviewingkey | Import a viewing key into the wallet |
| [**zImportWalletZImportwalletPost**](WalletMethodsApi.md#zImportWalletZImportwalletPost) | **POST** /z_importwallet | Import keys from a wallet export file |


<a name="dumpPrivKeyDumpprivkeyGet"></a>
# **dumpPrivKeyDumpprivkeyGet**
> DumpPrivKeyResponse dumpPrivKeyDumpprivkeyGet(DumpPrivKeyRequest)

Reveal the private key for a given address

    Reveals the private key corresponding to the specified transparent address.  ### Description - This endpoint is used to retrieve the private key associated with a given transparent address.  - It&#39;s important to handle the output with care as the private key controls access to the assets held in the address.  ### Input Parameters - &#x60;t_addr&#x60;: The transparent address for which the private key is to be revealed.  ### Example Request - &#x60;GET /dumpprivkey?t_addr&#x3D;myaddress&#x60;  ### Response - Returns a JSON object containing the private key in a string format.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;key\&quot;: \&quot;5J1m2B2K5m3...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the address is invalid or not specified. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The output should be kept secure as it provides complete control over the assets in the address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **DumpPrivKeyRequest** | [**DumpPrivKeyRequest**](../Models/DumpPrivKeyRequest.md)|  | |

### Return type

[**DumpPrivKeyResponse**](../Models/DumpPrivKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="dumpWalletDumpwalletPost"></a>
# **dumpWalletDumpwalletPost**
> DumpWalletResponse dumpWalletDumpwalletPost(filename)

Dump wallet keys

    Dumps taddr wallet keys in a human-readable format.  ### Description - Dumps transparent address (taddr) wallet keys to a specified file. Overwriting an existing file is not permitted.  ### Input Parameters - &#x60;filename&#x60;: A string representing the filename to which the wallet keys will be dumped. The file will be saved in the folder set by the &#x60;pasteld -exportdir&#x60; option.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;my_wallet_dump\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet keys are dumped.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/dumped/file/my_wallet_dump\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.  ### Note - Use this endpoint for transparent address wallet key backups.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**DumpWalletResponse**](../Models/DumpWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAccountAddressGetaccountaddressGet"></a>
# **getAccountAddressGetaccountaddressGet**
> GetAccountAddressResponse getAccountAddressGetaccountaddressGet(account)

Get the current Pastel address for receiving payments

    Get the current Pastel address for receiving payments to a specified account.  ### Description - This endpoint returns the current Pastel address for receiving payments to the specified account.  - Note: This method is deprecated.  ### Input Parameters - &#x60;account&#x60;: (string, required) MUST be set to the empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error.  ### Example Request - &#x60;GET /getaccountaddress?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON object containing the Pastel address for the account.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcashaddress\&quot;: \&quot;t1KSLVSVdZD1Cz8TCr7FBG8m5xKwKMBrMT6\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if an invalid account name is provided. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is deprecated and may be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**GetAccountAddressResponse**](../Models/GetAccountAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getAddressesByAccountGetaddressesbyaccountGet"></a>
# **getAddressesByAccountGetaddressesbyaccountGet**
> oas_any_type_not_mapped getAddressesByAccountGetaddressesbyaccountGet(account)

Get addresses by account

    Get the list of addresses for the given account.  ### Description - **DEPRECATED**: This endpoint is deprecated and might be removed in future versions. It returns the list of addresses associated with a specified account. - The account argument must be set to the empty string &#x60;\&quot;\&quot;&#x60; to represent the default account. Passing any other string will result in an error.  ### Input Parameters - &#x60;account&#x60;: (string, required) The account name. Must be set to &#x60;\&quot;\&quot;&#x60; for the default account.  ### Example Request - &#x60;GET /getaddressesbyaccount?account&#x3D;\&quot;\&quot;&#x60;  ### Response - Returns a JSON array of strings, each representing a Pastel address associated with the given account.  ### Example Response &#x60;&#x60;&#x60;json [   \&quot;paxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot;,   \&quot;payyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\&quot; ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the account parameter is not the empty string. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is primarily used for wallet management and account balance tracking.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **account** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getReceivedByAccountGetreceivedbyaccountGet"></a>
# **getReceivedByAccountGetreceivedbyaccountGet**
> GetReceivedByAccountResponse getReceivedByAccountGetreceivedbyaccountGet(GetReceivedByAccountRequest)

Get the total amount received by an account

    Get the total amount received by addresses with a specified account in transactions with at least a certain number of confirmations.  ### Description - This endpoint returns the total amount received by addresses associated with a given account, considering transactions with at least the specified number of confirmations. - Note: The &#39;account&#39; parameter is deprecated and should be set to an empty string \&quot;\&quot; to represent the default account.  ### Input Parameters - &#x60;account&#x60; (string, required): Must be set to the empty string \&quot;\&quot; to represent the default account. Passing any other string will result in an error. - &#x60;minconf&#x60; (int, optional, default&#x3D;1): Only include transactions confirmed at least this many times.  ### Example Request - &#x60;GET /getreceivedbyaccount?account&#x3D;\&quot;\&quot;&amp;minconf&#x3D;1&#x60;  ### Response - Returns the total amount received by the specified account.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;amount\&quot;: 123.45 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetReceivedByAccountRequest** | [**GetReceivedByAccountRequest**](../Models/GetReceivedByAccountRequest.md)|  | |

### Return type

[**GetReceivedByAccountResponse**](../Models/GetReceivedByAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="importAddressImportaddressPost"></a>
# **importAddressImportaddressPost**
> ImportAddressResponse importAddressImportaddressPost(ImportAddressRequest)

Import an address

    Import an address or script (in hex) that can be watched as if it were in your wallet but cannot be used to spend.  ### Description - This endpoint adds an address or script to your wallet as a watch-only address. This means you can see incoming transactions to it, but not spend its funds. - The &#x60;rescan&#x60; option will rescan the wallet for transactions, but this can be time-consuming.  ### Input Parameters - &#x60;address&#x60;: The address to import. - &#x60;label&#x60;: An optional label for the address. - &#x60;rescan&#x60;: A boolean indicating whether to rescan the wallet for transactions. Default is true.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;myaddress\&quot;,     \&quot;label\&quot;: \&quot;testing\&quot;,     \&quot;rescan\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns &#x60;null&#x60; on successful addition of the address. In case of an error, an error message is returned.  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint with caution as rescanning can take a considerable amount of time.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ImportAddressRequest** | [**ImportAddressRequest**](../Models/ImportAddressRequest.md)|  | |

### Return type

[**ImportAddressResponse**](../Models/ImportAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="importPrivKeyImportprivkeyPost"></a>
# **importPrivKeyImportprivkeyPost**
> ImportPrivKeyResponse importPrivKeyImportprivkeyPost(zcashprivkey, label, rescan)

Import a private key

    Import a private key into the wallet.  ### Description - Adds a Zcash-format private key to your wallet, allowing the wallet to use funds associated with the key&#39;s address.  ### Input Parameters - &#x60;zcashprivkey&#x60;: The Zcash private key to be imported (required). - &#x60;label&#x60;: An optional label for the address (optional, default empty string). - &#x60;rescan&#x60;: A boolean indicating whether the wallet should be rescanned for transactions after importing the key (optional, default true).  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;zcashprivkey\&quot;: \&quot;mykey\&quot;,     \&quot;label\&quot;: \&quot;testing\&quot;,     \&quot;rescan\&quot;: false } &#x60;&#x60;&#x60;  ### Response - Returns the address associated with the imported private key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;address\&quot;: \&quot;t1XYZabc123...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Importing a private key can take minutes if rescan is true.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zcashprivkey** | **String**|  | [default to null] |
| **label** | **String**|  | [optional] [default to null] |
| **rescan** | **Boolean**|  | [optional] [default to true] |

### Return type

[**ImportPrivKeyResponse**](../Models/ImportPrivKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="importWalletImportwalletPost"></a>
# **importWalletImportwalletPost**
> ImportWalletResponse importWalletImportwalletPost(filename)

Import a wallet from a dump file

    Import taddr keys from a wallet dump file.  ### Description - This endpoint imports taddr keys from a specified wallet dump file. This is useful for restoring a wallet from a backup.  ### Input Parameters - &#x60;filename&#x60;: The path to the wallet dump file to be imported.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;path/to/exportdir/nameofbackup\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a confirmation message upon successful import.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;message\&quot;: \&quot;Wallet imported successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure that the wallet dump file exists at the specified path before calling this endpoint.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ImportWalletResponse**](../Models/ImportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listAccountsListaccountsGet"></a>
# **listAccountsListaccountsGet**
> ListAccountsResponse listAccountsListaccountsGet(minconf, includeWatchonly)

List account balances

    List the balances of all accounts in the wallet.  ### Description - Returns a list of accounts with their respective balances. Accounts are identified by their names.  ### Input Parameters - &#x60;minconf&#x60; (optional): Minimum number of confirmations for a transaction to be included. - &#x60;includeWatchonly&#x60; (optional): Include balances in watch-only addresses.  ### Example Request - &#x60;GET /listaccounts?minconf&#x3D;1&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON object containing account names and their balances.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;accounts\&quot;: [         {\&quot;account\&quot;: \&quot;account_name\&quot;, \&quot;balance\&quot;: 123.45},         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**Minconf_1**](../Models/.md)|  | [optional] [default to 1] |
| **includeWatchonly** | [**Includewatchonly_1**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**ListAccountsResponse**](../Models/ListAccountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listAddressAmountsListaddressamountsGet"></a>
# **listAddressAmountsListaddressamountsGet**
> ListAddressAmountsResponse listAddressAmountsListaddressamountsGet(include\_empty, ismine\_filter)

List balance on each address

    List the balance on each address in the wallet.  ### Description - This endpoint lists the balances associated with each address in the wallet. - It allows filtering of addresses based on whether they have a balance and the type of ownership (all, watchOnly, spendableOnly).  ### Input Parameters - &#x60;include_empty&#x60;: (bool, optional, default&#x3D;false) Include addresses with empty balances. - &#x60;ismine_filter&#x60;: (str, optional, default&#x3D;all) Filter for \&quot;all\&quot;, \&quot;watchOnly\&quot;, or \&quot;spendableOnly\&quot; addresses.  ### Example Request - &#x60;GET /listaddressamounts?include_empty&#x3D;true&amp;ismine_filter&#x3D;spendableOnly&#x60;  ### Response - Returns a JSON object with addresses as keys and their corresponding balances as values.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;balances\&quot;: {         \&quot;t1XYZ...abc\&quot;: 0.5,         \&quot;t1ABC...xyz\&quot;: 1.2     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for obtaining an overview of wallet balances distributed across different addresses.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **include\_empty** | [**Include_Empty**](../Models/.md)|  | [optional] [default to false] |
| **ismine\_filter** | [**Ismine_Filter**](../Models/.md)|  | [optional] [default to all] |

### Return type

[**ListAddressAmountsResponse**](../Models/ListAddressAmountsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listReceivedByAddressListreceivedbyaddressGet"></a>
# **listReceivedByAddressListreceivedbyaddressGet**
> oas_any_type_not_mapped listReceivedByAddressListreceivedbyaddressGet(minconf, includeempty, includeWatchonly)

List balances by receiving address

    List balances by receiving address.  ### Description - This endpoint returns the list of balances associated with each receiving address.  ### Input Parameters - &#x60;minconf&#x60;: The minimum number of confirmations before payments are included. Default is 1. - &#x60;includeempty&#x60;: Whether to include addresses that haven&#39;t received any payments. Default is false. - &#x60;includeWatchonly&#x60;: Whether to include watchonly addresses (see &#39;importaddress&#39;). Default is false.  ### Example Request - &#x60;GET /listreceivedbyaddress?minconf&#x3D;1&amp;includeempty&#x3D;true&amp;includeWatchonly&#x3D;false&#x60;  ### Response - Returns a JSON array with information about each address and its associated balance.  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;involvesWatchonly\&quot;: true,         \&quot;address\&quot;: \&quot;receivingaddress\&quot;,         \&quot;account\&quot;: \&quot;accountname\&quot;,         \&quot;amount\&quot;: 1.234,         \&quot;confirmations\&quot;: 5     },     ... ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The &#x60;account&#x60; field is deprecated and will be removed in future versions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **minconf** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to 1] |
| **includeempty** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |
| **includeWatchonly** | [**oas_any_type_not_mapped**](../Models/.md)|  | [optional] [default to false] |

### Return type

[**oas_any_type_not_mapped**](../Models/AnyType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listTransactionsListtransactionsGet"></a>
# **listTransactionsListtransactionsGet**
> ListTransactionsResponse listTransactionsListtransactionsGet(ListTransactionsRequest)

List recent transactions

    List up to &#39;count&#39; most recent transactions skipping the first &#39;from&#39; transactions for account &#39;account&#39;.  ### Description - This endpoint returns up to &#39;count&#39; most recent transactions skipping the first &#39;from&#39; transactions for account &#39;account&#39;. - It can include transactions to watch-only addresses if specified.  ### Input Parameters - &#x60;account&#x60;: (Optional) The account name. Should be \&quot;*\&quot;. - &#x60;count&#x60;: (Optional, default&#x3D;10) The number of transactions to return. - &#x60;from&#x60;: (Optional, default&#x3D;0) The number of transactions to skip. - &#x60;include_watch_only&#x60;: (Optional, default&#x3D;false) Include transactions to watchonly addresses.  ### Example Request - &#x60;GET /listtransactions?account&#x3D;*&amp;count&#x3D;20&amp;from&#x3D;100&amp;include_watch_only&#x3D;true&#x60;  ### Response - Returns a list of transaction information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transactions\&quot;: [         {             \&quot;account\&quot;: \&quot;...\&quot;,             \&quot;address\&quot;: \&quot;...\&quot;,             \&quot;category\&quot;: \&quot;...\&quot;,             \&quot;amount\&quot;: ...,             \&quot;vout\&quot;: ...,             ...         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ListTransactionsRequest** | [**ListTransactionsRequest**](../Models/ListTransactionsRequest.md)|  | |

### Return type

[**ListTransactionsResponse**](../Models/ListTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zExportKeyZExportkeyPost"></a>
# **zExportKeyZExportkeyPost**
> ZExportKeyResponse zExportKeyZExportkeyPost(ZExportKeyRequest)

Reveal the private key corresponding to a z-address

    Reveals the private key corresponding to the specified z-address.  ### Description - This endpoint is used to extract the private key associated with a given z-address. - The private key can then be used for various purposes, including wallet backup and migration.  ### Input Parameters - &#x60;zaddr&#x60;: A string representing the z-address for which the private key is required.  ### Example Request - &#x60;POST /z_exportkey&#x60;   &#x60;&#x60;&#x60;json   {       \&quot;zaddr\&quot;: \&quot;myzaddress\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the private key associated with the specified z-address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;key\&quot;: \&quot;5Jxxxxx...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the z-address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint cautiously as exposing private keys can lead to security risks.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZExportKeyRequest** | [**ZExportKeyRequest**](../Models/ZExportKeyRequest.md)|  | |

### Return type

[**ZExportKeyResponse**](../Models/ZExportKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zExportViewingKeyZExportviewingkeyGet"></a>
# **zExportViewingKeyZExportviewingkeyGet**
> ZExportViewingKeyResponse zExportViewingKeyZExportviewingkeyGet(zaddr)

Export the viewing key for a Z-address

    Export the viewing key for a specified Z-address (zaddr).  ### Description - This endpoint reveals the viewing key corresponding to a given Z-address.  - The key can then be used with the &#x60;z_importviewingkey&#x60; method.  ### Input Parameters - &#x60;zaddr&#x60;: A string representing the Z-address for which the viewing key is requested.  ### Example Request - &#x60;GET /z_exportviewingkey?zaddr&#x3D;myaddress&#x60;  ### Response - Returns a JSON object containing the viewing key for the specified Z-address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;viewing_key\&quot;: \&quot;Zivk...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the Z-address is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The returned viewing key allows viewing the transaction details associated with the Z-address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zaddr** | **String**|  | [default to null] |

### Return type

[**ZExportViewingKeyResponse**](../Models/ZExportViewingKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zExportWalletZExportwalletPost"></a>
# **zExportWalletZExportwalletPost**
> ExportWalletResponse zExportWalletZExportwalletPost(filename)

Export wallet keys

    Export all wallet keys, for taddr and zaddr, in a human-readable format.  ### Description - Exports all wallet keys, including both transparent (taddr) and shielded (zaddr) addresses, to a specified file. Overwriting an existing file is not permitted.  ### Input Parameters - &#x60;filename&#x60;: A string representing the filename to which the wallet keys will be exported. The file will be saved in the folder set by the &#x60;pasteld -exportdir&#x60; option.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;my_wallet_export\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the full path of the destination file where the wallet keys are exported.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;path\&quot;: \&quot;/path/to/exported/file/my_wallet_export\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if the filename parameter is not provided or if the file already exists.  ### Note - Use this endpoint to backup wallet keys securely.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ExportWalletResponse**](../Models/ExportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetNewAddressZGetnewaddressGet"></a>
# **zGetNewAddressZGetnewaddressGet**
> ZGetNewAddressResponse zGetNewAddressZGetnewaddressGet(address\_type)

Generate a new shielded address

    Generate a new shielded address for receiving payments.   ### Description - This endpoint returns a new shielded (Zcash) Sapling address for receiving payments.  ### Input Parameters - &#x60;type&#x60;: (Optional) The type of address to generate. Currently, only &#39;Sapling&#39; type is supported.  ### Example Request - &#x60;GET /z_getnewaddress?type&#x3D;Sapling&#x60;  ### Response - Returns a JSON object containing the new shielded Zcash address.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;zcash_address\&quot;: \&quot;zs1qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - HTTP 400: Bad Request if an invalid address type is specified.  ### Note - Used for creating new addresses to receive shielded transactions.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **address\_type** | [**Address_Type**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**ZGetNewAddressResponse**](../Models/ZGetNewAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zGetTotalBalanceZGettotalbalanceGet"></a>
# **zGetTotalBalanceZGettotalbalanceGet**
> ZGetTotalBalanceResponse zGetTotalBalanceZGettotalbalanceGet(ZGetTotalBalanceRequest)

Get the total balance of both transparent and private funds

    Get the total value of funds stored in the node&#39;s wallet.  ### Description - This endpoint returns the total balance of both transparent and private funds in the node&#39;s wallet. - The balance is calculated based on the specified minimum number of confirmations and can include watchonly addresses.  ### Input Parameters - &#x60;minconf&#x60; (int, optional, default&#x3D;1): Only include transactions confirmed at least this many times. - &#x60;includeWatchonly&#x60; (bool, optional, default&#x3D;false): Include balance in watchonly addresses.  ### Example Request - &#x60;GET /z_gettotalbalance?minconf&#x3D;5&amp;includeWatchonly&#x3D;true&#x60;  ### Response - Returns a JSON object containing the total balance of transparent and private funds.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;transparent\&quot;: 100.0,     \&quot;private\&quot;: 50.0,     \&quot;total\&quot;: 150.0 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Balance calculations with watchonly addresses require the corresponding viewing keys.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZGetTotalBalanceRequest** | [**ZGetTotalBalanceRequest**](../Models/ZGetTotalBalanceRequest.md)|  | |

### Return type

[**ZGetTotalBalanceResponse**](../Models/ZGetTotalBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zImportKeyZImportkeyGet"></a>
# **zImportKeyZImportkeyGet**
> ZImportKeyResponse zImportKeyZImportkeyGet(zkey, rescan, start\_height)

Import a Z key into the wallet

    Imports a Z key (as returned by z_exportkey) to your wallet.  ### Description - Adds a Z key to your wallet and optionally rescans the wallet for transactions.  ### Input Parameters - &#x60;zkey&#x60;: The Z key to be imported (required). - &#x60;rescan&#x60;: Option to rescan the wallet for transactions - can be \&quot;yes\&quot;, \&quot;no\&quot;, or \&quot;whenkeyisnew\&quot; (optional, default&#x3D;\&quot;whenkeyisnew\&quot;). - &#x60;start_height&#x60;: Block height to start rescan from (optional, default&#x3D;0).  ### Example Request - &#x60;GET /z_importkey?zkey&#x3D;mykey&amp;rescan&#x3D;yes&amp;start_height&#x3D;30000&#x60;  ### Response - Returns a JSON object containing the type and address corresponding to the imported spending key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;address\&quot;: \&quot;ps1xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Importing a key can take minutes to complete if rescan is true. The call will block until the rescan is complete.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **zkey** | **String**|  | [default to null] |
| **rescan** | **String**|  | [optional] [default to null] |
| **start\_height** | **Integer**|  | [optional] [default to null] |

### Return type

[**ZImportKeyResponse**](../Models/ZImportKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="zImportViewingKeyZImportviewingkeyPost"></a>
# **zImportViewingKeyZImportviewingkeyPost**
> ZImportViewingKeyResponse zImportViewingKeyZImportviewingkeyPost(ZImportViewingKeyRequest)

Import a viewing key into the wallet

    Import a viewing key into your wallet.  ### Description - This endpoint adds a viewing key (as returned by z_exportviewingkey) to your wallet. It allows you to track transactions associated with the viewing key&#39;s address.  ### Input Parameters - &#x60;vkey&#x60;: The viewing key to be imported. - &#x60;rescan&#x60;: Rescan option for the wallet transactions. Can be \&quot;yes\&quot;, \&quot;no\&quot;, or \&quot;whenkeyisnew\&quot;. - &#x60;start_height&#x60;: The block height from which to start the rescan.  ### Example Request - &#x60;POST /z_importviewingkey&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;vkey\&quot;: \&quot;your_viewing_key\&quot;,     \&quot;rescan\&quot;: \&quot;yes\&quot;,     \&quot;start_height\&quot;: 30000 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the type and address corresponding to the imported viewing key.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;sapling\&quot;,     \&quot;address\&quot;: \&quot;pastel_address\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request. - Specific errors for invalid viewing key or if the key already exists in the wallet.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ZImportViewingKeyRequest** | [**ZImportViewingKeyRequest**](../Models/ZImportViewingKeyRequest.md)|  | |

### Return type

[**ZImportViewingKeyResponse**](../Models/ZImportViewingKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="zImportWalletZImportwalletPost"></a>
# **zImportWalletZImportwalletPost**
> ZImportWalletResponse zImportWalletZImportwalletPost(filename)

Import keys from a wallet export file

    Imports taddr and zaddr keys from a wallet export file. This is typically used after using &#x60;z_exportwallet&#x60;.  ### Description - Allows for the importation of taddr and zaddr keys from a previously exported wallet file.  ### Input Parameters - &#x60;filename&#x60;: The path to the wallet file that needs to be imported.  ### Example Request - &#x60;POST /z_importwallet&#x60; with payload: &#x60;&#x60;&#x60;json {     \&quot;filename\&quot;: \&quot;path/to/exportdir/nameofbackup\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object indicating the success or failure of the import operation.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;success\&quot;: true,     \&quot;message\&quot;: \&quot;Wallet imported successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the filename parameter is missing or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Ensure the path to the wallet file is correct and accessible.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filename** | **String**|  | [default to null] |

### Return type

[**ZImportWalletResponse**](../Models/ZImportWalletResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

