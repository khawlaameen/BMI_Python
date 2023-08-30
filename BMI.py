#function to calculate bmi 
def calculate_BMI(weight,height):
    #convert meter and KG
   bmi=(weight*10)/((height*height)*.001)
   return bmi

#check the result of bmi and give description
def interpret_BMI(bmi):
    if (bmi < 18.5):
       print("Underweight")
  
    elif (bmi >18.5 and bmi <= 25 ):
      print("Normal weight")   

    
    elif (bmi >25 and bmi <= 30 ):
      print("Overweight" )  

    
    elif (bmi > 30 ):
      print("Obese")   

    
#ask user to enter his/her weight and height
weight=float(input("enter your wight"))
height=float(input("enter your height"))

#call the function and pass the user inputs to it
bmi =calculate_BMI(weight,height)
#check the result of bmi and give description
des= interpret_BMI(bmi)
