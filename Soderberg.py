import json

index_temperature = input("请输入当前指数温度:")
file_name = "data/records.json"
with open(file_name,'a') as f_obj:
    json.dump(index_temperature,f_obj)
    print("应该投资{}".format(float(100)))
