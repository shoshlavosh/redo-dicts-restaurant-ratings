def sort_ratings(file):
    """Restaurant rating lister."""

    ratings_file = open(file)

    ratings_dict = {}

    new_restaurant = input("Please enter a restaurant name: ")
    new_rating = input(f"Please enter a rating for {new_restaurant}: ")

    ratings_dict[new_restaurant] = new_rating #add user input to the dictionary

    print()

    for line in ratings_file:
        #next 3 lines are taken from the solution
        line = line.rstrip()

        restaurant, score = line.split(":")

        ratings_dict[restaurant] = score

    # print(ratings_dict)


    sorted_ratings = sorted(ratings_dict.items())

    for restaurant, rating in sorted_ratings:
        print(f"{restaurant} is rated at {rating}.")



sort_ratings("scores.txt")

