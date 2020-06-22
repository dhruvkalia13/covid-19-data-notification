import http.client
import json
import schedule
import time

from win10toast import ToastNotifier


def job():
    print("Notification incoming (every hour)...")
    conn = http.client.HTTPSConnection("coronavirus-19-api.herokuapp.com")
    payload = ''
    headers = {}
    conn.request("GET", "/countries/india/", payload, headers)
    res = conn.getresponse()

    data = res.read()
    data = json.loads(data)
    name_of_country = data['country']
    total_cases = data['cases']
    total_deaths = data['deaths']

    toaster = ToastNotifier()
    toaster.show_toast(name_of_country, "Total cases - %s \nTotal Deaths - %s" % (total_cases, total_deaths))


job()
schedule.every(1).hour.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
