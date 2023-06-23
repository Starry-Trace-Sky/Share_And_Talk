"""
=================================================
@Project -> File    ：Share_And_Talk -> publish
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/23 20:43
@用途               ：
@email              ：3385213313@qq.com
==================================================
"""
import pysnooper
import os
from github import Github


with pysnooper.snoop():
    token = os.environ.get('GITHUB_TOKEN')
    g = Github(token)

    repo = g.get_repo('Share_And_Talk')

    # 获取最新 tag
    latest_tag = repo.get_tags()[0]
    tag_name = latest_tag.name
    tag_message = latest_tag.commit.message

    # 创建 release
    repo.create_git_release(tag=tag_name, name=tag_name, message=tag_message)
