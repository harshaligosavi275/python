x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ct = input("\t\t\t\tType 'encrypt' for encryption, type 'decrypt' for decryption\n\t\t\t\t")
def encryption():
    loop=True
    while(loop):
        #  ct = input("\t\t\t\tType 'encrypt' for encryption, type 'decrypt' for decryption\n\t\t\t\t")
         message = input("\t\t\t\tType your message: ")
         shift_number = int(input("\t\t\t\tType the shift key: "))
         encrypted_result=" "
         for i in message:
                    if i in x:
                        i1=x.index(i)
                        e=(i1+shift_number)%26
                        i2 = x[e] 
                        encrypted_result = encrypted_result+i2  
                    else:
                        encrypted_result = encrypted_result+" " 
        
         print("\t\t\t\tHere's the encrypted result:", encrypted_result)
         yes_no= input("\t\t\t\tType 'Yes' if you want to go again. Otherwise Type 'no'\n\t\t\t\t")
         if(yes_no=='yes' or yes_no=='Yes'):
                 continue
         else:
                 loop=False
                 
   
    
def decryption():
    # ct = input("\t\t\t\tType 'encrypt' for encryption, type 'decrypt' for decryption\n\t\t\t\t")
    loop=True
    while(True):
      message = input("\t\t\t\tType your message: ")
      shift_number = int(input("\t\t\t\tType the shift key: "))
      decrypted_result=" "
      for i in message:
                    if i in x:
                        i1=x.index(i)
                        dn=(i1-shift_number)%26
                        i2 = x[dn]
                        decrypted_result = decrypted_result+i2
                    else:
                        decrypted_result = decrypted_result+" "  
      print("\t\t\t\tHere 's the decrypted result:",decrypted_result)
      yes_no= input("\t\t\t\tType 'Yes' if you want to go again. Otherwise Type 'no'\n\t\t\t\t")
      if(yes_no=='yes' or yes_no=='Yes'):
           continue
      else:
           loop=False
    
if(ct=='encrypt'):
          encryption()
elif(ct=='decrypt'):
        #   ct = input("\t\t\t\tType 'encrypt' for encryption, type 'decrypt' for decryption\n\t\t\t\t")
          decryption()
else:
    print("Invalid Operation")
