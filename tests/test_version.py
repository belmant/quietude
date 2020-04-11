import pytest
from addon_helper import get_version

ADDON = 'quietude'


def test_versionID_pass():
    expect_version = (0, 0, 1)
    return_version = get_version(ADDON)
    assert expect_version == return_version
