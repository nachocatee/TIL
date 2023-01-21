def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if user_data['id'][-1] in '0123456789': # id의 마지막 값
        return True
    else:
        return False



# 아이디의 마지막 글자는 반드시 0~9 사이의 숫자로 끝나야 함
# 위 조건을 만족하면 True, 그렇지 않으면 False
# 'id'의 밸류값 출력
    # if user_data['id'] == '' or user_data['password'] == '':
    #     return False
    # else:
    #     return True
# user_data1['id'][-1]

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False


