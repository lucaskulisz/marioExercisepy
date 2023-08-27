def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 8:
                return value
            else:
                print("Please enter a positive integer between 1 and 8 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def main():
    height = get_int("Height: ")

    for i in range(height):
        spaces = " " * (height - i - 1)
        hashes_left = "#" * (i + 1)
        hashes_right = "#" * (i + 1)
        gap = " " * 2

        print(f"{spaces}{hashes_left}{gap}{hashes_right}")


if __name__ == "__main__":
    main()
