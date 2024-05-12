from sqlalchemy import func

from connect_db import session
from models import Grade

results = session.query(func.round(func.avg(Grade.grade_value), 2).label('avg_grade'))\

for result in results:
    print(result.avg_grade)
