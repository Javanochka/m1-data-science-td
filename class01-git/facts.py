#!/usr/bin/env python3
import collections
import sys


Person = collections.namedtuple('Person', ['github_login', 'first_name', 'last_name', 'facts'])
people = [
    Person(github_login='example', first_name='Name', last_name='Surname',
           facts=['Fact-right.', 'Fact-write.', 'Fact-right.']),
    Person(github_login='javanochka', first_name='Anna', last_name='Nikiforovskaja',
           facts=['I can meow like a cat', 'I am a PhD student', 'I am not Estonian']),
    Person(github_login="cat", first_name="Martha", last_name="KittyCat",
           facts=['I am a dog',"I can say meow", "I like milk"]),
    Person(github_login='tunji17', first_name='Oyetunji', last_name='Abioye',
            facts=['I am not Nigerian', 'I am a Ms student', 'I can fly']),
    Person(github_login="robin", first_name="Tweety", last_name="Bird",
           facts=["I have arms", "I can fly", "I eat worms"]),
    Person(github_login="Hawawou", first_name="Hawawou", facts=['I am a student', 'I am from Togo', 'I love cats'])
]
# facts are numerated from 0
answers = {'example': 1,
           'javanochka': 2,
           'cat': 0,
           'robin': 0}


def format_person_info(person):
    return f'Name: {person.first_name} {person.last_name}.'


def list_people():
    for p in people:
        print(f'Github login: {p.github_login}.', format_person_info(p))


def list_facts(github_login):
    found = list(filter(lambda p: p.github_login == github_login, people))
    if len(found) == 0:
        print(f'No person with login {github_login}')
    elif len(found) > 1:
        print('Github logins are not unique.')
    else:
        person = found[0]
        print(format_person_info(person), 'Facts:')
        print(*[f'{i}. {person.facts[i]}' for i in range(len(person.facts))], sep='\n')


def check_answer(github_login, answer):
    if github_login not in answers:
        print("Sorry, I don't know the answer yet")
    elif answers[github_login] == answer:
        print('You are right! This fact is actually wrong!')
    else:
        print('No, this fact is right. Try again.')


def run_cmd(input_cmd):
    tokens = input_cmd.split()
    if len(tokens) == 0:
        return
    if tokens[0] == 'exit':
        sys.exit(0)
    if tokens[0] == 'people':
        list_people()
    elif tokens[0] == 'facts':
        list_facts(tokens[1])
    elif tokens[0] == 'answer':
        check_answer(tokens[1], int(tokens[2]))
    else:
        print('No such command')


def load_answers():
    with open('answers', 'r') as f:
        for line in f:
            login, number = line.strip().split()
            answers[login] = int(number)


if __name__ == '__main__':
    print("Hi! Let's play the game of facts!")
    # load_answers()
    while True:
        print('> ', end='', flush=True)
        try:
            run_cmd(sys.stdin.readline().strip())
        except Exception: # This is a VERY bad style.
            continue
