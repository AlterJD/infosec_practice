import rsa

(public_key, private_key) = rsa.newkeys(1024)
print("\n", str(public_key))
print("\n", str(private_key), "\n")

new_str = str(private_key)
new_str = new_str[11:(len(new_str)-2)]
new_list = new_str.split(', ')
print(int(new_list[0]))
print(int(new_list[1]))
print(int(new_list[2]))
print(int(new_list[3]))