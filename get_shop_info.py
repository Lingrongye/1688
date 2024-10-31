import requests
import re
# cookies = {
#     '_med': 'dw:1280&dh:800&pw:2560&ph:1600&ist:0',
#     'cna': '0duMH1FNeUsBASQAYABhe6MA',
#     'xlly_s': '1',
#     'cookie1': 'ACk0FVpSiiLcSC3c4aYV%2FU%2BlX1Z0cbLUfXy9BvxJLsA%3D',
#     'cookie2': '18afdf0f1d03bec50b1e7432ddbcc455',
#     'cookie17': 'UUphzpYtCw1vFYdFHA%3D%3D',
#     'sgcookie': 'E100GMKy41e1QPF5vBv9M5i%2BLl3Cfh70mZKoyw3Z4bcHsVBBivnBNDtxXUos5qloiihiFYYueW4i9gReUoVVbLgtavJVog6Zs6vXVYm6HymOrTs%3D',
#     't': 'f7aa0e7cc5610a7905d50620e4517ee9',
#     '_tb_token_': 'e67a56e7385e7',
#     'sg': '716',
#     'csg': '81b8fa2c',
#     'lid': 'tb185365847',
#     'unb': '2204157185341',
#     'uc4': 'id4=0%40U2grFbW2I5UvVXdvTtlCknlruGS2c0oV&nk4=0%40FY4PZPoOwFojuMgibAKskpunh%2FAwRQ%3D%3D',
#     '_nk_': 'tb185365847',
#     '__cn_logon__': 'true',
#     '__cn_logon_id__': 'tb185365847',
#     'ali_apache_track': 'c_mid=b2b-2204157185341d5ed1|c_lid=tb185365847|c_ms=1',
#     'ali_apache_tracktmp': 'c_w_signed=Y',
#     'last_mid': 'b2b-2204157185341d5ed1',
#     '_csrf_token': '1728441851105',
#     'taklid': '280cac183a9e4a06b0d02e66f57558c0',
#     '__mwb_logon_id__': 'tb185365847',
#     'mwb': 'ng',
#     '_m_h5_tk': '24b2d7b3f5891d48e20d4fad98460342_1728464377724',
#     '_m_h5_tk_enc': 'b0b812206053be259aa124c2f3c544db',
#     'leftMenuLastMode': 'COLLAPSE',
#     'leftMenuModeTip': 'shown',
#     '_user_vitals_session_data_': '{"user_line_track":true,"ul_session_id":"qj29r2sfxkq","last_page_id":"puchengss.1688.com%2Ft1kprv89mt"}',
#     'tfstk': 'gA1ne_61_9JC_tD6VPRQEaWFkketd2OWjghJ2QKzQh-62vECwbXl0aGpUp8r7V-GVHppTQdoqiK6vTU7RLzlvaGJU_KRZ21GmbhLAJ_rZQdzDoFYMw_pNQrxsDyMFDT2-XPJLboNRMIOjZNYMw_eojvUSSCKdO2kY3RyLplw7hT28bSyLdPwfUTrYUlUSN-6bUkrTXPZ7U8j8XSyaPbwfU8Vlv-Ca6CaAMAuelCca1YHKn7ghbllfjpe0w-ia85M-7tV8hcraHL6WEbGJkcfWB6RmEIL_Xjc8tSP3GPitd6FS_vfNDzwaLWOHpXgYbxO9OfM96rShNQMYKAOBRZpeBjhhn9UClslSHIPtdo3X3BAW6JG0lhGVLXFxFRV43kZ3HesNFzR_YMWLFTMDZh5wA1u2R4aSPDqPp868nUgSYMWLFTMDP4inb9e5e-A.',
#     'isg': 'BNzcbhRK1-mce6O2ixkw0Z88rfqOVYB_yUzlv7bdy0eqAX2L3mZJD-mzZWn5vbjX',
# }
#
# headers = {
#     'authority': 'puchengss.1688.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#     'cache-control': 'max-age=0',
#     # 'cookie': '_med=dw:1280&dh:800&pw:2560&ph:1600&ist:0; cna=0duMH1FNeUsBASQAYABhe6MA; xlly_s=1; cookie1=ACk0FVpSiiLcSC3c4aYV%2FU%2BlX1Z0cbLUfXy9BvxJLsA%3D; cookie2=18afdf0f1d03bec50b1e7432ddbcc455; cookie17=UUphzpYtCw1vFYdFHA%3D%3D; sgcookie=E100GMKy41e1QPF5vBv9M5i%2BLl3Cfh70mZKoyw3Z4bcHsVBBivnBNDtxXUos5qloiihiFYYueW4i9gReUoVVbLgtavJVog6Zs6vXVYm6HymOrTs%3D; t=f7aa0e7cc5610a7905d50620e4517ee9; _tb_token_=e67a56e7385e7; sg=716; csg=81b8fa2c; lid=tb185365847; unb=2204157185341; uc4=id4=0%40U2grFbW2I5UvVXdvTtlCknlruGS2c0oV&nk4=0%40FY4PZPoOwFojuMgibAKskpunh%2FAwRQ%3D%3D; _nk_=tb185365847; __cn_logon__=true; __cn_logon_id__=tb185365847; ali_apache_track=c_mid=b2b-2204157185341d5ed1|c_lid=tb185365847|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; last_mid=b2b-2204157185341d5ed1; _csrf_token=1728441851105; taklid=280cac183a9e4a06b0d02e66f57558c0; __mwb_logon_id__=tb185365847; mwb=ng; _m_h5_tk=24b2d7b3f5891d48e20d4fad98460342_1728464377724; _m_h5_tk_enc=b0b812206053be259aa124c2f3c544db; leftMenuLastMode=COLLAPSE; leftMenuModeTip=shown; _user_vitals_session_data_={"user_line_track":true,"ul_session_id":"qj29r2sfxkq","last_page_id":"puchengss.1688.com%2Ft1kprv89mt"}; tfstk=gA1ne_61_9JC_tD6VPRQEaWFkketd2OWjghJ2QKzQh-62vECwbXl0aGpUp8r7V-GVHppTQdoqiK6vTU7RLzlvaGJU_KRZ21GmbhLAJ_rZQdzDoFYMw_pNQrxsDyMFDT2-XPJLboNRMIOjZNYMw_eojvUSSCKdO2kY3RyLplw7hT28bSyLdPwfUTrYUlUSN-6bUkrTXPZ7U8j8XSyaPbwfU8Vlv-Ca6CaAMAuelCca1YHKn7ghbllfjpe0w-ia85M-7tV8hcraHL6WEbGJkcfWB6RmEIL_Xjc8tSP3GPitd6FS_vfNDzwaLWOHpXgYbxO9OfM96rShNQMYKAOBRZpeBjhhn9UClslSHIPtdo3X3BAW6JG0lhGVLXFxFRV43kZ3HesNFzR_YMWLFTMDZh5wA1u2R4aSPDqPp868nUgSYMWLFTMDP4inb9e5e-A.; isg=BNzcbhRK1-mce6O2ixkw0Z88rfqOVYB_yUzlv7bdy0eqAX2L3mZJD-mzZWn5vbjX',
#     'referer': 'https://puchengss.1688.com/page/index.html?spm=a261y.7663282.wp_pc_common_header_companyName_undefined.0',
#     'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
# }
#
# params = {
#     'spm': 'a2615.12330364.wp_pc_common_topnav.0',
# }


