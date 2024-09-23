N,X = map(int,input().split())
A = list(map(int,input().split()))
result = False

for i in range(N):
    if A[i] == X:
        result = True

if result == True:
    print("Yes")
else:
    print("No")