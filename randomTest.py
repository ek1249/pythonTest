import random

print(random.randrange(100));

#문제 0-100사이의 난수를 10개 출력해 봅니다.
print();
print("-"*50);
for _ in range(0,10):
    print(random.randrange(50,100),end=" ")

#c언어 코드를 파이썬으로 변경해 봅니다.
print()
print("-"*50)
next = 1
def rand():
    global next
    next = next *1103515245 + 12345
    return (next //65536) % 32768

print(rand())
print("-"*50)

for i in range(10):
    print(rand(),end=" ")
