import csv
import logging


class Writer:
    def __init__(self, args, headers):
        self.timeFormat = "%Y/%m/%d %H:%M:%S"
        self.filename = args.outFilename
        self.headers = headers.split(',')
        with open(self.filename, 'w+') as csvFile:
            csvFile.truncate(0)
        logging.debug(f"output file is created {self.headers}")

    def set_time_format(self, timeFormat):
        self.timeFormat = timeFormat

    def get_time_format(self):
        return self.timeFormat

    def write_headers(self):
        with open(self.filename, 'w+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(self.headers)
        logging.debug(f"header: {self.filename} is added")

    def write_one_line(self, record):
        time = record.get_time().strftime(self.timeFormat)
        speed = "%.6f" % record.get_wind_speed()
        direction = "%.6f" % record.get_wind_direction_deg()
        with open(self.filename, "a") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([time, speed, direction])

    def __str__(self):
        return f"file {self.filename} (with headers: {self.headers})"
