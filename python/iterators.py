# Iterators are to iterate through the object like a list, tuple, string and iter() is the key word used to iterate
# through the objects using next() for the next element in object also we use reversed() to reverse the iteration

lst=[1,2,3,4,5]
name=iter(lst)
print(f'name {name}')
print(next(name)) #1 is a output
rev=reversed(lst)
print(next(rev))  #5 is a output

# Lets implement a remote control class that allows you to press "next"
# button to go to next TV channel

class RemoteControl:
    def __init__(self):
        self.channels=['HBO','CNN','STAR','SIASAT']
        self.index=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]
    
channel=RemoteControl()
itr=iter(channel)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
