from pycrontab import crontab, crontab_run
print("job init success")
script2 = '/volumeUSB1/usbshare/py/delete_dup.py'
crontab.every('hour').interval(3).execute(script2," -a")

script1 = '/volumeUSB1/usbshare/py/test_alert.py'
crontab.every('minute').interval(30).execute(script1,None)

crontab_run(debug=True)
