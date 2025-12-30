#!/usr/bin/env python3
"""
Validador del repositorio de Circuitos Eléctricos.
Verifica la estructura de carpetas y archivos del repositorio.
"""

import os
import json
from pathlib import Path


def validate_module_structure(module_path: Path) -> list:
    """Valida la estructura de un módulo."""
    errors = []
    required_items = ['00-Intro.md', 'theory', 'methods', 'problems', 
                      'Resumen-Formulas.md', 'manifest.json']
    
    for item in required_items:
        item_path = module_path / item
        if not item_path.exists():
            errors.append(f"Falta: {item} en {module_path}")
    
    return errors


def validate_manifest(manifest_path: Path) -> list:
    """Valida el contenido de manifest.json."""
    errors = []
    required_fields = ['id', 'name', 'description', 'topics', 'status']
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for field in required_fields:
            if field not in data:
                errors.append(f"Campo faltante '{field}' en {manifest_path}")
    except json.JSONDecodeError as e:
        errors.append(f"Error JSON en {manifest_path}: {e}")
    except FileNotFoundError:
        errors.append(f"No se encuentra: {manifest_path}")
    
    return errors


def validate_repository(repo_root: Path) -> list:
    """Valida la estructura completa del repositorio."""
    all_errors = []
    
    # Verificar carpetas principales
    main_folders = ['00-META', '01-Circuitos-CD', '02-Circuitos-CA']
    for folder in main_folders:
        folder_path = repo_root / folder
        if not folder_path.exists():
            all_errors.append(f"Carpeta principal faltante: {folder}")
    
    # Validar módulos de CD
    cd_path = repo_root / '01-Circuitos-CD'
    if cd_path.exists():
        for module_dir in cd_path.iterdir():
            if module_dir.is_dir() and module_dir.name.startswith(('01-', '02-', '03-', '04-', '05-')):
                all_errors.extend(validate_module_structure(module_dir))
                manifest = module_dir / 'manifest.json'
                if manifest.exists():
                    all_errors.extend(validate_manifest(manifest))
    
    # Validar módulos de CA
    ca_path = repo_root / '02-Circuitos-CA'
    if ca_path.exists():
        for module_dir in ca_path.iterdir():
            if module_dir.is_dir() and module_dir.name.startswith(('01-', '02-', '03-', '04-', '05-', '06-')):
                all_errors.extend(validate_module_structure(module_dir))
                manifest = module_dir / 'manifest.json'
                if manifest.exists():
                    all_errors.extend(validate_manifest(manifest))
    
    return all_errors


def main():
    """Función principal."""
    repo_root = Path(__file__).parent.parent.parent
    
    print("Validando repositorio de Circuitos Eléctricos...")
    print(f"Ruta: {repo_root}")
    print("-" * 50)
    
    errors = validate_repository(repo_root)
    
    if errors:
        print(f"\n❌ Se encontraron {len(errors)} errores:\n")
        for error in errors:
            print(f"  • {error}")
        return 1
    else:
        print("\n✅ El repositorio tiene una estructura válida.")
        return 0


if __name__ == "__main__":
    exit(main())
