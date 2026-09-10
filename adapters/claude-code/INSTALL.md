# Install in Claude Code

Claude Code supports Agent Skills at the user level or inside a project. A user-level installation makes the Academy available across projects.

## macOS or Linux

```bash
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.claude/skills/ai-academy"
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.claude\skills\ai-academy"
```

Start the Academy with:

```text
/ai-academy
```

If Claude Code was already running when the top-level skill directory was created, restart it once. Claude Code normally detects later edits to an existing skill without a restart.

For a project-only install, clone the repository to `.claude/skills/ai-academy` in that project.

## Stay current

This install does not update itself. Curriculum and media change on `main`.

- In a terminal, `cd` into the installed `ai-academy` directory (`~/.claude/skills/ai-academy` or the project `.claude/skills/ai-academy`) and run `git pull`.
- Restart Claude Code if you just created the top-level skills folder; later pulls into an existing skill usually apply without a restart.
- What changed for learners: [`content/RELEASE_NOTES.md`](../../content/RELEASE_NOTES.md). Updating is optional and never required to finish a lesson you already started.

Source: [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills). Last verified 2026-09-07.
