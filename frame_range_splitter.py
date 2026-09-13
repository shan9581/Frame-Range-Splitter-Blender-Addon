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




    bpy.types.Scene.total_frames_start = bpy.props.IntProperty(
            name = "Start Frame?",
            default = 1,
            min = 0
        )
    bpy.types.Scene.total_frames_end = bpy.props.IntProperty(
                name = "End Frame?",
                default = 1,
                min = 0
            )

    bpy.types.Scene.num_computers = bpy.props.IntProperty(
        name = "How many computers?",
        default = 1,
        min = 1
    )

    bpy.types.Scene.current_computer = bpy.props.IntProperty(
            name = "Which computer is this",
            default = 1,
            min = 1
        )
    def calculate_new_frame_range(total_frames_end,total_frames_start,num_computers,current_computer):

        amount_of_frames = total_frames_end - total_frames_start

        chunk_size = amount_of_frames / num_computers

        new_start_frame = total_frames_start + (chunk_size * (current_computer- 1))

        new_end_frame = total_frames_start + (chunk_size * current_computer)

        bpy.context.scene.frame_start = new_start_frame
        
        bpy.context.scene.frame_end = new_end_frame


    
    def draw(self, context):
        #add a label
        self.layout.label(text="Hello World")
        self.layout.operator("mesh.primitive_cone_add")
        
        self.layout.prop(context.scene, "total_frames_start")
        
        self.layout.prop(context.scene, "total_frames_end")
        
        self.layout.prop(context.scene, "num_computers")
        
        self.layout.prop(context.scene, "current_computer")

        self.layout.operator(self.calculate_new_frame_range)

#register panel so it will be displayed
bpy.utils.register_class(VIEW3D_PT_frame_range_splitter)

