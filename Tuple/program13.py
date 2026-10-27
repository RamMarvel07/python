original = (10, 20, 30, 40, 50)
print("Original Tuple :", original)
mod_list = list(original)   
mod_list[2] = 99           
mod_list.append(60)         
modified_tuple = tuple(mod_list)
print("Modified Tuple :", modified_tuple)
