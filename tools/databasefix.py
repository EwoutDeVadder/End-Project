# at the start of my Database, I saved the data wrong. I didn't use comma's and the ID was incorrect. I changed the ID's manually but I thought
# it could be a good challenge to decode the data with programming.
# this converts a string formatted in: "65.6162.6563.3157.1559.1265.1580.794.14100.5694.3286.179.7176.576.0280.7785.0988.9895.7293.2391.5585.5179.976.1259.86"
# and changes it to decimal values according to how many you want after the dot, this is changed with the static offset variable.
# at the end it puts everything in a list.

# doesnt work with negative numbers.
# sometimes, there aren't enough numbers after a comma so the program buggs out. I am unable to find a fast fix without making 20 exceptions.
# this is an example of string that will give the script an error: 34.450.0-0.01.0242.5324.6245.34

stringList = input()
tempVar = ''
myList = []
static_offset = 2
cur_offset = 0
afterDecimal = False
for l in stringList:    
    if l:
        tempVar += l;
        if afterDecimal and l != '.':
            cur_offset += 1
    
    if cur_offset == static_offset:
        myList.append(float(tempVar))
        cur_offset = 0
        afterDecimal = False
        tempVar = ''
    elif l == '.':
        afterDecimal = True
    
print(myList)