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


# init vars
pattern = r"v\d+\.\d+\.\d+"
githubRef = os.environ.get("GITHUB_REF")
# latest tag
tag = githubRef.split('/')[-1]

with open('README.md', encoding='utf-8') as f:
    content = f.readlines()

Content = ''.join(content)
# match version position
result = re.findall(pattern, Content)[0]
re.sub(pattern, tag, Content)
print(Content)

# update REAMDE.md
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(Content)
