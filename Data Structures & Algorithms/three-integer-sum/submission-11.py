class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        print(str(nums))
        # i is first index, outer sweep
        # l = j, r = k, inner sweep
        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i] , nums[j] , nums[k]] not in output:
                        output.append([nums[i] , nums[j] , nums[k]])
                    j+=1
                    k-=1
                    continue
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        return output


