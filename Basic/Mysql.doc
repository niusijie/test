## 1、Mysql：是一种关系型数据库

## 2、Sql分类

DDL数据定义语言:create,drop,alter   (对库、表级)

DML数据操控语言：update,inster,delete （对表级）

DCL:数据控制语言：grant,if

## 3、数据库的增删改查

增：create database 数据库名

删：drop database  数据库名

改：alter database 数据库名 character 字符集 collate 校对规则

查：查看所有数据库：show databases;

　　查看某个数据库：show create database 数据库名；

## 4、数据表的增删改查

### 增

create table 表名{

​		字段 类型（长度）约束

​	}

**字段**：任意命名

**类型**：

string -->char varchar

float --> float

double --> double

文本文件 -->text

boolean --> bit

**约束：**

主键约束:primark key 用于保证该字段的值具有唯一性

唯一约束:unique 用于保证该字段的值具有唯一性，可以为空

非空约束：not null  用于保证该字段的值不能为空

外键约束：foreign key  用于限制二个表的关系，用于保证该字段的值必须来自于主表关联列的值



### 删

- 删表: drop table 表名

  

### 改

- **修改表添加列：**

*** alter table** **表名 add** **列名** **类型(****长度)** **约束;**

  \* alter table employee add image varchar(50);

- **修改表删除列：**

*** alter table** **表名 drop** **列名;**

  \* alter table employee drop job;

- **修改表的列的类型长度及约束:**

*** alter table** **表名 modify** **列名** **类型(****长度)** **约束;**

  \* alter table employee modify image varchar(80) not null;

- **修改表的列名**

*** alter table** **表名 change** **旧列名** **新列名** **类型(****长度)** **约束;**

  \* alter table employee change image eimage varchar(60);

- **修改表名**

*** rename table** **旧表名 to** **新表名;**

  \* rename table employee to user;

- **修改表的字符集：**

*** alter table** **表名character set** **字符集;**

  \* alter table user character set gbk;



### 查

查看表结构： desc 表名

show tables;



## 5、数据表内容的增删改查

### 增 

*** insert into** **表名 (****列名,****列名,...) values (****值1,****值2,...);   ---****插入指定列的值**

*** insert into** **表名 values (****值1,****值2,...);          ---****插入所有列的值**



### 删

删表内容：

- 删指定行  delect from 表名 where
- 删全部内容  delect from 表名   

​					truncate table 表名  

同 --》删除表全部数据，保留表结构，立刻释放磁盘空间

异 --》 Delete可以rollback撤销，truncate不能。



### 改

 **update** **表 set** **列名=****值,****列名=****值 [where** **条件];**

- **注意事项：**

***** **列名和值类型也要一致.**

***** **值不能超过列的最大长度.**

***** **值是字符串或日期,****需要使用单引号.**



### 查

select * from 表名 where  id = 1 group by name order by age 



 ![image-20200918175946749](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20200918175946749.png)

\* **交叉连接**：

  \* select * from A,B;  --- 获得的是两个表的笛卡尔积.

\* **内连接**: inner join -- inner 可以省略

  \* 显式内连接：select * from A inner join B on 条件;

  \* 隐式内连接：select * from A,B where 条件;

\* **外连接**：outer join -- outer 可以省略

   \* 左外连接：left outer join -- select * from A left outer join B on 条件;

  \* 右外连接：right outer join -- select * from A right outer join B on 条件;

【**多表查询的子查询**】

- 一个SQL语句查询的过程中需要依赖另一个查询语句.

SELECT * FROM customer c,orders o WHERE c.cid = o.cid AND c.cid IN (SELECT cid FROM orders WHERE addr LIKE '海淀%');

 



很赞的文章！！：https://www.cnblogs.com/xinlixue/p/6792523.html

