from csv import DictWriter
import requests as rqst
from bs4 import BeautifulSoup as bs
import os.path


def Result_Bot_function(RegistrationNo, url):
    import csv

    '''
    This function scrap the data from webpage using BeautifulSoup4
    '''
    url = f'https://......./{RegistrationNo}//&RegNo={RegistrationNo}'
    web = rqst.get(url)

    soup = bs(web.content, "html.parser")
    # text =  soup.body.table.style1
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

        CGPA = soup.find(
            'table', {'id': 'ctl00_ContentPlaceHolder1_GridView3'})

        for i in CGPA.find_all('td')[-1]:
            title = i.text.strip()
            CGPA = title

        # SEMESTER WISE SGPA
        SEM = soup.find('table', {'id': 'ctl00_ContentPlaceHolder1_GridView3'})

        SEM_values = []
        for td in SEM.find_all('td'):
            title = td.text.strip()
            SEM_values.append(title)

        Student = {
            'Registration No': RegistrationNo,
            'Student Name': Student_Name,
            'College Code': College_Code,
            'College Name': College_Name,
            'Course Code': Course_Code,
            'Course Name': Course_Name,
            'Semester': semester,
            'SEM I': SEM_values[0],
            'SEM II': SEM_values[1],
            'SEM III': SEM_values[2],
            'SEM IV': SEM_values[3],
            'SEM V': SEM_values[4],
            'SEM VI': SEM_values[5],
            'SEM VII': SEM_values[6],
            'SEM VIII': SEM_values[7],
            'CGPA': CGPA
        }

        header = ['Registration No', 'Student Name', 'College Code', 'College Name', 'Course Code', 'Course Name',
                  'Semester',          'SEM I', 'SEM II', 'SEM III', 'SEM IV', 'SEM V', 'SEM VI', 'SEM VII', 'SEM VIII', 'CGPA']

        # custom file name for seperate csv files
        Reg_No = str(RegistrationNo)
        clg_code = Reg_No[5:8]
        Branch_code = Reg_No[2:5]
        csv_file = f"Result/{Reg_No[0:2]}_CLG_{clg_code}_{Branch_code}.csv"

       # check file does exist or not
        file_exists = os.path.isfile(csv_file)

        try:
            with open(csv_file, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=header)
                # write header once only when file does not exist
                if not file_exists:
                    writer.writeheader()
                # if file does exist then write the content, not header
                writer.writerow(Student)
        except IOError:
            print("I/O error")
    else:
        print(f'Result Unavailable: {RegistrationNo}')


RegistrationNo = 0
url = f'https://......./{RegistrationNo}//&RegNo={RegistrationNo}'

Result_Bot_function(RegistrationNo, url)