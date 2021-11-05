# Code Fixes

## Attack 1
I removd the safe tag on line 62 of item-single.html, causing the page to not render my script.

## Attack 2
I added 'django.middleware.csrf.CsrfViewMiddleware' to the middleware on line 49 in settings.py to enable csrf protection.
In the post request on line 79 in gift.html I added {% csrf_token %}  to enable the csrf protections for that post request. 

## Attack 3
I removed the quotes around the %s format specifier in line 194 in views.py so that the string cannot be escaped. 

## Attack 4
On line 60 of extras.py the input is placed into shlex.quote(card_path_name). This sanitizes the input and turns it into a string that cannot be treated as a command. I then place the sanitized output into my system call. The command injection is no longer possible. 