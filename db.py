from sqlalchemy import create_engine, text

# print(sqlalchemy.__version__)
connection_db_string = "mysql+pymysql://y7b16ohh4pjqgt6nktmr:pscale_pw_uQs2AIRZJKqR5O7AcA3sxXh7bYnCJHPOTNAzhfJGO4N@aws.connect.psdb.cloud/jobapplicationapp?charset=utf8mb4"
engine = create_engine(
    connection_db_string,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem",
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    rd = [dict(row) for row in result.all()]
    print(rd)