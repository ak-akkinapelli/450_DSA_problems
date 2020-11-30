
#my initial approach
#break the string and add the charecters reverse
#order using "insert" to list and rejoin them
def reverseWord(s):
    #your code here
    y =[]
    for x in s:
        y.insert(0,x)
    print("".join(y))



#Famous approach on internet, direct syntax to reverse it

def reverseWord(s):
    print(s[::-1])

s= input()
reverseWord(s)
