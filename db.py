from sqlalchemy import create_engine, text
import os

# print(sqlalchemy.__version__)
connection_db_string = "mysql+pymysql://9my4d87sby3jbk1w8y16:pscale_pw_eNYMWxFGvDzP63KFSLVK4M96FF4uy5m3CaPzWERDTZM@aws.connect.psdb.cloud/jobapplicationapp?charset=utf8mb4"
engine = create_engine(
    connection_db_string,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

def load_jobs_fromdb():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        column_names = result.keys()
        jobs = []
        for row in result.all():
            jobs.append(dict(zip(column_names, row)))
        return jobs