import akshare as ak

try:
    # 调用新股申购与中签查询接口，可根据需求修改 symbol 参数
    # symbol 可选值示例："全部股票", "沪市主板", "科创板", "深市主板", "创业板" 等
    df = ak.stock_xgsglb_em(symbol="全部股票")  
    # 打印所有列名
    print("当前返回的字段名：", df.columns.tolist())
    # 若想查看具体数据，可额外打印
    print("返回的数据示例：")
    print(df.head())
except Exception as e:
    print("获取数据失败：", e)
