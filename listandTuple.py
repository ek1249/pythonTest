#list tuple
#[]   ()
#tuple : list의 상수버전

a = [10,20,30]
b = (10,20,30);

print(type(a))
print(type(b))

#b[0] = 100 tuple의 값은 변경시킬수 없다!
print(b)

print("="*50)
def multi(n):
    return n+2,n*n

a,b = multi(5)
print(a)
print(b)