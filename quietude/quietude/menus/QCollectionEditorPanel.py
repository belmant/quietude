import bpy
from ..core import qcollections

class QCollectionEditorPanel(bpy.types.Panel):
    """Creates a Panel in the scene context of the properties editor"""
    bl_label = "QCollection Editor"
    bl_idname = "VIEW3D_PT_QCollectionEditorPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Edit"
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout
        qcollection_root = qcollections.get_qcollection_root(create_auto=False)
        if qcollection_root:
            qcol_active = qcollections.find_common_qcollection([context.active_object])
            layout.label(text="QCollections Editor")
            col = layout.column()
            col.template_list("QCOLLECTION_UI_qcollections_list", "", qcollection_root, propname="children", active_dataptr=qcol_active, active_propname="", rows=5)
        
