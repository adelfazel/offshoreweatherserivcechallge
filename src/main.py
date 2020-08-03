import argparse
import logging
from datetime import datetime
from reader import reader
from writer import writer
from service.converter import WindRecord

outputHeaders = 'datetime,WindSpeed,WindDir'
def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true'):
        return True
    elif v.lower() in ('no', 'false'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def set_logging_params(args):
    log_time_format = "%Y%m%d_%H_%M_%S"
    log_format = '%(asctime)-15s %(message)s'
    log_level = logging.DEBUG if args.verbose else logging.INFO
    log_filename = f'logs/{datetime.now().strftime(log_time_format)}.log'
    open(log_filename, 'w+')
    logging.basicConfig(filename=log_filename, format=log_format, level=log_level)
    logging.getLogger('globalLogger')


def get_runtime_params():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity", default=False, type=str2bool)
    parser.add_argument("-a", "--averageResults", help="average for x minutes of records", default=False, type=str2bool)
    parser.add_argument("-s", "--batchSize", help="number of minutes to average", default=10)
    parser.add_argument("-f", "--inFilename", help="the name of csv file to read from", default="data/sample.csv")
    parser.add_argument("-o", "--outFilename", help="the name of csv file to writer to", default="out/result.csv")
    return parser.parse_args()


def run():
    args = get_runtime_params()
    args.averageResults = str2bool(args.averageResults)
    args.verbose = str2bool(args.verbose)

    set_logging_params(args)
    fileReader = reader.Reader(args)
    fileWirter = writer.Writer(args, outputHeaders)
    fileWirter.write_headers()
    for batch in fileReader.get_one_batch():
        record = WindRecord(batch['datetime'], batch["u-comp"], batch["v-comp"])
        fileWirter.write_one_line(record)



if __name__ == "__main__":
    run()
