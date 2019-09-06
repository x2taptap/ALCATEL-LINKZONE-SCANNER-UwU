import requests
import json
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'http://mw70.home/index.html',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    '_TclRequestVerificationKey': 'KSDHSDFOGQ5WERYTUIQWERTYUISDFG1HJZXCVCXBN2GDSMNDHKVKFsVBNf',
}
CRED    = '\33[31m'
CBLUE = '\33[34m'
CITALIC = '\33[3m'
ENDC = '\033[0m'


datainfo = '{"id":"12","jsonrpc":"2.0","method":"GetSystemInfo","params":{}}'
datastatus = '{"id":"12","jsonrpc":"2.0","method":"GetSystemStatus","params":{}}'
datasim = '{"id":"12","jsonrpc":"2.0","method":"GetSimStatus","params":{}}'

rinfo = requests.post('http://mw70.home/jrd/webapi', headers=headers, data=datainfo, verify=False)
rstatus = requests.post('http://mw70.home/jrd/webapi', headers=headers, data=datastatus, verify=False)
rsim = requests.post('http://mw70.home/jrd/webapi', headers=headers, data=datasim, verify=False)


jinfo = json.loads(rinfo.text)
jstatus = json.loads(rstatus.text)
jsim = json.loads(rsim.text)

print("\n" + CITALIC + CRED + "LINKZONE SCAN 0w0" + ENDC + "\n")
print("=============================================================")
print("5G SSID: " + jstatus['result']['Ssid_5g'].replace("\n",""))
print("2G SSID: " + jstatus['result']['Ssid_2g'].replace("\n",""))
print("Signal Strength: " + str(jstatus['result']['SignalStrength']).replace("\n",""))
print("Battery Level: " + str(jstatus['result']['BatteryLevel']).replace("\n","") + "%")
print("Network Name: " + jstatus['result']['NetworkName'].replace("\n",""))
print("Device Name : " + jinfo['result']['DeviceName'].replace("\n",""))
print("Software Version: " + jinfo['result']['SwVersion'].replace("\n",""))
print("Hardware Version: " + jinfo['result']['HwVersion'].replace("\n",""))
print("WebUI Version: " + jinfo['result']['WebUiVersion'].replace("\n",""))
print("IMEI: " + jinfo['result']['IMEI'].replace("\n",""))
print("IMSI: " + jinfo['result']['IMSI'].replace("\n",""))
print("ICCID: " + jinfo['result']['ICCID'].replace("\n",""))
print("PLMN: " + jsim['result']['PLMN'].replace("\n",""))
print("Mac Address 5G: " + jinfo['result']['MacAddress5G'].replace("\n",""))
print("Mac Address 2.4G: " + jinfo['result']['MacAddress'].replace("\n",""))
print("=============================================================")
print("\n" + CITALIC + CBLUE + "Author: kasjan321 aka x2taptap" + ENDC)