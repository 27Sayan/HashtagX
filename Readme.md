# HashtagX Tool

HashtagX is a Python tool designed for generating and searching for hashtags on X (formerly known as Twitter) based on custom names and keywords.

## Description

The **HashtagX Tool** helps users create multiple hashtag combinations using a name and customizable keywords. It supports searching for tweets related to the generated hashtags and can save the results in a CSV file for further analysis. This tool is particularly useful for finding genre-specific hashtags, such as `#person1comedy` or `#person2motivation` or `#funnyperson3`.

## Features

- Generate multiple hashtag combinations using a given name and custom keywords.
- Search and retrieve tweets associated with the generated hashtags.
- Save retrieved tweet data to a CSV file.
- Works for both multiple and single hashtag searches.

## Installation

Follow the following steps for installation of the tool. 

```bash
git clone https://github.com/27Sayan/HashtagX.git
cd Hashtagx
pip install -r requirements.txt
```

## How to Use

### 1. Searching for Multiple Hashtags
To search for multiple hashtag combinations (e.g., `#person1fraud`, `#person2comedy`):
1. Modify the `keywords.txt` file to include words or genres you want to combine with the name (e.g., fraud, scam, comedy).
2. Run `hashtagx.py` to generate the hashtags:
   ```bash
   python hashtagx.py
3. The tool will output hashtags based on the name and keywords you provided. You can use these hashtags for further analysis.

### 2. Searching for a Single Hashtag
To search for a single hashtag::
1. Keep the `keywords.txt` file empty..
2. Run `hashtagx.py` directly:
   ```bash
   python hashtagx.py
3. The tool will generate a hashtag based on the provided name without combining it with any keywords.

## Note

This tool is for educational purposes only. I am not responsible for any misuse of this tool.

## License

This project is licensed under the [GPLv3.](https://github.com/27Sayan/HashtagX/blob/main/LICENSE)
