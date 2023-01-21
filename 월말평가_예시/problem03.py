def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if user_data['id'] == '' or user_data['password'] == '': # id와 password 두개의 key의 value 값이 하나라도 비어있으면
        return False
    else:
        return True


# 비어있는 문자열이면 False, 그렇지 않으면 True
# 딕셔너리의 value가 비어있으면 false를 출력하는거
# value 값을 출력 하는 법 -> dic['key']

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True