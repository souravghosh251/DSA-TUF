class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        i, j = 0, len(arr) - 1

        while i < j:
            curr_sum = arr[i][0] + arr[j][0]
            if curr_sum == target:
                return [arr[i][1], arr[j][1]]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1

        return []
