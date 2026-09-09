#!/usr/bin/env python3
"""Build the Microsoft Copilot Cowork distribution from canonical sources."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "packages" / "ai-academy-cowork.zip"
MAX_COMPANION_FILES = 20
MAX_TOTAL_BYTES = 10 * 1024 * 1024
MAX_SKILL_BYTES = 1 * 1024 * 1024

RUNTIME_FILES = (
    "SKILL.md",
    "assets/module-01-llm.png",
    "assets/prompt-engineering-map.png",
    "checks/module-01-llm.md",
    "checks/prompt-engineering.md",
    "curriculum/foundations.md",
    "curriculum/module-01-llm.md",
    "curriculum/onboarding.md",
    "curriculum/program-map.md",
    "curriculum/prompt-engineering.md",
    "exercises/module-01-llm.md",
    "exercises/prompt-engineering.md",
    "references/builder-mode.md",
    "resources/curated-content.md",
    "resources/module-01-analogies.md",
    "resources/visuals.md",
    "rubrics/interaction-grading.md",
    "schemas/progress-record.md",
    "ui/interaction-patterns.md",
)


def main() -> None:
    paths = [ROOT / relative for relative in RUNTIME_FILES]
    missing = [str(path.relative_to(ROOT)) for path in paths if not path.is_file()]
    if missing:
        raise SystemExit(f"Missing runtime files: {', '.join(missing)}")

    companion_count = len(paths) - 1
    total_bytes = sum(path.stat().st_size for path in paths)
    skill_bytes = (ROOT / "SKILL.md").stat().st_size

    if companion_count > MAX_COMPANION_FILES:
        raise SystemExit(
            f"Cowork permits {MAX_COMPANION_FILES} companion files; found {companion_count}."
        )
    if total_bytes > MAX_TOTAL_BYTES:
        raise SystemExit(
            f"Cowork permits {MAX_TOTAL_BYTES} total bytes; found {total_bytes}."
        )
    if skill_bytes > MAX_SKILL_BYTES:
        raise SystemExit(
            f"Cowork permits a {MAX_SKILL_BYTES}-byte SKILL.md; found {skill_bytes}."
        )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as archive:
        for path in paths:
            info = ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())

    print(
        f"Built {OUTPUT.relative_to(ROOT)} with {companion_count} companion files "
        f"({total_bytes} uncompressed bytes)."
    )


if __name__ == "__main__":
    main()
