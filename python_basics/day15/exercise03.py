"""
    得到正确成绩异常测试
"""
def get_score():
    try:
       score = int(input("请输入成绩："))
    except:
        score=get_score()
    return score

print(get_score())