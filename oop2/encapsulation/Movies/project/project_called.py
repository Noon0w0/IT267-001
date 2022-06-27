from condo import Condo

ideo = Condo("ideo5",18,"Ladphrao",80,"condo 20 Floors")
ideo.show()

from project import Project
home = Project("Ladawan",15,"Bang Yai")
home.show()
print(f'budget : {home.get_budget()} MB')