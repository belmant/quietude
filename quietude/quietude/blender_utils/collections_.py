import bpy

def populate_collection(collection, objs):
    for obj in objs:
        if obj not in collection.objects.values(): # object already in collection
            collection.objects.link(obj)

def is_collection_present(key):
    try:
        qcolroot = bpy.data.collections[key]
    except KeyError:
        qcolroot = None
    return qcolroot

def is_subcollection(collection, key):
    return (key in list(collection.children.keys()))