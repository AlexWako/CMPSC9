def multiply(x,y):
    if y == 0:
        return 0
    if y>0:
        return(x + multiply(x, y - 1))
    if y<0:
        return(-multiply(x, -y))

def collectMultiples(intList, n):
    if intList == []:
        return []
    if (intList[0] % n == 0):
        return [intList[0]] + collectMultiples(intList[1:], n)
    else:
        return collectMultiples(intList[1:], n)
      
def countVowels(s):
    if len(s) == 0:
        return 0
    else:
        return 'AEIOUaeiou'.count(s[0]) + countVowels(s[1:])

def reverseVowels(s):
    if len(s) == 0:
        return ""
    if s[-1] in 'AEIOUaeiou':
        return s[-1] + reverseVowels(s[:-1])
    else:
        return reverseVowels(s[:-1])

def removeSubString(s, sub):
    if sub == '':
        return s
    if s == sub:
        return ''
    if sub in s:
        return removeSubString((s[:s.index(sub)]) + (s[s.index(sub) + len(sub):]), sub)
    return s

