import random
import json

def load_keywords(file_path):
    with open(file_path, 'r') as file:
        keywords = [line.strip() for line in file.readlines()]
    return keywords

def generate_hashtags(name, keywords):
    name_parts = name.split()
    hashtags = []
    for keyword in keywords:
        hashtags.append(f"{''.join(name_parts)}{keyword}")
        hashtags.append(f"{name_parts[0]}{keyword}")
        hashtags.append(f"{keyword}{''.join(name_parts)}")
        hashtags.append(f"{keyword}{name_parts[0]}")
    return hashtags

def save_hashtags(file_path, hashtags):
    with open(file_path, 'w') as file:
        json.dump(hashtags, file, indent=4)
    print(f"Hashtags saved to {file_path}")

def main():
    try:
        keywords_file = 'keywords.txt'
        output_file = 'generated_hashtags.json'

        name = input("Enter the name to generate hashtags for: ").strip()
        keywords = load_keywords(keywords_file)
        hashtags = generate_hashtags(name, keywords)
        save_hashtags(output_file, hashtags)  
    except KeyboardInterrupt:
            exit(0)
            return  

if __name__ == "__main__":
    main()
