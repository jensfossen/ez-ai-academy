# Install in Microsoft Copilot Cowork

Cowork accepts custom skills from its Customize page or from a OneDrive skill folder. The prebuilt Academy package contains the canonical `SKILL.md` plus only the runtime learning files; development tests, site files, and GitHub configuration are excluded to stay within Cowork's package limits. The ZIP prefers numbered Modules 1–4. Foundations index, Models landscape lesson, curated-content registry, Graph Engineering live lesson, the Models landscape check, Module 1 analogies, and the Module 3–4 map PNGs stay in a full checkout; mentors skip those files when missing.

## Recommended: upload the package

1. Download [`packages/ai-academy-cowork.zip`](../../packages/ai-academy-cowork.zip).
2. In Cowork, open **Customize → Skills**.
3. Select the arrow next to **Add**, then **Upload skill**.
4. Choose the ZIP and accept Cowork's skill evaluation flow.
5. Start a new Cowork session and ask: **“Start EZ AI Academy as a new learner.”** Cursor slash aliases (`/ez-ai-academy`, `/start`) are not in this ZIP.

## OneDrive alternative

Extract the ZIP so these files live under:

```text
/Documents/Cowork/skills/ai-academy/
```

`SKILL.md` must be directly inside that folder. Cowork discovers OneDrive skills at the start of a session.

## Stay current

An uploaded ZIP is a snapshot. Cowork does not pull `main` for you.

- Download a fresh [`packages/ai-academy-cowork.zip`](../../packages/ai-academy-cowork.zip) from this repository (or rebuild it with `python scripts/package-cowork.py` after `git pull`).
- In Cowork, upload the new ZIP from **Customize → Skills** (same flow as first install), or replace the extracted files under `/Documents/Cowork/skills/ai-academy/`.
- Start a new Cowork session so the mentor loads the new `SKILL.md`.
- What changed for learners: [`content/RELEASE_NOTES.md`](../../content/RELEASE_NOTES.md) on GitHub. That file is not inside the ZIP. Updating is optional and never required to finish a lesson you already started.

## Package constraints

Microsoft currently allows a `SKILL.md` up to 1 MB, up to 20 companion files, and 10 MB total per skill. Run the repository packaging check before publishing a new ZIP:

```bash
python scripts/package-cowork.py
```

The script fails rather than producing a package that exceeds those limits. Cowork custom skills are currently unavailable on mobile.

Source: [Microsoft Learn — Use Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork). Last verified 2026-09-07.
