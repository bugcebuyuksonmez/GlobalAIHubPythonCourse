my_list=[1,2,3,4,5,6]

num=int(len(my_list)/2)
first_half=my_list[:num]
second_half=my_list[num:]
my_list[0:3]=second_half
my_list[3:7]=first_half
print(my_list)