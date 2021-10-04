import os
import shutil
import json


def path(*args):
    return os.path.join('d:/Development/representation', *args)


def load_json(file):
    with open(file) as json_file:
        return json.load(json_file)


def replace_placeholders(path_in, path_out, replacements):
    with open(path_out, 'w+') as fo:
        with open(path_in) as fi:
            text = fi.read()
            for placeholder in replacements:
                text = text.replace(placeholder, replacements[placeholder])
            fo.write(text)


def copycontents(source, target):
    for entry in os.scandir(source):
        if entry.is_file():
            shutil.copy(entry, os.path.join(target, entry.name))
        if entry.is_dir():
            shutil.copytree(entry, os.path.join(target, entry.name))


def replace_in_file(file, search_for, replace_by):
    with open(file) as f:
        content = f.read()
    content = content.replace(search_for, replace_by)
    with open(file, "w") as f:
        f.write(content)


if __name__ == '__main__':

    shutil.copy(path('python', 'examples', 'server', 'openapi_server', '__main__.py'),
                path('python', '.dev', 'temp'))

    shutil.copy(path('python', 'examples', 'server', 'openapi_server', 'controllers', 'default_controller.py'),
                path('python', '.dev', 'temp'))

    shutil.rmtree(path('python', 'examples', 'server', 'openapi_server'))

    os.mkdir(path('python', 'examples', 'server', 'openapi_server'))

    os.system("java.exe -jar openapi-generator-cli-5.2.0.jar generate -g python-flask -i {} -o {}"
              .format(path('api', 'openapi.yaml'), path('python', '.dev', 'openapi')))

    copycontents(path('python', '.dev', 'openapi', 'openapi_server'),
                 path('python', 'examples', 'server', 'openapi_server'))

    shutil.copy(path('python', '.dev', 'temp', '__main__.py'),
                path('python', 'examples', 'server', 'openapi_server'))

    shutil.copy(path('python', '.dev', 'temp', 'default_controller.py'),
                path('python', 'examples', 'server', 'openapi_server', 'controllers'))

    shutil.rmtree(path('python', 'examples', 'server', 'openapi_server', 'test/'))

    os.remove(path('python', 'examples', 'server', 'openapi_server', 'controllers', '__init__.py'))
    os.remove(path('python', 'examples', 'server', 'openapi_server', 'controllers', 'security_controller_.py'))
    os.remove(path('python', 'examples', 'server', 'openapi_server', 'models', '__init__.py'))
    os.remove(path('python', 'examples', 'server', 'openapi_server', 'models', 'schema_error.py'))

    #replace_in_file(path('fdrtd/', 'webserver/', 'encoder.py'), 'openapi_server', 'fdrtd.webserver')
    #replace_in_file(path('fdrtd/', 'webserver/', 'util.py'), 'openapi_server', 'fdrtd.webserver')
    #replace_in_file(path('fdrtd/', 'webserver/', 'models', 'base_model_.py'), 'openapi_server', 'fdrtd.webserver')
    #replace_in_file(path('fdrtd/', 'webserver/', 'openapi', 'openapi.yaml'), 'openapi_server', 'fdrtd.webserver')
