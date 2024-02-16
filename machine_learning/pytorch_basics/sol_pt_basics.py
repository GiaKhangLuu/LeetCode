import json
from numpy.typing import NDArray
import torch
import torch.nn
#from torchtyping import TensorType

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:

    def reshape(self, to_reshape):
        # torch.reshape() will be useful - check out the documentation
        m, n = to_reshape.shape
        return torch.reshape(to_reshape, (m * n // 2, 2))

    def average(self, to_avg):
        # torch.mean() will be useful - check out the documentation
        return torch.mean(to_avg, dim=0)

    def concatenate(self, cat_one, cat_two):
        # torch.cat() will be useful - check out the documentation
        return torch.cat((cat_one, cat_two), dim=1)

    def get_loss(self, prediction, target):
        # torch.nn.functional.mse_loss() will be useful - check out the documentation
        return torch.nn.functional.mse_loss(prediction, target)

    def test(self, inp, expectation):
        cmd = inp["cmd"]
        out = None
        if cmd == "reshape":
            to_reshape = torch.tensor(inp["to_reshape"])
            out = self.reshape(to_reshape)
        elif cmd == "average":
            to_avg = torch.tensor(inp["to_avg"])
            out = self.average(to_avg)
        elif cmd == "concatenate":
            cat_one = torch.tensor(inp["cat_one"])
            cat_two = torch.tensor(inp["cat_two"])
            out = self.concatenate(cat_one, cat_two)
        else:
            prediction = torch.tensor(inp["prediction"])
            target = torch.tensor(inp["target"])
            out = self.get_loss(prediction, target)

        if (out == torch.tensor(expectation)).all():
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_pt_basics.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)