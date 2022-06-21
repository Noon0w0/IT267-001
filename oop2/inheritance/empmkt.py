from employee import Employee

class EmpMKT(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.location = 'Bangkok'
        self.commision = 30
        self.department = 'Marketing'

    def add_location(self,location):
        self.location = location

    def add_commission(self,commission):
        self.commission = commission

    def emp_detail(self):
        print("===== EmployeeMarketing Detail =====")
        #เรียกใช้เมธอท emp_detail ของคราส Employee เพื่อแสดง id, name
        super().emp_detail()
        print(f'location: {self.location}')
        print(f'commission: {self.commission} %')
    
    def mkt_salary(self):
        self._emp_salary()