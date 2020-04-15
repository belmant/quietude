import bpy
from ..utils import access, exceptions
from ..blender_utils import collections_ as collections
from ...log import logger
import re
from typing import *


qcollection_number_pattern = re.compile(r"qcollection_(\d+)")

active_qcollection_names = []

QCOLLECTION_PREFIX = 'qcollection'
QCOLLECTION_ROOT_NAME = 'Quietude'
MAKE_QCOLLECTION_ROOT_VISIBLE = True

class QCollection():

    def __init__(self, properties: Optional[Mapping[str, bpy.types.Property]] = None):
        self.collection = QCollection.create_qcollection()
        self.properties = properties
        logger.debug(f"Active QCollections: {active_qcollection_names}")


    @classmethod
    def create_qcollection(cls):
        """Creates a new qcollection, with the smallest number possible.
        """
        qcollection_root = get_qcollection_root()
        qcollections = list(qcollection_root.children.values())
        logger.debug(f"QCollections: {qcollections}")
        if not qcollections:
            return instance_qcollection(1)
        else:
            for index, number in enumerate(iter_get_qcollection_numbers()):
                logger.debug(f"Index: {index}, Number: {number}")
                if (index + 1) != number:
                    logger.debug(f"MATCH for Index: {index}, Number: {number}")
                    return instance_qcollection(index + 1)
            return instance_qcollection(number + 1)

    def populate(self, objs):
        collections.populate_collection(self.collection, objs)


def extract_qcollection_number(qcollection_name):
    return int(re.search(qcollection_number_pattern, qcollection_name).group(1))

def get_qcollection_root():
    qcollection_root = access.get_key(QCOLLECTION_ROOT_NAME, bpy.data.collections)
    if not qcollection_root:
        qcollection_root = bpy.data.collections.new(QCOLLECTION_ROOT_NAME)
        if MAKE_QCOLLECTION_ROOT_VISIBLE:
            bpy.context.scene.collection.children.link(qcollection_root)
    return qcollection_root

def get_qcollection_by_number(number):
    return get_qcollection_root().children[f"{QCOLLECTION_PREFIX}_{number}"]

def iter_find_obj_in_collections(obj):
    collections = bpy.data.collections
    for name, collection in collections.items():
        if obj in collection.objects.items():
            yield collection

def iter_find_obj_in_qcollections(obj_name):
    qcollection = get_qcollection_root()
    for subcollection in qcollection_root.children.values():
        if obj_name in subcollection.object.keys():
            yield subcollection

def iter_get_qcollection_numbers():
    qcollection_root = get_qcollection_root()
    yield from sorted(map(extract_qcollection_number, qcollection_root.children.keys()))

def instance_qcollection(number):
    qcollection_root = get_qcollection_root()
    new_qcollection = bpy.data.collections.new(f'qcollection_{number}')
    qcollection_root.children.link(new_qcollection)
    active_qcollection_names.append(f'qcollection_{number}')
    return new_qcollection



