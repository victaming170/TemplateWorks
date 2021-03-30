import json

# ================= initial
write_first = True

json_dict = {
    'cfg_int': 3,
    'cfg_float': 3.14,
    'cfg_list': 3*[0],
    'cfg_str': "welcome!",
    '中文': '你好',
    'cfg_bool': True,
    'cfg_dict': {
        'k0': 6,
        'k1': 'hello, json.',
        'k2': [0, 1, 'three', [4.1, 4.4, '4.8'], 5],
        'k3': {
            'subk0': 9,
            'subk1': 'hello, dictionary.',
            'subk2': ['Mon', 'Tue', 'Wed']
            }
        }
}

json_name = 'template.json'

if write_first:
    # dump
    # 要向json写中文且易于阅读，需要使用"utf-8"打开json文件，且在"dump"时将"ensure_ascii"设为False；
    # 也可以做后者或全不做，这样的json中文可被python解释器正常处理，只是不易于阅读；
    with open(json_name, 'w', encoding='utf-8') as fj:
        json.dump(json_dict, fj, ensure_ascii=False, indent=4)
    print('-\ndump first\n-')

# load
# 如果向json写入时使用了'utf-8'编码且关闭了'ensure_ascii'，那么读取必须指定使用'utf-8'解码
with open(json_name, 'r', encoding='utf-8') as fj:
    json_dict_load = json.load(fj)

for k in json_dict_load:
    print(f'{k}: {json_dict_load[k]}')

