import requests
payload = {
"startStation" : "2f940836-cedc-41ef-8e28-c2336ac8fe68", 
"endStation"   : "e6e26e66-7dc1-458f-b2f3-71ce65fdc95f" ,
"theDay"       : "2017/11/23" ,
"timeSelect"   : "18:00",
#"waySelect": "DepartureInMandarin",
 "waySelect"  : "ArrivalInMandarin",
}

res = requests.post("https://m.thsrc.com.tw/tw/TimeTable/SearchResult", data = payload)
with open('thsrc.dat', 'w', encoding="utf8") as fh :
    fh.write(res.text)
