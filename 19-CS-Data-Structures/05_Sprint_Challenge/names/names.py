import time


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

## bad solution to fix, O(n ^ 2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

## better solution
def merge_lists(l1, l2):
    if not isinstance(l1, list):
        raise Exception(f'{l1} is not a list')
    if not isinstance(l2, list):
        raise Exception(f'{l2} is not a list')

    merged_l = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            merged_l.append(l1.pop(0))
        else:
            merged_l.append(l2.pop(0))
    return merged_l + l1 + l2


def merge_sort(l):
    if len(l) < 2:
        return l

    mid_i = len(l) // 2
    l1, l2 = merge_sort(l[:mid_i]), merge_sort(l[mid_i:])
    return merge_lists(l1, l2)


def get_dupes(l1, l2):
    duplicates = []
    l1_i, l2_i = 0, 0
    while l1_i < len(l1) - 1 or l2_i < len(l2) - 1:
        if l1[l1_i] < l2[l2_i]:
            l1_i += 1
        elif l2[l2_i] < l1[l1_i]:
            l2_i += 1
        else:
            duplicates.append(l1[l1_i])
            l1_i += 1
            l2_i += 1

    return duplicates

start_time = time.time()
duplicates = get_dupes(merge_sort(names_1), merge_sort(names_2))
end_time = time.time()
print(
    "---- Merge Sort ----", 
    f"{len(duplicates)} duplicates:",
    f"{', '.join(duplicates)}",
    f"runtime: {end_time - start_time} seconds",
    sep='\n\n'
)

## best solution
from binary_search_tree import BinarySearchTreeNode

start_time = time.time()

BST = BinarySearchTreeNode(names_1[0])
for name in names_1[1:]:
    BST.insert(name)

duplicates = []
for name in names_2:
    if BST.contains(name):
        duplicates.append(name)

end_time = time.time()

print(
    "---- Merge Sort ----", 
    f"{len(duplicates)} duplicates:",
    f"{', '.join(duplicates)}",
    f"runtime: {end_time - start_time} seconds",
    sep='\n\n'
)