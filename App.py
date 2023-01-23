from constants import TEAMS, PLAYERS
import copy


players = copy.copy(PLAYERS)
teams = copy.copy(TEAMS)
data = players, teams


def clean_data(players):
	cleaned_players_list = []
	for player in PLAYERS:
		cleaned = {}
		cleaned["name"] = player["name"]
		cleaned["guardians"] = player["guardians"]
		if player["experience"] == "YES":
			cleaned["experience"] = True
		elif player["experience"] == "NO":
			cleaned["experience"] = False
		split_height = player["height"].split(" ")
		cleaned["height"] = int(split_height[0])
		cleaned_players_list.append(cleaned)
	return cleaned_players_list


def balance_teams(players, teams):
	num_players_team = int(len(PLAYERS) / len(TEAMS))
	balanced_teams = []
	for team in teams:
		players_on_team = players[:num_players_team]
		players = players[num_players_team:]
		balanced_teams.append({
			"team": team,
			"players": players_on_team
		})

	return num_players_team, balanced_teams


def main():
	print("BASKETBALL TEAM STATS TOOL")

	print("\n-----MENU-----")
	print("\nHere are your choices:\n A) Display Team Stats \n B) Quit")
	menu = ['A', 'B', 'a', 'b']
	option = str(input("\nEnter your option: "))

	while option not in menu:
		option = str(input("Oops, that´s not a valid answer. Enter your option: "))

	if option == "A" or option == "a":
		print("\nA) {} \nB) {} \nC) {}".format(teams[0], teams[1], teams[2]))
		choose_team = ["A", "B", "C", "a", "b", "c"]
		team_option = str(input("\nEnter your option:  "))

		while team_option not in choose_team:
			team_option = str(input("Oops, that´s not a valid answer. Enter your option: "))

		if team_option == "A" or team_option == "a":
			team_number = 0
		elif team_option == 'B' or team_option == "b":
			team_number = 1
		elif team_option == "C" or team_option == "c":
			team_number = 2
		else:
			exit()
	else:
		exit()


	chosen_team = teams[team_number]
	num_players_team, balanced_teams = balance_teams(clean_data(players), teams)

	for team in balanced_teams:
		if team["team"] == chosen_team:
			print("\nTeam: {} Stats".format(chosen_team))
			print("-------------------------------")
			print("Total players: {}".format(num_players_team))

			player_names = []
			for player in team["players"]:
				player_names.append(player["name"])
			print("\nPlayers on Team: \n{}".format(player_names))


if __name__ == "__main__":
    main()
