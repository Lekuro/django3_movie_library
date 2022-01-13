# 3 Class-based View

# request.POST  # Only handles form data.  Only works for 'POST' method.
# request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

# return Response(data)  # Renders to content type as requested by the client.

# http http://127.0.0.1:8000/api/snippets/
# http http://127.0.0.1:8000/api/snippets/2/

# http://127.0.0.1:8000/api/snippets/
# http://127.0.0.1:8000/api/snippets/2/

# http://127.0.0.1:8000/mixin/snippets/
# http://127.0.0.1:8000/mixin/snippets/2/

# http://127.0.0.1:8000/generic/snippets/
# http://127.0.0.1:8000/generic/snippets/2/

# python manage.py runserver

# We can control the format of the response that we get back, either by using the Accept header:
# http http://127.0.0.1:8000/api/snippets/ Accept:application/json  # Request JSON
# http http://127.0.0.1:8000/api/snippets/ Accept:text/html         # Request HTML

# Or by appending a format suffix:
# http http://127.0.0.1:8000/api/snippets.json  # JSON suffix
# http http://127.0.0.1:8000/api/snippets.api   # Browsable API suffix

# Similarly, we can control the format of the request that we send, using the Content-Type header.
# POST using form data
# http --form POST http://127.0.0.1:8000/api/snippets/ code="print(123)"

# POST using JSON
# http --json POST http://127.0.0.1:8000/api/snippets/ code="print(456)"

# http --form --debug POST http://127.0.0.1:8000/api/snippets/ code="print(123)"
# http --json --debug POST http://127.0.0.1:8000/api/snippets/ code="print(456)"
