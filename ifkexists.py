def quickSort(A, si, ei): 
    if si < ei: 
        pi=partition(A,si,ei) 
        quickSort(A,si,pi-1) 
        quickSort(A,pi+1,ei) 
def partition(A, si, ei): 
    x = a[ei] 
    i = (si-1) 
    for j in range(si,ei): 
        if a[j] <= x: 
            i += 1
            a[i], a[j] = a[j], a[i] 
        a[i+1], a[ei] = a[ei], a[i+1]          
    return i+1
a = [1,4,45,6,10,-8] 
n = 16
if (hasArrayTwoCandidates(a, len(a), n)): 
    print("Array has two elements with the given sum") 
else: 
    print("Array doesn't have two elements with the given sum") 
  
