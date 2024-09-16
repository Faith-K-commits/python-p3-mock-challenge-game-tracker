class Game:
    def __init__(self, title):
        # Set the title (ensuring immutability)
        self.title = title
        self._results = []  # Store all results associated with this game

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Title cannot be changed once set.")
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string.")
        self._title = value

    def results(self):
        # Returns a list of all results for the game
        return self._results

    def players(self):
        # Returns a unique list of all players who have played this game
        return list(set([result.player for result in self._results]))

    def average_score(self, player):
        # Returns the average score of a specific player for this game
        player_scores = [result.score for result in self._results if result.player == player]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0


class Player:
    def __init__(self, username):
        self.username = username
        self._results = []  # Store all results associated with this player

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not isinstance(value, str):
            raise ValueError("Username must be a string.")
        if not 2 <= len(value) <= 16:
            raise ValueError("Username must be between 2 and 16 characters long.")
        self._username = value

    def results(self):
        # Returns a list of all results for this player
        return self._results

    def games_played(self):
        # Returns a unique list of games the player has played
        return list(set([result.game for result in self._results]))

    def played_game(self, game):
        # Returns True if the player has played the game, False otherwise
        return game in self.games_played()

    def num_times_played(self, game):
        # Returns the number of times the player has played the game
        return sum(1 for result in self._results if result.game == game)


class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        
        # Register result in both player and game
        player._results.append(self)
        game._results.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if hasattr(self, '_score'):
            raise AttributeError("Score cannot be changed once set.")
        if not isinstance(value, int):
            raise ValueError("Score must be an integer.")
        if not 1 <= value <= 5000:
            raise ValueError("Score must be between 1 and 5000.")
        self._score = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if not isinstance(value, Player):
            raise ValueError("Must be an instance of Player.")
        self._player = value

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        if not isinstance(value, Game):
            raise ValueError("Must be an instance of Game.")
        self._game = value
