# .88b  d88. d888888b d8b   db  d888b  Cb  .d8b.  d8b   db db      d888888b       .o88b. d888888b d888888b db    db         
# 88'YbdP`88   `88'   888o  88 88' Y8b `D d8' `8b 888o  88 88        `88'        d8P  Y8   `88'   `~~88~~' `8b  d8'         
# 88  88  88    88    88V8o 88 88       ' 88ooo88 88V8o 88 88         88         8P         88       88     `8bd8'          
# 88  88  88    88    88 V8o88 88  ooo    88~~~88 88 V8o88 88         88         8b         88       88       88            
# 88  88  88   .88.   88  V888 88. ~8~    88   88 88  V888 88booo.   .88.        Y8b  d8   .88.      88       88            
# YP  YP  YP Y888888P VP   V8P  Y888P     YP   YP VP   V8P Y88888P Y888888P       `Y88P' Y888888P    YP       YP            
#                                                                                                                           
#                                                                                                                           
# .d8888. d8888b. d88888b  .o88b. d888888b  .d8b.  db            .o88b. d888888b d888888b d888888b d88888D d88888b d8b   db 
# 88'  YP 88  `8D 88'     d8P  Y8   `88'   d8' `8b 88           d8P  Y8   `88'   `~~88~~'   `88'   YP  d8' 88'     888o  88 
# `8bo.   88oodD' 88ooooo 8P         88    88ooo88 88           8P         88       88       88       d8'  88ooooo 88V8o 88 
#   `Y8b. 88~~~   88~~~~~ 8b         88    88~~~88 88           8b         88       88       88      d8'   88~~~~~ 88 V8o88 
# db   8D 88      88.     Y8b  d8   .88.   88   88 88booo.      Y8b  d8   .88.      88      .88.    d8' db 88.     88  V888 
# `8888Y' 88      Y88888P  `Y88P' Y888888P YP   YP Y88888P       `Y88P' Y888888P    YP    Y888888P d88888P Y88888P VP   V8P 
#                                                                                                                           
#                                                                                                                           
# d888888b d8888b.       d888b  d88888b d8b   db d88888b d8888b.  .d8b.  d888888b  .d88b.  d8888b.                          
#   `88'   88  `8D      88' Y8b 88'     888o  88 88'     88  `8D d8' `8b `~~88~~' .8P  Y8. 88  `8D                          
#    88    88   88      88      88ooooo 88V8o 88 88ooooo 88oobY' 88ooo88    88    88    88 88oobY'                          
#    88    88   88      88  ooo 88~~~~~ 88 V8o88 88~~~~~ 88`8b   88~~~88    88    88    88 88`8b                            
#   .88.   88  .8D      88. ~8~ 88.     88  V888 88.     88 `88. 88   88    88    `8b  d8' 88 `88.                          
# Y888888P Y8888D'       Y888P  Y88888P VP   V8P Y88888P 88   YD YP   YP    YP     `Y88P'  88   YD                          
#                                                                                                                           
#明安里市特殊市民身份识别码生成器 | Mingan'li City Special Citizen ID Generator
#Python 第一版 | Python v1
#由 Diamochang 开发 | Developed by Diamochang (Mike Wang) [https://github.com/Diamochang]
#明安里市网站：www.minganli.line.pm | Mingan'li City's Website: www.minganli.line.pm

import sys #用于退出程序等
from platform import python_version #用于显示 Python 版本
import random #用于生成五位随机码
import qrcode #用于生成识别码的二维码形式
import time #用于受理时间和办结时间的记录
import barcode
from barcode.writer import ImageWriter #用于生成印制在特殊市民身份卡的条形码
import os #用于创建文件夹保存条形码和办结单

#欢迎信息和副本校验
print("--------------------------------------")
print(" 明安里市特殊市民身份识别码生成器")
print(" Python 第一版")
print(" 由 Diamochang 开发")
print(" ")
print(" 人人尽力，拯救我们赖以为生的水资源！")
print("--------------------------------------")
print("欢迎使用身份识别码生成器！")
print("检查 Python 版本......")
if sys.version_info >= (3,0):
    print("Python 版本符合要求（",python_version(),"，最低要求 3.0.0）",sep='')
else:
    print("Python 版本不符合最低要求 3.0.0。在 Python 2 上直接运行本程序会有兼容性问题，请参考 https://docs.python.org/3/howto/pyporting.html 修改程序使其兼容 Python 2。")
    sys.exit(1) #返回不兼容信息后直接终止程序
print("本程序需要验证校验码才能使用。请在下面输入仓库（或明安里市系列网站）向你提供的校验码。")
try:
    chkinput = input("校验码：")
except EOFError:
    pass
#密文提取校验码
chkenc = "" #此处暂时留白
def dectry(p):
    defk = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
    chkcode = ""
    for i,j in zip(p.split("_")[:-1],defk):
        temp = chr(int(i) - ord(j))
        chkcode = chkcode+temp
    return chkcode
chkcode = dectry(chkenc)
if chkinput == chkcode:
    print("验证成功！")
else:
    print("验证失败，请确认你输入的校验码是否准确无误。如果输入正确的校验码却返回此信息，程序有可能被恶意篡改，请前往本程序的仓库或明安里市系列网站重新下载。")
    sys.exit(1) #返回验证失败信息后直接终止程序
#AcpTime = time.strftime("%Y-%m-%d %H:%M:%S CST(UTC+8)",time.localtime()
print("--------------------------------------") #分隔

#基本信息
print("下面，请输入一些基本信息。")
try:
    Name = input("1.请输入被登记人姓名：")
    Gender = input("2.请输入被登记人的性别（对于机械生命体，这里填写制造者设定的性别。可填男/女/无性别特征）：")
except EOFError:
    pass
GenderCode = ""
if Gender == "男":
    GenderCode = "M"
elif Gender == "女":
    GenderCode = "F"
elif Gender == "无性别特征":
    GenderCode = "N"
elif not Gender is None:
    print("此值不能为空，请重新输入。")
else:
    print("输入了无效值，请重新输入。")
print("所在区简写供使用：龙明区-LM 两江区-LJ 兰花区-LH 兰花港区-LHG 启源县-QY 修定区-XD 云萍县-YP")
try:
    Zone = input("3.请输入被登记人所在的区（简写）：")
except EOFError:
    pass
ZoneCode = ""
ZoneName = ""
if Zone == "LM":
    ZoneCode = "202"
    ZoneName = "龙明区"
elif Zone == "LJ":
    ZoneCode = "201"
    ZoneName = "两江区"
elif Zone == "LH":
    ZoneCode = "205"
    ZoneName = "兰花区"
elif Zone == "LHG":
    ZoneCode = "305"
    ZoneName = "兰花港区"
elif Zone == "QY":
    ZoneCode = "206"
    ZoneName = "启源县"
elif Zone == "XD":
    ZoneCode == "203"
    ZoneName = "修定区"
elif Zone == "YP":
    ZoneCode = "204"
    ZoneName = "云萍县"
elif not Zone is None:
    print("此值不能为空，请重新输入。")
else:
    print("输入了无效值，请重新输入。")
try:
    Type = input("4.请输入被登记人的种类（机械生命体/人形兽类）：")
except EOFError:
    pass
if Type == "机械生命体":
    TypeCode = "RO"
elif Type == "人形兽类":
    TypeCode = "FU"
elif not Type is None:
    print("此值不能为空，请重新输入。")
else:
    print("输入了无效值，请重新输入。")
try:
    Birthday = input("5.请输入被登记人的出生日期（对于机械生命体，这里填写生命体首次激活日期。日期格式YYYYMMDD）：")
except EOFError:
    pass
if not Birthday is None:
    print("此值不能为空，请重新输入。")
print("--------------------------------------") #分隔

#信息确认及身份识别码生成
print("请与被登记人核对以下信息：")
print("姓名：",Name,sep='')
print("性别：",Gender,sep='')
print("所在区：",ZoneName,sep='')
print("特殊市民种类：",Type,sep='')
print("出生/首次激活日期：",Birthday,sep='')
try:
    Confirm = input("确认信息无误？（Y/N）")
except EOFError:
    pass
def mkdir(path):  #创建文件夹
    # os.path.exists 函数判断文件夹是否存在
    folder = os.path.exists(path)

    # 判断是否存在文件夹如果不存在则创建为文件夹
    if not folder:
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print('os.path.exists 返回：没有此文件夹。 ')
        print('os.makedirs 返回：文件夹创建成功。 ')
    else:
        print('os.path.exists 返回：文件夹已经存在。')
def Generate():
    #生成身份识别码
    print("生成中......")
    RandomNum = str(random.randint(0,99999)).zfill(5)
    ID = ZoneCode + TypeCode + Birthday + RandomNum + GenderCode
    #EndTime = time.strftime("%Y-%m-%d %H:%M:%S CST(UTC+8)",time.localtime()
    print("生成的身份识别码是：",ID,sep='')
    #创建办结单
    print("正在创建办结单......")
    mkdir("\\Bill")
    BillFile = '\\Bill\\23-SCID-' + ID + '.txt'
    #BillTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()
    with open(rBillFile,"w") as file:
     file.write("明安里市政务服务大厅 办结单\n")
     file.write("创建日期：",BillTime,"\n")
     file.write("----------------------------------\n")
     file.write("姓名：",Name,"\n")
     file.write("性别：",Gender,"\n")
     file.write("所在区：",ZoneName,"\n")
     file.write("----------------------------------\n")
     file.write("办理窗口：23-明安里市特殊市民管理中心\n")
     file.write("办理业务：明安里市特殊市民身份信息登记\n")
     file.write("受理人编号：23001\n")
     file.write("受理日期：",AcpTime,"\n")
     file.write("办结日期：",EndTime,"\n")
     file.write("----------------------------------\n")
     file.write("此单据是您需要办理的业务办结的凭据。为防止隐私泄露，请您妥善保存。\n")
     file.write("如果您对本次业务办理感到满意，或者您有意见建议，请对该窗口进行评价反馈。\n")
     file.write("明安里市政务服务便民热线：12345。\n")
    print("办结单已创建，请至",BillFile,"查看及打印。")
    #条形码生成
    print("正在生成条形码......")
    BarcodeFile = "SCID-" + ID + "_png"
    Barcode = barcode.CODE128(ID, writer=ImageWriter())
    Barcode.save(BarcodeFile)
    print("条形码已生成，请至 SCID-",ID,".png 查看。",sep='')
    #标准二维码生成
    print("正在生成二维码......")
    QRFile = "QR-SCID-" + ID + ".png"
    QRStandard = qrcode.QRCode( 
    version=5,  # 二维码的大小
    box_size=10, #二维码最小正方形的像素数量
    error_correction=qrcode.constants.ERROR_CORRECT_H, #设置最高纠错等级
    border=4 #设置外围白色边框
)
    QRStandard.add_data(ID) # 设置二维码数据
    QRImgS = QRStandard.make_image() # 创建二维码图片
    QRImgS.save(QRFile) # 保存二维码
    print("二维码已生成，请至 QR-SCID-",ID,".png 查看。",sep='')
if Confirm == "Y":
    Generate()
    print("生成完成。如果需要再生成，请重新启动此程序。")
    sys.exit(0)
elif Confirm == "y":
    Generate()
    print("生成完成。如果需要再生成，请重新启动此程序。")
    sys.exit(0)
elif Confirm == "N":
    print("操作取消。请重新启动程序进行生成。")
    sys.exit(0)
elif Confirm == "n":
    print("操作取消。请重新启动程序进行生成。")
    sys.exit(0)
else:
    print("输入了无效值，请重新输入。")