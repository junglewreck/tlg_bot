import requests, lxml.html
from bs4 import BeautifulSoup
# session = requests.Session()
url = 'https://issa.beltelecom.by/main.html'
values = {'oper_user': '1770002571701',
          'passwd': '49217'}

r = requests.post(url, data=values)
c = r.content
soup = BeautifulSoup(c, "lxml".decode('cp1251', 'ignore'))
result = soup.findAll('div', style="font-size:16px;float:right;padding-bottom:5px;")
result_dict = []
for i in result:
	result_dict.extend(i.find_all(text=''))
result_dict = str(result_dict)
true_result = result_dict[62:69]
print (true_result + "RUB")
# samples = soup.find_all("div", "content")
# print samples[0]


# bsObj = BeautifulSoup(r.read());
# print(bsObj.h1)
# print type(r.content)

# params = {'oper_user': '1770002571701', 'passwd': '49217'}
# s = session.post('https://issa.beltelecom.by/main.html', params)
# print ("Cookie is set to:")
# print(s.cookies.get_dict())
# print("---------------")
# print("Going to profile page....")
# s = requests.get("https://issa.beltelecom.by/servact.html")
# print(s.text)
