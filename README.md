# news20-front-page

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/freezzard/news20-front-page/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/freezzard/news20-front-page/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A classic newspaper front page for Friday 20 November 2026, drawn entirely in code. Forty verified stories from that one day: three illustrated hero cards (Cyclone Akvan's landfall in Odisha, the missile barrage on Kyiv's river bridges, COP31's fossil-fuel deadlock), ten more illustrated cards, a region tally bar, the day in numbers, a dot-matrix world map with the thirteen cards pinned, twenty-seven one-line briefs, and a date-check footer that names what was left out as other days' news. The Python program in this repo (render.py, scenes.py, draw.py, data.py) draws the page at 2048x2048 and exports the 1024x1024 entry.png; main.ts copies those bytes to the output directory.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=2k68scpr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
