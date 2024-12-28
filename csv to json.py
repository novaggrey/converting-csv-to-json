import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    try:
        # Read the CSV and add data to a dictionary
        data = []
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        # Write data to a JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        print(f"CSV file has been successfully converted to JSON and saved at {json_file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Hardcoded file paths for testing purposes
    csv_file_path = "dar-es-salaam.csv"  # Replace with your CSV file path
    json_file_path = "output.json"  # Replace with your desired JSON output path

    # Convert the CSV to JSON
    csv_to_json(csv_file_path, json_file_path)
