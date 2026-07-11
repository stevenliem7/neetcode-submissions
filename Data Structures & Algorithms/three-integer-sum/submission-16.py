class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        print(str(nums))
        # i is first index, outer sweep
        # l = j, r = k, inner sweep
        for i in range(len(nums) - 1):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    output.append([nums[i] , nums[j] , nums[k]])
                    # Remove duplicate j,k because it will result in the same tuple
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j+=1
                    k-=1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return output


