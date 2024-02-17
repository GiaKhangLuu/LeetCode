import json
from numpy.typing import NDArray
import torch
import torch.nn as nn
#from torchtyping import TensorType

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution(nn.Module):
    def __init__(self):
        super().__init__()
        torch.manual_seed(0)
        # Define the architecture here
        num_inputs, num_outputs = 28 * 28, 10
        self.neural_network = nn.Sequential(
            nn.Linear(num_inputs, 512),
            nn.ReLU(),
            nn.Dropout(p=0.2),
            nn.Linear(512, num_outputs),
            nn.Sigmoid()
        )
    
    def forward(self, images):
        torch.manual_seed(0)
        output = self.neural_network(images)
        # Return the model's prediction to 4 decimal places
        return output


    def test(self, inp, expectation):
        seed = inp["seed"]
        torch.manual_seed(0)
        images = torch.randn(1, 28 * 28)

        out = self.forward(images)
        out = torch.round(out, decimals=4).detach()

        if (out == torch.tensor(expectation)).all():
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_digit_classifier.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)