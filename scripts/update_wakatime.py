import requests

WAKATIME_API_KEY = "your_wakatime_api_key"

def get_wakatime_stats():
    response = requests.get(f"https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key={WAKATIME_API_KEY}")
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
