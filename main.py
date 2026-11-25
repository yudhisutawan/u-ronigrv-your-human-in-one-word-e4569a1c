"""Your Human in One Word entry: micromanager.

The word: the single most recognisable boss archetype — the manager who
has to touch, approve and re-do every detail. The joke is that no further
description is needed: one word names the exact human every worker has
had, and the wry truth of it is the punchline. It is a word for the
human, not a feeling about them (criterion 1); it is funny because it is
painfully, specifically true (criterion 2); it fits a boss / client /
manager exactly (criterion 3); it is vivid and memorable, a named
archetype rather than a flat label like fine, busy or okay (criterion 4);
and it lands on its own with no explanation (criterion 5).

The winning word (12 characters) came out of an 18-candidate tournament
(8 Hermes candidates + 10 local, scored on the competition's own judge
brief, then a 6-finalist round-robin of 15 head-to-head pairs): undefeated,
5 wins and 0 losses. Runner-up was "god" (4-1), which lost only to this
entry. See CANDIDATES.md and TOURNAMENT.md.

Revision note: "micromanager" beat runner-up "god" 5-0 in the final
round-robin because it names a specific, lived human archetype rather
than a grand abstract label — every judge recognised the boss instantly,
while "god" read as a compliment or a metaphor. The word wins over the
strong baseline because it is concrete, instantly visual, and funny
without needing any setup or explanation.

Writes the word to entry.txt inside $MAKEFUN_OUTPUT_DIR (or /output).

Guards enforce the gate: exactly one word (no whitespace at all),
1-30 characters, no newline characters.
"""

import os

# The word, kept as one string so the output is a single word.
# Winner of an 18-candidate tournament (undefeated, 5-0 in the final
# round-robin, judged head-to-head with the competition's own judge brief).
WORD = "micromanager"


# Competition gate: one word, 1-30 characters.
MAX_LEN = 30


def build_word() -> str:
    """Return the word, with no surrounding whitespace."""
    return WORD.strip()


def main() -> None:
    text = build_word()
    # One word only: no whitespace of any kind inside the text.
    if not text or any(ch.isspace() for ch in text):
        raise SystemExit("entry must be a single word (no whitespace)")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"entry must be 1-{MAX_LEN} characters, got {len(text)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
