def mat(a, b, n):
	ret = [[0]*n for i in range(n)]
	for i in range(n):
		for j in range(n):
			for k in range(n):
				ret[i][j] = (ret[i][j]+a[i][k]*b[k][j])%1000000007
	return ret
def fib(n):
    l = [[1,1],[1,0]]
    ans = [[1,0],[0,1]]
    while(n):
        if n%2:
            ans = mat(ans, l, 2)
        l = mat(l, l, 2)
        n//=2
    return ans[1][0]        
n, m = map(int, input().split())
while n:
    n, m = m%n, n
print(fib(m)%1000000007)