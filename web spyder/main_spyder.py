import urllib
from bs4 import BeautifulSoup as bs

resp = urllib.request.urlopen('https://vocaloid.fandom.com/wiki/Wowaka')
html_data = resp.read().decode('utf-8')                              
soup = bs(html_data, 'html.parser')
music_info = soup.find_all('a') 
music_info_list = []
for i in music_info[41:]:
    line = i.get('href')
    if str(line)[:7] == '/wiki/%':
        music_info_list.append(line)
del_c = 'abcdefghijklmnopqrstuvwxyz/\)(,ABCDEFGHIJKLMNOPQRStUVWXYZ.'
del(music_info_list[-1])
def Initialize_Soup(Link):
    Resp = urllib.request.urlopen('https://vocaloid.fandom.com' + Link)
    Html_Data = Resp.read().decode('utf-8')
    Soup = bs(Html_Data, 'html.parser')
    return Soup

def Abstract_Script(SoupData):
    Script = SoupData.find(style="width:100%")
    Script = Script.find_all('td')
    Script_List = []
    for i in Script:
        Line = str(i.text)
        for j in del_c:
            Line = Line.replace(j, '')
        Line = Line.replace('\n', '')
        Script_List.append(Line)
    return Script_List

def Write_TextFile(FileName, FileList):
    File_Holder = open(FileName, 'w', errors = 'ignore')
    for i in FileList:
        File_Holder.write(i +  '\n')
    File_Holder.close()
testcounter = 1
NameCounter = 1
for item in music_info_list:
    soup = Initialize_Soup(item)
    music_script = Abstract_Script(soup)
    if NameCounter < 10:
        Write_TextFile('0' + str(NameCounter) + '.txt', music_script)
    else:
        Write_TextFile(str(NameCounter) + '.txt', music_script)
    NameCounter = NameCounter + 1





