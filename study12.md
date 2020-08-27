## 一、测试环境的学习

### 1.mindwork官网

1、 第一步用Key登录跳板机

2、直接敲satool查看本组服务器的分组列表

3、选择分组以及服务器

![image-20200824150951991](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200824150951991.png)7\

4、通过sudo su - 切换到开发机的root权限

5、切换到mindworks官网项目，目录：/data/www/mindworks-v2  （*cd /data/www/mindworks-v2*）

6、拉取该路径下的代码： git pull 后执行命令构建 npm run build:test

7、在如下路径下添加‘’到本机host文件

![image-20200824144142007](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200824144142007.png)

配置hosts18.211.47.130 [mindworks-v2.test.com](http://mindworks-v2.test.com/) [api.mindworks-creative.com](http://api.mindworks-creative.com/)

8、访问测试环境

### 2.素材仓库

1、登录跳板机

2、切换权限 sudo su -

3、切换到素材仓库项目，后端目录：/data/www/portal-backend 前端目录：/data/www/portal-fe

4、拉取代码

5、配置host 18.211.47.130 [creative-api-test.mintegral.com](http://creative-api-test.mintegral.com/) [playable-portal-testapi.mintegral.com](http://playable-portal-testapi.mintegral.com/)

6、登录到http://playable-portal-test.mintegral.com/#/system/profile测试

## 二、琐碎知识补充

1、系统会首先自动从Hosts文件中寻找对应的IP地址，一旦找到，浏览器会立即打开对应网页，如果没有找到，则浏览器会将网址提交DNS服务器进行IP地址解析。这也是提高快速打开网页的方法！

2、Cookie和Session

**使用Cookie原因**:http协议是无状态协议从而服务端不晓得是谁来访问

**来源**：服务端向客户端发送一33个Cookie

**存储**：在浏览器存储

**Cookie**:（小型文本）相当于可定义期限的会员卡。内可包含多种属性。，

**Session**：用于记录客户在该服务器的会话或操作。存放在服务器中，通过sessionID来查找，

sessionID一开始会跟随Cookie发送到客户端浏览器。

Session 对象存储特定用户会话所需的属性及配置信息。这样，当用户在应用程序的 Web 页之间跳转时，存储在 Session 对象中的变量将不会丢失，而是在整个用户会话中一直存在下去。当用户请求来自应用程序的 Web 页时，如果该用户还没有会话，则 Web 服务器将自动创建一个 Session 对象。当会话过期或被放弃后，服务器将终止该会话。

## 三、计算机网络基础

### 1、OSI7层协议

物理层--》数据链路层--》网络层--》传输层--》会话层--》表示层--》应用层

### 2、TCP/IP 4层协议

网络接口层--》网络层--》传输层--》应用层

![image-20200826114545686](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200826114545686.png)

##### （1）物理层

确保数据在物理媒体上运输。重要的设备：中继器和集线器（工作原理都是通过对信号进行**再生**：*放大信号*和**重定时**。从而使得它们能够在网络上传输更长的距离）。（MAC地址来转发帧）

##### （2）数据链路层



![image-20200826115524247](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200826115524247.png)



**作用包括**：物理地址寻址、数据的成帧、流量控制、数据的检错、重发等



##### （3）网络层

网络层的目的是实现两个端系统之间的数据透明传送，具体功能包括寻址和路由选择、连接的建立、保持和终止等。

**基本数据单位为IP数据报**

-  **包含的主要协议：**
- 　　**IP协议（Internet Protocol，因特网互联协议）;**
- 　　**ICMP协议（Internet Control Message Protocol，因特网控制报文协议）;**
- 　　**ARP协议（Address Resolution Protocol，地址解析协议）;**
- 　　**RARP协议（Reverse Address Resolution Protocol，逆地址解析协议）。**
- 　　**> 重要的设备：路由器。**

个人理解：物理层通过中继器和集线器进行远距离的数据传送，而再通过数据链路层进行短距离的区域传送找到目标电脑。

##### （4）传输层

传输层则负责将数据可靠地传送到相应的端口。

主要协议：TCP协议和UDP协议

重要设备：网关





