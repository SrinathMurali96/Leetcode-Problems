Search Insert Position

nums,target = [1,3,5,6], 5

for i in range(0,len(nums)):
        if nums[i] == target or nums[i]>target:
            print( i)
            break
print(i+1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0

        # targetがnumsの最大値より大きい
        if target > nums[-1]:
            return len_nums
        # targetがnumsの最小値より小さい又は等しい
        elif target < nums[0] or target == nums[0]:
            return 0
        # targetがnumsの最大値と等しい
        elif target == nums[-1]:
            return len_nums - 1
        
        # 二分法
        # 左側から探索用変数
        low = 0
        # 右側から探索用変数
        high = len_nums - 1

        while low < high:
            if (high - low) // 2 > 0:
                mid = low + (high - low) // 2
                # nums[mid]の値とtargetを比較してlow又はhighを更新していく
                if nums[mid] < target:
                    low = mid
                elif nums[mid] > target:
                    high = mid
                elif nums[mid] == target:
                    return mid
            else:
                return high
 