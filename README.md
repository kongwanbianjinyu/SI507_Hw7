# SI507_Hw7

This is Hw7 for SI507 University of Michigan. For this assignment, I will create a basic Flask application, that greets a user
and tells them the top technology news stories for that day. I would retrieve the top 5 articles from the New York Times from the technology section.

## Get API keys

You need to obtain an API key for Top Stories API on New York Times. The link to get the API key and the documentation can be found at https://developer.nytimes.com/. Make sure to include your API key in a file called “secrets.py” with a line:
```
api_key = ""
```
## Output
1.If the user goes to the default homepage (http://127.0.0.1:5000/), your output should be "Welcome".
2.If the user goes to the (http://127.0.0.1:5000/name/{Your Name}), your output should be "Hello, {Your Name}!".
3.If the user goes to the (http://127.0.0.1:5000/headlines/{Your Name}), your output should be NYT headlines of “Technology” category.

## Extra Credit
1.If the user goes to the (http://127.0.0.1:5000/links/{Your Name}), your output should be NYT headlines of “Technology” category with link.
2.If the user goes to the (http://127.0.0.1:5000/images/{Your Name}), your output should get a table of “Technology” category stories. The first column are ids, the second column are headlines and the last column are images thumbnails.


