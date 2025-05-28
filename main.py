import requests
import csv
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; Bot/1.0; +https://example.com/bot)"
}

def extract_subreddit_name(url):
    match = re.search(r"reddit\.com/r/([\w\d_]+)", url)
    return match.group(1) if match else None

def fetch_reddit_data(subreddit, use_proxy=False, proxies=None):
    url = f"https://www.reddit.com/r/{subreddit}.json"
    try:
        resp = requests.get(url, headers=headers, proxies=proxies if use_proxy else None, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        listing = data.get("data", {})
        after = listing.get("after")
        dist = listing.get("dist")
        children = listing.get("children", [])

        if not children:
            print(f"[!] No posts found in r/{subreddit}.")
            return None

        subscribers = children[0]["data"].get("subreddit_subscribers", "N/A")

        print(f"[✓] r/{subreddit}: {dist} posts, After = {after}, Subscribers = {subscribers}")
        return {
            "subreddit": subreddit,
            "posts_fetched": dist,
            "after_token": after,
            "subscribers": subscribers
        }

    except requests.RequestException as e:
        print(f"[!] Request error for r/{subreddit}:", e)
    except ValueError as e:
        print(f"[!] JSON parsing error for r/{subreddit}:", e)

    return None

# Load subreddit URLs from file
try:
    with open("subreddit.txt", "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("[!] File 'subreddit.txt' not found.")
    exit()

# Extract subreddit names
subreddits = [extract_subreddit_name(url) for url in urls]
subreddits = [s for s in subreddits if s]

if not subreddits:
    print("[!] No valid subreddits found.")
    exit()

# Proxy setup
proxy_file_exists = os.path.exists("proxy.txt") and os.path.getsize("proxy.txt") > 0
use_proxy = False
proxies = None

if proxy_file_exists:
    use_proxy_input = input("Do you want to use proxy from proxy.txt? (y/n): ").strip().lower()
    if use_proxy_input == "y":
        with open("proxy.txt", "r") as pf:
            line = pf.readline().strip()
            try:
                ip, port, user, password = line.split(":")
                proxy_auth = f"http://{user}:{password}@{ip}:{port}"
                proxies = {
                    "http": proxy_auth,
                    "https": proxy_auth
                }
                use_proxy = True
                print("[✓] Proxy is enabled.")
            except ValueError:
                print("[!] Invalid proxy format in 'proxy.txt'. Expected format: ip:port:user:pass")
                use_proxy = False
else:
    print("[!] No proxy file found or it is empty. Continuing without proxy.")

# Fetch subreddit data
results = []
for subreddit in subreddits:
    result = fetch_reddit_data(subreddit, use_proxy, proxies)
    if result:
        results.append(result)

# Save to TXT
with open("subreddit_results.txt", "w", encoding="utf-8") as txt_file:
    for item in results:
        txt_file.write(
            f"Subreddit: {item['subreddit']}\n"
            f"Posts fetched: {item['posts_fetched']}\n"
            f"After token: {item['after_token']}\n"
            f"Subscribers: {item['subscribers']}\n\n"
        )

# Save to CSV
with open("subreddit_results.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["subreddit", "posts_fetched", "after_token", "subscribers"])
    writer.writeheader()
    writer.writerows(results)

print("\n[✓] Data saved to 'subreddit_results.txt' and 'subreddit_results.csv'")
