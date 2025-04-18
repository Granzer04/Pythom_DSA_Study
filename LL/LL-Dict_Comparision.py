head = {
            "value": 11,
            "next": {
                        "value": 3,
                        "next": {
                                    "value": 23,
                                    "next": {
                                                "value": 7,
                                                "next": None
                                    }
                        }
            }
}

print(head['next']['next']['value'])

# This would only run with a Linked List But similar to what the Dict syntax is
# print(my_linked_list.head.next.next.value)