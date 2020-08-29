import time
from selenium import webdriver
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet('统计')

#第一步:实例化对象
driver = webdriver.Chrome(r'F:/软测所需工具/chromedriver.exe')
# 第二步打开目标网址
driver.get('https://www.bilibili.com/')
#等待界面元素加载
driver.implicitly_wait(2)
#通过类名找目标元素
k = driver.find_element_by_class_name('nav-search-keyword')
k.send_keys('蜡笔小新台配')
#通过css属性查找元素
driver.find_element_by_css_selector('.nav-search-btn button').click()
time.sleep(2)
# 获取所有见面句柄
window = driver.window_handles
# 选择界面
driver.switch_to_window(window[-1])
aTags = driver.find_elements_by_class_name('title')
row = 0
for aTag in aTags:
    em = aTag.get_attribute('title')
    sh.write(row,0,em)
    row+=1
    print(em)
book.save(r'C:/Users/pc/Desktop/git本地库/学习软测之路/表格绘制/web自动化保存数据.xls')
# # 记得退出
driver.quit()
# driver.close()关闭当前页面 ,可进行js操纵 :driver.execute_script()

# 按钮可进行 ： .click() 点击;.submit() 提交
# 输入框可进行： .clean() 清除； .send_key() 填入
