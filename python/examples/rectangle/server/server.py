import uuid

from rectangle import Rectangle


class Server:

    def __init__(self):
        self.lut_name_to_class = {"Rectangle": Rectangle}
        self.lut_uuid_to_repr = {}
        self.lut_repr_to_uuid = {}

    def list_representations(self):
        return {'type': 'list', 'list': self.lut_name_to_class.keys()}

    def create_representation(self, args, kwargs):
        return self.response(self.lut_name_to_class[args[0]])

    def upload_representation(self, args, kwargs):
        return self.response(args[0])

    def call_representation(self, representation_uuid, args, kwargs):
        rep = self.lut_uuid_to_repr[representation_uuid]
        res = rep(*args, **kwargs)
        return self.response(res)

    def download_representation(self, representation_uuid):
        rep = self.lut_uuid_to_repr[representation_uuid]
        return {'type': 'object', 'object': rep}

    def release_representation(self, representation_uuid):
        representation = self.lut_uuid_to_repr[representation_uuid]
        del self.lut_repr_to_uuid[representation]
        del self.lut_uuid_to_repr[representation_uuid]
        return self.response(None)

    def create_attribute(self, representation_uuid, attribute_name):
        rep = self.lut_uuid_to_repr[representation_uuid]
        atr = getattr(rep, attribute_name)
        return self.response(atr)

    def response(self, result):

        if result is None:
            return {'type': 'none'}

        if result in self.lut_repr_to_uuid:
            representation_uuid = self.lut_repr_to_uuid[result]
        else:
            representation_uuid = str(uuid.uuid4())
            self.lut_repr_to_uuid[result] = representation_uuid
            self.lut_uuid_to_repr[representation_uuid] = result

        return {'type': 'uuid', 'uuid': representation_uuid}
