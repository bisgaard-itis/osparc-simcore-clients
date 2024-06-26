# pylint: disable=redefined-outer-name
# pylint: disable=unused-argument
# pylint: disable=unused-variable
# pylint: disable=too-many-arguments

import datetime
import os

import pytest

# Dictionary to store start times of tests
_test_start_times = {}


def _utc_now():
    return datetime.datetime.now(tz=datetime.timezone.utc)


def _construct_graylog_url(api_host, start_time, end_time):
    """
    Construct a Graylog URL for the given time interval.
    """
    base_url = api_host.replace("api.", "monitoring.", 1).rstrip("/")
    url = f"{base_url}/graylog/search"
    start_time_str = start_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    end_time_str = end_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    query = f"from={start_time_str}&to={end_time_str}"
    return f"{url}?{query}"


def pytest_runtest_setup(item):
    """
    Hook to capture the start time of each test.
    """
    _test_start_times[item.name] = _utc_now()


def pytest_runtest_makereport(item, call):
    """
    Hook to add extra information when a test fails.
    """
    if call.when == "call":

        # Check if the test failed
        if call.excinfo is not None:
            test_name = item.name
            test_location = item.location
            api_host = os.environ.get("OSPARC_API_HOST", "")

            diagnostics = {
                "test_name": test_name,
                "test_location": test_location,
                "api_host": api_host,
            }

            # Get the start and end times of the test
            start_time = _test_start_times.get(test_name)
            end_time = _utc_now()

            if start_time:
                diagnostics["graylog_url"] = _construct_graylog_url(
                    api_host, start_time, end_time
                )

            # Print the diagnostics
            print(f"\nDiagnostics for {test_name}:")
            for key, value in diagnostics.items():
                print("  ", key, ":", value)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.pluginmanager.register(pytest_runtest_setup, "osparc_test_times_plugin")
    config.pluginmanager.register(pytest_runtest_makereport, "osparc_makereport_plugin")
