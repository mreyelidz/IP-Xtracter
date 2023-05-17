import re

# Define regular expression for detecting IP addresses
ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Open the text file
with open('myfile.txt', 'r') as file:

    # Loop through each line in the file
    for line in file:

        # Find all IP addresses in the current line using the regular expression
        ips = re.findall(ip_regex, line)

        # If one or more IP addresses were found, print each one on a new line
        if ips:
            for ip in ips:,
                print(ip)
