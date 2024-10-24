
# URL-Scrapper
Tool for SQL Injection attacks

A tool that allows you to combine sites with potential SQL Injection vulnerability into a single .txt file using google dorks and use it in bulk vulnerability search tools


## fix it for yourself
Remember to set the number of pages to be visit
```python
for _ in range(5):
```

selectors can sometimes change. find the selector and fix it
```python
search_results = driver.find_elements(By.XPATH, "//span[@jscontroller='msmzHf']/a")
```

  
## usage

run code

```bash
  python main.py
```

text to be used to search for potentially vulnerable sites example.

```bash
  details.php?id=
```
