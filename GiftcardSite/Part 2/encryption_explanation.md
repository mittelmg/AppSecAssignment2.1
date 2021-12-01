#  Database Models Encryption:
To Implement this I imported the django-cryptography module in models.py. From this I used the encrypt() function which I wrapped around the sensative feilds in my card class. 
Specficially, in models.py I wrapped encrypt around the class variables fp (line 45), data (line 42), and amount (line 44) because these are the data that are most sensative and could be useful if the data was leaked.
Encrypyting these values will block any hacker who might obtain the records from using the cards. 

The encrypt() function is very useful because it both encrypts and decrypts the data as needed using the value I set for SECRET_KEY.

# Key Management:
To truely potect my encrypted data above I need to protect my SECRET_KEY  and other sensative values such as DEBUG . 
To protect these, I need to seperate their values from my source code. I can do so using the decouple library.
To implement, I first created a .env file in my root directory and copied my sensative values into that .env file, DEBUG (line 6) and SECRET_KEY(line 2).
In settings.py I then make these value's accessable to my app by importing the decouple module (line 16) and using its congif() function to connect my env file with settings.py.
I connect my secret key with the value in .env with the config function on line 27 and connect my DEBUG value with .env on line 30 of settings.py. 
When the app fetches either of these values from settings.py, the variable will use the config function to look up and return the value specified in the parenthesis in .env.

This process sucessfully seperates my sensative secret key value into the .env and decouples my source code from this value so that their plain text values aren't sitting in the code waiting to be stolen. 

