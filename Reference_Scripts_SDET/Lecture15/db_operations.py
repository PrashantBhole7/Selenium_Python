# insert, update, delete

import mysql.connector

insert_query = "INSERT into Persons values(111,'Attarde','Parag','Ayodhya Nagar','Jalgaon')"
update_query = "update Persons set LastName='Patil' where PersonID=111"
delete_query = "delete from Persons where PersonID=234"

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="prashant", passwd="Prashantb07089@", database="pytsel")
    curs = con.cursor()  # create cursor
    curs.execute(update_query)  #  execute query through cursor
    con.commit()  # commit transaction
    con.close()
except:
    print("Connection Unsuccessful")
print("Finished...")