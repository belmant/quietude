import bpy

class CollectionModifierMenu(bpy.types.Operator):
    bl_idname = "quietude.display_collection_modifier_menu"
    bl_label = "Display Collection Modifiers"
    bl_description = "Displays the Collection Modifier menu"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.wm.call_menu_pie(name="VIEW3D_MT_CollectionModifierMenu")
        return {"FINISHED"}
