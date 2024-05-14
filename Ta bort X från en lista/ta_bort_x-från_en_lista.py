
number_list = [10,1,3,3,3,9,2,3,6,7,9,5,0,10,4]
new_number_list = []

what = int(input("What nummber do you want to remove:"))
remove_list = []




for num in number_list:

    if num == what:
        pass
    else:
        new_number_list.append(num)
    
print(new_number_list)