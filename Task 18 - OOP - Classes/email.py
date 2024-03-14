class Email:
    """
    The `Email` class represents an email with attributes for email address, subject line, email
    content, and a method to mark the email as read.
    """

    has_been_read = False


    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    def mark_as_read(self):
        """
        The function `mark_as_read` sets the `has_been_read` attribute to True.
        """
        self.has_been_read = True



def populate_inbox(inbox):
    """
    The function `populate_inbox` creates 3 sample emails and adds them to the provided `inbox` list.
    
    :param inbox: The `inbox` parameter is a list that contains email objects. The `populate_inbox`
    function creates three sample email objects (`email1`, `email2`, `email3`) and adds them to the
    `inbox` list using the `extend` method
    """
    email1 = Email("sender1@example.com", "Welcome to HyperionDev!", "Hello, and welcome!")
    email2 = Email("sender2@example.com", "Great work on the bootcamp!", "Keep up the good work!")
    email3 = Email("sender3@example.com", "Your excellent marks!", "Congratulations on your achievements!")
    
    inbox.extend([email1, email2, email3])


def list_emails(inbox):
    """
    The function `list_emails` iterates through an inbox of emails and prints the email address and
    subject line of each email along with its index.
    
    :param inbox: The `list_emails` function is designed to iterate over an `inbox` and
    print out the email addresses and subject lines of each email in the inbox.
    """
    for index, email in enumerate(inbox):
        print(f"{index} - From: {email.email_address} - Subject: {email.subject_line}")


# Create a function which displays a selected email. 
def read_email(inbox):
    """
    The function `read_email` takes an inbox list as input, prompts the user to enter the index of the
    email they want to read, displays the email details if the index is valid, and marks the email as
    read.
    
    :param inbox: The `read_email` function takes an `inbox` parameter and prompts the user to enter
    the index of the email they want to read from the inbox. It then checks if the index is within
    the valid range of the inbox length and displays the email details if the index is valid, and marks
    the email as read.
    """
    index = int(input("Enter the index of the email you want to read: "))
    if 0 <= index < len(inbox):
        email = inbox[index]

        print(f"\n|  From:  |  {email.email_address}")
        print_line()
        print(f"| Subject |  {email.subject_line}")
        print_line()
        print(f"| Content |  {email.email_content}")
        print_line()

        email.mark_as_read()
        print(f"\nEmail from {email.email_address} has been marked as read.")
    else:
        print("Invalid index.")


def print_line():
    """
    The function 'print_line()' prints a line of 80 dashes.
    """
    print("-"*80)



def main():
    """
    The main function simulates an email inbox where users can read emails, view unread emails,
    or quitthe application.
    """
    inbox = []

    populate_inbox(inbox)

    print("\n\t\tHello! Welcome to the Email Simulator\n")
    print_line()

    while True:
        user_choice = int(input('''\nWould you like to: 
                                
    1. Read an email
    2. View unread emails
    3. Quit application                        
                                
    Enter your choice:  ''')) 
        print_line()   

        if user_choice == 1:
            read_email(inbox)

        elif user_choice == 2:
            unread_emails = [email for email in inbox if not email.has_been_read]
            if len(unread_emails) == 0:
                print("\nNo unread emails.")
            else:
                print("\nUnread emails:\n")
                list_emails(unread_emails)

        elif user_choice == 3:
            print("Quitting application. Goodbye!\n")
            break

        else:
            print("Oops - Invalid choice! Please try again.")


if __name__ == "__main__":
    main()