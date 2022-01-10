def solution(prices):
    answer = [0]
    #stack에 (price, 떨어지지 않는 기간) tuple 저장
    price_stack = []
    
    #뒤집어서 생각! 마지막은 무조건 0 이므로 제외하고 생각
    prices.reverse()
    
    for i in range(1, len(prices)):
        #print(prices[i], price_stack)
        # 스택의 맨 위 값과 지금 가격 비교
        # 스택 맨 위 값이 더 클때까지 (가격 떨어지지x), pop하면서 계속 더하기
        count = 1
        while (len(price_stack)>0 and prices[i] <= price_stack[-1][0]):
            count += price_stack.pop()[1]
        price_stack.append((prices[i], count))
        answer.append(count)   
    
    answer.reverse()
    
    return answer