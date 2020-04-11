import os
import sys
import argparse
import pytest
import bpy

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
    args = parser.parse_args(argv)
    return args.test


def main():
    addon_helper.install_addon(ADDON)
    test = parse_cli()
    if test:
        pytest.main(["tests", "-v", "-x"])


if __name__ == '__main__':
    main()
