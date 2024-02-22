def get_json(url, page, lang_name):
    data = {'first': 'true', 'pn': page, 'kd': lang_name}
    json = requests.post(url, data).json()
    list_con = json['content']['positionResult']['result']
    info_list = []
    for i in list_con:
        info = []
        info.append(i['companyShortName'])
        info.append(i['companyName'])
        info.append(i['salary'])
        info.append(i['city'])
        info.append(i['education'])
        info_list.append(info)
    return info_list
