"""
This program is to sort the arrays an n-D array (value of n given by the user) by the last index of each sub array within the array.

For Example;
n = 3
arr = [[1,5,1],[0,2,-1],[5,5,5,6]]

The output of the above example is;
[[0,2,-1],[1,5,1],[5,5,5,6]]

"""

#code
n = int(input('enter the number of arrays :'))
arr = []
a = []
for i in range(0,n):
    a = list(input("enter : ").split(" "))
    arr.append(a)
print("The array before sorting:",arr)
arr.sort(key=lambda x:x[-1])            #the code to sort the above array
print("The sorted array is:",arr)
