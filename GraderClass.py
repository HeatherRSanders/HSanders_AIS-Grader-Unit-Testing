import sys
class Grader:
    def gradeInfo(self):
        name = input("Type your name here: ")
        assignment = input("Type an assignment name: ")
        try:
            grade = float(input("Enter the grade number for that assignment: "))
        except:
            grade = -1
            
        if grade <=100 and grade >=90:
            print("Hello %s\nYour letter grade for %s assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements." % (name, assignment))
        elif grade <90 and grade >=80:
            print("Hello %s\nYour letter grade for %s assignment is as follows: B\nAssignment details:\nYou have met most of the assignment's requirements." % (name, assignment))
        elif grade <80 and grade >=70:
            print("Hello %s\nYour letter grade for %s assignment is as follows: C\nAssignment details:\nYou have met many of the assignment's requirements." % (name, assignment))
        elif grade <70 and grade >=60:
            print("Hello %s\nYour letter grade for %s assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements." % (name, assignment))
        elif grade <60 and grade >=0:
            return grade
        else:
            return "You did not entered a grade number between 0 ant 100."
# newGrader = Grader()
# print(newGrader.gradeInfo())