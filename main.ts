// Entry for make.fun bounty gta6-meme-x-01 ("Post a GTA 6 meme on X").
// Node 22, standard library only. It copies POST.json from the repository
// root to /output/POST.json, where the gate reads the posted X post's URL.
// That is all it has to do: the entry is the post itself. The house reads
// the post from X (its first picture and its text) and hands that to the
// judge. Nothing this program writes about the post is judged.
//
// POST.json ships with a placeholder address; replace it with the real
// post URL (https://x.com/<handle>/status/<id>) before submitting.
//
// Outside the grader, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand in
// for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });
const src = join(BOT_DIR, 'POST.json');
try {
  const parsed = JSON.parse(readFileSync(src, 'utf8'));
  if (typeof parsed !== 'object' || parsed === null || typeof parsed.url !== 'string') {
    throw new Error('POST.json must be a JSON object with a string "url"');
  }
  copyFileSync(src, join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
