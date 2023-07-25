import re

def search_and_create_files(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

            # Define the regular expression pattern to search for
            pattern = r'(?:[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}|[a-zA-Z0-9_]+[/\\])?(?:[^:]+:[^\s]+)'

            # Define exclusion patterns for password hashes, plain_password_hex, [*], dpapi_machinekey, dpapi_userkey, [-], Microsoft hashes, LM hashes, NTLMv2 hashes, (Pwn3d!), specific hash formats, SP.NETAutoGenKeys, lines starting with SCM:{, and lines containing L$NetPro
            exclusion_patterns = [
                r'\b(?:[0-9a-fA-F]{32}|[0-9a-fA-F]{40}|[0-9a-fA-F]{64})\b',  # Common password hashes
                r'\b(?:[0-9a-fA-F]{16})\b',  # DES-CBC-MD5 hashes
                r'\b(?:plain_password_hex)\b',  # plain_password_hex
                r'\[\*\]',  # Lines containing "[*]"
                r'\b(?:dpapi_machinekey|dpapi_userkey)\b',  # Lines containing "dpapi_machinekey" or "dpapi_userkey"
                r'\[-\]',  # Lines containing "[-]"
                r'\b(?:[a-fA-F0-9]{32})\b',  # Microsoft NTLM hashes
                r'NL\$KM:[a-fA-F0-9]{32}',  # LM hashes
                r'S-\d+-\d+-\d+#\d:',  # NTLMv2 hashes
                r'\(Pwn3d!\)',  # Lines containing "(Pwn3d!)"
                r'ASP\.NETAutoGenKeys2\.0\.50727\.1433:[0-9a-fA-F]+',  # Lines containing specified hash format
                r'L\$ASP\.NETAutoGenKeysV44\.0\.30319\.0:[0-9a-fA-F]+',  # Lines containing another specified hash format
                r'SP\.NETAutoGenKeys',  # Lines containing SP.NETAutoGenKeys
                r'SCM:{',  # Lines starting with SCM:{
                r'L\$NetPro',  # Lines containing L$NetPro
            ]

            # Use re.findall() to find all matches in the content
            matches = [line.strip() for line in content if re.search(pattern, line)]

            # Create lists to store potential cleartext passwords and other matches
            potential_cleartext_passwords = []
            remaining_matches = []

            # Separate potential cleartext passwords from other matches
            for match in matches:
                if any(re.search(pattern, match) for pattern in exclusion_patterns):
                    remaining_matches.append(match)
                else:
                    if "[+]" not in match and "(Pwn3d!)" not in match:
                        potential_cleartext_passwords.append(match)

            # Write potential cleartext passwords to a file
            with open('potential-cleartext-passwords.txt', 'w') as cleartext_file:
                for match in potential_cleartext_passwords:
                    cleartext_file.write(match + '\n')

            # Write other matches to a file
            with open('remaining-file.txt', 'w') as remaining_file:
                for match in remaining_matches:
                    remaining_file.write(match + '\n')

            print("Potential cleartext passwords saved to 'potential-cleartext-passwords.txt'.")
            print("Other matches saved to 'remaining-file.txt'.")

        # Print the contents of potential-cleartext-passwords.txt to the terminal
        with open('potential-cleartext-passwords.txt', 'r') as cleartext_file:
            print("\nContents of 'potential-cleartext-passwords.txt':")
            print(cleartext_file.read())

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path to the file to search: ")
    search_and_create_files(input_file)
