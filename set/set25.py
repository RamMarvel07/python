user1_friends = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
user2_friends = {"Charlie", "Diana", "Frank", "Grace", "Bob"}
print("User 1 friends:", user1_friends)
print("User 2 friends:", user2_friends)
mutual_friends   = user1_friends.intersection(user2_friends)
unique_to_user1  = user1_friends.difference(user2_friends)
unique_to_user2  = user2_friends.difference(user1_friends)
total_friends    = user1_friends.union(user2_friends)
print("\nMutual friends           :", mutual_friends)
print("Friends unique to User 1 :", unique_to_user1)
print("Friends unique to User 2 :", unique_to_user2)
print("Total unique friends      :", total_friends)
