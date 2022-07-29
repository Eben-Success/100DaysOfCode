# Capitalize names

def format_name():
    f_name = input("Enter yor first name\n").title()
    l_name = input("Enter your last name:\n").title()

    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    else:
        print(f"{f_name}  {l_name}")


format_name()
