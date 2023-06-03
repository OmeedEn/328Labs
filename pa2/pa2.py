#take in input from a seperate file and then perform merge sort to sort it all under 10 seconds runtime
#Omeed Enshaie

def merge(a0, a1, arr):
    i0 = 0
    i1 = 0
    for i in range(0, len(arr), 1):
        if i0 == len(a0):
            arr[i] = a1[i1]
            i1 = i1 + 1
        elif i1 == len(a1):
            arr[i] = a0[i0]
            i0 = i0 + 1
        elif a0[i0] <= a1[i1]:
            arr[i] = a0[i0]
            i0 = i0 + 1
        else:
            arr[i] = a1[i1]
            i1 = i1 + 1

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    L = mergeSort(arr[0:mid])
    R = mergeSort(arr[mid:len(arr)])
    merge(L, R, arr)
    return arr

file = open("Input.txt", "r")
arr = list(file.read())
mergeSort(arr)

f = open("output.txt", "w")
f.write(''.join(arr))
file.close()
f.close()
