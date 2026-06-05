
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, passenger):
        self.queue.append(passenger)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None

    def peek(self):
        if len(self.queue) > 0:
            return self.queue[0]
        return None

    def display(self):
        if len(self.queue) == 0:
            print("No passengers waiting.")
        else:
            print("Passengers Waiting:")
            for passenger in self.queue:
                print(passenger)

queue = Queue()

while True:
    print("\n1. Add Passenger")
    print("2. Serve Passenger")
    print("3. View Next Passenger")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        name = input("Add Passenger: ")
        queue.enqueue(name)

    elif choice == 2:
        passenger = queue.dequeue()
        if passenger:
            print("Passenger Served:")
            print(passenger)
        else:
            print("No passengers in queue.")

    elif choice == 3:
        passenger = queue.peek()
        if passenger:
            print("Next Passenger:")
            print(passenger)
        else:
            print("No passengers in queue.")

    elif choice == 4:
        queue.display()

    elif choice == 5:
        break

    else:
        print("Invalid Choice")






