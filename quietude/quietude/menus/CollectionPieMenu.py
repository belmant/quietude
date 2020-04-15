import bpy

class CollectionPieMenu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_CollectionPieMenu"
    bl_label = "Collection menu."

    def draw(self, context):
        pie = self.layout.menu_pie()
        pie.operator('quietude.display_collection_modifier_menu', text="Add Collection Modifier")
        