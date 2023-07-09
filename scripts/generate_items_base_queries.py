import os
import json
import logging
import datetime
import traceback

start_id = 1
end_id = 14364

query_template = "INSERT INTO `items_base` (`id`, `sprite_id`, `public_name`, `item_name`, `type`, `width`, `length`, `stack_height`, `allow_stack`, `allow_sit`, `allow_lay`, `allow_walk`, `allow_gift`, `allow_trade`, `allow_recycle`, `allow_marketplace_sell`, `allow_inventory_stack`, `interaction_type`, `interaction_modes_count`, `vending_ids`, `multiheight`, `customparams`, `effect_id_male`, `effect_id_female`, `clothing_on_walk`) VALUES ({0}, {1}, '{2}', '{2}', 's', 1, 1, 0.00, 0, {3}, {4}, {5}, 1, 1, 0, 0, 1, '{6}', {7}, '0', '0', '{8}', 0, 0, '0');"

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
    id = item.get("id")
    classname = item.get("classname")
    customparams = item.get("customparams")
    canstandon = item.get("canstandon")
    cansiton = item.get("cansiton")
    canlayon = item.get("canlayon")

    if id is None or classname is None:
        error_msg = "Error: Invalid item data found in JSON."
        logging.error(error_msg)
        print(error_msg)
        continue

    if start_id <= id <= end_id:
        if classname.startswith("wf_"):
            interaction_type = classname
            interaction_modes_count = 2
        elif classname.startswith("clothing_"):
            interaction_type = "clothing"
            interaction_modes_count = 2
        else:
            interaction_type = "default"
            interaction_modes_count = 1

        allow_walk = 1 if canstandon else 0
        allow_sit = 1 if cansiton else 0
        allow_lay = 1 if canlayon else 0
        query = query_template.format(id, id, classname, allow_sit, allow_lay, allow_walk, customparams or "0", interaction_modes_count, "0")
        queries.append(query)

# Console log the number of queries generated
num_queries = len(queries)
print(f"Number of queries generated: {num_queries}")

# Join the queries with a newline character to separate them
all_queries = "\n".join(queries)

# Create the "generated" folder if it doesn't exist in the root directory
folder_name = os.path.join(os.getcwd(), "..", "generated")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Write the queries to the file
file_name = os.path.join(folder_name, "items_base_generated.txt")
file_path = os.path.join(folder_name, file_name)
try:
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(all_queries)
    success_msg = f"Queries generated successfully and saved to '{file_path}'."
    print(success_msg)
except OSError as e:
    error_msg = f"Error: Failed to write the queries to the file.\nFile error: {str(e)}"
    logging.error(error_msg, exc_info=True)
    print(error_msg)
    exit(1)

# Check if any errors were logged
if logging.getLogger().hasHandlers() and logging.getLogger().handlers[0].level == logging.INFO:
    print(f"Some errors occurred during the generation process. Please check the log file at '{log_file_path}' for details.")
else:
    print("No errors were encountered during the generation process.")
