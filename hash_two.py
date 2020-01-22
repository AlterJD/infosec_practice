import random

def hash_two(key, initial_str):
    initial_list = [ord(i) for i in initial_str]
    #print(initial_list)
    result = ''.join([str(initial_list[i] ^ initial_list[i+1]) for i in range(len(initial_list)-1)])
    result += str(initial_list[0] ^ initial_list[-1])
    return result

    
def test_func(key):
    check_set = set()
    for i in range(5000):
        new_string = ''.join([chr(random.randrange(65, 122)) for _ in range(7)])
        if i < 10:
            print(new_string)
        check_set.add(hash_two(key, new_string))
        if i < 10:
            print(hash_two(key, new_string))
            print(len(check_set))
    print('Процент коллизий:', len(check_set)/ 5000)

k = 5
string = 'I see you'
print(hash_two(k, string))
test_func(k)
    