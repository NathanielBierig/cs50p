class Jar:
    
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return(f"\nCookies: {'🍪'* self.size} ({self.size}/{self.capacity})")

    def deposit(self,n ):
        
        if self._size + n > self.capacity:
            self._size = self.capacity
            raise ValueError("too many cokies")

        self._size += n

    def withdraw(self, n):
        if self._size- n < 0:
            self._size = 0
            raise ValueError("out of cookies")
        self._size -= n
      

    @property
    def capacity(self):
        return self._capacity 
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1 or not capacity:
            raise ValueError("invalid size")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
  
def main():
    cap = int(input("how big would you like your jar: "))
    jar = Jar(cap)
    cook = int(input("how many cookies would you like to start with: "))
    jar.deposit(cook)



    while True:
        try:
            print(f"\nCookies: {jar}")

            action = input("d = Deposit, w = Withdraw, or q = Quit? ").strip().lower()

            if action == "d":
                n = int(input("How many? "))
                jar.deposit(n)

            elif action == "w":
                n = int(input("How many? "))
                jar.withdraw(n)

            elif action == "q":
                print("have a good day and enjoy the cookies")
                break

            else:
                print("Invalid option.")

        except EOFError:
            print()
            break

        except ValueError as e:
            print(e)
            


if __name__ == "__main__":
    main()