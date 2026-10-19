"""Tests autocontenidos del validador: python -m unittest discover -s scripts -p 'test_*.py'"""
from __future__ import annotations
import copy
import importlib.util
from pathlib import Path
import unittest

p = Path(__file__).with_name("validate_storyboard.py")
spec = importlib.util.spec_from_file_location("validate_storyboard", p)
mod = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(mod)

def fixture():
    return {
        "duration": 10.0, "fps": 25, "width": 1920, "height": 1080,
        "shots": [
            {
                "id": "s01", "start": 0, "end": 5,
                "narration": "La empresa construye máquinas de litografía.",
                "semantic_target": "ASML: sala real de maquinaria EUV",
                "visual_type": "video",
                "asset_id": "asml001",
                "asset_path": "sources/euv.mp4",
                "source_fingerprint": "asml:video-original-001",
                "source_url": "https://asml.com/media/example",
                "license_url": "https://asml.com/permissions",
                "license": "licencia explícita",
                "match_reason": "Muestra la máquina específica mencionada, no stock aleatorio.",
                "verified": True
            },
            {
                "id": "s02", "start": 5, "end": 10,
                "narration": "La luz pasa por espejos hacia la oblea.",
                "semantic_target": "secuencia técnica de espejos EUV",
                "visual_type": "graphic",
                "graphic_id": "euv-corte-001",
                "graphic_question": "¿Cómo se proyecta el patrón en una oblea?",
                "graphic_storyboard": ["Fuente de luz EUV se ilumina", "Espejos dirigen el haz y aparece la oblea"],
                "why_graphic": "El plano de la máquina no revela su interior óptico.",
                "match_reason": "Explica exactamente el mecanismo que describe el locutor.",
                "verified": True
            }
        ]
    }

class TestValidator(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(mod.validate(fixture()), [])
    def test_duplicate_video(self):
        d=fixture()
        dup=copy.deepcopy(d["shots"][0])
        dup.update(id="s03", start=5.0, end=10.0)
        d["shots"][1]=dup
        self.assertTrue(any("REPETIDO" in e for e in mod.validate(d)))
    def test_duplicate_graphic(self):
        d=fixture()
        d["shots"][0]=copy.deepcopy(d["shots"][1])
        d["shots"][0].update(id="s01", start=0.0, end=5.0)
        self.assertTrue(any("GRÁFICO REPETIDO" in e for e in mod.validate(d)))
    def test_timing_gap(self):
        d=fixture()
        d["shots"][1]["start"]=5.35
        self.assertTrue(any("hueco/solapamiento" in e for e in mod.validate(d)))
    def test_unverified(self):
        d=fixture()
        d["shots"][1]["verified"]=False
        self.assertTrue(any("verified=true" in e for e in mod.validate(d)))
    def test_missing_license(self):
        d=fixture()
        d["shots"][0]["license_url"]=""
        self.assertTrue(any("license_url" in e for e in mod.validate(d)))
    def test_bad_graph(self):
        d=fixture()
        d["shots"][1]["graphic_storyboard"]=["Aparece todo"]
        self.assertTrue(any("graphic_storyboard" in e for e in mod.validate(d)))
    def test_chart_source(self):
        d=fixture()
        d["shots"][1]["visual_type"]="chart"
        self.assertTrue(any("data_source" in e for e in mod.validate(d)))
    def test_missing_media_file(self):
        d=fixture()
        self.assertTrue(any("archivo ausente" in e for e in mod.validate(d,check_files=True)))
if __name__ == "__main__":
    unittest.main()
