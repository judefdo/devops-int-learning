import os
import re
''' 
    . - Any Character except new line
    \d - Digit (0-9)
    \D - Not a digit Note:- All captitals negate
    \w - Word character (A-Z,a-z,0-9, _ (underscore)
    \W - not  word
    \s - matches whitespace, new line tab
    \S - which is opposite to above
   
    
    Anchors, Dont match any characters but are used in conjunction with other pattern
     \b - Word boundary, indicated by space or alphaanumberic character
    \B - Not a word boundry
    ^ - begining of string
    $ - end of string
    [] - matches characters in brackets. NOTE- you dont need to escape characters inside character set
    [^] - matches not in brackets ( negates )
    - Specifiy Range
    
    . - Means any character
    Quantifiers:
    * -  0 or more 
    + -  1 or more
    ? - 0 or one
    {3} - Exact Number
    {3-4} - Range of numbers, min and max
    
    () - Groups can group patterns
    ! - Either or
    '''

searchtext = '''
From: Guido van Rossum (gui...@CNRI.Reston.Va.US)
hanha
phone number is 555.333.3423
phone number 2 is 542-334-1234
phone number 3 is (533)-333-3423
pnumbe3 4 is 800-889-2343
p         is 900-334-3234

Mr Raghu
Mr. subba
Ms mom
Mrs. mommy
Mr. T
emails
CoreMsachele@gmail.com
Core.Msachel@niervisity.edu
core-232-mache@mywork-domain.net

'''
# - Example below uses . which matches everything
pattern = re.compile(r'.') # r is a raw string, which python dont interpret
matches = pattern.finditer(searchtext)
#for match in matches:
    #print("Example1")
    #print(match)
# - Example below Matches only one with period. jut do it by escaping
# pattern = re.compile(r'\.')  # r is a raw string, which python dont interpret
# matches = pattern.finditer(searchtext)
# for match in matches:
#     print("Example2")
    #print(match)
# - Example to match only digit
pattern = re.compile(r'\d')  # r is a raw string, which python dont interpret
matches = pattern.finditer(searchtext)
#for match in matches:
    #print(match)
# - Similarly you cana find Matches which is not a digit with \D
# - Similarly for \w and \W
# - Example to match space
pattern = re.compile(r'\s')  # r is a raw string, which python dont interpret
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)
# - exaample to match a boundary
pattern = re.compile(r'\bha') # - Matches \boundary and character, example space and chaaracters.
# it wont match if there is not boundary to start. boundary need to be before it
matches = pattern.finditer(searchtext)
#for match in matches:
#    print(match)
# - Example \B gives you opposite
# - to try
# - $ and ^ is ending and begining
# - lets match phone number. this matches phone with - and also with . because . meansy anycharacter
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')  # r is a raw string, which python dont interpret
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)

# now replace . with a character set []
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
# same as above behavior but it uses charaacter set which can tell you only put those character
# NOTE- you dont need to escape characters inside character set
# NOTE- eventhough there are multiple characters inside character set, it only matches one character

# - Match 800 and 900

pattern = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d')  # r is a raw string, which python dont interpret
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)
# Sepcify Range
pattern = re.compile(r'[8-9]00[.-]\d\d\d[.-]\d\d\d\d')
# Search for lower and upper case. lowercase range immediately followed by upper case or vice versa
pattern = re.compile(r'[a-zA-Z]')
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)
# possible ranges [a-z] or [A-Z]
# if you put caret inside range it negates
# [^a-z] matches which is not lower case letter
# [^b]at matches cat,rat but not bat
# with Quantifiers \d{3}.d{3}.d{4} is same as \d\d\d etc
# Example to match Mr
# start with r'Mr\.' Now to match with or without period use ? quantifier
# r'Mr\.?'
# Now we match space and Upper case letter
# r'Mr\.?\s[A-Z] - matches Mr S
# now lets use \w to match word
# now we decide what quantifier to use, to match single letter and full word
# r'Mr\.?\s[A-Z]\w+ this doesn't match Mr. T
# to match 0 word and more, use *
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)
# Example grouping patterns
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)

# Example to group another way
# Example grouping patterns
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# lets match email
# lowercase and upper case untill we hit @ and same pattern
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+')
matches = pattern.finditer(searchtext)
# for match in matches:
#     print(match)
# above is not matching with . lets add that to a character set

pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.[a-zA-Z]+') # . matches one with .
# add . - to both name and domain character set and
pattern = re.compile(r'[a-zA-Z.-]+@[a-zA-Z-]+\.(edu|com|.net)')
# email matching pattern from internet
# r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Matching url
urls = '''
https://www.google.com
https://youtube.com
http://coreyms.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?') # s? means 0 or 1 character of s
# match wwww
pattern = re.compile(r'https?//(www)?') # http://www or https://
# match domain
pattern = re.compile(r'https?//(www)?\w+\.') # matches after https://www.google
#now .com
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)

for match in matches:
    print(match)
# lets extract those values as groups. whichever you need to extract just put them in parenthesis
# below i am using for google and .com type
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
# now we have 3 groups, one which is optional www and second is domain like google and third is .com
# and also group(0) which matches all. Note adding groups wont change the result. you still get same resule

# for match in matches:
#     print(match)
# for match in matches:
#     print(match.group(0))
# for match in matches:
#     print(match.group(1))
# for match in matches:
#     print(match.group(2))

for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))

# for loop multiple times did not work. only one forloop worked
# substitute url
# now you can substitute 2 and 3
# substitute url is used to replace entire pattern with searched pattern. this is used to clean up
# example if you want https://google.com to be replaced only with google.com
# do the following
subbed_url = pattern.sub(r'\2\3',urls) # searches pattern and replaces with searched pattern
print(subbed_url) # prints as list of tuples of matched groups. remember you grouped 3 times

# - Example usage of findall
# findall returns all matched string as list
matches = pattern.findall(urls)
for match in matches:
    print(match)
print(pattern.findall(urls))
# - pattern.match doesn't return iterable and it only matches begingin of string. dont use it
# - better to use patter.search to search the string in entire string

def thisisold():
    with open("log.log","r") as file:
        for line in file:
            #print(line)
            # 64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235
            #date_re = re.compile('(?P<a_year>\d{2,4})-(?P<a_month>\d{2})-(?P<a_day>\d{2}) (?P<an_hour>\d{2}):(?P<a_minute>\d{2}):(?P<a_second>\d{2}[.\d]*)')
            re_search = re.compile('(?P<my_ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
            found = re_search.match(line)
            #if found is not None:
                #print found.groupdict()
            #re_search = re.compile('(?P<my_day>\d{1,2})\/(?P<month>[a-zA-Z]+)\/(?P<a_year>\d{2,4})')
            re_search = re.compile('(?P<my_day>\\/[a-zA-Z]+)')
            found = re_search.match(line)
            if found is not None:
                print(found.groupdict())

            # parts = [
            #     r'(?P<host>\S+)',  # host %h
            #     r'\S+',  # indent %l (unused)
            #     r'(?P<user>\S+)',  # user %u
            #     r'\[(?P<time>.+)\]',  # time %t
            #     r'"(?P<request>.*)"',  # request "%r"
            #     r'(?P<status>[0-9]+)',  # status %>s
            #     r'(?P<size>\S+)',  # size %b (careful, can be '-')
            #     r'"(?P<referrer>.*)"',  # referrer "%{Referer}i"
            #     r'"(?P<agent>.*)"',  # user agent "%{User-agent}i"
            # ]
            # 64.242.88.10 - - [07/Mar/2004:16:54:55 -0800] "GET /twiki/bin/rdiff/Main/NicholasLee HTTP/1.1" 200 7235
            parts = [
                r'(?P<host>\S+)',  # host %h
                r'\S+',  # indent %l (unused) \S  means 'anything but a whitespace character'.
                #r'- +',  # indent %l (unused)
                r'[\s-]+', # Multiple space and Dash
                r'(?P<every_thing>\[(.*?)\])'
                #r'\[',   # Matching [
                #r'(?P<my_day>\d{1,2})\/(?P<month>[a-zA-Z]+)\/(?P<m_year>\d{2,4})',

               # r'(?P<next>:)',  # or Matching : 16:52:35 -0800] "GET /twiki/bin/edit/Main/Flush_service_name?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
                #r'(?P<myday>\d{1,2})'
                #r'(?P<next2>\d+)'
                #r'(?P<next>:)'
                #r'(?P<time>\d{1,2}:)'
                #r'(?P<next>\S+)',  # indent %l (unused)




            ]

            #pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

            pattern = re.compile(r'\s+'.join(parts) )
            found = pattern.match(line)
            #if found is not None:
                #print found.groupdict()
            # print unmatched
            #s = pattern.sub('', line)
            #print "unmatched is " + s

            # Method 2
            parts = [
                r'(?P<host>\S+)',  # host %h
                r'\S+',  # indent %l (unused) \S  means 'anything but a whitespace character'.
                # r'- +',  # indent %l (unused)
                r'[\s-]+',  # Multiple space and Dash
                r'(?P<ignorethis>\[)',


                # r'\[',   # Matching [
                # r'(?P<my_day>\d{1,2})\/(?P<month>[a-zA-Z]+)\/(?P<m_year>\d{2,4})',

                # r'(?P<next>:)',  # or Matching : 16:52:35 -0800] "GET /twiki/bin/edit/Main/Flush_service_name?topicparent=Main.ConfigurationVariables HTTP/1.1" 401 12851
                # r'(?P<myday>\d{1,2})'
                # r'(?P<next2>\d+)'
                # r'(?P<next>:)'
                # r'(?P<time>\d{1,2}:)'
                # r'(?P<next>\S+)',  # indent %l (unused)

            ]

            # pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

            pattern = re.compile(r'\s+'.join(parts))
            found = pattern.match(line)
            if found is not None:
                print (found.groupdict())
            # print unmatched
            s = pattern.sub('', line)
            print("unmatched is ->" + s)




    """
    \D{3} any three non digits
    \s+ one or more white spaces
    \d{1,2} one to two digits
    \d{2} exactly two digits
    (:\d{2}){2} two occurrences of (: followed by two digits)
    
    r"[^\S\n\t]+"
    The [^\S] matches any char that is not a non-whitespace = any char that is whitespace. However, since the character class is a negated one, when you add characters to it they are excluded from matching.
    
    Python demo:
    
    import re
    a='rasd\nsa sd'
    print(re.findall(r'[^\S\n\t]+',a))
    # => [' ']
    
    """
