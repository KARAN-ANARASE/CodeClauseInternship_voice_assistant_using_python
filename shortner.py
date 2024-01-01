# LINK SHORTENER USING PYTHON 5 LINES CODE ONLY
import pyshorteners
url = input('Enter the URL:')
s = pyshorteners.Shortener()
shortened_url = s.tinyurl.short(url)
print(f"Shortened URL: {shortened_url}")


