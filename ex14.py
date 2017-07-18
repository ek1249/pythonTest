#dataType int float bool str
#collection list tuple set dictionary
#           []   ()    {}   {}

a = [1,3,5,7]
print(a[0])
print(len(a))
for i in range(0,len(a)):
    print(a[i],end="")


#문제 a의 내용을 거꾸로 출력해 봅니다.
#방법 1
print()
print("-"*50)
z = len(a)
for i in range(z-1,-1,-1):
    print(a[i], end=" ")

#방법2
print()
print("-"*50)
for i in reversed(a):
    print(i,end=" ")