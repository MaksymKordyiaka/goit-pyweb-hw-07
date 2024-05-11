from models import Student, Group, Teacher, Subject, Grade
from connect_db import session

from faker import Faker

fake = Faker()

if __name__ == '__main__':
    students = 10

    for _ in range(students):
        student = Student(first_name=fake.first_name(), last_name=fake.last_name())
        session.add(student)

    session.commit()