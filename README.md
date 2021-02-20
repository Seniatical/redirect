# Redirect
Check if a website is hiding sneaky redirects for you!

**Usage:**
```py
import redirect

url = 'URL_HERE'

check = redirect.Redirect(url)

if check.is_redirect:
    print(check.redirect_url)
else:
    print(check.url)
```
