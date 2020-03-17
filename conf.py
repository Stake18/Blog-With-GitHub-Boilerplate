# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "Stake18/stake18.github.io@master"
}

# 站点设置
site_name = "大木桩18's Blog"
site_logo = "${static_prefix}icon.jpg"
site_build_date = "2020-3-17T00:00+08:00"author = "Stake18"
email = "swjh2000@foxmail.com"
author_homepage = "https://ignister.cn"
description = "苟利国家生死以，岂因祸福避趋之。"
key_words = ['Maverick',  'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "牌人杂记",
        "url": "https://ignister.cn",
        "brief": "Enjoy Playing."
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "GitHub",
        "url": "https://github.com/Stake18",
        "icon": "gi gi-github"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
