
import math

rides = []


# Function 1: Display Menu
def display_menu():
    print("\n========== CAB BOOKING SYSTEM ==========")
    print("1. Book Ride")
    print("2. View Ride History")
    print("3. Search Ride")
    print("4. Revenue Report")
    print("5. Longest Ride")
    print("6. Highest Fare")
    print("7. Daily Summary")
    print("8. Exit")
    print("========================================")


# Validate Text
def get_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Error: This field cannot be empty.")


# Validate Customer Name
def get_name(prompt):
    while True:
        name = get_text(prompt)

        if any(char.isalpha() for char in name) and all(
            char.isalpha() or char in " .'-" for char in name
        ):
            return name

        print("Error: Enter a valid name using letters and spaces.")


# Validate Distance
def get_distance():
    while True:
        try:
            distance = float(input("Distance (KM): ").strip())

            if math.isfinite(distance) and distance > 0:
                return distance

            print("Error: Distance must be a positive finite number.")

        except ValueError:
            print("Error: Enter a valid numeric distance.")


# Function 2: Calculate Fare
def calculate_fare(distance):
    if (
        not isinstance(distance, (int, float))
        or not math.isfinite(distance)
        or distance <= 0
    ):
        raise ValueError("Distance must be a positive finite number.")

    if distance <= 5:
        rate = 15
    elif distance <= 15:
        rate = 12
    else:
        rate = 10

    return 50 + distance * rate


# Function 3: Book Ride
def book_ride():
    print("\n========== BOOK A RIDE ==========")

    name = get_name("Customer Name: ")
    pickup = get_text("Pickup Location: ")

    while True:
        destination = get_text("Destination: ")

        if destination.casefold() != pickup.casefold():
            break

        print("Error: Pickup and destination cannot be the same.")

    distance = get_distance()
    fare = calculate_fare(distance)

    ride = {
        "name": name,
        "pickup": pickup,
        "destination": destination,
        "distance": distance,
        "fare": fare
    }

    rides.append(ride)

    print("\nRide booked successfully!")
    show_ride(ride)


# Display Ride Details
def show_ride(ride):
    print("Customer Name:", ride["name"])
    print("Pickup:", ride["pickup"])
    print("Destination:", ride["destination"])
    print(f"Distance: {ride['distance']:g} KM")
    print(f"Fare: Rs.{ride['fare']:.2f}")
    print("----------------------------------------")


# Function 4: View Ride History
def view_rides():
    if not rides:
        print("\nNo rides booked yet.")
        return

    print("\n========== RIDE HISTORY ==========")

    for number, ride in enumerate(rides, start=1):
        print(f"\nRide Number: {number}")
        show_ride(ride)


# Function 5: Search Ride
def search_ride():
    name = get_name("Enter Customer Name: ")

    matches = [
        ride for ride in rides
        if ride["name"].casefold() == name.casefold()
    ]

    if not matches:
        print("No ride found for this customer.")
        return

    print(f"\nFound {len(matches)} ride(s):")

    for ride in matches:
        show_ride(ride)


# Function 6: Revenue Report
def revenue_report():
    if not rides:
        print("\nNo rides available for the revenue report.")
        return

    total = len(rides)
    revenue = sum(ride["fare"] for ride in rides)

    print("\n========== REVENUE REPORT ==========")
    print("Total Rides:", total)
    print(f"Total Revenue: Rs.{revenue:.2f}")
    print(f"Average Fare: Rs.{revenue / total:.2f}")


# Bonus 1: Longest Ride
def longest_ride():
    if not rides:
        print("\nNo rides available.")
        return

    ride = max(rides, key=lambda item: item["distance"])

    print("\n========== LONGEST RIDE ==========")
    print("Customer Name:", ride["name"])
    print(f"Distance: {ride['distance']:g} KM")


# Bonus 2: Highest Fare
def highest_fare():
    if not rides:
        print("\nNo rides available.")
        return

    ride = max(rides, key=lambda item: item["fare"])

    print("\n========== HIGHEST FARE ==========")
    print("Customer Name:", ride["name"])
    print(f"Highest Fare: Rs.{ride['fare']:.2f}")


# Bonus 3: Daily Summary
def daily_summary():
    if not rides:
        print("\nNo rides available for the daily summary.")
        return

    total = len(rides)
    revenue = sum(ride["fare"] for ride in rides)
    distance = sum(ride["distance"] for ride in rides)
    highest = max(ride["fare"] for ride in rides)

    print("\n========== DAILY REPORT ==========")
    print("Total Rides:", total)
    print(f"Total Revenue: Rs.{revenue:.2f}")
    print(f"Average Distance: {distance / total:.2f} KM")
    print(f"Highest Fare: Rs.{highest:.2f}")
    print("==================================")


# Main Application
def main():
    actions = {
        "1": book_ride,
        "2": view_rides,
        "3": search_ride,
        "4": revenue_report,
        "5": longest_ride,
        "6": highest_fare,
        "7": daily_summary
    }

    while True:
        display_menu()

        choice = input("Enter Your Choice (1-8): ").strip()

        if choice == "8":
            print("Thank you for using the Cab Booking System!")
            break

        action = actions.get(choice)

        if action is None:
            print("Invalid choice! Please enter a number from 1 to 8.")
        else:
            action()


# Run Application
if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nProgram closed.")
