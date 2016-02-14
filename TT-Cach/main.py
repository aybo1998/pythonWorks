from random import randint
print '''
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
|                                                           |
|                Welcome To TT-Cash Game  V 1.00            |
| Law of the game :                                         |
|   Write a number Consists of 8 number                     |
|   and the first number is 9 .                             |
|                                                           |
|  * If you went to go out write exit                       |
|                                                           |
|                                         By Club Gnulug    |
|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|
 '''

m = str(randint(90000000,99999999))
attempts=10
try:
    while True:
        print '\n\nyou have %s attempts '%attempts
        answer = raw_input('Enter the number :')
        t = ''
        if answer == 'exit':
            print '\n\nyou welcome !! '
            exit()
        elif len(answer)!=8:
            print 'Please write 8 number '
            continue
        else:
            x = 0
            while x<len(m):
                if m[x] == answer[x]:
                    t += m[x]
                else:
                    t += '*'
                x += 1
            print t
            attempts -= 1
            if m==answer:
                print '\n\n Very Good !! :) '
            elif attempts == 0:
                print '\n\nI\'m sorry but you lose \nthe right number is %s'%m
                answer = raw_input('\nif you want replay enter yes \nif not enter exit \n\n your answer :')
                if answer =='yes':
                    m = str(random.randint(90000000,99999999))
                    attempts=10
                    continue
                else:
                    print ' Thank you for playing !! '
                    break
except KeyboardInterrupt:
    print "\n\nyou welcome !! "
