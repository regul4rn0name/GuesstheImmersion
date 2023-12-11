import mysql.connector
from match_ids_module import match_ids

import matchdecode

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="main",
        password="",
        database="matches",
        port="8889"
    )

    mycursor = mydb.cursor()
    sql = "SELECT match_id FROM `Andrey` WHERE `index` = 185"

    mycursor.execute(sql)
    fetched_match_ids = mycursor.fetchall()

    # Extract match_ids from the fetched data and append them to the existing array
    match_ids.extend([match_id[0] for match_id in fetched_match_ids])

    print(match_ids)
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    mycursor.close()
    mydb.close()

matchdecode.main()

