import pandas as pd
import os
import sys
import random
import matplotlib
import matplotlib.pyplot as plt

# membuat class rumah
class Rumah:
    pass


# membuat instansiasi dari class rumah
rumah1 = Rumah()

# menambahkan property ke object
rumah1.x = 10

print(rumah1.x)

# keyword untuk mengapus object / class
del(Rumah)
del(rumah1)


class Rumah:
    # menambahkan variable ke class
    x = 10
    
rumah1 = Rumah()

print(rumah1.x)

# menambahkan anonymus function ke object
rumah1.tambah1 = lambda: rumah1.x+1

print(rumah1.tambah1())

del(Rumah)
del(rumah1)


class Rumah:
    x = 10
    # function lambda di bawah ini hanya bisa dipanggil dalam konteks class tidak bisa dalam keadaan object
    tambah1=lambda: Rumah.x+1


# rumah ke-3
print("ini rumah ke-3")
rumah1 = Rumah()

print(f"class: {Rumah.x}")
print(f"object: {rumah1.x}")
print(Rumah.tambah1())

# perubahan pada variable dibawah ini hanya akan berdampak pada konteks object tidak pada konteks class
rumah1.x+=1
print(f"class: {Rumah.x}")
print(f"object: {rumah1.x}")


del(Rumah)
del(rumah1)


class Rumah:
    x=10


def tambah1():
    return Rumah.x+1


Rumah.tambah1 = tambah1


rumah1 = Rumah()

# function tambah1 hanya bisa dipanggil pada konteks class tidak pada konteks object
print(Rumah.tambah1())

del(Rumah)
del(rumah1)