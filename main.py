from selenium import webdriver
import time


class GetList(object):

    def __init__(self, username, password):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(375, 667)
        self.driver.get('https://weibo.cn/')
        self.driver.find_element_by_xpath('/html/body/div[2]/div/a[1]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="loginName"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginWrapper"]').click()
        self.driver.find_element_by_xpath('//*[@id="loginAction"]').click()
        time.sleep(3)

    def get_follow_list(self, sleep_time=2.5):
        print("=" * 100)
        print("开始获取关注列表")
        # self.driver.minimize_window()
        follow_list = []
        follow_namelist = []
        follow_urllist = []
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[2]').click()
        time.sleep(3)
        follow_pages = self.driver.find_element_by_xpath('/html/body/div[15]/form/div/input[1]').get_attribute('value')
        # print(follow_pages)
        for j in range(int(follow_pages)):
            for i in range(0, 10):
                element = "/html/body/table[" + str(i+1) + "]/tbody/tr/td[2]/a[1]"
                try:
                    following_name = self.driver.find_element_by_xpath(element)
                    follow_namelist.append(following_name.text)
                    follow_urllist.append(following_name.get_attribute('href'))
                except:
                    continue
            try:
                self.driver.find_element_by_link_text("下页").click()
            except:
                break
            time.sleep(sleep_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
        for i in range(len(follow_namelist)):
            follow_list.append([follow_namelist[i], follow_urllist[i]])
        filename = "following_" + str(time.strftime("UTC%Y-%m-%d_%H-%M-%S", time.gmtime())) + ".txt"
        output = open(str(filename), "w", encoding="utf-8")
        for f in follow_list:
            output.write(",".join(f) + "\n")
        output.close()
        print("关注列表已成功保存")
        print("=" * 100)


    def get_fan_list(self, sleep_time=2.5):
        print("=" * 100)
        print("开始获取粉丝列表")
        # self.driver.minimize_window()
        fan_list = []
        fan_namelist = []
        fan_urllist = []
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/a[3]').click()
        time.sleep(3)
        fan_pages = self.driver.find_element_by_xpath('/html/body/div[5]/div[12]/form/div/input[1]').get_attribute('value')
        # print(fan_pages)
        for j in range(0, int(fan_pages)):
            for i in range(0, 10):
                element = "/html/body/div[5]/table[" + str(i + 1) + "]/tbody/tr/td[2]/a[1]"
                try:
                    fan_name = self.driver.find_element_by_xpath(element)
                    fan_namelist.append(fan_name.text)
                    fan_urllist.append(fan_name.get_attribute('href'))
                except:
                    continue
            try:
                self.driver.find_element_by_link_text("下页").click()
            except:
                break
            time.sleep(sleep_time)
        self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()

        for i in range(len(fan_namelist)):
            fan_list.append([fan_namelist[i], fan_urllist[i]])
        filename = "fan_" + str(time.strftime("UTC%Y-%m-%d_%H-%M-%S", time.gmtime())) + ".txt"
        output = open(str(filename), "w", encoding="utf-8")
        for f in fan_list:
            output.write(",".join(f) + "\n")
        output.close()
        print("粉丝列表已成功保存")
        print("=" * 100)

    def file_mutual_following(self):
        pass


while True:
    print("="*100)
    print("1.获取关注列表")
    print("2.获取粉丝列表")
    print("3.同时获取关注和粉丝列表")
    print("4.使用两个本地已有的列表比对关注/粉丝变化情况（暂未完成）")
    print("5.使用本地已有的列表比对当前关注/粉丝变化情况（暂未完成）")
    print("6.退出本软件")
    print("=" * 100)
    num = int(input("请输入所需要的操作编号："))
    if num == 1:
        speed = float(input("设置获取列表时点击下一页的等待时间 若不设置请直接回车 默认值为2.5秒（单位：秒）："))
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList(name, psd)
        if speed == "":
            continue
        else:
            main.get_follow_list(speed)
    elif num == 2:
        speed = float(input("设置获取列表时点击下一页的等待时间 若不设置请直接回车 默认值为2.5秒（单位：秒）："))
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList(name, psd)
        if speed == "":
            continue
        else:
            main.get_fan_list(speed)
    elif num == 3:
        speed = float(input("设置获取列表时点击下一页的等待时间 若不设置请直接回车 默认值为2.5秒（单位：秒）："))
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList(name, psd)
        if speed == "":
            continue
        else:
            main.get_follow_list(speed)
            main.get_fan_list(speed)
    elif num == 6:
        print("程序已关闭")
        break
    else:
        print("输入错误，请重新输入")
        continue



