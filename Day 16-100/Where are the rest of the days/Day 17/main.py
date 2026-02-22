class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User(1, "Patrik")
user2 = User(2, "Spongebob")

print(f"User: {user1.username}\nFollowers: {user1.followers}\nFollowing: {user1.following}\n")
print(f"User: {user2.username}\nFollowers: {user2.followers}\nFollowing: {user2.following}")

user1.follow(user2)
print(f"\n\n{user1.username} followed {user2.username}\n\n")

print(f"User: {user1.username}\nFollowers: {user1.followers}\nFollowing: {user1.following}\n")
print(f"User: {user2.username}\nFollowers: {user2.followers}\nFollowing: {user2.following}")