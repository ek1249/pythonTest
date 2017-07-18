import re

a='''12
    34  
    56'''
print(a)

import re
data = '''1223 tiger 100
5678 korea 101
1531 lion 102
1534 monkey 103
1254 simon 104
'''
name = re.findall('[A-Z]|[a-z]+',data)
print(name)

#문제 이름이 k로 시작하는 사람만 출력하시오
import re
data = '''1223 tiger 100
5678 korea 101
1531 lion 102
1534 monkey 103
1254 simon 104
'''
name = re.findall(r'[^a-zA-Z]k[a-z]*',data)
print(name)

#문제 전화번호만 출력해봅니다.
import re
data = '''1223 tiger 100
5678 korea 101
1531 lion 102
1534 monkey 103
1254 simon 104
'''
num = re.findall('[:digit:]',data)
print(num)

data = '''1223 김철수 100
5678 홍길동 101
1531 강감찬 102
1534 유관순 103
1254 이성계 104
'''

name = re.findall('김[가-힣]+',data)
print(name )
#전화번호만 출력해 봅니다.
data = '''1223 김철수 100
5678 홍길동 101
1531 강감찬 102
1534 유관순 103
1254 이성계 104
'''

phones = re.findall('\d{4}',data,re.MULTILINE)
print(phones)

#고객번호만 출력해 봅니다.
ids = re.findall('\d{3}',data,re.MULTILINE)
print(ids )
