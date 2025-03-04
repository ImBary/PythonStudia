from itertools import permutations

def unique_permutations(perms):
    return list(map(list, set(permutations(perms))))

# Przykład użycia
perms = [1, 2, 2]
print(unique_permutations(perms))