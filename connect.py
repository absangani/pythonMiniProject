import sqlite3

class myconnect:

    def __init__(self):
        self.conn = sqlite3.connect("emp.db")
        self.c = self.conn.cursor()
        try:
            self.c.execute(''' create table if not exists emp 
            (id integer primary key autoincrement, name text,email text,mobile_no text,e_type text,experience integer,salary integer)''')
        except:
            pass

    def insertData(self,name,email,mobile_no,e_type,experience,salary):
        self.c.execute('''insert into emp values(:id,:name,:email,:mobile_no,:e_type,:experience,:salary)''',
            {'id':None,'name':name,'email':email, 'mobile_no':mobile_no , 'e_type':e_type,'experience':experience,'salary':salary})
        self.conn.commit()

    def display(self):
        #name = input("Enter employee name : ")
        self.c.execute("select * from emp")
        for i in self.c:
            print("---------------------------------------------------")
            print("Name : ",i[1])
            print("Email : ",i[2])
            print("Mobile NO : ",i[3])
            print("Type : ",i[4])
            print("Experience : ",i[5])
            print("Salary : ",i[6])