class employee : 
    language = "python"
    salary = 200000

    def data(self):
        print(f"This is a {self.language} language  & Salary is {self.salary}")


    def print(self):
        print("Lets lean.....................")

    # @staticmethod
    # def print():
    #     print("Lets lean.....................")


Amit = employee()
Amit.language = "java"
# print(Amit.language , Amit.salary)
Amit.print()
Amit.data()
# employee.data(Amit)