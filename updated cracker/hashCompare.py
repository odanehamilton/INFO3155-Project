import crypt

salt = 'hidden'
dicttxt =[]
hashdict =[]
dicttxt =[word.rstrip('\n') for word in open('dictionary.txt')]
hashdict =[word.split() for word in open('hashdic.txt')]
i=0
count = len(dicttxt)

while (i < count):
		decryptpass = dicttxt[i]
		encryptpass = hashdict[0][i]
		case1 = crypt.crypt(decryptpass,salt)
		case2 = encryptpass
	
		print (decryptpass + "'s encryption: " + case1)
		print ("Hash for Dictionary Word: " + encryptpass + "\n")
	
		if (case1 == case2):
			print ("Match Found: " + case1 + '=' + decryptpass + "\n")
		i=i+1

