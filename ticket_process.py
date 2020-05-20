from time import sleep

TICKET_PRICE = 10

tickets_remaining = 100
name=""

def clear():
    sleep(2)
    print("\033[H\033[J")

# Gather the user's name and assign it to a new var
def get_name():
    user_name= input("Please enter your name:  ")
    return (user_name)

# Gather the user's name and assign it to a new var
def purchase_info(name):
    print("Welcome {}.".format(name))
    while True:
        try:
            requested_tickets=input("How many tickets would you like?")
            requested_tickets =int(requested_tickets)
            while requested_tickets > tickets_remaining:
                print("Sorry there are only {} tickets available.".format(tickets_remaining))
                requested_tickets=input("How many tickets would you like?")
                requested_tickets =int(requested_tickets)
            break

        except ValueError:
            print("Oops!  That was not a valid number.")

    print("Number of requested tickets" and requested_tickets)    
    requested_tickets=int(requested_tickets)
    return(requested_tickets)


#Purchase confirmation, allows for cancelation.    
def confirm_msg(number_of_tickets, price_of_tickets, tickets_remaining):
    confirmation = input("You are purchasing {} tickets at ${} each.  Your total is ${}.  Please press 'Y' to confirm, 'E' to edit, or 'C' to cancel.".format(number_of_tickets, TICKET_PRICE, price_of_tickets))
    return(confirmation)

#Full ticket purchasing 
def purchase_tickets(tickets_remaining,name):
    print("Hurry there are only {} tickets remaining".format(tickets_remaining))
    if name == "":
      name=get_name()
    number_of_tickets=purchase_info(name)
    price_of_tickets = number_of_tickets * TICKET_PRICE
    confirm_state=confirm_msg(number_of_tickets, price_of_tickets,tickets_remaining)
    
    if confirm_state.upper() == "C":
        cancel= input("Are you sure you want to cancel? Press 'Y' to cancel or any other key to go back.")
        if cancel.upper() == "Y":
            print("Purchase cancelled.  Have a nice day.")
            confirm_state=""
            clear()
        else:
            confirm_state=confirm_msg(number_of_tickets, price_of_tickets,tickets_remaining)
        
    if confirm_state.upper() == "Y":
        print("Thank you. You purchased {} tickets for ${}.".format(number_of_tickets, price_of_tickets))
        
    if confirm_state.upper() == "E":
        clear()
        number_of_tickets = 0
        purchase_tickets(tickets_remaining, name)

    return(tickets_remaining-number_of_tickets)    
       
# Checks to see if tickets are sold out, if they are ends program
while tickets_remaining >0:
    name=""
    tickets_remaining = purchase_tickets(tickets_remaining,name)
    clear()
print("Sorry, this event is sold out.")