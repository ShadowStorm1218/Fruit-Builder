filepath = r"C:\Windows\System32\drivers\etc\hosts"

# open the file in write mode
with open(filepath, "w") as file:
    # write new content to the file
    file.write("0.0.0.0\t\treddit.com\n")
    file.write("0.0.0.0\t\twww.reddit.com\n")
