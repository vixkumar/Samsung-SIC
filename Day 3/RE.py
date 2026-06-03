"""
import re
txt1 = "life is awesome"
txt2 = "blablabla"
print(re.search("life", txt1))
"""


import re
text = "please call 010-2345"
regex = re.compile('(\d{3})-(\d{4}-\d{4})')
match_obj = regex.search(text)
print(match_obj)

