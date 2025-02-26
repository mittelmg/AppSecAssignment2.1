# Bugs

## Attack 1 (attack1.txt): Cross site scripting vulnerability

I crafted this http get request: http://127.0.0.1:8000/buy.html?director=<script>alert('xxs')</script>attacked%211 
When send to the server, this allows me to trigger an allert that says 'xxs' to the view of the web page. 


This vulerability exsi specifically for get requests that that access the buy_cards_view. 
In this view, when a GET request is submitted with the 'director' variable set the item_single.html template is rendered. 
In this template, if the director value is not 'none' it is intended to 'print' 'Endorsed by' the value of the director variable. Because this value can ben be set by user data submitted in the http request, I can submit whatever data or code I want.
Normally, django would filter out such user generated input but this variable value is marked as 'safe' which allows user generated input to run sucessfully on the site. 
Beacuse html doesn't distinguish between code and data, I am able to submit not text data but a script that runs when the page is rendered.
This triggers my alert message. 

### Remediation: I removd the safe tag on line 62 of item-single.html, causing the page to not render my script.

## Attack 2(attack2.txt): CSRF attack 

To sucessfully force a user to buy a card for me the target user must submit a gift card post request on the gift.html page.
Using Burp suite I can intercept that post request and set the username variable to my username. This sets the request to gift a card to me, rather than the intended recipiant.
This intercepted request will include their security credentials, tricking the server into assumeing they are gifting the card to me through their live session. 
I then  send the edit request to the server via a curl command.
This request sucessfully forces them to gift a card to my account. 

### Remediation: 
I added 'django.middleware.csrf.CsrfViewMiddleware' to the middleware on line 63 in settings.py to enable csrf protection.
In the post request on line 79 in gift.html I added {% csrf_token %}  to enable the csrf protections for that post request. 
I also added tokens on line 79 of item-single.html, line 78 of login.html, line 72 of register.html, line 93 of use-card.html to further secure the site. 

## Attack 3 (attack3.txt): SQL Injection
The attack can be found in my attack3.gftcrd file.
To retreive the salted passwords I can take advantage of the sites use of the raw() sql query function. 
Raw is a function that avoids input validation and submits whatever user generated query it is given.
Within the code, the raw querey submits a format string using the signature data input in the text of the giftcard file provided to the program by the user. 
To trigger this, I have to input a giftcard file in the 'choose file' feild on the use cards view. When I click 'submit' a post request containing my file is submitted to the server. 
The code then enters the use_card_view(request) function in views which contains the target raw() query. 

To take advantage of raw()'s vulnerailities, I crafted a gift card that first inputs a ' in order to close the single quotes around the %s format specifier and therefore cause whatever follows to be treated as an additional sql command rather than a string.
My string then follows with UNION SELECT password FROM LegacySite_user which adds a second sql query to the pre exsisting query inside the raw() function.
This query selects the password column from the user table, the column that contains the salted passwords. 
I end this with anothe signle quote "'" which acts to close the full string contained within the raw functions input. 
The response I get is an error response that cotains all the salted passwords - including the password for admin. 

### Remediation: 
I removed the quotes around the %s format specifier in line 197 in views.py so that the string cannot be escaped. 


## Attack 4: Command Injection (attack4.txt and attackfile.txt). 

The text file I input in order to trigger the attack is in attackfile.txt. The post request that acts as my attack is in attack4.txt. 

The parse_card_data(card_file_data, card_path_name) function in extras.py contains a system() call that submits a call that incldes user submitted data.
This vulnreability allows me to craft data that can trigger the server to execute whatever command I desire - a command injection attack. 
To do so, I needed to carefully craft a post request that navirgates the code to this function call. 
Specifically, I needed to create a user that didn't have any cards assigned to them.
On the use_card_view, I submitted a .txt file rather than a gift card file  and intercepted the post reqest that is triggered when I click submit.
I edit that post request and set 'card supplied' to 'False.' This cases the code to enter the  elif request.method == "POST" and request.POST.get('card_supplied', False): branch of the use_card_view(request) function in views.py.
Accessing this branch, the system sets the variable card_file_path to my user generated card file name which will later be entered into the system() call.
This variable is entered into the parse_card_data() function where the system call resides.
To by pass the  if type(card_file_data) != str: branch which would avoid the system call I had to input a text file, that contains a data that is indeed a string and, not a gift card file. The program then allows my to continue to the 'except' branch and onto the system() call. 

The data I then enter into the system call I set in my post request by editing the card_fname variable. I set its value to "dd""; echo 'hello';".
This value is assigned to the  cared_path_name variable that is entered into the system call. This valiables value when entered into system() is "/tmp/dd""; echo 'hello';_202_parser.gftcrd"

Here is what each of the components do inside the system command in order to allow me to preform a command injection attack:
"dd" is just a random string that represents the file name. 
' "" ' The first of these quotes terminates the cared_path_name string in the system call and the second terminates the pre-formatted string of commands that the function is designed to submit.
" ; "this allows me to append a second command onto the now terminated first command in the system call.
" Echo 'hello'; " - this is my command that forces ther serve to run an echo hello request. The server does indeed run this request and prints it on the terminal screen running the server program.
My input file had to be a text 

### Remediation: 
On line 61 of extras.py the input is placed into shlex.quote(card_path_name). This sanitizes the input and turns it into a string that cannot be treated as a command. I then place the sanitized output into my system call on line 63. The command injection is no longer possible. 



# Regression Testing
I confiugred a yaml file and workflows folder to create the test environment, a requirements.txt file to set up the environemnt, and a test case but I simply couldn't figure out how to work this. I put a lot of work into this, but I simply don't know whats wrong. Hopefully the work I've done can get me some partial credit. 
