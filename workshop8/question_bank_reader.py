question_bank_path: str = "C:\\Users\\tavkh\\PycharmProjects\\Python105\\workshop8\\question_bank.txt"


with open(question_bank_path) as f:
    current_question: str = ""
    questions: dict = {}
    
    for line in f.readlines():
        key, value = line.split(':')
        value = value.strip('\n')
        if key == 'Question':
            current_question = value
            questions[current_question] = [] 
        else:
            questions[current_question].append(value)
        
    print(questions)

