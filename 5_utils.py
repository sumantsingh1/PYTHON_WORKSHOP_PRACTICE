import os  # Importing OS module to execute system-level commands

# =========================
# WINDOWS SYSTEM COMMANDS
# =========================

# Display basic system information (OS version, memory, architecture)
print("Windows System Information:")
print(os.system('systeminfo'))

# Show current system uptime
print("Windows System Uptime:")
print(os.system('net stats workstation'))

# Display disk usage information
print("Windows Disk Usage:")
print(os.system('wmic logicaldisk get size,freespace,caption'))

# Display memory (RAM) information
print("Windows Memory Information:")
print(os.system('wmic OS get FreePhysicalMemory,TotalVisibleMemorySize /Value'))


# =========================
# LINUX SYSTEM COMMANDS (COMMENTED)
# =========================

# Show disk usage in human-readable format
# print("Linux Disk Usage:")
# print(os.system('df -h'))

# Show system uptime and load average
# print("Linux System Uptime:")
# print(os.system('uptime'))

# Show RAM usage in human-readable format
# print("Linux Memory Information:")
# print(os.system('free -h'))

# Show detailed system information
# print("Linux System Information:")
# print(os.system('uname -a'))
