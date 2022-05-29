import importlib
import inspect
import pkgutil

from django.contrib import admin

def _process_admin_module(module):
    """Inspect module, register admin.ModelAdmin classes with Django."""
    for _, val in inspect.getmembers(module):
        if inspect.isclass(val) and issubclass(val, admin.ModelAdmin):
            model = getattr(val, 'model', None)
            if model:
                admin.site.register(model, val)

def _import_module(module_name):
    """Import a module relative to this module."""
    return importlib.import_module('.%s' % module_name, __name__)

def _main():
    for _, module_name, _ in pkgutil.walk_packages(__path__):
        _process_admin_module(_import_module(module_name))

_main()
