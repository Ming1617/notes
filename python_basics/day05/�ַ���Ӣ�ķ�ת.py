#字符串英文反转
#“how are you”  --->  “you are how”
str_temp="how are you"
str_list=str_temp.split(" ")
str_list=str_list[::-1]
print(str_list)
str_temp=" ".join(str_list)
print(str_temp)