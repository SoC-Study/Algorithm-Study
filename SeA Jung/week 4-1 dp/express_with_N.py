def solution(N, number):
    answer = -1
    possible_num = [0]

    for i in range(1, 9):
        numbers = set()
        # 단순 나열
        numbers.add(int(str(N) * i))

        for j in range(1, i):
            for x in possible_num[j]:
                for y in possible_num[i-j]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)

                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break

        possible_num.append(numbers)

    return answer
