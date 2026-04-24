import pyshorteners

def shorten_url():
    try:
        url = input("Enter long URL: ").strip()
        s = pyshorteners.Shortener()

        short_url = s.tinyurl.short(url)
        print("Short URL:", short_url)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    shorten_url()
