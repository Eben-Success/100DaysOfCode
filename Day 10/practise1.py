# Funciton with output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide any valid inputs"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


f_name = input("What is your first name:\n")
l_name = input("What is your last name:\n")

print(format_name(f_name, l_name))
