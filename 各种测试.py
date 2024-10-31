# import re
# import json
# text = 'window.__INIT_DATA = { "key": "value", "anotherKey": "anotherValue" data'
# match = re.search(r'window\.__INIT_DATA\s*=\s*{(.*?)data', text, re.DOTALL)
#
# if match:
#     content = "{" + match.group(1) + "}"
#     content = json.loads(content)
#     print("Matched content:", content['key'])
# else:
#     print("No match found.")
key = "【6口+6个宝】100%分成&gt;8000毫安【超级快充&gt;1231w"
options = key.split('&gt;')
print(options)