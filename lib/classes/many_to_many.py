class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0 and not hasattr(self, 'title'):
            self._title = title
        # else:
        #     raise ValueError('title must be non-empty string and title attribute is not initialized yet.')

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in Result.all if result.game == self})

    def average_score(self, player):
        count = 0
        sum = 0
        for result in Result.all:
            if result.game == self and result.player == player:
                count += 1
                sum += result.score
        return sum / count

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise ValueError('username must be a string with its length in between 2 and 16.')

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in Result.all if result.player == self})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        count = 0
        for result in Result.all:
            if result.player == self and result.game == game:
                count += 1
        return count
    
    @classmethod
    def highest_scored(cls, game):
        player_stats = {}
        for result in Result.all:
            if result.game == game:
                stat = player_stats.get(result.player, {})
                player_stats[result.player] = {
                    'sum': stat.get('sum', 0) + result.score,
                    'count': stat.get('count', 0) + 1
                }

        highest_avg = -1
        highest_avg_player = None
        for player in player_stats:
            avg = player_stats[player]['sum'] / player_stats[player]['count']
            if avg > highest_avg:
                highest_avg = avg
                highest_avg_player = player
        
        return highest_avg_player

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score
        # else:
        #     raise ValueError('score must be an integer with its value in between 1 and 5000. And score attribute is not initialized yet.')
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #     raise ValueError('player must be an instance of Player')
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        # else:
        #     raise ValueError('game must be an instance of Game')
    
