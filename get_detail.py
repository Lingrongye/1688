import requests
import re
import json
import pandas as pd
from itertools import zip_longest
cookies = {
    'cna': '0duMH1FNeUsBASQAYABhe6MA',
    '_m_h5_tk': 'db902cc5bc1e3a602ad7d0daabba179f_1730227329189',
    '_m_h5_tk_enc': '69cecd007e5c26d6aeadd7fcbdad1308',
}
headers = {
    # 'cookie': 'cna=0duMH1FNeUsBASQAYABhe6MA; _m_h5_tk=b0694277bcbefe0a9b0ccb97cb6b604a_1728449729702; _m_h5_tk_enc=0e29dc867f0d7b01085c09daa0ea5350; xlly_s=1; cookie1=ACk0FVpSiiLcSC3c4aYV%2FU%2BlX1Z0cbLUfXy9BvxJLsA%3D; cookie2=18afdf0f1d03bec50b1e7432ddbcc455; cookie17=UUphzpYtCw1vFYdFHA%3D%3D; sgcookie=E100GMKy41e1QPF5vBv9M5i%2BLl3Cfh70mZKoyw3Z4bcHsVBBivnBNDtxXUos5qloiihiFYYueW4i9gReUoVVbLgtavJVog6Zs6vXVYm6HymOrTs%3D; t=f7aa0e7cc5610a7905d50620e4517ee9; _tb_token_=e67a56e7385e7; sg=716; csg=81b8fa2c; lid=tb185365847; unb=2204157185341; uc4=id4=0%40U2grFbW2I5UvVXdvTtlCknlruGS2c0oV&nk4=0%40FY4PZPoOwFojuMgibAKskpunh%2FAwRQ%3D%3D; _nk_=tb185365847; __cn_logon__=true; __cn_logon_id__=tb185365847; ali_apache_track=c_mid=b2b-2204157185341d5ed1|c_lid=tb185365847|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; last_mid=b2b-2204157185341d5ed1; _csrf_token=1728441851105; taklid=280cac183a9e4a06b0d02e66f57558c0; _user_vitals_session_data_={"user_line_track":true,"ul_session_id":"5wbkkamqcj4","last_page_id":"detail.1688.com%2Fhfts9yl4xvf"}; JSESSIONID=90244746DB7F2A5499B0328A261825A5; isg=BK6u9XciRZxaf7F45TPix1nm_wRwr3KpT8ZXcdh2DrFHu0wVQD49ubaocCdXW2rB; tfstk=gadIEt6opkqCKQeeHb3Nh6u1YbCS73GVyz_JoUFUy6CdNbT5bwe8w7p1VhK1v2fPah1OlwERpB-yVTtyXMIrKBPWfULAYakHT796xEBFaQTuNaLJq2jr-A8H-_f-0m5SgeYh7eFxWc5-yFClr3j3Cj8H-PC-0mlqguN3fAdR23BpWPQ5XgC8w3IOBZQ4v_CJ2VsOoZP82_FLBGQlXgCRw3L9u5E1SvswRVmiZduULiTdf7FJ1bXCceezw7d1R9TpJG9BdC_CdiBGvGuD9h8JTBXitW5k7KtWehh_O3TpH3Ie6mF54KbWyZ1xirs9OUO1KdlYfNv98LdHAzNR-BRVFiXsy7XP6IWvHHaooFCdy3XDamVhvULDiK5jN5CCeglTgiGGj8a1n7Q10Vg_E82oTCeEJVkg19QG7sus5-ylpNb10Vg_E8XdSN2q5Vw4E',
    'referer': 'https://www.1688.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.69',
}

def get_detail(url,file_path,tag):
    response = requests.get(url,cookies=cookies, headers=headers)
    match = re.search(r'window\.__INIT_DATA\s*=\s*{(.*?),"seed"', response.text, re.DOTALL)
    tags= tag
    if match:
        try:
            data ="{" + match.group(1) + "}"
            data = json.loads(data)
            src_img = data['data']['1081181309881']['data']['offerImgList']
            item_title = data['data']['1081181309881']['data']['subject']
            # 额外的字段
            handler = item_title
            vendor = "WF"
            title = item_title
            # tags = tag
            status = 'draft'
            variant_fulfillment_service = 'manual'
            variant_inventory_policy = 'deny'

            sku_info = data['globalData']['skuModel']['skuProps']
            image_map = {}
            all_options = []
            for sku in sku_info:
                all_options.append(sku['prop'])
                value = sku['value']
                for v in value:
                    if len(v.get('imageUrl',''))!=0:
                        image_map[v['name']] = v['imageUrl']

            if len(all_options)>3:
                print("属性超过3个，无法处理")
                exit()
            detail_sku = data['globalData']['skuModel']['skuInfoMapOriginal']
            sku_list = []
            for key,value in detail_sku.items():
                # 拆分
                options = key.split('&gt;')
                options += [None] * (3 - len(options))
                sku_data = {}
                sku_data['option1'] = options[0]
                sku_data['option2'] = options[1]
                sku_data['option3'] = options[2]

                # 查找 image_map 中第一个匹配的值
                for option in options:
                    if option in image_map:
                        sku_data['img'] = image_map[option]
                        break
                else:
                    # 如果没有找到匹配项，则设置为空字符串
                    sku_data['img'] = None
                sku_data['price'] = value.get('price','')
                if sku_data['price'] == '':
                    sku_data['price'] = value['discountPrice']
                sku_list.append(sku_data)
            df_skus = pd.DataFrame(sku_list)
            # 转换为列表的元组形式

            result = list(df_skus.apply(lambda row: (
                row['option1'], row['option2'], row['option3'],
                row['img'], row['price']
            ), axis=1))

            src_position = [i for i in range(1,len(src_img)+1)]

            param_info = data['data']['1081181309201']['data']
            text_info = ''
            for item in param_info:
                text_info += item['name'] + ':' + item['value'] + '  '

            if len(handler) == 0 or len(title) == 0 or len(src_img) == 0:
                exit()

            image_alt_text = "<p>" + text_info + "</p>"
            # # 使用 zip_longest 处理不等长的 image_src 和 image_position
            image_src_filled = list(zip_longest(src_img, [], fillvalue=None))
            image_position_filled = list(zip_longest(src_position, [], fillvalue=None))
            # 构造 DataFrame 数据
            data = []
            for idx, combination in enumerate(result):
                row = []

                # 只在第一行添加 option_name 和其他附加字段
                if idx == 0:
                    row.extend([title, tags, status, image_alt_text, 'True'])  # 添加 Handle, Title, Variant Inventory Policy
                    row.append('Color')
                    row.append(result[idx][0])
                    row.append(all_options[1] if len(all_options) > 1 else None)
                    row.append(result[idx][1])
                    row.append(all_options[2] if len(all_options) > 2 else None)
                    row.append(result[idx][2])
                    row.append(result[idx][3])
                else:
                    # 从第二行开始，只添加 option_value 和 None 占位符
                    row.extend([None, None, None, None, None])
                    row.append(None)
                    row.append(result[idx][0])
                    row.append(None)
                    row.append(result[idx][1])
                    row.append(None)
                    row.append(result[idx][2])
                    # 添加图片链接（如果存在）
                    row.append(result[idx][3])

                # 添加 image_src 和 image_position
                row.append(image_src_filled[idx][0] if idx < len(image_src_filled) else None)
                row.append(image_position_filled[idx][0] if idx < len(image_position_filled) else None)
                row.append(handler)
                row.append(variant_fulfillment_service)
                row.append(variant_inventory_policy)

                row.append(result[idx][4])
                row.append(vendor)

                data.append(row)

            # 定义 DataFrame 的列名
            columns = ['Title', 'Tags', 'Status', 'Body (HTML)', "Published", 'Option1 Name', 'Option1 Value', 'Option2 Name',
                       'Option2 Value', 'Option3 Name',
                       'Option3 Value', 'Variant Image', 'Image Src', 'Image Position', 'Handle', 'Variant Fulfillment Service',
                       'Variant Inventory Policy', "Variant Price", "Vendor"]

            # 创建 DataFrame
            new_df = pd.DataFrame(data, columns=columns)
            if new_df['Variant Image'].isnull().all():
                if len(src_img) > 0:
                    new_df['Variant Image'] = src_img[0]
                else:
                    new_df['Variant Image'] = None
            df = pd.read_csv(file_path, encoding='utf-8-sig')
            df = pd.concat([df, new_df], ignore_index=True)
            # 保存到文件
            df.to_csv(file_path, index=False, encoding='utf-8-sig')

        except Exception as e:
            print("爬取失败")
            print(e)
            print(response.text)
            return

    else:
        print("爬取失败"+ url)

        print(response.text)
        return


if __name__ == '__main__':
    get_detail('https://detail.1688.com/offer/837549705223.html?_t=1730343887497&spm=a2615.7691456.co_0_0_wangpu_score_0_0_0_0_0_0_0000_0.0', 'test.csv', 'test')