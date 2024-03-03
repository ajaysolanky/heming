import requests
import json

# The URL where your Flask app is running, change it if you deploy it somewhere else
url = "http://127.0.0.1:5000/review"

# The instruction and passage to be reviewed
data = {
    "instruction": "Suggest edits to this passage to make it clearer and better-written",
    "passage": "Remote eng teams rely on regularly written standups over Slack to maintain visibility & productivity. However, these updates are onerous for ICs to write and for managers to review. In order to recall what got done yesterday & needs to get done today, ICs need to revisit information on platforms like JIRA, Github, and Google Docs, shuttle it over, and then synthesize it into an update within Slack. This is stressful and time-consuming, which results in low quality updates that are often not published at all. Managers, as a result, struggle to get a reliable pulse on what their team is working on and how they’re tracking against their goals."
}

# Sending a POST request to the Flask app
response = requests.post(url, json=data)

# Printing the response from the server
response_text = response.json()['response']['response']
print("Response:\n", response_text)

def apply_markup_to_text(text):
    """
    Takes a string with <delete> and <insert> tags and applies the changes
    to produce the modified text.
    """
    import re

    # Pattern to find all <delete>...</delete> and <insert>...</insert> tags
    delete_pattern = r"<delete>.*?<\/delete>"
    insert_pattern = r"<insert>(.*?)<\/insert>"

    # Remove all <delete>...</delete> tags
    modified_text = re.sub(delete_pattern, "", text)

    # Replace all <insert>...</insert> tags with their contents
    modified_text = re.sub(insert_pattern, r"\1", modified_text)

    return modified_text

print("\nModified Result:\n", apply_markup_to_text(response_text))