# Install in Codex

Codex discovers personal skills from `~/.codex/skills`. Clone the repository directly into that directory so the repository root remains the skill root.

## macOS or Linux

```bash
mkdir -p "$HOME/.codex/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.codex/skills/ai-academy"
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.codex\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.codex\skills\ai-academy"
```

Restart Codex if the skill does not appear. Then start with:

```text
Use $ai-academy to start a new learning journey.
```

## Stay current

This install does not update itself. Curriculum and media change on `main`.

- In a terminal, `cd` into the installed `ai-academy` directory (`~/.codex/skills/ai-academy` on macOS/Linux) and run `git pull`.
- Restart Codex if the skill does not pick up the new files.
- What changed for learners: [`content/RELEASE_NOTES.md`](../../content/RELEASE_NOTES.md). Updating is optional and never required to finish a lesson you already started.

Source: [OpenAI — Agent Skills](https://developers.openai.com/plugins/build/skills.md). Last verified 2026-09-07.
