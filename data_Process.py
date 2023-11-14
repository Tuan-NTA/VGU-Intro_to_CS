#open the dataset
import re
def read_dataset(file_path):
    dataset = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                pattern = r'\[Q\]\s(.*?)\s\[G\]\s(.*?)\s\[R\]\s(.*?)\s\[A\]\s(.*)'
                match = re.search(pattern, line)
                if match:
                    question, guessing_keywords, required_keywords, answer = match.groups()
                    dataset.append((question.lower(), guessing_keywords.lower().split(', '), required_keywords.lower().split(', '), answer))
                else:
                    pass

    return dataset

def calculate_probability(guessing_keywords, user_input):
    keyword_count = len(guessing_keywords)
    overlapping_count = sum(keyword in user_input for keyword in guessing_keywords)
    return overlapping_count / keyword_count

def get_answer(question, guessing_keywords, required_keywords, dataset):
    max_probability = 0
    best_answer = None

    for item in dataset:
        keywords = item[2]
        if all(keyword in question for keyword in keywords):
            probability = calculate_probability(guessing_keywords, question)
            if probability > max_probability:
                max_probability = probability
                best_answer = item[3]

    return best_answer
dataset = read_dataset("dataset.txt")
def answer(userinput):
    user_input = userinput.lower()

   
    matching_answer = None
    for item in dataset:
        guessing_keywords = item[1]
        required_keywords = item[2]
        if all(keyword in user_input for keyword in required_keywords):
            matching_answer = get_answer(user_input, guessing_keywords, required_keywords, dataset)
            if matching_answer:
                return matching_answer
            else:
                return "I'm sorry, I cannot answer that question"
