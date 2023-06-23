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
import sys
from requests import get

import pysnooper

def getLatestTag():
    """get repository the latest tag"""
    url = 'https://api.github.com/repos/Skyler-Sun/Share_And_Talk/tags'
    req = get(url)
    if req.status_code == 200:
        tagName = req.json()[0]['name']
        return tagName
    else:
        return False

with pysnooper.snoop():
    # init vars
    pattern = r"v\d+\.\d+\.\d+"
    # latest tag
    latestTag = getLatestTag()
    if not latestTag:
        sys.exit(1)
    # read README.md
    with open('README.md', encoding='utf-8') as f:
        content = f.readlines()
    # replace version
    Content = ''.join(content)
    # match version position
    result = re.findall(pattern, Content)[0]
    Content = re.sub(pattern, latestTag, Content)

    # update REAMDE.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(Content)
