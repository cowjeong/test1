import tempfile

filename = tempfile.mktemp()
print(filename)

f = tempfile.NamedTemporaryFile(prefix="mytemp", suffix=".txt", dir=tempfile.gettempdir())
print(f.name)