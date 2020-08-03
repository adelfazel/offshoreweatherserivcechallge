import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../src')

import main
from src.reader import reader


def test_reader_init_reads_header():
    args = main.get_runtime_params()
    args.inFilename = "tests/data/testDataSmall.csv"
    fileReader = reader.Reader(args)
    assert fileReader.get_headers() == 'datetime,u-comp,v-comp'.split(",")


def test_reader_batch_one_line():
    args = main.get_runtime_params()
    args.inFilename = "tests/data/testDataSmall.csv"
    fileReader = reader.Reader(args)
    headers = fileReader.get_headers()
    expectedResult = []
    expectedResult.append({headers[0]: fileReader.convert_string_to_time('2020-03-27 04.00.00'),
                           headers[1]: 1.662758,
                           headers[2]: -3.345694})
    expectedResult.append({headers[0]: fileReader.convert_string_to_time('2020-03-27 04.01.00'),
                           headers[1]: 1.710038,
                           headers[2]: -3.842012})
    acutalResult = [row for row in fileReader.get_one_batch()]
    assert expectedResult == acutalResult


def test_reader_batch_average():
    args = main.get_runtime_params()
    args.inFilename = "tests/data/testDataSmall.csv"
    args.averageResults = True
    fileReader = reader.Reader(args)
    headers = fileReader.get_headers()
    expectedResult = [
        {headers[0]: fileReader.convert_string_to_time('2020-03-27 04.00.00'),
         headers[1]: (1.662758 + 1.710038) / 2,
         headers[2]: (-3.345694 - 3.842012) / 2}]
    acutalResult = [row for row in fileReader.get_one_batch()]
    assert expectedResult == acutalResult
