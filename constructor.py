class Employee:
    language = "python"
    salary = 200000

    def __init__(self, name, language, salary):
        print("Hi, I am under the constructor")
        self.name = name
        self.language = language
        self.salary = salary

    def data(self):
        print(f"This is {self.language} language & Salary is {self.salary}")

    def learn(self):
        print("Let's learn.....................")
        print("")
    


# Object creation
amit = Employee("AMIT", "C++", 3000000)

# Output
print(amit.language, amit.salary, amit.name)

# Method calls
amit.data()
amit.learn()
