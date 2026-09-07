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

To update later, run `git pull` inside the installed `ai-academy` directory.

Source: [OpenAI — Agent Skills](https://developers.openai.com/plugins/build/skills.md). Last verified 2026-09-07.
