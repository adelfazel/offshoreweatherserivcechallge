# offshoreweatherserivcechallge

# Introduction
The program is written in response to the challenge expressed in Programming_Exercise_OWS.pdf By Adel Fazel at 2020/08/02. 

# A few notes:
For writing average results, if the final 'batch' of records contains less than the amount required to create a batch, the avearge of remaining records will displayed. For example if there are 23 records with with 10 minute interval averaging, the final batch of records will contain 3 records, and average of that will be displayed. 
Input data is assumed to be valid, especially there is no check that the records are not one minute apart. However the script is resilient threeif it fails to read the record it will discard it. 

# To use
git clone https://github.com/adelfazel/offshoreweatherserivcechallge
go to wherever you have downloaded it
source venv/bin/activate
make init
make test
make run
python3 src/main.py 

Parameters to consider to add:
parser.add_argument("-a", "--averageResults", help="average for x minutes of records", default=False, type=str2bool)
parser.add_argument("-s", "--batchSize", help="number of minutes to average", default=10)
parser.add_argument("-f", "--inFilename", help="the name of csv file to read from", default="data/sample.csv")
parser.add_argument("-o", "--outFilename", help="the name of csv file to writer to", default="out/result.csv")

e.g.
python3 src/main.py -a True -o out/averagedResult

# more notes
the basic results are added to out/ folder 

