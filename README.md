# Simple TODO app using Django
## Installation

Python and Django need to be installed
.

```bash
pip install django
```

## Usage
Goto main folder and run

```python
python manage.py runserver
```
Then go to the browser and enter the URL http://127.0.0.1:8000/

## Users side:
- View list of TODO items.
- Create a new TODO item.
- Edit existing TODO item.
- Delete a TODO item.

## Django admin interface:
- List display with all the fields including deleted from non-admin interface.
- Search and filtering .
- Download action to get bulk entries of todo list in csv format.

## APIs:
- To list all the todo items: http://127.0.0.1:8000/view
- To get the details of individual item: http://127.0.0.1:8000/view/<id>
