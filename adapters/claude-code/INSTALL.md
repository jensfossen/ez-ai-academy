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

For a project-only install, clone the repository to `.claude/skills/ai-academy` in that project. To update either installation, run `git pull` inside the installed directory.

Source: [Claude Code — Extend Claude with skills](https://code.claude.com/docs/en/skills). Last verified 2026-09-07.
