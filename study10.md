## 一、今日琐碎问题滴记录

![image-20200819152043714](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200819152043714.png)

在git进行commit时遇到这一问题解决方法。

设置全局用户并指定邮箱

git config --global user.email  “填入邮箱”

git config --global user.name “自定义用户名”



## 二、客户提供测试步骤总结

1. 点击预览查看横竖屏

2. 点击预览网址通过开发者工具查看在不同平台上的界面适配问题以及请求步骤

3. 查看详情需求

4. 将测试网址进行替换并在真机测试

   （1）横屏和竖屏的界面布局如何。

   （2）基础功能响应结合（人眼+fiddler everwhere）

   

三、问题

1、穿山甲app测试时：deeplink URL要填写什么

2、穿山甲app测试时：点击close按钮直接跳出

3、IronSource无法生成测试码



## 三、内部制作测试步骤

注意事项：进行较全面的覆盖测试如对 IA 和 RV 、视频播放以及不播放

#### 1、点击待测对象了解交付信息。了解投放渠道

#### 2、点击浏览查看是否兼容。以及响应问题

#### 3、在M渠道

##### （1）288

播放视频

查看界面

基础功能

自适应

然后看埋点是否遗漏

----------------------------------------------

不播放视频

查看界面

基础功能

自适应

然后看埋点是否遗漏

##### （2）94

播放视频

查看界面

基础功能

自适应

然后看埋点是否遗漏

----------------------------------------------

不播放视频

查看界面

基础功能

自适应

然后看埋点是否遗漏

#### 4、在DSP渠道

##### （1）DoubleClick

按照文档所诉，修改测试网址：PS注意要去掉代理。

##### （2）Mopub

在网页：根据要测试的对象选择网址--》点击Main.py脚本中的DSP按钮然后在

![image-20200820154758128](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200820154758128.png)

得到我们的HTML，然后复制到测试台并save

在移动端：后台数据自动保存到移动端的（test:只PL;  pl-rv：pl+video）

Android的是在pltest

##### （3）Chartboost

运行脚本--》在fiddler 的autorespond中添加rule（按照文档添加） 然后按照文档操作即可（PS不可点击跳转是正常的）

##### （4）inneractive

运行main.py文件生成对应mock文件：inneractice_ec.json，inneractice.json--》登录文档中指定网址--》将

inneractice_ec.json文本内容复制到markup

![image-20200820171643436](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200820171643436.png)

5、在Google渠道

安装文档上传Zip，能成功上传即可。

6、Applovin

安卓：在机上实操时黑屏属于正常现象可忽略，点击成功即可不一定需要跳转到商店。

IOS:相对应的应用打不开所以直接在网页上预览即可

7、DSP生成的json文件中 有ec的是没有视频的，没有ec是有视频的

8、install后才弹出猜你喜欢或者结束gamend是可以的

9、loading稍微有点久才跳出来没关系

10、Unity

不要用代理！！！

11、客户提供：猜你喜欢挡着按钮或图标没关系

12、endcard类型可以在播放完毕后自动gamend，但下载这需要自行操作

13、facbook没有下载函数是正常的

14、客户提供错别字不用管

15、DCO类素材不用管action

16、客户提供产品名称和内容不一致时不用管

17、游戏gamend是根据gamestart的时间开始计算而不包含视频播放时间，若视频播放后直接gamend则不合理。

18、只有客户提供(ss)的需要打回 ，其余都是跟研发讲就行。Voodoo优先测试，voodoo在非ss

19、检验兜底语言是什么，可在lang=参数中输入不存在的值进行校验。

## 四、mindWork官网检测

20、750要用iPhoneX看



## 五、遇到invalbe token问题

![image-20200914152732228](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200914152732228.png)

由于文本中有重复的<body>标签被正则匹配，所以要避免被匹配

1、通过基础包ID在基础包管理中找到对应的基础包并下载下来

2、打开基础包中的html文本找到报错句子 <body --》‘<’+’body

3、重新压缩PS注意要是ZIP格式，然后点击任务管理中的更新重新上传即可