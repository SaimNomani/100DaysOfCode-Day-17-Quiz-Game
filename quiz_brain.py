

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.user_response=''
        self.user_score=0
        self.question_list = question_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        self.user_response=(input(f"Q.{self.question_number}: {current_question.text} (True/False): ")).title()
        self.is_answer_correct(self.user_response, current_question.answer)

    def still_has_questions(self):
        return self.question_number <len(self.question_list)

    def is_answer_correct(self, user_ans, correct_ans):
        if user_ans==correct_ans:
            self.user_score+=1
            print(f"You got it right\nIt was {correct_ans}\nYour score: {self.user_score}/{self.question_number}\n")
            return
        print(f"Wrong answer\nIt was {correct_ans}\nYour score: {self.user_score}/{self.question_number}\n")



