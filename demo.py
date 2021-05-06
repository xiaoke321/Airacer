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
        # TODO url：获取飞机元数据
        self.url_3 = "https://aircharterguide-api.tuvoli.com/api/v1/aircharterguide/aircraft-photos"

        # TODO url：获取飞机机票数据
        self.url_4 = "https://aircharterguide-api.tuvoli.com/api/v1/operator/aircraft-fleet"


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
            return (data["data"], airport_code)
        return []

    def get(self):
        airport_code = input("请输入机场代码（[这里面的字符] 例如：KLVK）：")
        result, airport_code = self.airport_data(airport_code=airport_code)
        if not result:
            return False
        print("找到%s种结果，符合:" %str(len(result)))
        for i in result:
            if i["AirportCode"] != airport_code:
                continue
            # print(json.dumps(i))
            params = {
                "aircraftId": i["AircraftID"]
            }
            response = self.session.get(url=self.url_3, params=params)
            data = response.json()
            print(json.dumps({
                "ShortDesc": i.get("ShortDesc"),                # 描述
                "AircraftID": i.get("AircraftID"),                   # 飞机ID
                "CompanyID": i.get("CompanyID"),
                "LocationID": i.get("LocationID"),
                "AirportCode": i.get("AirportCode"),             # 机场代码
                "CategoryName": i.get("CategoryName"),           # 类别名称
                "ManufacturerName": i.get("ManufacturerName"),   # 制造商
                "TypeName": i.get("TypeName"),                   # 类型名称
                "TypeCode": i.get("TypeCode"),                   # 类型代码
                "Tailnumber": i.get("Tailnumber"),               # 尾号
                "Seats": i.get("Seats"),                         # 座位
                "Year": i.get("Year"),
                "IsAmbulance": i.get("IsAmbulance"),             # is救护车
                "IsCargo": i.get("IsCargo"),                     # is货物
                "RegionName": i.get("RegionName"),               # 地区
                "CountryName": i.get("CountryName"),             # 国家
                "CountryCode": i.get("CountryCode"),             # 国家代码
                "StateName": i.get("StateName"),                 # 州（名）
                "StateCode": i.get("StateCode"),                 # 州（代码）
                "San Francisco": i.get("San Francisco"),
                "City": i.get("City"),
                "CurrencyCode": i.get("CurrencyCode"),           # 货币
                "CurrencyID": i.get("CurrencyID"),               # 货币id
                "BookRateMax": i.get("BookRateMax"),             # 账面价值最大值
                "BookRateMin": i.get("BookRateMax"),             # 账面价值最小值
                "BookAvgRate": i.get("BookAvgRate"),
                "AdRank": i.get("AdRank"),                       # 广告排名
                "AdType": i.get("AdType"),                       # 广告类型
                "AirplaneManagerAircraftID": i.get("AirplaneManagerAircraftID"),
                "Distance": i.get("Distance"),                   # 距离
                "IsEnhanced": i.get("IsEnhanced"),               # 增强
                "IsAdvertiser": i.get("IsAdvertiser"),           # is广告商
                "navigationUrl": i.get("navigationUrl"),
                "locationStr": i.get("locationStr"),             # 位置
                "aircraftType": i.get("aircraftType"),           # 飞机型号
                "priceRange": i.get("priceRange"),               # 价格范围
                "logoPath": i.get("logoPath"),
                "seatsInfo": i.get("seatsInfo"),                 # 座位信息
                "imagesShow": data,
            }))
            # input("回车继续下一条：")


            # params = {
            #     "companyId": i["CompanyID"],
            #     "locationId": i["LocationID"],
            #     "dataType": "8",
            #     "city": i["City"],
            #     # "city": "all",
            # }
            # response = self.session.get(url=self.url_4, params=params)
            # data = response.json()["data"]
            # # print(data)
            # if not data:
            #     print("数据空")
            # for i in data:
            #     print(json.dumps(i))
            # input("回车继续下一条：")



if __name__ == '__main__':
    demo = Demo()
    demo.get()
