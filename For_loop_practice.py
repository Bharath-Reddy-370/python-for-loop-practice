#Write a for loop that prints all multiples of 3 between 1 and 30.
#for i in range(1, 31):
#    j = 3
#    print(f"{j} X {i} = {i*j} ")
#    print()

 #Write a program using a for loop that calculates the sum of numbers from 1 to 10.

#for i in range(1, 11):
#    J = 0
#    J += i
#    print(f"sum: {i}+{J} = {i+J}")

#for name in "Bharath":
#    print(name)

Name = input("Enter your name : " )
Vowels = "AEIOUaeiou"
count = 0
for char in Name:
    if char in Vowels:
        print(char)
        count += 1
print("Number of vowels in count : ", count)