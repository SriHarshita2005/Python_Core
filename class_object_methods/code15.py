# Create a class Course that:
# Tracks total courses created.
# Each course has a title, duration, and enrolled_students.
# Provides a method to enroll a new student.
# Allows updating the minimum duration for a valid course across all instances.
# Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.Creating multiple courses.
# 2.Enrolling students.
# 3.Updating minimum duration and checking durations.

class Course:
    total_courses=0
    def __init__(self,title,duration,enrolled_students):
        self.title=title
        self.duration=duration
        self.enrolled_students=enrolled_students
        Course.total_courses+=1
    def enroll(self):
        self.enrolled_students+=1

    @classmethod
    def update_min_duration(cls, new_duration):
        cls.min_duration = new_duration
        print("Minimum duration updated to:", cls.min_duration)

    @staticmethod
    def valid_duration(duration):
        return duration > 0 and duration <= 100
c1 = Course("Python", 30, 10)
c2 = Course("Java", 40, 5)
c3 = Course("C++", -5, 2)   # invalid duration
courses = [c1, c2, c3]
c1.enroll()
c2.enroll()
print("Before update:")
for c in courses:
    print(c.title,
          "| Duration valid:", Course.valid_duration(c.duration),
          "| Students:", c.enrolled_students)
Course.update_min_duration(10)
print("\nAfter update:")
for c in courses:
    print(c.title,
          "| Duration valid:", Course.valid_duration(c.duration),
          "| Students:", c.enrolled_students)
print("\nTotal Courses:", Course.total_courses)