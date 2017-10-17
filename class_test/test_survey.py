import unittest
from class_test.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        self.my_survey = AnonymousSurvey('')
        self.responses = ['English', 'Spanlish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_respose(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_stor_three_response(self):
        for response in self.responses:
            self.my_survey.store_respose(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
