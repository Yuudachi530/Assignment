
import smtplib
from email.mime.text import MIMEText

mailto_list = ['ygjzcycdr@outlook.com'] # 收信人邮箱，可填写多个
mail_host = 'smtp.163.com' # smtp的服务器地址
mail_user = 'ygjzcycdr@163.com' # 发信人邮箱
mail_pass = 'OSQELCNRFLYRNAZF' #授权码

#邮件内容
msg = MIMEText('你好')
msg['Subject'] = '用程序发送的电子邮件'
msg['From'] = mail_user
#重组收件人信息
msg['To'] = ";".join(mailto_list)

#发送电子邮件
try:
    s = smtplib.SMTP()
    
    #连接SMTP服务器
    s.connect(mail_host)
    #用账号和密码登录
    
    s.login(mail_user, mail_pass)
    #发送
    s.sendmail(mail_user, mailto_list, msg.as_string())
    #退出服务器
    s.close()
    print('发送完成')

#发送出现问题
except Exception as e:
    print(str(e))
    print()
    print('发送失败')











