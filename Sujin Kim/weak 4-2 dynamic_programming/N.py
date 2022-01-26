def solution(N, number):
    
    numbers = [set([N*int('1'*i)]) for i in range(1, 9)] 
    
    for i in range(8):
        for j in range(i):
            for num1 in numbers[j]:
                for num2 in numbers[i-j-1]: 
                    
                    numbers[i].add(num1 + num2)
                    numbers[i].add(num1 - num2)
                    numbers[i].add(num1 * num2)
                    if num2 != 0:
                        numbers[i].add(num1//num2)
        
        if number in numbers[i]:
            return i+1 
    return -1
