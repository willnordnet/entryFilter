import csv
import json

input_file = "./input/100_recent_examples_json.csv"
output_file = "./output/100_recent_examples_json_washed.csv"

# Step 1: Take a multi-row CSV file as input
with open(input_file, 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

# Step 3: Process remaining rows and filter selected attributes
filtered_rows = []
for row in rows:
    json_data = json.loads(row[0])
    selected_values = ["cstno=" + str(json_data["cstno"])]
    for account in json_data["accounts"]:
        selected_values.append("accno=" + str(account["accno"]))
        if "alias" in account:
            selected_values.append("alias=" + account["alias"])
        if "nonbankaccount" in account:
            selected_values.append("bankaccount=" + account["nonbankaccount"])

    filtered_row = [selected_values]
    filtered_row.extend(row[1:])
    filtered_rows.append(filtered_row)

# Step 4: Save the output into a new CSV file
with open(output_file, 'w') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerows(filtered_rows)

print("Output file saved successfully!")
