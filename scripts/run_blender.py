import argparse
import os
import sys
import subprocess
import re
from glob import glob


def parse_cli():
    parser = argparse.ArgumentParser()

    python_flag_names = ["--test"]
    python_flags = []

    parser.add_argument('--bversion', type=str, default='2.82', help="Blender version to run.")
    parser.add_argument(python_flag_names[0], action='store_true', help="Runs tests only.")
    args, blender_flags = parser.parse_known_args()

    for flag in python_flag_names:
        value = getattr(args, flag.strip('--'))
        if value:
            if isinstance(value, bool):
                python_flags.append(flag)
            else:
                python_flags.append(f"{flag}={value}")

    return args.bversion, blender_flags, python_flags


def get_executable_extension():
    if sys.platform in ["win32", "win64"]:
        ext = ".exe"
    else:
        ext = ""
    return ext


def main(blender, blender_flags, python_call):
    local_python = os.path.join(os.getcwd(), "scripts")
    os.environ["LOCAL_PYTHONPATH"] = local_python

    cmd = f".{os.sep}{blender} {' '.join(blender_flags)} {python_call}"
    print(cmd)
    result = int(os.system(cmd))
    if 0 == result:
        return 0
    else:
        return 1


if __name__ == "__main__":

    blender_version, blender_flags, python_flags = parse_cli()

    ext = get_executable_extension()

    blender_executables = glob(f"external{os.sep}blender-{blender_version}*{os.sep}blender{ext}")
    if not blender_executables:
        raise Exception(
            f"No Blender executable found for version {blender_version}. Please make sure that a Blender matching this version is installed in the directory 'external', or install one with 'python scripts.get_blender --bversion={blender_version}'.")
    if len(blender_executables) > 1:
        raise Exception(f"Too many blenders returned: {blender_executables}")

    blender = blender_executables[0]

    python_file = "scripts/loader.py"
    python_call = f"--python \"{python_file}\""

    if "--test" in python_flags and '-b' not in blender_flags:
        blender_flags.append('-b')

    if python_flags:
        python_call += f" -- {' '.join(python_flags)}"

    exit_val = main(blender, blender_flags, python_call)
    sys.exit(exit_val)
