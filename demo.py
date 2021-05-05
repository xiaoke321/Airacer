import requests
from fake_useragent import UserAgent
import json

class Demo():

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
            'User-Agent': str(UserAgent().random),
        })
        # TODO url：获取出发地机场代码
        self.url_1 = "https://aircharterguide-api.tuvoli.com/api/v1/airport/all"
        # TODO url：获取机场数据
        self.url_2 = "https://aircharterguide-api.tuvoli.com/api/v1/aircharterguide/aircrafts-search"
        # TODO url：获取飞机机票数据
        self.url_3 = "https://aircharterguide-api.tuvoli.com/api/v1/operator/aircraft-fleet"


        # TODO 获取--出发地--机场代码
        _from = input("请输入出发地（模糊匹配 例如：china）：")
        response = self.session.get(url=self.url_1, params={"searchText": _from})
        data = response.json()["data"]
        for i in data:
            print(i)

    def airport_data(self, airport_code="KLVK"):
        params = {
            "Radius": "50",   # TODO 距离，默认=50
            "AirportCode": airport_code,
            "MinSeats": "1",  # TODO 座位，默认=1
        }
        response = self.session.get(url=self.url_2, params=params)
        data = response.json()
        if data.get("data"):
            return data["data"]
        return []

    def get(self):
        airport_code = input("请输入机场代码（[这里面的字符]）：")
        result = self.airport_data(airport_code=airport_code)
        if not result:
            return False
        for i in result:
            params = {
                "companyId": i["CompanyID"],
                "locationId": i["LocationID"],
                "dataType": "8",
                "city": i["City"],
                # "city": "all",
            }
            # print(params)
            response = self.session.get(url=self.url_3, params=params)
            data = response.json()["data"]
            # print(data)
            if not data:
                print("数据空")
            for i in data:
                print(json.dumps(i))
            input("回车继续下一条：")

if __name__ == '__main__':
    demo = Demo()
    demo.get()
