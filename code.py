def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight/(height*height)
 print(str(bmi))
 if bmi < 18.5:
  print ("User is under weight")
  return -1
 elif bmi >= 18.5 and bmi <= 25.0:
  print ("User is normal weight")
  return 0
 elif bmi > 25.0:
  print ("User is over weight")
  return 1

weight = float(input())
height = float(input())
calculate_bmi(weight, height)

