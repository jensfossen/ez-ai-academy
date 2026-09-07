# Install in Microsoft Copilot Cowork

Cowork accepts custom skills from its Customize page or from a OneDrive skill folder. The prebuilt Academy package contains the canonical `SKILL.md` plus only the runtime learning files; development tests, site files, and GitHub configuration are excluded to stay within Cowork's package limits.

## Recommended: upload the package

1. Download [`packages/ai-academy-cowork.zip`](../../packages/ai-academy-cowork.zip).
2. In Cowork, open **Customize → Skills**.
3. Select the arrow next to **Add**, then **Upload skill**.
4. Choose the ZIP and accept Cowork's skill evaluation flow.
5. Start a new Cowork session and ask: **“Start Easy AI Academy as a new learner.”**

## OneDrive alternative

Extract the ZIP so these files live under:

```text
/Documents/Cowork/skills/ai-academy/
```

`SKILL.md` must be directly inside that folder. Cowork discovers OneDrive skills at the start of a session.

## Package constraints

Microsoft currently allows a `SKILL.md` up to 1 MB, up to 20 companion files, and 10 MB total per skill. Run the repository packaging check before publishing a new ZIP:

```bash
python scripts/package-cowork.py
```

The script fails rather than producing a package that exceeds those limits. Cowork custom skills are currently unavailable on mobile.

Source: [Microsoft Learn — Use Copilot Cowork](https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/use-cowork). Last verified 2026-09-07.
