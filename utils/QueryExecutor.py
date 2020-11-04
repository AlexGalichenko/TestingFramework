import snowflake.connector as sf


# conn = sf.connect(
#     account='eaebsco.us-east-1'
#     ,user='ynikolin'
#     ,password='qQ3420308674'
#     ,role='EA_QA_TEAM'
#     ,database='EA_DU_DEV'
# )
# cur = conn.cursor()
#
# cur.execute("SELECT COUNT(*) FROM DWH_CORE.S_LOAN_CIRCULATION")
# one_row = cur.fetchone()
# print(one_row[0])
# cur.close()
class QueryExecutor(object):
    def __init__(self, p_acc: str, p_user: str, p_pwd: str, p_role: str, p_db_name: str):
        self.sf_connection = sf.connect(
            account=p_acc
            , user=p_user
            , password=p_pwd
            , role=p_role
            , database=p_db_name
        )

    def execute_query(self, p_query_text: str):
        cursor = self.sf_connection.cursor()
        cursor.execute(p_query_text)
        res = cursor.fetchone()[0]
        cursor.close()
        print(res)

        return res