import re

class validations:

    def validatemob(self,mob):
        pattern = re.compile(r'\d{10}\\n')
        if(pattern.match(mob)):
            return True
        else:
            print("Re-enter Mobile Number")
            return False

    def validatemail(self,mail):
        pattern = re.compile(r'([a-zA-Z0-9-]+)@([a-zA-Z-]+)(\.[a-z]{3})?(\.[a-zA-Z]+)')
        if(pattern.match(mail)):
            return True
        else:
            print("Re-enter valid mail id")
            return False