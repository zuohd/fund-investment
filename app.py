import json


from fund import FundRecord

index_temperature = input("请输入当前指数温度:")
fund_record=FundRecord(396)
fund_record.calculate_reference_amount(float(index_temperature))
file_name = "data/records.json"
with open(file_name,'a') as f_obj:
    json.dump(index_temperature,f_obj)
    print("应该投资{}".format(fund_record.reference_amount))
