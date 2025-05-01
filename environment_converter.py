import subprocess

# Step 1: Get the conda list --export output
conda_path = r"D:\anaconda3\Scripts\conda.exe"  # Adjust as needed
output = subprocess.check_output([conda_path, "list", "--export"], text=True)

# Step 2: Convert to pip-style requirements
requirements = []
for line in output.splitlines():
    if line.strip() and not line.startswith("#"):
        parts = line.split("=")
        if len(parts) >= 2:
            pkg = parts[0]
            ver = parts[1]
            requirements.append(f"{pkg}=={ver}")

# Step 3: Write to requirements.txt
with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(requirements))

print("requirements.txt generated successfully.")
