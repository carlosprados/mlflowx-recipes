import importlib

from opengate.recipes.anomaly.v1.recipe import AnomalyRecipe
def _get_class_from_string(fully_qualified_class_name):
    module, class_name = fully_qualified_class_name.rsplit(".", maxsplit=1)
    test = importlib.import_module(module)
    return getattr(test, class_name)
