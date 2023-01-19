from scrapper import Result_Bot_function, url


def Reg_generator(Reg_Year, Reg_Branch_Code, Reg_Clg_code, Reg_Student_Id):
    """
    This function wil return the all combination of registration number:
    Reg_Year =        [18, 19, 20, 21]
    Reg_Branch_Code = [101, 102, 103, 104]
    Reg_Clg_code  =   [130, 131, 132]
    """

    for reg in Reg_Year:
        for clg in Reg_Clg_code:
            for branch in Reg_Branch_Code:
                for student_id in Reg_Student_Id:
                    new_reg = f"{reg}{branch}{clg}{student_id:03d}"
                    Result_Bot_function(int(new_reg), url)

'''The value of student_id is formatted to always have 3 digits by using the :03d syntax. This means that if student_id is less than 100, it will be padded with leading zeros to make it have 3 digits. For example, if student_id is 5, the resulting string will be 005. If student_id is 123, the resulting string will be 123.'''

if __name__ == "__main__":
    Reg_Year = list(range(18, 19, 1))
    Reg_Branch_Code = list(range(101, 105, 1))
    Reg_Clg_code = list(range(113, 127, 1))
    Reg_Student_Id = list(range(1, 61))

    Reg_generator(Reg_Year, Reg_Branch_Code, Reg_Clg_code, Reg_Student_Id)

    # RegistrationNo = int(    
    #     str(Reg_Year[0])
    #     + str(Reg_Branch_Code[0])
    #     + str(Reg_Clg_code[0])
    #     + str(Reg_Student_Id[0]).zfill(3)
    # )

    # url = f'https://......./{RegistrationNo}'//&RegNo={RegistrationNo}'