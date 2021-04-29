def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%1000
	return ret
def matPow(l, n, b):
    ret = [[1 if i==j else 0 for i in range(n)] for j  in range(n)]
    while(b):
        if b%2:
            ret = mat(ret, l, n)
        l = mat(l, l, n)
        b//=2 
    return ret
def matsum(matlist, n):
    ret = matlist[0]
    for i in range(1, len(matlist)):
        for j in range(n):
            for k in range(n):
                ret[j][k] = (ret[j][k] + matlist[i][j][k])%1000
    return ret
def divide(matrix, b, n):
    e = [[1 if i==j else 0 for i in range(n)] for j  in range(n)]
    if b==1:
        return mat(matrix, e, n)
    if b%2:
        return matsum([mat(divide(matrix, b//2, n),matsum([e, matPow(matrix, n, b//2)], n), n), matPow(matrix, n, b)],n)
    return mat(divide(matrix, b//2, n),matsum([e, matPow(matrix, n, b//2)], n), n)

n, b = map(int, input().split())
l = [list(map(int, input().split())) for i in range(n)]
ans = divide(l, b, n)
for i in ans:
	print(*i)