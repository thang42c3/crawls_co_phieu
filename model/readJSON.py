import json

# Opening JSON file
f = open(r'..\file_csv\lich_su_gia_co_phieu.json', "r")

# returns JSON object as
# a dictionary
data = json.loads(f.read())
print(data['22-12-2006']['Gia_tham_chieu'])

a = []
for i in data:
    a.append(i)

t = '24-03-2021' in a
print(t)

print(a)
# Closing file
f.close()
# Iterating through the json
# list
