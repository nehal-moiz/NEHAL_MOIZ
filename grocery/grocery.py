dict = {}

while True:

    try:

        # Get user input

        grocery = input()

        # Check if grocery is in dict

        if grocery in dict:

            # Create new value for key

            dict_val = dict[grocery] + 1

            # Replace old key's value with new one

            dict[grocery] = dict_val

        else:

            # Create new key and assign value

            dict[grocery] = 1

    except EOFError:

        print()

        # Print all the items in alphabetical order

        for i in sorted(dict):

            key = i.upper()

            value = dict[i]

            print(f'{value} {key}')

        # Stop while loop

        break
