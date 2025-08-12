# file = open("D:\sample6.txt", "r") 
# content = file.readlines() 
# print(content) 
# file.close() 

# file =open("D:/sample2.docx", "w")
# file.close()

# file = open("sample7.txt", "a") 
# file.write("\nAppended text.\n") 
# file.close() 

# file = open("sample2.txt", "w")
# lines = "HTML"
# file.write(lines) 
# file.close()

# file = open("sample17.txt", "r") 
# content = file.read() 
# print(content) 
# file.close() 

# file = open("sample2.txt", "a") 
# file.write("\ntxt") 
# file.close() 

# file = open("sample2.txt", "r") 
# lines = file.readline() 
# print(lines) 
# file.close() 

# file = open("sample2.txt", "w") 
# lines = ["Hello\n", "Welcome to Python file handling\n"] 
# file.writelines(lines) 
# file.close() 

# file = open("sample.txt", "w")
# file.write("H")
# file.close()

# file = open("sample5.txt", "a")
# file.write("Appended text.\n")
# file.close()

# with open("sample2.txt", "r") as file1:
#     content = file1.read()
#     print(content)



# with open("sample2.txt", "r") as file:
#     content = file.read()
#     position = file.tell()
#     print(position)
#     print(content)


# file = open("sample2.txt", "r")
# file.seek(5)  
# print(file.read())





# try:
#     file = open("sample17.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found!")




with open("barco.jpeg", "rb") as file:
    content=file.read()
    print(content)

