import re

def remove_ips(source_file, target_file, ip_file):
    # Read the content of the source file
    with open(source_file, 'r') as file:
        content = file.readlines()

    # Read the IP addresses from the IP file
    with open(ip_file, 'r') as file:
        ips = file.readlines()
    ips = [ip.strip() for ip in ips]

    # Remove IP addresses and corresponding blank lines from the content
    cleaned_content = []
    removed_ips = []
    for line in content:
        if line.strip() not in ips:
            cleaned_content.append(line)
        else:
            removed_ips.append(line.strip())

    # Write the cleaned content to the target file
    with open(target_file, 'w') as file:
        file.writelines(cleaned_content)

    # Print removed IPs
    print("Task complete. IP addresses removed from", source_file, "based on", ip_file)
    print("Removed IPs:")
    for ip in removed_ips:
        print(ip)

    # Print updated list of IPs in the target file
    print("Updated list of IPs in", target_file)
    with open(target_file, 'r') as file:
        updated_ips = file.readlines()
    for ip in updated_ips:
        print(ip.strip())

# Example usage
source_file = 'source.txt'   # Path to the file containing IP addresses to clean
target_file = 'target.txt'   # Path to the file to write the cleaned content
ip_file = 'ip_list.txt'      # Path to the file containing the list of IP addresses to remove

remove_ips(source_file, target_file, ip_file)