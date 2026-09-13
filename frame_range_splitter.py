bl_info = {
    "name": "Frame Range Splitter",
    "blender": (2,80,0),
}


import bpy

class VIEW3D_PT_frame_range_splitter(bpy.types.Panel):
    """frame range splitter"""
    bl_idname = "VIEW3D_PT_frame_range_splitter" 
    bl_label = "Frame Range Splitter"

    #define where in blender UI it will be
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Frame Range Splitter"

    
    def draw(self, context):
        #add a label
        self.layout.label(text="Hello World")

#register panel so it will be displayed
bpy.utils.register_class(VIEW3D_PT_frame_range_splitter)


