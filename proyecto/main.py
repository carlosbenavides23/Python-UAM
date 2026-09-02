import importlib
import pkgutil
from types import ModuleType

try:
    from . import utilidades
except ImportError:
    import utilidades


def importar_todos_los_modulos():
    modulos: list[ModuleType] = []
    for modulo in pkgutil.iter_modules(utilidades.__path__):
        if not modulo.ispkg:
            modulos.append(
                importlib.import_module(f"{utilidades.__name__}.{modulo.name}")
            )
    return modulos


def ejecutar_modulos(modulos):
    ejecutados = []
    for modulo in modulos:
        ejecutar = getattr(modulo, "main", None)
        if callable(ejecutar):
            ejecutar()
            ejecutados.append(modulo.__name__)
    return ejecutados


def main():
    modulos = importar_todos_los_modulos()
    ejecutados = ejecutar_modulos(modulos)

    operaciones = importlib.import_module(f"{utilidades.__name__}.operaciones")

    print(f"Módulos cargados: {len(modulos)}")
    if ejecutados:
        print(f"Módulos ejecutados: {', '.join(ejecutados)}")
    print(f"10 + 5 = {operaciones.suma(10, 5)}")


if __name__ == "__main__":
    main()
