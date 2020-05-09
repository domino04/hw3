import requests
from bs4 import BeautifulSoup
from noteforhw import extract_info

import csv
file = open("note-hw.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "img_src", "page_link", "writer", "cop"])

final_result = []
for i in range(8):
    print(f'{i+1}번째 페이지 크롤링 중...')
    note_html = requests.get(f'https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={i}')
    note_soup = BeautifulSoup(note_html.text,"html.parser")
    note_list_box = note_soup.find("ol", {"class" : "basic"})
    note_list = note_list_box.find_all('li')

    result = extract_info(note_list)
    #result는 한페이지의 모든 상품
    final_result = final_result + result
    #final_result = [{}, {}, {}, ... =>80] + [{}, {}, {}, ... =>80] + ...
    #final_result ==> 80*n개의 상품

print(final_result)


for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['img_src'])
    row.append(result['page_link'])
    row.append(result['writer'])
    row.append(result['cop'])
    writer.writerow(row)

print('크롤링 끝')