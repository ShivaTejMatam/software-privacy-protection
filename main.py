try:
  from py_essentials import hashing as hs
except:
  import os
  try:
    print("installing dependencies")
    os.system("pip install py_essentials")
  except:
    print("Connnect to internet and run")
   
  

if __name__=='__main__':
  from py_essentials import hashing as hs
  print("Select Your File")
  File_path = input("Enter path of file")
  try:  
    hash = hs.fileChecksum(File_path, "sha256")
    i = int(input("1 . Generate Hash \n2 . Check Hash"))
    if i == 1:
      print("Your hash :",hash)
    elif i == 2:
      j = ("Paste the hash")
      if j == hash:
        print("File not corrupted")
      else:
        print("File Corrupted")
    else:
      print("Invalid Choice")
  except:
    print("invalid Choice")
