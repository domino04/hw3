#import requests
#from bs4 import BeautifulSoup   #Beautifulsoup를 통해서 이제 적분을 할 수 있게 됨.
#note_html = requests.get('https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%85%B8%ED%8A%B8&pagingIndex=1&pagingSize=80&viewType=list&sort=rel&frm=NVSHPAG&query=%EB%85%B8%ED%8A%B8')

#note_soup = BeautifulSoup(note_html.text, "html.parser")
#note_list_box = note_soup.find("ul", {"class" : "goods_list"})
#note_list = note_list_box.find_all("li", {"class" : "_itemSection"}

#title = note_list[0].find("div", {"class" : "tit"}).find("a").string
#price = note_list[0].find("span", {"class" : "price"}).text
#img_src = note_list[0].find('img', {"class" : "_productLazyImg"})['data-original']
#print(img_src)


import requests
from bs4 import BeautifulSoup
from note import extract_info

import csv
file = open("notes.csv", mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["title", "price", "img_src", "page_link"])

final_result = []
for i in range(5):
    print(f'{i+1}번째 페이지 크롤링 중...')
    note_html = requests.get(f'https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%85%B8%ED%8A%B8&pagingIndex={i}&pagingSize=40&viewType=list&sort=rel&frm=NVSHPAG&query=%EB%85%B8%ED%8A%B8')
    note_soup = BeautifulSoup(note_html.text,"html.parser")
    note_list_box = note_soup.find("ul", {"class" : "goods_list"})
    note_list = note_list_box.find_all('li', {"class" : "_itemSection"})

    result = extract_info(note_list)
    #result는 한페이지의 모든 상품
    final_result = final_result + result
    #final_result = [{}, {}, {}, ... =>80] + [{}, {}, {}, ... =>80] + ...
    #final_result ==> 80*n개의 상품

print(final_result)


for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['price'])
    row.append(result['img_src'])
    row.append(result['page_link'])
    writer.writerow(row)

print('크롤링 끝')