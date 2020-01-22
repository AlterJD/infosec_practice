import random


def hash_one(key, initial_str):
    initial_list = [ord(i) for i in initial_str]
    max_len = 122
    hash_list = [random.randrange(65, 122) for _ in range(0, max_len)]
    for i in initial_list:
        j = i - key
        hash_list[i] = j
    #print(hash_list)
    result = ''.join([chr(i) for i in hash_list])
    return result


def test_func(key):
    check_set = set()
    for i in range(5000):
        new_string = ''.join([chr(random.randrange(65, 122)) for _ in range(7)])
        if i < 10:
            print(new_string)
        check_set.add(hash_one(key, new_string))
        if i < 10:
            print(hash_one(key, new_string))
            print(len(check_set))
    print('Процент коллизий:', len(check_set)/ 5000)
    

k = 13
random.seed(k)
print(hash_one(k, 'hello world'))
print(hash_one(k, 'hello worle'))
result = hash_one(k, 'I see you')
print(result)
test_func(k)

