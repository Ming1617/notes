import re

html='''


<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
'''
re_bds='<div class="animal">.*?title="(.*?)".*?content">(.*?)</p>'
pattern=re.compile(re_bds,re.S)
r_list=pattern.findall(html)
#问题2
for r in r_list:
    print('动物名称：',r[0].strip())
    print('动物描述：',r[1].strip())
    print('*'*50)
# print(r_list)