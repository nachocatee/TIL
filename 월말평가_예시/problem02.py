def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    over_60 = [] # 60점이 넘는 과목들의 리스트 생성
    
    for i in range(0, len(scores)):
        if scores[i] >= 60:
            over_60.append(scores[i]) # over_60 리스트에 추가
    
    return len(over_60) # 개수가 출력되어야 함으로 len()


# 60점 이상인 과목의 개수!
# 리스트를 만들고 60점 이상이면 카운트


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3

