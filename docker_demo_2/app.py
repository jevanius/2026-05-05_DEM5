from pathlib import Path
from datetime import datetime

out = Path("/data/hello.txt")

#Checking and printing current content of the file
if out.exists():
    current_content = out.read_text()
    print("Current Content:")
    print(current_content)
else:
    print("File does not exist in the volume")

#Apending a new line
with out.open("a") as f:
    f.write(f"Hello docker volume! {datetime.now()}\n")