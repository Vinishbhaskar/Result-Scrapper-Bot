from Result_BOT_Final import Result_BOT


def Reg_generator(Reg_Year, Reg_Branch_Code, Reg_Clg_code, Reg_Student_Id, url):
    """
    This function wil return the all combination of registration number
    """

    """
    Reg_Year =    [18, 19, 20, 21]
    Reg_Branch_Code = [101, 102, 103, 104]
    Reg_Clg_code  = [130, 131, 132]

    """

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
    # print(newReg)
    # return int(newReg)


Reg_Year = list(range(18, 20, 1))
Reg_Branch_Code = list(range(104, 105, 1))
Reg_Clg_code = list(range(135, 136, 1))
Reg_Student_Id = list(range(1, 61))


RegistrationNo = int(
    str(Reg_Year[0])
    + str(Reg_Branch_Code[0])
    + str(Reg_Clg_code[0])
    + str(Reg_Student_Id[0]).zfill(3)
)

url = f'https://......./{RegistrationNo}'


Reg_generator(Reg_Year, Reg_Branch_Code, Reg_Clg_code, Reg_Student_Id, url)