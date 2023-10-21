########### THIS CEASER CIPHER IS CREATED BY OZ-CODEZ ##########
######################### HAVE FUN #############################
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Ceaser Cipher")
def encrypt(text,shift):
  text_last =""

  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position+ shift
      new_letter = alphabet[new_position]
      text_last+=new_letter
    else:
      text_last +=letter
  print(f"the encoded text is {text_last}")
def decrypt(text,shift):
  text_last = ""

  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position - shift
      new_letter = alphabet[new_position]
      text_last += new_letter
    else:
      text_last += letter
  print(f"the decoded text is {text_last}")

go_on = True

while go_on:

  okay_input = False
  while  not okay_input:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if(direction.lower() == "encode" or direction.lower() == "decode"):
      okay_input =True
  text = input("Type your message:\n").lower()

  while True:
    try:
      shift = int(input("Type the shift number:\n"))
      break
    except:
      print("You need to enter a number")

  if (shift > 26):
    shift = shift % 26

  if direction.lower() == "encode":
    encrypt(text,shift)
  elif direction.lower() == "decode":
    decrypt(text,shift)

  ask_go_on = input("Do you wanna continue type 'yes' otherwise 'no' ")
  if ask_go_on == "no":
    go_on = False
    print("Goodbye")



