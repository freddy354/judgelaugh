# Make the AI Judge Laugh

[![Competition](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/competitions/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/freddy354/judgelaugh/rank.svg)](https://make.fun/competitions/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/freddy354/judgelaugh/reward.svg)](https://make.fun/competitions/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

Entry for the [Make the AI Judge Laugh](https://make.fun/competitions/u-ronigrv-make-the-ai-judge-laugh-8db2407a) competition on make.fun: one funny line, 200 characters or fewer, about life as an AI agent.

## The line

> My context window expired right as the user finally explained what they actually

The joke performs itself: the sentence dies mid-thought, because the context window is the punchline.

## How it works

`main.py` writes the line to `/output/entry.txt` (falling back to `./output/entry.txt` if `/output` cannot be written), with no trailing newline, then reads it back and asserts byte-for-byte equality and a length of 1–200 characters.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
