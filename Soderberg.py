import json
print("基金切换规则说明：当出现另一只指数温度低于当前指数2度（5度一定要切换）以上的时候，\n"
      "我们就要迅速把这只指数对应的基金揽入怀中。之前的那个指数只要没超过40度就继续持有，\n"
      "等它超过40度开始按比例卖出")
index_temperature = input("请输入当前指数温度:")
file_name = "data/records.json"
with open(file_name,'a') as f_obj:
    json.dump(index_temperature,f_obj)
    print("应该投资{}".format(float(100)))
