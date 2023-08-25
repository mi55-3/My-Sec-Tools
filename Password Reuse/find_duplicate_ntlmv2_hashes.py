import os

def extract_ntlmv2_hash(line):
    # Split the line by ':' and extract the fourth field (index 3) which should contain the NTLMv2 hash
    fields = line.split(':')
    if len(fields) >= 4:
        return fields[3]
    return None

def find_duplicate_ntlmv2_hashes(input_file, output_file):
    # Dictionary to store NTLMv2 hashes as keys and the associated lines as values
    hash_dict = {}

    # Open the input file in read mode and process its lines
    with open(input_file, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            # Check if the line starts with 'SMB' and does not contain 'STATUS_LOGON_FAILURE'
            if line.startswith('SMB') and "STATUS_LOGON_FAILURE" not in line:
                # Extract the NTLMv2 hash from the line
                ntlmv2_hash = extract_ntlmv2_hash(line)
                if ntlmv2_hash is not None:
                    # Add the line to the hash_dict using the NTLMv2 hash as the key
                    if ntlmv2_hash in hash_dict:
                        hash_dict[ntlmv2_hash].append(line)
                    else:
                        hash_dict[ntlmv2_hash] = [line]
                else:
                    # Print an error message if the line does not contain the expected fields
                    print(f"Error parsing line {line_number}: {line}")

    # Write the duplicate NTLMv2 hashes and their associated lines to the output file
    with open(output_file, 'w') as output:
        for ntlmv2_hash, lines in hash_dict.items():
            if len(lines) > 1:
                output.write(f"Duplicate NTLMv2 Hash: {ntlmv2_hash}\n")
                output.write("\n".join(lines) + "\n\n")

    # Print to terminal the number of times each duplicate hash has been reused
    for ntlmv2_hash, lines in hash_dict.items():
        if len(lines) > 1:
            print(f"Hash: {ntlmv2_hash}, Reused {len(lines)} times")

if __name__ == "__main__":
    input_file = "sam.txt"
    output_file = "output.txt"
    
    # Get the current script directory and build the input and output file paths
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_file_path = os.path.join(script_directory, input_file)
    output_file_path = os.path.join(script_directory, output_file)
    
    # Call the function to find duplicate NTLMv2 hashes and write the output to the file
    find_duplicate_ntlmv2_hashes(input_file_path, output_file_path)
    
    # Print a message indicating where the output file is written
    print(f"Duplicate NTLMv2 hashes written to {output_file}.")
