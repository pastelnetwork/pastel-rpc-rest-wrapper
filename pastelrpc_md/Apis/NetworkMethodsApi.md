# NetworkMethodsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNodeAddnodePost**](NetworkMethodsApi.md#addNodeAddnodePost) | **POST** /addnode | Add, remove, or try a connection to a node |
| [**getAddedNodeInfoGetaddednodeinfoGet**](NetworkMethodsApi.md#getAddedNodeInfoGetaddednodeinfoGet) | **GET** /getaddednodeinfo | Get information about added nodes |
| [**getConnectionCountGetconnectioncountGet**](NetworkMethodsApi.md#getConnectionCountGetconnectioncountGet) | **GET** /getconnectioncount | Get the number of connections to other nodes |
| [**getNetTotalsGetnettotalsGet**](NetworkMethodsApi.md#getNetTotalsGetnettotalsGet) | **GET** /getnettotals | Get network traffic information |
| [**getNetworkInfoGetnetworkinfoGet**](NetworkMethodsApi.md#getNetworkInfoGetnetworkinfoGet) | **GET** /getnetworkinfo | Get various state info regarding P2P networking |
| [**getNetworksInfoGetnetworksinfoGet**](NetworkMethodsApi.md#getNetworksInfoGetnetworksinfoGet) | **GET** /getnetworksinfo | Get information about all the networks |
| [**getPeerInfoGetpeerinfoGet**](NetworkMethodsApi.md#getPeerInfoGetpeerinfoGet) | **GET** /getpeerinfo | Get data about each connected network node |
| [**listBannedListbannedGet**](NetworkMethodsApi.md#listBannedListbannedGet) | **GET** /listbanned | List all banned IPs/Subnets |


<a name="addNodeAddnodePost"></a>
# **addNodeAddnodePost**
> AddNodeResponse addNodeAddnodePost(AddNodeRequest)

Add, remove, or try a connection to a node

    Attempt to add or remove a node from the addnode list, or try a connection to a node once.  ### Description - This endpoint manages nodes in the addnode list. It can add a node to the list, remove a node from the list, or try a connection to a node once. - The &#39;node&#39; parameter specifies the node (IP address and port), and the &#39;command&#39; parameter specifies the action to be taken (&#39;add&#39;, &#39;remove&#39;, or &#39;onetry&#39;).  ### Input Parameters - &#x60;node&#x60; (string, required): The node&#39;s address in the format &#x60;IP:port&#x60;. - &#x60;command&#x60; (string, required): The command to execute, which can be &#39;add&#39;, &#39;remove&#39;, or &#39;onetry&#39;.  ### Example Request &#x60;&#x60;&#x60;json {     \&quot;node\&quot;: \&quot;192.168.0.6:9933\&quot;,     \&quot;command\&quot;: \&quot;onetry\&quot; } &#x60;&#x60;&#x60;  ### Response - Returns a success message or null if the command is executed successfully.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;result\&quot;: \&quot;Node added successfully\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Use this method cautiously as it can modify the node&#39;s peer connections.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **AddNodeRequest** | [**AddNodeRequest**](../Models/AddNodeRequest.md)|  | |

### Return type

[**AddNodeResponse**](../Models/AddNodeResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="getAddedNodeInfoGetaddednodeinfoGet"></a>
# **getAddedNodeInfoGetaddednodeinfoGet**
> GetAddedNodeInfoResponse getAddedNodeInfoGetaddednodeinfoGet(dns, node)

Get information about added nodes

    Get information about the given added node or all added nodes.  ### Description - This endpoint returns information about nodes that have been added using the &#x60;addnode&#x60; RPC command.  - It can return information about all added nodes or a specific node, if specified.  ### Input Parameters - &#x60;dns&#x60;: A boolean value indicating whether detailed information is required. - &#x60;node&#x60;: (Optional) The specific node to get information about.  ### Example Request - &#x60;GET /getaddednodeinfo?dns&#x3D;true&amp;node&#x3D;192.168.0.201&#x60;  ### Response - Returns a JSON object containing information about added nodes.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;nodes\&quot;: [         {             \&quot;addednode\&quot;: \&quot;192.168.0.201\&quot;,             \&quot;connected\&quot;: true,             \&quot;addresses\&quot;: [                 {                     \&quot;address\&quot;: \&quot;192.168.0.201:9933\&quot;,                     \&quot;connected\&quot;: \&quot;outbound\&quot;                 }             ]         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 400: Bad Request if the parameters are invalid. - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **dns** | **Boolean**|  | [default to null] |
| **node** | **String**|  | [optional] [default to null] |

### Return type

[**GetAddedNodeInfoResponse**](../Models/GetAddedNodeInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getConnectionCountGetconnectioncountGet"></a>
# **getConnectionCountGetconnectioncountGet**
> GetConnectionCountResponse getConnectionCountGetconnectioncountGet()

Get the number of connections to other nodes

    Get the number of connections to other nodes in the Pastel network.  ### Description - This endpoint returns the total number of connections that the node has to other nodes in the network. It&#39;s an indicator of the node&#39;s connectivity and participation in the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getconnectioncount&#x60;  ### Response - Returns a JSON object containing the total number of connections.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;connection_count\&quot;: 15 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and monitoring the node&#39;s network activity.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConnectionCountResponse**](../Models/GetConnectionCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetTotalsGetnettotalsGet"></a>
# **getNetTotalsGetnettotalsGet**
> GetNetTotalsResponse getNetTotalsGetnettotalsGet()

Get network traffic information

    Get information about network traffic, including total bytes received, total bytes sent, and current time.  ### Description - This endpoint returns statistics about the network traffic, including the total number of bytes received and sent by the node since startup, as well as the current time in milliseconds.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnettotals&#x60;  ### Response - Returns a JSON object containing the network traffic statistics.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;totalbytesrecv\&quot;: 123456,     \&quot;totalbytessent\&quot;: 654321,     \&quot;timemillis\&quot;: 1627891234567 } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for monitoring and diagnostics of the node&#39;s network activity.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetTotalsResponse**](../Models/GetNetTotalsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetworkInfoGetnetworkinfoGet"></a>
# **getNetworkInfoGetnetworkinfoGet**
> GetNetworkInfoResponse getNetworkInfoGetnetworkinfoGet()

Get various state info regarding P2P networking

    Get an object containing various state information regarding P2P networking.  ### Description - This endpoint returns an object containing various state information regarding the P2P networking of the Pastel node. - It provides details like server version, protocol version, connections, and network information.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnetworkinfo&#x60;  ### Response - Returns a JSON object containing various state info regarding P2P networking.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;version\&quot;: 5000000,     \&quot;subversion\&quot;: \&quot;/MagicBean:5.0.0[-v]/\&quot;,     \&quot;protocolversion\&quot;: 170013,     \&quot;localservices\&quot;: \&quot;000000000000040d\&quot;,     \&quot;timeoffset\&quot;: 0,     \&quot;connections\&quot;: 10,     \&quot;networks\&quot;: [         {             \&quot;name\&quot;: \&quot;ipv4\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;\&quot;         }     ],     \&quot;relayfee\&quot;: 0.00001000,     \&quot;localaddresses\&quot;: [         {             \&quot;address\&quot;: \&quot;123.45.67.89\&quot;,             \&quot;port\&quot;: 8333,             \&quot;score\&quot;: 1         }     ],     \&quot;warnings\&quot;: \&quot;\&quot; } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkInfoResponse**](../Models/GetNetworkInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getNetworksInfoGetnetworksinfoGet"></a>
# **getNetworksInfoGetnetworksinfoGet**
> GetNetworksInfoResponse getNetworksInfoGetnetworksinfoGet()

Get information about all the networks

    Get detailed information about all the networks known to the node.  ### Description - This endpoint provides information about each network that the node is aware of. It includes details like the network&#39;s name, its accessibility status, and any associated proxy settings.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getnetworksinfo&#x60;  ### Response - Returns a JSON array of objects, each representing a network with its specific details.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;networks\&quot;: [         {             \&quot;name\&quot;: \&quot;ipv4\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;192.168.1.1:9050\&quot;,             \&quot;proxy_randomize_credentials\&quot;: true         },         {             \&quot;name\&quot;: \&quot;ipv6\&quot;,             \&quot;limited\&quot;: false,             \&quot;reachable\&quot;: true,             \&quot;proxy\&quot;: \&quot;\&quot;,             \&quot;proxy_randomize_credentials\&quot;: false         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for network diagnostics and for understanding the node&#39;s perspective of the network topology.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworksInfoResponse**](../Models/GetNetworksInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getPeerInfoGetpeerinfoGet"></a>
# **getPeerInfoGetpeerinfoGet**
> GetPeerInfoResponse getPeerInfoGetpeerinfoGet()

Get data about each connected network node

    Get data about each connected network node as a json array of objects.  ### Description - This endpoint returns detailed information about each peer connected to the Pastel network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /getpeerinfo&#x60;  ### Response - Returns a JSON array containing information about each connected network node.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;peers\&quot;: [         {             \&quot;id\&quot;: 1,             \&quot;addr\&quot;: \&quot;host:port\&quot;,             \&quot;addrlocal\&quot;: \&quot;ip:port\&quot;,             \&quot;services\&quot;: \&quot;xxxxxxxxxxxxxxxx\&quot;,             \&quot;lastsend\&quot;: 1617704837,             \&quot;lastrecv\&quot;: 1617704837,             ...         },         ...     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - Useful for network diagnostics and analysis.

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPeerInfoResponse**](../Models/GetPeerInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listBannedListbannedGet"></a>
# **listBannedListbannedGet**
> ListBannedResponse listBannedListbannedGet()

List all banned IPs/Subnets

    List all banned IPs/Subnets in the network.  ### Description - This endpoint retrieves a list of all IP addresses and subnets that have been banned from the network.  ### Input Parameters - None: This endpoint does not require any input parameters.  ### Example Request - &#x60;GET /listbanned&#x60;  ### Response - Returns a JSON array of objects, each containing the banned address and the timestamp until which it is banned.  ### Example Response &#x60;&#x60;&#x60;json {     \&quot;banned_addresses\&quot;: [         {             \&quot;address\&quot;: \&quot;192.168.1.0/24\&quot;,             \&quot;banned_until\&quot;: 1625097600         },         {             \&quot;address\&quot;: \&quot;10.0.0.5\&quot;,             \&quot;banned_until\&quot;: 1625098000         }     ] } &#x60;&#x60;&#x60;  ### Possible Errors - HTTP 500: Internal Server Error if there&#39;s an issue in processing the request.  ### Note - This endpoint is useful for network administrators and developers to audit and manage network access.

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListBannedResponse**](../Models/ListBannedResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

