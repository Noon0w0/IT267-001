
#สร้างฟังชั่นเปิด ปิดไฟ
global switch_is_status
def turnon() :
    global switch_is_status
    switch_status = True #เปลี่ยนสถานะเป็นปิดไฟ

#ฟังชั่นปิดไฟ
def turnoff():
    global switch_is_status
    switch_status = False

switch_status = False #ปิด

print(f"switch_status = {switch_status}") #False
turnon()
print(f"switch_status = {switch_status}") #Ture
turnoff()
print(f"switch_status = {switch_status}")#False
turnoff()
print(f"switch_status = {switch_status}")
turnoff()
