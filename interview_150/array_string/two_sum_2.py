numbers = [0, 0, 3, 3]
target = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print([i + 1, j + 1])
        elif numbers[i] + numbers[j] > target:
            break
