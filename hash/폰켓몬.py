def solution(nums):
    mx = len(nums) // 2
    nums = set(nums)

    if len(nums) >= mx:
        return mx
    else:
        return len(nums)