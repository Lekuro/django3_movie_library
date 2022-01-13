# 4 Authentication and permissions
# new project is good idea

# rm -f db.sqlite3
# rm -r snippets/migrations
# python manage.py makemigrations snippets
# python manage.py migrate
# python manage.py createsuperuser

# http://127.0.0.1:8000/users/
# http://127.0.0.1:8000/users/2/
# http://127.0.0.1:8000/snippets/
# http://127.0.0.1:8000/snippets/2/

# http POST http://127.0.0.1:8000/snippets/ code="print(123)"
#     {"detail": "Authentication credentials were not provided."}

# http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(789)"
# {
#     "id": 1,
#     "owner": "admin",
#     "title": "foo",
#     "code": "print(789)",
#     "linenos": false,
#     "language": "python",
#     "style": "friendly"
# }
