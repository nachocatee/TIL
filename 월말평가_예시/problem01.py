def max_score(scores):
    pass
    # 여기에 코드를 작성합니다.
    max = scores[0] # scores 리스트의 0번째 요소를 첫번째 값으로 설정

    for i in range(0, len(scores)):
        if max >= scores[i]:
            max = max
        else:
            max = scores[i] 
    return max


# scores 가 리스트로 주어짐
# 각각의 값 중에 젤 큰거를 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90



