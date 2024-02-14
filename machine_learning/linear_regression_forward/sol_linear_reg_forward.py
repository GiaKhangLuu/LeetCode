import json
import numpy as np
from numpy.typing import NDArray

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)

        return np.round(np.matmul(X, weights), 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # model_prediction is an Nx1 NumPy array
        # ground_truth is an Nx1 NumPy array
        # HINT: np.mean(), np.square() will be useful
        # return round(your_answer, 5)
        N = len(ground_truth)
        return round(np.mean(np.square(model_prediction - ground_truth)), 5)

    def test(self, inp, expectation):
        cmd = inp["cmd"]
        out = None
        if cmd == "get_model_prediction":
            X, weights = inp["X"], inp["weights"]
            out = self.get_model_prediction(X, weights)
        else:
            model_prediction, ground_truth = inp["model_prediction"], inp["ground_truth"]
            ground_truth = np.array(ground_truth)
            out = self.get_error(model_prediction, ground_truth)
        
        if out.tolist() == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)

if __name__ == '__main__':
    file_test_case = open('./data_linear_reg_forward.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(inp, expectation)