
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error


def main():

    reading = pd.read_csv("reading_values.csv")
    
    levels = pd.read_csv("levels_values.csv")
    try:
        conn = msql.connect(host='localhost', database="GreenHouseRealTime", user='root_payload',  
                        password='')
        if conn.is_connected():
            cursor = conn.cursor()
            for i, row in levels.iterrows():
                sql = "INSERT INTO levels_values VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                # print(row)
                cursor.execute(sql, tuple(row))
                conn.commit()
    except Error as e:
        print(f"{str(e)}")


if __name__ == "__main__":
    main()
