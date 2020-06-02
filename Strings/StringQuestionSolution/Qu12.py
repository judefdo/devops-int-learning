#Hakerrank sherlockAndAnagrams
from collections import Counter
#For a given string cdcd
def genlist(s,size):
    print("SIZE:",size, s)
    res = [s[i:i+size] for i in range(len(s))]
    print(res)
    return res


def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        print(a)
        b = Counter(a)
        print(b)
        for j in b:
            count+=b[j]*(b[j]-1)/2
            print(b[j])
    return int(count)

def sherlockAndAnagrams1(s):
    result=0
    for repeat in range(len(s)//2):
#        org=list(map(lambda x:x, s))
        org=genlist(s,repeat+1)
        count=0
        for s1 in org:
            print(s1, org[count+1:])
 #           res=list(filter(lambda x: sorted(x)==sorted(x[]),org))
            print(len(res))
            if s1 in org[count+1:] :
                result += 1
            count += 1
    return result

if __name__ == '__main__':
    string1="cdcd"
    result=sherlockAndAnagrams(string1)
    print(result)