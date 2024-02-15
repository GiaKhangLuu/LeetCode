import numpy as np
from numpy.typing import NDArray
import json

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def get_derivative(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64], N: int, X: NDArray[np.float64], desired_weight: int) -> float:
        # note that N is just len(X)
        return -2 * np.dot(ground_truth - model_prediction, X[:, desired_weight]) / N

    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.squeeze(np.matmul(X, weights))

    learning_rate = 0.01

    def train_model(
        self, 
        X: NDArray[np.float64], 
        Y: NDArray[np.float64], 
        num_iterations: int, 
        initial_weights: NDArray[np.float64]
    ) -> NDArray[np.float64]:

        # you will need to call get_derivative() for each weight
        # and update each one separately based on the learning rate!
        # return np.round(your_answer, 5)

        weights = [initial_weights]

        for _ in range(num_iterations):
            predictions = self.get_model_prediction(X, weights[-1])
            derivative_w1 = self.get_derivative(predictions, Y, 
                                                Y.shape[0], X, 0)
            derivative_w2 = self.get_derivative(predictions, Y, 
                                                Y.shape[0], X, 1)
            derivative_w3 = self.get_derivative(predictions, Y, 
                                                Y.shape[0], X, 2)
            derivative_W = np.array([derivative_w1,
                                     derivative_w2,
                                     derivative_w3])
            new_weight = weights[-1] - self.learning_rate * derivative_W
            weights.append(new_weight)

        return np.round(weights[-1], 5)
    
    def test(self, func, inp, expectation):
        X, Y, num_iter, init_weights = inp["X"], inp["Y"], inp["num_iterations"], inp["initial_weights"]
        X, Y, init_weights = np.array(X), np.array(Y), np.array(init_weights)

        out = func(X, Y, num_iter, init_weights)
        
        if out.tolist() == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))
            print(out)
            print(expectation)
    
if __name__ == '__main__':
    file_test_case = open('./data_linear_reg_training.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.train_model, inp, expectation)