import sqlite3

conn = sqlite3.connect('patient.db')

cur = conn.cursor()
#cur.execute("create table patientinfo(name varchar(30), result varchar(30))")
cur.execute("insert into patientinfo values('XYZ','diabetic')")
conn.commit()