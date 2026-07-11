class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1 for n in nums]
        post = [1 for n in nums]
        output = [0 for n in nums]

        for i in range(len(nums)):
            if i != 0:
                pre[i] = nums[i] * pre[i-1]
            else:
                pre[i] = nums[i]
        print(str(pre))
        
        for j in range(len(nums) - 1, -1, -1):
            if j != len(nums) - 1:
                post[j] = nums[j] * post[j+1]
            else:
                post[j] = nums[j]
        
        print(str(post))
        for k in range(len(nums)):
            print(k)
            # Edge case: If first element, only take post
            if k == 0:
                output[k] = post[k+1]
                continue
            # Edge case 2: If last element, only take pre
            elif k == len(nums) - 1:
                output[k] = pre[k-1]
                continue
            output[k] = pre[k-1] * post[k+1]

        return output