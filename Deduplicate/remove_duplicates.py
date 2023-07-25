def add_extra_line(file_path):
    try:
        # Add an extra line at the end of the file
        with open(file_path, 'a') as file:
            file.write("\n")

        # Now read the file and remove duplicates
        with open(file_path, 'r') as file:
            lines = file.readlines()
            unique_lines = set()

            # Remove duplicates from the lines
            for line in lines:
                unique_lines.add(line)

            # Create a new file with deduplicated results
            deduplicated_file_path = 'deduplicated-results.txt'
            with open(deduplicated_file_path, 'w') as deduplicated_file:
                for line in unique_lines:
                    deduplicated_file.write(line)

            num_duplicates = len(lines) - len(unique_lines)
            if num_duplicates > 0:
                print(f"{num_duplicates} duplicate result(s) removed.")
            else:
                print("No duplicate results found.")

            print(f"Deduplicated results saved to '{deduplicated_file_path}'.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to the file to search and remove duplicates: ")
    add_extra_line(input_file)
