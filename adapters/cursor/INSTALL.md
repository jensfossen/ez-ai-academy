# Install in Cursor

Cursor supports Agent Skills in personal and project directories. A personal installation makes the Academy available across projects.

## macOS or Linux

```bash
mkdir -p "$HOME/.cursor/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.cursor/skills/ai-academy"
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force "$HOME\.cursor\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.cursor\skills\ai-academy"
```

In Cursor chat, type `/` and select `ai-academy`. You can also ask naturally to start Easy AI Academy.

For a project-only install, clone the repository to `.cursor/skills/ai-academy` or `.agents/skills/ai-academy` in that project. Cursor can also discover compatible Claude and Codex skill directories. If you use Cursor Cloud Agents, enable skill synchronization in **Settings → Agents → Sync Skills** for personal skills.

To update later, run `git pull` inside the installed `ai-academy` directory.

Source: [Cursor — Agent Skills](https://cursor.com/docs/skills). Last verified 2026-09-07.
