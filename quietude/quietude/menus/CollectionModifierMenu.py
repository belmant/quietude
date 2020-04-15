import bpy

class CollectionModifierMenu(bpy.types.Menu):
    # label is displayed at the center of the pie menu.
    bl_idname = "VIEW3D_MT_CollectionModifierMenu"
    bl_label = "Collection Modifiers"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()
        # operator_enum will just spread all available options
        # for the type enum of the operator on the pie
        pie.operator_enum(operator="quietude.add_collection_modifier", property="modifier_type")
        