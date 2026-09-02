"""Utilidades para generar reportes básicos desde ``main``."""

from __future__ import annotations

import inspect
import json
from datetime import datetime
from pathlib import Path
from types import ModuleType
from typing import Any, Iterable


def _resumen_modulo(modulo: ModuleType) -> dict[str, Any]:
    """Obtiene las funciones y clases definidas públicamente en un módulo."""
    funciones = []
    clases = []
    for nombre, objeto in inspect.getmembers(modulo):
        if nombre.startswith("_"):
            continue
        if inspect.isfunction(objeto) and objeto.__module__ == modulo.__name__:
            funciones.append(nombre)
        elif inspect.isclass(objeto) and objeto.__module__ == modulo.__name__:
            clases.append(nombre)
    return {
        "nombre": modulo.__name__,
        "funciones": sorted(funciones),
        "clases": sorted(clases),
    }


def generar_reporte(
    modulos: Iterable[ModuleType] | ModuleType | None = None,
) -> dict[str, Any]:
    """Genera un reporte básico a partir de todos los módulos indicados.

    Ejemplo de uso en ``main``::

            reporte = generar_reporte([modulo_usuarios, modulo_ventas])
    """
    if modulos is None:
        lista = []
    elif isinstance(modulos, ModuleType):
        lista = [modulos]
    else:
        lista = list(modulos)

    return {
        "fecha_generacion": datetime.now().isoformat(timespec="seconds"),
        "total_modulos": len(lista),
        "modulos": [_resumen_modulo(modulo) for modulo in lista],
    }


def guardar_reporte(reporte: dict[str, Any], ruta: str | Path = "reporte.json") -> Path:
    """Guarda el reporte en JSON y devuelve la ruta del archivo creado."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        json.dumps(reporte, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return destino


def generar_y_guardar_reporte(
    modulos: Iterable[ModuleType] | ModuleType | None = None,
    ruta: str | Path = "reporte.json",
) -> Path:
    """Atajo para que ``main`` genere y guarde el reporte en una sola llamada."""
    return guardar_reporte(generar_reporte(modulos), ruta)
