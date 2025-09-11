from data import local_question_data
from question_model import Question
from quiz_brain import QuizBrain
import requests
import html
from ui import QuizUI

url = "https://opentdb.com/api.php?amount=10&type=boolean"

# fetching the data from the API if available, otherwise using local data.
try:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    question_data = response.json()["results"]
except (requests.RequestException, ValueError):
    print("Could not access the API. Using local questions instead.")
    question_data = local_question_data

question_bank = []

for i in question_data:
        question_bank.append(Question(html.unescape(i["question"]), i["correct_answer"]))


quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
