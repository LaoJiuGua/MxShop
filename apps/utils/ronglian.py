from ronglian_sms_sdk import SmsSDK
import json

accId = '8a216da8747ac982017495d377c72059'
accToken = '69ac60da9fff49d6a887ca149ebb53b3'
appId = '8aaf070877807ed80177af4ef4030574'


def send_message(mobile,code):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = mobile
    datas = (code, '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    resp = json.loads(resp)
    return resp
