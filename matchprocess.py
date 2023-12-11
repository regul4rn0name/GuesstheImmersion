import mysql.connector
from match_ids_module import match_ids  # Assuming match_ids is a list of values


def main():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="main",
            password="",
            database="matches",
            port="8889"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO Andrey (match_id) VALUES (%s)"

        # Assuming match_ids is a list of values
        # If match_ids is a list of tuples, use executemany
        for match_id in match_ids:
            mycursor.execute(sql, (match_id,))

        mydb.commit()
        print("Records inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        mycursor.close()
        mydb.close()


if __name__ == "__main__":
    main()
