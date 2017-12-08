class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.socre=score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart=Student('guohan',80)
bart.print_score()