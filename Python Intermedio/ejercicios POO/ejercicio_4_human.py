class Head:
    def __init__(self):
        pass


class Hand:
    def __init__(self):
        pass


class Arm:
    def __init__(self, hand):
        self.hand = hand


class Feet:
    def __init__(self):
        pass


class Leg:
    def __init__(self, feet):
        self.feet = feet


class Torso:
    def __init__(self, head, right_arm, left_arm):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm


class Human:
    def __init__(self, name):
        self.name = name

        head = Head()

        right_hand = Hand()
        right_arm = Arm(right_hand)

        left_hand = Hand()
        left_arm = Arm(left_hand)

        right_feet = Feet()
        right_leg = Leg(right_feet)

        left_feet = Feet()
        left_leg = Leg(left_feet)

        self.torso = Torso(head, right_arm, left_arm)
        self.right_leg = right_leg
        self.left_leg = left_leg


name = input("Enter the human's name: ").strip()
person = Human(name)

print(f"\nHuman: {person.name}")
print(f"  Torso: {type(person.torso).__name__}")
print(f"    Head: {type(person.torso.head).__name__}")
print(f"    Right arm: {type(person.torso.right_arm).__name__}")
print(f"      Right hand: {type(person.torso.right_arm.hand).__name__}")
print(f"    Left arm: {type(person.torso.left_arm).__name__}")
print(f"      Left hand: {type(person.torso.left_arm.hand).__name__}")
print(f"  Right leg: {type(person.right_leg).__name__}")
print(f"    Right feet: {type(person.right_leg.feet).__name__}")
print(f"  Left leg: {type(person.left_leg).__name__}")
print(f"    Left feet: {type(person.left_leg.feet).__name__}")
