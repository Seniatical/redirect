# Redirect
A simple python module to check websites!

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
