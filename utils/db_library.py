import sqlite3, yaml
from typing import Dict, Optional
from sqlite3 import Error

def make_system_table():
    with sqlite3.connect(r"C:\Users\user\Desktop\1354163.db") as db_connection:
        cursor = db_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lv1_tor_win_system(
                System_FILE TEXT,
                Onion_Site TEXT
            )
        """
        )
        db_connection.commit()
        return db_connection

def insert_system_data(row, row2):
    list=[]
    list.append([row, row2])
    connection = make_system_table()
    with connection:
        cursor = connection.cursor()
        sql = f"""
            INSERT OR REPLACE INTO lv1_tor_win_system VALUES (
                ?,
                ?
            )
        """
        cursor.execute(
            sql,
            (
                list[0][0],
                list[0][1]
            ),
        )
        connection.commit()
    return connection



def make_memory_table():
    with sqlite3.connect(r"C:\Users\user\Desktop\AFAN.db") as db_connection:
        cursor = db_connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lv1_tor_win_memory_socks(
                Built_Number TEXT,
                Fingerprint1 TEXT,
                Fingerprint2 TEXT,
                Fingerprint3 TEXT,
                Fingerprint4 TEXT,
                Fingerprint5 TEXT,
                Built_Flags TEXT,
                Purpose TEXT,
                HS_State TEXT,
                Rend_Query TEXT,
                Time_Created TEXT,
                SOCKS_Username TEXT,
                SOCKS_Password TEXT
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS lv1_tor_win_memory_credential(
                Form_Sent TEXT,
                Redirect_URL TEXT,
                csrf_token TEXT,
                Unknown_str TEXT,
                Req_Username TEXT,
                Req_Password TEXT,
                req_capcha TEXT,
                Login TEXT
            )
        """
        )
        db_connection.commit()
        return db_connection


def make_tails_table(conn):
    try:
        DB = conn.cursor()
        DB.execute(""" CREATE TABLE IF NOT EXISTS nvram_usb_history(
                            manufacture_model,
                            input_file_path,
                            input_file_offset,
                            nvar_entry_blob
                            ); """)
    except Error as e:
        print(e)




def insert_socks_data(row: Dict[str, Optional[str]]):
    connection = make_memory_table()
    with connection:
        cursor = connection.cursor()
        sql = f"""
            INSERT OR REPLACE INTO lv1_tor_win_memory_socks VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """
        cursor.execute(
            sql,
            (
                row[0]["built_num"],
                row[0]["fingerprint1"],
                row[0]["fingerprint2"],
                row[0]["fingerprint3"],
                row[0]["fingerprint4"],
                row[0]["fingerprint5"],
                row[0]["built_flag"],
                row[0]["purpose"],
                row[0]["hs_state"],
                row[0]["rend_query"],
                row[0]["time_created"],
                row[0]["socks_username"],
                row[0]["socks_password"]
            ),
        )
        connection.commit()
    return connection


def insert_credential_data(row: Dict[str, Optional[str]]):
    connection = make_memory_table()
    with connection:
        cursor = connection.cursor()
        sql = f"""
            INSERT OR REPLACE INTO lv1_tor_win_memory_credential VALUES (
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
        """
        cursor.execute(
            sql,
            (
                row["form_sent"],
                row["redirect_url"],
                row["csrf_token"],
                row["undefined"],
                row["req_username"],
                row["req_password"],
                row["req_capcha"],
                row["login"]
            ),
        )
        connection.commit()
    return connection


def insert_tails_data(conn, values):
    DB_Insert = """ 
    INSERT INTO nvram_usb_history(
    manufacture_model, 
    input_file_path, 
    input_file_offset, 
    nvar_entry_blob)
               VALUES(?,?,?,?) """
    cur_Insert = conn.cursor()
    cur_Insert.execute(DB_Insert, values)
    conn.commit()
    return cur_Insert