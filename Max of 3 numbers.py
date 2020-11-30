#largest of 3 numbers
#myApproach compare all 6 permutations.
class Solution:
    def middle(A,B,C):
        #code here
        if(A>B & B>C):
            return B
        elif(A>B & B<C):
            return B
        elif(A<B & A<C):
            return C
        elif(A<B & A>C):
            return A
            
        elif(A<B & B>C):
            return C
            
        elif(A<B & B<C):
            return B

#Best approach
class Solution(A,B,C):
    return sorted([A,B,C])[1]

A=input()
B=input()
C=input()
Solution(A,B,C)

