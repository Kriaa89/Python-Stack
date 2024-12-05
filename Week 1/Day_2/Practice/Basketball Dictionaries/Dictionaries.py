class Player:
    def __init__(self, new_data):
        self.name = new_data ["name"]
        self.age = new_data ["age"]
        self.position = new_data ["position"]
        self.team = new_data ["team"]
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
player_kevin = Player(jason)
player_kevin = Player(kyrie)

players = [
    {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age":32,"position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age":33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age":32,"position": "Power Foward", "team": "Philidelphia 76ers"},
    {"name": "DeMar DeRozan","age": 32,"position": "Shooting Guard","team": "Chicago Bulls"}
]
new_team = []
for new_data in players:
    new_team.append(Player(new_data))
for player in new_team: # print to verify the loop 
    print(player.name, player.age)

