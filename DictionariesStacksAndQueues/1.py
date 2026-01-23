# Create a dictionary describing your mobile phone. 
# Use 6 key-value pairs of data. 
# Then, using for loop, display the contents of the dictionary. 
# To read a key and value, use the items() method.

mobile = {
'OS':'Android',
'Brand':'Xiaomi',
'Model':'Redmi Note 5',
'RAM':'4GB',
'Battery':'4000mAh',
'Processor':'Qualcomm Snapdragon 625'
}

for key,value in mobile.items():
    print(f'{key} : {value}')
