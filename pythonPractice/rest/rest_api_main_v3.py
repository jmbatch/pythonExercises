import requests
from requests.auth import HTTPBasicAuth
import os
import json
from jinja2 import Template
from typing import Union, Dict, Optional


class APIClient:
    def __init__(self, base_url: str, auth_type: Optional[str] = None, auth: Optional[Union[str, tuple]] = None):
        """
        Initializes the APIClient instance.

        Parameters:
        - base_url: The base URL for the API
        - auth_type: Type of authentication ('basic', 'api_key', 'bearer')
        - auth: Authentication data (tuple for basic auth, string for API key or bearer token)
        """
        self.base_url = base_url
        self.auth_type = auth_type
        self.auth = auth
        self.session = requests.Session()

    def request(self, endpoint: str, method: str = 'GET', headers: Optional[Dict[str, str]] = None,
                data: Optional[Union[Dict, str]] = None, params: Optional[Dict[str, str]] = None) -> None:
        """
        Sends an API request.

        Parameters:
        - endpoint: The API endpoint (relative to base_url)
        - method: HTTP method ('GET', 'POST', etc.)
        - headers: Request headers
        - data: Payload for POST/PUT requests (JSON)
        - params: Query parameters for GET requests
        """
        url = f"{self.base_url}/{endpoint}"
        if self.auth_type == 'basic' and isinstance(self.auth, tuple):
            auth = HTTPBasicAuth(*self.auth)
        elif self.auth_type == 'api_key' and isinstance(self.auth, str):
            headers = headers or {}
            headers['api-key'] = self.auth
            auth = None
        elif self.auth_type == 'bearer' and isinstance(self.auth, str):
            headers = headers or {}
            headers['Authorization'] = f"Bearer {self.auth}"
            auth = None
        else:
            auth = None

        try:
            response = self.session.request(method, url, headers=headers, auth=auth, json=data, params=params, timeout=10)
            response.raise_for_status()
            self.handle_response(response)
        except requests.RequestException as e:
            print(f"Error during API call: {e}")

    def handle_response(self, response: requests.Response) -> None:
        """
        Handles the API response and prints it based on the content type.
        
        Parameters:
        - response: The HTTP response object
        """
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            try:
                error_data = response.json()
                print(f"Error details: {json.dumps(error_data, indent=2)}")
            except ValueError:
                print(f"Non-JSON response: {response.text}")
            return
        
        content_type = response.headers.get('Content-Type', '').lower()
        
        if 'application/json' in content_type:
            json_data = response.json()
            print(json.dumps(json_data, indent=2))  # Pretty-print JSON
        elif 'application/xml' in content_type or 'text/xml' in content_type:
            print("XML response not handled in this example.")
        elif 'text/plain' in content_type:
            print(response.text)
        else:
            print("Unsupported response type.")

    def send_configuration(self, endpoint: str, template_path: str, template_vars: Dict) -> None:
        """
        Sends a configuration to the server using a JSON payload rendered from a Jinja2 template.

        Parameters:
        - endpoint: The API endpoint to send the configuration to
        - template_path: Path to the Jinja2 template file
        - template_vars: Variables to inject into the template
        """
        with open(template_path, 'r') as template_file:
            template = Template(template_file.read())

        # Render the template with the provided variables
        rendered_json = template.render(template_vars)
        
        # Convert rendered string to JSON format
        json_payload = json.loads(rendered_json)

        # Set the appropriate headers for the request
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Make a POST request with the rendered JSON data
        self.request(endpoint=endpoint, method='POST', headers=headers, data=json_payload)

# Set base URL and API endpoint
BASE_URL = 'https://api.scripture.api.bible/v1'
# ENDPOINT = 'bibles/06125adad2d5898a-01/books/MAT/chapters'
ENDPOINT = 'bibles?language=eng'

# Retrieve the API key from environment variables
API_KEY = os.getenv('API_KEY', 'your_default_api_key_if_none')

# Set headers for the request
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Initialize the API client with API key authentication
client = APIClient(base_url=BASE_URL, auth_type='api_key', auth=API_KEY)

# Make the API request
client.request(endpoint=ENDPOINT, method='GET', headers=headers)

# This is for sending POST requests
# Define variables for the template
# template_vars = {
#     "server_name": "example-server",
#     "max_connections": 500,
#     "timeout": 30,
#     "compression": True,
#     "logging_level": "DEBUG"
# }

# Send the configuration using the template
# client.send_configuration(endpoint=ENDPOINT, template_path='server_config.json.j2', template_vars=template_vars)