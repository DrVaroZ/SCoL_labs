from serializers.xml.xml_parser import dumps_from_dict, loads_to_dict
from serializers.source.serializer import serialize, deserialize


class XmlSerializer:
    @staticmethod
    def dumps(obj):
        obj = serialize(obj)

        return dumps_from_dict(obj)

    @staticmethod
    def loads(item):
        item = loads_to_dict(item)

        return deserialize(item)

    @staticmethod
    def dump(item, file):
        file.write(XmlSerializer.dumps(item))

    @staticmethod
    def load(file):
        return XmlSerializer.loads(file.read())
