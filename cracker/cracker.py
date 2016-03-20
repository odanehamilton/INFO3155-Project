import os
import crypt


def passCracker(passcrypt, user):
    salt = passcrypt[0:2]
    dictionary = open('dictionary1.txt','r')
    for word in dictionary.readlines():
        word=word.strip('\n')
        wordcrypt = crypt.crypt(word,salt)
        if (wordcrypt == passcrypt):
            print 'Success! ' + user + "'s password was cracked."
            print user + "'s password is: " + word + "\n"+ "\n"
            return
    print user + "'s password could not be cracked." + "\n" + "\n"
    return

def main():
    x = 2
    while (x != 1):
        username = raw_input("\n Please enter a username: ")	
        password = raw_input("\n Please enter a password: ")
        salt = password[0:2]
        passCrypt = crypt.crypt(password,salt)
        file = open("passwords.txt", "a")
        file.write(username + ':' + passCrypt + ':' + '\n')
        file.close()
        f = raw_input("\nPlease enter a value other than 1 for x to continue entering data: ")
        x = int(f)

    passDoc = open('passwords.txt')
    for line in passDoc.readlines():
        if ':' in line:
            user = line.split(':')[0]
            passcrypt = line.split(':')[1].strip(' ')
            print "[*][*][*]Cracking Password for user: " + user + " [*][*][*]"
            passCracker(passcrypt, user)

if __name__ == '__main__':
    main()
