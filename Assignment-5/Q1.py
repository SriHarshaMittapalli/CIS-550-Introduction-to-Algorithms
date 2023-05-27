class Solution:
    def longestPalindrome(self, s):
        #input: string
        #output: longest Palindrome
        # Time complexity using DP is O(n^2), Time complexity using brute-force attack is O(n^3)
        input_size, input_index = len(s), 0; dynamic_programming_table, longest_string = [[0] * input_size for i in range(input_size)], "null"
        while input_index < input_size: dynamic_programming_table[input_index][input_index], longest_string = 1, s[input_index]; input_index = input_index + 1
        for input_index in range(input_size - 1):
            if s[input_index] == s[input_index + 1]: dynamic_programming_table[input_index][input_index + 1], longest_string = 1, s[input_index:input_index + 2]
        for length_of_palindrome in range(3, input_size+1):
            for input_row in range(input_size-length_of_palindrome + 1):
                input_column = input_row + length_of_palindrome - 1
                if (s[input_row] == s[input_column]) and (dynamic_programming_table[input_row + 1][input_column - 1]): dynamic_programming_table[input_row][input_column], longest_string = 1, s[input_row:input_column + 1]
        return longest_string

if __name__ == "__main__":
    test = Solution()
    res = test.longestPalindrome("abcdzdcab")
    if res == 'cdzdc':
        print('PASS')