with open("data_cleaning.txt", "r") as file:
    for line in file:
        if line.strip():  # Check if the line is not empty
            cleaned_line = line.strip()  # Remove extra spaces and newlines
            print(cleaned_line.lower())  # Convert to lowercase and print