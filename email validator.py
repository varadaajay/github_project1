import re
email_id=input("Enter your email_id:")
pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

if re.search(pattern, email_id):
  print("f{email_id} is --Valid--")
else:
  print("f{email_id} is --Not_Valid--")