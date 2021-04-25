##IMPORTING A TEXT FILE
text = open("input.txt",'r')
d = dict()
prizes = []
for i in text:
    words = i.split(":")
    d[int(words[1])] = (words[0])  #CREATING A DICTIONARY OF PRODUCTS AND PRIZES
    prizes.append(int(words[1]))
#print(d)
text.close()


##SORTING THE PRIZES OF THE GOODIES IN ASCENDING ORDER
prizes.sort()
#print(prizes)

## GETTING INPUT FROM THE USER FOR NUMBER OF THE EMPOLYEES
n = int(input())

## MAIN PROGRAM
number_of_items = len(prizes)
i = 0
r = str()
mininum_range = prizes[number_of_items-1]
while (i+n-1)< len(prizes):
    x = prizes[i+n-1] - prizes[i]
    #print(x)
    if mininum_range > x :
        mininum_range = x
        r = i
    i += 1

output = str()
output = "Number of the employees: "+ str(n)+"\n\n" + "Here the goodies that are selected for distribution are:\n"

for j in range(0,n):
    y = r+j
    z = prizes[y]
    output += d[z] + ": " + str(z) + "\n"
output += "And the difference between the chosen goodie with highest price and the lowest price is " + str(mininum_range)
print(output)

##WRITING AN OUTPUT IN TEXT FILE
out = open("output3.txt","w")
out.write(output)
out.close()
