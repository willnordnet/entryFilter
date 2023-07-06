import csv
import json

import yaml

# input_file = "./input/user_4.csv"
# input_file = "./input/100_recent_examples_json.csv"
# output_file = "./output/100_recent_examples_json_washed.csv"
# output_file = "./output/user_4_washed.csv"
input_file = "./input/" + input(
    "Sessionsdata json/yaml must be in row[0]. Enter the path to the input CSV file under ./input: ")
output_file = "./output/" + input("Enter the path for the output CSV file under ./output: ")


def is_valid_json(json_str):
    try:
        json.loads(json_str)
    except json.JSONDecodeError:
        return False
    return True


def is_valid_yaml(yaml_str):
    try:
        yaml.safe_load(yaml_str)
    except yaml.YAMLError:
        return False
    return True


# Step 1: Take a multi-row CSV file as input
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

# Step 3: Process remaining rows and filter selected attributes
filtered_rows = []
for row in rows:
    # print("Processing session ID: " + row[1])
    selected_values = []
    if is_valid_json(row[0]):
        json_data = json.loads(row[0])
        selected_values.append("customer no=" + str(json_data["cstno"]))
        for account in json_data["accounts"]:
            selected_values.append("account no=" + str(account["accno"]))
            if "alias" in account:
                selected_values.append("alias=" + account["alias"])
            if "nonbankaccount" in account:
                selected_values.append("bankaccount=" + account["nonbankaccount"])
    elif is_valid_yaml(row[0]):
        yaml_data = yaml.safe_load(row[0])
        selected_values.append("customer no=" + str(yaml_data.get("cstno")))
        if "display_account" in yaml_data:
            selected_values.append("display account=" + str(yaml_data.get("display_account")))
        accounts = yaml_data['nasa_accounts']
        for account in accounts:
            selected_values.append("account no=" + str(account))
            if "alias" in accounts[account]:
                selected_values.append("alias=" + str(accounts[account]['alias']))
    else:
        print("Error! Invalid JSON/YAML sessionsdata: " + row[0])

    filtered_row = []
    filtered_row.extend(row[1:])
    filtered_row.append(selected_values)
    filtered_rows.append(filtered_row)

# Step 4: Save the output into a new CSV file
with open(output_file, 'w') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerows(filtered_rows)

print("Successful. " + str(len(filtered_rows)) + " Saved in " + output_file)
