# Install in Cursor

## Clone the repository in Cursor

If Cursor is already installed:

1. Use **File → New Window → Clone repo** (or the Cursor **Clone repo** option).
2. Paste `https://github.com/jensfossen/ez-ai-academy`.
3. In chat, type `/` and choose `ai-academy`, or ask naturally to start EZ AI Academy.

## Other install paths

Use these when you want a personal skill across projects, a project-only copy, or a terminal clone.

### Personal skills folder

A personal install at `~/.cursor/skills` makes the Academy available across projects.

**macOS or Linux**

```bash
mkdir -p "$HOME/.cursor/skills"
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME/.cursor/skills/ai-academy"
```

**Windows PowerShell**

```powershell
New-Item -ItemType Directory -Force "$HOME\.cursor\skills" | Out-Null
git clone https://github.com/jensfossen/ez-ai-academy.git "$HOME\.cursor\skills\ai-academy"
```

Then start the same way: type `/` and choose `ai-academy`, or ask naturally to start EZ AI Academy.

### Project-only

Clone the repository to `.cursor/skills/ai-academy` or `.agents/skills/ai-academy` in that project. Cursor can also discover compatible Claude and Codex skill directories.

To update any clone later, run `git pull` inside the installed `ai-academy` directory.

## Cursor IDE chat vs Cloud Agent

These are different surfaces. Do not treat a Cloud Agent result as an IDE native-UI Pass. Rich-UI work is tracked in [#24](https://github.com/jensfossen/ez-ai-academy/issues/24). Research notes: [`RICH_UI.md`](RICH_UI.md).

**Cursor IDE chat** is the reference surface. Prefer native choice cards or blocks and in-chat video when the IDE provides them (plan-mode–like cards are the north-star analogy). Public Cursor docs do not publish a skill-author API for those widgets — do not invent one, and do not put host-specific markup in core curriculum. If a native control is missing, use the Markdown numbered-list and link fallbacks.

**Cursor Cloud Agent** uses Markdown fallbacks only. Cloud Agents may load `SKILL.md` from a checkout of this repository, or from a personal install after enabling **Settings → Agents → Sync Skills**. Cloud Agent chat uses numbered-list choices (native tappable cards are unavailable). Offer lesson video as an external link plus the text alternative; in-chat playback is not available. Image acceptance is a markdown image plus alt text, or a meaningful description; inline raster display is UI-dependent and not guaranteed.

Source: [Cursor — Agent Skills](https://cursor.com/docs/skills). Last verified 2026-09-07. IDE native-card and in-chat-video mechanisms remain research (see [#24](https://github.com/jensfossen/ez-ai-academy/issues/24)).
