genre = input("Enter genre: ").strip().lower()
age_group = input("Enter age group: ").strip().lower()

if age_group == "child":
    if genre == "animation":
        print("Recommended movie: Toy Story")
    elif genre == "comedy":
        print("Recommended movie: Paddington")
    else:
        print("No recommendation available")
elif age_group == "adult":
    if genre == "comedy":
        print("Recommended movie: The Hangover")
    elif genre == "action":
        print("Recommended movie: Inception")
    else:
        print("No recommendation available")
else:
    print("No recommendation available")
