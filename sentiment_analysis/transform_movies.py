import csv
import os
write_url = open('data/temp.csv','w')
wr = csv.writer(write_url,dialect='excel',delimiter='\t')
line = ''
with open('data/urls.csv') as read_url:
    reader = csv.reader(read_url)
    firstline = True
    for row in reader:
    	if firstline:
    		line = row
    		firstline = False
    		continue
    	wr.writerow(row)
os.system("rm -rf data/urls.csv")
wr.writerow(line)
os.system("mv data/temp.csv data/urls.csv")