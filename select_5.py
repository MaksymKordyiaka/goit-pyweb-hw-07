from connect_db import session
from models import Teacher, Subject

results = session.query(Teacher.last_name, Subject.subject_name)\
    .select_from(Teacher)\
    .join(Subject)\
    .filter(Teacher.teacher_id == 2)\
    .all()

for result in results:
    print(result)