# Problem: Social Graph — friends & mutual friends (design)
#
# Model a social network of people (identified by strings). Support: adding an
# (undirected) friendship "abc"—"xyz", getting a person's friend count, and the
# mutual friends shared between two people.

# Social graph
# people (strings)

# "abc" - "xyz" friends

# person -> count of friends 
# person1 and person2 -> mutual friends

# A - B   B - C
# A , C

# {string : set()}

# ============================================================
# Approach: Hash map + adjacency sets (graph model)
#   build O(E), friend-count O(1), mutual-friends O(deg)
# ============================================================
# social = {name -> Person}; each Person holds a set of friend Persons, and
# buildRelations wires both directions per edge. This is the optimal shape for
# these queries — friend-count is O(1) (set size), mutuals is O(deg) by scanning
# one friend set against the other's membership. BUG as written: self.friends is
# init'd as {} (a dict) but addFriend calls .append (a list method) => raises
# AttributeError. Per the {string: set()} note, make it a set: self.friends =
# set() and self.friends.add(person).
class Person:
    def __init__(self,name):
        self.name=name
        self.friends = {} 
    def addFriend(self,person):
        self.friends.append(person)

    def getFriends(self):
        return len(self.friends)
    
    def getMutualsWith(self,person2):
        mutuals = []
        for friend in self.friends:
            if friend in person2.friends:
                mutuals.append(friend)
        return mutuals


def buildRelations(relations):
    social = {}

    for pa,pb in relations:
        person1 = None
        person2 = None
        if pa not in social:
            person1 = Person(pa)
            social[pa]=person1
        else:
            person1= social[pa]
        if pb not in social:
            person2 = Person(pb)
            social[pb]=person2
        else:
            person2= social[pb]
        person1.addFriend(person2)
        person2.addFriend(person1)
    
