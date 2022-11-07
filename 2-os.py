import time
from itertools import product
from hashlib import sha256 as hash_
import threading

print("Как расшифровать:")
print("\tОднопоточно\t\t\tМногопоточно")
print("\t[1]\t\t\t\t\t[2]")

choise = int(input())
hash_array = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'

if choise == 1:
    timee = time.time()
    for j in range(3):
        start_time = time.time()
        for i in product("abcdefghijklmnopqrstuvwxyz", repeat=5):
            if hash_("".join(i).encode("utf-8")).hexdigest() == hash_array[j]:
                print("".join(i), (time.time() - start_time))
                break
    print(time.time() - timee)

elif choise == 2:
    hash_array = '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f', '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b', '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad'

    void = []

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def sha(first, second):
        start_timer = time.time()
        for j in alphabet[first:second]:
            for k in product(alphabet, repeat=4):
                temp = j
                temp += "".join(k).encode("utf-8")
                x = hash_(temp).hexdigest()
                if x == hash_array[0] or x == hash_array[1] or x == hash_array[2]:
                    if x not in void:
                        print(temp, (time.time() - start_timer))
                        void.append(x)
        

        

thr1 = threading.Thread(target = sha, args=(0, 6)).start()
thr2 = threading.Thread(target = sha, args=(6, 12)).start()
thr3 = threading.Thread(target = sha, args=(12, 18)).start()
thr4 = threading.Thread(target = sha, args=(18, 27)).start()
        



