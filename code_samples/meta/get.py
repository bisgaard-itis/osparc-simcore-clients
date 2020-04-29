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
