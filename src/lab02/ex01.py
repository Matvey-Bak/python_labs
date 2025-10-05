def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        return ("ValueError")
    else:
        return min(nums), max(nums)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([]))
print(min_max([-5, -2, -9]))