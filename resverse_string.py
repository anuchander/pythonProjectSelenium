#resverse the entire string. So if the input string is "Hello how are you" after reversal it becomes
"uoy era woh olleH"

str1 = "Hello how are you"
print("The given string is :", str1)

str2 = str1[::-1]
print(str2)

#reverse the words in a string in-place. So the string "Hello how are you" should become "you are how Hello"
str1 = "Hello how are you"
str2 = str1.split(" ")
print("The new str2 string is: ", str2)
print(str2[::-1])
   

