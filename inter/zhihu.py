import requests
session=requests.session()
#忽略警告
requests.packages.urllib3.disable_warnings()
session.headers['content-type']='application/x-www-form-urlencoded'
session.headers['user-agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
session.headers['x-zse-83']='3_2.0'
res=session.post('https://www.zhihu.com/udid')
print(res.text)
print(session.cookies)
#session.headers['cookie']='d_c0="AJDi5k_1hRCPTk-97Bvko561c_sGC6ROFao=|1576647692"; q_c1=64c862b4944a4509b6415df8dca99eda|1576647737000|1513836692000; __utma=51854390.1581097568.1576647741.1576647741.1576647741.1; __utmz=51854390.1576647741.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20171221=1; l_cap_id="NWY0YTExYTgyM2Y4NDc1ZDgxNzkxMzlhZTAwMzI4NmQ=|1576721444|d71874a37d1fa226ef3a9c0b1a0bb8f09d1afa1d"; r_cap_id="MzUwYzY1MjJlZjdiNDRjOWIxNGFkYTJkYjAwYjQyOWI=|1576721444|197096e17c5fcb2c44e395c8259a936f6fc6bdb0"; cap_id="YTQ5OGY2Y2ZiY2ZmNDdlOTk2ZjIyODQxZTBjY2I0ODA=|1576721444|4a286f7908cdb45d42a70960bda9493a3a24472a"; _zap=aa6692ab-7054-4b07-a89d-2625fc7bf665; _xsrf=FzIOHweOtfepgRIlwWcPYRpL40OvPbje; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1576647697,1576721308,1576721443,1578292553; tst=r; capsion_ticket="2|1:0|10:1578292955|14:capsion_ticket|44:MTY1YWEwM2YwZWFhNGY5ZjgyZWE2ODNhNmMyNTI5MDI=|beb202f885a8c142767776764bce98ad302258ad7fd2bc06d1782d45ce09d81a"; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1578296111|1578292549; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1578296115'
res=session.get('https://www.zhihu.com/api/v3/oauth/captcha?lang=cn')
print(res.text)

res=session.post('https://www.zhihu.com/api/v3/oauth/sign_in',
                 data='a8H0c79qkLnm2LF0z_pKg9H92Ltxg6O1XGO12rN0cT2tJvS8XLp1DhHKEMVVoBH0sTYhxU9qkLk12LF0z0pMebw1shoYi9omEqYhggHMcvOOsBOB8BF0g6S0gLOfkComBvCmevgqkLP9F9e0zMNmUBHqkLnm2Lf8PqxGQJe8ST2tUwO8mXY0Xg9hHhV9oqoMZu3qk4Q0oTYpkMFqmM20rQuyPh2pkLP9BLfBJJHmkCOOcBF0z_x0o6LB68xpkM2qsXN8oH98Hh2pNhFqmXtyUU98gwYfcTF8TBOqk4X92LkYkCpGZbSBDggqkLPfgG3ZsUO1iugZJvOfXqYhzqNMcCeMST2to8tyM8Yyk0U06M2pr_e0zRVmUbcMgcS_eBF0z_NM-ccM2wNOXqYhzuVKeCpGEwxO3BF0zRF0gDUqr02YrXNqzgY827XyNqFp6XY8M828oQLBFqYfXqYhygSVe9LBDrOf',verify=False)
print(res.text)