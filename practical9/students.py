class students:
    def __init__(self, name, major, portfolio, project, exam):
        self.name=name
        self.major = major
        self.portfolio = portfolio
        self.project = project
        self.exam = exam
s = students("name","major",0,0,0)
s.name = input("name is:")
s.major = input("major is")
if s.major != "BMS" and s.major != "BMI":
    print("error")
s.portfolio = int(input("the score for code portfolio is:"))
if s.portfolio > 100 or s.portfolio < 0:
    print("error")
s.project = int(input("the score for group project is:"))
if s.project > 100 or s.project < 0:
    print("error")
s.exam = int(input("the exam score is:"))
if s.exam > 100 or s.exam < 0:
    print("error")
print(s.name,s.major,s.portfolio,s.project,s.exam)