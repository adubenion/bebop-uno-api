class User:

    in_game = False

    def __init__(self, id, username, wins, losses):
        self.id = id
        self.username = username
        self.wins = wins
        self.losses = losses

    def get_users():
        success = "I got all the users!"
        return success

    def get_user (id):
        success = f"I got one user! the id is {id}"
        return success

    def create_user():
        success = "I just made a user!"
        return success

    def update_user():
        success = "I just updated a user!"
        return success
        
    def delete_user():
        success = "I just deleted a user!"
        return success