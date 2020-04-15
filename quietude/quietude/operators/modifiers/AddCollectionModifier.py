import bpy
from ...blender_utils import modifiers
from ...core import qcollections

available_modifiers = [
    ("DISPLACE", "Displace", "Displace modifier"), 
    ("ARRAY", "Array", "Array modifier"),
    ("MIRROR", "Mirror", "Mirror modifier")
    ]

class AddCollectionModifier(bpy.types.Operator):
    bl_idname = "quietude.add_collection_modifier"
    bl_label = "Add Collection Modifier"
    bl_description = "Adds a modifier on all objects from the same collection at once"
    bl_options = {"REGISTER", "UNDO"}

    modifier_type: bpy.props.EnumProperty(items=available_modifiers,
                                          name="Collection modifiers",
                                          description="Modifiers that can be applied to a collection"
                                          )

    @classmethod
    def poll(cls, context):
        return context.selected_objects != []

    def execute(self, context):
        qcol = qcollections.QCollection()
        objs = context.selected_objects
        qcol.populate(objs)
        modifiers.add_modifier_to_objs(context, objs, self.modifier_type)
        return {"FINISHED"}
