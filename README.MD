# AppSecAssignment2.1 Important Files and Directories

## Part 1 Directory

### Attack1.txt
Contains a text file with the url that when used, triggers the xxs attrack

### Attack2.txt 
Contains an example post request that when used, triggeres the csrf attack for a given user in order to force them to gift me their giftcard. More information on how this is done can be found in bugs.txt

### Attack3.txt
Contains a post request that triggers the SQL injection that allows me to get the salted password for admin, and all users for that matter.

### Attack4request.txt
This contains a post request that triggers a command injection. THis is the official 'file' for this attack.

### Attack4file.txt
This is the text file i input into the use card page in ordre to trigger the attack. This is not the attack, but only a component used to partially generate the post request found in attack4request.txt

### Bugs.md
Contains my list of bugs and explainations of how I carried out each attack.
References the location of all changes I made in the code to fix the attacks. 

### Signing-key.pub
The ascii armoored gpg key. 

## GitCardSite Directory
The 'part 1 complete' commit marks the files needed for part 1, this inlcudes the bug fixes for my code. The made bugs.txt md commit is also used for part one as is the 
'added more csrf tokens' commit.
The 'part 2 complete' commit marks the files needed for part 2. The 'making sure my repos match' commit is also for part 2. 

## Part 2 Directory

### encryption-explaination.md 
which explains my changes 

## .github/workflows
Regression testing

## test.py
contains an attempt at a regression test for attack 1 (couldn't get it configured right)

