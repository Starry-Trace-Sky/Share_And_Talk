# Share And Talk博客网站

![](https://img.shields.io/badge/Author1-Skyler_Sun-blue)
![](https://img.shields.io/badge/Author2-xjq-purple)

![](https://img.shields.io/badge/License-MIT-red)
![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Framework-Django-yellow)
![](https://img.shields.io/badge/Latest_Version-v1.3.5-brightgreen)

![网站主页](2023-06-10_192627.png)

## 功能介绍😁

1. 支持用户认证，头像上传（目前只支持qq头像和gravatar头像）
2. 支持文章发布，点赞，编辑，删除
3. 支持一级分类和二级分类标签
4. 支持文章markdown语法，高亮代码，Katex科学公式，flowchart流程图

## 注意事项💻

1. 网站上传文件位置位于`uploads`文件夹中，如需更改，请参见`ShareAndTalk/settings.py`
2. 本网站遵循[MIT License](./LICENSE)，使用本网站即代表用户同意该协议。用户使用本网站后，若造成不符合法律的不良影响，所承担的责任均与本网站的开发者无关

## 安装配置🍔

安装依赖

```bash
pip install -r requirements.txt
```

### 1.配置数据库

打开`ShareAndTalk/settings.py`，找到如下代码

```python
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your Database Name here',
        'USER': 'Your Database Account',
        'PASSWORD': 'Your Database Password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4' # database code
            # default sort order: utf8mb4_general_ci
        }
    }
}
```

将根据你使用的数据库进行相应更改

例如：
- 本项目测试的运行环境为**Mysql 8.0.32**
- 数据库运行在本地，`root`密码为`123456`
- 对应的数据库已建立好，名字为`myblog`，编码格式为`utf8mb4`，默认排序规则为`utf8mb4_general_ci`
，则进行如下配置

```python
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4' # database code
            # default sort order: utf8mb4_general_ci
        }
    }
}
```

### 2.配置语言

默认是根据中国的情况配置好了的。

如需更改，请在`ShareAndTalk/settings.py`找到如下代码

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'
```

将语言和时区对应修改即可，参见：

[语言标识符列表🚅](http://www.i18nguy.com/unicode/language-identifiers.html)

[时区列表1🧪](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

[时区列表2🎈](https://www.zeitverschiebung.net/cn/all-time-zones.html)

若你的语言不是中文，则还需要删除`ShareAndTalk/settings.py`中的以下代码

```python
# Default language
LANGUAGES = [
    ('zh-hans', '中文（简体）'),
]
```

### 3.配置邮箱

此功能用于主页底部的**用户反馈**

打开`ShareAndTalk/settings.py`，找到以下代码

```python
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True # Enable TLS transportation
EMAIL_HOST_USER = 'Your Email'
EMAIL_HOST_PASSWORD = 'Your Password'
DEFAULT_FROM_EMAIL = 'Your Email'

DEFAULT_RECIPIENT_LIST = ['Your Email']
```

将`EMAIL_HOST_USER`，`EMAIL_HOST_PASSWORD`，`DEFAULT_FROM_EMAIL`修改为你自己的邮箱和秘钥
此处默认设置为qq邮箱，若需要更改，请参考[django邮箱配置]()

将`DEFAULT_FROM_EMAIL`改为收件邮箱地址

### 4.创建超级用户

在本项目根目录下，打开`powershell`，输入以下命令

```bash
py manage.py createsuperuser
```

根据提示进行创建即可

## 部署🌭

1. 打开`ShareAndTalk/settings.py`，将

```python
DEBUG = True
```

改为

```python
DEBUG = False
```

2. 打开`powershell`，cd到仓库根目录后，运行以下命令，将静态文件收集到`static`文件夹中

```bash
py manage.py collectstatic
```

注：`static`文件夹在运行命令后会自动创建，若需更改文件夹位置，请修改`ShareAndTalk/settings.py`的以下代码

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
if not DEBUG:
    STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'), # Change your static folder here
    )
    STATIC_ROOT = os.path.join(BASE_DIR,'static') # Change your static folder here
```

3. 配置apache2和数据库服务

### 常用命令

1. 恢复表结构（进入mysql）（先检查是否已恢复）(account,key:root skyler)

```
mysql> source backup/db_structure.sql;
```

2. 还原数据库数据

```bash
py manage.py loaddata backup/xxx.json
```

3. Django Shell

```bash
py manage.py shell
```

### 运行环境

```text
asgiref==3.6.0
certifi==2023.5.7
charset-normalizer==3.1.0
Django==4.2.1
django-mdeditor==0.1.20
django-simpleui==2023.3.1
emoji==2.2.0
fontawesome==5.10.1.post1
idna==3.4
Markdown==3.4.3
mysqlclient==2.1.1
PySnooper==1.1.1
requests==2.30.0
sqlparse==0.4.4
tzdata==2023.3
urllib3==2.0.2

```
