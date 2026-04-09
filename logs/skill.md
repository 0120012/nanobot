<skills>
  <skill available="true">
    <name>skill-creator</name>
    <description>Create or update AgentSkills. Use when designing, structuring, or packaging skills with scripts, references, and assets.</description>
    <location>/www/git/nanobot/nanobot/skills/skill-creator/SKILL.md</location>
  </skill>
  <skill available="false">
    <name>summarize</name>
    <description>Summarize or extract text/transcripts from URLs, podcasts, and local files (great fallback for “transcribe this YouTube/video”
    <location>/www/git/nanobot/nanobot/skills/whisper-stt-skill/SKILL.md</location>
  </skill>
  <skill available="true">
    <name>weather</name>
    <description>Get current weather and forecasts (no API key required).</description>
    <location>/www/git/nanobot/nanobot/skills/weather/SKILL.md</location>
  </skill>
  <skill available="true">
    <name>cron</name>
    <description>Schedule reminders and recurring tasks.</description>
    <location>/www/git/nanobot/nanobot/skills/cron/SKILL.md</location>
  </skill>
  <skill available="true">
    <name>tmux</name>
    <description>Remote-control tmux sessions for interactive CLIs by sending keystrokes and scraping pane output.</description>
    <location>/www/git/nanobot/nanobot/skills/tmux/SKILL.md</location>
  </skill>
  <skill available="false">
    <name>github</name>
    <description>Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries.</description>
    <location>/www/git/nanobot/nanobot/skills/github/SKILL.md</location>
    <requires>CLI: gh</requires>
  </skill>
  <skill available="true">
    <name>agent-browser</name>
    <description>Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating pages, filling forms, clicking buttons, taking screenshots, extracting data, testing web apps, or automating any browser task. Triggers include requests to "open a website", "fill out a form", "click a button", "take a screenshot", "scrape data from a page", "test this web app", "login to a site", "automate browser actions", or any task requiring programmatic web interaction.</description>
    <location>/www/git/nanobot/nanobot/skills/agent-browser/SKILL.md</location>
  </skill>
  <skill available="true">
    <name>clawhub</name>
    <description>Search and install agent skills from ClawHub, the public skill registry.</description>
    <location>/www/git/nanobot/nanobot/skills/clawhub/SKILL.md</location>
  </skill>
</skills>