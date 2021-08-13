import sys
from matplotlib import pyplot as plt
data=[]
p=""
c=0
count=[]
protocol=[]
value=[]


for line in sys.stdin:
    line = line.strip()
    line=line.strip("\n")
    print line
    # remove leading and trailing whitespace
    words = line.split()
    print words
    for x in words:
    	data.append(x)
print data
for x in data:
	if (data.index(x))%2==0:
		protocol.append(data[data.index(x)])
		c+=10
		count.append(c)
	else:
		value.append(int(data[data.index(x)]))

print count
print"\nEnd"
print protocol
print"\nEnd"
print value

plt.bar(count,value,align='center')
plt.xticks(count,protocol)
plt.title('Prorocol Analysis')
plt.ylabel('Usage')
plt.xlabel('Protocols')
plt.show()