import base64 as b64
string = "Egghead"
string = string.encode("ASCII")
print(b64.b85encode(string))


#b'Q*dEpYh-m~Wd'
#b'b7gLGX>@6JWl(Q!c~oI(Y)5r@'