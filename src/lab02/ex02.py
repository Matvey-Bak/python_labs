def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0:
        return nums
    else:
        mnojestvo = set(nums)
        mnojestvo = sorted(mnojestvo)
        return mnojestvo
    
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
