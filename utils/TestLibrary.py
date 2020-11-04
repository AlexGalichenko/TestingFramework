import pandas as pd

class TestLibrary(object):
    def __init__(self, p_lib_path: str):
        self.lib_path = p_lib_path

    def __read_test_library(self, p_lib_path: str):
