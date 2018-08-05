import re


file = open('output/cquery.out', 'r')
file = file.read()
numbers = re.findall(r"[-+]?\d*\.\d+|\d+", file)
#print(numbers)
myfile = open('output/sentiment.txt', 'w')
i=0;
for item in numbers:
	i=i+1
	if len(numbers)==i:
		break;
	myfile.write("%s\n" % item)