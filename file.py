# file = open("D:\sample6.txt", "r") 
# content = file.readlines() 
# print(content) 
# file.close() 


# file = open("sample3.txt", "a") 
# file.write("Appended text.\n") 
# file.close()  


# with open("sample3.txt", "r") as abc: 
#     content = abc.read() 
#     print(content) 

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



# with open("sample3.txt", "r") as file:
#     content = file.read()
#     position = file.tell()
#     print(position)
#     print(content)


# file = open("sample3.txt", "r")
# file.seek(6)  
# print(file.read())


# try:
#     file = open("sample17.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found!")




# with open("barco.jpeg", "rb") as file:
#     content=file.read()
#     print(content)



# file = open("sample17.txt", "r")
# content = file.read()
# print(content)


from docx import Document

# Create a new document
doc = Document()
doc.add_heading("My First DOCX File", level=1)
doc.add_paragraph("Hello, world! This is my first .docx file created using Python 🐍")
doc.add_paragraph("We can add multiple lines, just like writing a text file.")

# Save the file
doc.save("example.docx")


doc = Document("example.docx")

# Print all paragraphs
for para in doc.paragraphs:
    print(para.text)