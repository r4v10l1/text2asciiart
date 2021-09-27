
def main():

    #########################################
    ascii_art_spaces = " "  # Put here the characters you want to replace with " "
    output_file_path = "output.txt"
    #########################################

    text_file_path = input(" Text file path: ")
    ascii_art_file_path = input(" Ascii art file path: ")

    with open(output_file_path, "w") as empty_output_file:  # Clear output.txt
        empty_output_file.write("\n")

    with open(text_file_path, "r") as text_file:
        text = str(text_file.readlines()[0].strip())

    char_pos = 0
    with open(ascii_art_file_path, "r") as ascii_art_file:
        for line in ascii_art_file:
            if not line:
                break
            for char in line:
                if char is ascii_art_spaces:
                    with open("output.txt", "a") as output_file:
                        output_file.write(" ")
                else:
                    with open("output.txt", "a") as output_file:
                        output_file.write(text[char_pos])
                        char_pos += 1
                        if char_pos == len(text):
                            char_pos = 0

            with open(output_file_path, "a") as output_file:
                output_file.write("\n")

    print(" Done! Saved as output.txt")
    exit(1)

main()
