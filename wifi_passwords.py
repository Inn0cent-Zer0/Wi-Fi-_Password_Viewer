import subprocess

# Get all saved Wi-Fi profiles on the system
data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")

# Extract only the profile names (SSID)
profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

# Print header
print("{:<30}|  {:<}".format("Wi-Fi Name", "Password"))
print("-" * 45)

# Loop through each profile and retrieve password (if any)
for profile in profiles:
    try:
        # Get detailed info for each profile including key=clear to see password
        results = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"]
        ).decode("utf-8").split("\n")

        # Extract password line (Key Content)
        password = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]

        # Display profile name and password
        print("{:<30}|  {:<}".format(profile, password[0] if password else ""))
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(profile, "ERROR"))
