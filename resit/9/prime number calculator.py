b = int(input('the number is:'))
def hsh(a):
    if a <= 1:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True
if hsh(b):
    print("YES")
else:
    print('NO')
if hsh(28):
    k = "YES"
else:
     k = 'NO'
print('example: 28',k)