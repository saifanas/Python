# map ()    =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function, iterable)


store = [("shirts",20.00),
         ("pants",25.00),
         ("jackets",50.00),
         ("socks",10.00)]

to_inrs = lambda data: (data[0], data[1]*0.24)
to_dollars = lambda data: (data[0], data[1]/0.24)

store_inrs = list(map(to_dollars, store))

for i in store_inrs:
    print(i)