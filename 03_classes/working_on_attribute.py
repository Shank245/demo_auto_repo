class emp:
    def get_name_age_salary(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        return None

    def display_detalls(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Salary: ", self.salary)
        return None


emp1 = emp()
emp2 = emp()

emp1.get_name_age_salary("John", 30, 50000)
emp2.get_name_age_salary("Jane", 25, 60000)

emp1.display_detalls()
emp2.display_detalls()
