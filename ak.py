import akshare as ak

try:
    # 调用新股申购接口
    df = ak.stock_new_share_subscribe()
    # 打印所有列名
    print("当前返回的字段名：", df.columns.tolist())
except Exception as e:
    print("获取数据失败：", e)
