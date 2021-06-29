import requests
import json



url_items = "http://office-api.hubilon.kr/equip/update"
#response = requests.get(url_items)
headers = {
  "accept": "application/json;charset=UTF-8",
  "userId": "admin",
  "Content-Type": "application/json;charset=UTF-8"
}

newItem = {

  "message": {

    "header": {

      "userId": "82047554",

      "userPasswd": "",

      "userName": "LDAP테스트4",

      "telNo": "01074451945",

      "userCellPhoneNo": "01074451945",

      "orgId": "C361443",

      "orgName": "양평고객기술팀",

      "orgTypeCode": "INS_USER",

      "job_equnr": "",

      "currentPageNo": "",

      "currentPageCount": "",

      "pageUseYN": "",

      "sessionId": "4C5nnrmjsVKsbZWSjkk8Dsfi.nbase01",

      "orgCode": "361443"

    },

    "body": {

      "param": {

       

      },

      "paramList": [

        {

          "WORKID": "0006",

          "PRCID": "0035",

          "CHKSCAN": "X",

          "PDAUSER": "82047554"

        }

      ],

      "subParamList": [

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

      ]

    },

    "call": "ANDROID",

    "jobSeq": "1",

    "operatorId": "",

    "runProgramId": "",

    "sysRegisterDate": {

     

    },

    "sysUpdateDate": {

     

    }

  }

}


newItem2 = {

  "message": {

    "header": {

      "userId": "82047554",

      "userPasswd": "",

      "userName": "LDAP테스트4",

      "telNo": "01074451945",

      "userCellPhoneNo": "01074451945",

      "orgId": "C361443",

      "orgName": "양평고객기술팀",

      "orgTypeCode": "INS_USER",

      "job_equnr": "",

      "currentPageNo": "",

      "currentPageCount": "",

      "pageUseYN": "",

      "sessionId": "4C5nnrmjsVKsbZWSjkk8Dsfi.nbase01",

      "orgCode": "361443"

    },

    "body": {

      "param": {

       

      },

      "paramList": [

        {

          "WORKID": "0006",

          "PRCID": "0035",

          "CHKSCAN": "X",

          "PDAUSER": "82047554"

        }

      ],

      "subParamList": [

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

      ]

    },

    "call": "ANDROID",

    "jobSeq": "1",

    "operatorId": "",

    "runProgramId": "",

    "sysRegisterDate": {

     

    },

    "sysUpdateDate": {

     

    }

  }

}

def out(equip_barcode):
  newItem2['message']['body']['subParamList'][0]['BARCODE']=equip_barcode
  response = requests.post(url_items, headers = headers ,data=json.dumps(newItem2))


out("123456")
# print(newItem)

# response = requests.post(url_items, headers = headers ,data=json.dumps(newItem))

# print(response.text)