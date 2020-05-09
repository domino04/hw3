import requests
from bs4 import BeautifulSoup
from coronahospitalnote import extract_info
import csv

file = open("coronahospitalnote.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["시도", "시군구", "선별진료소", "전화번호"])


hospital_html = requests.get('https://www.mohw.go.kr/react/popup_200128_3.html')
hospital_html.encoding = 'utf-8'

hospital_soup = BeautifulSoup(hospital_html.text, "html.parser")
hospital_list_box = hospital_soup.find("tbody", {"class" : "tb_center"})
hospital_list = hospital_soup.find_all("tr")
final_result = extract_info(hospital_list)

for result in final_result:
    row =[]
    row.append(result['시도'])
    row.append(result['시군구'])
    row.append(result['선별진료소'])
    row.append(result['전화번호'])
    writer.writerow(row)

print('크롤링 끝')