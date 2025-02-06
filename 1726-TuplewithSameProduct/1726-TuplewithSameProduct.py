class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        result_dct = {}

        def calc_num_pairs(x):
            return 8*(((x-1)*x)//2)


        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                temp_val = nums[i]*nums[j]
                if temp_val not in result_dct:
                    result_dct[temp_val] = 1
                else:
                    result_dct[temp_val] += 1

        print(result_dct)
        ret = 0
        for v in result_dct.values():
            if v >= 2:
                ret += calc_num_pairs(v)
        return ret