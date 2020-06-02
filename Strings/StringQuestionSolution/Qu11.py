from collections import Counter

givenstring="two times three is not four"
matchstring="two times two is four"

def matchstring(givenstring, matchstring):
    givecounter = Counter(givenstring)
    matchcounter = Counter(matchstring)

    for word, count in matchcounter.items():
        if word not in givencounter and givencounter.get(word)< count:
            givecounter.get
            return False
    return True

if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    if checkMagazine(magazine, note):
        print("Yes")
    else:
        print("No")