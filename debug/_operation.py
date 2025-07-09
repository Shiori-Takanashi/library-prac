def debug_operation():
    the_number = None
    the_number = 10
    print(f"The number is now: {the_number}")


if __name__ == "__main__":
    try:
        debug_operation()
    except TypeError as e:
        print(f"An error occurred: {e}")
        print("It seems like 'the_number' was not initialized properly.")
        print(
            "Please ensure that 'the_number' is assigned a value before performing operations on it."
        )
