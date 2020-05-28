# split 100,000,000.000 

import re
pattern=r"[.,]+"

#print("\n".join(re.split(pattern,input())))


# group dict

m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(m.groupdict())
#{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}


#string2="..123456789101222213141516171820212223"
string2="Hackerank"
#Sample Output

#1
#Explanation

#.. is the first repeating character, but it is not alphanumeric.
#1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.
patter=r'([a-zA-Z0-9])\1+'
res=re.search(patter,string2)
if res == None:
    print(-1)
else:
    print(res.group(1))

#string3="rabcdeefgyYhFjkIoomnpOeorteeeeet"
string3="abaabaabaabaae"
pattern=r'([aeiouAEIOU]{2,})'
#res=re.findall(pattern,input())
res1 = list(map(lambda x: x,re.findall(pattern,string3)))
if len(res1) == 0:
    print( -1)
else:

    
    print(res1)


s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, string3, re.I)
print('\n'.join(a or ['-1']))


#substring match
string1="aaadaa"
#string2="aa"
string2="j"
res=list(map(lambda x:(x.start(),x.start()+len(string2)-1),re.finditer(r'(?={})'.format(string2),string1)))
print(res)
if len(res) > 1:
    print("\n".join(str(res1) for res1 in res ))
else:
    print((-1,-1))