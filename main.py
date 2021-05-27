if __name__=='__main__':
  print("Select Your File")
  try:
    i = int(t("1 . Generate Hash \n2 . Check Hash"))
    if i == 1:
      hash = "yerxrogihad;ojmGPIOHLh EP($^D%&F^*hpjoP
      print("Your hash :",hash)
    else i == 2:
      j = ("Paste the hash")
      if j == hash:
        print("File not corrupted")
      else:
        print("File Corrupted")
  expect:
    print("invalid Choice")
  
