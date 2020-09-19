import random

class Applicant:
    def __init__(self):
        self.luck = random.random()
        self.capability = random.random()
    
    def score(self):
        return self.luck * 5 + self.capability * 95

applicants = []
for i in range(20000):
    applicants.append(Applicant())

applicants.sort(reverse=True, key=lambda x: x.score())

for i in range(10):
    print(f"{applicants[i].score()}={applicants[i].capability*100} + {applicants[i].luck*100}")