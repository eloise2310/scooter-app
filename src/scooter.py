# scooter.py

class Scooter:
    next_serial = 1  # Class variable for tracking the serial number

    def __init__(self, station):
        self.station = station  # Station where the scooter is located
        self.checked_out_user = None  # The user who has rented the scooter
        self.serial = Scooter.next_serial  # Unique serial number for each scooter
        Scooter.next_serial += 1  # Increment the serial number for the next scooter
        self.charge = 100  # Initial charge percentage
        self.is_broken = False  # Track if the scooter is broken

    def rent(self, user):
        if self.charge < 20:
            raise ValueError("Scooter needs charging.")
        elif self.is_broken:
            raise ValueError("Scooter needs repair.")
        else:
            self.station = None  # Remove scooter from station since it's rented
            self.checked_out_user = user

    def dock(self, station):
        self.station = station  # Dock the scooter at a new station
        self.checked_out_user = None  # Remove the checked-out user
