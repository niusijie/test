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



