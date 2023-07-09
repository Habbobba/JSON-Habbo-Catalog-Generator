import os
import json
import logging
import datetime
import traceback

query_template = "INSERT INTO `catalog_pages` (`id`, `parent_id`, `caption_save`, `caption`, `page_layout`, `icon_color`, `icon_image`, `min_rank`, `order_num`, `visible`, `enabled`, `club_only`, `vip_only`, `page_headline`, `page_teaser`, `page_special`, `page_text1`, `page_text2`, `page_text_details`, `page_text_teaser`, `room_id`, `includes`) VALUES ({}, 2, '', '{}', 'default_3x3', 1, 1, 1, 1, '1', '1', '0', '0', '', '', '', NULL, NULL, NULL, NULL, 0, '');"

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
        json_data = json_data.get("roomitemtypes", {}).get("furnitype", [])
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
furniline_set = set()
category_set = set()
captions_set = set()

# Start the ID from 100
id = 100

for item in json_data:
    classname = item.get("classname")
    furniline = item.get("furniline")
    category = item.get("category")

    if classname is None or furniline is None or category is None:
        continue

    if furniline == '' or category == '':
        continue

    try:
        if furniline not in furniline_set:
            if furniline not in captions_set:
                furniline_query = query_template.format(id, furniline)
                queries.append(furniline_query)
                captions_set.add(furniline)
                furniline_set.add(furniline)
                # Increment the ID by 1
                id += 1

        if category not in category_set:
            if category not in captions_set:
                category_query = query_template.format(id, category)
                queries.append(category_query)
                captions_set.add(category)
                category_set.add(category)
                # Increment the ID by 1
                id += 1
    except Exception as e:
        error_msg = f"Error generating query for item with classname '{classname}': {str(e)}"
        logging.error(error_msg, exc_info=True)
        print(error_msg)
        traceback.print_exc()

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
file_name = os.path.join(folder_name, "catalog_pages_generated.txt")
try:
    with open(file_name, "w", encoding='utf-8') as file:
        file.write(all_queries)
    success_msg = f"Queries generated successfully and saved to '{file_name}'."
    print(success_msg)
except OSError as e:
    error_msg = f"Error: Failed to write the queries to the file.\nFile error: {str(e)}"
    logging.error(error_msg, exc_info=True)
    print(error_msg)

# Check if any errors were logged
if logging.getLogger().hasHandlers() and logging.getLogger().handlers[0].level == logging.INFO:
    print(f"Some errors occurred during the generation process. Please check the log file at '{log_file_path}' for details.")
else:
    print("No errors were encountered during the generation process.")
