## ♛ JSON Habbo Catalog Generator ♛

The Habbo Catalog Generator automates catalog creation for Arcturus Morningstar. This user-friendly tool offers options to generate the entire catalog or specific components like clothing, items, walls, and pages. It provides instant generation of queries and is accessible for users with minimal experience.

## Instructions

1. **Place the `furnidata.json` file:** Move the `furnidata.json` file into the `furnidata` folder located in the root directory.

2. **Ensure script availability:** Make sure that the `scripts` folder contains all the necessary script files mentioned below.

3. **Run the `generator.py` script:** Execute the `generator.py` script to access the catalog generation interface.

## Available Scripts

1. **Catalog Clothing**: Generates SQL queries for clothing items to populate the `catalog_clothing` table.

2. **Catalog Items**: Generates SQL queries for items to populate the `catalog_items` table.

3. **Wall Catalog Items**: Generates SQL queries for wall items to populate the `catalog_items` table.

4. **Catalog Pages**: Generates SQL queries for catalog pages to populate the `catalog_pages` table.

5. **Items Base**: Generates SQL queries for general items to populate the `items_base` table.

6. **Wall Items Base**: Generates SQL queries for wall items to populate the `items_base` table.

## Running the Generator

The Habbo Catalog Generator provides two interface options:

1. **Generate Catalog**: Executes all the scripts located in the `scripts` folder to generate the catalog data. Before running this option, configure the correct ID ranges in each script file based on your `furnidata.json`.

2. **Run Specific Script**: Allows you to run a specific script individually. This option provides a list of available scripts, and you can select the script you want to run.

## Setting up the Catalog from Scratch

If you are creating a catalog from scratch, follow these steps to ensure a smooth catalog creation process:

1. Check the "database" folder in the root directory for a SQL file called `catalog_pages.sql`. This file contains all the default pages required for a catalog to function correctly.

2. Import the `catalog_pages.sql` file into your database management system (e.g., MySQL) to create the necessary tables and populate them with the default catalog pages.

3. Verify that the tables and catalog pages are successfully imported into your database.

4. Proceed with the catalog generation process using the instructions provided above.

If you encounter any issues or have further questions, please contact Gizmo#1813 on Discord.

## Note

Make sure to configure the script files properly before executing them to ensure the generated queries match your `furnidata.json` file.

## Reminder
You have to have a formatted furnidata.json file for this script to work properly. If you need assistance in formatting the furnidata.json file, you can use the [JSON Furnidata Formatter](https://github.com/Habbobba/JSON-Furnidata-Formatter) tool available on GitHub. This tool is designed specifically to format furnidata.json files, ensuring correct JSON syntax and proper formatting. Follow the instructions provided in the tool's repository to format your furnidata.json file using the tool.

## Credits

This collection of scripts was created by Gizmo.

## Donate

If you wish to donate, please contact Gizmo#1813 on Discord.
