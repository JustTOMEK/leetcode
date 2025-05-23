import itertools

nums = [-1, 0, 1, 2, -1, -4]
answers = []
for combo in itertools.combinations(nums, 3):
    if sum(combo) == 0:
        lst = list(combo)
        lst.sort()
        if lst not in answers:
            answers.append(lst)

print(answers)
