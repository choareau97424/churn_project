import json
import requests
import pandas as pd
import os

#url = "https://api.twitter.com/2/tweets/search/recent?query=from:TwitterDev"
#response = requests.request("GET", url, headers=headers).json()
#df = pd.DataFrame(response['data'])
#df.to_csv('response_python.csv')

df = pd.read_json (r"C:\Users\wsiou\Downloads\churn.json")
df.to_csv (r'C:\Users\wsiou\churn.csv', index = None)



#pdObj = pd.read_json('export.json', orient='index')
#pdObj.to_csv('streaming.csv', index=False)



"""
def get_exams_questions_data(file_path: str, limit: int, testType: str, subject: str):
    exams_obj = []
    wb_obj = openpyxl.load_workbook(file_path)
    sheet_obj = wb_obj.active
    m_row = sheet_obj.max_row

    for i in range(2, m_row + 1):
        question_obj = {}
        question_obj["question"] = str(sheet_obj.cell(row=i, column=1).value) if sheet_obj.cell(row=i, column=1).value is not None else ""
        question_obj["subject"] = str(sheet_obj.cell(row=i, column=2).value) if sheet_obj.cell(row=i, column=2).value is not None else ""
        question_obj["use"] = str(sheet_obj.cell(row=i, column=3).value) if sheet_obj.cell(row=i, column=3).value is not None else ""
        question_obj["answer"] = str(sheet_obj.cell(row=i, column=4).value) if sheet_obj.cell(row=i, column=4).value is not None else ""
        question_obj["OptionA"] = str(sheet_obj.cell(row=i, column=5).value) if sheet_obj.cell(row=i, column=5).value is not None else ""
        question_obj["OptionB"] = str(sheet_obj.cell(row=i, column=6).value) if sheet_obj.cell(row=i, column=6).value is not None else ""
        question_obj["OptionC"] = str(sheet_obj.cell(row=i, column=7).value) if sheet_obj.cell(row=i, column=7).value is not None else ""
        question_obj["OptionD"] = str(sheet_obj.cell(row=i, column=8).value) if sheet_obj.cell(row=i, column=8).value is not None else ""
        question_obj["remark"] = str(sheet_obj.cell(row=i, column=9).value) if sheet_obj.cell(row=i, column=9).value is not None else ""
        if question_obj["use"] == testType and question_obj["subject"] == subject:
            exams_obj.append(question_obj)

    random.shuffle(exams_obj)

    return exams_obj[0:limit]
"""
