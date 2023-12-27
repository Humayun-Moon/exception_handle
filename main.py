# Exception = events deteted during execation the enterrupt the flow of a program
try:
    num = int(input("Enter a number to divide : "))
    denominator = int(input("Enter a number divide by : "))
    result = num/ denominator
    # print(result)
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 Enter a interprete number") 
except ValueError as e:
    print(e)
    print("you can't divide a number by words")        
except Exception:
    print("Something went wrong")
else:
    print("You got your answer")
    print(result) 
finally:
    print("This will always execute")       





    # https://www.youtube.com/watch?v=j_q6NGOwDJo