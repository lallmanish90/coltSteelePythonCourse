"""
Iterator:
-an object that can be iterated upon. An object which returns data, one element at a time
when next() is called on it
Iterable:
-an object which will return an iterator  when inter() is called on it.


**next**
-when next() is called on an iterator, the iterator returns for next item. it keeps 
doing so until it raises a Stopiterator error

"""
# writeing own custom loops


# def my_for(iterable, func):
#     iterator = iter(iterable)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration:
#             print("end of iterator")
#             break
#         else:
#             func(item)


# my_for("lol", print)

# working with iterators

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(50, 70):
    print(x)
