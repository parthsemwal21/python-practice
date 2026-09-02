# q1. Write a function fizzbuzz(n) that takes a single number and prints "Fizz" if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz"
# 5 if it's divisible by both, otherwise print the number itself

def fizbuzz(n):
    if n%3==0 and n%5==0:
         print("fizzbuzz")
    elif n%3==0:
          print("fizz")
    elif n%5==0:
     print("buzz")
    return(n)
    

ans=fizbuzz(15)
ans=fizbuzz(9)
ans=fizbuzz(20)
ans=fizbuzz(7)

print(ans)  




