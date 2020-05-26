# How do you check if two strings are a rotation of each other?

#1. Create a temp string and store concatenation of str1 to
 #      str1 in temp.
#                          temp = str1.str1
#    2. If str2 is a substring of temp then str1 and str2 are 
#       rotations of each other.
#
#    Example:                 
#                     str1 = "ABACD"
#                     str2 = "CDABA"

#     temp = str1.str1 = "ABACDABACD"
#     Since str2 is a substring of temp, str1 and str2 are 
#     rotations of each other.


def rotat(string1, string2):
    temp=string1+string1
    if temp.count(string2) > 0:
        return 0
    else:
        return 1

str1 = "ABACD"
str2 = "CDABA"

if rotat(str1,str2):
    print("The string don't rotate")
else:
    print("The string rotate")