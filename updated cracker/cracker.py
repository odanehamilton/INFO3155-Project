import crypt
from datetime import datetime

#Time Stamp
time_stamp = datetime.now()

def passCracker(password):
	salt = 'hidden'
	return crypt.crypt(password,salt)

def main():
	#Accepts and Encrypt a password
	password = raw_input("\n Please enter a password: ")
	passCrypt = passCracker(password)
	file = open("hashpass.txt", "a")
	file.write(passCrypt + '\n')
	file.close()
	print passCrypt
	#Encrypt words from Dictionary
	dictionary = open('dictionary.txt','r')
	for word in dictionary.readlines():
        	word=word.strip('\n')
        	wordcrypt = passCracker(word)
		print 'Password encrypted...'
		#Storing Hashed Password
		print "Storing encrypted password to file..."
		file = open("hashdic.txt", "a")
		file.write(wordcrypt + '\n')
		file.close()

	print "Encryption Complete - "
    
if __name__ == '__main__':
    main()
