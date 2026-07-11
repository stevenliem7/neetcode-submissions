class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        output = [1 for n in nums]

        # First pass, fill prefixes
        for k in range(1, len(nums) + 1, 1):
            output[k-1] = output[k-1] * pre
            pre = pre * nums[k-1]

        # Second pass, fill postfixes
        for k in range(len(nums) - 1, -1, -1):
            output[k] = output[k] * post
            post = post * nums[k]
             
        return output