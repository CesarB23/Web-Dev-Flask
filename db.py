from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
# print(sqlalchemy.__version__)
CONNECTION_DB_STRING = os.getenv("CONNECTION_DB_STRING")
engine = create_engine(
    CONNECTION_DB_STRING,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)
print(CONNECTION_DB_STRING)
def load_jobs_fromdb():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
        return jobs

def load_job_fromdb(id):
 with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id={id}"))
    rows = result.all()
    columnn_names = result.keys()
    if len(rows) == 0:
       return None
    else:
       return dict(zip(columnn_names,rows[0]))   
    
    

