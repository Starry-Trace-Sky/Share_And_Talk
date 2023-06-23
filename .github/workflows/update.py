"""
=================================================
@Project -> File    ：Share_And_Talk -> update
@IDE                ：PyCharm
@Author             ：Skyler Sun
@Date               ：2023/6/23 19:46
@用途               ：
@email              ：3385213313@qq.com
==================================================
"""
import re
import os
import sys
from subprocess import call
from github import Github

import pysnooper


with pysnooper.snoop():
    # init vars
    pattern = r"v\d+\.\d+\.\d+"
    # latest tag
    token = os.environ.get('GITHUB_TOKEN')
    g = Github(token)

    repo = g.get_repo('Skyler-Sun/Share_And_Talk')

    latestTag = repo.get_tags()[0]
    tagName = latestTag.name
    # read README.md
    with open('README.md', encoding='utf-8') as f:
        content = f.readlines()
    # replace version
    Content = ''.join(content)
    # match version position
    result = re.findall(pattern, Content)[0]
    if result == tagName:
        sys.exit()

    Content = re.sub(pattern, tagName, Content)

    # update REAMDE.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(Content)

    # commit changes
    call(['git', 'add', '.'])
    call(['git', 'commit', '-m', 'Auto update README.md version'])
    call(['git', 'push', 'origin', 'main'])

    # create release
    tagMessage = latestTag.commit.message
    repo.create_git_release(tag=tagName, name=tagName, message=tagMessage)
