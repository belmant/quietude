import os
import sys
import re
import time
import zipfile
import shutil
import bpy
import bpy.path


def zip_target(target, target_location):
    if target_location is None:
        target_location = target + ".zip"
    zf = zipfile.ZipFile(target_location, "w")
    if os.path.isdir(target):
        for dirname, subdirs, files in os.walk(target):
            zf.write(dirname)
            for filename in files:
                zf.write('/'.join((dirname, filename)))
    else:
        zf.write(target)
    zf.close()


def get_addon_location(addon_name):
    final_location = os.path.join(bpy.context.preferences.filepaths.script_directory, addon_name)
    return final_location


def install_addon(addon_name):
    source_location = addon_name
    zip_location = source_location + ".zip"
    if os.path.exists(zip_location):
        os.remove(zip_location)

    zip_target(source_location, zip_location)
    bpy.ops.preferences.addon_install(overwrite=True, filepath=os.path.abspath(zip_location))
    bpy.ops.preferences.addon_enable(module=addon_name)


def disable(addon_name):
    bpy.ops.preferences.addon_disable(module=addon_name)


def get_version(addon_name):
    mod = sys.modules[addon_name]
    return mod.bl_info.get("version", (-1, -1, -1))
