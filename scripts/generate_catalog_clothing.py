import os
import json
import logging
import datetime
import traceback

query_template = "INSERT INTO `catalog_clothing` (`name`, `setid`) VALUES ('{}', '{}');"

# Path to the JSON file
json_file_path = os.path.join("..", "furnidata", "furnidata.json")

# Set up logging
log_folder = os.path.join(os.getcwd(), "..", "logging")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_file_path = os.path.join(log_folder, f"error_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO)

try:
    # Load JSON data from file with specified encoding
    with open(json_file_path, encoding='utf-8') as file:
        json_data = json.load(file)
except FileNotFoundError as e:
    error_msg = f"Error: JSON file '{json_file_path}' not found. {str(e)}"
    logging.error(error_msg, exc_info=True)
    print(error_msg)
    exit(1)
except json.JSONDecodeError as e:
    error_msg = f"Error: Failed to parse JSON file '{json_file_path}'.\nJSON error: {str(e)}"
    logging.error(error_msg, exc_info=True)
    print(error_msg)
    exit(1)

queries = []
for item in json_data.get("roomitemtypes", {}).get("furnitype", []):
    classname = item.get("classname")
    customparams = item.get("customparams")
    if classname is None:
        error_msg = "Error: Invalid item data found in JSON."
        logging.error(error_msg)
        print(error_msg)
        continue

    if classname.startswith("clothing_") or classname in ["test_nft_clothing2", "test_nft_clothing"]:
        try:
            if customparams is not None:
                setid = customparams.replace(" ", "")  # Remove spaces if they exist
            else:
                setid = "your_default_setid"  # Set a default value for setid if customparams is None

            query = query_template.format(classname, setid)
            queries.append(query)
        except Exception as e:
            error_msg = f"Error generating query for item with classname '{classname}': {str(e)}"
            logging.error(error_msg, exc_info=True)
            print(error_msg)

# Console log the number of queries generated
num_queries = len(queries)
print(f"Number of queries generated: {num_queries}")

# Join the queries with a newline character to separate them
all_queries = "\n".join(queries)

# Create the "generated" folder if it doesn't exist in the root directory
folder_name = os.path.join(os.getcwd(), "..", "generated")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Write the queries to the file in the "generated" folder
file_name = os.path.join(folder_name, "catalog_clothing_generated.txt")
try:
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(all_queries)
    success_msg = f"Queries generated successfully and saved to '{file_name}'."
    print(success_msg)
except OSError as e:
    error_msg = f"Error: Failed to write the queries to the file.\nFile error: {str(e)}"
    logging.error(error_msg, exc_info=True)
    print(error_msg)

# Log the number of queries generated
logging.info(f"Number of queries generated: {num_queries}")

# Check if any errors were logged
if logging.getLogger().hasHandlers() and logging.getLogger().handlers[0].level == logging.INFO:
    print(f"Some errors occurred during the generation process. Please check the log file at '{log_file_path}' for details.")
else:
    print("No errors were encountered during the generation process.")
