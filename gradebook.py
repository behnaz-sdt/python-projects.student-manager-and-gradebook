class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    def add_student(self, student):
        student_id = student.get_id()

        if student_id not in self.students:
            self.students[student_id] = student
            self.grades[student_id] = {}

            print("Student added successfully.")

        else:
            print("Student already exists.")

    def add_course(self, course):
        course_code = course.course_code

        if course_code not in self.courses:
            self.courses[course_code] = course

            print("Course added successfully.")

        else:
            print("Course already exists.")

    


























