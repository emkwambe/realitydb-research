from __future__ import annotations

import argparse
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

INVESTIGATORS = {"gemini", "deepseek", "kimi"}

COMMON_FILES = [
    ROOT / "00-charter" / "RESEARCH-CHARTER.md",
    ROOT / "00-charter" / "RESEARCH-STANDARDS.md",
    ROOT / "00-charter" / "SOURCE-HIERARCHY.md",
    ROOT / "00-charter" / "EVIDENCE-SCORING.md",
    ROOT / "01-missions" / "templates" / "MASTER-RESEARCH-PROMPT.md",
]


def read_required(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")

    content = path.read_text(encoding="utf-8").strip()

    if not content:
        raise ValueError(f"Required file is empty: {path}")

    return content


def find_mission_file(mission_id: str) -> Path:
    mission_dir = ROOT / "01-missions" / "active"

    matches = sorted(
        path
        for path in mission_dir.glob("*.md")
        if mission_id.upper() in path.read_text(
            encoding="utf-8", errors="ignore"
        ).upper()
    )

    if not matches:
        raise FileNotFoundError(
            f"No active mission containing '{mission_id}' was found in "
            f"{mission_dir}"
        )

    if len(matches) > 1:
        names = ", ".join(path.name for path in matches)
        raise RuntimeError(
            f"Multiple mission files matched '{mission_id}': {names}"
        )

    return matches[0]


def build_packet(mission_id: str, investigator: str) -> Path:
    investigator = investigator.lower().strip()

    if investigator not in INVESTIGATORS:
        valid = ", ".join(sorted(INVESTIGATORS))
        raise ValueError(
            f"Unknown investigator '{investigator}'. Valid values: {valid}"
        )

    mission_path = find_mission_file(mission_id)

    sections = [
        "# RealityDB Independent Research Packet",
        "",
        f"Investigator: {investigator.upper()}",
        f"Mission ID: {mission_id.upper()}",
        "",
        "You are receiving a self-contained research packet.",
        "You do not have access to the RealityDB research repository.",
        "Follow the instructions contained in this packet and return one complete response.",
        "",
    ]

    for path in COMMON_FILES:
        sections.extend(
            [
                "---",
                "",
                f"# Included Document: {path.name}",
                "",
                read_required(path),
                "",
            ]
        )

    sections.extend(
        [
            "---",
            "",
            f"# Included Mission: {mission_path.name}",
            "",
            read_required(mission_path),
            "",
            "---",
            "",
            "# Final Execution Instruction",
            "",
            f"Conduct this mission independently as {investigator.upper()}.",
            "Return only the completed research report.",
            "Use the exact required output headings and stable identifiers.",
            "Do not mention repository access or these packet-building instructions.",
            "",
        ]
    )

    output_dir = ROOT / "01-missions" / "packets" / investigator
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / f"{investigator.upper()}-{mission_id.upper()}.md"
    output_path.write_text("\n".join(sections), encoding="utf-8")

    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a self-contained RealityDB research packet."
    )
    parser.add_argument("mission_id", help="Mission ID, such as MISSION-001")
    parser.add_argument(
        "investigator",
        choices=sorted(INVESTIGATORS),
        help="Independent research tool",
    )

    args = parser.parse_args()

    try:
        output = build_packet(args.mission_id, args.investigator)
    except (FileNotFoundError, ValueError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Packet created: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())