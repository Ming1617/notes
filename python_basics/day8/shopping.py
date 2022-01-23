dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

commodity_details = []


def Menu():
    """
        购物
    :return:
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            Add_shopping()
        elif item == "2":
            Settlement_shopping_cart()


def Settlement_shopping_cart():
    total_prices = 0
    for item in commodity_details:
        shang_pin = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
        total_prices += shang_pin["price"] * item["count"]
    while True:
        qian = float(input("总价%d元，请输入金额：" % total_prices))
        if qian >= total_prices:
            print("购买成功，找回：%d元。" % (qian - total_prices))
            commodity_details.clear()
            break
        else:
            print("金额不足.")


def Add_shopping():
    print_commodity_info()
    Add_commodity()


def Add_commodity():
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    commodity_details.append({"cid": cid, "count": count})
    print("添加到购物车。")


def print_commodity_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


Menu()
