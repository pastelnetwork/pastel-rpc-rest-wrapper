# TicketMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**](TicketMethodsApi.md#estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet) | **GET** /tickets/tools/estimatenftstoragefee | Estimate storage fee for NFT registration |
| [**getTotalStorageFeeTicketsToolsGettotalstoragefeePost**](TicketMethodsApi.md#getTotalStorageFeeTicketsToolsGettotalstoragefeePost) | **POST** /tickets/tools/gettotalstoragefee | Calculate Total Storage Fee for NFT Registration |
| [**listTicketsTicketsListGet**](TicketMethodsApi.md#listTicketsTicketsListGet) | **GET** /tickets/list | List tickets of a specific type |
| [**registerActionTicketTicketsRegisterActionPost**](TicketMethodsApi.md#registerActionTicketTicketsRegisterActionPost) | **POST** /tickets/register_action | Register new Action ticket |
| [**registerNftTicketTicketsRegisterNftPost**](TicketMethodsApi.md#registerNftTicketTicketsRegisterNftPost) | **POST** /tickets/register/nft | Register a new NFT ticket |
| [**registerRoyaltyTicketTicketsRegisterRoyaltyPost**](TicketMethodsApi.md#registerRoyaltyTicketTicketsRegisterRoyaltyPost) | **POST** /tickets/register_royalty | Register new change payee of the NFT royalty ticket |
| [**registerTransferTicketTicketsRegisterTransferPost**](TicketMethodsApi.md#registerTransferTicketTicketsRegisterTransferPost) | **POST** /tickets/register/transfer | Register a transfer ticket |
| [**registerUsernameTicketsRegisterUsernamePost**](TicketMethodsApi.md#registerUsernameTicketsRegisterUsernamePost) | **POST** /tickets/register/username | Register a Username Change Request ticket |
| [**ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**](TicketMethodsApi.md#ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet) | **GET** /tickets/findbylabel/{ticket_type}/{label} | Find tickets by label |
| [**ticketsFindTicketsFindGet**](TicketMethodsApi.md#ticketsFindTicketsFindGet) | **GET** /tickets/find | Find Pastel tickets |
| [**ticketsGetTicketsGetGet**](TicketMethodsApi.md#ticketsGetTicketsGetGet) | **GET** /tickets/get | Get a Pastel ticket by transaction ID |
| [**ticketsRegisterAcceptTicketsRegisterAcceptPost**](TicketMethodsApi.md#ticketsRegisterAcceptTicketsRegisterAcceptPost) | **POST** /tickets/register/accept | Register an accept ticket |
| [**ticketsRegisterCollectionTicketsRegistercollectionPost**](TicketMethodsApi.md#ticketsRegisterCollectionTicketsRegistercollectionPost) | **POST** /tickets/registercollection | Register a collection ticket |
| [**ticketsRegisterDownTicketsRegisterDownPost**](TicketMethodsApi.md#ticketsRegisterDownTicketsRegisterDownPost) | **POST** /tickets/register/down | Register a Take Down Request Ticket |
| [**ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**](TicketMethodsApi.md#ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost) | **POST** /tickets/register/ethereumaddress | Register Ethereum Address Change Request |
| [**ticketsRegisterIdTicketsRegisterIdPost**](TicketMethodsApi.md#ticketsRegisterIdTicketsRegisterIdPost) | **POST** /tickets/register_id | Register Pastel ID identity |
| [**ticketsRegisterMnidTicketsRegisterMnidPost**](TicketMethodsApi.md#ticketsRegisterMnidTicketsRegisterMnidPost) | **POST** /tickets/register/mnid | Register Masternode PastelID |
| [**ticketsRegisterOfferTicketsRegisterOfferPost**](TicketMethodsApi.md#ticketsRegisterOfferTicketsRegisterOfferPost) | **POST** /tickets/register/offer | Register an offer ticket |
| [**ticketsTicketsCommandGet**](TicketMethodsApi.md#ticketsTicketsCommandGet) | **GET** /tickets/{command} | Execute Pastel Ticket Commands |
| [**ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**](TicketMethodsApi.md#ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost) | **POST** /tickets/tools/searchthumbids | Search for NFT registration tickets and thumbnail hash |
| [**ticketsToolsTicketsToolsPost**](TicketMethodsApi.md#ticketsToolsTicketsToolsPost) | **POST** /tickets/tools | Execute various ticket tools commands |
| [**validateOwnershipTicketsToolsValidateownershipPost**](TicketMethodsApi.md#validateOwnershipTicketsToolsValidateownershipPost) | **POST** /tickets/tools/validateownership | Validate item ownership by Pastel ID |


<a name="estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet"></a>
# **estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet**
> EstimateNftStorageFeeResponse estimateNftStorageFeeTicketsToolsEstimatenftstoragefeeGet(image\_size\_in\_mb)

Estimate storage fee for NFT registration

    Estimate the storage fee for NFT registration based on the image size.   ### Description - This endpoint estimates the storage fee in PSL for NFT registration for a given image size.  ### Input Parameters - &#x60;image_size_in_mb&#x60;: The estimated size of the image in megabytes (MB).  ### Example Request - &#x60;GET /tickets/tools/estimatenftstoragefee?image_size_in_mb&#x3D;3&#x60;  ### Response - Returns a JSON object containing the estimated minimum, average, and maximum storage fees for the NFT.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;estimated_nft_storage_fee_min\&quot;: 100,     \&quot;estimated_nft_storage_fee_average\&quot;: 150,     \&quot;estimated_nft_storage_fee_max\&quot;: 200 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the image size is not provided or invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for users and applications to estimate the cost of NFT registration.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **image\_size\_in\_mb** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**EstimateNftStorageFeeResponse**](../Models/EstimateNftStorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTotalStorageFeeTicketsToolsGettotalstoragefeePost"></a>
# **getTotalStorageFeeTicketsToolsGettotalstoragefeePost**
> GetTotalStorageFeeResponse getTotalStorageFeeTicketsToolsGettotalstoragefeePost(GetTotalStorageFeeRequest)

Calculate Total Storage Fee for NFT Registration

    Calculate the total storage fee for the NFT registration ticket.  ### Description - This endpoint calculates the full storage fee for NFT registration based on the provided ticket details and image size.  ### Input Parameters - &#x60;ticket&#x60;: Base64 encoded ticket created by the creator. - &#x60;signatures&#x60;: Base64 encoded signatures and Pastel IDs of the creator and verifying masternodes. - &#x60;pastelid&#x60;: The registering masternode (MN1) Pastel ID. - &#x60;passphrase&#x60;: Passphrase for the private key associated with the Pastel ID. - &#x60;label&#x60;: Label for the ticket. - &#x60;fee&#x60;: Agreed upon storage fee. - &#x60;imagesize&#x60;: Size of the image in MB.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: \&quot;ticket-blob\&quot;,     \&quot;signatures\&quot;: \&quot;{signatures}\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;label\&quot;,     \&quot;fee\&quot;: 100,     \&quot;imagesize\&quot;: 3 } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the total storage fee for the NFT registration.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;totalstoragefee\&quot;: 500 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used during the NFT registration process to calculate the storage fee.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **GetTotalStorageFeeRequest** | [**GetTotalStorageFeeRequest**](../Models/GetTotalStorageFeeRequest.md)|  | |

### Return type

[**GetTotalStorageFeeResponse**](../Models/GetTotalStorageFeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="listTicketsTicketsListGet"></a>
# **listTicketsTicketsListGet**
> TicketsListResponse listTicketsTicketsListGet(ticket\_type, filter, min\_height)

List tickets of a specific type

    List all tickets of a specific type registered in the system.  ### Description - This endpoint allows querying different types of tickets in the Pastel network, such as PastelID, NFT, and Act tickets.  - It supports various filters to narrow down the results based on specific criteria.  ### Input Parameters - &#x60;ticket_type&#x60;: The type of ticket to list. Example: &#39;id&#39;, &#39;nft&#39;, &#39;act&#39;, etc. - &#x60;filter&#x60;: Optional filter to apply when listing tickets. Example: &#39;all&#39;, &#39;active&#39;, &#39;inactive&#39;, etc. - &#x60;min_height&#x60;: Optional minimum block height for returned tickets.  ### Example Request - &#x60;GET /tickets/list?ticket_type&#x3D;id&amp;filter&#x3D;all&amp;min_height&#x3D;250000&#x60;  ### Response - Returns a JSON object containing a list of tickets as per the requested type and filters.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {             \&quot;ticket_type\&quot;: \&quot;id\&quot;,             \&quot;ticket_details\&quot;: {...}         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The endpoint&#39;s flexibility allows for extensive querying capabilities across different ticket types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **filter** | [**Filter**](../Models/.md)|  | [optional] [default to null] |
| **min\_height** | [**Min_Height**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsListResponse**](../Models/TicketsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="registerActionTicketTicketsRegisterActionPost"></a>
# **registerActionTicketTicketsRegisterActionPost**
> ActionTicketResponse registerActionTicketTicketsRegisterActionPost(ActionTicketRequest)

Register new Action ticket

    Register a new Action ticket on the Pastel blockchain.  ### Description - This endpoint is used to register a new Action ticket, supporting action types like &#39;sense&#39; and &#39;cascade&#39;. - The ticket includes details like action type, caller PastelID, block number, and application-specific data.  ### Input Parameters - &#x60;action_ticket&#x60;: Base64 encoded Action ticket. - &#x60;signatures&#x60;: Signatures and Pastel IDs of the principal and verifying masternodes. - &#x60;pastelid&#x60;: The Pastel ID of the registering masternode. - &#x60;passphrase&#x60;: The passphrase to the private key associated with Pastel ID. - &#x60;label&#x60;: A label for the ticket. - &#x60;fee&#x60;: The storage fee. - &#x60;address&#x60;: (Optional) Pastel blockchain t-address for funding.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;action_ticket\&quot;: \&quot;&lt;encoded-ticket&gt;\&quot;,     \&quot;signatures\&quot;: \&quot;&lt;signatures-json&gt;\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj...\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;label\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns information about the registered Action ticket including transaction ID, height, and ticket details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;transaction_id\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         // Ticket details     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ActionTicketRequest** | [**ActionTicketRequest**](../Models/ActionTicketRequest.md)|  | |

### Return type

[**ActionTicketResponse**](../Models/ActionTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerNftTicketTicketsRegisterNftPost"></a>
# **registerNftTicketTicketsRegisterNftPost**
> RegisterNFTTicketResponse registerNftTicketTicketsRegisterNftPost(RegisterNFTTicketRequest)

Register a new NFT ticket

    Register a new NFT ticket in the Pastel blockchain.  ### Description - This endpoint registers a new NFT ticket on the Pastel blockchain. It requires authentication via Pastel ID and passphrase.  ### Input Parameters - &#x60;nft_ticket&#x60;: Base64 encoded NFT ticket created by the creator. - &#x60;signatures&#x60;: Signatures and Pastel IDs of the principal and verifying masternodes. - &#x60;pastelid&#x60;: The registering masternode&#39;s Pastel ID. - &#x60;passphrase&#x60;: Passphrase for the Pastel ID private key. - &#x60;label&#x60;: Label for the ticket. - &#x60;fee&#x60;: Storage fee for the NFT registration. - &#x60;address&#x60;: (Optional) Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nft_ticket\&quot;: \&quot;base64-encoded-ticket\&quot;,     \&quot;signatures\&quot;: \&quot;signatures-json\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;label\&quot;: \&quot;My NFT\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;optional-address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the transaction ID and ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;transaction-id\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;nft-reg\&quot;,         \&quot;nft_ticket\&quot;: {},         ...     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Used for registering new NFTs on the blockchain.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterNFTTicketRequest** | [**RegisterNFTTicketRequest**](../Models/RegisterNFTTicketRequest.md)|  | |

### Return type

[**RegisterNFTTicketResponse**](../Models/RegisterNFTTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerRoyaltyTicketTicketsRegisterRoyaltyPost"></a>
# **registerRoyaltyTicketTicketsRegisterRoyaltyPost**
> RegisterRoyaltyTicketResponse registerRoyaltyTicketTicketsRegisterRoyaltyPost(RegisterRoyaltyTicketRequest)

Register new change payee of the NFT royalty ticket

    Register a new change payee of the NFT royalty ticket. If successful, the method returns the transaction ID.  ### Description - This endpoint registers a new recipient for NFT royalty payments, effectively changing the payee. - It requires the transaction ID of the NFT register ticket, PastelIDs of the new and current royalty recipients, and the passphrase for the old PastelID.  ### Input Parameters - &#x60;nft_txid&#x60; (string, required): The txid of the NFT register ticket. - &#x60;new_pastelid&#x60; (string, required): The PastelID of the new royalty recipient. - &#x60;old_pastelid&#x60; (string, required): The PastelID of the current royalty recipient. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with &#39;old-pastelid&#39;. - &#x60;address&#x60; (string, optional): The Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;nft_txid\&quot;: \&quot;907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440\&quot;,     \&quot;new_pastelid\&quot;: \&quot;newPastelID123\&quot;,     \&quot;old_pastelid\&quot;: \&quot;oldPastelID456\&quot;,     \&quot;passphrase\&quot;: \&quot;yourPassphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the details of the registered NFT royalty ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;generatedTxId\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;nft-royalty\&quot;,         \&quot;version\&quot;: 1,         \&quot;pastelID\&quot;: \&quot;oldPastelID456\&quot;,         \&quot;new_pastelID\&quot;: \&quot;newPastelID123\&quot;,         \&quot;nft_txid\&quot;: \&quot;907e5e4c6fc4d14660a22afe2bdf6d27a3c8762abf0a89355bb19b7d9e7dc440\&quot;,         \&quot;signature\&quot;: \&quot;signatureString\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterRoyaltyTicketRequest** | [**RegisterRoyaltyTicketRequest**](../Models/RegisterRoyaltyTicketRequest.md)|  | |

### Return type

[**RegisterRoyaltyTicketResponse**](../Models/RegisterRoyaltyTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerTransferTicketTicketsRegisterTransferPost"></a>
# **registerTransferTicketTicketsRegisterTransferPost**
> RegisterTransferTicketResponse registerTransferTicketTicketsRegisterTransferPost(RegisterTransferTicketRequest)

Register a transfer ticket

    Register a transfer ticket in the Pastel network.  ### Description - This endpoint registers a Transfer ticket, completing the transfer of an NFT from one owner to another in a secure manner.  ### Input Parameters - &#x60;offer_txid&#x60;: The transaction ID of the Offer ticket. - &#x60;accept_txid&#x60;: The transaction ID of the Accept ticket. - &#x60;pastel_id&#x60;: The Pastel ID of the new owner. Must match the Pastel ID used to sign the Accept ticket. - &#x60;passphrase&#x60;: Passphrase of the private key associated with the new owner&#39;s Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Request JSON Format &#x60;&#x60;&#x60;json {     \&quot;offer_txid\&quot;: \&quot;offer_transaction_id\&quot;,     \&quot;accept_txid\&quot;: \&quot;accept_transaction_id\&quot;,     \&quot;pastel_id\&quot;: \&quot;new_owner_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;private_key_passphrase\&quot;,     \&quot;address\&quot;: \&quot;funding_t_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the registered transfer ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;transfer\&quot;,         \&quot;pastelID\&quot;: \&quot;new_owner_pastel_id\&quot;,         \&quot;offer_txid\&quot;: \&quot;offer_transaction_id\&quot;,         \&quot;accept_txid\&quot;: \&quot;accept_transaction_id\&quot;,         \&quot;item_txid\&quot;: \&quot;item_transaction_id\&quot;,         \&quot;registration_txid\&quot;: \&quot;registration_transaction_id\&quot;,         \&quot;signature\&quot;: \&quot;signature_value\&quot;     },     \&quot;height\&quot;: \&quot;block_height\&quot;,     \&quot;txid\&quot;: \&quot;transaction_id\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used to securely transfer ownership of NFTs within the Pastel network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterTransferTicketRequest** | [**RegisterTransferTicketRequest**](../Models/RegisterTransferTicketRequest.md)|  | |

### Return type

[**RegisterTransferTicketResponse**](../Models/RegisterTransferTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="registerUsernameTicketsRegisterUsernamePost"></a>
# **registerUsernameTicketsRegisterUsernamePost**
> RegisterUsernameResponse registerUsernameTicketsRegisterUsernamePost(RegisterUsernameRequest)

Register a Username Change Request ticket

    Register a Username Change Request ticket with the specified username and Pastel ID.  ### Description - This endpoint registers a new username change request ticket in the Pastel network. - The Pastel ID must already exist and be stored in the node.  ### Input Parameters - &#x60;username&#x60;: The username to be associated with the specified Pastel ID. - &#x60;pastel_id&#x60;: The Pastel ID with which the username is to be associated. - &#x60;passphrase&#x60;: The passphrase to access the private key associated with the Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain address to fund the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;username\&quot;: \&quot;example_user\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the username registration ticket, including the transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;username\&quot;,         \&quot;pastelID\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,         \&quot;username\&quot;: \&quot;example_user\&quot;,         \&quot;fee\&quot;: \&quot;0.01\&quot;,         \&quot;signature\&quot;: \&quot;...\&quot;     },     \&quot;height\&quot;: \&quot;123456\&quot;,     \&quot;txid\&quot;: \&quot;abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is crucial for users who wish to change their username associated with their Pastel ID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterUsernameRequest** | [**RegisterUsernameRequest**](../Models/RegisterUsernameRequest.md)|  | |

### Return type

[**RegisterUsernameResponse**](../Models/RegisterUsernameResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet"></a>
# **ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet**
> TicketsFindByLabelResponse ticketsFindByLabelTicketsFindbylabelTicketTypeLabelGet(ticket\_type, label)

Find tickets by label

    Find various types of Pastel tickets by label.  ### Description - This endpoint searches for different types of Pastel tickets (like NFT, collection, or action registration tickets) using a specific label.  ### Input Parameters - &#x60;ticket_type&#x60;: The type of ticket to search for (nft, action, collection). - &#x60;label&#x60;: The label used for ticket search.  ### Example Request - &#x60;GET /tickets/findbylabel/nft/someLabel&#x60;  ### Response - Returns a JSON object containing a list of tickets that match the given label.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {\&quot;ticket_data\&quot;: {\&quot;ticket_field1\&quot;: \&quot;value1\&quot;, \&quot;ticket_field2\&quot;: \&quot;value2\&quot;}},         {\&quot;ticket_data\&quot;: {\&quot;ticket_field1\&quot;: \&quot;value3\&quot;, \&quot;ticket_field2\&quot;: \&quot;value4\&quot;}}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the ticket type is invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this endpoint to search for tickets by their labels across different ticket types.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | **String**|  | [default to null] |
| **label** | **String**|  | [default to null] |

### Return type

[**TicketsFindByLabelResponse**](../Models/TicketsFindByLabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsFindTicketsFindGet"></a>
# **ticketsFindTicketsFindGet**
> Response_Tickets_Find_Tickets_Find_Get ticketsFindTicketsFindGet(ticket\_type, key)

Find Pastel tickets

    Find various types of Pastel tickets based on a given key.  ### Description - This endpoint searches for different types of Pastel tickets in the blockchain.  ### Input Parameters - &#x60;ticket_type&#x60;: Type of the ticket to find (e.g., &#39;id&#39;, &#39;nft&#39;, &#39;act&#39;, etc.). - &#x60;key&#x60;: The key to use for ticket search.  ### Example Request - &#x60;GET /tickets/find?ticket_type&#x3D;nft&amp;key&#x3D;exampleKey&#x60;  ### Response - Returns a JSON object or an array of objects containing the ticket data.  ### Example Response &#x60;&#x60;&#x60;json [     {         \&quot;ticket_id\&quot;: \&quot;exampleTicketId\&quot;,         \&quot;ticket_data\&quot;: {             \&quot;field1\&quot;: \&quot;value1\&quot;,             \&quot;field2\&quot;: \&quot;value2\&quot;             // ... other ticket data fields         }     }     // ... other tickets ] &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The structure and type of ticket returned depend on the ticket type being searched.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ticket\_type** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **key** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |

### Return type

[**Response_Tickets_Find_Tickets_Find_Get**](../Models/Response_Tickets_Find_Tickets_Find_Get.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsGetTicketsGetGet"></a>
# **ticketsGetTicketsGetGet**
> TicketsGetResponse ticketsGetTicketsGetGet(TicketsGetRequest)

Get a Pastel ticket by transaction ID

    Get any Pastel ticket by its transaction ID (txid).  ### Description - This endpoint retrieves a specific Pastel ticket based on its transaction ID. - It optionally decodes the ticket properties if &#39;decode_properties&#39; is set to true.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the ticket. - &#x60;decode_properties&#x60;: (Optional) Boolean flag to decode ticket properties, default is false.  ### Example Request - &#x60;GET /tickets/get?txid&#x3D;bc1c5243284272dbb22c301a549d112e8bc9bc454b5ff50b1e5f7959d6b56726&amp;decode_properties&#x3D;true&#x60;  ### Response - Returns a JSON object containing the ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;property1\&quot;: \&quot;value1\&quot;,         \&quot;property2\&quot;: \&quot;value2\&quot;,         // Other ticket properties     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsGetRequest** | [**TicketsGetRequest**](../Models/TicketsGetRequest.md)|  | |

### Return type

[**TicketsGetResponse**](../Models/TicketsGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterAcceptTicketsRegisterAcceptPost"></a>
# **ticketsRegisterAcceptTicketsRegisterAcceptPost**
> TicketsRegisterAcceptResponse ticketsRegisterAcceptTicketsRegisterAcceptPost(TicketsRegisterAcceptRequest)

Register an accept ticket

    Register an accept ticket for a specific offer on the Pastel network.  ### Description - This endpoint is used to accept an offer for a ticket on the Pastel network. - It creates an accept ticket that indicates the acceptance of an offer.  ### Input Parameters - &#x60;offer_txid&#x60;: The transaction ID of the offer ticket to accept. - &#x60;price&#x60;: The accepted price in PSL. It should be equal to or more than the asked price in the offer ticket. - &#x60;pastel_id&#x60;: The Pastel ID of the new owner. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the creator&#39;s Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;offer_txid\&quot;: \&quot;example_txid\&quot;,     \&quot;price\&quot;: 100000,     \&quot;pastel_id\&quot;: \&quot;example_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;example_passphrase\&quot;,     \&quot;address\&quot;: \&quot;example_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the ticket details, block height, and transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;accept\&quot;,         \&quot;pastelID\&quot;: \&quot;example_pastel_id\&quot;,         \&quot;offer_txid\&quot;: \&quot;example_txid\&quot;,         \&quot;price\&quot;: 100000,         \&quot;signature\&quot;: \&quot;example_signature\&quot;     },     \&quot;height\&quot;: \&quot;example_height\&quot;,     \&quot;txid\&quot;: \&quot;example_txid\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterAcceptRequest** | [**TicketsRegisterAcceptRequest**](../Models/TicketsRegisterAcceptRequest.md)|  | |

### Return type

[**TicketsRegisterAcceptResponse**](../Models/TicketsRegisterAcceptResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterCollectionTicketsRegistercollectionPost"></a>
# **ticketsRegisterCollectionTicketsRegistercollectionPost**
> RegisterCollectionTicketResponse ticketsRegisterCollectionTicketsRegistercollectionPost(RegisterCollectionTicketRequest)

Register a collection ticket

    Register a new collection ticket on the Pastel blockchain.  ### Description - This endpoint is used for registering a new collection ticket, representing a collection of NFTs on the Pastel blockchain. - The ticket includes collection details like name, creator, authorized contributors, and metadata.  ### Input Parameters - &#x60;collection_ticket&#x60;: Base64 encoded collection ticket. - &#x60;signatures&#x60;: Signatures and Pastel IDs of principal and verifying masternodes. - &#x60;pastelid&#x60;: The Pastel ID of the registering masternode (MN1). - &#x60;passphrase&#x60;: Passphrase for the private key associated with PastelID. - &#x60;label&#x60;: A label for the ticket. - &#x60;fee&#x60;: Storage fee for registering the ticket. - &#x60;address&#x60;: (Optional) Pastel blockchain address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;collection_ticket\&quot;: \&quot;Base64EncodedTicket\&quot;,     \&quot;signatures\&quot;: {         \&quot;principal\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;},         \&quot;mn2\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;},         \&quot;mn3\&quot;: {\&quot;PastelID\&quot;: \&quot;Signature\&quot;}     },     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;yourPassphrase\&quot;,     \&quot;label\&quot;: \&quot;MyCollection\&quot;,     \&quot;fee\&quot;: 100,     \&quot;address\&quot;: \&quot;OptionalAddress\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns details of the registered collection ticket including transaction ID, height, and ticket information.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;TransactionId\&quot;,     \&quot;height\&quot;: 123456,     \&quot;ticket\&quot;: {         ... // Detailed ticket information     },     ... // Other fields } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **RegisterCollectionTicketRequest** | [**RegisterCollectionTicketRequest**](../Models/RegisterCollectionTicketRequest.md)|  | |

### Return type

[**RegisterCollectionTicketResponse**](../Models/RegisterCollectionTicketResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterDownTicketsRegisterDownPost"></a>
# **ticketsRegisterDownTicketsRegisterDownPost**
> TicketsRegisterDownResponse ticketsRegisterDownTicketsRegisterDownPost(txid, pastelid, passphrase, address)

Register a Take Down Request Ticket

    Register a take down request ticket in the Pastel Network.  ### Description - This endpoint registers a take down request ticket, which is a request to take down a piece of content. It returns the transaction ID if successful.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID. - &#x60;pastelid&#x60;: The Pastel ID. Note: Pastel ID must be generated and stored inside the node. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the Pastel ID. - &#x60;address&#x60;: (Optional) The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;pastelid\&quot;: \&quot;your_pastel_id\&quot;,     \&quot;passphrase\&quot;: \&quot;your_passphrase\&quot;,     \&quot;address\&quot;: \&quot;optional_pastel_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the details of the registered take down request ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;your_pastel_id\&quot;,         \&quot;timeStamp\&quot;: \&quot;timestamp\&quot;,         \&quot;signature\&quot;: \&quot;signature\&quot;     },     \&quot;height\&quot;: \&quot;block_height\&quot;,     \&quot;txid\&quot;: \&quot;transaction_id\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is used for registering take down requests in the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **txid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **address** | [**Address**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsRegisterDownResponse**](../Models/TicketsRegisterDownResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost"></a>
# **ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost**
> TicketsRegisterEthereumAddressResponse ticketsRegisterEthereumAddressTicketsRegisterEthereumaddressPost(TicketsRegisterEthereumAddressRequest)

Register Ethereum Address Change Request

    Register an Ethereum Address Change Request ticket.  ### Description - This endpoint registers a change of Ethereum address associated with a given Pastel ID.  ### Input Parameters - &#x60;ethereum_address&#x60;: The Ethereum address to be mapped with the Pastel ID. - &#x60;pastel_id&#x60;: The Pastel ID. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the Pastel ID. - &#x60;address&#x60; (optional): The Pastel blockchain t-address for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;ethereum_address\&quot;: \&quot;0x863c30dd122a21f815e46ec510777fd3e3398c26\&quot;,     \&quot;pastel_id\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;optional_t_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the details of the registered Ethereum address change request.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;ethereumAddress\&quot;,         \&quot;pastelID\&quot;: \&quot;jXYqZNPj...\&quot;,         \&quot;ethereumAddress\&quot;: \&quot;0x863c30d...\&quot;,         \&quot;fee\&quot;: \&quot;0.1\&quot;,         \&quot;signature\&quot;: \&quot;...\&quot;     },     \&quot;height\&quot;: \&quot;123456\&quot;,     \&quot;txid\&quot;: \&quot;xyz123abc...\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if input parameters are incorrect. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterEthereumAddressRequest** | [**TicketsRegisterEthereumAddressRequest**](../Models/TicketsRegisterEthereumAddressRequest.md)|  | |

### Return type

[**TicketsRegisterEthereumAddressResponse**](../Models/TicketsRegisterEthereumAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterIdTicketsRegisterIdPost"></a>
# **ticketsRegisterIdTicketsRegisterIdPost**
> TicketsRegisterIdResponse ticketsRegisterIdTicketsRegisterIdPost(TicketsRegisterIdRequest)

Register Pastel ID identity

    Register a Pastel ID identity on the Pastel blockchain.  ### Description - This endpoint is used to register a new Pastel ID identity. - The Pastel ID must be pre-generated and stored inside the node.  ### Input Parameters - &#x60;pastelid&#x60; (string, required): The Pastel ID. The Pastel ID must be generated and stored inside the node. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with the Pastel ID and stored inside the node. - &#x60;address&#x60; (string, required): The Pastel blockchain t-address to use for funding the transaction.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;tPmjPqWdUXD68JBTWYBTtqeCDwdFwwRjikg\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the transaction ID and other details of the registered Pastel ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;jXaShWhN...\&quot;,         \&quot;address\&quot;: \&quot;tPmjPqWdUXD68...\&quot;,         \&quot;timeStamp\&quot;: \&quot;2021-04-25T15:30:00\&quot;,         \&quot;signature\&quot;: \&quot;HwMv...&#x3D;\&quot;     },     \&quot;height\&quot;: \&quot;100000\&quot;,     \&quot;txid\&quot;: \&quot;3a1b2c3d4e5f6789a0b1c2d3e4f5a678b9c0d1e2f3a4b5c6d7e8f9g0h1i2j3k4\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterIdRequest** | [**TicketsRegisterIdRequest**](../Models/TicketsRegisterIdRequest.md)|  | |

### Return type

[**TicketsRegisterIdResponse**](../Models/TicketsRegisterIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsRegisterMnidTicketsRegisterMnidPost"></a>
# **ticketsRegisterMnidTicketsRegisterMnidPost**
> TicketsRegisterMnidResponse ticketsRegisterMnidTicketsRegisterMnidPost(pastelid, passphrase, address)

Register Masternode PastelID

    Register the identity of the current Masternode into the blockchain.   ### Description - This endpoint registers the PastelID of the Masternode on the blockchain. It requires an active Masternode.  ### Input Parameters - &#x60;pastelid&#x60;: The PastelID to register. The PastelID must be generated and stored inside the node. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the PastelID. - &#x60;address&#x60; (optional): The Pastel blockchain t-address to use for funding the registration.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;pastelid\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot;,     \&quot;address\&quot;: \&quot;P_address\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the registration details of the Masternode PastelID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;pastelid\&quot;,         \&quot;pastelID\&quot;: \&quot;jXaShWhNtatHVPWRNPsvjoVHUYes2kA7T9EJVL9i9EKPdBNo5aTYp19niWemJb2EwgYYR68jymULPtmHdETf8M\&quot;,         \&quot;address\&quot;: \&quot;P_address\&quot;,         \&quot;outpoint\&quot;: \&quot;\&quot;,         \&quot;timeStamp\&quot;: \&quot;\&quot;,         \&quot;signature\&quot;: \&quot;\&quot;     },     \&quot;height\&quot;: \&quot;12345\&quot;,     \&quot;txid\&quot;: \&quot;abcd1234\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Only active Masternodes can register their PastelID.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **pastelid** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **passphrase** | [**oas_any_type_not_mapped**](../Models/.md)|  | [default to null] |
| **address** | [**Address**](../Models/.md)|  | [optional] [default to null] |

### Return type

[**TicketsRegisterMnidResponse**](../Models/TicketsRegisterMnidResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsRegisterOfferTicketsRegisterOfferPost"></a>
# **ticketsRegisterOfferTicketsRegisterOfferPost**
> TicketsRegisterOfferResponse ticketsRegisterOfferTicketsRegisterOfferPost(TicketsRegisterOfferRequest)

Register an offer ticket

    Register an offer ticket in the Pastel network.  ### Description - Registers an offer ticket on the Pastel network. This is used for offering an NFT for sale, either as the original creator or as the current owner if the NFT has been transferred.  ### Input Parameters - &#x60;txid&#x60;: The transaction ID of the ticket to offer. This is either the NFT Activation ticket (if the current owner is the original creator) or a Transfer ticket (if the current owner is not the original creator). - &#x60;price&#x60;: The offer price in PSL. - &#x60;pastel_id&#x60;: The Pastel ID of the current owner. This must be the same Pastel ID used to sign the ticket referred to by &#x60;txid&#x60;. - &#x60;passphrase&#x60;: The passphrase to the private key associated with the creator&#39;s Pastel ID. - &#x60;valid_after&#x60;: (Optional) The block height after which this offer ticket will become active. - &#x60;valid_before&#x60;: (Optional) The block height after which this offer ticket is no longer valid. - &#x60;copy_number&#x60;: (Optional) If present, will replace the original not yet accepted Offer ticket with this copy number. - &#x60;address&#x60;: (Optional) The Pastel blockchain address to use for funding the registration. - &#x60;intended_for&#x60;: (Optional) The Pastel ID of the intended recipient of the offer.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;txid\&quot;: \&quot;txid_value\&quot;,     \&quot;price\&quot;: 100000,     \&quot;pastel_id\&quot;: \&quot;pastel_id_value\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase_value\&quot;,     \&quot;valid_after\&quot;: 0,     \&quot;valid_before\&quot;: 0,     \&quot;copy_number\&quot;: 0,     \&quot;address\&quot;: \&quot;address_value\&quot;,     \&quot;intended_for\&quot;: \&quot;intended_for_value\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing details of the registered offer ticket.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;ticket\&quot;: {         \&quot;type\&quot;: \&quot;offer\&quot;,         \&quot;pastelID\&quot;: \&quot;pastel_id_value\&quot;,         \&quot;txid\&quot;: \&quot;txid_value\&quot;,         \&quot;copy_number\&quot;: \&quot;0\&quot;,         \&quot;asked_price\&quot;: \&quot;100000\&quot;,         \&quot;valid_after\&quot;: \&quot;0\&quot;,         \&quot;valid_before\&quot;: \&quot;0\&quot;,         \&quot;signature\&quot;: \&quot;signature_value\&quot;     },     \&quot;height\&quot;: \&quot;block_height_value\&quot;,     \&quot;txid\&quot;: \&quot;txid_value\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the input parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsRegisterOfferRequest** | [**TicketsRegisterOfferRequest**](../Models/TicketsRegisterOfferRequest.md)|  | |

### Return type

[**TicketsRegisterOfferResponse**](../Models/TicketsRegisterOfferResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsTicketsCommandGet"></a>
# **ticketsTicketsCommandGet**
> TicketsResponse ticketsTicketsCommandGet(command)

Execute Pastel Ticket Commands

    Execute various commands related to Pastel tickets.  ### Description - This endpoint allows for the execution of various commands related to Pastel tickets such as registering, activating, finding, listing, and getting tickets.  ### Input Parameters - &#x60;command&#x60;: The Pastel ticket command to execute. Available commands include register, activate, find, findbylabel, list, get, and tools.  ### Example Request - &#x60;GET /tickets/register&#x60;  ### Response - Returns the result of the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Result of the executed command\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the command is not recognized. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The functionality of this endpoint depends on the specific command executed.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **command** | **String**|  | [default to null] |

### Return type

[**TicketsResponse**](../Models/TicketsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost"></a>
# **ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost**
> TicketSearchThumbIdsResponse ticketsToolsSearchthumbidsTicketsToolsSearchthumbidsPost(TicketSearchThumbIdsRequest)

Search for NFT registration tickets and thumbnail hash

    Search for the NFT registration tickets and thumbnail_hash using filters defined by the search_json parameter (Base64-encoded).  ### Description - This endpoint allows searching for NFT registration tickets and associated thumbnail hashes based on various criteria. - The search criteria are provided as a Base64-encoded JSON string.  ### Input Parameters - &#x60;search_json_base64&#x60;: A Base64-encoded JSON string defining the search criteria. The JSON structure includes fields like &#39;creator&#39;, &#39;blocks&#39;, &#39;copies&#39;, &#39;rareness_score&#39;, &#39;nsfw_score&#39;, and &#39;fuzzy&#39; for fuzzy searches.  ### Example Request - &#x60;POST /tickets/tools/searchthumbids&#x60; with JSON body:   &#x60;&#x60;&#x60;json   {       \&quot;search_json_base64\&quot;: \&quot;eyJjcmVhdG9yIjogIm1pbmUiLCAiYmxvY2tzIjogWzIwMDAwLDMwMDAwXSwgImNvcGllcyI6IFswLDJdfQ&#x3D;&#x3D;\&quot;   }   &#x60;&#x60;&#x60;  ### Response - Returns a JSON array of objects with NFT registration ticket \&quot;txid\&quot; and thumbnail hash.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;tickets\&quot;: [         {\&quot;txid\&quot;: \&quot;txid_1\&quot;, \&quot;thumbnail_hash\&quot;: \&quot;thumbnail_hash_1\&quot;},         {\&quot;txid\&quot;: \&quot;txid_2\&quot;, \&quot;thumbnail_hash\&quot;: \&quot;thumbnail_hash_2\&quot;}     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid or if the Base64 decoding fails. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketSearchThumbIdsRequest** | [**TicketSearchThumbIdsRequest**](../Models/TicketSearchThumbIdsRequest.md)|  | |

### Return type

[**TicketSearchThumbIdsResponse**](../Models/TicketSearchThumbIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="ticketsToolsTicketsToolsPost"></a>
# **ticketsToolsTicketsToolsPost**
> TicketsToolsResponse ticketsToolsTicketsToolsPost(TicketsToolsRequest)

Execute various ticket tools commands

    Execute a set of Pastel ticket tools commands.  ### Description - This endpoint provides a variety of tools related to Pastel tickets, enabling operations like printing trading chains, getting registration tickets by transfer txid, validating usernames and ethereum addresses, and more.  ### Input Parameters - &#x60;command&#x60; (str, required): The command to be executed. - &#x60;additional_params&#x60; (List[str], optional): Additional parameters required for specific commands.  ### Example Request - &#x60;POST /tickets/tools&#x60; with JSON body: &#x60;&#x60;&#x60;json {     \&quot;command\&quot;: \&quot;printtradingchain\&quot;,     \&quot;additional_params\&quot;: [\&quot;param1\&quot;, \&quot;param2\&quot;] } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object containing the result of the executed command.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: {         \&quot;key\&quot;: \&quot;value\&quot;     } } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - The specific output and required additional parameters depend on the command executed.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **TicketsToolsRequest** | [**TicketsToolsRequest**](../Models/TicketsToolsRequest.md)|  | |

### Return type

[**TicketsToolsResponse**](../Models/TicketsToolsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="validateOwnershipTicketsToolsValidateownershipPost"></a>
# **validateOwnershipTicketsToolsValidateownershipPost**
> ValidateOwnershipResponse validateOwnershipTicketsToolsValidateownershipPost(ValidateOwnershipRequest)

Validate item ownership by Pastel ID

    Validate item ownership by Pastel ID.  ### Description - This endpoint checks whether the given Pastel ID is the owner of a specified item. - It returns details of the item, including the type, ownership status, item transaction ID, and transfer ticket transaction ID.  ### Input Parameters - &#x60;item_txid&#x60; (string, required): The transaction ID of the original NFT registration. - &#x60;pastelid&#x60; (string, required): The registered Pastel ID supposed to own the item. - &#x60;passphrase&#x60; (string, required): The passphrase to the private key associated with the Pastel ID.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;item_txid\&quot;: \&quot;e4ee20e436d33f59cc313647bacff0c5b0df5b7b1c1fa13189ea7bc8b9df15a4\&quot;,     \&quot;pastelid\&quot;: \&quot;jXYqZNPj21RVnwxnEJ654wEdzi7GZTZ5LAdiotBmPrF7pDMkpX1JegDMQZX55WZLkvy9fxNpZcbBJuE8QYUqBF\&quot;,     \&quot;passphrase\&quot;: \&quot;passphrase\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a JSON object with the item type, ownership status, item transaction ID, and transfer ticket transaction ID.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;type\&quot;: \&quot;unknown\&quot;,     \&quot;owns\&quot;: false,     \&quot;txid\&quot;: \&quot;\&quot;,     \&quot;transfer\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This method is critical for confirming ownership of NFTs and other registered items on the Pastel Network.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ValidateOwnershipRequest** | [**ValidateOwnershipRequest**](../Models/ValidateOwnershipRequest.md)|  | |

### Return type

[**ValidateOwnershipResponse**](../Models/ValidateOwnershipResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

