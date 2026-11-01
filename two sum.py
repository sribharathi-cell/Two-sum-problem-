nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

for num in nums:
    for num2 in nums:
        if num != num2 and num + num2 == target:
            print([nums.index(num), nums.index(num2)])
            break