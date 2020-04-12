# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import importlib
from .log import logger

reimport = 'bpy' in locals()
if reimport:

    logger.debug("Reimporting all modules.")

if reimport:
    importlib.reload(auto_load)
else:
    from . import auto_load

auto_load.init_modules()

if reimport:
    for module in auto_load.modules:
        if 'auto_load' not in module.__name__:
            importlib.reload(module)
else:
    for module in auto_load.modules:
        if 'auto_load' not in module.__name__:
            importlib.import_module(module.__name__)

auto_load.init_classes()

import bpy

bl_info = {
    "name": "Quietude",
    "author": "Cédric Belmant",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "category": "Object",
}


def register():
    auto_load.register()
    logger.debug("Quietude registered.")


def unregister():
    logger.debug("Unregistering Quietude.")
    auto_load.unregister()
