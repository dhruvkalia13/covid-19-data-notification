import http.client
import json
import schedule
import time

from win10toast import ToastNotifier

def job():
    print("Notification incoming (every 15 minutes)...")
    conn = http.client.HTTPSConnection("coronavirus-19-api.herokuapp.com")
    payload = ''
    headers = {}
    conn.request("GET", "/countries/india/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    test1 = json.loads(data)

    toaster = ToastNotifier()
    toaster.show_toast(test1['country'], "Total cases - %s \nTotal Deaths - %s" % (test1['cases'], test1['deaths']))

job()
schedule.every(15).minutes.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
