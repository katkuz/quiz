import json
import sys
import requests

api_url = 'https://bjornkjellgren.se/quiz/v2/questions'


def get_questions():
    """ Return a json with all questions and answers from API"""
    try:
        response_api = requests.get(api_url)
        questions_and_answers = json.loads(response_api.text)['questions']
    except requests.ConnectionError:
        print("Can't get questions and answers. Quitting")
        sys.exit()
    return questions_and_answers


def send_statistics(question_id, correctness):
    """ Send statistics with correct/incorrect answered question back to API"""
    try:
        response = requests.post(
            api_url, json={'id': question_id, 'correct': correctness}
        )
        if response.status_code != 200:
            print("Can't reach API to send statistics")
    except requests.ConnectionError:
        print("Can't reach API to send statistics")
