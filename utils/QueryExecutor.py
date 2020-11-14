import snowflake.connector as sf


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

        return res