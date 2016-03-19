import os
import sys
import crypt
from datetime import datetime

#Time Stamp
time_stamp = datetime.now()

def passCracker(passcrypt,dictionary):
    salt = passcrypt[0:2]
    dictionary = open('dictionary.txt','r')
    for word in dictionary.readlines():
        word=word.strip('\n')
        wordcrypt = crypt.crypt(word,salt)
        if (wordcrypt == passcrypt):
            print 'Notification: [Success] Password Match Found!!!' + word + '\n'
            print time_stamp
        else:
            print 'Notification: [Failure] Match not found!!!'
            print time_stamp
    return

def main():
    username = raw_input("\n Please enter a username: ")	
	password = raw_input("\n Please enter a password: ")
	salt = password[0:2]
	passCrypt = crypt.crypt(password,salt)
	print passCrypt
	file = open("password.txt", "a")
	file.write(username + ':' + passCrypt + '\n')
	file.close()
	print passCrypt
	
    
    #passDoc = raw_input("\n Please enter file path for password file: ")
    #for file in os.listdir(os.getcwd()):
        #if file.endswith(".txt"):
            #if file.startswith("dictionary"):
                #print"Please Submit Another File!!!"
    #passCracker(cryptPass, dictionary)

if __name__ == '__main__':
    main()
