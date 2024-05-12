from connect_db import session
from models import Student, Grade, Subject

results = session.query(Student.last_name, Subject.subject_name)\
    .join(Grade, Subject.subject_id == Grade.subject_id)\
    .join(Student, Grade.student_id == Student.student_id)\
    .filter(Student.student_id == 18)\
    .distinct()\
    .all()

for result in results:
    print(result)