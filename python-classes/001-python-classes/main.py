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