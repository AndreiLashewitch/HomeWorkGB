tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
def generation_tuple(tutors, klasses):
    for item in range(max(len(tutors), len(klasses))):
        if i < len(tutors) and i < len(klasses):
            pair = (tutors[i], klasses[i])
        elif i > len(klasses):
            pair = (tutors[i], None)
        else:
            pair = (tutors[i], None)
        yield pair

if __name__ == "__mane__":
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    new_generation_tuple = generation_tuple(tutors, klasses)
    for i in new_generation_tuple:
        print(i)