class UserInput:
    def __init__(self):
        self.exit_keyword = "bye"

    def get_location(self) -> str:
        try:
            location = input("Enter the location to check weather (or 'bye' to exit): ").strip()
            return location
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            return self.exit_keyword

    def should_exit(self, location: str) -> bool:
        return location.lower() == self.exit_keyword.lower()

    def show_welcome_message(self) -> None:
        print("Welcome to the Weather Checker!")
        print("You can check weather for any location.")
        print("Type 'bye' to exit the program.\n")

    def show_goodbye_message(self) -> None:
        print("Thank you for using Weather Checker! Goodbye!")

    def show_invalid_location_message(self) -> None:
        print("Please enter a valid location name.\n")