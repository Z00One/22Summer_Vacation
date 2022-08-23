def solution(numbers):
    if len(numbers) > 1:
        numbers = sorted([str(num) for num in numbers])
        numbers.sort(key = len)
        compareValue = len(numbers[-1])
        a = numbers[0]
        b = numbers[1]
        value = a + b if a * 3 > (b * 3)[:len(a * 3) + 1] else b + a
        return value + solution(numbers[2:])
    
    else:
        return numbers[0]
print(solution( [ 67,676,677,]))