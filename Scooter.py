class Scooter:
    next_serial = 1  # Class-level variable to track serial numbers

    def __init__(self, station):
        self.station = station
        self.checked_out_user = None
        self.serial = Scooter.next_serial  # Use class variable to assign serial
        Scooter.next_serial += 1  # Increment the serial number for the next instance
        self.charge = 100
        self.is_broken = False

    def rent(self, user):
        """Rent the scooter to a user."""
        if self.charge < 20:
            raise ValueError("Scooter needs to charge")
        elif self.is_broken:
            raise ValueError("Scooter needs repair")
        else:
            self.station = None
            self.checked_out_user = user

    def dock(self, station):
        """Dock the scooter at a station."""
        self.station = station
        self.checked_out_user = None
