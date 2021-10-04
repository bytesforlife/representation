import connexion
import six

from openapi_server.models.args_kwargs import ArgsKwargs  # noqa: E501
from openapi_server.models.inline_response_default import InlineResponseDefault  # noqa: E501
from openapi_server import util


def call_representation(representation_uuid, args_kwargs):  # noqa: E501
    """call a server-side object

    call a server-side object such as a static function, a member function, or in case of a class, its constructor # noqa: E501

    :param representation_uuid: 
    :type representation_uuid: 
    :param args_kwargs: an ordered list of unnamed arguments, followed by a key-value dictionary of named arguments
    :type args_kwargs: dict | bytes

    :rtype: Dict[str, object]
    """
    if connexion.request.is_json:
        args_kwargs = ArgsKwargs.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_attribute(representation_uuid, attribute_name):  # noqa: E501
    """create a representation of an attribute of a representation

    create a representation of an attribute of a representation # noqa: E501

    :param representation_uuid: 
    :type representation_uuid: 
    :param attribute_name: 
    :type attribute_name: str

    :rtype: Dict[str, object]
    """
    return 'do some magic!'


def create_representation(args_kwargs):  # noqa: E501
    """create a representation

    create a representation, a client-side reference to a server-side object. the representation will be wrapped client-side, so that it may be interacted with as if it were a local object. # noqa: E501

    :param args_kwargs: an ordered list of unnamed arguments, followed by a key-value dictionary of named arguments
    :type args_kwargs: dict | bytes

    :rtype: Dict[str, object]
    """
    if connexion.request.is_json:
        args_kwargs = ArgsKwargs.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def download_representation(representation_uuid):  # noqa: E501
    """download a serialized version of a server-side object

    download a serialized version of a server-side object itself (instead of its representation). think of this as a de-referencing operation, downloading the object to the client. # noqa: E501

    :param representation_uuid: 
    :type representation_uuid: 

    :rtype: Dict[str, object]
    """
    return 'do some magic!'


def list_representations():  # noqa: E501
    """list available server-side objects

    returns a list of server-side objects that are available to be represented client-side. typical choices are classes, static functions, and other singletons. instances, their attributes, and other variables may also be referenced. # noqa: E501


    :rtype: Dict[str, object]
    """
    return 'do some magic!'


def release_representation(representation_uuid):  # noqa: E501
    """release a representation

    release the representation of a server-side object # noqa: E501

    :param representation_uuid: 
    :type representation_uuid: 

    :rtype: Dict[str, object]
    """
    return 'do some magic!'


def upload_representation(args_kwargs):  # noqa: E501
    """upload an object, and return its representation

    upload an object to the server, and return a reference for future interaction. # noqa: E501

    :param args_kwargs: an ordered list of unnamed arguments, followed by a key-value dictionary of named arguments
    :type args_kwargs: dict | bytes

    :rtype: Dict[str, object]
    """
    if connexion.request.is_json:
        args_kwargs = ArgsKwargs.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
