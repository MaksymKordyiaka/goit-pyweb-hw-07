from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Group, Teacher, Subject, Grade
from datetime import datetime
import random

engine = create_engine('sqlite:///study.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

if __name__ == '__main__':

    if session.query(Group).count() == 0:
        groups = ["Group A", "Group B", "Group C"]
        for group_name in groups:
            group = Group(group_name=group_name)
            session.add(group)
        session.commit()

    if session.query(Student).count() == 0:
        for _ in range(30):
            first_name = fake.first_name()
            last_name = fake.last_name()
            group_id = random.randint(1, 3)
            student = Student(first_name=first_name, last_name=last_name, group_id=group_id)
            session.add(student)
        session.commit()

    if session.query(Teacher).count() == 0:
        for _ in range(3):
            teacher = Teacher(first_name=fake.first_name(), last_name=fake.last_name())
            session.add(teacher)
        session.commit()

    if session.query(Subject).count() == 0:
        subjects = {
            "Mathematics": 1,
            "Physics": 1,
            "Chemistry": 2,
            "Biology": 2,
            "History": 3,
            "Literature": 3
        }
        for subject_name, teacher_id in subjects.items():
            subject = Subject(subject_name=subject_name, teacher_id=teacher_id)
            session.add(subject)
        session.commit()

    if session.query(Grade).count() == 0:

        # Початок семестру на 1 лютого
        start_date = datetime(2024, 2, 1)
        end_date = datetime(2024, 5, 31)
        for student in session.query(Student):
            for subject in session.query(Subject):
                for _ in range(3):
                    grade_date = fake.date_time_between(start_date=start_date, end_date=end_date)
                    grade_value = random.randint(51, 100)  # Випадкова оцінка від 60 до 100
                    grade = Grade(
                        student_id=student.student_id,
                        first_name=student.first_name,
                        last_name=student.last_name,
                        subject_id=subject.subject_id,
                        grade_value=grade_value,
                        grade_date=grade_date
                    )
                    session.add(grade)
        session.commit()
