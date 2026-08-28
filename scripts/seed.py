
import json

from pathlib import Path

ignored = [".git", ".obsidian"]

vaults = {}
for path in Path("/home/asura/Documents/vaults/").rglob("*"):
    if not any(part in ignored for part in path.parts):

        if not path.is_file():
            continue

        curr = vaults
        for i in range(5, len(path.parts) - 1):
            dir = path.parts[i]
            if dir not in vaults:
                vaults[dir] = {}

            curr = vaults[dir]

        curr.append(path.parts[len(path.parts) - 1])

print(json.dumps(vaults, indent=2))
