import os
import base64
import requests

# Decode the obfuscated WakaTime API key from Base64
encoded_api_key = os.getenv('WAKATIME_API_KEY_ENCODED')

if encoded_api_key:
    decoded_api_key = base64.b64decode(encoded_api_key).decode('utf-8')
else:
    raise ValueError("API key not found. Ensure the WAKATIME_API_KEY_ENCODED is set.")

def get_wakatime_stats():
    response = requests.get(f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={decoded_api_key}")
    return response.json()

def update_readme():
    stats = get_wakatime_stats()

    breakdown_section = "\n".join(
        [f"- {lang['name']}: {lang['percent']}%" for lang in stats['data']['languages']]
    )

    with open("README.md", "r") as f:
        readme = f.read()

    updated_readme = readme.split("<!--START_SECTION:waka-->")[0] + \
                     f"<!--START_SECTION:waka-->\n{breakdown_section}\n<!--END_SECTION:waka-->" + \
                     readme.split("<!--END_SECTION:waka-->")[1]

    with open("README.md", "w") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    update_readme()