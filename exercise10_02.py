#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input('Enter file:')
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dict = dict()
for line in handle :
    if line.startswith('From ') :
        line = line.split()
        time = line[5]
        shour = time.split(':')
        hour = shour[0]
        dict[hour]=dict.get(hour, 0) + 1

for k, v in sorted(dict.items()):
    print(k,v)