bl_info = {
    "name": "Frame Range Splitter",
    "blender": (2,80,0),
}


import bpy



#making the calculations into an operator that can be called by the panel button
class calculate_new_frame_range(bpy.types.Operator):
    bl_idname = "scene.calculate_new_range"
    bl_label = "Calculate New Frame Range"

    #the formula to calculate the new range
    def execute(self, context):
        
        amount_of_frames = context.scene.total_frames_end - context.scene.total_frames_start + 1
        
        chunk_size = amount_of_frames // context.scene.num_computers
        if  amount_of_frames % context.scene.num_computers != 0:
            chunk_size += 1
        
        new_start_frame = context.scene.total_frames_start + (chunk_size * (context.scene.current_computer- 1))

        #ensures new start frame does not overlap with previous end frame so that it does not render the same thing twice
        if (context.scene.total_frames_start + (chunk_size * (context.scene.current_computer - 1))) == new_start_frame:
            if context.scene.current_computer != 1:
                new_start_frame +=1

        new_end_frame = context.scene.total_frames_start + (chunk_size * context.scene.current_computer)

        print(new_start_frame)
        print(new_end_frame)
        
        bpy.context.scene.frame_start = new_start_frame
        bpy.context.scene.frame_end = new_end_frame
        

        return {'FINISHED'}


class VIEW3D_PT_frame_range_splitter(bpy.types.Panel):
    """frame range splitter"""
    bl_idname = "VIEW3D_PT_frame_range_splitter" 
    bl_label = "Frame Range Splitter"

    #define where in blender UI it will be
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Frame Range Splitter"



    #fields on the panel
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
    


    
    def draw(self, context):
        #add a label
        self.layout.label(text="Hello World")
        self.layout.operator("mesh.primitive_cone_add")
        
        self.layout.prop(context.scene, "total_frames_start")
        
        self.layout.prop(context.scene, "total_frames_end")
        
        self.layout.prop(context.scene, "num_computers")
        
        self.layout.prop(context.scene, "current_computer")

        self.layout.operator("scene.calculate_new_range")

#register panel so it will be displayed
#def register():
bpy.utils.register_class(calculate_new_frame_range)
bpy.utils.register_class(VIEW3D_PT_frame_range_splitter)


"""
def unregister():
        
    bpy.utils.unregister_class(calculate_new_frame_range)
    bpy.utils.unregister_class(VIEW3D_PT_frame_range_splitter)
"""