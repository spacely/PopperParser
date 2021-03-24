import yaml,json

with open(r'wf.yml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    wf_file = yaml.load(file, Loader=yaml.FullLoader)

    _json_file = json.dumps(wf_file)

    open("testfile.json", "w").write(_json_file)

with open("testfile.json") as f:
	data = json.load(f)

##print(data['steps'][0]['id'])

##for a in data['steps']:
##	print(a)

for dictionary_Data in data['steps']:
	for key in dictionary_Data:
		if key == 'id':
			new_key ='name'
			dictionary_Data[new_key] = dictionary_Data.pop(key)
			print(dictionary_Data)


print(data)


##print(type(data['steps'][0]))
##print(type(data['steps']))
    ##print( type(testfile.json))

   