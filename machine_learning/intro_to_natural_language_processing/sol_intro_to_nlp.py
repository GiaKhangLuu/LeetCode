import json
import torch
import torch.nn as nn

color_code = {'green': '\033[92m',
            'red': '\033[91m',
            'end': '\033[0m'}

class Solution:
    def get_dataset(self, positive, negative):
        word_list = set()
        combined = positive + negative

        words_in_sentences = [sentence.split(' ') for sentence in combined]
        for sentence in words_in_sentences:
            for word in sentence:
                word_list.add(word)

        word_list = sorted(list(word_list))    
        word_dict = {word: float(word_id + 1) for word_id, word in enumerate(word_list)}
        
        encode_words = []
        for sentence in words_in_sentences:
            encode_words.append(torch.tensor([word_dict[word] for word in sentence]))
        
        return nn.utils.rnn.pad_sequence(encode_words, batch_first=True)

    def test(self, func, inp, expectation):
        positive, negative = inp["positive"], inp["negative"]

        out = func(positive, negative)

        if out.tolist() == expectation:
            print('{}Correct{}'.format(color_code['green'], color_code['end']))
        else:
            print('{}Wrong{}'.format(color_code['red'], color_code['end']))

if __name__ == '__main__':
    file_test_case = open('./data_intro_to_nlp.json')
    test_case = json.load(file_test_case)
    solution = Solution()

    for i in range(len(test_case)):
        inp, expectation = list(test_case[i].values())

        print('>>>>>>>>>>> Test case: {} <<<<<<<<<<'.format(i + 1))
        solution.test(solution.get_dataset, inp, expectation)
