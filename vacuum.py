class VacuumCleaner:
    def __init__(self):
        self.location = "A"  # Initial location of vacuum cleaner
        self.status = {"A": "CLEAN", "B": "CLEAN"}  # Initial status of both rooms
        self.cost = 0  # Initial cost

    def get_percept(self):
        return self.location, self.status[self.location]  # Returns current location and status

    def suck(self):
        self.status[self.location] = "CLEAN"  # Cleans the current location
        self.cost += 1  # Sucking dirt adds to cost
        print(f"Sucked dirt at location {self.location}")

    def move_left(self):
        if self.location == "B":
            self.location = "A"  # Move from B to A
            print("Moved to location A")

    def move_right(self):
        if self.location == "A":
            self.location = "B"  # Move from A to B
            print("Moved to location B")

    def start(self):
        while True:
            location, status = self.get_percept()
            print(f"Current location: {location}, Status: {status}")
            if status == "DIRT":
                self.suck()
            else:
                if location == "A":
                    self.move_right()
                else:
                    self.move_left()
            if self.status["A"] == "CLEAN" and self.status["B"] == "CLEAN":
                print(f"Both rooms are clean. Total cost: {self.cost}.")
                break

if __name__ == "__main__":
    i = 0
    while i < 4:
        i += 1
        vacuum = VacuumCleaner()
        initial_location = input("Enter initial location (A/B): ").strip().upper()
        initial_status_A = input("Enter status of room A (CLEAN/DIRT): ").strip().upper()
        initial_status_B = input("Enter status of room B (CLEAN/DIRT): ").strip().upper()
        vacuum.location = initial_location
        vacuum.status["A"] = initial_status_A
        vacuum.status["B"] = initial_status_B
        vacuum.start()

"""
---------------- Sample Output ----------------

Enter initial location (A/B): A
Enter status of room A (CLEAN/DIRT): DIRT
Enter status of room B (CLEAN/DIRT): CLEAN
Current location: A, Status: DIRT
Sucked dirt at location A
Moved to location B
Current location: B, Status: CLEAN
Moved to location A
Both rooms are clean. Total cost: 1.

------------------------------------------------

Enter initial location (A/B): B
Enter status of room A (CLEAN/DIRT): CLEAN
Enter status of room B (CLEAN/DIRT): DIRT
Current location: B, Status: DIRT
Sucked dirt at location B
Moved to location A
Current location: A, Status: CLEAN
Moved to location B
Both rooms are clean. Total cost: 1.

------------------------------------------------

Enter initial location (A/B): A
Enter status of room A (CLEAN/DIRT): DIRT
Enter status of room B (CLEAN/DIRT): DIRT
Current location: A, Status: DIRT
Sucked dirt at location A
Moved to location B
Current location: B, Status: DIRT
Sucked dirt at location B
Moved to location A
Both rooms are clean. Total cost: 2.

------------------------------------------------

Enter initial location (A/B): B
Enter status of room A (CLEAN/DIRT): CLEAN
Enter status of room B (CLEAN/DIRT): CLEAN
Current location: B, Status: CLEAN
Moved to location A
Current location: A, Status: CLEAN
Moved to location B
Both rooms are clean. Total cost: 0.

"""