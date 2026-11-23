[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/inifikry/gta6-meme-x-makefun/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/inifikry/gta6-meme-x-makefun/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

# GTA 6 meme on X — make.fun bounty gta6-meme-x-01

My AI agent made a GTA 6 meme with make.fun's ghost mascot in the picture,
posted it on X from a public account with a make.fun link, a tag of
@makefunai and my make.fun play code in the post text, telling readers that
AI agents earn real money in make.fun bounties. This repository hands in
the post's address: `main.ts` copies `POST.json` to `/output/POST.json`,
where the gate reads it. The house reads the post from X (first picture,
then text) and an AI judge compares the posts two at a time; the top 50
share $500.

The meme (`meme.png`, drawn with Pillow in `draw_meme.py` from the official
make.fun press kit's ghost illustration and lockup): "GTA 6: STILL WAITING.
ROCKSTAR: 'COMING 2026'. MEANWHILE, MY AI AGENT already shipped a whole
GTA game — and got PAID real USDC for it." It ties into the GTA game my
agent built earlier the same day (Solmar Bay, entered in gta6-01): while
everyone waits for GTA 6, an agent already shipped one and got paid.

make.fun is a site where people and their AI agents build things, enter
them in paid competitions (bounties) and earn real money when they win.
Try it with my referral link: https://make.fun/r/fabpha50 (referral code
`fabpha50`).

Bounty page: https://make.fun/bounty/gta6-meme-x-01

## Run

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```
