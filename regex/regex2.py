import re
# learning
# if you put .*? you can retrive all characters
# if you group it you can get as group (.*?)
# if you want to retrieve more than value then group more times example within double quotes all values
# then \"(.*?)\s(.*?)\"
# if you group outside you get one value including double quotes
# if you group inside with space then you can get more
# best option is to group by space, example (.*?)\s+(.*?)
str1 = '64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235'

# Trial
pattern = re.compile(r'(.*?\s)')
matches = pattern.match(str1)

print("-->"+matches.group(1)+"<--")
print("-------only IP")
pattern = re.compile(r'(.*?\s)')
matches = pattern.match(str1)
if matches:
    print("-->"+matches.group(1)+"<--")
print(matches)
#
print("Trying to Match-----------")
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
matches = pattern.finditer(str1)
for match in matches:
    print(match)
    print(match.group())
pattern = re.compile(r'(\[(.*?)\])')
matches = pattern.finditer(str1)
for match in matches:
    print(match)
    print("Matching Square Brace")
    print(match.group())

pattern = re.compile(r'(\"(.*?)\")\s+(\d{1,3})\s+(\d{1,4})')
matches = pattern.finditer(str1)
for match in matches:
    print("Match")
    print(match)
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))
    print(match.group(4))
# Now i am using first to get ip, then group all characters till ", retrieview withing "" to a group and then remaining.
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)(\"(.*?)\")\s+(\d{1,3})\s+(\d{1,4})')
matches = pattern.finditer(str1)
# for match in matches:
#     print("Match")
#     print(match)
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))
#     print(match.group(4))
#
# (NOTWORKING)Now i will add group to retrieve anything betwen square braces
#str1 = '64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235'

# (\"(.*?)\") is taking one pattern with double quote and one group witout double quote
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)(\"(.*?)\")\s+(\d{1,3})\s+(\d{1,4})')
matches = pattern.finditer(str1)
for match in matches:
    print("After including square bracket Match")
    #print(match)
    print("Entire Match " + match.group(0))
    print("First Group is IP " + match.group(1))
    print("Next Group contains - and  Square Brace" + match.group(2))
    print("Next is Full status " + match.group(3))
    print("Next is http code  " + match.group(4))
    print("next is Status Code in digit " + match.group(5))
    print("Next is port in digit " + match.group(6))
   

# remove duplicate double quote group. by grouping without double quote
# (\"(.*?)\") is taking one pattern with double quote and one group witout double quote
# above has two groups one with double quote and one witut(contributed inside
# (.*?) only retrives contents
#str1 = '64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235'

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)\"(.*?)\"\s+(\d{1,3})\s+(\d{1,4})')

matches = pattern.finditer(str1)
for match in matches:
    print("After including square bracket Match")
    #print(match)
    print("Entire Match " + match.group(0))
    print("First Group is IP " + match.group(1))
    print("Next Group contains - and  Square Brace" + match.group(2))
    print("Next is Full status " + match.group(3))
    print("Next is http code  " + match.group(4))
    print("next is port " + match.group(5))

# Now lets attempt to get content of [] by .*? grouping that is (.*?) surrounded by braces
#str1 = '64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235'

pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)\[(.*?)\]\s+\"(.*?)\"\s+(\d{1,3})\s+(\d{1,4})')
print("---------Trying for Square Braces---------------------")
matches = pattern.finditer(str1)
for match in matches:
    print("After including square bracket Match")
    #print(match)
    print("Entire Match " + match.group(0))
    print("First Group is IP " + match.group(1))
    print("prints - - " + match.group(2))
    print("Content of Square Braces " + match.group(3))
    print("Content of Double Quota " + match.group(4))
    print("HTTP Status Code  " + match.group(5))
    print("Port Number  " + match.group(6))

# Now i want to get request Type, GET
print("---------Trying to get GET ---------------------")
#str1 = '64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235'
# withing double quota i added two group instead of one group
# by adding \"(.*?)\s(.*?)\" i can extract two values instead of one
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)\[(.*?)\]\s+\"(.*?)\s(.*?)\"\s+(\d{1,3})\s+(\d{1,4})')

matches = pattern.finditer(str1)
for match in matches:
    print("Match")
    #print(match)
    print("Entire Match " + match.group(0))
    print("First Group is IP " + match.group(1))
    print("prints - - " + match.group(2))
    print("Content of Square Braces " + match.group(3))
    print("HTTP type within double quote " + match.group(4))
    print("HTTP Response  " + match.group(5))
    print("HTTP Status  " + match.group(6))
    print("Port Number  " + match.group(7))

print("----------------------------------------------------------------------------------------------------------------------------")
st = 'abc123def2343a4'
a = re.findall('[0-9]+',st)
print(a)
a = re.findall('[a-z]+',st)
print(a)
# initializing string
test_string = "There are 2 apples for 4 persons"

# printing original string
print("The original string : " + test_string)

# using re.findall()
# getting numbers from string
temp = re.findall(r'\d+', st)
res = list(map(int, temp))

# print result
#print("The numbers list is : " + str(''.join(res)))

# initializing string
test_string = "There are 2 apples for 4 persons"

# printing original string
print("The original string : " + test_string)

# using List comprehension + isdigit() +split()
# getting numbers from string
res = [int(i) for i in test_string.split() if i.isdigit()]

# print result
print("The numbers list is : " + str(res))
#
# Use of re.search() and re.match() –
# re.search() and re.match() both are functions of re module in python. These function are very efficient and fast for searching in strings. The function searches for some substring in a string and return a match object if found, else it returns none.
#
# re.search() vs re.match() –
# There is a difference between the use of both functions. Both return first match of a substring found
# in the string, but re.match() searches only in the first line of the string and return match object if found,
# else return none. But if a match of substring is found in some other line other than the first line of string (in case of a multi-line string), it returns none.
# While re.search() searches for the whole string even if the string contains multi-lines and tries to find a match of the substring in all the lines of string.
