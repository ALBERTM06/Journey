# Text write (overwrites file)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("First line\nSecond line\n")

# Text append
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("Appended line\n")

# Text read
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()          # one big string
    # or: lines = f.readlines() # list of lines (with \n)
    # or: for line in f:        # iterate line by line
