arr = [-3,45,-13,-4,245,-134254]
n = len(arr)


def Sort(arr,n):
    lo =0
    for x in range(0,n):
        if(arr[x]<=0):
            arr[lo],arr[x] = arr[x],arr[lo]
            lo+=1
    print(arr)

Sort(arr,n)
