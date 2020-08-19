## 一、琐碎补充知识

git 是通过insert黏贴数据

## 二、学习Fiddler

1、AutoResponder（重定向）

即通过选你操作的目标网址进行重定向。且可以将本地文件传输到web服务器![image-20200817162209027](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200817162209027.png)

2、Ctrl+F查找目标

3、inspectors跟踪获取信息

## 三、通过ssh key 连接gitLab

1、已有一个本地仓库和gitLab账号

2、通过 ssh-keygen -t rsa -C ‘xxx@xxx.com’**然后一路回车**

（ps:此处的邮箱应该为你注册该账号时所用邮箱）

3、然后打开~/.ssh/id_rsa.pub文件(~表示用户目录，比如我的windows就是C:\Users\Administrator)，复制其中的内容

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200817144011526.png" alt="image-20200817144011526" style="zoom:80%;" />

4、打开gitlab找到图中指定位置

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200817144320601.png" alt="image-20200817144320601" style="zoom:50%;" />

5、将复制到的key复制到指定位置即可。

参考网址:https://www.cnblogs.com/hafiz/p/8146324.html



## 四、问题

1、问题一：不知怎么将会话拉到指定位置，以及不了解其作用。

![image-20200817152701297](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200817152701297.png)

2、这种乱码会有影响吗？

![image-20200817155045542](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200817155045542.png)