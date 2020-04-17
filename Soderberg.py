import json
index_temperature = input("指数温度多少?")
file_name = "data/records.json"
with open(file_name,'w+') as f_obj:
    json.dump(index_temperature,f_obj)
    print("应该投资{}".format(float(100)))
