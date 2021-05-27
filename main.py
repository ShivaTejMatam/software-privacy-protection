import hashlib

class RSA:
    def PasswordHasher(self, file):
        return hashlib.sha256(file.encode()).hexdigest()

if __name__=='__main__':
  print("Select Your File")
  File_path = input("Enter path of file")
  File = open(File_path , "r")
  try:
    i = int(input("1 . Generate Hash \n2 . Check Hash"))
    if i == 1:
      hasher = RSA()
      hash = hasher.PasswordHasher(File)
      print("Your hash :",hash)
    else i == 2:
      j = ("Paste the hash")
      hash = hasher.PasswordHasher(File)
      if j == hash:
        print("File not corrupted")
      else:
        print("File Corrupted")
  expect:
    print("invalid Choice")
  
