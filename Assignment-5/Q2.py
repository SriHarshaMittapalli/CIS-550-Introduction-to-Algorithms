class Solution(object):
    def pick(self, nums):
        """
        input: int list, numbers of coins
        output: maximum number
        """
        size_of_list = len(nums)
        dynamic_programming_1, dynamic_programming_1[0], dynamic_programming_1[1], dynamic_programming_index1 = [0] * size_of_list, nums[0], max(nums[0], nums[1]), 2
        while dynamic_programming_index1 < size_of_list: dynamic_programming_1[dynamic_programming_index1], dynamic_programming_index1 = max(dynamic_programming_1[dynamic_programming_index1 - 2]+nums[dynamic_programming_index1], dynamic_programming_1[dynamic_programming_index1 - 1]), dynamic_programming_index1 + 1
        dynamic_programming_2, dynamic_programming_2[0], dynamic_programming_2[1], dynamic_programming_index2 = [0] * size_of_list, 0, nums[1], 2
        while dynamic_programming_index2 < size_of_list: dynamic_programming_2[dynamic_programming_index2], dynamic_programming_index2 = max(dynamic_programming_2[dynamic_programming_index2 - 2]+nums[dynamic_programming_index2], dynamic_programming_2[dynamic_programming_index2 - 1]), dynamic_programming_index2 + 1
        maximum = max(dynamic_programming_1[-2], dynamic_programming_2[-1])
        return maximum
if __name__ == "__main__":
    res = Solution().pick([1, 2, 3, 4, 5, 6, 7])
    print(res)
    if res == 15:
        print('PASS')