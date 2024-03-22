import importlib
import pkgutil
import plugins
from flask import Flask

app =  Flask(__name__)
for _, name, _ in pkgutil.iter_modules(plugins.__path__, plugins.__name__ + "."):
    module =  importlib.import_module(name)
    try:
        app.register_blueprint(getattr(module, "blueprint_plugin"))
    except Exception as e:
        print("Exception: ", e)


@app.route('/')
def index():
    return 'MAIN PAGE'

print('url_map:')
print(app.url_map)
#app.run(host= '0.0.0.0', port=8080, debug=True)
