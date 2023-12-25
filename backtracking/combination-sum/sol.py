import json
import time
import math

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:

    def combinationSum_neetcode_version(self, candidates, target):
        rs = []

        def dfs(i, curr, total):
            if total == target:
                rs.append(curr.copy())
                return
            if total > target or i >= len(candidates):
                return

            cand = candidates[i]
            left_curr = curr.copy()
            left_curr.append(cand)
            dfs(i, left_curr, total + cand)
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return rs

    def combinationSum_khang_version(self, candidates, target):
        rs = []
        for i, cand in enumerate(candidates):
            max_num_cands = target // cand
            sub_candidates = candidates[i+1:]
            for num_cands in range(1, max_num_cands + 1):
                sub_target = target - num_cands * cand
                if sub_target == 0:
                    rs.append([cand] * num_cands)
                else:
                    combinations = self.combinationSum_khang_version(sub_candidates, sub_target)
                    if len(combinations):
                        for com in combinations:
                            com.extend([cand] * num_cands)
                        rs.extend(combinations)

        return rs

    def test(self, func, inp, expectation):
        candidates, target = inp['candidates'], inp['target']
        out = func(candidates, target)

        cnt = 0
        for output_com in out:
            for exp_com in expectation:
                output_com = sorted(output_com)
                exp_com = sorted(exp_com)
                if output_com == exp_com:
                    cnt += 1
        if cnt == len(out) == len(expectation):
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.combinationSum_khang_version, inp, expectation)
        #solution.test(solution.combinationSum_neetcode_version, inp, expectation)


