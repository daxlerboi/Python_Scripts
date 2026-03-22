import pyperclip

def windows_to_wsl_path(win_path):
    path = win_path.replace("\\", "/")
    
    if ":" in path:
        drive, rest = path.split(":", 1)
        path = f"/mnt/{drive.lower()}{rest}"
    
    return f'cd "{path}"'


win_input = input("Paste Windows path: ")
wsl_command = windows_to_wsl_path(win_input)

pyperclip.copy(wsl_command)

print("Copied to clipboard:")
print(wsl_command)
