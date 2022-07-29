import time
import json

"""
Pseudo code:
1. Create dictionary: key is the digit/letter, value is array contains
    index of the corresponding digit/letter in string input.
2. Find even longest palindromic substring
3. Find odd longest palindromic substring
"""

class Test:

    def verifyAnswer(self, expected, output):
        return True if len(expected) == len(output) else False

class Solution:

    def longestPalindrome(self, s):
   
        letter_to_index_dict = dict()
        result = ''

        # Create dictionary
        for i in range(len(s)):
            letter = s[i]
            # letter didnt exist in dict
            if not letter_to_index_dict.get(letter):
                letter_to_index_dict[letter] = [i]
            else:
                letter_to_index_dict[letter].append(i)

        if len(list(letter_to_index_dict.keys())) == 1:
            return s

        even_longest_palindrome = self.findEvenLongestPalindrome(s, letter_to_index_dict)
        odd_longest_palindrome = self.findOddLongestPalindrome(s, letter_to_index_dict)

        result = (odd_longest_palindrome if 
                len(odd_longest_palindrome) > len(even_longest_palindrome) else 
                even_longest_palindrome)

        result = s[0] if result == '' else result

        return result

    def findEvenLongestPalindrome(self, s, letter_to_index_dict):
        
        even_longest_palindrome = ''

        for letter in list(letter_to_index_dict.keys()):
            letter_indexs = letter_to_index_dict[letter]

            for i in range(len(letter_indexs) - 1):
                left_index, right_index = letter_indexs[i], letter_indexs[i + 1]

                if left_index != right_index - 1:
                    continue

                # Detect letter appear twice in a row, start to 
                # find palindromic
                left_char, right_char = [], []
                while (left_index >= 0) and (right_index < len(s)) and (s[left_index] == s[right_index]):
                    left_char.append(s[left_index])
                    right_char.append(s[right_index])
                    left_index -= 1     
                    right_index += 1

                left_char.reverse() 
                left_half_string = ''.join(left_char)
                right_half_string = ''.join(right_char)
                temp = left_half_string + right_half_string

                if len(temp) > len(even_longest_palindrome):
                    even_longest_palindrome = temp
                 
        return even_longest_palindrome                

    def findOddLongestPalindrome(self, s, letter_to_index_dict):

        odd_longest_palindrome = ''

        for letter in list(letter_to_index_dict.keys()):
            letter_indexs = letter_to_index_dict[letter]

            for i in range(len(letter_indexs)):
                curr_index = letter_indexs[i]
                left_index, right_index = curr_index - 1, curr_index + 1

                # Detect letter appear twice in a row, start to 
                # find palindromic
                left_char, right_char = [], []
                middle_char = s[curr_index]
                while (left_index >= 0) and (right_index < len(s)) and (s[left_index] == s[right_index]):
                    left_char.append(s[left_index])
                    right_char.append(s[right_index])
                    left_index -= 1     
                    right_index += 1

                left_char.reverse()                    
                left_half_string = ''.join(left_char)
                right_half_string = ''.join(right_char)
                temp = left_half_string + middle_char + right_half_string

                if len(temp) > len(odd_longest_palindrome):
                    odd_longest_palindrome = temp
                 
        return odd_longest_palindrome                

##################################################
# Test 
##################################################

file_test_case = open('./data.json')
test_case = json.load(file_test_case)

for i in range(len(test_case)):
    input, expected = list(test_case[i].values())
    
    start = time.time()
    output = Solution().longestPalindrome(input)
    end = time.time()
    result = Test().verifyAnswer(expected, output)
    color = '\033[92m' if result else '\033[31m'


    print('----------- Test case ', i + 1, '---------------')
    print('>>>>>>>>>>> Output ', output)
    print('>>>>>>>>>>> Expected ', expected)
    print('>>>>>>>>>>> Result: {}{}{}'.format(color, result, '\033[0m'))
    print('>>>>>>>>>>> Total time: {} ms'.format(round(end - start, 4)))

