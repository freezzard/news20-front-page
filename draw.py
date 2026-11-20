"""Drawing helpers, text fitting and the dot-matrix world map.

The map is built from per-row land segments on a 96 x 44 grid:
each land cell becomes one dot, which keeps the continents
recognisable at small sizes without any external geography file.
Segment columns are inclusive and follow the grid rule
column = (longitude + 180) / 3.75, row = (84 - latitude) / 3.36.
"""

from PIL import Image, ImageDraw, ImageFont

FONT_DIR = "/usr/share/fonts/truetype/noto/"
FONT_FILES = {
    "serif-black": "NotoSerifDisplay-Black.ttf",
    "serif-xbold": "NotoSerifDisplay-ExtraBold.ttf",
    "serif-bold": "NotoSerif-Bold.ttf",
    "serif": "NotoSerif-Regular.ttf",
    "serif-italic": "NotoSerif-Italic.ttf",
    "sans": "NotoSans-Regular.ttf",
    "sans-med": "NotoSans-Medium.ttf",
    "sans-bold": "NotoSans-Bold.ttf",
    "sans-xbold": "NotoSans-ExtraBold.ttf",
}
FONT_CACHE = {}


def load_font(kind, size):
    cache_key = kind + ":" + str(size)
    cached_font = FONT_CACHE.get(cache_key)
    loaded_font = cached_font
    if cached_font is None:
        loaded_font = ImageFont.truetype(FONT_DIR + FONT_FILES[kind], size)
        FONT_CACHE[cache_key] = loaded_font
    return loaded_font


def wrap_lines(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        trial_line = word
        if current_line != "":
            trial_line = current_line + " " + word
        trial_width = draw.textlength(trial_line, font=font)
        fits = trial_width <= max_width
        next_line = trial_line
        if fits is False:
            lines.append(current_line)
            next_line = word
        current_line = next_line
    if current_line != "":
        lines.append(current_line)
    return lines


def draw_wrapped(draw, xy, text, font, fill, max_width, line_gap, max_lines):
    lines = wrap_lines(draw, text, font, max_width)
    clipped_lines = lines
    if len(lines) > max_lines:
        clipped_lines = lines[:max_lines]
    pen_y = xy[1]
    for line_text in clipped_lines:
        draw.text((xy[0], pen_y), line_text, font=font, fill=fill)
        pen_y = pen_y + line_gap
    used_height = pen_y - xy[1]
    return used_height


def centered_text(draw, center_x, y, text, font, fill):
    text_width = draw.textlength(text, font=font)
    draw.text((center_x - text_width / 2, y), text, font=font, fill=fill)
    return text_width


def chip(draw, xy, label, fill, text_fill):
    chip_font = load_font("sans-xbold", 19)
    label_width = draw.textlength(label, font=chip_font)
    chip_box = (xy[0], xy[1], xy[0] + label_width + 18, xy[1] + 27)
    draw.rectangle(chip_box, fill=fill)
    draw.text((xy[0] + 9, xy[1] + 3), label, font=chip_font, fill=text_fill)
    return chip_box[2] - chip_box[0]


MAP_COLS = 96
MAP_ROWS = 44
MASK_SEGMENTS = [
    [(8, 14), (30, 38), (55, 57), (65, 70), (80, 85)],
    [(6, 16), (28, 40), (54, 58), (62, 72), (78, 90)],
    [(4, 18), (26, 36), (74, 80)],
    [(2, 24), (51, 54), (59, 95)],
    [(3, 26), (50, 95)],
    [(2, 28), (44, 44), (48, 95)],
    [(4, 20), (25, 30), (49, 95)],
    [(5, 20), (24, 29), (45, 46), (47, 95)],
    [(6, 30), (45, 95)],
    [(7, 30), (44, 92)],
    [(8, 29), (45, 88)],
    [(9, 29), (44, 88), (90, 92)],
    [(10, 28), (44, 88), (89, 91)],
    [(10, 28), (44, 46), (48, 49), (51, 58), (59, 86), (88, 90)],
    [(11, 27), (44, 89)],
    [(12, 25), (43, 75), (76, 86)],
    [(13, 23), (43, 75), (76, 85), (86, 86)],
    [(14, 21), (43, 74), (77, 82)],
    [(15, 19), (43, 73), (77, 81), (84, 84)],
    [(16, 18), (44, 72), (77, 80)],
    [(16, 18), (44, 61), (70, 73), (77, 79)],
    [(26, 33), (44, 60), (74, 93)],
    [(26, 35), (44, 59), (74, 93)],
    [(27, 36), (45, 58), (76, 92)],
    [(27, 37), (46, 57), (78, 90)],
    [(28, 37), (46, 57), (80, 88), (90, 94)],
    [(28, 38), (46, 57)],
    [(29, 38), (47, 56), (60, 61)],
    [(29, 38), (47, 56), (79, 89)],
    [(30, 38), (47, 55), (60, 60), (78, 90)],
    [(30, 37), (48, 55), (77, 90)],
    [(31, 37), (48, 54), (60, 60), (77, 89)],
    [(31, 36), (49, 54), (78, 88)],
    [(31, 36), (49, 53), (79, 87)],
    [(32, 35), (50, 52), (80, 86), (94, 94)],
    [(32, 35), (81, 85), (88, 88), (93, 94)],
    [(32, 34), (93, 93)],
    [(32, 34), (92, 93)],
    [(32, 33)],
    [(32, 33)],
    [(32, 32)],
    [(32, 32)],
    [],
    [],
]


def build_land_mask():
    mask_rows = []
    for segment_row in MASK_SEGMENTS:
        row_cells = [" "] * MAP_COLS
        for seg_start, seg_end in segment_row:
            seg_col = seg_start
            while seg_col <= seg_end:
                row_cells[seg_col] = "X"
                seg_col = seg_col + 1
        mask_rows.append("".join(row_cells))
    return mask_rows


LAND_MASK = build_land_mask()

MAP_LON_MIN = -180.0
MAP_LON_SPAN = 360.0
MAP_LAT_MAX = 84.0
MAP_LAT_SPAN = 148.0


def map_point(lon, lat, box):
    frac_x = (lon - MAP_LON_MIN) / MAP_LON_SPAN
    frac_y = (MAP_LAT_MAX - lat) / MAP_LAT_SPAN
    point_x = box[0] + frac_x * (box[2] - box[0])
    point_y = box[1] + frac_y * (box[3] - box[1])
    return (point_x, point_y)


def draw_world_map(canvas, box, land_fill, sea_fill):
    map_draw = ImageDraw.Draw(canvas)
    map_draw.rectangle(box, fill=sea_fill)
    cell_w = (box[2] - box[0]) / MAP_COLS
    cell_h = (box[3] - box[1]) / MAP_ROWS
    dot_r = min(cell_w, cell_h) * 0.52
    row_index = 0
    for mask_row in LAND_MASK:
        col_index = 0
        for mask_cell in mask_row:
            cell_is_land = mask_cell == "X"
            if cell_is_land:
                dot_cx = box[0] + (col_index + 0.5) * cell_w
                dot_cy = box[1] + (row_index + 0.5) * cell_h
                dot_box = (dot_cx - dot_r, dot_cy - dot_r, dot_cx + dot_r, dot_cy + dot_r)
                map_draw.ellipse(dot_box, fill=land_fill)
            col_index = col_index + 1
        row_index = row_index + 1
    return map_draw


def draw_map_pin(draw, xy, number, fill, ring_fill):
    pin_r = 16
    pin_box = (xy[0] - pin_r, xy[1] - pin_r, xy[0] + pin_r, xy[1] + pin_r)
    draw.ellipse(pin_box, fill=fill, outline=ring_fill, width=3)
    label = str(number)
    label_font = load_font("sans-xbold", 20)
    label_width = draw.textlength(label, font=label_font)
    draw.text((xy[0] - label_width / 2, xy[1] - 11), label, font=label_font, fill=ring_fill)
    return pin_r
