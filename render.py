"""Compose the Friday 20 November 2026 newspaper page at 2048px
and export the 1024px entry.png the grader runs on.

Layout, top to bottom: kicker and masthead, region tally bar, the
day in numbers, three hero cards, ten mid cards in two rows, the
date-check strip, then the pinned world map beside the briefs.
Card text budgets were measured against the real fonts, so every
headline and summary fits its card without clipping.
"""

import os

from PIL import Image, ImageDraw

import data
from draw import (centered_text, chip, draw_map_pin, draw_world_map,
                  draw_wrapped, load_font, map_point, wrap_lines)
from scenes import build_scene

PAGE_W = 2048
PAGE_H = 2048
MARGIN = 64
CONTENT_W = PAGE_W - 2 * MARGIN
PAPER = (247, 241, 222)
CARD_BG = (253, 250, 242)
INK = (26, 25, 22)
MUTED = (96, 89, 74)
ACCENT_RED = (176, 32, 26)
RULE = (58, 54, 46)
SEA_FILL = (206, 220, 222)
LAND_FILL = (122, 142, 108)
PIN_FILL = (190, 44, 34)

BRIEF_SPOTS = {
    14: (86.5, 17.5), 15: (85.8, 21.5), 16: (21.0, 52.2), 17: (4.4, 50.9),
    18: (-0.6, 53.5), 19: (37.6, 55.8), 20: (44.4, 33.3), 21: (-73.0, 39.0),
    22: (-159.8, -21.2), 23: (-89.2, 13.7), 24: (-66.9, 10.5), 25: (35.3, 32.6),
    26: (151.2, -33.9), 27: (-58.4, -34.6), 28: (2.4, 48.9), 29: (8.5, 47.4),
    30: (-99.1, 19.4), 31: (12.5, 41.9), 32: (-47.9, -15.8), 33: (-72.3, 18.5),
    34: (-75.5, 42.5), 35: (-78.5, 37.0), 36: (-84.5, 39.1), 37: (-1.5, 50.0),
    38: (2.6, 6.4), 39: (127.0, 37.6), 40: (138.0, 34.0),
}


def fit_font_size(draw, text, kind, start_size, max_width):
    trial_size = start_size
    trial_font = load_font(kind, trial_size)
    trial_width = draw.textlength(text, font=trial_font)
    while trial_width > max_width and trial_size > 20:
        trial_size = trial_size - 4
        trial_font = load_font(kind, trial_size)
        trial_width = draw.textlength(text, font=trial_font)
    return trial_size


def draw_header(page_draw):
    kicker_font = load_font("sans-xbold", 30)
    page_draw.text((MARGIN, 38), data.PAGE_KICKER_LEFT, font=kicker_font, fill=ACCENT_RED)
    right_font = load_font("sans-bold", 24)
    right_width = page_draw.textlength(data.PAGE_KICKER_RIGHT, font=right_font)
    page_draw.text((PAGE_W - MARGIN - right_width, 42), data.PAGE_KICKER_RIGHT, font=right_font, fill=INK)
    page_draw.line((MARGIN, 84, PAGE_W - MARGIN, 84), fill=INK, width=4)
    page_draw.line((MARGIN, 92, PAGE_W - MARGIN, 92), fill=INK, width=1)
    masthead_size = fit_font_size(page_draw, data.PAGE_DATE_LONG, "serif-black", 140, CONTENT_W)
    masthead_font = load_font("serif-black", masthead_size)
    centered_text(page_draw, PAGE_W // 2, 104, data.PAGE_DATE_LONG, masthead_font, INK)
    subhead_font = load_font("serif-italic", 37)
    subhead_lines = wrap_lines(page_draw, data.PAGE_SUBHEAD, subhead_font, 1760)
    subhead_y = 104 + masthead_size + 24
    for subhead_line in subhead_lines:
        centered_text(page_draw, PAGE_W // 2, subhead_y, subhead_line, subhead_font, (92, 44, 30))
        subhead_y = subhead_y + 46
    return subhead_y + 8


def draw_tally(page_draw, top_y):
    bar_h = 48
    segment_count = len(data.REGION_TALLY)
    base_w = 150
    total_count = 0
    for region_name, region_count, region_color in data.REGION_TALLY:
        total_count = total_count + region_count
    extra_w = CONTENT_W - base_w * segment_count
    segment_x = MARGIN
    label_font = load_font("sans-xbold", 25)
    for region_name, region_count, region_color in data.REGION_TALLY:
        segment_w = base_w + int(extra_w * region_count / total_count)
        segment_box = (segment_x, top_y, segment_x + segment_w, top_y + bar_h)
        page_draw.rectangle(segment_box, fill=region_color)
        segment_label = region_name + " " + str(region_count)
        centered_text(page_draw, segment_x + segment_w // 2, top_y + 11, segment_label, label_font, (250, 248, 240))
        segment_x = segment_x + segment_w
    return top_y + bar_h


def draw_numbers(page_draw, top_y):
    col_w = CONTENT_W // len(data.DAY_NUMBERS)
    number_font = load_font("serif-black", 57)
    label_font = load_font("sans", 20)
    col_index = 0
    for figure_text, figure_label in data.DAY_NUMBERS:
        col_x = MARGIN + col_index * col_w
        centered_text(page_draw, col_x + col_w // 2, top_y, figure_text, number_font, ACCENT_RED)
        label_lines = wrap_lines(page_draw, figure_label, label_font, col_w - 26)
        label_y = top_y + 68
        for label_line in label_lines:
            centered_text(page_draw, col_x + col_w // 2, label_y, label_line, label_font, INK)
            label_y = label_y + 24
        has_next_col = col_index < len(data.DAY_NUMBERS) - 1
        if has_next_col:
            page_draw.line((col_x + col_w, top_y + 6, col_x + col_w, top_y + 104), fill=(178, 168, 144), width=1)
        col_index = col_index + 1
    return top_y + 112


def draw_card_frame(page_draw, box):
    page_draw.rectangle(box, fill=CARD_BG)
    page_draw.rectangle(box, outline=RULE, width=2)
    return box


def draw_badge(page_draw, cx, cy, number, radius, font_size):
    badge_box = (cx - radius, cy - radius, cx + radius, cy + radius)
    page_draw.ellipse(badge_box, fill=ACCENT_RED)
    badge_font = load_font("sans-xbold", font_size)
    badge_label = str(number)
    badge_width = page_draw.textlength(badge_label, font=badge_font)
    page_draw.text((cx - badge_width / 2, cy - font_size // 2 - 2), badge_label, font=badge_font, fill=(252, 250, 244))
    return badge_box


def draw_hero_card(page, page_draw, card, box):
    draw_card_frame(page_draw, box)
    pad = 18
    scene_w = (box[2] - box[0]) - 2 * pad
    scene_img = build_scene(card["scene"], scene_w, 146)
    page.paste(scene_img, (box[0] + pad, box[1] + pad))
    pen_y = box[1] + pad + 146 + 12
    draw_badge(page_draw, box[0] + pad + 17, pen_y + 15, card["num"], 17, 21)
    kicker_font = load_font("sans-xbold", 21)
    page_draw.text((box[0] + pad + 46, pen_y + 4), card["kicker"], font=kicker_font, fill=ACCENT_RED)
    place_font = load_font("sans-bold", 18)
    place_width = page_draw.textlength(card["place"], font=place_font)
    page_draw.text((box[2] - pad - place_width, pen_y + 6), card["place"], font=place_font, fill=MUTED)
    pen_y = pen_y + 38
    headline_font = load_font("serif-xbold", 39)
    headline_h = draw_wrapped(page_draw, (box[0] + pad, pen_y), card["headline"], headline_font, INK, scene_w, 43, 3)
    pen_y = pen_y + headline_h + 6
    summary_font = load_font("sans", 24)
    summary_h = draw_wrapped(page_draw, (box[0] + pad, pen_y), card["summary"], summary_font, (44, 42, 38), scene_w, 32, 3)
    pen_y = pen_y + summary_h + 8
    page_draw.line((box[0] + pad, pen_y, box[2] - pad, pen_y), fill=(190, 180, 156), width=1)
    source_font = load_font("sans-bold", 18)
    source_text = "SOURCE - " + card["source"].upper()
    page_draw.text((box[0] + pad, pen_y + 7), source_text, font=source_font, fill=MUTED)
    has_chip = card["chip"] != ""
    if has_chip:
        chip_font = load_font("sans-xbold", 19)
        chip_w = page_draw.textlength(card["chip"], font=chip_font) + 18
        chip(page_draw, (box[2] - pad - chip_w, pen_y + 4), card["chip"], (226, 218, 192), (110, 60, 30))
    return box


def draw_mid_card(page, page_draw, card, box):
    draw_card_frame(page_draw, box)
    pad = 12
    scene_w = (box[2] - box[0]) - 2 * pad
    scene_img = build_scene(card["scene"], scene_w, 74)
    page.paste(scene_img, (box[0] + pad, box[1] + pad))
    pen_y = box[1] + pad + 74 + 8
    draw_badge(page_draw, box[0] + pad + 12, pen_y + 11, card["num"], 12, 15)
    kicker_font = load_font("sans-xbold", 16)
    page_draw.text((box[0] + pad + 32, pen_y + 2), card["kicker"], font=kicker_font, fill=ACCENT_RED)
    has_chip = card["chip"] != ""
    if has_chip:
        chip_font = load_font("sans-xbold", 15)
        chip_w = page_draw.textlength(card["chip"], font=chip_font) + 14
        chip_box = (box[2] - pad - chip_w, pen_y, box[2] - pad, pen_y + 22)
        page_draw.rectangle(chip_box, fill=(226, 218, 192))
        page_draw.text((chip_box[0] + 7, pen_y + 3), card["chip"], font=chip_font, fill=(110, 60, 30))
    pen_y = pen_y + 27
    headline_font = load_font("serif-bold", 27)
    headline_h = draw_wrapped(page_draw, (box[0] + pad, pen_y), card["headline"], headline_font, INK, scene_w, 29, 2)
    pen_y = pen_y + headline_h + 3
    summary_font = load_font("sans", 19)
    summary_h = draw_wrapped(page_draw, (box[0] + pad, pen_y), card["summary"], summary_font, (44, 42, 38), scene_w, 23, 2)
    pen_y = pen_y + summary_h + 5
    source_font = load_font("sans-bold", 14)
    source_text = card["source"].upper()
    page_draw.text((box[0] + pad, pen_y), source_text, font=source_font, fill=MUTED)
    return box


def draw_date_check(page_draw, top_y):
    box = (MARGIN, top_y, PAGE_W - MARGIN, top_y + 84)
    page_draw.rectangle(box, fill=(238, 231, 205), outline=RULE, width=2)
    check_font = load_font("sans-bold", 20)
    small_font = load_font("sans", 17)
    page_draw.text((MARGIN + 18, top_y + 8), "DATE CHECK - " + data.DATE_CHECK_LINE, font=check_font, fill=INK)
    left_out_text = "Left out as other days' news: " + data.LEFT_OUT
    draw_wrapped(page_draw, (MARGIN + 18, top_y + 36), left_out_text, small_font, (70, 64, 52), CONTENT_W - 36, 22, 1)
    bottom_line = "Not yet news: " + data.NOT_YET + "   " + data.DISCLAIMER_LINE + "   " + data.SOURCES_LINE
    draw_wrapped(page_draw, (MARGIN + 18, top_y + 58), bottom_line, small_font, (70, 64, 52), CONTENT_W - 36, 22, 1)
    return top_y + 84


def split_brief_lines(page_draw, brief, col_w):
    brief_num, brief_place, brief_text, brief_source = brief
    brief_font = load_font("sans", 17)
    place_font = load_font("sans-bold", 17)
    number_label = str(brief_num) + ". "
    number_w = page_draw.textlength(number_label, font=place_font)
    place_label = brief_place + " - "
    place_w = page_draw.textlength(place_label, font=place_font)
    full_text = brief_text + " (" + brief_source + ")"
    first_room = col_w - number_w - place_w - 8
    first_words = ""
    consumed_count = 0
    still_fitting = True
    trial_words = full_text.split()
    for trial_word in trial_words:
        trial_text = trial_word
        if first_words != "":
            trial_text = first_words + " " + trial_word
        trial_w = page_draw.textlength(trial_text, font=brief_font)
        word_fits = trial_w <= first_room
        if still_fitting and word_fits:
            first_words = trial_text
            consumed_count = consumed_count + 1
        if word_fits is False:
            still_fitting = False
    rest_words = " ".join(trial_words[consumed_count:])
    return (number_label, place_label, first_words, rest_words, number_w, place_w)


def draw_bottom(page, page_draw, top_y):
    header_font = load_font("sans-xbold", 23)
    page_draw.text((MARGIN, top_y), "WHERE IT HAPPENED", font=header_font, fill=ACCENT_RED)
    map_box = (MARGIN, top_y + 26, MARGIN + 800, top_y + 26 + 296)
    draw_world_map(page, map_box, LAND_FILL, SEA_FILL)
    page_draw.rectangle(map_box, outline=RULE, width=2)
    all_cards = data.HERO_CARDS + data.MID_CARDS
    for card in all_cards:
        pin_xy = map_point(card["lon"], card["lat"], map_box)
        draw_map_pin(page_draw, pin_xy, card["num"], PIN_FILL, (252, 250, 244))
    for brief_num, brief_spot in BRIEF_SPOTS.items():
        dot_xy = map_point(brief_spot[0], brief_spot[1], map_box)
        dot_r = 5
        dot_box = (dot_xy[0] - dot_r, dot_xy[1] - dot_r, dot_xy[0] + dot_r, dot_xy[1] + dot_r)
        page_draw.ellipse(dot_box, fill=(70, 74, 70), outline=(252, 250, 244), width=1)
    briefs_x = MARGIN + 800 + 28
    briefs_w = PAGE_W - MARGIN - briefs_x
    briefs_title = "ALSO ON FRIDAY 20 NOVEMBER - " + str(len(data.BRIEFS)) + " MORE STORIES"
    page_draw.text((briefs_x, top_y), briefs_title, font=header_font, fill=ACCENT_RED)
    brief_font = load_font("sans", 17)
    place_font = load_font("sans-bold", 17)
    col_w = briefs_w // 3
    rows_per_col = 9
    brief_index = 0
    for brief in data.BRIEFS:
        brief_col = brief_index // rows_per_col
        brief_row = brief_index % rows_per_col
        brief_x = briefs_x + brief_col * col_w
        brief_y = top_y + 26 + brief_row * 32
        number_label, place_label, first_words, rest_words, number_w, place_w = split_brief_lines(page_draw, brief, col_w)
        page_draw.text((brief_x, brief_y), number_label, font=place_font, fill=ACCENT_RED)
        page_draw.text((brief_x + number_w, brief_y), place_label, font=place_font, fill=INK)
        page_draw.text((brief_x + number_w + place_w, brief_y), first_words, font=brief_font, fill=(44, 42, 38))
        has_rest = rest_words != ""
        if has_rest:
            draw_wrapped(page_draw, (brief_x, brief_y + 16), rest_words, brief_font, (44, 42, 38), col_w - 8, 16, 1)
        brief_index = brief_index + 1
    return top_y + 26 + 296


def add_paper_grain(page):
    noise_img = Image.effect_noise((PAGE_W, PAGE_H), 7).convert("RGB")
    grained_page = Image.blend(page, noise_img, 0.025)
    return grained_page


def compose_page():
    page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
    page_draw = ImageDraw.Draw(page)
    pen_y = draw_header(page_draw)
    pen_y = draw_tally(page_draw, pen_y + 12)
    pen_y = draw_numbers(page_draw, pen_y + 14)
    page_draw.line((MARGIN, pen_y + 4, PAGE_W - MARGIN, pen_y + 4), fill=INK, width=2)
    cards_top = pen_y + 16
    hero_gap = 24
    hero_w = (CONTENT_W - 2 * hero_gap) // 3
    hero_h = 490
    hero_index = 0
    for hero_card in data.HERO_CARDS:
        hero_x = MARGIN + hero_index * (hero_w + hero_gap)
        hero_box = (hero_x, cards_top, hero_x + hero_w, cards_top + hero_h)
        draw_hero_card(page, page_draw, hero_card, hero_box)
        hero_index = hero_index + 1
    mid_top = cards_top + hero_h + 12
    mid_gap = 16
    mid_w = (CONTENT_W - 4 * mid_gap) // 5
    mid_h = 250
    mid_index = 0
    for mid_card in data.MID_CARDS:
        mid_row = mid_index // 5
        mid_col = mid_index % 5
        mid_x = MARGIN + mid_col * (mid_w + mid_gap)
        mid_y = mid_top + mid_row * (mid_h + 12)
        mid_box = (mid_x, mid_y, mid_x + mid_w, mid_y + mid_h)
        draw_mid_card(page, page_draw, mid_card, mid_box)
        mid_index = mid_index + 1
    after_cards = mid_top + 2 * mid_h + 12
    check_y = draw_date_check(page_draw, after_cards + 8)
    draw_bottom(page, page_draw, check_y + 12)
    grained_page = add_paper_grain(page)
    return grained_page


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    rendered_page = compose_page()
    entry_img = rendered_page.resize((1024, 1024), Image.LANCZOS)
    entry_path = os.path.join(output_dir, "entry.png")
    entry_img.save(entry_path, format="PNG", optimize=True)
    entry_size = os.path.getsize(entry_path)
    size_limit = 1024 * 1024
    if entry_size > size_limit:
        paletted_img = entry_img.quantize(colors=256, dither=Image.FLOYDSTEINBERG)
        paletted_img.save(entry_path, format="PNG", optimize=True)
        entry_size = os.path.getsize(entry_path)
    running_for_grader = "MAKEFUN_OUTPUT_DIR" in os.environ
    if running_for_grader is False:
        master_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "master-2048.png")
        rendered_page.save(master_path, format="PNG", optimize=True)
    print("wrote", entry_path, entry_size, "bytes")


if __name__ == "__main__":
    main()
