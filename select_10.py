from connect_db import session
from models import Student, Teacher, Subject, Group

results = session.query(Student.last_name, Subject.subject_name, Teacher.last_name)\
    .select_from(Student)\
    .join(Teacher, Subject.teacher_id == Teacher.teacher_id)\
    .filter(Student.student_id == 15)\
    .filter(Teacher.teacher_id == 3)\
    .all()

for result in results:
    print(result)