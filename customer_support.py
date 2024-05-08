from abc import ABC, abstractmethod
import random
import string

def generate_id(length = 7):
    # genrating ids for the tickets.
    return "".join(random.choice(seq= string.ascii_letters) for _ in range(length))

class SupportTicket:
    """
    Support ticket class that is created by the users of the application.
    """

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class TicketOrderingStrategy(ABC):
    # abstract class for handeling ordering strategies.
    @abstractmethod
    def create_ordering(self, ticket_list):
    # abstract method for ordering tickets that is implemented by the child classes.
        pass

class FIFOOrderingStrategy(TicketOrderingStrategy):
    # first in first out.
    def create_ordering(self, ticket_list: list[SupportTicket]) -> list[SupportTicket]:
        self.ticket_list = ticket_list
        return self.ticket_list.copy()

class FILOOderingStrategy(TicketOrderingStrategy):
    # first in last out.
    def create_ordering(self, ticket_list: list[SupportTicket]) -> list[SupportTicket]:
        ticket_list.reverse()
        return ticket_list
    
class RandomOderingStrategy(TicketOrderingStrategy):
    # random order.
    def create_ordering(self, ticket_list: list[SupportTicket]) -> list[SupportTicket]:
        ticket_list_copy = ticket_list.copy()
        random.shuffle(ticket_list_copy)
        return ticket_list_copy


class CustomerSupport:
    """
    class that handles creation and processing of support tickets.
    """

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = []
        self.processing_strategy = processing_strategy
    
    def create_ticket(self, customer, issue):
        # creating and adding tickets into the list.
        self.tickets.append(SupportTicket(customer, issue))
    
    def process_tickets(self):
        # Creating ordered list of tickets.
        tickets = self.processing_strategy.create_ordering(self.tickets)

        # if no tickets in the list, nothing to do.
        if len(tickets) == 0:
            print("Nothing to do here, work done!")
            return
        
        # go through the tickets.
        for ticket in tickets:
            self.process_ticket(ticket)
        
    def process_ticket(self, ticket):
        print("==============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==============================")
        

# creating the application.
app = CustomerSupport(RandomOderingStrategy())

# registering few tickets
app.create_ticket('John', 'I am not able to search for 11th season of Game of Thrones.')
app.create_ticket('Jane', "I want my money back!!!")
app.create_ticket('Josh', "How to see if any body has my Netflix login?")

# processing the tickets
app.process_tickets()
