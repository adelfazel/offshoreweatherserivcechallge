import sys, os
from datetime import datetime
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../src')

from src.service import converter


def test_convert_speed():
    uComp = 1.0
    vComp = 1.0
    expectedSpeed = 1.414213562
    windRecord = converter.WindRecord(datetime.now(), uComp, vComp)
    assert abs(windRecord.get_wind_speed() - expectedSpeed) < 0.00001


def test_convert_dir_q1():
    uComp = 1.0
    vComp = 1.0
    expectedDegree = -135
    windRecord = converter.WindRecord(datetime.now(), uComp, vComp)
    assert abs(converter.rad_to_degree(windRecord.get_phi_rads()) - expectedDegree) < 0.00001

def test_convert_dir_q2():
    uComp = 1.0
    vComp = -1.0
    expectedDegree = -45
    windRecord = converter.WindRecord(datetime.now(), uComp, vComp)
    assert abs(converter.rad_to_degree(windRecord.get_phi_rads()) - expectedDegree) < 0.00001

def test_convert_dir_q3():
    uComp = -1.0
    vComp = -1.0
    expectedDegree = 45
    windRecord = converter.WindRecord(datetime.now(), uComp, vComp)
    assert abs(converter.rad_to_degree(windRecord.get_phi_rads()) - expectedDegree) < 0.00001

def test_convert_dir_q4():
    uComp = -1.0
    vComp = 1.0
    expectedDegree = 135
    windRecord = converter.WindRecord(datetime.now(), uComp, vComp)
    assert abs(converter.rad_to_degree(windRecord.get_phi_rads()) - expectedDegree) < 0.00001

