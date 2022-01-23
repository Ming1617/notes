import csv

with open('fengyun.csv','w',encoding='utf-8',newline='')as f:
    writer=csv.writer(f)
    #写一行  -  参数为列表
    writer.writerow(['步惊云','超哥哥'])
    #写n行 - [(),(),()]
    writer.writerows([('聂风','梦'),('秦霜','孔慈')])