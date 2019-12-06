#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length
    ticket_list = []

    for ticket in tickets:
        ticket_list.append(ticket)

    length = 0
    recent = None
    while length < len(tickets):
        for ticket in ticket_list:
            if ticket.source == "NONE":
                route.append(ticket.destination)
                recent = ticket.destination
                ticket_list.remove(ticket)
                length +=1
            else:
                recent = ticket.destination
                next_link = hash_table_retrieve(hashtable, recent.destination)
                route.append(next_link.destination)
                length +=1




    print(type(route))

  

    length = 0
    while length < len(ticket_list):
        for ticket in ticket_list:
            if ticket.source == "NONE":
                route.insert(1, ticket.destination)
                ticket_list.remove(ticket)
                length += 1

            else:
                if ticket.source != "NONE":
                    previous = hash_table_retrieve(hashtable, ticket.destination)
                    #print(previous)
                    route.append(ticket.destination)
                    route.append(ticket.source)
                    ticket_list.remove(ticket)
                    length += 1

                else:
                    print("IS NONE")
                    #route.append(ticket.source)
                    ticket_list.remove(ticket)
                    length += 1

    print(route)
    

    return route
