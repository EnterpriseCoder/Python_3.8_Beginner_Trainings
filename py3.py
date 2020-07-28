for y in range(0,100):
    print("2 Player Rock Scissor Paper game  without dictonaries long way by arda duman")
    time = int(input("Choose Number Of Round(1 to 10) :" ))
    p1score=0
    p2score=0
    for x in range(0,time):
        p1=input("P1 Enter:"+"rock scissor paper").lower()
        p2=input("P2 Enter:"+"rock scissor paper").lower()   

        while p1=='rock':
            
            
            if p2=='scissor':
                p1score=p1score+1
                p2score=p1score+0

                print("ScoreBoard\n P1 = "+str(player1)+" \n P2 = "+ str(player2))
            elif p2=='paper':
                p2score=p2score+1
                p1score=p1score+0


            elif p1==p2:
                p1score=p1score+0.5
                p2score=p2score+0.5

            else:
                pass
            break
            

        while p1=='paper':
            
            if p2=='scissor':
                p1score=p1score+0
                p2score=p2score+1
                

            elif p2=='rock':
                p1score=p1score+1
                p2score=p2score+0

            elif p1==p2:
                p1score=p1score+0
                p2score=p2score+0
            else:
                pass
            
            break
        while p1=='scissor':

            if p2=='paper':
                p1score=p1score+1
                p2score=p2score+0

            elif p2=='rock':
                p1score=p1score+1
                p2score=p2score+0

            elif p1==p2:
                p1score=p1score+0
                p2score=p2score+0

            else:
                pass
            break
        print("p1's score :"+str(p1score)+ "\n"+ "p2's score :"+str(p2score))
            
