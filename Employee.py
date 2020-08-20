from PermenetEmployee import Per_Emp
from connect import myconnect
from validation import validations


class Employee:

    _name = ''
    _email = ''
    _mobile_no = ''
    _e_type = ''
    _experience = ''
    _salary = ''

    def __init__(self):
        self._name = input("Enter Name : ")
        self._email = input("Enter Email : ")
        objvalid = validations()
        while(not objvalid.validatemail(self._email)):
            self._email = input("Enter Email : ")

        self._mobile_no = input("Enter mobile no : ")
        while(not objvalid.validatemob(self._mobile_no)):
            self._mobile_no = input("Enter mobile no : ")

        self._e_type = input("Enter type : ",)
        self._experience = int(input("Enter Experience : "))
        self._salary = self.getsalary()

    def getsalary(self):
        if self._e_type == "P" or self._e_type == "p":
            opemp = Per_Emp()
            return opemp.calculatesalary(self._experience)
        else:
            print("Invalid Employee. Please enter only 'p' or 'P'")


    @staticmethod
    def addnote():
        data = input("enter note")
        file = open("note.txt","a+")
        file.write(data)
        print("Note added")

print("1 : Add Emp")
print("2 : Display Emp")
print("3 : Add note")
choice = int(input("Enter your choice : "))
#choice code

if choice == 1:
    c = Employee()
    obj = myconnect()
    obj.insertData(c._name,c._email,c._mobile_no,c._e_type,c._experience,c._salary)
elif choice == 2:
    obj = myconnect()
    obj.display()
elif choice == 3:
    Employee.addnote()
else:
    print("invalind choice")

