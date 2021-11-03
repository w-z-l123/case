import unittest,requests
import ddt
from movie.dy.excle import duqu
a = duqu('3.xls')
b = a.get_data()

@ddt.ddt
class MyTestCase(unittest.TestCase):
    a = None

    def setUp(self) -> None:
        url = 'http://mobile.bwstudent.com/movieApi/tool/v1/encrypt?password=123456'
        data = {'password': '123456'}
        r = requests.get(url=url, params=data)
        # print(r.text)
        miwen = r.json()["cipherText"]
        print('-----------------')
        print(miwen)
        print('-----------------')
        url2 = 'http://mobile.bwstudent.com/movieApi/user/v2/login'
        data2 = {'email': '723749304@qq.com', 'pwd': miwen}
        r2 = requests.post(url=url2, params=data2)
        print(r2.text)
        MyTestCase.a = {'userId': str(r2.json()['result']['userId']),
                        'sessionId': str(r2.json()['result']['sessionId'])}

    @ddt.data(*b)
    @ddt.unpack
    def test01(self,movieId,page,count):  # 根据电影的id查询电影评论
        url = 'http://mobile.bwstudent.com/movieApi/movie/v2/findAllMovieComment'
        data = {'movieId':movieId,'page':page,'count':count}
        r = requests.get(url=url,params=data,headers=MyTestCase.a)
        print(r.text)

if __name__ == '__main__':
    unittest.main()
