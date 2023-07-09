import os
import json
import logging
import datetime
import traceback

start_id = 4001
end_id = 4774

query_template = "INSERT INTO `items_base` (`id`, `sprite_id`, `public_name`, `item_name`, `type`, `width`, `length`, `stack_height`, `allow_stack`, `allow_sit`, `allow_lay`, `allow_walk`, `allow_gift`, `allow_trade`, `allow_recycle`, `allow_marketplace_sell`, `allow_inventory_stack`, `interaction_type`, `interaction_modes_count`, `vending_ids`, `multiheight`, `customparams`, `effect_id_male`, `effect_id_female`, `clothing_on_walk`) VALUES ({0}0, {1}, '{2}', '{2}', 'i', 1, 1, 0.00, 0, 0, 0, 0, 1, 1, 0, 0, 1, '{3}', {4}, '0', '0', '{5}', 0, 0, '0');"

# Path to the JSON file
json_file_path = os.path.join("..", "furnidata", "furnidata.json")

# Set up logging
log_folder = os.path.join(os.path.dirname(os.getcwd()), "logging")
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
log_file_path = os.path.join(log_folder, f"error_log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
logging.basicConfig(filename=log_file_path, level=logging.INFO)

try:
    # Load JSON data from file with specified encoding
    with open(json_file_path, encoding='utf-8') as file:
        json_data = json.load(file)
        json_data = json_data.get("wallitemtypes", {}).get("furnitype", [])
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
for item in json_data:
    id = item.get("id")
    classname = item.get("classname")

    if id is None or classname is None:
        error_msg = "Error: Invalid item data found in JSON."
        logging.error(error_msg)
        print(error_msg)
        continue

    if start_id <= id <= end_id:
        if classname in ["post.it", "post.it.vd", "post_it_xmas", "post_it_dreams", "post_it_shakesp", "post_it_juninas", "post_it_vd", "post_it"]:
            interaction_type = "postit"
        elif classname in ["external_image_wallitem_poster", "external_image_wallitem_poster_small"]:
            interaction_type = "external_image"
        elif classname == "roomdimmer" or classname.startswith("dimmer_"):
            interaction_type = "dimmer"
            interaction_modes_count = 2
        elif classname == "habbowheel" or classname == "ads_tlc_wheel":
            interaction_type = "colorwheel"
            interaction_modes_count = 10
        else:
            interaction_type = "default"
            interaction_modes_count = 1

        try:
            query = query_template.format(id, id, classname, interaction_type, interaction_modes_count, "0")
            queries.append(query)
        except Exception as e:
            error_msg = f"Error: Failed to generate query for classname '{classname}'.\n{str(e)}"
            logging.error(error_msg, exc_info=True)
            print(error_msg)

# Console log the number of queries generated
num_queries = len(queries)
print(f"Number of queries generated: {num_queries}")

# Join the queries with a newline character to separate them
all_queries = "\n".join(queries)

# Create the "generated" folder if it doesn't exist in the parent directory
folder_name = os.path.join(os.path.dirname(os.getcwd()), "generated")
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Write the queries to the file
file_name = "items_base_wall_generated.txt"
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
