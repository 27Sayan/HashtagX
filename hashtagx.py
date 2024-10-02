import asyncio  
from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from configparser import ConfigParser
from random import randint
import json  
import subprocess

def load_hashtags(filename):
    with open(filename, 'r') as file:
        hashtags = json.load(file)
    return list(set(hashtags)) 

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_hashtags():
    subprocess.run(["python", "generator.py"])

async def search_tweets_and_print_links(hashtags, num_links, save_to_file):
    try:
        hashtag_query = ' OR '.join([f'#{hashtag}' for hashtag in hashtags])  
        QUERY = f'({hashtag_query})'

        global client
        client = Client(language='en-US')

        await client.login(auth_info_1=username, auth_info_2=email, password=password)
        client.save_cookies('cookies.json')  

        if save_to_file:
            with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Sr No', 'Username', 'Description', 'Link'])

        tweet_count = 0
        tweets = None

        while tweet_count < num_links:  
            try:
                tweets = await get_tweets(tweets, QUERY)
            except TooManyRequests as e:
                rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
                print(f'{datetime.now()} - Rate limit reached. Waiting until {rate_limit_reset}')
                wait_time = rate_limit_reset - datetime.now()
                await asyncio.sleep(wait_time.total_seconds()) 
                continue

            if not tweets:
                print(f'{datetime.now()} - No more tweets found')
                break

            for tweet in tweets:
                if any(f'#{hashtag}' in tweet.text for hashtag in hashtags):
                    tweet_count += 1
                    tweet_data = [
                        tweet_count,                   
                        tweet.user.name,            
                        tweet.text,                    
                        f"https://x.com/{tweet.user.screen_name}/status/{tweet.id}" 
                    ]

                    if save_to_file:
                        with open('tweets.csv', 'a', newline='', encoding='utf-8') as file:
                            writer = csv.writer(file)
                            writer.writerow(tweet_data)

                    print(tweet_data[3])

        print(f'{datetime.now()} - Done! Retrieved {tweet_count} tweets')
    except Exception as e:
        print(f"Ran into a problem: {str(e)}\nQuitting...")
        return

async def get_tweets(tweets, query):
    if tweets is None:
        print(f'{datetime.now()} - Getting tweets...')
        tweets = await client.search_tweet(query, product='Top') 
    else:
        wait_time = randint(5, 10)
        print(f'{datetime.now()} - Getting more tweets after {wait_time} seconds ...')
        await asyncio.sleep(wait_time)  
        tweets = await tweets.next()

    return tweets

def main():
    clear_terminal() 
    print(r''' 
             _  _                    _        _               __ _  __  __  
            | || |   __ _     ___   | |_     | |_    __ _    / _` | \ \/ /  
            | __ |  / _` |   (_-<   | ' \    |  _|  / _` |   \__, |  >  <   
            |_||_|  \__,_|   /__/_  |_||_|   _\__|  \__,_|   |___/  /_/\_\  
            _|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
            "`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

            ''') 

    try:
        hashtags_file = 'generated_hashtags.json'

        generate_hashtags() 

        hashtags = load_hashtags(hashtags_file)

        if not hashtags:
            return

        while True:
            try:
                num_links = int(input("Enter the number of links to retrieve: "))
                if num_links <= 0:
                    print("Please enter a number greater than 0.")
                    continue
                break  
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        while True:
            save_to_file_input = input("Do you want to save the output to a file? (yes/no): ").strip().lower()
            if save_to_file_input in ('yes', 'y'):
                save_to_file = True
                break
            elif save_to_file_input in ('no', 'n'):
                save_to_file = False
                break
            else:
                print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.")

        asyncio.run(search_tweets_and_print_links(hashtags, num_links, save_to_file))

    except KeyboardInterrupt:
        print("\nQuitting...")  
        exit(0)
    except Exception as e:
        print(f"Ran into a problem: {str(e)}\nSee You Soon...")
        exit(0)

    print("\nDone. Bye Bye...")
    exit(0)

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')
    username = config['X']['username']
    email = config['X']['email']
    password = config['X']['password']
    
    main()
