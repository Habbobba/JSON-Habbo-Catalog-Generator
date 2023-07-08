## Habbo Catalog Generator

These scripts generate SQL queries using a JSON file (furnidata.json) for catalog items in a virtual world, populating a database with relevant data.

## Instructions

1. **Place the `furnidata.json` file:** Move the `furnidata.json` file into the `furnidata` folder located in the root directory.

2. **Ensure script availability:** Make sure that the `scripts` folder contains all the necessary script files mentioned below.

3. **Run the `generator.py` script:** Execute the `generator.py` script to access the catalog generation interface.

## Interface Options

1. **Generate Catalog**: Executes all the scripts located in the `scripts` folder to generate the catalog data. Before running this option, make sure to configure the correct ID ranges in each script file based on your `furnidata.json`.

2. **Run Specific Script**: Allows you to run a specific script individually. This option provides a list of available scripts, and you can select the script you want to run.

## Available Scripts

1. **Catalog Clothing**: Generates SQL queries for clothing items to populate the `catalog_clothing` table.

2. **Catalog Items**: Generates SQL queries for items to populate the `catalog_items` table.

3. **Wall Catalog Items**: Generates SQL queries for wall items to populate the `catalog_items` table.

4. **Catalog Pages**: Generates SQL queries for catalog pages to populate the `catalog_pages` table.

5. **Items Base**: Generates SQL queries for general items to populate the `items_base` table.

6. **Wall Items Base**: Generates SQL queries for wall items to populate the `items_base` table.

## Running a Specific Script

If you choose the **Run Specific Script** option, you will be prompted to enter the number corresponding to the script you want to run. Each script generates the required SQL queries for a specific catalog component.

## Configuring ID Ranges

Before executing the scripts, ensure that you configure the ID ranges in each script file to match the desired catalog items in your `furnidata.json`. Locate the `start_id` and `end_id` variables at the top of each script file and adjust them accordingly.

## Note

Make sure to configure the script files properly before executing them to ensure the generated queries match your `furnidata.json` file.

## Credits

This collection of scripts was created by Gizmo.

## Donate
If you wish to donate, please contact Gizmo#1813 on Discord.
