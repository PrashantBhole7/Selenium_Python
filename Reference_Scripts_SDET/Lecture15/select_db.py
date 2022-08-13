# insert, update, delete

import mysql.connector


try:
    con = mysql.connector.connect(host="localhost", port=3306, user="prashant", passwd="Prashantb07089@", database="pytsel")
    curs = con.cursor()  # create cursor
    curs.execute("select * FROM Persons")  #  execute query through cursor
    for row in curs:
        print(row)

    con.close()
except:
    print("Connection Unsuccessful")
print("Finished...")