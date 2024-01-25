#This is linear search in python
#It has O(n) complexity
def linearSearch(list, num):
    for i in list:
        if list[i] == num:
            return i
        else:
            return None
        
list_num = [5,45,21,8,63,9,41,22,10]
res = linearSearch(list_num, 48)
print(f"{res}")