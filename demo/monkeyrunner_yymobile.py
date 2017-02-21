#coding:utf-8
'''
Created on 2017年2月21日

@author: geelaro
'''
from com.android.monkeyrunner import MonkeyRunner
import time
import sys
now = time.strftime("%Y-%m-%d-%H-%M-%S")

# 指定我们要保存图片的位置和打印log的位置
path = 'D:\\picture\\'
logpath = "D:\\log\\"
# python中获取当前运行的文件的名字
name = sys.argv[0].split("\\")
filename = name[len(name) - 1]
# 新建一个log文件
log = open(logpath + filename[0:-3] + "-log" + now + ".txt", 'w')


# 连接设备
device = MonkeyRunner.waitForConnection()
# 安装app
# device.installPackage('E:\\downloads\\offical.apk') 
log.write("安装apk……\n")
# 等待2秒
MonkeyRunner.sleep(2)


# 启动app，参数里是app的包名/活动名
device.startActivity(component="com.duowan.mobile/com.yy.mobile.ui.home.MainActivity")
# 打印操作信息
log.write("启动app……\n")
# 等待2秒
MonkeyRunner.sleep(5)
# 截图
result = device.takeSnapshot()
# 保存截图 
result.writeToFile(path + "首页".decode('utf-8') + now + '.png', 'png')



# 点击的位置坐标。
device.touch(60, 148, 'DOWN_AND_UP')
MonkeyRunner.sleep(5)
# 输入72082645字样
device.type("72082645")
#点击确定
device.touch(500, 300, 'DOWN_AND_UP')

# 截图
result1 = device.takeSnapshot()
# 保存截图
result1.writeToFile(path + "个人页".decode('utf-8') + now + '.png', 'png')


# 下面就开始对之前的截图进行对比了
# 第一张截图做对比，去文件中找到我们要对比的图片
resultTrue = MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue.png')
log.write("主页面对比图片……\n")
# 判断图片相识度是否是为90%
if(result.sameAs(resultTrue, 0.5)):
    # 在命令行打印出信息
    print("主页面图片对比成功")
    # 打印信息到log文件
    log.write("主页面图片对比成功……\n")
else:
    # 打印信息到命令行
    print("主页面图片对比失败")
    log.write("主页面图片对比失败……\n")


# 去文件中找到我们规定的图片用来对比
result1True = MonkeyRunner.loadImageFromFile('D:\\picture2\\shottrue1.png')
# 判断图片相识度是否是为90%
if(result1.sameAs(result1True, 0.5)):
    print("个人页图片对比成功")
    log.write("个人页图片对比成功……\n")
else:
    print("个人页图片对比失败")
    log.write("个人页图片对比失败……\n")
