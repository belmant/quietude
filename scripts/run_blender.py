import argparse
import os
import sys
import subprocess
import re
from glob import glob

test_file = "scripts/load_pytest.py"


def main(blender, blender_flags, test_flag=''):
    local_python = os.path.join(os.getcwd(), "scripts")
    os.environ["LOCAL_PYTHONPATH"] = local_python

    cmd = f".{os.sep}{blender} {test_flag}{''.join(blender_flags)}"
    print(cmd)
    result = int(os.system(cmd))
    if 0 == result:
        return 0
    else:
        return 1


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--bversion', type=str, default='2.82', help="Blender version to run.")
    parser.add_argument('--test', action='store_true', help="Runs tests only.")
    args, unknown_args = parser.parse_known_args()
    return args.bversion, args.test, unknown_args


def get_executable_extension():
    if sys.platform in ["win32", "win64"]:
        ext = ".exe"
    else:
        ext = ""
    return ext


if __name__ == "__main__":

    blender_version, test, blender_flags = parse_cli()

    ext = get_executable_extension()

    blender_executables = glob(f"external{os.sep}blender-{blender_version}*{os.sep}blender{ext}")
    if not blender_executables:
        raise Exception(
            f"No Blender executable found for version {blender_version}. Please make sure that a Blender matching this version is installed in the directory 'external', or install one with 'python scripts.get_blender --bversion={blender_version}'.")
    if len(blender_executables) > 1:
        raise Exception(f"Too many blenders returned: {blender_executables}")

    blender = blender_executables[0]

    if test:
        test_flag = f"--python \"{test_file}\" "
        if '-b' not in blender_flags:
            blender_flags.append('-b')
    else:
        test_flag = ''

    exit_val = main(blender, blender_flags, test_flag=test_flag)
    sys.exit(exit_val)
