import re

# Matches any digit
# text = "There are 3 apples and 5 oranges."

# matches = re.findall(r"\d", text)
# print(matches)  


# text = "Hello Hello world"
# match = re.match(r"world", text)
# print(match)  

# text = "Hello world"
# match = re.search(r"world", text)
# print(match)  
# text = "Hello world"
# match = re.search(r"World", text, re.IGNORECASE)
# print(match)                                                                                                                                                                                                                                                                         

# text = "The price is 45 dollars, 30 cents, and 50 rupees."
# numbers = re.findall(r"\D+", text)
# print(numbers)  

# text = "Hello_ 123, welcome 456"
# new_text = re.sub(r"\D+", "123", text)
# print(new_text)  

# text = "apple, orange; banana, grape"
# fruits = re.split(r"[,;]", text)
# print(fruits)

# text = "John: 34, Alice: 45, Bob: 23" 
# matches = re.findall(r"(\D+): (\d+)", text) 
# print(matches) 

# text = "HELLO world"
# match = re.search(r"hello", text, re.IGNORECASE)
# print(match)  


# pattern = re.compile(r"\D+")
# text = "123 apples and 456 oranges"
# text1="123 banana and 456 apple"
# mat= pattern.findall(text)

# print(mat)  

# hell0= """fsgsfgpsgs
# sdgsdgsdugssujnnjdnfjdn
# adfhadbfahdfba
# vsdhhfisdhfdsuifhsdiufhsdi"""
# print(hell0)



# import re

text = """hello
world
hi boss"""

# Without re.MULTILINE
# match1 = re.search(r"^hi", text)
# print("Without MULTILINE:", match1)

# With re.MULTILINE
match2 = re.search(r"o$", text, re.MULTILINE)
print("With MULTILINE:", match2)


# text = """Hello World
# Python is fun"""

# match = re.search(r"d.Py", text, re.DOTALL)

# print(match)


#finditer
# text = "The price is 100 and then 200, 300"
# matches = re.finditer(r'\d+', text)
  
# for match in matches: 
#     print(f"Found {match.group()} at position {match.start()} to {match.end()}")


