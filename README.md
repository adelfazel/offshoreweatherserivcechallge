# offshoreweatherserivcechallge

# Introduction
The program is written in response to the challenge expressed in Programming_Exercise_OWS.pdf By Adel Fazel at 2020/08/02. 

# A few notes:
For writing average results, if the final 'batch' of records contains less than the amount required to create a batch, the avearge of remaining records will displayed. For example if there are 23 records with with 10 minute interval averaging, the final batch of records will contain 3 records, and average of that will be displayed. 
Input data is assumed to be valid, especially there is no check that the records are not one minute apart. However the script is resilient threeif it fails to read the record it will discard it. 
