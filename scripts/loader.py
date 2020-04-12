import os
import sys
import argparse
import pytest

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


def run_pytest():
    try:
        exit_val = pytest.main(["tests", "-v"])
    except Exception as e:
        print(e)
        exit_val = 1
    sys.exit(exit_val)


def main():
    addon_helper.install_addon(ADDON)
    test = parse_cli()
    if test:
        run_pytest()


if __name__ == '__main__':
    main()
