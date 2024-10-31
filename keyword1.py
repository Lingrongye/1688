import json

import requests
from utils import update_cookie,get_sign
from get_detail import get_detail
def get_keyword_goods(keyword,num_of_data=100,file_path='',tag=''):
	with open('cookies.json','r') as f:
		cookies = json.loads(f.read())

	headers = {
		'accept': '*/*',
		'accept-language': 'en-GB,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,en-US;q=0.6',
		# 'cookie': 'lid=tb803910983702; cna=G4ZhH0HjOgQCAd0EIpRREz/l; leftMenuLastMode=COLLAPSE; mtop_partitioned_detect=1; _m_h5_tk=89925a39df8066ba7acbb854cd1a761d_1728466838367; _m_h5_tk_enc=c514d37812679d2196c68e50a43deee2; cookie2=1872467ff8bba2baf013dd1a22b98308; hng=GLOBAL%7Czh-CN%7CUSD%7C999; t=ec0d59b37f284166e7017bee6aa82fb5; _tb_token_=e55e0b4bde8ed; ali_apache_track=c_mid=b2b-2218556594957c7d44|c_lid=tb803910983702|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; leftMenuModeTip=shown; xlly_s=1; cookie1=VFD9oiP8EuBmFNz7kXW%2B2SlRAKGqgzPQfhRkmb%2FDaO4%3D; cookie17=UUpgTsxLTodDFkvCug%3D%3D; sgcookie=E100tF%2BdwCqBxexeDaaigaFyZA53Y5dEDANY%2FEp4A54Pqee6W%2Bjkjiy6hxwnuggvcQ2PNx6ZJUtO8dE3bXmzvutrymjSwPIde0knDgNd0NwiPeM%3D; sg=274; csg=96fc5f74; unb=2218556594957; uc4=nk4=0%40FY4GsvaLBaBSNmC5Gwtx7zSd7aRq2eB4VA%3D%3D&id4=0%40U2gqwYWt%2BHbq0Y7slOivQu5kreOQQ%2Be8; _nk_=tb803910983702; __cn_logon__=true; __cn_logon_id__=tb803910983702; last_mid=b2b-2218556594957c7d44; _csrf_token=1728457266030; firstRefresh=1728457271800; lastRefresh=1728457271800; aliwwLastRefresh=1728457271838; is_identity=buyer; _is_show_loginId_change_block_=b2b-2218556594957c7d44_false; _show_force_unbind_div_=b2b-2218556594957c7d44_false; _show_sys_unbind_div_=b2b-2218556594957c7d44_false; _show_user_unbind_div_=b2b-2218556594957c7d44_false; __rn_alert__=false; ctk=449a0e6b4558392d9a3f68ef7d30f33d; aliwwLastNum=0; keywordsHistory=%E8%BF%9E%E8%A1%A3%E9%95%BF%E8%A3%99; isg=BHBwrrse43UMMb6tgq-7r1OgQT7CuVQDMsMBymrD5krRJRLPEsr5k-RWfSVF7wzb; tfstk=g-osEJOCi1fs9f_ZynpUPo7Z96rXLjtrBtwxExINHlETM2w4UsCxHCcjcWHm7ol4bZ_jaxPT_Kvccr3KnVJguCXjRfD87jMDI-FxMjNq7e-rIAq0DQPX43kiNBx6mq_ODHpYH8dzAK6rBAq0DB-PpR6IIbErH33YHJpQ3-7A6jFOJMeY9-QTDjFLJ8eP6oExMpaLF-CYB5FYv6ez9SEYDjHKMbfQKFNECpvvax7JGOMaOiIxAJdgwA6RVRo3CyV-BrLDoUe_57HTOQkdPoUKnricniaZB4c0efC91oHQFbwS1EW012HrbqH6AQEZjA38k0dckbZsGznTRtIjIoNTAJnJ3aVEA5lxfypPVrrK4zEt8eAaulwSMcc1hih-LYog-mO59S0aEkesM3dC4uIzNDu1l9alcJNydp_co2hXy1V5GobzWJ2U4p9CzZ4TKJNydp_coPe3KaJBda7c.; _user_vitals_session_data_={"user_line_track":true,"ul_session_id":"2tsdtmtr2co","last_page_id":"s.1688.com%2Folzjwx5oh0c"}',
		'referer': 'https://s.1688.com/',
		'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'script',
		'sec-fetch-mode': 'no-cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
	}

	params = {
		'jsv': '2.5.1',
		'appKey': '12574478',
		# 't': '1728457404265',
		# 'sign': 'b8738201f84302ef37f544f2c7e78605',
		'api': 'mtop.relationrecommend.WirelessRecommend.recommend',
		'v': '2.0',
		'jsonpIncPrefix': 'reqTppId_32517_getOfferList',
		# 'data': '{"appId":32517,"params":"{\\"beginPage\\":1,\\"pageSize\\":60,' \
		# 		'\\"method\\":\\"getOfferList\\",\\"pageId\\":\\"\\",' \
		# 		'\\"verticalProductFlag\\":\\"pcmarket\\",\\"searchScene\\":\\"pcOfferSearch\\",\\"charset\\":\\"GBK\\",' \
		# 		'\\"spm\\":\\"a26352.13672862.searchbox.0\\",\\"keywords\\":\\"手机壳\\"}"}'
	}
	data_para = '{"appId":32517,"params":"{\\"beginPage\\":1,\\"pageSize\\":60,' \
				'\\"method\\":\\"getOfferList\\",\\"pageId\\":\\"\\",' \
				'\\"verticalProductFlag\\":\\"pcmarket\\",\\"searchScene\\":\\"pcOfferSearch\\",\\"charset\\":\\"GBK\\",' \
				'\\"spm\\":\\"a26352.13672862.searchbox.0\\",\\"keywords\\":\\"%s\\"}"}' % keyword
	params['data'] = data_para
	sign, t = get_sign(data_para,cookies)
	params['t'] = t
	params['sign'] = sign
	response = requests.get(
		'https://h5api.m.1688.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
		params=params,
		cookies=cookies,
		headers=headers,
	)
	#data_para = '{"appId":32517,"params":"{\"beginPage\":1,\"pageSize\":60,\"method\":\"getOfferList\",\"pageId\":\"\",\"verticalProductFlag\":\"pcmarket\",\"searchScene\":\"pcOfferSearch\",\"charset\":\"GBK\",\"spm\":\"a26352.13672862.searchbox.0\",\"keywords\":\"%CA%D6%BB%FA%BF%C7\"}"}'
	try:
		if "令牌过期" in response.json()['ret'][0]:
			cookies,params = update_cookie(response,cookies,params,data_para)
			with open('cookies.json','w') as f:
				f.write(json.dumps(cookies))

			response = requests.get(
				'https://h5api.m.1688.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/',
				params=params,
				cookies=cookies,
				headers=headers,
			)

		items = response.json()['data']['data']['OFFER']['items']
		number_of_data = 0
		for item in items:
			print(item['data']['offerId'])
			if number_of_data >= num_of_data:
				break
			url = 'https://detail.1688.com/offer/'+ item['data']['offerId']+'.html'
			get_detail(url,file_path,tag)
			number_of_data += 1
			break

	except Exception as e:
		print(response.text)
		print(e)


if __name__ == '__main__':
	get_keyword_goods('戒指',10,'test.csv')

