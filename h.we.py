usernames=["noor",  "moy" , "braa"]
passwords=["2012" , "700" , "900"]
for i in range(3):
    username=input("inter username")
    password=input("inter password")
    if (username==usernames[0] and password==passwords[0]):
     print("welcome noor")
     break
    else:

      print("wrong password or username")

      continue
print("try later")

