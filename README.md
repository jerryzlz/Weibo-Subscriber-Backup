# Weibo-Subscriber-Backup
A Weibo spider base on selenium to backup all of subscribers.

## 功能描述
- 使用selenium爬取weibo.cn
- 备份现有关注/粉丝列表
- 导出txt格式文件方便查看
- 支持与过去列表比对查看列表增减变化
- 简单清爽，只专注列表增减变化

## 快速开始
1. 拥有python3.x环境
2. 下载源码
3. 解压后在当前目录下运行`pip3 install -r requirements.txt`安装selenium依赖环境
4. 运行`RUN_BEFORE_USE.bat`将浏览器内核移动至环境变量中（移动至用户目录\AppData\Local\Temp）也可手动将浏览器内核移动到其他环境变量地址中
5. 运行`Weibo Spider.py`即可

## 导出格式
- 文件名以fan_或following_开头后接导出的时间（UTC）
- 文件格式：
```sh
微博昵称， 微博主页地址

例：
wb昵称看简介， https://weibo.com/buyixiaohua
```
