#This is linear search in python
#It has O(n) complexity
def linearSearch(list, num):
    for i in list:
        if list[i] == num:
            return i
        else:
            return None
        
list_num = [5,45,21,8,63,9,41,22,10]
list_num2 = [54,22,100,32,5,8,74,99]

res = linearSearch(list_num, 48)
res2 = linearSearch(list_num2, 48)

print(f"{res}")
print(f"{res2}")

#this comment was added
#on feature2 branch

#this edit is done on master
#feature3 branch commit
#feature3 branch commit2
