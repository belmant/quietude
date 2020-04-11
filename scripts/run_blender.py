import argparse
import os
import sys
import subprocess
import re
from glob import glob


def main(blender, test_file):
    local_python = os.path.join(os.getcwd(), "scripts")
    os.environ["LOCAL_PYTHONPATH"] = local_python

    cmd = f'.{os.sep}{blender} -b --python "{test_file}"'
    print(cmd)
    result = int(os.system(cmd))
    if 0 == result:
        return 0
    else:
        return 1


def parse_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', type=str, default='2.82', help="Blender version to fetch.")
    args = parser.parse_args()
    return args.version


def get_executable_extension():
    if "win32" == sys.platform or "win64" == sys.platform:
        ext = ".exe"
    else:
        ext = ""
    return ext


if __name__ == "__main__":

    blender_version = parse_cli()

    ext = get_executable_extension()

    files = glob(f"external{os.sep}blender-{blender_version}*{os.sep}blender{ext}")
    if len(files) != 1:
        raise Exception(f"Too many blenders returned: {files}")

    blender = files[0]

    test_file = "scripts/load_pytest.py"

    exit_val = main(blender, test_file)

    sys.exit(exit_val)
