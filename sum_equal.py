def printPairs(arr, n, sum):
 
   
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")
 
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
printPairs(arr, n, sum)

output:
PS C:\Users\HIMA BINDU\Documents\Python VSC> python -u "e:\Practice\assinment1.py"
(1, 5) 
(1, 5) 
(7, -1)
 
