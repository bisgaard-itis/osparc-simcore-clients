# osparc.TokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**for_access_token_v0_token_post**](TokenApi.md#for_access_token_v0_token_post) | **POST** /v0/token | Login For Access Token


# **for_access_token_v0_token_post**
> Token for_access_token_v0_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Login For Access Token

Returns an access-token provided a valid authorization grant

### Example

```python
from __future__ import print_function
import time
import osparc
from osparc.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with osparc.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = osparc.TokenApi(api_client)
    username = 'username_example' # str | 
password = 'password_example' # str | 
grant_type = 'grant_type_example' # str |  (optional)
scope = '' # str |  (optional) (default to '')
client_id = 'client_id_example' # str |  (optional)
client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Login For Access Token
        api_response = api_instance.for_access_token_v0_token_post(username, password, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TokenApi->for_access_token_v0_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

