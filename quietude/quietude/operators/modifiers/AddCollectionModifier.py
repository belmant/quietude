import bpy

class AddCollectionModifier(bpy.types.Operator):
    bl_idname = "quietude.add_collection_modifier"
    bl_label = "Add collection modifier"
    bl_description = "Adds a modifier on all objects from the same collection at once."
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.selected_objects != []

    def execute(self, context):
        first_selected_object = bpy.context.view_layer.objects.active
        objects = context.selected_objects
        for obj in objects:
            if isinstance(obj.data, bpy.types.Mesh):
                bpy.context.view_layer.objects.active = obj
                bpy.ops.object.modifier_add(type='DISPLACE')
        bpy.context.view_layer.objects.active = first_selected_object
        return {"FINISHED"}
