import requests
import datetime
import time
headers = {
      'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
district_id=[294,276,265]

now_=datetime.datetime.now()
day_=str(now_.day)+"-"+str(now_.month)+"-"+str(now_.year)


def appoinment_update(dis,day):
    link_='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+str(dis)+'&date='+str(day)
    c_link=requests.get(link_,headers=headers)
    c=c_link.json()
    c=c['centers']
    for i in range(len(c)):
        j=(c[i]['sessions'])
        for k in range(len(j)):
            cap=j[k]['available_capacity']
            if int(cap) != 0:
                availability=str(j[k]['available_capacity_dose1'])+ ' dose 1 & ' + str(j[k]['available_capacity_dose2'])+ ' dose 2 of ' +str(j[k]['vaccine'])+ ' are available on '+str(j[k]['date'])+ ' for above ' + str(j[k]['min_age_limit'])+ ' @ '+str(c[i]['name'])+ ' '+str(c[i]['pincode'])
                print(availability)


def API_caller(districts,day):
    for district in districts:
        appoinment_update(district,day)

while True:
    API_caller(district_id,day_)
    print('Calling sethu API......')
    time.sleep(18)
