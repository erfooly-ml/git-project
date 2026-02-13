class Emp:
    increase_rate = 0.05
    def __init__(self,id, salary):
        self.id = id
        self.salary= salary

    def show_info(self):
        return self.id

    def increase_salary(self):
        self.salary *= Emp.increase_rate

