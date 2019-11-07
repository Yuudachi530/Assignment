import MeCab as mecab
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

del_character = '123456。。7890！（,?"''）-.!?！？，。=+-_——、，”。-”!:！!？?、：…“「」'
del_c = "ーあアいイうウえエおオかカきキくクけどだケでがこコさサしシすスせセそソたタちチつツてテとトな ナにニぬヌねネのノはハひヒふフへヘほホまマみミむムめメもモやヤいイゆユえエよヨらラりリるルれレろロわワいイうウえエをヲんン'"
def Initailize_TextFile(FileName):
    File_Holder = open(FileName + '.txt', 'r')
    File_List = File_Holder.readlines()
    File_Holder.close()
    return File_List

word_dic = {}
OWAKATI = mecab.Tagger('-Owakati')

def Word_Statistic(WordList):
    for i in WordList:
        Line = OWAKATI.parse(i)
        for cha in del_character:
            Line = Line.replace(cha, '')
        Line = Line.split()
        for j in Line:
            if j not in word_dic:
                word_dic[j] = 1
            else:
                word_dic[j] = word_dic[j] + 1

for i in range(1, 12 + 1):
    if i < 10:
        word_list = Initailize_TextFile('0'+ str(i))
    else:
        word_list = Initailize_TextFile(str(i))
    Word_Statistic(word_list)

for c in del_c:
    if c not in word_dic:
        continue
    else:
        del word_dic[c]

d_order = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
color_back = Image.open('mothercolor.png')
color_back = np.array(color_back)
image_colors = ImageColorGenerator(color_back)
# print(d_order)
wowaka_mask = Image.open('timg6.png')
wowaka_mask = np.array(wowaka_mask)
print(type(wowaka_mask))
wc = WordCloud(font_path='C:\Windows\Fonts\BIZ-UDGothicR.ttc', max_words=2000, mask=wowaka_mask,
               stopwords=None, background_color='white')
wc.fit_words(word_dic)
#BIZ-UDMinchoM.ttc
wc.recolor(color_func=image_colors)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()





