#return Kth smallest element

def kthSmallest(arr,k):
    return sorted(arr)[k-1]

arr= input()
k=input()
kthSmallest(arr,k)
