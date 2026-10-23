'''
Create a class movie with the following:
Attributes:
movie_name : name of the movie
total_seats : total seats available in the theater
ticket_price : Price per ticket
booked_seat : starts at 0

methods:
book_tickets(num_tickets) --> books the given number of tickets if enough seats are available, confirm the booking and show the total
                              amount to pay. if not, show "Sorry, not enough seats available"

show_status() --> display movie name, seat available and seat booked so far
'''

class Movie:
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0


    def book_tickets(self, num_of_tickets: int):
        if num_of_tickets > self.total_seats - self.booked_seats:
            print("Sorry, not enough seats available.")
        else:
            self.booked_seats += num_of_tickets
            self.total_seats -= num_of_tickets
            print("Your ticket is booked.")
            print(f"Total price is : {self.ticket_price * num_of_tickets}")


    def show_status(self) -> None:
        print(f"movie name = {self.movie_name}")
        print(f"seats available = {self.total_seats}")
        print(f"Total booked = {self.booked_seats}\n")

movie = Movie("Krish 3", 100, 499)

movie.book_tickets(80)
movie.show_status()
movie.book_tickets(50)
movie.show_status()