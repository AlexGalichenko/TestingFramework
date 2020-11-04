# class SnowflakeConnector(object):
import snowflake.connector as sf

conn = sf.connect(
    user='ynikolin'
    ,role='EA_QA_TEAM'
    ,database='EA_DU_DEV'
    ,password='qQ3420308674'
    ,account='eaebsco.us-east-1'
)

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM DWH_CORE.S_LOAN_CIRCULATION")
one_row = cur.fetchone()
print(one_row[0])
cur.close()