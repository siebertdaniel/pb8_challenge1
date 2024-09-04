from media_factory import MediaFactory

def main():
    # Now let's create some movies!
    # First, we find a production company with the abstract factory
    # We have to specify a genre so the production company knows what type of movie and trailer we want.
    factory = MediaFactory.find_production_company("Action")

    # After they found us a production company, we can create our movie.
    movie = factory.create_movie()

    # Let's see what the movie is about.
    # We start with the movie itself.
    print("# Action Movie:")
    print(movie.display())

    # After that, we can list us all the individual scenes which were used to make this movie
    print("# Action Scenes:")
    for scene in movie.recorded_scenes:
        print(scene)

    # Now, let's create a trailer with the same production studio hat made the movie
    trailer = factory.create_trailer(movie)

    # Now let's see the trailer.
    print("# Action Trailer:")
    print(trailer.display())

    print("#####################################################################################################################################")

    # Great! This movie sure will be a hollywood blockbuster.
    # Let's create another one, using the other concrete factory this time.
    # For that, we call the same abstract company to find us a production company
    second_factory = MediaFactory.find_production_company("Drama")

    # Create a second movie and trailer
    second_movie = second_factory.create_movie()
    second_trailer = second_factory.create_trailer(second_movie)

    # And lastly, see what they are about
    print("# Drama Movie:")
    print(second_movie.display())
    print("# Drama Scenes:")
    for scene in second_movie.recorded_scenes:
        print(scene)
    print("# Drama Trailer:")
    print(second_trailer.display())

    # Great, we did it!
    # Instead of having to talk to the concrete production studios, we talked to the abstract production studio.
    # We still got the same end results (two movies and trailers), without having to worry about creating a drama movie with an action trailer.
    # Neat! Thanks Abstract Factory Pattern!

if __name__ == "__main__":
    main()