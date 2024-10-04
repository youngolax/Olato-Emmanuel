class University:
    def __init__(self):
        self.student_name = ['Odongo', 'Suzan']
        self.course_unit = ['Data Communication', 'Introduction to Cybersecurity']
        self.lecturer_name = ['Prof Tushabe', 'Dr.Olax']
    def students(self):
        return f"Students: {','.join(self.student_name)}"
    def courses(self):
        return f"Courses: {','.join(self.course_unit)}"
    def lecturers(self):
        return f"Lecturers: {','.join(self.lecturer_name)}"
obj = University()
print(obj.students())
print(obj.courses())
print(obj.lecturers())

