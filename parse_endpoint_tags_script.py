import re

def parse_endpoints(file_path):
    # Open and read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex pattern to find the endpoints and tags
    pattern = re.compile(r'@router\.(get|post)\("(/[^"]+)"[^@]*?tags=\[([^\]]+)\]', re.IGNORECASE | re.DOTALL)
    no_tag_pattern = re.compile(r'@router\.(get|post)\("(/[^"]+)"', re.IGNORECASE | re.DOTALL)

    # Find all matches
    matches = pattern.findall(content)
    no_tag_matches = no_tag_pattern.findall(content)

    # Create a dictionary from the matches
    endpoints = {endpoint: tags.strip('"\' ') for _, endpoint, tags in matches}

    # Add endpoints without tags
    for method, endpoint in no_tag_matches:
        if endpoint not in endpoints:
            endpoints[endpoint] = "NA"
    return endpoints

# Example usage
file_path = "endpoint_functions.py"  # Replace with the correct file path

endpoints = parse_endpoints(file_path)
for endpoint, tag in endpoints.items():
    print(f"{endpoint}: {tag}")