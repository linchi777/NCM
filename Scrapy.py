import json
import random
import requests
import time
import csv
import codecs


def start_spider(song_id):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_{}?csrf_token='.format(song_id)
#请求头
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.53',
        'authority': 'http://music.163.com'
    }

    response = requests.get(url, headers=headers)
    print('请求 [ ' + url + ' ], 状态码为 ')
    print(response.status_code)
    # get_hot_comments(response.text)
    # 将数据写到 CSV 文件中
    write_to_file(get_hot_comments(response.text))


def get_hot_comments(response):
    data_list = []
    data = {}

    for comment in json.loads(response)['hotComments']:
        data['userId'] = comment['user']['userId']
        data['nickname'] = comment['user']['nickname']
        data['content'] = comment['content']
        data['likedCount'] = comment['likedCount']
        data['time'] = comment['time']
        data_list.append(data)
        data = {}
    # print(data_list)
    return data_list


def write_to_file(datalist):
    print('开始写入')
    file_name = 'ncmhotcomments(mac).csv'

    with codecs.open(file_name, 'a+', 'GBK') as csvfile:
        filednames = ['用户Id', '昵称', '评论内容', '点赞数', '评论长度']
        writer = csv.DictWriter(csvfile, fieldnames=filednames)

        writer.writeheader()
        for data in datalist:
            print(data)
            try:
                writer.writerow({filednames[0]: data['userId'],
                                 filednames[1]: data['nickname'],
                                 filednames[2]: data['content'],
                                 filednames[3]: data['likedCount'],
                                 filednames[4]: data['time']})
            except UnicodeEncodeError:
                print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

    print('成功将数据写入到 ' + file_name + ' 中！')


def get_song_id(url):
    """ 从 url 中截取歌曲的 id """
    song_id = url.split('=')[1]
    return song_id


def main():
    songs_url_list = [
        'https://music.163..com/song?id=1436709403',
        'https://music.163..com/song?id=1446251500',
        'https://music.163..com/song?id=1413585838',
        'https://music.163..com/song?id=493735012',
        'https://music.163..com/song?id=1387581250',
        'https://music.163..com/song?id=1442508316',
        'https://music.163..com/song?id=1433434738',
        'https://music.163..com/song?id=1436910205',
        'https://music.163..com/song?id=465921195',
        'https://music.163..com/song?id=1344897943',
        'https://music.163..com/song?id=1398663411',
        'https://music.163..com/song?id=1403215687',
        'https://music.163..com/song?id=1363948882',
        'https://music.163..com/song?id=1444961777',
        'https://music.163..com/song?id=403710393',
        'https://music.163..com/song?id=1400256289',
        'https://music.163..com/song?id=1413142894',
        'https://music.163..com/song?id=1330348068',
        'https://music.163..com/song?id=1374329431',
        'https://music.163..com/song?id=1407551413',
        'https://music.163..com/song?id=1346104327',
        'https://music.163..com/song?id=298213',
        'https://music.163..com/song?id=1331819951',
        'https://music.163..com/song?id=1406642934',
        'https://music.163..com/song?id=1423241987',
        'https://music.163..com/song?id=1365898499',
        'https://music.163..com/song?id=1384026889',
        'https://music.163..com/song?id=1359356908',
        'https://music.163..com/song?id=1376873330',
        'https://music.163..com/song?id=208902',
        'https://music.163..com/song?id=545350938',
        'https://music.163..com/song?id=1365393542',
        'https://music.163..com/song?id=1438865533',
        'https://music.163..com/song?id=1386460251',
        'https://music.163..com/song?id=1383927243',
        'https://music.163..com/song?id=1389090775',
        'https://music.163..com/song?id=1363205817',
        'https://music.163..com/song?id=1407358755',
        'https://music.163..com/song?id=1411358329',
        'https://music.163..com/song?id=1426649237',
        'https://music.163..com/song?id=1382596189',
        'https://music.163..com/song?id=29004400',
        'https://music.163..com/song?id=31010566',
        'https://music.163..com/song?id=1440443944',
        'https://music.163..com/song?id=569214250',
        'https://music.163..com/song?id=1336856777',
        'https://music.163..com/song?id=1297498908',
        'https://music.163..com/song?id=32835565',
        'https://music.163..com/song?id=569213220',
        'https://music.163..com/song?id=316686',
        'https://music.163..com/song?id=1425814935',
        'https://music.163..com/song?id=441491828',
        'https://music.163..com/song?id=1443928242',
        'https://music.163..com/song?id=1386259535',
        'https://music.163..com/song?id=1422212205',
        'https://music.163..com/song?id=1358848433',
        'https://music.163..com/song?id=1399112638',
        'https://music.163..com/song?id=496370620',
        'https://music.163..com/song?id=1426112587',
        'https://music.163..com/song?id=1405283464',
        'https://music.163..com/song?id=460578140',
        'https://music.163..com/song?id=483937795',
        'https://music.163..com/song?id=1313354324',
        'https://music.163..com/song?id=1383876635',
        'https://music.163..com/song?id=1381755293',
        'https://music.163..com/song?id=1352968308',
        'https://music.163..com/song?id=1357999894',
        'https://music.163..com/song?id=550138197',
        'https://music.163..com/song?id=35678875',
        'https://music.163..com/song?id=1391891631',
        'https://music.163..com/song?id=1293886117',
        'https://music.163..com/song?id=1412559986',
        'https://music.163..com/song?id=1385856956',
        'https://music.163..com/song?id=1336856449',
        'https://music.163..com/song?id=1372060183',
        'https://music.163..com/song?id=1412242872',
        'https://music.163..com/song?id=1334295185',
        'https://music.163..com/song?id=511391907',
        'https://music.163..com/song?id=569200213',
        'https://music.163..com/song?id=1373168742',
        'https://music.163..com/song?id=574566207',
        'https://music.163..com/song?id=554241732',
        'https://music.163..com/song?id=1415829224',
        'https://music.163..com/song?id=528326686',
        'https://music.163..com/song?id=1297802566',
        'https://music.163..com/song?id=1369798757',
        'https://music.163..com/song?id=1434062381',
        'https://music.163..com/song?id=1446235247',
        'https://music.163..com/song?id=1355147933',
        'https://music.163..com/song?id=1336856864',
        'https://music.163..com/song?id=1409329655',
        'https://music.163..com/song?id=1356350562',
        'https://music.163..com/song?id=430114655',
        'https://music.163..com/song?id=515453363',
        'https://music.163..com/song?id=28018075',
        'https://music.163..com/song?id=513360721',
        'https://music.163..com/song?id=1364343491',
        'https://music.163..com/song?id=536622304',
        'https://music.163..com/song?id=157276',
        'https://music.163..com/song?id=1440968432',
        'https://music.163..com/song?id=1303289043',
        'https://music.163..com/song?id=1335350269',
        'https://music.163..com/song?id=1442312981',
        'https://music.163..com/song?id=1377748865',
        'https://music.163..com/song?id=1343756008',
        'https://music.163..com/song?id=1349292048',
        'https://music.163..com/song?id=1297742167',
        'https://music.163..com/song?id=526116053',
        'https://music.163..com/song?id=1443592120',
        'https://music.163..com/song?id=1404906595',
        'https://music.163..com/song?id=405599470',
        'https://music.163..com/song?id=461347998',
        'https://music.163..com/song?id=1365221826',
        'https://music.163..com/song?id=1444738318',
        'https://music.163..com/song?id=480580003',
        'https://music.163..com/song?id=1355896807',
        'https://music.163..com/song?id=1397345903',
        'https://music.163..com/song?id=340383',
        'https://music.163..com/song?id=413812448',
        'https://music.163..com/song?id=1404511131',
        'https://music.163..com/song?id=449818741',
        'https://music.163..com/song?id=36270426',
        'https://music.163..com/song?id=516323185',
        'https://music.163..com/song?id=1412672813',
        'https://music.163..com/song?id=536096151',
        'https://music.163..com/song?id=514761281',
        'https://music.163..com/song?id=1439142552',
        'https://music.163..com/song?id=476659144',
        'https://music.163..com/song?id=1427444926',
        'https://music.163..com/song?id=515269424',
        'https://music.163..com/song?id=536099160',
        'https://music.163..com/song?id=1445761206',
        'https://music.163..com/song?id=26060065',
        'https://music.163..com/song?id=108390',
        'https://music.163..com/song?id=108463',
        'https://music.163..com/song?id=412911436',
        'https://music.163..com/song?id=86369',
        'https://music.163..com/song?id=417859631',
        'https://music.163..com/song?id=1404885266',
        'https://music.163..com/song?id=1376142151',
        'https://music.163..com/song?id=411214279',
        'https://music.163..com/song?id=1382666583',
        'https://music.163..com/song?id=25713022',
        'https://music.163..com/song?id=406475394',
        'https://music.163..com/song?id=1430287528',
        'https://music.163..com/song?id=174944',
        'https://music.163..com/song?id=406072775',
        'https://music.163..com/song?id=31445772',
        'https://music.163..com/song?id=1397021895',
        'https://music.163..com/song?id=1334363758',
        'https://music.163..com/song?id=31789010',
        'https://music.163..com/song?id=254574',
        'https://music.163..com/song?id=442314990',
        'https://music.163..com/song?id=29009655',
        'https://music.163..com/song?id=473817398',
        'https://music.163..com/song?id=418602088',
        'https://music.163..com/song?id=423228325',
        'https://music.163..com/song?id=191254',
        'https://music.163..com/song?id=483671599',
        'https://music.163..com/song?id=1387592437',
        'https://music.163..com/song?id=1411784809',
        'https://music.163..com/song?id=451703096',
        'https://music.163..com/song?id=1338695683',
        'https://music.163..com/song?id=1422303419',
        'https://music.163..com/song?id=558290126',
        'https://music.163..com/song?id=1444140174',
        'https://music.163..com/song?id=1315718569',
        'https://music.163..com/song?id=1363078221',
        'https://music.163..com/song?id=421423806',
        'https://music.163..com/song?id=287035',
        'https://music.163..com/song?id=1416772486',
        'https://music.163..com/song?id=1367452194',
        'https://music.163..com/song?id=452986458',
        'https://music.163..com/song?id=1308818967',
        'https://music.163..com/song?id=474739467',
        'https://music.163..com/song?id=1446233390',
        'https://music.163..com/song?id=175072',
        'https://music.163..com/song?id=1296833312',
        'https://music.163..com/song?id=1388357890',
        'https://music.163..com/song?id=1439333714',
        'https://music.163..com/song?id=1377078201',
        'https://music.163..com/song?id=1443143188',
        'https://music.163..com/song?id=1357825630',
        'https://music.163..com/song?id=1362247767',
        'https://music.163..com/song?id=1367609755',
        'https://music.163..com/song?id=1382985712',
        'https://music.163..com/song?id=1374154676',
        'https://music.163..com/song?id=1432156509',
        'https://music.163..com/song?id=40147554',
        'https://music.163..com/song?id=1357785909',
        'https://music.163..com/song?id=1408941731',
        'https://music.163..com/song?id=133998',
        'https://music.163..com/song?id=347230',
        'https://music.163..com/song?id=1375935067',
        'https://music.163..com/song?id=512359195',
        'https://music.163..com/song?id=415792881',
        'https://music.163..com/song?id=456185577',
        'https://music.163..com/song?id=1382423403',
        'https://music.163..com/song?id=480426313',
        'https://music.163..com/song?id=421423808',
    ]

    for each in songs_url_list:
        start_spider(get_song_id(each))
        time.sleep(random.randint(3, 5))


if __name__ == '__main__':
    main()

