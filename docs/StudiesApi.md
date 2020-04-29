# osparc.StudiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**studies_v0_studies_get**](StudiesApi.md#studies_v0_studies_get) | **GET** /v0/studies | List Studies
[**study_v0_studies_post**](StudiesApi.md#study_v0_studies_post) | **POST** /v0/studies | Create Study
[**study_v0_studies_study_id_delete**](StudiesApi.md#study_v0_studies_study_id_delete) | **DELETE** /v0/studies/{study_id} | Delete Study
[**study_v0_studies_study_id_get**](StudiesApi.md#study_v0_studies_study_id_get) | **GET** /v0/studies/{study_id} | Get Study
[**study_v0_studies_study_id_patch**](StudiesApi.md#study_v0_studies_study_id_patch) | **PATCH** /v0/studies/{study_id} | Update Study
[**study_v0_studies_study_id_put**](StudiesApi.md#study_v0_studies_study_id_put) | **PUT** /v0/studies/{study_id} | Replace Study


# **studies_v0_studies_get**
> object studies_v0_studies_get()

List Studies

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
    api_instance = osparc.StudiesApi(api_client)
    
    try:
        # List Studies
        api_response = api_instance.studies_v0_studies_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->studies_v0_studies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **study_v0_studies_post**
> object study_v0_studies_post()

Create Study

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
    api_instance = osparc.StudiesApi(api_client)
    
    try:
        # Create Study
        api_response = api_instance.study_v0_studies_post()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->study_v0_studies_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

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

# **study_v0_studies_study_id_delete**
> object study_v0_studies_study_id_delete(study_id)

Delete Study

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
    api_instance = osparc.StudiesApi(api_client)
    study_id = 'study_id_example' # str | 

    try:
        # Delete Study
        api_response = api_instance.study_v0_studies_study_id_delete(study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->study_v0_studies_study_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_v0_studies_study_id_get**
> object study_v0_studies_study_id_get(study_id)

Get Study

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
    api_instance = osparc.StudiesApi(api_client)
    study_id = 'study_id_example' # str | 

    try:
        # Get Study
        api_response = api_instance.study_v0_studies_study_id_get(study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->study_v0_studies_study_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_v0_studies_study_id_patch**
> object study_v0_studies_study_id_patch(study_id)

Update Study

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
    api_instance = osparc.StudiesApi(api_client)
    study_id = 'study_id_example' # str | 

    try:
        # Update Study
        api_response = api_instance.study_v0_studies_study_id_patch(study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->study_v0_studies_study_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **study_v0_studies_study_id_put**
> object study_v0_studies_study_id_put(study_id)

Replace Study

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
    api_instance = osparc.StudiesApi(api_client)
    study_id = 'study_id_example' # str | 

    try:
        # Replace Study
        api_response = api_instance.study_v0_studies_study_id_put(study_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StudiesApi->study_v0_studies_study_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **study_id** | **str**|  | 

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

