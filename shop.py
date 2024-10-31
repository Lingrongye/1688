import requests

cookies = {
    'cna': '0duMH1FNeUsBASQAYABhe6MA',
    'xlly_s': '1',
    'cookie1': 'ACk0FVpSiiLcSC3c4aYV%2FU%2BlX1Z0cbLUfXy9BvxJLsA%3D',
    'cookie2': '18afdf0f1d03bec50b1e7432ddbcc455',
    'cookie17': 'UUphzpYtCw1vFYdFHA%3D%3D',
    'sgcookie': 'E100GMKy41e1QPF5vBv9M5i%2BLl3Cfh70mZKoyw3Z4bcHsVBBivnBNDtxXUos5qloiihiFYYueW4i9gReUoVVbLgtavJVog6Zs6vXVYm6HymOrTs%3D',
    't': 'f7aa0e7cc5610a7905d50620e4517ee9',
    '_tb_token_': 'e67a56e7385e7',
    'sg': '716',
    'csg': '81b8fa2c',
    'lid': 'tb185365847',
    'unb': '2204157185341',
    'uc4': 'id4=0%40U2grFbW2I5UvVXdvTtlCknlruGS2c0oV&nk4=0%40FY4PZPoOwFojuMgibAKskpunh%2FAwRQ%3D%3D',
    '_nk_': 'tb185365847',
    '__cn_logon__': 'true',
    '__cn_logon_id__': 'tb185365847',
    'ali_apache_track': 'c_mid=b2b-2204157185341d5ed1|c_lid=tb185365847|c_ms=1',
    'ali_apache_tracktmp': 'c_w_signed=Y',
    'last_mid': 'b2b-2204157185341d5ed1',
    '_csrf_token': '1728441851105',
    'taklid': '280cac183a9e4a06b0d02e66f57558c0',
    '__mwb_logon_id__': 'tb185365847',
    '_m_h5_tk': '24b2d7b3f5891d48e20d4fad98460342_1728464377724',
    '_m_h5_tk_enc': 'b0b812206053be259aa124c2f3c544db',
    'leftMenuLastMode': 'COLLAPSE',
    'leftMenuModeTip': 'shown',
    'x5sec': '7b22733b32223a2230623939316339316135303162366131222c22617365727665723b33223a22307c434944626d4c6747454e72596a7166372f2f2f2f2f774561447a49794d4451784e5463784f44557a4e4445374e4443657765713342413d3d227d',
    'mwb': 'tm',
    '_user_vitals_session_data_': '{"user_line_track":true,"ul_session_id":"qj29r2sfxkq","last_page_id":"leichexiangbao.1688.com%2Faynpaomsx04"}',
    'tfstk': 'g79nbPA6QB5CxyN1PcWIZ3WU8-cTRk652UeRyTQr_N71eBdKRu2kAemCwph5EUbGq7zzU37krFQ1yD9KAFYkoEdd2Uddzg7M88CpE3wl438SAanI6HtCFTuxkTDvAHN9LvpeKara_hsuLzkYcbEFWTuxkAFTb6gdUedlUpMMbNslYW7ezRWNvNSUTM8P71SVDyWPUUoG7gIAYM5UTOrNDN7PUT8zQR85AW7BUppZReX6CmXobpShtZ-F8HKpQsaAoHWTE8fhB6qpYN2zUdAO19Ol8jZOP9QB5MYShJ6FZB8hbTDuQ9YBYL5MeVHAtnSyP9pZ4W729eLPZCg0HMXpssvHO0awYEQHg9t8m2KGiCffb1ruT9dvDL12Lv4fWsskoiY3-gu0_S7K18sZ2dP7N6S1jZKYFLF6-rv_0cmggu1FfM7xjcV7N6S1jZnijS25TGsFk',
    'isg': 'BJWVx__ZXtKzsXotaj5p2g7TpJFPkkmk2PNcBBc6f40UbrRg3-O_dCloOHJY32Fc',
}

headers = {
    'authority': 'h5api.m.1688.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'cna=0duMH1FNeUsBASQAYABhe6MA; xlly_s=1; cookie1=ACk0FVpSiiLcSC3c4aYV%2FU%2BlX1Z0cbLUfXy9BvxJLsA%3D; cookie2=18afdf0f1d03bec50b1e7432ddbcc455; cookie17=UUphzpYtCw1vFYdFHA%3D%3D; sgcookie=E100GMKy41e1QPF5vBv9M5i%2BLl3Cfh70mZKoyw3Z4bcHsVBBivnBNDtxXUos5qloiihiFYYueW4i9gReUoVVbLgtavJVog6Zs6vXVYm6HymOrTs%3D; t=f7aa0e7cc5610a7905d50620e4517ee9; _tb_token_=e67a56e7385e7; sg=716; csg=81b8fa2c; lid=tb185365847; unb=2204157185341; uc4=id4=0%40U2grFbW2I5UvVXdvTtlCknlruGS2c0oV&nk4=0%40FY4PZPoOwFojuMgibAKskpunh%2FAwRQ%3D%3D; _nk_=tb185365847; __cn_logon__=true; __cn_logon_id__=tb185365847; ali_apache_track=c_mid=b2b-2204157185341d5ed1|c_lid=tb185365847|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; last_mid=b2b-2204157185341d5ed1; _csrf_token=1728441851105; taklid=280cac183a9e4a06b0d02e66f57558c0; __mwb_logon_id__=tb185365847; _m_h5_tk=24b2d7b3f5891d48e20d4fad98460342_1728464377724; _m_h5_tk_enc=b0b812206053be259aa124c2f3c544db; leftMenuLastMode=COLLAPSE; leftMenuModeTip=shown; x5sec=7b22733b32223a2230623939316339316135303162366131222c22617365727665723b33223a22307c434944626d4c6747454e72596a7166372f2f2f2f2f774561447a49794d4451784e5463784f44557a4e4445374e4443657765713342413d3d227d; mwb=tm; _user_vitals_session_data_={"user_line_track":true,"ul_session_id":"qj29r2sfxkq","last_page_id":"leichexiangbao.1688.com%2Faynpaomsx04"}; tfstk=g79nbPA6QB5CxyN1PcWIZ3WU8-cTRk652UeRyTQr_N71eBdKRu2kAemCwph5EUbGq7zzU37krFQ1yD9KAFYkoEdd2Uddzg7M88CpE3wl438SAanI6HtCFTuxkTDvAHN9LvpeKara_hsuLzkYcbEFWTuxkAFTb6gdUedlUpMMbNslYW7ezRWNvNSUTM8P71SVDyWPUUoG7gIAYM5UTOrNDN7PUT8zQR85AW7BUppZReX6CmXobpShtZ-F8HKpQsaAoHWTE8fhB6qpYN2zUdAO19Ol8jZOP9QB5MYShJ6FZB8hbTDuQ9YBYL5MeVHAtnSyP9pZ4W729eLPZCg0HMXpssvHO0awYEQHg9t8m2KGiCffb1ruT9dvDL12Lv4fWsskoiY3-gu0_S7K18sZ2dP7N6S1jZKYFLF6-rv_0cmggu1FfM7xjcV7N6S1jZnijS25TGsFk; isg=BJWVx__ZXtKzsXotaj5p2g7TpJFPkkmk2PNcBBc6f40UbrRg3-O_dCloOHJY32Fc',
    'origin': 'https://leichexiangbao.1688.com',
    'referer': 'https://leichexiangbao.1688.com/',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
}

params = {
    'jsv': '2.7.0',
    'appKey': '12574478',
    't': '1728458823252',
    'sign': '8807106fdb82b2bc42d3b54db12ae149',
    'api': 'mtop.alibaba.alisite.cbu.server.ModuleAsyncService',
    'v': '1.0',
    'type': 'json',
    'valueType': 'string',
    'dataType': 'jsonp',
    'timeout': '10000',
}

data = {
    'data': '{"componentKey":"Wp_pc_common_offerlist","params":"{\\"memberId\\":\\"b2b-22119091455783cf89\\",\\"appdata\\":{\\"sortType\\":\\"wangpu_score\\",\\"sellerRecommendFilter\\":false,\\"mixFilter\\":false,\\"tradenumFilter\\":false,\\"quantityBegin\\":null,\\"pageNum\\":2,\\"count\\":30}}"}',
}

response = requests.post(
    'https://h5api.m.1688.com/h5/mtop.alibaba.alisite.cbu.server.moduleasyncservice/1.0/',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)