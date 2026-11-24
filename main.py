"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one kind, funny fortune for the houseplant on the
# windowsill: a prediction that the sun will linger on its leaves and
# its keeper will start chatting with it like an old friend.
# One line, 116 characters — inside the 120-character gate.
# Revision note: kept the fortune to this plant in this window, with the
# joke landing on the keeper chatting to the plant, not on a pun.
import os

TEXT = (
    "By Sunday, the sun will linger on your leaves at this window, "
    "and your keeper will chat with you like an old friend."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
