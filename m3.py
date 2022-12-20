char=input("enter the char")
if char>="A" and char<="Z":
    print(char)
    sp_char=input("enter special charecter")
    if sp_char=="#" or sp_char=="@":
        print(sp_char)
        digit=(input("enter number"))
        if digit>="0" and digit<="9":
            print(digit)
            spw=char+sp_char+digit
            print(len(spw))
            if len(spw)>=8:
                print(spw)
            else:
                print("wrong password")
        else:
            print("enter the number")
    else:
        print("enter the special character")
else:
    print("enter charecter")