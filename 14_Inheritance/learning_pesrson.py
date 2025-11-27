class Learner:
    def greeting(self):
        return 'Hello I am Learner'
    
    def learn(self):
        return 'I am learning Python'

class Student(Person, Learner):
    pass