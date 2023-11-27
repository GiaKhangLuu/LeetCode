import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def fourSum(self, nums, target):
        nums = sorted(nums)
        rs, quad = [], []

        def k_sum(k, start, target):
            if k != 2:
                for a in range(start, len(nums)):
                    if a > start and nums[a] == nums[a - 1]:
                        continue
                    quad.append(nums[a])
                    k_sum(k - 1, a + 1, target - nums[a])
                    quad.pop()
                return
            
            # Base case: two sum
            l, r = start, len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum > target:
                    r -= 1
                elif two_sum < target:
                    l += 1
                else:
                    rs.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        k_sum(4, 0, target)
        return rs
                                                    
    def test(self, func, inp, expectation):
        nums, target = inp['nums'], inp['target']
        out = func(nums, target)

        if len(out) == len(expectation):
            mask = [False] * len(out)
            for exp_quadruplet in expectation:
                for i, out_quadruplet in enumerate(out):
                    exp_quadruplet, out_quadruplet = sorted(exp_quadruplet), sorted(out_quadruplet)
                    if (exp_quadruplet == out_quadruplet) and (not mask[i]): 
                        mask[i] = True

            if sum(mask) == len(expectation):
                print('{}Correct{}'.format(color_code['green'], color_code['end']))
            else:
                print('{}Wrong{}'.format(color_code['red'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.fourSum, inp, expectation)

