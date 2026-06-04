class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
         return '🍪' * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("The capacity has to be greater than zero")
        self._capacity = capacity


    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0: #if size is negative
            raise ValueError("There aren't enough cookies!")
        elif size > self.capacity:
            raise ValueError("There isn't enough space!")
        else:
            self._size = size 
        
def main():
    capacity = int(input("Capacity: ")) 
    deposit = int(input("Deposit: "))
    withdraw = int(input("Withdraw: ")) 
    cookies = Jar(capacity)
    cookies.deposit(deposit) 
    cookies.withdraw(withdraw) 
    print(cookies)


if __name__ == "__main__":
    main()