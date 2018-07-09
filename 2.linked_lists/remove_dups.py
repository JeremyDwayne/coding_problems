"""
 Cracking the Coding Interview
 Excercise solved by Jeremy Winterberg
 08/07/18
 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
     How would you solve this problem without a temp buffer?
"""

from node import linked_list, node


def find_dups(llist):
    """
        finds duplicate values in linked list and removes them
    """
    d = dict()
    n = llist.head
    d[n.value] = 1
    while n.next is not None:
        if n.next.value in d:
            print("Duplicate found: " + str(n.next.value))
            n.next = n.next.next
        else:
            d[n.next.value] = 1
        n = n.next


def main():
    head = node()
    head.value = 0
    llist = linked_list()
    llist.head = head
    temp_node = head
    for i in range(1, 11):
        llist.add(temp_node, i)
        temp_node = temp_node.next

    temp_node = llist.head
    llist.add(temp_node, 5)

    find_dups(llist)
    llist.printl(llist.head)


main()
