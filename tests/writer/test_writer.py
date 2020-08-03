import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../src')

import main
from src.writer import writer
from src.service import converter
from datetime import datetime


def test_writer_init_creates_file():
    args = main.get_runtime_params()
    args.outFilename = "tests/out/sample.csv"
    writer.Writer(args, main.outputHeaders)
    assert os.path.isfile(args.outFilename)
    os.remove(args.outFilename)


def test_writer_headers():
    args = main.get_runtime_params()
    args.outFilename = "tests/out/sample.csv"
    fileWriter = writer.Writer(args, main.outputHeaders)
    fileWriter.write_headers()
    with open(args.outFilename) as csvFile:
        headers = csvFile.readline().strip()
        assert headers == main.outputHeaders
    os.remove(args.outFilename)


def test_writer_one_line():
    args = main.get_runtime_params()
    args.outFilename = "tests/out/sample.csv"
    fileWriter = writer.Writer(args, main.outputHeaders)
    time = datetime.strptime("2020-10-01 10:10:09", '%Y-%m-%d %H:%M:%S')
    uComp = -2.231231
    vComp = 1.231231
    WindData = converter.WindRecord(time, uComp, vComp)
    fileWriter.write_one_line(WindData)
    with open(args.outFilename) as csvFile:
        resultTime, resultSpeed, resultDegree = csvFile.readline().strip().split(",")
        assert datetime.strptime(resultTime, fileWriter.get_time_format()) == time
        assert resultSpeed == "%.6f" % WindData.get_wind_speed()
        assert resultDegree ==  "%.6f" % WindData.get_wind_direction_deg()

    os.remove(args.outFilename)
