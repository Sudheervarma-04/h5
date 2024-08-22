import datetime

class ChargingStation:
    def __init__(self, name, location, charging_type, available_slots):
        self.name = name
        self.location = location
        self.charging_type = charging_type  # e.g., 'fast', 'normal'
        self.available_slots = available_slots  # List of available time slots

    def book_slot(self, time_slot):
        if time_slot in self.available_slots:
            self.available_slots.remove(time_slot)
            print(f"Slot {time_slot} booked successfully at {self.name}.")
        else:
            print(f"Slot {time_slot} is not available at {self.name}.")

class ChargingSystem:
    def __init__(self):
        self.stations = []

    def add_station(self, station):
        self.stations.append(station)

    def find_stations(self, location=None, charging_type=None):
        results = self.stations
        if location:
            results = [station for station in results if station.location == location]
        if charging_type:
            results = [station for station in results if station.charging_type == charging_type]
        return results

    def display_stations(self, stations):
        if not stations:
            print("No stations found.")
            return
        for i, station in enumerate(stations):
            print(f"{i + 1}. {station.name} - {station.location} - {station.charging_type}")
            print(f"   Available Slots: {', '.join(station.available_slots)}")

    def book_slot_at_station(self, station_index, time_slot):
        if 0 <= station_index < len(self.stations):
            self.stations[station_index].book_slot(time_slot)
        else:
            print("Invalid station selection.")


def main():
    # Initialize the system and add some charging stations
    system = ChargingSystem()

    station1 = ChargingStation(
        name="GreenCharge Central",
        location="Vizag",
        charging_type="fast",
        available_slots=["10:00", "11:00", "12:00", "14:00"]
    )

    station2 = ChargingStation(
        name="EcoCharge West",
        location="Vizianagaram",
        charging_type="normal",
        available_slots=["09:00", "11:00", "15:00"]
    )

    station3 = ChargingStation(
        name="QuickCharge North",
        location="Vijayawada",
        charging_type="fast",
        available_slots=["08:00", "10:00", "12:00", "16:00"]
    )

    system.add_station(station1)
    system.add_station(station2)
    system.add_station(station3)

    while True:
        print("\nWelcome to the EV Charging Station Finder!")
        print("1. Find Charging Stations")
        print("2. Book a Charging Slot")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            location = input("Enter location to filter by (or leave empty to skip): ")
            charging_type = input("Enter charging type to filter by (fast/normal or leave empty to skip): ")
            found_stations = system.find_stations(location, charging_type)
            system.display_stations(found_stations)
        
        elif choice == '2':
            station_index = int(input("Enter the station number to book at: ")) - 1
            time_slot = input("Enter the time slot to book (e.g., 10:00): ")
            system.book_slot_at_station(station_index, time_slot)

        elif choice == '3':
            print("Thank you for using the EV Charging Station Finder. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
