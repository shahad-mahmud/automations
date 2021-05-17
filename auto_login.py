import requests

logininfo = {'username':'demo22', 'password':'demo'}
r = requests.post("http://hajirakhata.revesoft.com/Login.do", data=logininfo)
print(r.status_code)
if (r.status_code==200):
     print("Correct login")