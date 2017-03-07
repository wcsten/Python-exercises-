import random

question_list_tiger = [
    'Tiger 1',
    'Tiger 2',
    'Tiger 3',
    'Tiger 4',
    'Tiger 5'
]

question_list_bear = [
    'Bear 1',
    'Bear 2',
    'Bear 3',
    'Bear 4',
    'Bear 5'
]

question_list_turtle = [
    'Turtle 1',
    'Turtle 2',
    'Turtle 3',
    'Turtle 4',
    'Turtle 5'
]

second_question_step_list = []
third_question_step_list = []


def questions(question_list_tiger, question_list_bear, question_list_turtle, second_question_step_list):
    # Lógica para as questões relacionadas ao tigre
    question_tiger_number = random.randint(1, 5)
    question_tiger_number -= 1

    for index, obj in enumerate(question_list_tiger):
        if question_tiger_number == index:
            second_question_step_list.append(obj)

    # Lógica para as questões relacionadas ao Urso
    question_bear_number = random.randint(1, 5)
    question_bear_number -= 1

    for index, obj in enumerate(question_list_bear):
        if question_bear_number == index:
            second_question_step_list.append(obj)

    # Lógica para as questões relacionadas a Tartaruga
    question_turtle_number = random.randint(1, 5)
    question_turtle_number -= 1

    for index, obj in enumerate(question_list_turtle):
        if question_turtle_number == index:
            second_question_step_list.append(obj)

    # Lógica para mostrar a segunda lista de questões na tela
    for index, question in enumerate(second_question_step_list):
        index += 1
        print('{} - {}'.format(index, question))

def menu():
    choice = 'sim'

    while choice == 'sim':
        questions(question_list_tiger, question_list_bear, question_list_turtle, second_question_step_list)

        print('#' * 80)
        question_choice = int(input('Escolha de 1 a 3 a respectiva questão: '))
        print('#' * 80)

menu()
