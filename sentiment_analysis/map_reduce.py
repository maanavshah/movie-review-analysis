import functools

def count(characters):
    return functools.reduce(reducer, map(lambda char: dict([[char, 1]]), characters))
    
def reducer(i, j):
    for k in j: i[k] = i.get(k, 0) + j.get(k, 0)
    return i

content_file = open('output/sentiment.txt', 'r')
content = content_file.read().replace('\n', '')
dictionary = count(content)
print ("Sentiment\tFrequency")
file = open("output/map_reduce.out", 'w')
for key, value in dictionary.items() :
    print (key,"\t\t", value)
    key = str(key)
    value = str(value)
    file.write(key)
    file.write('\t')
    file.write( value)
    file.write('\n')
print ("\nGenerating pie chart!\n")