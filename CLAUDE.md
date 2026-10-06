# CLAUDE.md

Instructions for Claude when working in this repository.

## What this repo is

Released artifacts for the paper *Capability Is Not Deployability: The Office of
the CFO as a Distinct, Under-Benchmarked Domain for AI Agents*. Every number in
the paper must be derivable from the files here. See `README.md` for the file
map and `protocol.md` for the registered protocol.

The FinNLP 2026 submission (#111) was rejected on 31 Aug 2026 (scores
6/6/6/4/7, mean 5.8). The review points are already tracked in Linear and the
outcome is recorded in Notion; use those, do not recreate them (see below).

## Ground rules (apply to all work)

1. **Run `python3 recount.py` before and after any change** to a CSV, a note or
   a count. It must exit 0 or the paper and data disagree. If a change makes it
   fail on purpose (for example resolving screening records), update the script
   and the manuscript numbers together and say so in the commit.
2. **Never invent evidence.** Every coded cell needs an exact quotation and
   section in `notes/`. If a paper cannot be read in full, mark it pending; do
   not code it from the abstract.
3. **Date every negative claim** ("no dedicated benchmark identified as of
   <month year>"). When the search window moves, update the date everywhere.
4. **Keep AI-assisted work disclosed.** Search, screening and coding done by
   Claude must be recorded in `protocol.md` (what was done, what context the
   coder saw). A human second coder is still owed (see Linear).
5. **No model identifiers** in commits, notes, file contents or tracker items.
6. Edit CSVs by script or careful diff, never by hand-reformatting the file.

## Where things are tracked

| Need | Tool | Why |
|---|---|---|
| Work to do, status, owners, deadlines | **Linear** | One issue per unit of work, with a clear done-state |
| Reasoning, decisions, long-form writing, meeting notes | **Notion** | Durable, searchable, shareable prose |
| Data, code, protocol, evidence notes | **This repo (git)** | The source of truth for results |

Rule of thumb: if it has a "done" state, it is a Linear issue. If it explains
*why*, it is a Notion page. If it is a result, it lives in git. Link all three
to each other; never copy content between them.

This project already exists in both tools. **Find and update the existing items;
never create a parallel project, page or duplicate issue.**

- Linear project: `Q · FinNLP #111 (LIVE submission — archival, do not lose)`.
  Look it up with `list_projects` / `list_issues`; the team is the one that owns
  that project.
- Linear issues in it: EB1-45 (48 unresolved records, Done), EB1-46 (make the
  four dimensions conditional), EB1-47 (second human coder), EB1-48 (re-anchor
  to current APQC PCF), EB1-49 (cut to one paper), EB1-50 (decide: build the
  runnable benchmark or ship as a resource paper). EB1-10 and EB1-24 are closed.
- Notion: the paper's row in the author's evidence binder, found by searching
  `Capability Is Not Deployability`. It records the decision and the path back.
- **EB1-50 is the gating decision.** It says to decide before doing the other
  work. Do not start building a benchmark or restructuring the paper until the
  user has decided it, and remind them if it is overdue.
- **Keep private matters out of this repo.** The Linear team and the Notion
  binder also track unrelated personal and career items. Never copy those into
  commits, `CLAUDE.md`, notes or any released file, and do not read unrelated
  items.

## Linear conventions

**Create or update issues only when the user asks or the task clearly calls for
it. Search first (`list_issues`) to avoid duplicates.**

- **One issue per review point or work unit**, titled with a verb:
  `Resolve 48 unresolved screening records`, not `Search recall`.
- **Description template:**
  - *Why* (quote the reviewer point or limitation, name the reviewer)
  - *Done when* (checkable acceptance criteria, usually "`recount.py` passes
    and paper numbers updated")
  - *Files touched* (paths in this repo)
  - *Links* (Notion page, commit or PR)
- **Labels:** `search-recall`, `coding-validity`, `taxonomy`, `governance-rule`,
  `writing`, `benchmark-build`, `admin`.
- **Priority** follows how many reviewers raised it: 4 reviewers = Urgent/High,
  2 = Medium, 1 = Low.
- **Parent issue** per rejection round (`Revision after FinNLP 2026 reject`)
  with sub-issues for each item.
- **Status flow:** Backlog -> Todo -> In Progress -> In Review -> Done. Move an
  issue to Done only after `recount.py` passes on the final commit.
- Reference the issue ID in branch names and commit messages
  (`ABC-12: resolve screening records 1-24`).
- Comment on the issue when a decision changes scope. Do not close issues for
  work that was skipped; mark them Canceled with the reason.

## Notion conventions

**Create pages only for durable content, and say where you created them.** If
no parent page is given, create a private draft and tell the user.

Update the existing paper page rather than creating new structure. Put
decisions and their reasons there (date, decision, alternatives, reason, linked
Linear issue, linked commit). Only add a child page when content is too long for
the row, such as a per-reviewer response page or venue notes. If the user wants
a fuller hub, propose it first.

Page rules:
- Start every page with a one-line summary, then the date and last editor.
- Link to the Linear issue and to the repo path or commit, never paste data.
- Update the existing page rather than creating a near-duplicate; search first.

## Workflow for a typical task

1. Find or create the Linear issue; set it In Progress.
2. Read the relevant Notion decision-log entries so past rulings are respected.
3. Do the work in the repo on the designated branch; run `recount.py`.
4. Commit with the issue ID. Do not open a PR unless asked.
5. Add a Decision-log entry in Notion if any scope, claim or number changed.
6. Comment on the Linear issue with the commit link and move it to In Review.

## Safety and etiquette

- Linear and Notion posts are visible to others. Confirm with the user before
  posting to shared spaces, sending messages, or deleting anything.
- Never paste credentials, tokens or private reviewer correspondence beyond
  what the user supplied for this project.
- If Linear or Notion access fails (not authorized), say so plainly and keep
  the content in a local markdown draft under the repo instead of dropping it.
- Report outcomes faithfully: if `recount.py` fails or a step was skipped,
  say that in the issue comment.
