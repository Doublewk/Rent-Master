## 成都租房爬⾍、分析及可视化

**开发环境**：**Scrapy**、**Django5.0**

**项⽬描述**：该项⽬使⽤ **Scrapy** 框架爬取链家成都地区租房数据，通过 **Django** 框架写⼊数据库并使⽤ **Html** 将分析后的数据可视化展⽰到⽹⻚。

#### 教程
- 运行requirements.txt安装项目所需要的库
```
pip install -r requirements.txt
```

- 将rent目录下的settings.py文件中的数据库更换成你的数据库

- 进行数据库迁移
```
python manage.py makemigrations
python manage.py migrate
```

- 创建超级用户
```
python manage.py createsuperuser
```

- 进入rentSpider目录运行Scrapy进行爬虫

```
cd rentSpider
scrapy crawl house
```

- 启动Django

```
python manage.py runserver
```


