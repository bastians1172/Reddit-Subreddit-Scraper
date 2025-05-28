
# Reddit Subreddit Scraper 🛠️

A Python script that fetches public subreddit data (like number of posts, pagination tokens, and subscriber count) from Reddit using its public JSON API. Supports multiple subreddits and optional proxy configuration.

---

## 🔧 Features

- ✅ Supports multiple subreddits (from `subreddit.txt`)
- 🌐 Optional proxy support (from `proxy.txt`)
- 📄 Exports data to both `.txt` and `.csv` formats
- 🛡️ Uses custom User-Agent to avoid request blocks
- ⏱️ Request timeout handling

---

## 📁 Project Structure

```

reddit-scraper/
├── main.py                 # The main script
├── subreddit.txt           # Input file: list of subreddit URLs
├── proxy.txt               # (Optional) Proxy credentials (ip\:port\:user\:pass)
├── subreddit\_results.txt   # Output in plain text format
├── subreddit\_results.csv   # Output in CSV format
├── recruitment.txt         # pip requirements
└── README.md               # This documentation

````

---

## 💻 Requirements

- Python 3.7 or newer
- Required library: `requests`

Install dependencies via pip:

```bash
pip install -r recruitment.txt
````

---

## 🧾 Setup Instructions

1. **Clone or download the repo**

   ```bash
   git clone https://github.com/your-username/reddit-scraper.git
   cd reddit-scraper
   ```

2. **Add subreddits to `subreddit.txt`**

   ```
   https://www.reddit.com/r/webscraping
   https://www.reddit.com/r/datascience
   ```

3. **(Optional) Add proxy to `proxy.txt`**

   Format: `ip:port:user:pass`

   ```
   123.45.67.89:10000:username:password
   ```

4. **Run the script**

   ```bash
   python main.py
   ```

5. **Answer the prompt**

   * `Do you want to use a proxy? (y/n):`

---

## 📤 Output Files

### 📄 subreddit\_results.txt

Plain text output example:

```
Subreddit: webscraping
Total posts fetched: 27
After token: t3_18z0k9f
Subscribers: 10589

----------------------------------------

Subreddit: datascience
Total posts fetched: 25
After token: t3_18z9l5g
Subscribers: 1643200
```

### 📊 subreddit\_results.csv

CSV file viewable in Excel or Google Sheets:

| Subreddit   | TotalPosts | AfterToken  | Subscribers |
| ----------- | ---------- | ----------- | ----------- |
| webscraping | 27         | t3\_18z0k9f | 10589       |
| datascience | 25         | t3\_18z9l5g | 1643200     |

---

## ⚠️ Notes

* This tool uses Reddit’s **public** API (`.json` endpoints).
* Be respectful of Reddit’s terms of use – don’t abuse this for spam.
* If the request fails due to rate limiting or proxy issues, appropriate error messages will be displayed.

---

## 🧠 Use Cases

* Competitive subreddit research
* Data pipeline testing with public data
* Educational use for web scraping learners

---

## 🤖 Author

Created for educational purposes by Bastian 

---

## 📜 License

This project is open-source and available for learning or internal use.
Not intended for abuse or scraping personal/private data.

```

---

Kalau kamu butuh versi GitHub-ready (beserta badge, license, dsb), tinggal bilang bro.
```
#
