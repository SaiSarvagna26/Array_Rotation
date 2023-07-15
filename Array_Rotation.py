def rotate_array(A, B):
    n = len(A)
    B %= n  
    reverse_array(A, 0, n - 1)
    reverse_array(A, 0, B - 1)
    reverse_array(A, B, n - 1)

    return A


def reverse_array(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1


A = list(map(int,input().split()))
B = int(input())
result = rotate_array(A, B)
print(result) 
