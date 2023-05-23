import requests
import time

def make_api_call(path):
    # Make an API call using the provided path parameter
    url = f"https://api.example.com/{path}"  # Replace with the actual API URL
    response = requests.put(url)
    # Process the API response as needed
    print(f"Response for {path}: {response.status_code}")

def main():
    file_path = "path_file.txt"  # Replace with the path to your file
    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        path = line.strip()  # Remove leading/trailing whitespace and newlines
        make_api_call(path)
        time.sleep(0.01)  # Wait for 10ms (0.01 seconds) between each call

if __name__ == "__main__":
    main()