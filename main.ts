// Entry point for the news-image-20261120 submission.
//
// The deliverable image is entry.png beside this file: a one-page
// newspaper of Friday 20 November 2026, drawn entirely in code by
// the Python program in this repository (render.py, scenes.py,
// draw.py, data.py). This program's only job is to place those
// exact bytes where the grader expects them: /output/entry.png,
// or MAKEFUN_OUTPUT_DIR/entry.png when that variable is set
// outside the grader's container. Standard library only, no
// network, same bytes on every run.

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const sourceImageUrl = new URL('./entry.png', import.meta.url);
const targetImagePath = join(outputDir, 'entry.png');

copyFileSync(sourceImageUrl, targetImagePath);
