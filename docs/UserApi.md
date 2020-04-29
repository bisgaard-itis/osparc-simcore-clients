# osparc.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**my_profile_v0_user_get**](UserApi.md#my_profile_v0_user_get) | **GET** /v0/user | Get My Profile
[**my_profile_v0_user_patch**](UserApi.md#my_profile_v0_user_patch) | **PATCH** /v0/user | Update My Profile


# **my_profile_v0_user_get**
> User my_profile_v0_user_get()

Get My Profile

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
from __future__ import print_function
import time
import osparc
from osparc.rest import ApiException
from pprint import pprint
configuration = osparc.Configuration()
# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with osparc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = osparc.UserApi(api_client)
    
    try:
        # Get My Profile
        api_response = api_instance.my_profile_v0_user_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->my_profile_v0_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **my_profile_v0_user_patch**
> User my_profile_v0_user_patch()

Update My Profile

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
from __future__ import print_function
import time
import osparc
from osparc.rest import ApiException
from pprint import pprint
configuration = osparc.Configuration()
# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Enter a context with an instance of the API client
with osparc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = osparc.UserApi(api_client)
    
    try:
        # Update My Profile
        api_response = api_instance.my_profile_v0_user_patch()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->my_profile_v0_user_patch: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

