import os
import sys
import argparse
import pytest
import shutil
from pathlib import Path

try:
    sys.path.append(os.environ["LOCAL_PYTHONPATH"])
    import addon_helper
except Exception as e:
    print(e)
    sys.exit(1)

ADDON = "quietude"


def parse_cli():
    argv = sys.argv
    if "--" not in argv:
        argv = []
    else:
        argv = argv[argv.index("--") + 1:]  # get all args after "--"
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action='store_true', help="Only runs tests with pytest.")
    parser.add_argument('--install', action='store_true', help="Installs the addon (zips it and imports it from within Blender).")
    parser.add_argument('--bversion', type=str, default='2.82', help="Blender version.")
    args = parser.parse_args(argv)
    return args.test, args.bversion, args.install


def run_pytest():
    try:
        exit_val = pytest.main(["tests", "-v"])
    except Exception as e:
        print(e)
        exit_val = 1
    sys.exit(exit_val)


def main():
    test, blender_version, install = parse_cli()
    # remove_addon(blender_version)
    if install :
        path = addon_helper.get_addon_path(ADDON)
        if path.exists():
            print(f"Removing addon {ADDON}.")
            shutil.rmtree(path)
        print(f"Installing addon {ADDON}.")
        addon_helper.install_addon(ADDON)
    if test:
        run_pytest()


if __name__ == '__main__':
    main()
