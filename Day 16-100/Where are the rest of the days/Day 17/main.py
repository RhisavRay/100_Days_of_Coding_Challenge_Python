class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0

user1 = User(1, "user1")

print(user1.user_id)
print(user1.username)
print(user1.followers)