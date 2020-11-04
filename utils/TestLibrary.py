import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)
pd.set_option('max_columns', None)
pd.set_option('display.width', 10000)
# r'C:\Users\Yevhen_Nikolin\Desktop\dq_checks.json'
# r'C:\Users\Yevhen_Nikolin\Desktop\sqls\DWH_CORE\S_ITEM_GEN_INFO\CORE_S_ITEM_GEN_INFO_VALIDATE_ITEM_STATUS_MAPPING.sql'

class TestLibrary(object):
    def __init__(self, p_file_path: str):
        self.lib_path = p_file_path
        self.df_lib = self.__read_test_library(p_file_path)
        print(self.df_lib)

    def __read_test_library(self, p_file_path: str) -> pd.DataFrame:
        df = pd.read_json(p_file_path)

        return df

    def __read_script_file(self, p_file_path: str) -> str:
        with open(p_file_path, 'r') as f_obj:
            res = f_obj.read()
            print(res)

        return res

    def get_dq_check_property_by_name(self, p_dq_check_id: str, p_property_name: str) -> str:
        res = self.df_lib.query('dq_check_id ==\'' + p_dq_check_id + '\'')[p_property_name][0]

        return res

lib = TestLibrary(r'C:\Users\Yevhen_Nikolin\Desktop\dq_checks.json')
lib.get_dq_check_property_by_name('DQ_0025', 'name')