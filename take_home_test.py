import unittest
import requests
import json 
import unittest.mock
import pytest


### FIRST EXERCISE 
BASE_URL = 'https://test.com'

def create_uid(name:str, dob:str, gender:str):
    if name and dob and gender:
        name_list = [n[:2] for n in name.split(' ')]
        first_and_last = ''.join(name_list)
        birth_year = dob[:4]
        gender_initial = gender[:1]
        uid = f"{first_and_last}{birth_year}{gender_initial}".upper()
        return { "identifier": uid}, 200
    else:
        return {'error': "Missing required input"}, 400
    
def create_uid_api(name, dob, gender):
    API_ENDPOINT = BASE_URL + f'/patients/identifier?name={name}&dob={dob}&gender={gender}'
    response = requests.post(url = API_ENDPOINT)
    return response

class TestCreateIdentifier(unittest):

    @pytest.fixture()
    def mock_uid_info(self):
        """Returns static identifier data"""
        with open("resources/mock_data.json") as f:
            return json.load(f)
    
    @patch('aluna.tests.create_uid_api')
    def test_create_uid_success(self, mock_create_uid_api):
        """Given the data, test that the unique identifier is generated
        correctly."""
        response = mocker.Mock()
        response.json = mocker.Mock(return_value='TENE2023F')
        response.status_code = HTTPStatus.OK
        mocker.patch("app.requests.get", return_value=response)
        uid_info = create_uid(name='Test New', dob='2023-02-27', gender='Female')
        assert uid_info['identifier'] == mock_create_uid_api.return_value


### SECOND EXERCISE 
def validate_identifier(identifier) -> Any:
    url = BASE_URL + f'/identity?identifier={identifier}'
    response = requests.get(url)
    return response

class ValidateStoringIdentifier(unittest):
    @pytest.fixture()
    def mock_uid_info(self):
        with open("resources/mock_data.json") as f:
            return json.load(f)

    def success(self):
        new_identifier = create_uuid('Trisha Aguinaldo', '1993-02-07', 'Female')
        response = validate_identifier(new_identifier)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.body, {})

    def error(self):
        response = validate_identifier('INVALIDINDENTIFIER')
        self.assertEqual(response.status_code, 500)
        self.assertIsNotNone(response.error)

    def duplicate_identifier(self):
        response = validate_identifier('JUGO1940M')
        self.assertEqual(response.status_code, 409)
        self,.assertEqual(response.error, 'The record already exists')

### THIRD EXERCISE
""" I'm not quite sure if the test requires me to 
write E2E tests or frontend tests. I know how to do both 
but for JavaScript/React and Nightwatch/Selenium only. I 
assume that this task wants me to write manual test. Apologies if 
I misunderstood this exercise.
"""

#### Search Bar Patient Identifier
"""
1. Write a test to make sure that rectangle 2 and 
rectagle 1 renders on screen load. 
2. Both the text box and the "Find Patient" button have 
the correct placeholder/texts.
3. There are no duplicate inputs.
4. If a valid patient identifier is entered, the user is 
redirected to the correct patient identifier screen (rectangle 7)
4. Else, the user is redirected to the "No patient matches the 
identifier" page (rectangle 4)
"""

#### No Patient Matches
"""
1. Write a test to make sure all text in the screen renders: "< Back",
"No patient matches the identifier", and "<idenfier>"
2. User is redirected to the previous page if they click the "< Back" button
"""

#### Patient Found
"""
1. Write a test to make sure all text in the screen renders: "< Back",
"Patient found", and the data.
2. Make sure that all fields (name, dob, and gender) are the correct values
based on the identifier
3. User is redirected to the previous page if they click the "< Back" button
"""