import requests
import json



def searchBarcode(equipId) : 

  url_items = "http://office-api.hubilon.kr/equip/" + equipId
  #response = requests.get(url_items)
  headers = {
    "accept": "application/json;charset=UTF-8",
    "userId": "admin"
  }

  response = requests.get(url_items, headers=headers)
  data = response.json()
  if data['data'] is None:
    return_data = 0
    return return_data
  else:
    return data


# def searchBarcode(equipId) : 

#   url_items = "http://office-api.hubilon.kr/equip/" + equipId
#   #response = requests.get(url_items)
#   headers = {
#     "accept": "application/json;charset=UTF-8",
#     "userId": "admin"
#   }

#   response = requests.get(url_items, headers=headers)
#   data = response.json()
#   if data['data'] is None:
#     return_data = 0
#     return return_data
#   elif data['workId'] == "0007" :
#     return_data = {

#         "message": {

#           "header": {

#             "userId": "10148002",

#             "userPasswd": "",

#             "userName": "강현수",

#             "telNo": "01073001435",

#             "userCellPhoneNo": "01073001435",

#             "orgId": "C361443",

#             "orgName": "융합기술BDO",

#             "orgTypeCode": "INS_USER",

#             "job_equnr": "",

#             "currentPageNo": "",

#             "currentPageCount": "",

#             "pageUseYN": "",

#             "sessionId": "4C5nnrmjsVKsbZWSjkk8Dsfi.nbase01",

#             "orgCode": "361443"

#           },

#           "body": {

#             "param": {

            

#             },

#             "paramList": [

#               {

#                 "WORKID": "0006",

#                 "PRCID": "0035",

#                 "CHKSCAN": "X",

#                 "PDAUSER": "10148002"

#               }

#             ],

#             "subParamList": [

#               {

#                 "PARTTYPE": "30",

#                 "DEVTYPE": "40",

#                 "EXBARCODE": "",

#                 "BARCODE": equipId,

#                 "DEVICEID": data['data']['deviceId'],

#                 "SCAN": "1",

#                 "CHKZKOSTL": "",

#                 "ZPSTATU": "0080",

#                 "MAKTX": "LUT_DACB(DAC100)"

#               }

#             ]

#           },

#           "call": "ANDROID",

#           "jobSeq": 1,

#           "operatorId": "",

#           "runProgramId": "",

#           "sysRegisterDate": {

          

#           },

#           "sysUpdateDate": {

          

#           }

#         }

#       }
#     return return_data
#   else :
#     return_data = {

#       "message": {

#         "header": {

#           "userId": "10148002",

#           "userPasswd": "",

#           "userName": "강현수",

#           "telNo": "01073001435",

#           "userCellPhoneNo": "01073001435",

#           "orgId": "C361443",

#           "orgName": "양평고객기술팀",

#           "orgTypeCode": "INS_USER",

#           "job_equnr": "",

#           "currentPageNo": "",

#           "currentPageCount": "",

#           "pageUseYN": "",

#           "sessionId": "4C5nnrmjsVKsbZWSjkk8Dsfi.nbase01",

#           "orgCode": "361443"

#         },

#         "body": {

#           "param": {

          

#           },

#           "paramList": [

#             {

#               "WORKID": "0007",

#               "PRCID": "0270",

#               "ZDOCRT": "X",

#               "DEVICEID": "",

#               "UBARCODE": "5E2K9001809002112",

#               "CHKSTORT": "",

#               "CHKSCAN": "X",

#               "ZEQUIPLP": "B00000071710019012160",

#               "PDAUSER": "10148002"

#             }

#           ],

#           "subParamList": [

#             {

#               "PARTTYPE": "30",

#               "DEVTYPE": "40",

#               "BARCODE": equipId,

#               "CHKZKOSTL": "",

#               "DEVICEID": "000720276",

#               "EXBARCODE": "",

#               "KOSTL": "C363198",

#               "SCAN": "1",

#               "ZPSTATU": "0060",

#               "MAKTX": "LOC_U9024A-OLT-SCU-P1"

#             }

#           ]

#         },

#         "call": "ANDROID",

#         "jobSeq": 1,

#         "operatorId": "",

#         "runProgramId": "",

#         "sysRegisterDate": {

        

#         },

#         "sysUpdateDate": {

        

#         }

#       }

#     }
#     return return_data






