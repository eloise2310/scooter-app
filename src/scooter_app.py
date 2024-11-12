# scooter_app.py

from src.user import User
from src.scooter import Scooter

class ScooterApp:
    def __init__(self, stations=None, registered_users=None):
        # Initialize with some default stations if none provided
        self.stations = stations or {
            'station1': [],
            'station2': [],
            'station3': []
        }
        self.registered_users = registered_users or {}

    def register_user(self, username, password, age):
        if username in self.registered_users:
            raise ValueError("User already registered.")
        if age < 18:
            raise ValueError("Too young to register.")
        
        new_user = User(username, password, age)
        self.registered_users[username] = new_user
        print(f"{username} has been registered.")
        return new_user

    def login_user(self, username, password):
        user = self.registered_users.get(username)
        if not user:
            raise ValueError("Username or password is incorrect.")
        user.login(password)
        return f"{username} has been logged in."

    def logout_user(self, username):
        user = self.registered_users.get(username)
        if not user:
            raise ValueError("No such user is logged in.")
        user.logout()
        return f"{username} has been logged out."

    def create_scooter(self, station):
        if station not in self.stations:
            raise ValueError("No such station.")
        new_scooter = Scooter(station)
        self.stations[station].append(new_scooter)
        return f"Created new scooter at {station}: {new_scooter}"

    def dock_scooter(self, scooter, station):
        if station not in self.stations:
            raise ValueError("No such station.")
        if scooter.station == station:
            raise ValueError("Scooter is already at the station.")
        scooter.dock(station)
        self.stations[station].append(scooter)
        return f"Scooter docked at {station}: {scooter}"

    def rent_scooter(self, scooter, user):
        if scooter.station is None:
            raise ValueError("Scooter is already rented.")
        if scooter.station not in self.stations:
            raise ValueError("No such station.")
        
        for i, s in enumerate(self.stations[scooter.station]):
            if s == scooter:
                self.stations[scooter.station].pop(i)
                scooter.rent(user)
                print(f"Scooter rented to {user.username}.")
                return
        raise ValueError("Scooter not found at the station.")
  