# Random Password Generator
import random
import string

alphabetsLowerCase = list(string.ascii_lowercase)
alphabetsUpperCase = list(string.ascii_uppercase)
numbers = [0,1,2,3,4,5,6,7,8,9]
specialChar = ["!","@","#","$","%","^","&","*","-","+","_","=","<",">"]

print('Welcome to Password Generator!')

while True:

  '''
  # 4 digit random password generator
  alphabetLower = random.choice(alphabetsLowerCase)
  alphabetUpper = random.choice(alphabetsUpperCase)
  number = random.choice(numbers)
  specialChar = random.choice(specialChar)
  
  password = alphabetUpper + alphabetLower + str(number) + specialChar
  print('Your new 4 digit password is: %s' % password)
  '''

  # "S" digit random password generator
  S = int(input("Enter number of digits of password you want : "))
  ranPassword = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = S))
  print('Your new password is: %s' % ranPassword)

  response = input('Would you like another password? Type y or n: ')
  if response == 'n':
    break
