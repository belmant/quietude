import bpy
import pytest
from quietude.quietude.blender_utils import collections_ as collections


def test_init():
    bpy.ops.quietude.add_collection_modifier()
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.quietude.add_collection_modifier()

def test_qcollection_root_present():
    assert(collections.is_collection_present('Quietude'))
    

def test_qcollections_present():
    assert(collections.is_collection_present('qcollection_1'))
    assert(collections.is_collection_present('qcollection_1'))

def test_qcollections_children_of_root():
    qcolroot = bpy.data.collections['Quietude']
    assert(collections.is_subcollection(qcolroot, 'qcollection_1'))
    assert(collections.is_subcollection(qcolroot, 'qcollection_2'))

def test_qcollections_fill_empty_name_slots_at_creation():
    bpy.ops.quietude.add_collection_modifier()
    bpy.data.collections.remove(bpy.data.collections['qcollection_2'])
    bpy.ops.quietude.add_collection_modifier()
    assert(collections.is_collection_present('qcollection_1'))
    assert(collections.is_collection_present('qcollection_2'))
    assert(collections.is_collection_present('qcollection_3'))
    assert(not collections.is_collection_present('qcollection_4'))
