To start the API on your local - 

In the root directory
```
pipenv install
pipenv shell
```

Finally inside the shell - 
```
hypercorn main:app --reload
```