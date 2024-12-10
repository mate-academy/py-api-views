# Check Your Code Against the Following Points

## Code Style

1. Don't forget define the `related_name` for `ManyToManyField`.

2. Don't forget return `Response` with `errors` if serializer is not valid:

Good example:

```python
class GenreList(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Another good example:

```python
class GenreList(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

Bad example:

```python
class GenreList(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

Another bad example:

```python
class GenreList(APIView):
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
```

3. Group imports using `()` if needed.

Good example:

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin, 
    PermissionRequiredMixin,
)
```

Bad example:

```python
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin, PermissionRequiredMixin
```

Another bad example:

```python
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin, PermissionRequiredMixin,
)
```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
