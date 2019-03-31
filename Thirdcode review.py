theScoreIs = 0


print("The current score is " + str(theScoreIs))
print ("Hello and you current score is less than 10 try and get it there")

while(theScoreIs < 10):
    scoreAdd = input("Enter a number")
    theScoreIs = theScoreIs + int(scoreAdd)
    print("The current score is ")
    print(theScoreIs)

#print("The current score is " + theScoreIs + "The current score is higher than 10 :) end!")
