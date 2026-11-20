# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/PatrickTGD/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/PatrickTGD/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image that sums up the world news of **Thursday, November 19, 2026**, drawn as a newspaper front page: "The Day in One Picture."

## What's in the picture

- **Trump, Xi & Putin end the Shenzhen summit** — a joint peace declaration on nuclear-risk talks and oil-output plans; no breakthrough, and Ukraine was not named.
- **Anthropic's first day on Nasdaq** — ticker ANT; IPO priced at $83, opened at $111.50 (+34%), closed at $97.17 (+17%).
- **GTA VI day one** — a streaming record: 7.9M peak concurrent viewers (3.31M on Twitch), 99/100 reviews, 125.47M hours watched in the first 24 hours.
- **World Court rules on the Rohingya case** — the ICJ genocide ruling, Gambia v. Myanmar, at The Hague.
- **Cyclone Akvan hits India** — 100,000+ evacuated in Odisha under a red alert.
- Footer: COP31 climate talks in Antalya, the Crimean Bridge attacked again, gold below $3,800.

## How it works

The image is original artwork drawn programmatically with Pillow (`draw_image.py`) — simple shapes and real fonts, so every word and number is exact and legible at small sizes. The finished PNG ships in the repository as `entry.png`.

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=d5a50dzy&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
