import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def findMedianSortedArrays_version_2(self, nums1, nums2):
        nums1, nums2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        total_len = len(nums1) + len(nums2)
        num_left_total = math.ceil(total_len / 2)
        num_right_total = total_len - num_left_total
        
        l, r = 0, len(nums1)
        
        while True:
            partition_s1 = (l + r) // 2 
            partition_s2 = num_left_total - partition_s1
            max_left_s1 = nums1[partition_s1 - 1] if partition_s1 > 0 else float('-inf')
            min_right_s1 = nums1[partition_s1] if partition_s1 < len(nums1) else float('inf')
            max_left_s2 = nums2[partition_s2 - 1] if partition_s2 > 0 else float('-inf')
            min_right_s2 = nums2[partition_s2] if partition_s2 < len(nums2) else float('inf')

            if max_left_s1 <= min_right_s2 and max_left_s2 <= min_right_s1:
                if total_len % 2 == 0:
                    return (max(max_left_s1, max_left_s2) + min(min_right_s1, min_right_s2)) / 2
                else:
                    return max(max_left_s1, max_left_s2)
            if max_left_s1 > min_right_s2:
                r = partition_s1 - 1
            if max_left_s2 > min_right_s1:
                l = partition_s1 + 1

    def findMedianSortedArrays_version_1(self, nums1, nums2):
        nums1, nums2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)

        if len(nums1) == 0 and len(nums2) == 1:
            return nums2[0]

        total_len = len(nums1) + len(nums2)
        num_left_total = math.ceil(total_len / 2)
        num_right_total = total_len - num_left_total
        
        l, r = 0, len(nums1)
        m = (l + r) // 2 
        left_nums1, right_nums1 = nums1[:m], nums1[m:]
        partition_nums2 = num_left_total - len(left_nums1)
        left_nums2, right_nums2 = nums2[:partition_nums2], nums2[partition_nums2:]
        left_total = left_nums1.copy()
        left_total.extend(left_nums2)
        right_total = right_nums1
        right_total.extend(right_nums2)

        while max(left_total) > min(right_total):
            if len(left_nums1) == 0 or len(right_nums2) == 0 or left_nums1[-1] > right_nums2[0]:
                r = m - 1
            if len(left_nums2) == 0 or len(right_nums1) == 0 or left_nums2[-1] > right_nums1[0]:
                l = m + 1
            m = (l + r) // 2 if r >= 0 else 1
            left_nums1, right_nums1 = nums1[:m], nums1[m:]
            partition_nums2 = num_left_total - len(left_nums1)
            left_nums2, right_nums2 = nums2[:partition_nums2], nums2[partition_nums2:]
            left_total = left_nums1.copy()
            left_total.extend(left_nums2)
            right_total = right_nums1
            right_total.extend(right_nums2)
        if total_len % 2 == 0:
            return (max(left_total) + min(right_total)) / 2
        else:
            return max(left_total)

    def test(self, func, inp, expectation):
        nums1, nums2 = inp['nums1'], inp['nums2']
        out = func(nums1, nums2)
             
        if out == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print('{}Expectation: {}{}'.format(color_code['red'], expectation, color_code['end']))
            print('{}Output: {}{}'.format(color_code['red'], out, color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        #solution.test(solution.findMedianSortedArrays_version_1, inp, expectation)
        solution.test(solution.findMedianSortedArrays_version_2, inp, expectation)


