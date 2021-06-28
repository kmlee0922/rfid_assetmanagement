import requests
import json



url_items = "http://office-api.hubilon.kr/equip/update"
#response = requests.get(url_items)
headers = {
      "accept": "application/json;charset=UTF-8",

      "userId": "admin",

      "Content-Type": "application/json;charset=UTF-8"
}

newItem =  {
      "paramList": 
        {

          "WORKID": "0006",

          "PRCID": "0035",

          "CHKSCAN": "X",

          "PDAUSER": "82047554"

        },

      "subParamList":
        {

          "PARTTYPE": "30",

          "DEVTYPE": "40",

          "EXBARCODE": "",

          "BARCODE": "5E2K9001880003131",

          "DEVICEID": "000000132",

          "SCAN": "1",

          "CHKZKOSTL": "",

          "ZPSTATU": "0080",

          "MAKTX": "LUT_DACB(DAC100)"
        }
}
    

response = requests.post(url_items, headers = headers ,data=newItem)

print(response.text)