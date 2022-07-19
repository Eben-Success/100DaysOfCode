word_list = []

teams = 5
while teams < 6:
    teams = input("\nEnter 5 football teams\n")
    for team in teams:
        word_list += teams

    print(word_list)

