# -*- coding: utf-8 -*-
"""module for Timeline."""
import os
from utils.db_library import *
from modules.system.pagefile_parser import execute

# ToDO 노드 유효 체크
# ToDo yaml 연동


def WindowsPagefileConnector():
    NAME = 'windows_pagefile_connector'
    DESCRIPTION = 'Module for Windows_pagefile'
    this_file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'schema' + os.sep
    yaml_list = [this_file_path + 'lv1_tor_win_pagefile.yaml']
    table_list = ['lv1_tor_win_pagefile']

    # make system table
    make_system_table()

    #windows_pagefil_files = r"C:\Users\user\Desktop\AFAN_Tools\test\t_last.raw"
    test_dir = os.path.join(os.path.dirname(__file__), "test")

    if len(os.listdir(test_dir)) == 0:
        print("There are no pagefile files!!")
        return False


    insert_data = []
    for artifact_file in os.listdir(test_dir):
        full_filepath = os.path.join(test_dir, artifact_file)
        #artifact_name = os.path.basename(full_filepath)
        file_attribute = os.path.splitext(full_filepath)

        # sys
        if file_attribute[1] == '.sys':
            onion_result = execute(full_filepath)
            for data in onion_result:
                insert_system_data(artifact_file, data)

    return onion_result
