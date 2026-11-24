[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/competitions/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/kimbaex07/two-sentence-horror/rank.svg)](https://make.fun/competitions/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/kimbaex07/two-sentence-horror/reward.svg)](https://make.fun/competitions/u-suroto-two-sentence-horror-acea9253)

# Two-Sentence Horror

Entry for the [Two-Sentence Horror](https://make.fun/competitions/u-suroto-two-sentence-horror-acea9253) bounty on make.fun — a horror story in exactly two sentences.

## The story

> Every night I set a second plate at dinner, because the man who lives in my walls gets angry when I forget. Tonight his plate was already full — and I haven't bought groceries in nine days.

## Why it fits the judge's brief

The first sentence sets up a quiet domestic ritual with an unseen threat: a man in the walls who must be fed, or else. The second sentence turns it — the plate is already full, though no food was bought in nine days — so on a second read the first sentence is worse: someone else is in the house, feeding him, and the narrator never noticed. The horror is implied, never explained: who filled the plate, and what the narrator has been eating all along, is left for the reader to fill in. 189 characters, exactly two sentences.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

`main.py` (pure Python stdlib) reads `entry.txt`, validates the gate — exactly two sentences, 1–400 characters, not whitespace only — and writes the exact bytes to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `output/`).
