class Guild:
    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player):
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        filtered_players = [p for p in self.list_of_players if p == player]
        if filtered_players:
            return f"Player {player.name} is already in the guild."
        self.list_of_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        filtered_players = [p for p in self.list_of_players if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} is not in the guild."
        player = filtered_players[0]
        self.list_of_players.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        info = f"Guild: {self.name}\n"
        for player in self.list_of_players:
            info += player.player_info()
        return info
