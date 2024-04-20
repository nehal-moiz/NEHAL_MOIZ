names = []
# Compute a 'while loop' to create infinite loop
while True:
    try:
        # Prompt user for name
        prompt = input('Name: ')
        if len(prompt) != 0:
            names.append(prompt)
            # Define static text that bids fairwell/goodbye to all names in list
            bid = 'Adieu, adieu, to '
        else:orld
            pass
    except EOFError:
        # Print static text on same line as list of names
        print(bid, end='')
        # Compute a 'for loop' to iterate over list of names if no. of names in list is more than 2
        if len(names) > 2:
            for name in names:
                # If name is not last in list then add a comma as separator
                if name is not names[-1]:
                    name += ', '
                # If name is last in list then add 'and' before
                else:
                    name = 'and ' + name
                print(name, end='')
        # If no. of names in list equals two, compute a 'for loop' separate names with one 'and'
        elif len(names) == 2:
            for name in names:
                if name is names[0]:
                    name += ' and '
                print(name, end='')
        # If no. of names in list equals one, compute a 'for loop' without any separator
        elif len(names) == 1:
            for name in names:
                print(name, end='')
        else:
            pass
        print()
        break
