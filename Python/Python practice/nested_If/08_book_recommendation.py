age = int(input("Enter age: "))
genre = input("Enter genre: ").strip().lower()

if age < 18:
    if genre == "fantasy":
        print("Recommended book: Harry Potter")
    elif genre == "mystery":
        print("Recommended book: Nancy Drew")
    elif genre == "science fiction":
        print("Recommended book: The Giver")
    else:
        print("No recommendation available")
else:
    if genre == "mystery":
        print("Recommended book: Sherlock Holmes")
    elif genre == "fantasy":
        print("Recommended book: The Hobbit")
    elif genre == "science fiction":
        print("Recommended book: Dune")
    else:
        print("No recommendation available")
