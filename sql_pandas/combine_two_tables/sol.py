import json
import pandas as pd

color_code = {'green': '\033[92m',
              'red': '\033[91m',
              'end': '\033[0m'}

class Solution:
    def combine_two_tables(self, person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
        person_with_address = person.join(address.set_index("personId"), on="personId", how="left")
        person_with_address = person_with_address[["firstName", "lastName", "city", "state"]]
        return person_with_address

    def test(self, func, inp, expectation):
        person_col_names = inp['person_table']['column_names']
        person_ids = inp['person_table']['personId']
        person_lastnames = inp['person_table']['lastName']
        person_firstnames = inp['person_table']['firstName']

        person_data = []
        for p_id, lastname, firstname in zip(person_ids, person_lastnames, person_firstnames):
            person_data.append([p_id, lastname, firstname])
        person = pd.DataFrame(person_data, columns=person_col_names)

        address_col_names = inp['address_table']['column_names']
        address_ids = inp['address_table']['addressId']
        address_person_ids = inp['address_table']['personId']
        address_cities = inp['address_table']['city']
        address_states = inp['address_table']['state']

        address_data = []
        for a_id, person_id, city, state in zip(address_ids, address_person_ids, address_cities, address_states):
            address_data.append([a_id, person_id, city, state])
        address = pd.DataFrame(address_data, columns=address_col_names)

        output_col_names = expectation['column_names']
        output_firstname = expectation['firstName']
        output_lastname = expectation['lastName']
        output_city = expectation['city']
        output_state = expectation['state']

        output_data = []
        for firstname, lastname, city, state in zip(output_firstname, output_lastname, output_city, output_state):
            output_data.append([firstname, lastname, city, state])
        output = pd.DataFrame(output_data, columns=output_col_names)

        rs = func(person, address)

        rs = rs.where(pd.notna(rs), None)

        count = 0
        for colname in output_col_names:
            rs_data = rs[colname].tolist()
            expectation_data = output[colname].tolist()
            if rs_data == expectation_data:
                count += 1

        if count == len(output_col_names):
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
        solution.test(solution.combine_two_tables, inp, expectation)