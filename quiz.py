import datetime
import random

from questions import Add, Multiply

class Quiz:
    questions = []
    user_answers = []

    time_format = '%H:%M %p'

    def __init__(self):
        # generate 10 random questions with numbers from 1 to 10
        number_of_questions = int(input(
                'How many questions you would like our quiz to contain? '
        ))
        min = int(input(
                'What number would be the minimal in our quiz? '
        ))
        max = int(input(
                'What number would be the maximal in our quiz? '
        ))
        for _ in range(number_of_questions):
            type = random.randrange(0, 3)
            n1 = random.randint(min, max)
            n2 = random.randint(min, max)
            # add these questions into self.questions
            if type == 0:
                self.questions.append(Add(n1, n2))
            elif type == 1:
                self.questions.append(Subtract(n1, n2))
            elif type == 2:
                self.questions.append(Multiply(n1, n2))

    def take_quiz(self):
        print('=== THE QUIZ ===')

        # log the start time
        quiz_start = datetime.datetime.now()
        print('You started the quiz at {}\n'.format(
                quiz_start.strftime(self.time_format)
        ))

        # ask all of the questions
        for question in self.questions:
            result = self.ask(question)
            # log if they got the question right
            if result[0]:
                print('You got this one right in {} second(s)!!!\n'.format(
                        result[1].seconds)
                )

        # log the end time
        quiz_end = datetime.datetime.now()
        print('The quiz finished at {}\n'.format(
                quiz_end.strftime(self.time_format)
        ))

        # show a summary
        self.summary(quiz_start, quiz_end)

    def ask(self, question):
        # log the start time
        question_start = datetime.datetime.now()
        print('You started this question at {}'.format(
                question_start.strftime(self.time_format)
        ))

        # capture the answer
        user_answer = input('Solve it: {} = '.format(question.text))

        # check the answer
        result = int(user_answer) == question.answer
        self.user_answers.append(int(user_answer))

        # log the end time
        question_end = datetime.datetime.now()
        print('You finished this question at {}\n'.format(
                question_end.strftime(self.time_format)
        ))

        # send back the elapsed time, too
        elapsed_time = question_end - question_start

        # if the answer is right, send back True
        if result:
            return [True, elapsed_time]

        # otherwise, send back False
        else:
            return [False, elapsed_time]

    # 'qs' for 'quiz_start', 'qe' for 'quiz_end'
    def summary(self, qs, qe):

        # print how many you got right and the total # of questions. 5/10
        righties = 0
        for index in range(len(self.questions)):
            if self.questions[index].answer == int(self.user_answers[index]):
                righties += 1
        print('Right answers ::: {}/{} !!!'.format(
                righties, len(self.questions)
        ))

        # print the total time for the quiz
        total_seconds = (qe - qs).seconds
        quiz_time_minutes = total_seconds // 60
        quiz_time_seconds = total_seconds % 60
        print('Total time for the quiz ::: {}:{} !!!\n'.format(
                quiz_time_minutes, quiz_time_seconds
        ))

    def show_questions(self):
        for question in self.questions:
            print('({}) {} = {};'.format(
                    self.questions.index(question) + 1,
                    question.text, question.answer
            ))

my_quiz = Quiz()
my_quiz.take_quiz()
