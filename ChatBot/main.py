from difflib import get_close_matches

def get_best_match(user_question: str, questions: dict) -> str | None:
    questions: list[str] = [q for q in questions]
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)

    if matches:
        return matches[0]


def chat_bot(knowledge: dict):
    user_input:str = input('You: ')
    best_match: str | None = get_best_match(user_input, knowledge)

    if answer := knowledge.get(best_match):
        print(f'Bot: {answer}')
    else:
        print('Bot: I have no idea')

if __name__ == '__main__':
    brain: dict = {'hello': 'hey there',
                   'how are you': 'I am good',
                   'bye': 'see you later'
                   }

    chat_bot(knowledge=brain)