# a set of key value pairs is called dictionary
#dictionaries are mutable
#dictionaries do not allow duplicates

d = {1:'hello','two':42,'blah':[1,2,3],'dictionary':{1:'yo',2:'hoho'}}
#the key is written at first and the value is at last
del(d['dictionary'][1])
print(d['dictionary'])



#the keys() will return the list of all the keys in the dictionaries
x  = d.keys()
print(x)

#the values() method will return the list of all the values in a dictionary
y = d.values()
print(y)

#The items() method will return each item in a dictionary, as tuples in a list.
a = d.items()
print(a)

#To determine if a specified key is present in a dictionary use the in keyword:
if 1 in d:
    print("Yes ",1,"Exists in the dictionary")