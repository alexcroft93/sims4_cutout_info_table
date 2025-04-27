import bpy

obj = bpy.context.active_object

if obj and obj.type == 'MESH':
    world_verts = [obj.matrix_world @ v.co for v in obj.data.vertices]

    min_x = min(v.x for v in world_verts)
    max_x = max(v.x for v in world_verts)
    min_y = min(v.y for v in world_verts)
    max_y = max(v.y for v in world_verts)
    min_z = min(v.z for v in world_verts)
    max_z = max(v.z for v in world_verts)

    # (X,Z,Y)
    print("Max:")
    print(f"{max_x:.6f},{max_z:.6f},{max_y:.6f}")
    print("Min:")
    print(f"{min_x:.6f},{min_z:.6f},{min_y:.6f}")
else:
    print("Select a plane first!")
