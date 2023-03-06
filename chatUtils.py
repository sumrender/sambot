import os
from dotenv import load_dotenv
from gpt_index import GPTSimpleVectorIndex

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANSWER_SEQUENCE = "\nAI:"
QUESTION_SEQUENCE = "\nHuman: "
MAX_CONTEXT_QUESTIONS = 10
INSTRUCTIONS = """Act like you are a chatbot for accops.com.
You have to help users with the product details, asking them
which product the user needs help with, in the first question only.
"""
previous_questions_and_answers = []


def ask_bot(new_question):
    input_index = './index.json'
    index = GPTSimpleVectorIndex.load_from_disk(input_index)

    context = ""
    for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
        context += QUESTION_SEQUENCE + question + ANSWER_SEQUENCE + answer

    context += QUESTION_SEQUENCE + new_question + ANSWER_SEQUENCE
    response = index.query(INSTRUCTIONS + context, response_mode="compact")
    previous_questions_and_answers.append((new_question, response.response))
    return response.response


if __name__ == "__main__":
    while True:
        new_question = input("Ask the bot: \n")
        print(ask_bot(new_question))
