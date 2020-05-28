import json
json_var =""" 
{ 
	"Country": { 
		"name": "INDIA", 
		"Languages_spoken": [ 
			{ 
				"names": ["Hindi", "English", "Bengali", "Telugu"] 
			} 
		] 
	} 
} 
"""
var = json.loads(json_var) 
print(var['Country']['Languages_spoken'][0]['names'])

for key in var.keys():
    print(key,var[key])