import random
import time
print('1-rock , 2-paper, 3- scissor, 4- end')
a = int(input('enter a number'))
uscore = 0
pcscore = 0
while(a!=4):
    
    if a > 4 or a <= 0:
        print("choose a correct number")
    else:       
        if a == 1:
             print('you choose rock')
        elif a == 2:
             print('you choose paper')
        else:
            print('you choose scissor')    


        print('computer choosing')
        time.sleep(3)     
        b = random.randint(1,3)
        if b == 1 :
            print('PC choose 1-rock')
        if b == 2 :
            print('PC choose 2-paper')
        if b == 3 :
            print('PC choose 3-scissor')

        time.sleep(2)

        if (a == 1 and b == 1) or (a == 2 and b == 2) or (a == 3 and b == 3):
            print('Tie')
        if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
            print("PC wins")
            pcscore+=1
            print("pc score: ", pcscore ,"user score: ", uscore)
        if (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
            print('User wins')
            uscore+=1
            print("pc score: ", pcscore ,"user score: ", uscore)
    a = int(input('enter a number'))
time.sleep(2)
print('Final Score of user is {0} and PC is {1}'.format(uscore,pcscore))
if pcscore > uscore :
    print('PC wins the game')
elif uscore > pcscore:
    print('User wins the game')
else :
    print("The game is a tie")
print('game ends')


