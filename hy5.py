def cal(old):
    print ("Your dog is "+str((old-2)*4+24)+" years old in human years.")
old = input("Enter your dog's age(3 or older):")
cal(int(old))