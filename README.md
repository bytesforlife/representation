![license](https://img.shields.io/github/license/bytesforlife/representation)
![swagger-validator](https://img.shields.io/swagger/valid/3.0?specUrl=https%3A%2F%2Fraw.githubusercontent.com%2Fbytesforlife%2Frepresentation%2Fmain%2Fapi%2Fopenapi.yaml)
![CodeQL](https://github.com/bytesforlife/representation/workflows/CodeQL/badge.svg)
![Pylint](https://raw.githubusercontent.com/bytesforlife/representation/main/.github/badges/pylint.svg)


# description

`representation` is a minimalistic cross-language client-server framework.
representations are client-side references to server-side objects.
they can be interacted with as if they were local objects.


# usage

## Python

```bash
pip install representation
```

```python
import representation

api = representation.Api('http://localhost:8080')

# create a reference to a server-side class
Rectangle = api.create('Rectangle')

# client-side code is executed server-side
rectangle = Rectangle(width=10, height=5)
area = rectangle.area()

# finally, return the value of the server-side object
print(api.download(area))
```


# how to report bugs

please [open an issue](https://github.com/bytesforlife/representation/issues/new)


# license

`representation` is free and open source software under the MIT license.
see the [`LICENSE`](https://github.com/bytesforlife/representation/tree/main/LICENSE) file for more information.
