# RECURSION APPROACH
def print_depth_recur(data, level=1):
    """
    [Uses recursion to find depth of key it uses O(n^2) time complexity as the recursion depends on the number of keys and a for loop.
    If the depth level is more than the systems recursion limit, it will give error. However, this looks simpler and easy to read.]

    Args:
        data ([dict]): [takes dictionary]
        level (int, optional): [This is the value that gets incremented]. Defaults to 1.

    Returns:
        [func]: [return self function to allow the recursion to happen]
    """
    for k, v in data.items():
        print(k, level)
        if isinstance(v, dict):
            return print_depth_recur(v, level=level+1)


# ITERATIVE APPROACH
def print_depth(data):
    """
    [This solves the issue of exceeding the recursive limit for bigger tree structure by using stack. 
    This also uses O(n^2) time complexity as there's two loops] 

    Args:
        data ([dict]): [takes dictionary]
    """
    stack = [(data, list(data.keys()))]
    while stack:
        c, keys = stack.pop()
        while keys:
            k, keys = keys[0], keys[1:]
            print(k, len(stack)+1)
            v = c[k]
            if isinstance(v, dict):
                stack.append((c, keys))
                stack.append((v, list(v.keys())))
                break


# TEST CASE
a = {
    "key1": 1,
    "key2": {"key3": 1,
             "key4": {"key5": 4
                      }
             }
}

print_depth_recur(a)
print_depth(a)
