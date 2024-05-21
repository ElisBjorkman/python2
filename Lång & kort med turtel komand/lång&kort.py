
import turtle 

turtle.color('red') 

svar = input("Hur långt ska jag gå? (kort/långt):") 
if svar == "kort": 
    turtle.forward(50) 
elif svar == "långt": 
    turtle.forward(200) 
else: 
    print("Förstår inte")