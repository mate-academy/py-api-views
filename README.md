# API Views

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before starting.

Now, you are going to implement views via class-based views.

Create `Genre`, `Actor`, `CinemaHall` models and update `Movie` model to
the ones you wrote in Django ORM module. Modules should have such fields:
- `Actor`: `first_name`, `last_name`
- `Genre`: `name` (note: must be unique)
- `CinemaHall`: `name`, `rows`, `seats_in_row`
- `Movie`: `title`, `description`, `actors`, `genres`, `duration`. (note: you 
already have a new field here) 

Create serializers for all these models. Do not use related serializers for
ManyToMany relations.

Use the following command to load prepared data from fixture to test and debug your code:
  `python manage.py loaddata cinema_serviсe_db_data.json`.

Create views for models interaction endpoints via different class-based views:
- For the `Genre` model use an `APIView`
- For the `Actor` model use a `GenericAPIView`
- For the `CinemaHall` model use a `GenericViewSet`
- For the `Movie` model use a `ModelViewSet` and `routers`

Feel free to add more data using admin panel, if needed.

For every `<entity>` from `actors`, `genres`, `cinema_halls`, `movies`, such
endpoints should work:
* `GET api/cinema/<entity>/` - should return a list of the all entity items
* `POST api/cinema/<entity>/` - should create a new entity based on passed data
* `GET api/cinema/<entity>/<pk>/` - should return an entity with given id
* `PUT api/cinema/<entity>/<pk>/` - should update the entity with given id based on passed data
* `PATCH api/cinema/<entity>/<pk>/` - should partially update the entity with given id based on passed data
* `DELETE api/cinema/<entity>/<pk>/` - should delete the entity with given id

### Note: Check your code using this [checklist](checklist.md) before pushing your solution.
