import os
import subprocess

# Mapping of script names to user-friendly names
script_names = {
    "generate_catalog_clothing.py": "Catalog Clothing",
    "generate_catalog_items_queries.py": "Catalog Items",
    "generate_catalog_items_wall_queries.py": "Wall Catalog Items",
    "generate_catalog_pages_queries.py": "Catalog Pages",
    "generate_items_base_queries.py": "Items Base",
    "generate_items_base_wall_queries.py": "Wall Items Base"
}

# List of available scripts
scripts = list(script_names.keys())

# Path to the scripts folder
scripts_folder = os.path.join(os.getcwd(), "scripts")

# Change the current working directory to the scripts folder
os.chdir(scripts_folder)

# Function to run a specific script
def run_script(script):
    print(f"Running {script_names[script]}...")
    subprocess.run(["python", script])

# Function to generate the catalog
def generate_catalog():
    print("This command executes all the scripts located in your scripts folder.")
    print("Additionally, remember to configure the correct ranges. Open the script files and find the range options at the top that correspond to the IDs in your furnidata.json.")
    user_input = input("Would you like to proceed? (yes/no): ")
    if user_input.lower() == "yes" or user_input == "1":
        print("Generating Catalog...")
        for script in scripts:
            run_script(script)
    elif user_input.lower() == "no" or user_input == "2":
        print("Catalog generation canceled.")
    else:
        print("Invalid input. Catalog generation canceled.")

# Function to run a specific script
def run_specific_script():
    print("Available Scripts:")
    for index, script in enumerate(scripts, start=1):
        print(f"{index}. {script_names[script]}")
    script_number = int(input("Enter the number of the script you want to run: "))
    if 1 <= script_number <= len(scripts):
        run_script(scripts[script_number - 1])
    else:
        print("Invalid script number.")

# Prompt user for input
print("Options:")
print("1. Generate Catalog")
print("2. Run Specific Script")
user_input = input("Enter the number of the option to proceed: ")

# Determine which option to execute based on user input
if user_input == "1":
    generate_catalog()
elif user_input == "2":
    run_specific_script()
else:
    print("Invalid option.")

# Change the current working directory back to the original folder
os.chdir("..")
