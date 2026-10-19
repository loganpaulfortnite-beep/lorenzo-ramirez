#!/usr/bin/env python3
"""Validación determinista del storyboard documental.

Uso:
    python3 validate_storyboard.py proyecto/storyboard.json
    python3 validate_storyboard.py proyecto/storyboard.json --check-files
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any
from urllib.parse import urlparse

VISUAL_TYPES = {"video", "archive", "graphic", "map", "chart", "document"}
MEDIA_TYPES = {"video", "archive", "document"}
GRAPHIC_TYPES = {"graphic", "map", "chart"}
TIMELINE_TOLERANCE = 0.08
DURATION_TOLERANCE = 0.15

def is_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    u = urlparse(value)
    return u.scheme in {"https", "http"} and bool(u.netloc)

def validate(data: dict[str, Any], *, check_files: bool = False, base_dir: str = ".") -> list[str]:
    errors: list[str] = []
    def err(message: str) -> None:
        errors.append(message)

    if not isinstance(data, dict):
        return ["La raíz del JSON debe ser un objeto."]
    try:
        duration = float(data["duration"])
        fps = float(data["fps"])
        width = int(data["width"])
        height = int(data["height"])
    except (KeyError, TypeError, ValueError):
        return ["Faltan duration, fps, width o height numéricos."]
    if duration <= 0 or fps not in {24, 25, 30, 50, 60}:
        err("La duración debe ser positiva y fps debe ser 24, 25, 30, 50 o 60.")
    if width < 1280 or height < 720 or width / height < 1.6 or width / height > 1.9:
        err("Resolución insuficiente o aspecto distinto del documental 16:9.")

    shots = data.get("shots")
    if not isinstance(shots, list) or not shots:
        return errors + ["shots debe ser una lista no vacía."]
    ids: set[str] = set()
    asset_ids: set[str] = set()
    fingerprints: set[str] = set()
    graphic_ids: set[str] = set()
    asset_hashes: set[str] = set()
    previous_end = 0.0
    duration_sum = 0.0
    for index, shot in enumerate(shots):
        label = f"shot[{index}]"
        if not isinstance(shot, dict):
            err(f"{label}: debe ser un objeto.")
            continue
        identifier = shot.get("id")
        if not identifier or not isinstance(identifier, str):
            err(f"{label}: id obligatorio.")
        elif identifier in ids:
            err(f"{label}: id repetido: {identifier}")
        else:
            ids.add(identifier)
        try:
            start = float(shot["start"])
            end = float(shot["end"])
            if start < 0 or end <= start:
                err(f"{label}: rango temporal inválido ({start}, {end}).")
            if abs(start - previous_end) > TIMELINE_TOLERANCE:
                err(f"{label}: hueco/solapamiento de {start - previous_end:+.3f}s.")
            if end - start > 25:
                err(f"{label}: plano >25 s; justificar editorialmente o dividir.")
            previous_end = end
            duration_sum += end - start
        except (KeyError, ValueError, TypeError):
            err(f"{label}: start y end deben ser números.")
        narration = shot.get("narration", "")
        target = shot.get("semantic_target", "")
        reason = shot.get("match_reason", "")
        if not isinstance(narration, str) or len(narration.strip()) < 5:
            err(f"{label}: falta narración transcrita.")
        if not isinstance(target, str) or len(target.strip()) < 9:
            err(f"{label}: falta sujeto visual específico (semantic_target).")
        if not isinstance(reason, str) or len(reason.strip()) < 22:
            err(f"{label}: match_reason debe justificar la correspondencia semántica (>=22 caracteres).")
        if shot.get("verified") is not True:
            err(f"{label}: requiere verified=true tras comprobación humana/editorial.")

        kind = shot.get("visual_type")
        if kind not in VISUAL_TYPES:
            err(f"{label}: visual_type desconocido {kind!r}.")
            continue
        if kind in MEDIA_TYPES:
            for key, used in (("asset_id", asset_ids), ("source_fingerprint", fingerprints)):
                value = shot.get(key)
                if not isinstance(value, str) or not value.strip():
                    err(f"{label}: falta {key}.")
                elif value in used:
                    err(f"{label}: RECURSO REPETIDO {key}={value}.")
                else:
                    used.add(value)
            for key in ("source_url", "license_url"):
                if not is_url(shot.get(key)):
                    err(f"{label}: falta URL verificable {key}.")
            license_name = shot.get("license")
            if not isinstance(license_name, str) or len(license_name.strip()) < 4:
                err(f"{label}: falta licencia/permisos aclarados.")
            asset_path = shot.get("asset_path")
            if not isinstance(asset_path, str) or not asset_path:
                err(f"{label}: asset_path requerido.")
            elif check_files:
                path = (Path(base_dir) / asset_path).resolve()
                if not path.is_file() or path.stat().st_size == 0:
                    err(f"{label}: archivo ausente/vacío: {path}")
            sha = shot.get("sha256")
            if sha:
                if sha in asset_hashes:
                    err(f"{label}: archivo duplicado SHA256={sha}")
                asset_hashes.add(sha)
        else:
            visual_id = shot.get("graphic_id")
            if not isinstance(visual_id, str) or not visual_id.strip():
                err(f"{label}: falta graphic_id.")
            elif visual_id in graphic_ids:
                err(f"{label}: GRÁFICO REPETIDO graphic_id={visual_id}.")
            else:
                graphic_ids.add(visual_id)
            question = shot.get("graphic_question")
            if not isinstance(question, str) or len(question.strip()) < 16:
                err(f"{label}: requiere pregunta cognitiva graphic_question.")
            moves = shot.get("graphic_storyboard")
            if not isinstance(moves, list) or len(moves) < 2 or any(not isinstance(m, str) or len(m.strip()) < 8 for m in moves):
                err(f"{label}: graphic_storyboard requiere >=2 pasos concretos.")
            why = shot.get("why_graphic")
            if not isinstance(why, str) or len(why.strip()) < 23:
                err(f"{label}: explicar por qué el vídeo real no basta (why_graphic).")
            if kind in {"map", "chart"} and not is_url(shot.get("data_source")):
                err(f"{label}: mapa/chart requiere data_source HTTP(S).")
    if abs(previous_end - duration) > DURATION_TOLERANCE:
        err(f"Fin {previous_end:.3f}s distinto de duración {duration:.3f}s.")
    if abs(duration_sum - duration) > DURATION_TOLERANCE:
        err(f"Suma de planos {duration_sum:.3f}s distinta de duración {duration:.3f}s.")
    return errors

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="QA del storyboard de Despegamos")
    parser.add_argument("storyboard", type=Path)
    parser.add_argument("--check-files", action="store_true", help="Comprobar medios descargados")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.storyboard.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: no se puede leer JSON: {exc}")
        return 2
    errors = validate(data, check_files=args.check_files, base_dir=str(args.storyboard.parent))
    if errors:
        print(f"FALLA QA: {len(errors)} errores en {args.storyboard}")
        for e in errors:
            print(" - " + e)
        return 1
    print(f"OK: {len(data['shots'])} planos, {data['duration']} segundos; sin recursos duplicados ni huecos.")
    print("ATENCIÓN: OK estructural NO sustituye revisión visual/editorial de los clips.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
