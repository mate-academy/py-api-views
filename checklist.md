# Check Your Code Against the Following Points

## Don't forget to add `.gitignore` file BEFORE pushing

Make sure you don't push DB files (files with `.sqlite`, `.db3`, etc. extension).

Make sure you don't push `.pyc`, `.idea` files.


## Code Style
1. Avoid using an `if` condition to check if a serializer is valid. Instead, use the `raise_exception=True` flag when calling `serializer.is_valid()`. This will automatically raise a `ValidationError` if the data is invalid, which is then caught by the DRF exception handler to return a `400 Bad Request` response.


Good example:
```python
if request.method == 'POST':
    serializer = MovieSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
```

Bad example:
```python
if request.method == 'POST':
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

2. Make sure that your `Response` returns status code:

Good example:

```python
if request.method == "GET":
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)
```

Bad example:

```python
if request.method == "GET":
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
```

3. If you specify `max_length` then it's more reasonable 
to use `CharField` instead of `TextField`:

Good example:

```python
class Book(models.Model):
    description = models.CharField(max_length=255)
```

Bad example:

```python
class Book(models.Model):
    description = models.TextField(max_length=255)
```

4. Make sure that all your endpoints end with `/`:

Good example:

```python
urlpatterns = [
    path("movies/<pk>/", movie_detail, name="movie-detailed")
]
```

Bad example:

```python
urlpatterns = [
    path("movies/<pk>", movie_detail, name="movie-detailed")
]
```

5. Make sure you catch an error in `@api_view` in case that object doesn't exist. 
Use `get_object_or_404` instead of `try`/`except` for this purpose.

6. Make sure you've added a blank line at the end of all your files.
7. A serializer field is required by default. ([DRF required documentation](https://www.django-rest-framework.org/api-guide/fields/#required))
8. Your project should be one-styled, don't use double and single quotes at the same time. Double quotes are preferred.

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
