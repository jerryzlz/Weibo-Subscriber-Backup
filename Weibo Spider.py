from selenium import webdriver
import time
"""
File Description: 
Author: jerryzlz
Mail: jerryzlz4@hotmail.com
"""


class GetList(object):

    def init(self, username, password):
        """
        初始化浏览器窗口
        :param username: 登录手机/邮箱
        :param password: 登录密码
        """
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

    def get_follow_list(self, speed=1.5):
        """
        获取关注列表
        :param speed: 等待翻页时间（单位：秒）
        :return: None
        """
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
            time.sleep(speed)
        self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()
        for i in range(len(follow_namelist)):
            follow_list.append([follow_namelist[i], follow_urllist[i]])
        filename = "following_" + str(time.strftime("UTC%Y-%m-%d_%H-%M-%S", time.gmtime())) + ".txt"
        output = open(str(filename), "w", encoding="utf-8")
        for f in follow_list:
            output.write(",".join(f) + "\n")
        output.close()
        print("关注列表已成功保存")
        print("文件名为：{}" .format(filename))
        print("=" * 100)

    def get_fan_list(self, speed=1.5):
        """
        获取粉丝列表
        :param speed: 等待翻页时间（单位：秒）
        :return: None
        """
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
            time.sleep(speed)
        self.driver.find_element_by_xpath('/html/body/div[1]/a[1]').click()

        for i in range(len(fan_namelist)):
            fan_list.append([fan_namelist[i], fan_urllist[i]])
        filename = "fan_" + str(time.strftime("UTC%Y-%m-%d_%H-%M-%S", time.gmtime())) + ".txt"
        output = open(str(filename), "w", encoding="utf-8")
        for f in fan_list:
            output.write(",".join(f) + "\n")
        output.close()
        print("粉丝列表已成功保存")
        print("文件名为：{}" .format(filename))
        print("=" * 100)

    def close(self):
        self.driver.quit()

    def difference(self, list1, list2):
        """
        获得两个列表之间的差值
        :param list1: 输入列表1
        :param list2: 输入列表2
        :return: 返回差值列表
        """
        list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
        return list_dif

    def compare(self, old_filepath, new_filepath):
        """

        :param old_filepath: 输入列表1的文件名
        :param new_filepath: 输入列表2的文件名
        :return: None
        """
        old_file, new_file = open(old_filepath, "r", encoding="utf-8"), open(new_filepath, "r", encoding="utf-8")
        old_list, old_urllist, new_list, new_urllist, compared = [], [], [], [], []
        for line in old_file:
            old_list.append(line.strip("\n").split(","))
        for line in new_file:
            new_list.append(line.strip("\n").split(","))

        for i in range(len(old_list)):
            old_urllist.append(old_list[i][1])
        for i in range(len(new_list)):
            new_urllist.append(new_list[i][1])

        for i in old_urllist:
            if old_urllist.count(i) > 1:
                old_urllist.remove(i)
        for i in new_urllist:
            if new_urllist.count(i) > 1:
                new_urllist.remove(i)

        compared = self.difference(old_urllist, new_urllist)
        print(compared)
        if len(compared) != 0:
            filename = "compared_" + str(time.strftime("UTC%Y-%m-%d_%H-%M-%S", time.gmtime())) + ".txt"
            output = open(str(filename), "w", encoding="utf-8")
            for f in compared:
                output.write(f + "\n")
            output.close()
            print("=" * 100)
            print("粉丝列表已成功保存")
            print("文件名为：{}".format(filename))
        else:
            print("=" * 100)
            print("两个列表之间没有区别，未保存对比列表")


while True:
    print("="*100)
    print("1.获取关注列表")
    print("2.获取粉丝列表")
    print("3.同时获取关注和粉丝列表")
    print("4.使用两个本地已有的列表比对列表之间变化情况")
    print("0.退出本软件")
    print("=" * 100)
    num = int(input("请输入所需要的操作编号："))
    if num == 1:
        print("=" * 100)
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList()
        main.init(name, psd)
        main.get_follow_list(0.5)
        main.close()
    elif num == 2:
        print("=" * 100)
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList()
        main.init(name, psd)
        main.get_fan_list(0.5)
        main.close()
    elif num == 3:
        print("=" * 100)
        name = input("请输入登录邮箱/手机号：")
        psd = input("请输入密码：")
        main = GetList()
        main.init(name, psd)
        main.get_follow_list(0.5)
        main.get_fan_list(0.5)
        main.close()
    elif num == 4:
        print("=" * 100)
        print("将输出两个列表的差值")
        file1 = input("请输入第一个列表的文件名：")
        file2 = input("请输入第二个列表的文件名：")
        main = GetList()
        main.compare(file1, file2)
    elif num == 0:
        print("程序已关闭")
        break
    else:
        print("=" * 100)
        print("输入错误，请重新输入")
        continue
