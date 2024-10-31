import requests
import execjs
import time
import re

def update_cookie(response, cookies, params, data_para):
	cookies['_m_h5_tk'] = response.headers['set-cookie'].split('_m_h5_tk=')[1].split(';')[0]
	cookies['_m_h5_tk_enc'] = response.headers['set-cookie'].split('_m_h5_tk_enc=')[1].split(';')[0]

	token = cookies['_m_h5_tk'].split('_')[0]
	ts = int(time.time() * 1000)
	key = '12574478'
	para = token + "&" + str(ts) + "&" + key + "&" + data_para
	sign = execjs.compile(open('new1.js', 'r', encoding='utf-8').read()).call('c', para)
	params['sign'] = sign
	params['t'] = str(ts)
	return cookies, params


def get_sign(data, cookies):
	token = cookies['_m_h5_tk'].split('_')[0]
	ts = int(time.time() * 1000)
	key = '12574478'
	para = token + "&" + str(ts) + "&" + key + "&" + data
	sign = execjs.compile(open('new1.js', 'r', encoding='utf-8').read()).call('c', para)
	return sign, ts

def get_shop_info(url,cookies,headers):
    response = requests.get(url, cookies=cookies, headers=headers)
    match = re.search(r'memberId=(.*?)&', response.text, re.DOTALL)
    if match:
        print(match.group(1))
        return match.group(1)
    else:
        print(response.text)
        return None