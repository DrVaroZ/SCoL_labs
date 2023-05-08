from serializers.json.json_parser import parse_json
from serializers.source.serializer import serialize, deserialize


class JsonSerializer:
    @staticmethod
    def dumps(item):
        return str(serialize(item)).replace("\n", "\\n")

    @staticmethod
    def dump(item, file):
        file.write(JsonSerializer.dumps(item))

    @staticmethod
    def loads(item):
        return deserialize(parse_json(item.replace("\\n", "\n")))

    @staticmethod
    def load(file):
        return JsonSerializer.loads(file.read())
