# Removed From Scrapper.py

for i in SEM.find_all('td')[0]:
    title = i.text.strip()
    SEM1 = title
for i in SEM.find_all('td')[1]:
    title = i.text.strip()
    SEM2 = title
for i in SEM.find_all('td')[2]:
    title = i.text.strip()
    SEM3 = title
for i in SEM.find_all('td')[3]:
    title = i.text.strip()
    SEM4 = title
for i in SEM.find_all('td')[4]:
    title = i.text.strip()
    SEM5 = title
for i in SEM.find_all('td')[5]:
    title = i.text.strip()
    SEM6 = title
for i in SEM.find_all('td')[6]:
    title = i.text.strip()
    SEM7 = title
for i in SEM.find_all('td')[7]:
    title = i.text.strip()
    SEM8 = title

data = [RegistrationNo, Student_Name, College_Code, College_Name, Course_Code, Course_Name, semester,
                SEM1, SEM2, SEM3, SEM4, SEM5, SEM6, SEM7, SEM8, CGPA]




# Removed from main.py
reg = 0
branch = 0
clg = 0
i = 0
while reg < len(Reg_Year):
    while clg < len(Reg_Clg_code):
        while branch < len(Reg_Branch_Code):
            while i < len(Reg_Student_Id):
                c = str(Reg_Year[reg])+str(Reg_Branch_Code[branch]
                                            )+str(Reg_Clg_code[clg])
                newReg = int(c+str(Reg_Student_Id[i]).zfill(3))
                Result_BOT(newReg, url)

                i += 1
            branch += 1
            i = 0
        branch = 0
        clg += 1
        i = 0
    reg += 1
    clg = 0
    i = 0
