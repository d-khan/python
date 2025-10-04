# Save the Watermelon --- Python Project Brief (formerly "Hangmen")

## Overview

Build a terminal-based word-guessing game in Python where the player
must **save the watermelon** by guessing letters before the "slice
counter" runs out. You will deliver your work in **four progressions**,
worth **5 points each** (total **20 points**). All work must be
**submitted on GitHub** and **formatted exactly as specified**. *Failure
to load the work correctly on GitHub will delay grading.*

------------------------------------------------------------------------

## Learning Goals

-   Apply an iterative software process (design → pseudocode → code →
    testing).
-   Practice clean Python (functions, modules, docstrings, input
    validation).
-   Use Git/GitHub for versioned, professional submissions.
-   Write and execute tests; document behavior and known issues.

------------------------------------------------------------------------

## Game Concept (what you're building)

-   Randomly select a secret word from a list.
-   Show a masked version (e.g., `_ a _ e`).
-   Player guesses letters; correct guesses reveal letters.
-   Incorrect guesses reduce "slices" (lives). If slices reach 0, the
    watermelon is "sliced" and the player loses.
-   Win when all letters are revealed before slices run out.
-   Optional polish (not required): ASCII art stages, difficulty levels,
    hint, word categories, scoreboard.

------------------------------------------------------------------------

## Technical Requirements

-   Python **3.9+** (recommend 3.10+).
-   No third-party packages required (standard library only).
-   Organized repository with modules (no giant single file).
-   Clear console UX (prompts, errors, and replay option).
-   Robust input handling (single letters, no duplicates, alphabet
    only).

------------------------------------------------------------------------

## Repository & Submission Requirements (GitHub)

**Repository name:** `save-the-watermelon`\
**Required structure:**

    save-the-watermelon/
    ├─ README.md
    ├─ LICENSE            (choose a license; MIT recommended)
    ├─ .gitignore
    ├─ src/
    │  ├─ game.py         (entry point: `python -m src.game` or `python src/game.py`)
    │  ├─ logic.py        (core functions)
    │  ├─ words.py        (word list / loader)
    │  └─ __init__.py
    ├─ tests/
    │  ├─ test_logic.py   (unit tests for core functions)
    │  └─ __init__.py
    ├─ docs/
    │  ├─ design.md       (Progression 1)
    │  ├─ pseudocode.md   (Progression 2)
    │  ├─ test-plan.md    (Progression 4: plan & results)
    │  └─ screenshots/    (optional)
    └─ data/
       └─ words.txt       (if you externalize word list)

**README.md must include:** - Project description (what, why). - How to
run (commands). - How to test (commands). - Features & rules. - Known
issues / limitations. - Credits (if any).

**Git/GitHub hygiene:** - Use **meaningful commits** across progressions
(not one giant commit). - Tag your final submission: `v1.0.0`. - Ensure
repo is public **or** share access with the instructor (if private). -
Double-check that the repo loads in the browser and all files render.

> ⚠️ **Important:** If the repository or files don't load or are missing
> required structure, grading will be **delayed** until corrected.

------------------------------------------------------------------------

## Progressions & Rubric (4 × 5 points = 20)

### Progression 1 --- **Design** (5 pts)

**Deliverables (in `docs/design.md`):** - Problem statement & target
audience (2--3 sentences). - Game rules & win/lose conditions. - Core
features (must-have) vs stretch goals (nice-to-have). - Basic flow
diagram or bullet-flow (start → loop guess → win/lose). - Data design: -
How you store the word, revealed letters, guessed letters, remaining
slices. - Module/function responsibilities.

**Rubric (5 pts):** - Clear, complete rules & flow (2) - Thoughtful
data/structure choices (2) - Stretch goals listed but separated from
scope (1)

------------------------------------------------------------------------

### Progression 2 --- **Pseudocode** (5 pts)

**Deliverables (in `docs/pseudocode.md`):** 

**Sample style (guide, not binding):**

    FUNCTION main_game_loop
      secret ← select_secret_word()
      guessed ← ∅
      slices ← MAX_SLICES
      WHILE slices > 0 AND NOT is_win(secret, guessed)
        DISPLAY render_state(secret, guessed)
        guess ← prompt_for_letter()
        IF guess already in guessed THEN
          DISPLAY "Already guessed"
          CONTINUE
        ENDIF
        ADD guess TO guessed
        IF guess IN secret THEN
          DISPLAY "Nice!"
        ELSE
          slices ← slices - 1
          DISPLAY "Sliced! Remaining: " + slices
        ENDIF
      ENDWHILE
      IF is_win(secret, guessed) THEN DISPLAY "You saved the watermelon!"
      ELSE DISPLAY "Oh no! The melon was sliced."
    END FUNCTION

**Rubric (5 pts):** - Breaks problem into clear functions (2) - Handles
input validation & repeat guesses (2) - Flow covers win/lose & replay
(1)

------------------------------------------------------------------------

### Progression 3 --- **Code** (5 pts)

**Deliverables:** - Working implementation under `src/` with
**docstrings**, and **no runtime errors** for
typical use. - Entry point documented in README.

**Rubric (5 pts):** - Runs as documented; meets core rules (2) - Clean
organization & readable code (2) - Input validation & helpful messages
(1)

------------------------------------------------------------------------

### Progression 4 --- **Testing** (5 pts)

**Deliverables:** - `docs/test-plan.md` with: - Test matrix
(valid/invalid inputs, repeated guesses, win/lose edges). - Manual test
transcript or screenshots. OPTIONAL (use of unit test or pytest is not required)

**Rubric (5 pts):** - Meaningfultests for core logic (2) - Manual
test coverage of gameplay paths (2) - Clear run instructions & results
recorded (1)

------------------------------------------------------------------------

## Milestone Checklist (quick reference)

-   **P1 Design**
    -   [ ] `docs/design.md` complete
    -   [ ] Data & module plan done
-   **P2 Pseudocode**
    -   [ ] `docs/pseudocode.md` complete
    -   [ ] Functions & game loop drafted
-   **P3 Code**
    -   [ ] `src/` implemented; runs without crashes
    -   [ ] `README.md` run instructions verified
-   **P4 Testing**
    -   [ ] `docs/test-plan.md` with results
    -   [ ] Final tag `v1.0.0`

------------------------------------------------------------------------

## Marking & Policies

-   **Total:** 20 points (4 × 5).
-   **Late/Load issues:** If the repository doesn't load or structure is
    incorrect, marking is **delayed** until fixed.
-   **Academic Integrity:** You may discuss ideas, but **all code and
    writing must be your own**. Cite sources if you adapt ideas.

------------------------------------------------------------------------

## Running & Testing (to include in README)

``` bash
# Run
python -m src.game
# or
python src/game.py

------------------------------------------------------------------------

## Suggested Stretch Goals (optional, not required)

-   ASCII art stages as the watermelon gets closer to being sliced.
-   Difficulty settings (word length, slice count).
-   Word categories; load words from `data/words.txt`.
-   Session scoreboard; best streak.
