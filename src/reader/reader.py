import os
import logging
import csv
from datetime import datetime
from functools import reduce

logger = logging.getLogger('globalLogger')


class Reader:
    def __init__(self, args):
        self.timeFormat = '%Y-%m-%d %H.%M.%S'
        self.averageResult = args.averageResults
        self.batchSize = args.batchSize
        self.filename = args.inFilename
        assert os.path.isfile(self.filename), "input file doesn't exist, ensure file is in 'data' folder"
        if args.averageResults:
            assert self.batchSize > 1, "invalid averaging size requested, it must be greater than 1"
        with open(self.filename) as csvFile:
            self.headers = csvFile.readline().strip().split(",")

        logger.debug(f"header file read: {self.headers}")

    def get_headers(self):
        return self.headers

    def set_time_format(self, timeFormat):
        self.timeFormat = timeFormat

    def get_time_format(self):
        return self.timeFormat

    def convert_string_to_time(self, timestr):
        return datetime.strptime(timestr, self.timeFormat)

    def get_one_batch(self):
        with open(self.filename) as csvFile:
            csvFile.readline()
            reader = csv.DictReader(csvFile, fieldnames=self.get_headers())
            if self.averageResult:
                batch = []
                for rowIndex, record in enumerate(reader):
                    cleanRecord = self.clean_record(record)
                    if cleanRecord:
                        if (rowIndex % self.batchSize == 0 and rowIndex > 0):
                            yield self.calculate_average_batch(batch)
                            batch = []
                        batch.append(cleanRecord)
                if batch:
                    yield self.calculate_average_batch(batch)
            else:
                for record in reader:
                    cleanRecord = self.clean_record(record)
                    if cleanRecord:
                        yield cleanRecord

    def calculate_average_batch(self, batch):
        if batch:
            res = {}
            res['datetime'] = batch[0]['datetime']
            batchUComp = reduce(lambda x, y: x + y, map(lambda x: x['u-comp'], batch))
            batchVComp = reduce(lambda x, y: x + y, map(lambda x: x['v-comp'], batch))
            res['u-comp'] = batchUComp / len(batch)
            res['v-comp'] = batchVComp / len(batch)
            return res
        return None

    def clean_record(self, record):
        res = {}
        try:
            res['datetime'] = self.convert_string_to_time(record['datetime'])
            res['u-comp'] = float(record['u-comp'])
            res['v-comp'] = float(record['v-comp'])
            return res
        except Exception as e:
            logger.error(f"unable to process {record}; exception thown {e}")
        return None

    def __str__(self):
        return f"file {self.filename} (with headers: {self.headers})"
