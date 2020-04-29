# osparc.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_health_health_get**](DefaultApi.md#service_health_health_get) | **GET** /health | Check Service Health
[**service_metadata_meta_get**](DefaultApi.md#service_metadata_meta_get) | **GET** /meta | Get Service Metadata


# **service_health_health_get**
> object service_health_health_get()

Check Service Health

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
    api_instance = osparc.DefaultApi(api_client)
    
    try:
        # Check Service Health
        api_response = api_instance.service_health_health_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->service_health_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_metadata_meta_get**
> object service_metadata_meta_get()

Get Service Metadata

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
    api_instance = osparc.DefaultApi(api_client)
    
    try:
        # Get Service Metadata
        api_response = api_instance.service_metadata_meta_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->service_metadata_meta_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

