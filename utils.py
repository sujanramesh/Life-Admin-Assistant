def get_valid_input(prompt, min_val=None, max_val=None, allow_float=False):
    
    while True:
        try:
            user_input = input(prompt).strip()

            
            if not user_input:
                print("Input cannot be empty.")
                continue

            
            value = float(user_input) if allow_float else int(user_input)

            
            if min_val is not None and value < min_val:
                print(f"Minimum allowed is {min_val}.")
                continue

            if max_val is not None and value > max_val:
                print(f"Maximum allowed is {max_val}.")
                continue

            return value

        except ValueError:
            expected = "a number" if allow_float else "a whole number"
            print(f"Please enter {expected}.")