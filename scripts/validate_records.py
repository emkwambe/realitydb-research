from pathlib import Path
import sys
import yaml

REQUIRED_FIELDS = {
    "source_id",
    "company",
    "industry",
    "source_url",
    "evidence_classification",
}


def validate_yaml(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        record = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        return [f"{path}: invalid YAML: {exc}"]

    missing = sorted(field for field in REQUIRED_FIELDS if not record.get(field))
    if missing:
        errors.append(f"{path}: missing required fields: {', '.join(missing)}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    files = list((root / "data" / "raw").rglob("*.yaml"))
    errors = [error for path in files for error in validate_yaml(path)]

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Validated {len(files)} YAML research records.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
