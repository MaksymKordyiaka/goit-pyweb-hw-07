from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date, Float

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.group_id'))

class Group(Base):
    __tablename__ = 'groups'

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(50), nullable=False)
    students = relationship("Student")

class Teacher(Base):
    __tablename__ = 'teachers'

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    subjects = relationship("Subject")

class Subject(Base):
    __tablename__ = 'subjects'

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))

class Grade(Base):
    __tablename__ = 'grades'

    grade_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    grade_value = Column(Float, nullable=False)
    grade_date = Column(Date, nullable=False)
