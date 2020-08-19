# coding=utf-8
import unittest
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.HTMLTestRunner_cn import HTMLTestRunner

cur_path = os.path.dirname(os.path.realpath(__file__))
print('当前目录', cur_path)


def all_case():
    curdir = os.path.realpath(__file__)  # 当前目录
    back_curdir = os.path.dirname(curdir)  # 返回上一个层级
    curpath = os.path.join(os.path.dirname(back_curdir), 'all_Case')  # 定位到case目录
    print('运行目录', curpath)
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # 输出报告目录
    report_path = os.path.join(os.path.dirname(back_curdir), 'report', now + 'report.html')

    discover = unittest.defaultTestLoader.discover(start_dir=curpath, pattern='test*.py')
    report = report_path
    # 打开文件
    open_report = open(report, 'wb')
    # 运行已打开的open_report文件给result_file,包含输出样式
    result_file = HTMLTestRunner(open_report, verbosity=2,
                                 title='测试报告结果',
                                 description='壹行天下app自动化测试结果',
                                 retry=1)
    result_file.run(discover)
    open_report.close()


def get_report_file(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtpserver, report_file, port=465):
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"App自动化测试报告-请下载附件查看详情"
    msg["from"] = sender
    if isinstance(receiver, str):
        msg["to"] = receiver
    if isinstance(receiver, list):
        msg["to"] = ",".join(receiver)
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out !')


if __name__ == '__main__':
    all_case()
    # 获取最新的测试报告文件
    report_file = get_report_file(cur_path)  # 3获取最新的测试报告

    # 邮箱配置
    sender = "zhaozhenxing@transinfo.com.cn"
    psw = "zzx910129"
    smtp_server = "smtp.263.net"
    port = 465
    receiver = "zhaozhenxing@transinfo.com.cn"  # 多个时候为list
    # send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告
