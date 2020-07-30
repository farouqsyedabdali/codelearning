class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade


class Course:
  course_list = []
  students = []
  def __init__(self, course_name, grade, max_students):
    self.course_name = course_name
    self.grade = grade
    self.max_students = max_students
    Course.course_list.append(self.course_name)


  def addStudent(self, student):
    if len(Course.students) < self.max_students:
      Course.students.append(student)
      print(f"{s.name} has been registered into {c.course_name}")
    else:
      print(f"{student.name} is not eligable for this class!")
      self.selectCourse(student)

  
  def selectCourse(self, student):
    print(Course.course_list)
    while True:
      selection = input(f"{student.name}, Select a course (case sensitive): ")
      if selection in Course.course_list:
        self.addStudent(student)
        break
      elif selection not in Course.course_list:
        print("Choose a course in the list!")


while True:
  c = Course(input("Course Name: "), int(input("Grade: ")), int(input("Max Students: ")))
  status = input("Want to add another course? Y/N: ").lower()
  if status == "n":
    break
  else:
    pass

print(c.course_list)

while True:
  s = Student(input("Student Name: "), int(input("Grade: ")))
  c.selectCourse(s)
  status = input("Want to add another student? Y/N: ").lower()
  if status == "n":
    break
  elif status == "y":
    pass

