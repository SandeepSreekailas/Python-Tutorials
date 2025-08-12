# a= {
#     "name" : "john",
#     "name1" : "sandeep",
#     "age" : 22,
#     "place" :"palakkad"
# }

# a["city"] = "New York"
 
# print(a)  



# my_dict = {"name": "John", "age": 30, "city": "New York"}
# age = my_dict.pop("age")
# print(age)         
# print(my_dict)     

# my_dict = {"name": "John", "age": 30, "place": "palakkad"}
# last_item = my_dict.popitem()
# print(last_item)   

# my_dict = {"name": "John", "age": 30}
# # del my_dict
# # print(my_dict)  

# my_dict.clear()
# print(my_dict)  


# nested_dict = {
#     "person1": {"name": "John", "age": 30},
#     "person2": {"name": "Alice", "age": 25}
# }

# print(nested_dict["person2"]["name"])  




# my_dict = {"name": "John", "age": 30, "city": "New York"}
# city = my_dict.setdefault("place", "New York")
# print(city)    
# print(my_dict)


# cubes = {num: num**3 for num in range(1, 6)}
# print("Dictionary with cubes:", cubes)


# my_dict = {"name": "John", "age": 30}
# my_dict.update({"city": "New York", "age": 31})
# print(my_dict)  


# keys = ["name", "age", "city"]
# new_dict = dict.fromkeys(keys, "abc")
# print(new_dict)  

# my_dict = {"name": "John", "age": 30, "city" : "delhi"}
# city = my_dict.setdefault("city", "New York")
# print(city)    
# print(my_dict)   

# student = {"name": "Alice", "age": 20, "grade": "A"}
# student.pop("age") 
# print("Dictionary after removing 'age':", student)

student = {"name": "Alice", "age": 20}
new_data = {"grade": "A", "city": "New York"}
student.update(new_data)
print("Updated dictionary:", student)