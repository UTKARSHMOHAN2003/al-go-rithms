def leaderprint(arr, n):
	
    # last element of an array is leader by default
    L = arr[n-1];
    print(L, " is a leader")
    
    # for finding leaders in other elements of the array
    for i in range(n-2, -1, -1):
        if (arr[i] > L):
            L = arr[i];
            print(L, " is a leader")
			
arr = [ 7, 6, 4, 5, 0, 1 ]
n = len(arr)
# calling function
leaderprint(arr, n)
