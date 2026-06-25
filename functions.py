def find_max(numbers):
    return max(numbers)

nums = [10, 45, 23, 67, 12]
print("Maximum:", find_max(nums))

#problem

movies = {
    "Leo": {"price": 200, "seats": 50},
    "Amaran": {"price": 180, "seats": 40},
    "Dragon": {"price": 150, "seats": 30}
}

def book_movie(movie_name, tickets):

    if movie_name not in movies:
        return "Movie not found"

    available_seats = movies[movie_name]["seats"]

    if tickets > available_seats:
        return "Seats not available"

    total_amount = tickets * movies[movie_name]["price"]

    movies[movie_name]["seats"] -= tickets

    return (
        f"\nBooking Successful!\n"
        f"Movie: {movie_name}\n"
        f"Tickets Booked: {tickets}\n"
        f"Total Amount: ₹{total_amount}\n"
        f"Remaining Seats: {movies[movie_name]['seats']}"
    )


movie = input("Enter Movie Name: ")
tickets = int(input("Enter Number of Tickets: "))

print(book_movie(movie, tickets))