import pandas as pd
import os
from utils.QueryExecutor import QueryExecutor
from datetime import datetime


class TestLibrary(object):
    def __init__(self, p_scripts_dir: str):
        self.scripts_dir = p_scripts_dir
        self.df_lib = self.__read_test_library()

    def print_test_library(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('max_colwidth', None)
        pd.set_option('max_columns', None)
        pd.set_option('display.width', 10000)
        print(self.df_lib)

    def __read_test_library(self) -> pd.DataFrame:
        df = pd.DataFrame()
        list_of_files = os.listdir(self.scripts_dir)
        # uid is a unique identifier of row in list of tests
        uid = 0

        for curr in list_of_files:
            df = df.append(self.__read_dq_check_info(curr, uid))
            uid = uid + 1

        df.set_index('uid', inplace=True)

        return df

    def __read_dq_check_info(self, p_file_name: str, p_uid: int) -> pd.DataFrame:
        file_path = self.scripts_dir + r'\\' + p_file_name
        res = pd.read_json(file_path)
        # add the "uid" column to the result data frame that will be used as row index
        res['uid'] = p_uid

        return res

    def __get_dq_check_property_by_name(self, p_dq_check_id: str, p_property_name: str) -> str:
        res = self.df_lib.query('dq_check_id ==\'' + p_dq_check_id + '\'')[p_property_name].values[0]

        return res

    def get_list_of_tests_by_params(self, p_params: dict) -> pd.DataFrame:
        query = str()
        is_mult_params = 1 if len(p_params) > 1 else 0

        # build a query string for self.df_lib
        # if there are multiple parameters passed to the query - add separators " & " between the parameters
        for key in p_params:
            query = query + key + '==\'' + p_params[key] + '\'' + (' & ' if is_mult_params == 1 else '')

        # also, if there are multiple parameters passed to the query - remove separators from the end of the string
        query = query if is_mult_params == 0 else query.strip().rstrip(' &')

        res = self.df_lib.query(query)

        return res

lib = TestLibrary(r'C:\Users\Yevhen_Nikolin\Desktop\dq_checks')
params = {"type": "dedicated", "layer": "DWH_CORE"}
# exc = QueryExecutor('eaebsco.us-east-1', 'ynikolin', 'qQ3420308674', 'EA_QA_TEAM', 'EA_DU_DEV')

lib.print_test_library()
print('============================================================================')
# print(lib.get_list_of_tests_by_params(params))
print(type(params))
print(params)