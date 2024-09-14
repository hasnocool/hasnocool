import json

def update_readme():
    with open('repos.json', 'r') as f:
        repos = json.load(f)

    project_section = "\n".join(
        [f"- [{repo['name']}]({repo['html_url']}) - {repo['description']}" for repo in repos]
    )

    with open("README.md", "r") as f:
        readme = f.read()

    updated_readme = readme.split("<!--START_SECTION:projects-->")[0] + \
                     f"<!--START_SECTION:projects-->\n{project_section}\n<!--END_SECTION:projects-->" + \
                     readme.split("<!--END_SECTION:projects-->")[1]

    with open("README.md", "w") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    update_readme()
