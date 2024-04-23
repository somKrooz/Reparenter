import unreal
import json
import os

editor_util = unreal.EditorLevelLibrary()
editor_asset_lib = unreal.EditorAssetLibrary()
material_lib = unreal.MaterialEditingLibrary()
selected_actor = unreal.EditorLevelLibrary.get_selected_level_actors()

paths = []
for i in selected_actor:
    static_mesh_component = i.get_component_by_class(unreal.StaticMeshComponent)
    material = static_mesh_component.get_material(0)
    split = str(material.get_full_name()).split(' ')[1]
    paths.append(split)

json_file_path = os.path.abspath(r"D:\Unreal Projects\Troll\Plugins\Reparent\dump.json")

with open(json_file_path, 'w') as json_file:
    json.dump(paths, json_file, indent=2)


def main(path_addr):
    newAddr = str(path_addr).split("'")[1]

    selected_actor = unreal.EditorLevelLibrary().get_selected_level_actors()

    for actor in selected_actor:
        actor.set_actor_hidden(True)

    material_to_reparent = editor_asset_lib.load_asset(newAddr)

    with open(r"D:\Unreal Projects\Troll\Plugins\Reparent\dump.json", 'r') as json_file:
        arr = json.load(json_file)


    for i in arr:
        Thing = unreal.load_asset(i,unreal.MaterialInstanceConstant)

        material_lib.set_material_instance_parent(Thing, material_to_reparent)
        editor_asset_lib.save_loaded_asset(Thing, False)

    for actor in selected_actor:
        actor.set_actor_hidden(False)
        print(f"{actor}: Reparented")
