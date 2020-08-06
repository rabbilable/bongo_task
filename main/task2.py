class Person(object):

    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


def print_depth_recur(data, level=1):
    """
    [Uses recursion to find depth of key it uses O(n^2) time complexity as there's a for loop and a recursion.
    It the depth level is more than the systems recursion limit, it will give error]

    Args:
        data ([dict]): [takes dictionary]
        level (int, optional): [This is the value that gets incremented]. Defaults to 1.

    Returns:
        [func]: [return self function to allow the recursion to happen]
    """
    for k, v in data.items():
        print(k, level)
        if isinstance(data, Person):
            person_details(data, level)
            if isinstance(data.father, Person):
                print_depth_recur(data.father, level+1)
        elif isinstance(v, dict):
            return print_depth_recur(v, level=level+1)


def person_details(person, level):
    fields = ["first_name", "last_name", "father"]
    for field in fields:
        print(f"{person.field} {level}")


# TEST CASE
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)
b = {"key1": 1,
     "key2": {"key3": 1,
              "key4": {"key5": 4,
                       "user": person_b,
                       }
              },
     }

print_depth_recur(b)
