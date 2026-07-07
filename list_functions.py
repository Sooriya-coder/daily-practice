#getting stronger in concepts of list functions in python
 # 1) append method , which is  used to add the new element in the end of the list
 
list=["virat","salt","padikal","rajat","jithesh sharma","tim","krunal","sheperd"]
list.append("Bhuvi")
print(list)

#2)insert method, which is used to add the new element in the specific index of the list

list.insert(8,"Rashid")
print(list)

#3)pop method, which is used to remove the element from the list based on index
list.pop(8)
print(list)

#4)extend method, which is used to add the new element in the end of the list,and also it is iterable function when the times of the program runs
list.extend(["Rashid", "Bhuvi"])
print(list)

#5)remove method, which is used to remove the element from the list based on value
list.remove("Rashid")
list.remove("Bhuvi")
print(list)

