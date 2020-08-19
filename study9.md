## 一、安装fiddler everwhere

1、官网下载地址 https://www.telerik.com/download/fiddler-everywhere

![image-20200818110324220](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818110324220.png)2、通过邮箱验证后登录就可以了。

## 二、如何通过fiddler everwhere对手机进行抓包

1、fiddler everwhere 设置

![image-20200818110537808](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818110537808.png)

![image-20200818110716057](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818110716057.png)

![image-20200818110820514](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818110820514.png)

**最后记得SAVE！！！**

2、iPhone设置

（1）在终端输入:ipconfig 查看本机IP![image-20200818145755257](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818145755257.png)

（2）手机设置：长按当前连接WiFi然后选修改网络，将代理选为自动 ，输入：服务器=本机IP地址；端口为fiddler ever where打开端口默认为 8866

（3）在任意浏览器输入ip+端口号 并下载证明书

在设置中查找关键词：证书 然后安装即可。

<u>iPhone下载后，在设置中找到安装后的证明书并安装。--》打开本机中的证明书并打开证明书。</u>

<u>安卓手机：在设置--》安全和隐私--》从SDK卡安装</u>



操作步骤：

1、手机与代理服务器连接

2、设定autorespone，将任意匹配的文件替换成我们要测试的文件

1、通过修改rv.txt中文件，替换成我们的测试网址(可调用main.py模块进行处理)

2、通过APP进行load，将内容下载下来，然后show展示。

## 三、琐碎知识补充

![image-20200818162629508](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200818162629508.png)

