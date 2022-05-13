# 문제 정보
# https://programmers.co.kr/learn/courses/30/lessons/42885
# 그리디

def solution(people, limit):

    # 그리디 알고리즘을 사용하기 위해 정렬
    people.sort()

    # 투포인터 사용
    idx_1 = 0
    idx_2 = len(people) - 1
    answer = 0

    # 혹시나 처음에 요소가 1개면 바로 종료
    if idx_1 == idx_2:
        answer += 1
        return answer

    while True: 
        if people[idx_1] + people[idx_2] <= limit:
            answer += 1
            idx_1 += 1
            idx_2 -= 1
            if idx_1 > idx_2: # 이 경우에는 이미 카운트가 완료 되어서 바로 break
                break
            elif idx_1 == idx_2:  # 혹시나 loop에서 idx_1 == idx_2가 되어버리면 answer += 1하고 break해야 함
                answer += 1
                break
        else:
            answer += 1
            idx_2 -= 1
            if idx_1 == idx_2:
                answer += 1
                break
    return answer
