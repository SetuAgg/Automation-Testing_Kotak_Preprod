import pytest
import pytest_html
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()




# import pytest


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
    """
    Hooks into each test and attaches highlighted outputs to HTML reports.
    """
    # outcome = yield
    # report = outcome.get_result()

    # if report.when == "call" and report.passed:  # Highlight for passed tests
        # Simulate a verified output to highlight in the report
        # verified_output = "<b style='color: green;'>Verified Output: Test Passed!</b>"
        # report.extra = getattr(report, "extra", [])
        # report.extra.append(pytest_html.extras.html(verified_output))







