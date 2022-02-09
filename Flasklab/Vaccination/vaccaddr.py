import requests
import json

class VaccAddress:
    def VaccAddrProccess(self):
        keyValue = r"j8b0Mnuz7av0XrUSk4VM9HSQ7UpBFVu%2F0ZpDOwjCMyrOcKc4hjTvlQcmeaYlI9paTOk%2Bb%2FxVQs7omZ0zJNQPcQ%3D%3D"   

        dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
        dataURL += "page=" + str(1) + "&perPage=" + str(10)
        dataURL += "&cond%5BorgZipaddr%3A%3ALIKE%5D=" + "오산시" 
        dataURL += "&serviceKey=" + keyValue
    
        dataResult = requests.get(dataURL)
        exchangeData = dataResult.text

        dataResult3 = json.loads(exchangeData)

        return dataResult3