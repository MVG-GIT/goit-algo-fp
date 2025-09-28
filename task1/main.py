from llist import LinkedList, merge_sorted

ll = LinkedList()
ll.insert_at_end(5)
ll.insert_at_end(3)
ll.insert_at_end(8)
ll.insert_at_end(1)

print("Initial list:")
ll.print_list()

ll.reverse()
print("After reverse:")
ll.print_list()

ll.sort()
print("After sorting:")
ll.print_list()



print("Merging lists")
l1 = LinkedList()
l1.insert_at_end(1)
l1.insert_at_end(4)
l1.insert_at_end(6)
l1.print_list()

l2 = LinkedList()
l2.insert_at_end(2)
l2.insert_at_end(3)
l2.insert_at_end(7)
l2.print_list()


merged = merge_sorted(l1, l2)
print("Merged sorted list:")
merged.print_list()
