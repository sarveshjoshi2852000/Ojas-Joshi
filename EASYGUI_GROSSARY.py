from easygui import *
import sys
while 1:
     msgbox("Hello,welcome to the supermarket!!")
     
     msg="What do you want to buy?"
     title="A1 SUPERMARKET"
     choices=["CHOCOLATES","BISCUITS","SOAPS","CLOTHS"]
     choice=choicebox(msg,title,choices)
     if str(choice)=="CHOCOLATES":
        msg1="Which chocolates do you want?"
        title1="CHOCOLATES"
        choice1=["DairyMilk","Hersheys","Nutella","Kitkat","Gems"]
        choice2=choicebox(msg1,title1,choice1)
     elif str(choice)=="BISCUITS":
        msg2="Which biscuits do you want?"
        title2="BISCUITS"
        choice3=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
        choice4=choicebox(msg2,title2,choice3)
     elif str(choice)=="SOAPS":
        msg3="Which SOAPS  do you want?"
        title3="SOAPS"
        choice5=["ParleG","Hide and Seek","Bourbon","Monaco","Marie"]
        choice6=choicebox(msg3,title3,choice5)

     else:
         sys.exit()
     
