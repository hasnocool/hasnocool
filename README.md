# Project Title
**Hasnocool**
=============================================

## Description
I built this to create a dynamic and informative README.md file that showcases my active GitHub repositories and WakaTime coding statistics! This project is all about experimenting with new technologies, learning from them, and sharing that knowledge with the world.

## Features
One cool feature is the ability to automatically update your README.md file with:

1. **GitHub Repositories**: A list of your active GitHub repositories, including their names, descriptions, and URLs.
2. **WakaTime Statistics**: Your coding statistics for the last 7 days, broken down by programming language.

## Installation
To get started, you'll need to have Python 3.x installed on your system. Then, simply clone this repository using:
```bash
git clone https://github.com/hasnocool/hasnocool.git
```
Next, create a `.env` file in the `scripts` directory with your WakaTime API key encoded in Base64 (see the example below). Finally, install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Usage
To update your README.md file, simply run the following commands from the project root directory:
```bash
python scripts/update_readme.py
python scripts/update_wakatime.py
```
These scripts will fetch and update your GitHub repositories and WakaTime statistics, respectively.

**Tips:**

* Make sure to keep your `.env` file secure by not sharing it with anyone.
* You can customize the appearance of your README.md file by modifying the `README.md` template in this repository.
* I'm thinking about adding a feature to automatically update your README.md file on a schedule (e.g., daily, weekly). Stay tuned!

## Contributing
If you'd like to contribute to this project, please fork it and submit a pull request with your changes. I'm always excited to see new ideas and improvements!

## License
This project is licensed under the MIT License.

## Tags/Keywords
* GitHub API
* WakaTime API
* README.md generator
* Dynamic documentation
* Programming languages statistics