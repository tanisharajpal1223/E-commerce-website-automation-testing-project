import pytest
import os
from datetime import datetime
from Utils.driver import get_driver

@pytest.fixture
def driver(request):
    driver = get_driver()
    driver.get("https://tutorialsninja.com/demo/")

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        if not os.path.exists("reports"):
            os.makedirs("reports")

        file_name = f"reports/fail_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        driver.save_screenshot(file_name)

    driver.quit()


# Hook to detect test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)