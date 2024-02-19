import json
import torch
import torch.nn as nn

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.embed_layer = nn.Embedding(vocabulary_size, 16)
        self.fc = nn.Linear(16, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Hint: The embedding layer outputs a B, T, embed_dim tensor
        # but you should average it into a B, embed_dim tensor before using the Linear layer

        # Return a B, 1 tensor and round to 4 decimal places
        embeddings = self.embed_layer(x)
        averaged = torch.mean(embeddings, dim=1)
        output = self.sigmoid(self.fc(averaged))

        return torch.round(output, decimals=4)

    def test(self, x, expectation):
        x = torch.tensor(x) 
        out = self.forward(x).detach()

        if (out == torch.tensor(expectation)).all():
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_sentiment_analysis.json')
    test_case = json.load(file_test_case)

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())
        vocabulary_size, x = inp["vocabulary_size"], inp["x"]
        solution = Solution(vocabulary_size)

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(x, expectation)