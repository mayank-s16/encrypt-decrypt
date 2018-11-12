s=input("Enter the text you want to encrypt or decrypt: ")
key="m&"+str(len(s)%10)+"&m"
ukey=input("Enter the key: ")
if ukey==key:
    print("Congrats you have entered the right key")
    l1=[]
    l=list(s)
    for _ in l:
        if _=='A':
            l1.append('!')
        elif _=='!':
            l1.append('A')
            
        elif _=='B':
            l1.append('*')
        elif _=='*':
            l1.append('B')
            
        elif _=='C':
            l1.append('&')
        elif _=='&':
            l1.append('C')
            
        elif _=='D':
            l1.append('#')
        elif _=='#':
            l1.append('D')
            
        elif _=='E':
            l1.append('@')
        elif _=='@':
            l1.append('E')
            
        elif _=='F':
            l1.append('0')
        elif _=='0':
            l1.append('F')
            
        elif _=='G':
            l1.append('9')
        elif _=='9':
            l1.append('G')
            
        elif _=='H':
            l1.append('d')
        elif _=='d':
            l1.append('H')
            
        elif _=='I':
            l1.append('/')
        elif _=='/':
            l1.append('I')
            
        elif _=='J':
            l1.append(' ')
        elif _==' ':
            l1.append('J')
            
        elif _=='K':
            l1.append('w')
        elif _=='w':
            l1.append('K')
            
        elif _=='L':
            l1.append('7')
        elif _=='7':
            l1.append('L')
            
        elif _=='M':
            l1.append('s')
        elif _=='s':
            l1.append('M')
            
        elif _=='N':
            l1.append('8')
        elif _=='8':
            l1.append('N')
            
        elif _=='O':
            l1.append('r')
        elif _=='r':
            l1.append('O')
            
        elif _=='P':
            l1.append('o')
        elif _=='o':
            l1.append('P')
            
        elif _=='Q':
            l1.append('z')
        elif _=='z':
            l1.append('Q')
            
        elif _=='R':
            l1.append('k')
        elif _=='k':
            l1.append('R')
            
        elif _=='S':
            l1.append('m')
        elif _=='m':
            l1.append('S')
            
        elif _=='T':
            l1.append('j')
        elif _=='j':
            l1.append('T')
            
        elif _=='U':
            l1.append('1')
        elif _=='1':
            l1.append('U')
            
        elif _=='V':
            l1.append('y')
        elif _=='y':
            l1.append('V')


            
        elif _=='W':
            l1.append('l')
        elif _=='l':
            l1.append('W')
            
        elif _=='X':
            l1.append('n')
        elif _=='n':
            l1.append('X')
            
        elif _=='Y':
            l1.append('f')
        elif _=='f':
            l1.append('Y')
            
        elif _=='Z':
            l1.append('q')
        elif _=='q':
            l1.append('Z')
            
        elif _=='b':
            l1.append('g')
        elif _=='g':
            l1.append('b')
            
        elif _=='a':
            l1.append('4')
        elif _=='4':
            l1.append('a')
            
        elif _=='c':
            l1.append('x')
        elif _=='x':
            l1.append('c')
            
        elif _=='e':
            l1.append('3')
        elif _=='3':
            l1.append('e')
            
        elif _=='h':
            l1.append('6')
        elif _=='6':
            l1.append('h')
            
        elif _=='i':
            l1.append('2')
        elif _=='2':
            l1.append('i')
            
        elif _=='p':
            l1.append('v')
        elif _=='v':
            l1.append('p')
            
        elif _=='t':
            l1.append('?')
        elif _=='?':
            l1.append('t')
            
        elif _=='u':
            l1.append('5')
        elif _=='5':
            l1.append('u')

        else:
            l1.append(_)
        ed="".join(l1)
    input("Press Enter Key for encryption or decryption")
    print("Your output is {}".format(ed))
    
else:
    print("Sorry your key is not correct.. Try again..")
