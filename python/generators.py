# Genarator is a simple way of crerating iterator
# Difference between yield and return. when we return something in a function returns and basically it destroies all its local varaibles and so on
# When we yield it preserves the state of last execution

def remote_control_next():
    yield "cnn"
    yield "espn"

itr=remote_control_next()
print(next(itr)) # cnn
print(next(itr)) # espn

# also we can do

for c in remote_control_next():
    print(c)

# Now we develop a fibonnaci series using the generators

def fib():
    a,b =0,1
    while True:
        yield a
        a,b=b,a+b

for f in fib():
    if f>50:
        break
    print(f)

# benifits of using the generators over class based iterator
# 1.you don't need to define iter() and next() methods
# 2.you don't need to raise stopiteration exception