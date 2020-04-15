from __future__ import annotations
from typing import *
import bpy

def add_modifier_to_objs(context: bpy.types.Context, objs: Sequence[bpy.types.Object], modifier_type: bpy.props.EnumProperty):
    first_selected_object = bpy.context.view_layer.objects.active
    for obj in objs:
        if isinstance(obj.data, bpy.types.Mesh):
            context.view_layer.objects.active = obj
            bpy.ops.object.modifier_add(type=modifier_type)
    context.view_layer.objects.active = first_selected_object