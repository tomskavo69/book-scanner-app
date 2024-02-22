def main():
    lang_name = input('职位名：')
    page = 1
    url = 'http://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    info_result = []
    while page < 31:
        info = get_json(url, page, lang_name)
        info_result = info_result + info
        page += 1
    wb = Workbook()
    ws1 = wb.active
    ws1.title = lang_name
    for row in info_result:
        ws1.append(row)
    wb.save('职位信息.xlsx')

if __name__ == '__main__':
    main()
