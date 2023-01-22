### 문제1


# N의 약수를 오름차순으로 출력하는 프로그램

N = int(input()) # input 값을 숫자로 바꾸기

result = [] # 결과값 리스트 생성
for i in range(1, 1001): # N이 1000이하의 자연수이기 때문에 i도 마찬가지
    if N % i == 0: # i 로 나눈 나머지가 0이라면
        result.append(i) # 결과값 리스트에 추가

print(*result) # 그냥 result를 출력하면 리스트에 담겨 나오니까 *로 언패킹


### 문제2


# list의 모든 요소들의 합을 반환하는 list_sum 함수

def list_sum(list):
    result = 0
    for i in range(len(list)): # 0부터 len(list) 까지
        result += list[i] # result 값에 더하기
    return result

print(list_sum([1, 2, 3, 4, 5]))

### 문제3


# 딕셔너리로 이루어진 list 전달받아서 'age' key에 해당하는 value 들의 합을 반환
# list[0]['age'] -> 12

def dict_list_sum(list):
    result = 0
    for i in range(len(list)): # 0부터 len(list)까지
        result += list[i]['age'] # 리스트의 딕셔너리의 age 밸류값 더하기
    return result

print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))


# age의 밸류값 추출 -> dict['age']
# list = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# print(list[0]['age']) # 12
# print(len(list)) # 2


### 문제4


# list의 모든 요소들의 합을 반환하는 함수
# 모든 요소를 합하자

# list = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
# print(*list) # [1], [2, 3], [4, 5, 6], [7, 8, 9, 10] # 이건 아니군
# # print(list[0][0] + list[1][0]) # 3 # 이거다!
# # list[i][j]
# # i는 0부터 len(list)까지
# # j는 0부터 len(list[i]) 까지
# print(len(list[1]))


def all_list_sum(list):
    result = 0
    for i in range(len(list)): # 0부터 list의 길이까지 
        for j in range(len(list[i])): # 0부터 list[i]의 길이까지
            result += list[i][j]
    return result

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))


### 문제5


# list를 전달받아 아스키 문자를 이어붙인 문자열 반환
# list = [83, 115, 65, 102, 89]


def get_secret_word(list):
    result = ''
    for i in range(len(list)): # 0부터 len(list)까지
        result += chr(list[i]) # ???: chr은 머지 <- 아스키 코드 표를 가져오는걸 어케 하는지 모르겠어서 정답 보고 참고함
    return result 

print(get_secret_word([83, 115, 65, 102, 89]))

# chr() 함수 -> 아스키 코드 값을 문자로 변환해 주는 함수
# ord() 함수 -> 특정한 한 문자를 아스키 코드 값으로 변환해 주는 함수


### 문제6

# word = 'happy'
# print(ord(word[0])) # 104 # type은 int

def get_secret_number(word):
    word_sum = 0
    for i in range(len(word)): # 0부터 len(word)까지
        word_sum += ord(word[i])
    return word_sum

print(get_secret_number('happy'))



### 문제7


# 문자열 2개를 전달 받아
# 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여
# 더 큰 합을 가진 문자열을 반환
# 같은 경우 둘 다 반환

# 먼저 문자열 2개의 아스키 숫자들의 합을 구해야 함
# 'delilah'를 각각 쪼개기
# word = 'delilah'
# print(*word) # d e l i l a h # 언패킹하기
# print(*word[0]) # d
# print(ord(*word[0])) # 100

def get_strong_word(a, b):
    sum_a = 0
    sum_b = 0
    for i in range(len(a)):
        sum_a += ord(*a[i])
    for j in range(len(b)):
        sum_b += ord(*b[j])
    if sum_a > sum_b:
        return a
    elif sum_a < sum_b:
        return b
    else:
        return a, b

print(get_strong_word('z', 'a'))
print(get_strong_word('delilah', 'dixon'))

# 나는 다 쪼개서 했는데 정답처럼 그냥 for i in a 이렇게만 해도 답 나오는군..