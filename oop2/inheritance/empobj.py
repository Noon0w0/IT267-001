from empit import EmpIT
from empmkt import EmpMKT

#create object employee IT
mike = EmpIT("001","Mike",60000)
mike.add_skill("Python, JavaSrcipt")
mike.add_experience(5)
mike.emp_detail()
mike.it_salary()

#create obj employee
anna = EmpMKT("002","Anna",35000)
anna.emp_detail()
anna.mkt_salary()

paul = EmpMKT("003","Paul",45000)
paul.add_commission(35)
paul.emp_detail()
paul.mkt_salary()