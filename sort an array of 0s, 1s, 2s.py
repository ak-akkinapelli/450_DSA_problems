#Sort an array of 0s, 1s and 2s

#I came up with an approach using for loop but it was sorting only once,
#it ain't going back and checking again, tried recursion but it fell in to an infite loop.


#Editorial Approach
def sort012(arr,n):
    # code here
    mid=0
    lo=0
    hi=n-1
    while(mid<=hi):
        if(arr[mid]==0):
            arr[mid],arr[lo] = arr[lo],arr[mid]
            mid +=1
            lo +=1
        elif(arr[mid]==1):
            mid +=1
        else:
            arr[hi],arr[mid] = arr[mid],arr[hi]
            hi -=1
    print(arr)

arr = [input()]
n = input()
sort012(arr, n)
