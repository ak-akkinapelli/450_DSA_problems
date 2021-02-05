#Cyclically rotate an array by one
def rotate( arr, n):
    
    y = arr.pop(n-1)
    arr.insert(0,y)
    return arr

