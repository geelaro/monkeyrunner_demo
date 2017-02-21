# Monkeyrunner API
## 概述
所述monkeyrunner API被包含在包中的三个模块 [com.android.monkeyrunner](https://developer.android.com/studio/test/monkeyrunner/index.html#APIClasses)：
- MonkeyRunner：一类为monkeyrunner程序的实用方法。这个类提供了用于连接monkeyrunner至设备或模拟器的方法。它也提供了用于创建用户界面的monkeyrunner程序和用于显示内置帮助的方法。
- MonkeyDevice：表示一个设备或模拟器。这个类提供了安装和卸载程序包，启动一个活动以及发送键盘或触摸事件到应用程序的方法。您也可以使用这个类来运行测试包。
- MonkeyImage：表示一个屏幕捕获图像。这个类提供了捕捉屏幕，将位图图像，以各种不同的格式，比较两个MonkeyImage对象，写一个图像文件的方法。

## 在Python中导入
- 分开导入，并自定义名方便调用
```
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
```
- 一次导入，用英文逗号（,）分开

```
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage 
```
## MonkeyRunner 
- 接入设备

```
#返回一个MonkeyDevice对象
#2种连接方式
#单设备
device=MonkeyRunner.waitForConnection()
#多设备
device=MonkeyRunner.waitForConnection (float timeout, string deviceId)
```
- 读取本地图片

```
MonkeyRunner.loadImageFromFile('D:\\shottrue.png')
```
- 延时,秒 

```
MoneyRunner.sleep(float seconds)
```
## MonkeyDevice
用MonkeyRunner.waitForConnection连接设备或模拟器，返回一个MonkeyDevice对象device。
- 安装apk

```
device.installPackage('myproject/bin/yy_offical.apk')
```
- 卸载apk,包名

```
device.removePackage ('com.duowan.mobile')
```
- 启动app

```
#参数是app的包名/活动名
device.startActivity(component="com.duowan.mobile/com.yy.mobile.ui.home.MainActivity")
```
- 触摸屏幕，（键码，类型）

```
#name为键码keycode,tye为按键类型
void press (string name, integer type)

#键码：
home键：KEYCODE_HOME
back键：KEYCODE_BACK
send键：KEYCODE_CALL
end键：KEYCODE_ENDCALL
上导航键：KEYCODE_DPAD_UP
下导航键：KEYCODE_DPAD_DOWN
左导航：KEYCODE_DPAD_LEFT
右导航键：KEYCODE_DPAD_RIGHT
ok键：KEYCODE_DPAD_CENTER
上音量键：KEYCODE_VOLUME_UP
下音量键：KEYCODE_VOLUME_DOWN
power键：KEYCODE_POWER
camera键：KEYCODE_CAMERA
menu键：KEYCODE_MENU

#按键类型：
UP, DOWN, DOWN_AND_UP

eg:device.press('KEYCODE_HOME',UP)
```
- 输入字符串
```
device.type("123456")
```
- 点击屏幕一个坐标点

```
# x y坐标，按键类型
void touch ( integer x, integer y, string type)

#按键类型：
UP, DOWN, DOWN_AND_UP

eg:device.touch(60, 148, 'DOWN_AND_UP')
```
- 唤醒屏幕

```
void wake()
```
- 重启

```
device.reboot()
```
- 截图

```
#返回一个MonkeyImage对象result
result = device.takeSnapshot()
```

## MonkeyImage 

通过device.takeSnapshot()得到一个MonkeyImage对象result。
- 保存截图

```
#将结果输出到文件,前面为路径，后面为图片类型，可写可不写
result.writeToFile('D:/shottrue1.png','png')
```
- 图片对比

```
#两个截图对比，判断相似度
boolean sameAs (MonkeyImage other, float percent)

eg:result1.sameAs(result2,0.9)
```




