"""Checks that pre-defense deliverables exist and are internally consistent."""
import csv
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md", ".gitignore", "CONTRIBUTING.md", "config/.env.example",
    "docs/01-project-proposal.md", "docs/02-evidence-of-relevance.md",
    "docs/03-literature-review.md", "docs/04-existing-systems-comparison.md",
    "docs/05-technology-comparison.md", "docs/06-requirements-specification.md",
    "docs/07-architecture-and-diagrams.md", "docs/08-ux-prototype.md",
    "docs/09-verification-and-evaluation-plan.md", "docs/10-project-management.md",
    "diagrams/src/01-system-context.mmd", "diagrams/src/02-use-cases.dot",
    "diagrams/src/03-components.mmd", "prototype/wireframes.html", "api/openapi.yaml",
]


def test_required_files_exist():
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    assert not missing, missing


def test_diagram_exports_exist_for_each_source():
    for src in (ROOT / "diagrams/src").iterdir():
        assert (ROOT / "diagrams/exports" / (src.stem + ".svg")).exists(), src.name


def test_openapi_is_valid_yaml_with_paths():
    spec = yaml.safe_load((ROOT / "api/openapi.yaml").read_text(encoding="utf-8"))
    assert spec["openapi"].startswith("3.")
    assert "/players/{playerId}/recommendations" in spec["paths"]
    for schema in spec["components"]["schemas"].values():
        assert "type" in schema


def test_rules_file_schema_and_unique_ids():
    data = yaml.safe_load((ROOT / "config/recommendation-rules.yaml").read_text(encoding="utf-8"))
    ids = [r["id"] for r in data["rules"]]
    assert len(ids) == len(set(ids))
    for r in data["rules"]:
        for key in ("id", "kpi", "condition", "recommendation", "rationale", "threshold_status"):
            assert key in r, (r["id"], key)


def test_literature_minimums():
    rows = list(csv.DictReader(open(ROOT / "docs/literature/literature-table.csv", encoding="utf-8")))
    assert len(rows) >= 12
    assert sum(r["type"] == "scientific" for r in rows) >= 8


def test_requirements_have_acceptance_criteria():
    text = (ROOT / "docs/06-requirements-specification.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^\| FR-\d+", text, re.M)) >= 15
    assert len(re.findall(r"^\| NFR-\d+", text, re.M)) >= 8


def test_no_obvious_secrets_committed():
    pattern = re.compile(r"(password|secret|api[_-]?key|token)\s*[:=]\s*['\"]?[A-Za-z0-9/+]{16,}", re.I)
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.suffix in {".py", ".yaml", ".yml", ".md", ".json", ".env", ".example"}:
            assert not pattern.search(p.read_text(encoding="utf-8", errors="ignore")), p
