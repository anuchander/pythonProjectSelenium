file1 = open("/Users/anu/PycharmProjects/pythonProjectSelenium/myfile.txt", 'w')
L = ["This is Delhi\n", "This is Paris\n", "This is London\n"]
file1.writelines(L)
file1.close()

#append adds at last
file1 = open("/Users/anu/PycharmProjects/pythonProjectSelenium/myfile.txt", 'a')
file1.write("This is Singapore\n")
file1.close()

file1 = open("/Users/anu/PycharmProjects/pythonProjectSelenium/myfile.txt", 'r')
print(file1.read())
file1.close()

file1 = open("/Users/anu/PycharmProjects/pythonProjectSelenium/myfile.txt", 'w')
file1.write("This is tomorrow\n")
file1.close()

file1 = open("/Users/anu/PycharmProjects/pythonProjectSelenium/myfile.txt", 'r')
print(file1.read())
file1.close()