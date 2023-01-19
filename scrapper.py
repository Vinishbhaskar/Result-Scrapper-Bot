from csv import DictWriter
import requests as rqst
from bs4 import BeautifulSoup as bs
import os.path


def Result_BOT(RegistrationNo, url):
    import csv

    '''
    This function scrap the data from webpage using BeautifulSoup4

    '''
    url = f'http://results.akuexam.net/ResultsBTechBPharm8thSemPub2022.aspx?Sem=VIII&RegNo={RegistrationNo}'

    web = rqst.get(url)
    Registration_num = str(RegistrationNo)
    clg_code = Registration_num[2:5]
    csv_file = f"Result/{Registration_num[0:2]}_Batch_College_Code_{clg_code}.csv"

    soup = bs(web.content, "html.parser")
    #text =  soup.body.table.style1
    status = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_DataList4'})

    if str(status) != 'None':
        semester = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList2_ctl00_Exam_Name'}).text
        Student_Name = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList1_ctl00_StudentNameLabel'}).text
        College_Name = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList1_ctl00_CollegeNameLabel'}).text
        College_Code = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList1_ctl00_CollegeCodeLabel'}).text
        Course_Code = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList1_ctl00_CourseCodeLabel'}).text
        Course_Name = soup.find(
            'span', {'id': 'ctl00_ContentPlaceHolder1_DataList1_ctl00_CourseLabel'}).text
        #SGPA = soup.find('span',{'id':'ctl00_ContentPlaceHolder1_DataList5_ctl00_GROSSTHEORYTOTALLabel'}).text
        CGPA = soup.find(
            'table', {'id': 'ctl00_ContentPlaceHolder1_GridView3'})

        for i in CGPA.find_all('td')[-1]:
            title = i.text.strip()
            CGPA = title

        # SEMESTER WISE SGPA
        SEM = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView3'})

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

        Student = {'Registration No': RegistrationNo,
                   'Student Name': Student_Name,
                   'College Code': College_Code,
                   'College Name': College_Name,
                   'Course Code': Course_Code,
                   'Course Name': Course_Name,
                   'Semester': semester,
                   # 'SGPA': SGPA,
                   'SEM I': SEM1,
                   'SEM II': SEM2,
                   'SEM III': SEM3,
                   'SEM IV': SEM4,
                   'SEM V': SEM5,
                   'SEM VI': SEM6,
                   'SEM VII': SEM7,
                   'SEM VIII': SEM8,
                   'CGPA': CGPA
                   }

        header = ['Registration No', 'Student Name', 'College Code', 'College Name', 'Course Code', 'Course Name', 'Semester',
                  'SEM I', 'SEM II', 'SEM III', 'SEM IV', 'SEM V', 'SEM VI', 'SEM VII', 'SEM VIII', 'CGPA']

        data = [RegistrationNo, Student_Name, College_Code, College_Name, Course_Code, Course_Name, semester,
                SEM1, SEM2, SEM3, SEM4, SEM5, SEM6, SEM7, SEM8, CGPA]

        file_exists = os.path.isfile(csv_file)

        try:
            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                if not file_exists:
                    writer.writeheader()
                # for i in data:
                writer.writerow(Student)
        except IOError:
            print("I/O error")
    else:
        print(f'Result Unavailable: {RegistrationNo}')


RegistrationNo = 0
url = f'https://......./{RegistrationNo}'

Result_BOT(RegistrationNo, url)