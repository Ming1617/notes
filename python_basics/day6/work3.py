"""
计算一个字符串中的字符以及出现的次数.
abcdeadbd
"""
str_temp="abcdeadbd"
dist_sum_str={}

for i in str_temp:
    if i in dist_sum_str.keys():
        dist_sum_str[i] = dist_sum_str[i]+1
    else:
        dist_sum_str[i] = 1
# print(dist_sum_str.keys())
print(dist_sum_str)
