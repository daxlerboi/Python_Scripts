def windows_to_wsl_path(win_path):
    # Replace backslashes with forward slashes
    path = win_path.replace("\\", "/")
    
    # Convert drive letter (C:) → /mnt/c
    if ":" in path:
        drive, rest = path.split(":", 1)
        path = f"/mnt/{drive.lower()}{rest}"
    
    return f'cd "{path}"'


# Example usage
win_input = input("Paste Windows path: ")
wsl_command = windows_to_wsl_path(win_input)

print("WSL command:")
print(wsl_command)
