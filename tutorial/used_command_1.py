# 1 serialization

# pip install pygments  # We'll be using this for the code highlighting
# python manage.py startapp snippets
# python manage.py makemigrations snippets
# python manage.py migrate snippets

# python manage.py shell

# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()
# snippet = Snippet(code='print("hello, world")\n')
# snippet.save()

# serializer = SnippetSerializer(snippet)
# serializer.data # native python data
#     {'title': '', 'code': 'print("hello, world")', 'linenos': False, 'language': 'python', 'style': 'friendly'}
# content = JSONRenderer().render(serializer.data)
# content # json data

# import io
# stream = io.BytesIO(content)# byte obj
# data = JSONParser().parse(stream)
# data # nativ python data

# serializer = SnippetSerializer(data=data) # object instance
# serializer.is_valid() # True
# serializer.validated_data
#     OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
# serializer.save() # <Snippet: Snippet object>

# serializer = SnippetSerializer(Snippet.objects.all(), many=True)
# serializer.data
#     [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]),
#      OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'),
#                  ('linenos', False), ('language', 'python'), ('style', 'friendly')]),
#      OrderedDict([('id', 3), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), ]

# from snippets.serializers import SnippetSerializer
# serializer = SnippetSerializer()
# print(repr(serializer))
#     id = IntegerField(read_only=True)
#     title = CharField(allow_blank=True, max_length=100, required=False)
#     code = CharField(style={'base_template': 'textarea.html'})
#     linenos = BooleanField(required=False)
#     language = ChoiceField(choices=[('abap', 'ABAP'), ('abnf', 'ABNF'), ('actionscript', 'ActionScript')]
# quit() or exit()

# python manage.py runserver

# pip install httpie
# pip uninstall httpie
# pip freeze > requirements.txt
# http http://127.0.0.1:8000/def/snippets/
# http http://127.0.0.1:8000/def/snippets/2/

# http://127.0.0.1:8000/def/snippets/
