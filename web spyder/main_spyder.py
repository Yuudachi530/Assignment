import urllib
from bs4 import BeautifulSoup as bs

resp = urllib.request.urlopen('http://blog.sina.com.cn/cqryg')
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
music_info = soup.find_all('div', class_ = 'blog_title')
counter = 0
list_info = []
for i in music_info:
    music_info_1 = music_info[counter].find_all('a', target = '_blank')
    counter = counter + 1
    for item in music_info_1:
        dic_info = {}
        operat = str(item).split()
        ele = dic_info['Title: '] = operat[1][6:-1]
        list_info.append(dic_info)

def Initialize_Soup(Link):
    Resp = urllib.request.urlopen(link)
    Html_Data = Resp.read().decode('utf-8')
    Soup = bs(Html_Data, 'html.parser')
    return Soup

def Find_Style(Soup): #Soup: list
    for i in Soup:
        Counter = 0
        Line = str(i) if i != None else ''
        if Line != '':
            for c in Line:
                if Line[Counter: Counter + 9] == 'font-size':
                    list1.append(i)
                Counter = Counter + 1
                if Counter == len(Line) - 9:
                    break
                
def Abstract_Text(Soup_Music_Script_List):
    for i in Soup_Music_Script_List:
        Text_Sum = i.text
    return Text_Sum

def Abstract_Title(Soup):
    Title = Soup.find('h2').text if Soup.find('h2') != None else 'unknown'
    return Title

def Write_TextFile(Text, FileName):
    Text = str(Text)
    File_Holder = open(str(FileName) + '.txt', 'w', errors='ignore')
    File_Holder.write(Text)
    File_Holder.close()
    
    
    
for item in list_info:
    list1 = []
    link = item['Title: ']
    soup = Initialize_Soup(link)
    music_script = soup.find_all('div')
    Find_Style(music_script)  
    Write_TextFile(Abstract_Text(list1), Abstract_Title(soup))







