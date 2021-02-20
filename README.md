# Redirect
A simple python module to check websites!

**Usage:**
```py
import redirect

url = 'URL_HERE'

redir = redirect.check(url)
if redir:
    print('Found a fishy site!')
else:
    print('Looks safe to me!')
```
