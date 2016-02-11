__author__ = 'Katherine'

def normalise_data(field):

    # Remove whitespace characters before and after
    field = field.rstrip()

    # Remove spaces in the middle
    field = field.replace (" ", "")
    # Convert to upper case
    field = field.upper()

    return field

def main():

    # Read in reference file
    reference_file = "local_authorities_output_file.csv"

    # Request postcode input from user
    postcode = input("Enter a postcode: ")

    # Standardise postcode format
    postcode = normalise_data(postcode)

    # Open reference file
    with open (reference_file, "r") as file_contents:
        # Loop over each line in file
        for line in file_contents:
            # Split on comma
            line = line.split(",")
            # Standardise postcode format
            line[0] = normalise_data(line[0])
            # Check if it matches user input
            if line[0] == postcode:
                # If it matches, print local authority
                print ("Local authority is", line[2])
                # End loop early
                break
        # If end of loop is reached without finding postcode, print error message
        else: print ("Postcode not found")

if __name__ == "__main__":
    main()
