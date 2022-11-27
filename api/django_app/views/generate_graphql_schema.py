from django.http import HttpResponse, HttpResponseNotFound

from api.django_app.graphql.schema import schema


def generate_graphql_schema(request):
    schema_path = "api/static/schema.graphql"
    __generate_schema__(schema_path)
    response = __create_response__(schema_path)
    return response


def __generate_schema__(schema_path: str):
    my_schema_str = schema.__str__()
    with open(schema_path, "w") as schema_file:
        schema_file.write(my_schema_str)


def __create_response__(schema_path: str):
    try:
        with open(schema_path) as f:
            file_data = f.read()

        content_type = "application/octet-stream"
        response = HttpResponse(file_data, content_type=content_type)
        response["Content-Disposition"] = 'attachment; filename="schema.graphql"'

    except OSError:
        response = HttpResponseNotFound("<h1>File does not exist</h1>")

    return response
