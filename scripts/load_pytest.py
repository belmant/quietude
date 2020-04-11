import pytest
import sys
import os


ADDON = "quietude"

try:
    sys.path.append(os.environ["LOCAL_PYTHONPATH"])
    import addon_helper
except Exception as e:
    print(e)
    sys.exit(1)


class SetupPlugin:
    def __init__(self, addon_name):
        self.addon_name = addon_name

    def pytest_configure(self, config):
        addon_helper.install_addon(self.addon_name)

    def pytest_unconfigure(self):
        #         cmd = "coverage xml"
        #         os.system(cmd)
        addon_location = addon_helper.get_addon_location(self.addon_name)
        addon_helper.disable(self.addon_name)


try:
    exit_val = pytest.main(["tests", "-v", "-x", "--cov", "--cov-report", "term-missing", "--cov-report", "xml", ], plugins=[SetupPlugin(ADDON)])
except Exception as e:
    print(e)
    exit_val = 1
sys.exit(exit_val)
