import base64 as b64, os

usr = b'RA^yzRB~Z%b4O`%F#'
psw = b'Q+04<a#Lkvb#i4;VRLhLZ*pV'
spackman = b'Q*dEpYh-m~Wd'
spackpsw = b'b7gLGX>@6JWl(Q!c~oI(Y)5r@'
asi = b'K~qT'
asipsw = b'MQ3MdWnp9'

Username = input("Username: ")
if Username.encode("ASCII") == b64.b85decode(usr):
  print("Correct Username")
  Password = input("Password: ")
elif Username.encode("ASCII") == b64.b85decode(spackman):
  print("Correct Username")
  Password = input("Password: ")
elif Username.encode("ASCII") == b64.b85decode(asi):
  print("Correct Username")
  Password = input("Password: ")
  if Password.encode("ASCII") == b64.b85decode(psw):
    print("Welcome to the dungeon")
  elif Password.encode("ASCII") == b64.b85decode(spackpsw):
    print("You are the best teacher anyone has ever had and I definitely would be saying this even if you weren't making me. I am so lucky.")
  elif Password.encode("ASCII") == b64.b85decode(asipsw):
    print("Hello ASI, you are an egg head!!!!")
  else:
    print("Wrong Password")
else:
  print("Incorrect Username")

