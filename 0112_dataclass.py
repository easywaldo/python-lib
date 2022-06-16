from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str
    age: int
    married: bool = False

user1 = User("easywaldo", 41, True)
user2 = User("easywaldo", 41, True)

print(user1)
print(user2)
print(user1 == user2)


user1.name = "John"