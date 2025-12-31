#!/usr/bin/env python3
"""
Validador del repositorio de Circuitos Eléctricos.
Verifica la estructura de carpetas y archivos del repositorio.
Incluye verificación de archivos de simulación Proteus (.pdsprj).
"""

import os
import json
from pathlib import Path


def validate_module_structure(module_path: Path) -> list:
    """Valida la estructura de un módulo."""
    errors = []
    warnings = []
    
    # Archivos y carpetas requeridos
    required_files = ['00-Intro.md', 'Resumen-Formulas.md', 'manifest.json']
    required_folders = ['theory', 'methods', 'problems', 'simulation']
    
    for item in required_files:
        item_path = module_path / item
        if not item_path.exists():
            errors.append(f"❌ Falta archivo: {item} en {module_path.name}")
    
    for folder in required_folders:
        folder_path = module_path / folder
        if not folder_path.exists():
            errors.append(f"❌ Falta carpeta: {folder}/ en {module_path.name}")
    
    return errors, warnings


def validate_manifest(manifest_path: Path) -> list:
    """Valida el contenido de manifest.json."""
    errors = []
    warnings = []
    
    required_fields = ['id', 'name', 'description', 'topics', 'status']
    recommended_fields = ['software_requirements', 'difficulty_levels', 'resource_map']
    
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for field in required_fields:
            if field not in data:
                errors.append(f"❌ Campo faltante '{field}' en {manifest_path.parent.name}/manifest.json")
        
        for field in recommended_fields:
            if field not in data:
                warnings.append(f"⚠️ Campo recomendado '{field}' faltante en {manifest_path.parent.name}/manifest.json")
                
    except json.JSONDecodeError as e:
        errors.append(f"❌ Error JSON en {manifest_path}: {e}")
    except FileNotFoundError:
        errors.append(f"❌ No se encuentra: {manifest_path}")
    
    return errors, warnings


def validate_simulation_files(module_path: Path) -> tuple:
    """Valida la existencia de archivos de simulación Proteus."""
    errors = []
    warnings = []
    info = []
    
    simulation_path = module_path / 'simulation'
    if simulation_path.exists():
        pdsprj_files = list(simulation_path.glob('*.pdsprj'))
        dsn_files = list(simulation_path.glob('*.dsn'))
        
        if pdsprj_files:
            info.append(f"📁 {module_path.name}: {len(pdsprj_files)} archivo(s) .pdsprj encontrado(s)")
        elif dsn_files:
            info.append(f"📁 {module_path.name}: {len(dsn_files)} archivo(s) .dsn encontrado(s)")
        else:
            warnings.append(f"⚠️ No hay archivos de simulación en {module_path.name}/simulation/")
    
    return errors, warnings, info


def validate_file_naming(module_path: Path) -> list:
    """Valida la nomenclatura de archivos según el estándar."""
    warnings = []
    
    prefixes = {
        'theory': 'TH-',
        'methods': 'MT-',
        'problems': ['PR-', 'EJ-'],
        'simulation': 'SIM-'
    }
    
    for folder, expected_prefix in prefixes.items():
        folder_path = module_path / folder
        if folder_path.exists():
            for file in folder_path.iterdir():
                if file.is_file() and file.suffix == '.md':
                    if isinstance(expected_prefix, list):
                        if not any(file.name.startswith(p) for p in expected_prefix):
                            warnings.append(f"⚠️ Nomenclatura: {file.name} debería iniciar con {' o '.join(expected_prefix)}")
                    else:
                        if not file.name.startswith(expected_prefix) and file.name != '.gitkeep':
                            warnings.append(f"⚠️ Nomenclatura: {file.name} debería iniciar con {expected_prefix}")
    
    return warnings


def validate_repository(repo_root: Path) -> tuple:
    """Valida la estructura completa del repositorio."""
    all_errors = []
    all_warnings = []
    all_info = []
    
    # Verificar carpetas principales
    main_folders = ['00-META', '01-Circuitos-CD', '02-Circuitos-CA']
    for folder in main_folders:
        folder_path = repo_root / folder
        if not folder_path.exists():
            all_errors.append(f"❌ Carpeta principal faltante: {folder}")
    
    # Verificar spice-models
    spice_path = repo_root / '00-META' / 'spice-models'
    if not spice_path.exists():
        all_warnings.append("⚠️ Carpeta 00-META/spice-models/ no encontrada")
    else:
        all_info.append("✅ Carpeta spice-models/ encontrada")
    
    # Validar módulos de CD
    cd_path = repo_root / '01-Circuitos-CD'
    if cd_path.exists():
        for module_dir in sorted(cd_path.iterdir()):
            if module_dir.is_dir() and module_dir.name.startswith(('01-', '02-', '03-', '04-', '05-')):
                errors, warnings = validate_module_structure(module_dir)
                all_errors.extend(errors)
                all_warnings.extend(warnings)
                
                manifest = module_dir / 'manifest.json'
                if manifest.exists():
                    errors, warnings = validate_manifest(manifest)
                    all_errors.extend(errors)
                    all_warnings.extend(warnings)
                
                errors, warnings, info = validate_simulation_files(module_dir)
                all_errors.extend(errors)
                all_warnings.extend(warnings)
                all_info.extend(info)
                
                all_warnings.extend(validate_file_naming(module_dir))
    
    # Validar módulos de CA
    ca_path = repo_root / '02-Circuitos-CA'
    if ca_path.exists():
        for module_dir in sorted(ca_path.iterdir()):
            if module_dir.is_dir() and module_dir.name.startswith(('01-', '02-', '03-', '04-', '05-', '06-')):
                errors, warnings = validate_module_structure(module_dir)
                all_errors.extend(errors)
                all_warnings.extend(warnings)
                
                manifest = module_dir / 'manifest.json'
                if manifest.exists():
                    errors, warnings = validate_manifest(manifest)
                    all_errors.extend(errors)
                    all_warnings.extend(warnings)
                
                errors, warnings, info = validate_simulation_files(module_dir)
                all_errors.extend(errors)
                all_warnings.extend(warnings)
                all_info.extend(info)
                
                all_warnings.extend(validate_file_naming(module_dir))
    
    return all_errors, all_warnings, all_info


def print_summary(errors: list, warnings: list, info: list):
    """Imprime un resumen formateado de la validación."""
    print("\n" + "=" * 60)
    print("📊 RESUMEN DE VALIDACIÓN DEL REPOSITORIO")
    print("=" * 60)
    
    if info:
        print("\n📋 Información:")
        for item in info:
            print(f"   {item}")
    
    if warnings:
        print(f"\n⚠️ Advertencias ({len(warnings)}):")
        for warning in warnings:
            print(f"   {warning}")
    
    if errors:
        print(f"\n❌ Errores ({len(errors)}):")
        for error in errors:
            print(f"   {error}")
    
    print("\n" + "-" * 60)
    if not errors and not warnings:
        print("✅ El repositorio tiene una estructura válida y completa.")
    elif not errors:
        print(f"✅ Estructura válida con {len(warnings)} advertencia(s).")
    else:
        print(f"❌ Se encontraron {len(errors)} error(es) y {len(warnings)} advertencia(s).")
    print("=" * 60 + "\n")


def main():
    """Función principal."""
    repo_root = Path(__file__).parent.parent.parent
    
    print("\n🔍 Validando repositorio de Circuitos Eléctricos...")
    print(f"📁 Ruta: {repo_root}")
    
    errors, warnings, info = validate_repository(repo_root)
    print_summary(errors, warnings, info)
    
    return 1 if errors else 0


if __name__ == "__main__":
    exit(main())
