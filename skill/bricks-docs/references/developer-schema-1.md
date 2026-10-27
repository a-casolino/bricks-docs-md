# Bricks Data Model

Source: https://academy.bricksbuilder.io/developer/schema/

*How Bricks stores and structures data: elements, content areas, page/template settings, and global data structures.*

This page explains how Bricks structures its data. Use it alongside the individual element and control schemas to understand or generate valid Bricks content. Each JSON file describes the exact shape of data Bricks reads and writes, so AI coding assistants, build tools, import/export scripts, and custom integrations can generate, validate, or transform Bricks content without the builder UI.

**Schema version:** 2.4.3

## Element structure

Every element in Bricks shares the same envelope, regardless of its type:

```json
{
  "id": "dlceeu",
  "name": "button",
  "parent": 0,
  "children": [],
  "settings": { "text": "I am a button", "style": "primary" },
  "label": "My Button"
}
```

The element envelope has 8 fields (`id`, `name`, `parent`, `children`, `settings`, `selectors`, `label`, `themeStyles`). The `settings` object combines three layers: element-specific controls, inherited CSS controls (the `_`-prefixed keys), and meta-settings (`_cssGlobalClasses`, `_conditions`, `_interactions`, `_attributes`, etc.).

See the [Element schema](./elements/common/element/) for the full envelope reference, settings layers, meta-settings, and selectors documentation.

## Content areas

A Bricks page (or any post type using Bricks) stores its elements across three independent content areas: header, content, and footer. Each content area is a flat array of elements with parent-child references (not a nested tree). An array may contain both regular elements and component instances (identifiable by the presence of a `cid` field).

| Content area | WordPress post meta key | Description |
|---|---|---|
| Header | `_bricks_page_header_2` | Header template elements |
| Content | `_bricks_page_content_2` | Main page/post content |
| Footer | `_bricks_page_footer_2` | Footer template elements |

All three content areas use the exact same data structure: an array of elements as described in the [Element schema](./elements/common/element/).

**Storage:** These are stored as serialized arrays in the `wp_postmeta` table.

| Data | Meta key | PHP constant |
|---|---|---|
| Header elements | `_bricks_page_header_2` | `BRICKS_DB_PAGE_HEADER` |
| Content elements | `_bricks_page_content_2` | `BRICKS_DB_PAGE_CONTENT` |
| Footer elements | `_bricks_page_footer_2` | `BRICKS_DB_PAGE_FOOTER` |

See the [Content Area schema](./general/content-area/) for the array structure and storage details.

### Responsive and state variants

CSS-related settings support breakpoint and pseudo-class suffixes using colon syntax. A setting key with no suffix applies at the base breakpoint (desktop by default):

```
_typography                          → base breakpoint (no suffix)
_typography:tablet_portrait          → tablet portrait breakpoint
_typography:mobile_landscape:hover   → mobile landscape + hover state
```

## Page settings

Per-page configuration controlling header/footer visibility, scroll behavior, SEO metadata, social sharing, and custom code injection. These settings apply to the specific post being edited and are separate from element settings and global data.

```json
{
  "headerDisabled": true,
  "scrollSnapType": "y proximity"
}
```

See the [page settings schema](./settings/page/) for all available controls.

**Storage:** Stored as a serialized array in the `wp_postmeta` table.

| Data | Meta key | PHP constant |
|---|---|---|
| Page settings | `_bricks_page_settings` | `BRICKS_DB_PAGE_SETTINGS` |

## Template settings

Settings specific to Bricks templates (stored as the `bricks_template` custom post type). Includes template conditions that determine where on the site a template is applied (e.g., entire website, specific post types, archives, or individual pages). Header templates also store layout settings such as sticky behavior here.

```json
{
  "templateConditions": [
    { "id": "iwjjdg", "main": "any" }
  ]
}
```

See the [template settings schema](./settings/template/) for all available controls.

**Storage:** Stored as serialized arrays in the `wp_postmeta` table.

| Data | Meta key | PHP constant |
|---|---|---|
| Template settings | `_bricks_template_settings` | `BRICKS_DB_TEMPLATE_SETTINGS` |
| Template type | `_bricks_template_type` | `BRICKS_DB_TEMPLATE_TYPE` |

## Global data structures

Bricks stores several global data structures as WordPress options. These are site-wide and shared across all pages and templates.

**Storage:** All global data is stored as serialized arrays in the `wp_options` table.

| Data | Option name | PHP constant |
|---|---|---|
| Global classes | `bricks_global_classes` | `BRICKS_DB_GLOBAL_CLASSES` |
| Global variables | `bricks_global_variables` | `BRICKS_DB_GLOBAL_VARIABLES` |
| Theme styles | `bricks_theme_styles` | `BRICKS_DB_THEME_STYLES` |
| Color palettes | `bricks_color_palette` | `BRICKS_DB_COLOR_PALETTE` |
| Breakpoints | `bricks_breakpoints` | `BRICKS_DB_BREAKPOINTS` |
| Components | `bricks_components` | `BRICKS_DB_COMPONENTS` |
| Pseudo-classes | `bricks_pseudo_classes` | `BRICKS_DB_PSEUDO_CLASSES` |

### Global classes

Reusable CSS class definitions that can be applied to any element via the `_cssGlobalClasses` setting. Edit a class once and every element using it updates everywhere. The `settings` object on a class follows the same structure as element settings, including support for breakpoint and pseudo-class variants using the colon syntax (e.g., `_typography:tablet_portrait`).

```json
[
  {
    "id": "xkatss",
    "name": "hero-section",
    "settings": {
      "_background": {
        "color": {
          "light": "#81D4FA",
          "raw": "var(--bricks-color-sky-blue)",
          "id": "573827"
        }
      },
      "_padding:mobile_portrait": {
        "top": "40",
        "bottom": "40"
      }
    },
    "modified": 1772645626,
    "user_id": 2
  }
]
```

See the [global classes schema](./global/global-classes/).

### Global variables

CSS custom properties that become available site-wide as `var(--variable-name)`. Used to define design tokens (colors, spacing, font sizes, etc.) that can be referenced from any element setting that accepts a CSS value.

```json
[
  { "id": "jeeawn", "name": "primary-color", "value": "green" },
  { "id": "ab3kxz", "name": "spacing-xl", "value": "80px" }
]
```

See the [global variables schema](./global/global-variables/).

### Theme styles

Site-wide default styling applied per element type (e.g., default section padding, heading typography, button colors). Each theme style requires conditions to determine which pages it applies to. Multiple theme styles can coexist with different conditions; a loading method setting controls whether only the most specific or all matching theme styles are applied on a given page.

```json
{
  "my-theme-style": {
    "label": "My Theme Style",
    "settings": {
      "conditions": {
        "conditions": [
          { "id": "vrniaa", "main": "any" }
        ]
      },
      "section": {
        "padding": { "top": "80", "right": "16", "left": "16", "bottom": "80" },
        "_rowGap": "32"
      },
      "heading": {
        "_typography": { "font-family": "Inter", "font-weight": "700" }
      }
    }
  }
}
```

See the [theme styles schema](./global/theme-styles/).

### Color palettes

Named color collections used across the builder. Multiple palettes can coexist. Each color stores a CSS variable reference (`raw`), the resolved light-mode value (`light`), and an optional dark-mode value (`dark`). The `raw` value is what gets written into settings; `light`/`dark` are the resolved display values.

```json
[
  {
    "id": "58e6a6",
    "name": "Brand Colors",
    "colors": [
      { "id": "920e35", "raw": "var(--bricks-color-red)", "light": "#f44336" },
      { "id": "58c724", "raw": "var(--bricks-color-blue)", "light": "#2196f3" },
      { "id": "3f6995", "raw": "var(--bricks-color-green)", "light": "#4caf50" }
    ]
  }
]
```

See the [color palettes schema](./global/color-palettes/).

### Breakpoints

Responsive breakpoint definitions. The entry marked `"base": true` is the default breakpoint; settings with no breakpoint suffix apply at this breakpoint (e.g., `_typography`). All other breakpoints generate a media query at their `width` value and are referenced via colon suffix on the setting key (e.g., `_typography:tablet_portrait`). Users can add custom breakpoints and modify widths.

```json
[
  { "base": true, "key": "desktop", "label": "Desktop", "width": 1279, "icon": "laptop" },
  { "key": "tablet_portrait", "label": "Tablet portrait", "width": 991, "icon": "tablet-portrait" },
  { "key": "mobile_landscape", "label": "Mobile landscape", "width": 767, "icon": "phone-landscape" },
  { "key": "mobile_portrait", "label": "Mobile portrait", "width": 478, "icon": "phone-portrait" }
]
```

See the [breakpoints schema](./global/breakpoints/).

### Components

Reusable element bundles, analogous to components in Vue or React. A component definition holds a tree of elements (`elements`) and an optional list of `properties` that expose specific controls for per-instance customization (e.g., a different heading text or image on each instance). When added to a page, a component instance is created that references the main component via `cid`.

```json
[
  {
    "id": "fdqkmn",
    "category": "Marketing",
    "desc": "A reusable CTA button with configurable label",
    "elements": [
      {
        "id": "fdqkmn",
        "name": "button",
        "parent": 0,
        "children": [],
        "settings": { "text": "Get started", "style": "dark" },
        "label": "CTA Button"
      }
    ],
    "properties": [
      {
        "id": "pbutxt",
        "label": "Button text",
        "type": "text",
        "connections": { "fdqkmn": ["text"] }
      }
    ],
    "_created": 1772645617,
    "_user_id": 2,
    "_version": "2.2-rc2"
  }
]
```

See the [components schema](./global/components/).

### Pseudo-classes

CSS pseudo-classes available in the builder for state variants (e.g., hover, active, focus). These determine which pseudo-class suffixes can be applied to CSS settings using the colon syntax (e.g., `_typography:mobile_portrait:hover`). The defaults are `:hover`, `:active`, and `:focus`, but users can add custom pseudo-classes via Bricks settings.

```json
[":hover", ":active", ":focus"]
```

See the [pseudo-classes schema](./global/pseudo-classes/).

## Nesting example

Below is a real-world hero section showing how elements nest via the flat array structure. The tree view shows the visual hierarchy, followed by the actual data.

```
section (Hero Section 06)
  └─ container
       ├─ block (Content Wrapper)
       │    ├─ heading (h1)
       │    ├─ text-basic (Tagline)
       │    ├─ text-basic (Lede)
       │    └─ div (Button Group)
       │         ├─ button
       │         └─ button (outline)
       └─ block (Media Wrapper)
            └─ image (eager, figure)
```

```json
[
  {
    "id": "13877b",
    "name": "section",
    "parent": 0,
    "children": ["65f029"],
    "settings": { "_cssGlobalClasses": ["skznjf"] },
    "label": "Hero Section 06"
  },
  {
    "id": "65f029",
    "name": "container",
    "parent": "13877b",
    "children": ["bf5a3e", "19454c"],
    "settings": { "_cssGlobalClasses": ["ubprdn"] }
  },
  {
    "id": "bf5a3e",
    "name": "block",
    "parent": "65f029",
    "children": ["c85e7f", "dfe903", "436fc0", "9b4d18"],
    "settings": { "_cssGlobalClasses": ["ebvzqj"] },
    "label": "Content Wrapper"
  },
  {
    "id": "c85e7f",
    "name": "heading",
    "parent": "bf5a3e",
    "children": [],
    "settings": {
      "text": "This hero headline is a temporary placeholder",
      "_cssGlobalClasses": ["deprgo"],
      "tag": "h1",
      "type": "hero"
    }
  },
  {
    "id": "dfe903",
    "name": "text-basic",
    "parent": "bf5a3e",
    "children": [],
    "settings": {
      "text": "Tagline",
      "tag": "p",
      "_cssGlobalClasses": ["dzwkrp", "xlqxzg"]
    },
    "label": "Tagline"
  },
  {
    "id": "436fc0",
    "name": "text-basic",
    "parent": "bf5a3e",
    "children": [],
    "settings": {
      "text": "While we're still finalizing our content, we've included this placeholder text to occupy the space temporarily.",
      "tag": "p",
      "_cssGlobalClasses": ["vpsyry", "ebhacb"]
    },
    "label": "Lede"
  },
  {
    "id": "9b4d18",
    "name": "div",
    "parent": "bf5a3e",
    "children": ["15596e", "c19a95"],
    "settings": { "_cssGlobalClasses": ["zoyzsf"] },
    "label": "Button Group"
  },
  {
    "id": "15596e",
    "name": "button",
    "parent": "9b4d18",
    "children": [],
    "settings": { "text": "Button" }
  },
  {
    "id": "c19a95",
    "name": "button",
    "parent": "9b4d18",
    "children": [],
    "settings": { "text": "Button Outline", "outline": true }
  },
  {
    "id": "19454c",
    "name": "block",
    "parent": "65f029",
    "children": ["849138"],
    "settings": { "_cssGlobalClasses": ["vxsvbb"] },
    "label": "Media Wrapper"
  },
  {
    "id": "849138",
    "name": "image",
    "parent": "19454c",
    "children": [],
    "settings": {
      "tag": "figure",
      "caption": "none",
      "image": {
        "id": 90346,
        "filename": "image_16-9_portrait.jpg",
        "size": "medium_large",
        "full": "https://example.com/wp-content/uploads/image_16-9_portrait.jpg",
        "url": "https://example.com/wp-content/uploads/image_16-9_portrait-768x1365.jpg"
      },
      "_cssGlobalClasses": ["zqibqu"],
      "loading": "eager"
    },
    "label": "Media",
    "themeStyles": []
  }
]
```

## Schema categories

### [Elements](./elements/accordion/)

Individual element schemas describing the settings, metadata, and value types for each element type. 182 element schemas available.

#### [Common](./elements/common/element/)

Shared element documentation: the [element schema](./elements/common/element/) (envelope, settings layers, meta-settings, selectors), [element conditions](./elements/common/conditions/) (display conditions with 32 condition keys and comparison operators), and [element interactions](./elements/common/interactions/) (event-driven behavior with triggers, actions, and sub-conditions).

### [General](./general/content-area/)

Foundational data structures: the [content area](./general/content-area/) schema (flat array container, storage, and meta keys).

### [Controls](./controls/text/)

Value schemas for each control type (text, select, checkbox, typography, etc.), describing the shape of data each control produces.

### [Global](./global/global-classes/)

Root schemas for global data structures: global classes, theme styles, components, color palettes, breakpoints, pseudo-classes, and global variables.

### [Settings](./settings/page/)

Page and template settings schemas describing the available settings controls.

---

# Audio Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/audio/

*Value schema for audio control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | — |
| `url` | string | — |
| `autoplay` | boolean | — |
| `loop` | boolean | — |
| `controls` | boolean | — |

---

# Align Items Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/align-items/

*Value schema for align-items control type*

---

# Background Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/background/

*Value schema for background control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `color` | any | Color value in various formats |
| `image` | object | Image settings |
| `video` | object | Video settings |
| `size` | string | — |
| `position` | string | — |
| `repeat` | string | One of: `repeat`, `repeat-x`, `repeat-y`, `no-repeat` |
| `attachment` | string | One of: `scroll`, `fixed`, `local` |

---

# Border Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/border/

*Value schema for border control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `width` | object | Spacing value with directional properties |
| `style` | string | One of: `none`, `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset` |
| `color` | any | Color value in various formats |
| `radius` | object | Spacing value with directional properties |

---

# Box Shadow Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/box-shadow/

*Value schema for box-shadow control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `values` | array | — |

---

# Button Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/button/

*UI-only control, no stored value*

---

# Checkbox Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/checkbox/

*Value schema for checkbox control type*

---

# Code Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/code/

*Value schema for code control type*

---

# Color Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/color/

*Value schema for color control type*

---

# Datepicker Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/datepicker/

*Date/time string*

---

# Direction Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/direction/

*Value schema for direction control type*

---

# Editor Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/editor/

*Rich text/HTML content*

---

# File Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/file/

*Value schema for file control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | — |
| `url` | string | — |

---

# Filters Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/filters/

*Value schema for filters control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `blur` | string | — |
| `brightness` | string | — |
| `contrast` | string | — |
| `grayscale` | string | — |
| `hue-rotate` | string | — |
| `invert` | string | — |
| `opacity` | string | — |
| `saturate` | string | — |
| `sepia` | string | — |

---

# Dimensions Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/dimensions/

*Unknown control type: dimensions*

---

# Icon Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/icon/

*Value schema for icon control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `library` | string | — |
| `icon` | string | — |
| `svg` | object | — |

---

# Image Gallery Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/image-gallery/

*Value schema for image-gallery control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `images` | array | — |

---

# Image Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/image/

*Value schema for image control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | — |
| `filename` | string | — |
| `url` | string | — |
| `size` | string | — |
| `full` | string | — |
| `useDynamicData` | string | — |

---

# Justify Content Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/justify-content/

*Value schema for justify-content control type*

---

# Number Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/number/

*Value schema for number control type*

---

# Query List Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/query-list/

*Unknown control type: query-list*

---

# Query Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/query/

*Value schema for query control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `NOTE` | any | — |
| `api_auth_api_key_name` | any | — |
| `api_auth_api_key_use_constant` | any | — |
| `api_auth_api_key_use_constant_info` | any | — |
| `api_auth_api_key_value` | any | — |
| `api_auth_api_location` | any | — |
| `api_auth_basic_password` | any | — |
| `api_auth_basic_use_constant` | any | — |
| `api_auth_basic_use_constant_info` | any | — |
| `api_auth_basic_username` | any | — |
| `api_auth_bearer_token` | any | — |
| `api_auth_bearer_use_constant` | any | — |
| `api_auth_bearer_use_constant_info` | any | — |
| `api_auth_sep` | any | — |
| `api_auth_type` | any | — |
| `api_body_json` | any | — |
| `api_body_params` | any | — |
| `api_body_type` | any | — |
| `api_docs` | any | — |
| `api_headers` | any | — |
| `api_method` | any | — |
| `api_name` | any | — |
| `api_params` | any | — |
| `api_params_sep` | any | — |
| `api_sep` | any | — |
| `api_url` | any | — |
| `body_separator` | any | — |
| `cache_time` | any | — |
| `headers_separator` | any | — |
| `id` | any | — |
| `objectType` | any | — |
| `pagination_enabled` | any | — |
| `pagination_method` | any | — |
| `pagination_page_offset_key` | any | — |
| `pagination_page_offset_key_location` | any | — |
| `pagination_page_param` | any | — |
| `pagination_param_location` | any | — |
| `pagination_separator` | any | — |
| `pagination_total_extract` | any | — |
| `response_path` | any | — |
| `response_separator` | any | — |

---

# Radio Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/radio/

*Unknown control type: radio*

---

# Repeater Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/repeater/

*Repeatable fields array*

---

# Select Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/select/

*Value schema for select control type*

---

# Spacing Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/spacing/

*Value schema for spacing control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `top` | string | Top spacing value with unit |
| `right` | string | Right spacing value with unit |
| `bottom` | string | Bottom spacing value with unit |
| `left` | string | Left spacing value with unit |

---

# Svg Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/svg/

*Value schema for svg control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | — |
| `url` | string | — |
| `library` | string | — |

---

# Link Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/link/

*Value schema for link control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `type` | string | — |
| `url` | string | — |
| `postId` | string \| integer | — |
| `newTab` | boolean | — |
| `rel` | string | — |
| `title` | string | — |
| `ariaLabel` | string | — |
| `lightboxId` | string | — |
| `lightboxType` | string | — |

---

# Text Align Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text-align/

*Value schema for text-align control type*

---

# Text Shadow Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text-shadow/

*Value schema for text-shadow control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `values` | array | — |

---

# Text Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text/

*Value schema for text control type*

---

# Transform Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/transform/

*Value schema for transform control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `translateX` | string | — |
| `translateY` | string | — |
| `translateZ` | string | — |
| `scaleX` | string | — |
| `scaleY` | string | — |
| `scaleZ` | string | — |
| `rotateX` | string | — |
| `rotateY` | string | — |
| `rotateZ` | string | — |
| `skewX` | string | — |
| `skewY` | string | — |
| `perspective` | string | — |

---

# Textarea Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/textarea/

*Value schema for textarea control type*

---

# Typography Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/typography/

*Value schema for typography control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `font-family` | string | — |
| `font-size` | string | — |
| `font-weight` | string \| integer | — |
| `font-style` | string | One of: `normal`, `italic`, `oblique` |
| `line-height` | string | — |
| `letter-spacing` | string | — |
| `text-align` | string | One of: `left`, `center`, `right`, `justify` |
| `text-transform` | string | One of: `none`, `uppercase`, `lowercase`, `capitalize` |
| `text-decoration` | string | — |
| `color` | any | Color value in various formats |

---

# Video Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/video/

*Value schema for video control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `source` | string | One of: `media`, `youtube`, `vimeo`, `url` |
| `id` | string \| integer | — |
| `url` | string | — |
| `youtubeId` | string | — |
| `vimeoId` | string | — |
| `autoplay` | boolean | — |
| `loop` | boolean | — |
| `muted` | boolean | — |
| `controls` | boolean | — |

---

# Content Area Schema

Source: https://academy.bricksbuilder.io/developer/schema/general/content-area/

*A Bricks content area is a flat array of elements stored in post meta. This page documents the array structure and storage.*

A content area is a flat array of element objects. Bricks uses three independent content areas per page (header, content, and footer), each stored in its own post meta key. The array is flat (not nested): parent-child relationships are expressed via the `parent` and `children` fields on each element.

For the structure of each element in the array, see the [Element schema](../elements/common/element/).

## Content areas

A Bricks page (or any post type using Bricks) stores its elements across three independent content areas:

| Content area | WordPress post meta key | Description |
|---|---|---|
| Header | `_bricks_page_header_2` | Header template elements |
| Content | `_bricks_page_content_2` | Main page/post content |
| Footer | `_bricks_page_footer_2` | Footer template elements |

All three use the exact same data structure: an array of elements as described in the [Element schema](../elements/common/element/).

## Storage

These are stored as serialized arrays in the `wp_postmeta` table.

| Data | Meta key | PHP constant |
|---|---|---|
| Header elements | `_bricks_page_header_2` | `BRICKS_DB_PAGE_HEADER` |
| Content elements | `_bricks_page_content_2` | `BRICKS_DB_PAGE_CONTENT` |
| Footer elements | `_bricks_page_footer_2` | `BRICKS_DB_PAGE_FOOTER` |

## Flat array structure

Elements reference each other by ID rather than nesting physically. A root-level element has `"parent": 0`; all others reference their parent's `id`. The `children` array on each element lists its direct children in order. This makes it easy to reorder, move, or flatten elements without restructuring a tree.

```json
[
  { "id": "aaa111", "name": "section", "parent": 0, "children": ["bbb222"], "settings": {} },
  { "id": "bbb222", "name": "heading", "parent": "aaa111", "children": [], "settings": { "text": "Hello" } }
]
```

The array may also contain component instances (identifiable by the presence of a `cid` field). See [Components](../global/components/) for details.

---

# Breakpoints Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/breakpoints/

*Documentation for Breakpoints Schema in Bricks Academy.*

## Item properties

| Property | Type | Description |
|---|---|---|
| `key` | string | — |
| `label` | string | — |
| `width` | integer | — |
| `widthBuilder` | integer | — |
| `icon` | string | — |
| `base` | boolean | — |
| `custom` | boolean | — |
| `edited` | boolean | — |
| `paused` | boolean | — |

---

# Color Palettes Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/color-palettes/

*Documentation for Color Palettes Schema in Bricks Academy.*

## Item properties

| Property | Type | Description |
|---|---|---|
| `id` | string | — |
| `name` | string | — |
| `colors` | array | — |

---

# Components Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/components/

*Documentation for Components Schema in Bricks Academy.*

## Item properties

| Property | Type | Description |
|---|---|---|
| `id` | string | — |
| `category` | string | — |
| `desc` | string | — |
| `elements` | array | — |
| `properties` | array | — |
| `propertyGroups` | array | — |
| `_created` | integer \| string | — |
| `_user_id` | integer \| string | — |
| `_version` | string | — |
| `variants` | array | — |
| `blockEditor` | integer \| boolean | — |
| `blockCategory` | string | — |
| `blockIcon` | object | — |
| `blockPreviewImage` | object | Image settings |

---

# Global Classes Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/global-classes/

*Documentation for Global Classes Schema in Bricks Academy.*

## Item properties

| Property | Type | Description |
|---|---|---|
| `id` | string | — |
| `name` | string | — |
| `category` | string | — |
| `settings` | dynamic | Dynamic map of all settings for this element or class. Keys are element-specific control names (e.g. `text`, `style`) or inherited CSS setting keys, optionally suffixed with a breakpoint and/or pseudo-class using colon syntax (e.g. `_typography:tablet_portrait:hover`). See the individual element schemas for available control keys. |
| `selectors` | array | Custom CSS selectors with scoped settings (since Bricks 2.0) |
| `modified` | integer \| string | — |
| `user_id` | integer \| string | — |
| `deletedAt` | integer \| string | — |

---

# Global Variables Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/global-variables/

*Documentation for Global Variables Schema in Bricks Academy.*

## Item properties

| Property | Type | Description |
|---|---|---|
| `id` | string | — |
| `name` | string | — |
| `value` | string | — |
| `category` | string | — |
| `type` | string | — |

---

# Pseudo-Classes Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/pseudo-classes/

*CSS pseudo-classes available in the builder for responsive/state variants. Stored as a WordPress option, user-configurable via Bricks settings.*

---

# Theme Styles Schema

Source: https://academy.bricksbuilder.io/developer/schema/global/theme-styles/

*Full schema for Bricks theme styles: per-section controls, types, CSS properties, and selectors.*

Theme styles define global CSS defaults for element types (buttons, headings, typography, etc.) and site-wide settings (colors, links, spacing). They are stored in the `bricks_theme_styles` WordPress option.

## Data structure

Each theme style has a `label` and a `settings` object. The settings object is keyed by section name, and each section contains controls that map to CSS properties.

## Storage

| Data | Option name | PHP constant |
|---|---|---|
| Theme styles | `bricks_theme_styles` | `BRICKS_DB_THEME_STYLES` |

The option value is an associative array keyed by theme style ID (e.g. `"flavor"`), with each entry being a `themeStyle` object.

## Responsive and state variants

Theme style control keys support the same colon syntax as element settings for breakpoint and pseudo-class variants:

```
typography                          → base breakpoint
typography:tablet_portrait          → tablet portrait
typography:mobile_portrait:hover    → mobile + hover
```

## Sections

### Accordion

Section key: `accordion`

Theme style controls for the "accordion" section. Default CSS selector: .brxe-accordion

| Key | Type | Label | CSS |
|---|---|---|---|
| `accordionIcon` | icon | Icon | — |
| `accordionIconExpanded` | icon | Icon expanded | — |
| `titleTypography` | typography | Title typography | `font` on `.accordion-title .title` |
| `subtitleTypography` | typography | Subtitle typography | `font` on `.accordion-subtitle` |
| `contentTypography` | typography | Content typography | `font` on `.accordion-content-wrapper` |

### Alert

Section key: `alert`

Theme style controls for the "alert" section. Default CSS selector: .brxe-alert

| Key | Type | Label | CSS |
|---|---|---|---|
| `padding` | spacing | Padding | `padding` |
| `typography` | typography | Typography | `font` |
| `border` | border | Border | `border` |
| `infoColor` | color | Text color | `color` on `&.info` |
| `infoBackground` | color | Background color | `background-color` on `&.info` |
| `infoBorder` | border | Border | `border` on `&.info` |
| `successColor` | color | Text color | `color` on `&.success` |
| `successBackground` | color | Background color | `background-color` on `&.success` |
| `successBorder` | border | Border | `border` on `&.success` |
| `warningColor` | color | Text color | `color` on `&.warning` |
| `warningBackground` | color | Background color | `background-color` on `&.warning` |
| `warningBorder` | border | Border | `border` on `&.warning` |
| `dangerColor` | color | Text color | `color` on `&.danger` |
| `dangerBackground` | color | Background color | `background-color` on `&.danger` |
| `dangerBorder` | border | Border | `border` on `&.danger` |
| `mutedColor` | color | Text color | `color` on `&.muted` |
| `mutedBackground` | color | Background color | `background-color` on `&.muted` |
| `mutedBorder` | border | Border | `border` on `&.muted` |

### Block

Section key: `block`

Theme style controls for the "block" section. Default CSS selector: .brxe-block

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))`, `align-items` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_gridGap` | number | Gap | `gap` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-block` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-block` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_alignItemsGrid` | align-items | Align items | `align-items` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_alignContentGrid` | align-items | Align content | `align-content` on `.brxe-block:where(:not(.accordion-content-wrapper):not(.accordion-title-wrapper))` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-block` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-block` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-block` |
| `width` | number | Width | `width` on `.brxe-block` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-block` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-block` |
| `margin` | spacing | Margin | `margin` on `.brxe-block` |
| `padding` | spacing | Padding | `padding` on `.brxe-block` |

### Button

Section key: `button`

Theme style controls for the "button" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.bricks-button` |
| `background` | color | Background color | `background-color` on `.bricks-button:where(:not([class*="bricks-background-"]):not([class*="bricks-color-"]):not(.outline))` |
| `border` | border | Border | `border` on `.bricks-button` |
| `boxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-button` |
| `transition` | text | Transition | `transition` on `.bricks-button` |
| `outlineTypography` | typography | Outline | `font` on `.bricks-button:where(.outline)` |
| `outlineBackground` | color | Outline | `background-color` on `.bricks-button:where(.outline)` |
| `outlineBorder` | border | Outline | `border` on `.bricks-button:where(.outline)` |
| `outlineBoxShadow` | box-shadow | Outline | `box-shadow` on `.bricks-button:where(.outline)` |
| `primaryTypography` | typography | Typography | `font` |
| `primaryBackground` | color | Background color | `background-color` |
| `primaryBorder` | border | Border | `border` |
| `primaryBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `primaryOutlineTypography` | typography | Outline | `font` |
| `primaryOutlineBackground` | color | Outline | `background-color` |
| `primaryOutlineBorder` | border | Outline | `border` |
| `primaryOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `secondaryTypography` | typography | Typography | `font` |
| `secondaryBackground` | color | Background color | `background-color` |
| `secondaryBorder` | border | Border | `border` |
| `secondaryBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `secondaryOutlineTypography` | typography | Outline | `font` |
| `secondaryOutlineBackground` | color | Outline | `background-color` |
| `secondaryOutlineBorder` | border | Outline | `border` |
| `secondaryOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `lightTypography` | typography | Typography | `font` |
| `lightBackground` | color | Background color | `background-color` |
| `lightBorder` | border | Border | `border` |
| `lightBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `lightOutlineTypography` | typography | Outline | `font` |
| `lightOutlineBackground` | color | Outline | `background-color` |
| `lightOutlineBorder` | border | Outline | `border` |
| `lightOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `darkTypography` | typography | Typography | `font` |
| `darkBackground` | color | Background color | `background-color` |
| `darkBorder` | border | Border | `border` |
| `darkBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `darkOutlineTypography` | typography | Outline | `font` |
| `darkOutlineBackground` | color | Outline | `background-color` |
| `darkOutlineBorder` | border | Outline | `border` |
| `darkOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `mutedTypography` | typography | Typography | `font` |
| `mutedBackground` | color | Background color | `background-color` |
| `mutedBorder` | border | Border | `border` |
| `mutedBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `mutedOutlineTypography` | typography | Outline | `font` |
| `mutedOutlineBackground` | color | Outline | `background-color` |
| `mutedOutlineBorder` | border | Outline | `border` |
| `mutedOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `infoTypography` | typography | Typography | `font` |
| `infoBackground` | color | Background color | `background-color` |
| `infoBorder` | border | Border | `border` |
| `infoBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `infoOutlineTypography` | typography | Outline | `font` |
| `infoOutlineBackground` | color | Outline | `background-color` |
| `infoOutlineBorder` | border | Outline | `border` |
| `infoOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `successTypography` | typography | Typography | `font` |
| `successBackground` | color | Background color | `background-color` |
| `successBorder` | border | Border | `border` |
| `successBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `successOutlineTypography` | typography | Outline | `font` |
| `successOutlineBackground` | color | Outline | `background-color` |
| `successOutlineBorder` | border | Outline | `border` |
| `successOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `warningTypography` | typography | Typography | `font` |
| `warningBackground` | color | Background color | `background-color` |
| `warningBorder` | border | Border | `border` |
| `warningBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `warningOutlineTypography` | typography | Outline | `font` |
| `warningOutlineBackground` | color | Outline | `background-color` |
| `warningOutlineBorder` | border | Outline | `border` |
| `warningOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `dangerTypography` | typography | Typography | `font` |
| `dangerBackground` | color | Background color | `background-color` |
| `dangerBorder` | border | Border | `border` |
| `dangerBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `dangerOutlineTypography` | typography | Outline | `font` |
| `dangerOutlineBackground` | color | Outline | `background-color` |
| `dangerOutlineBorder` | border | Outline | `border` |
| `dangerOutlineBoxShadow` | box-shadow | Outline | `box-shadow` |
| `sizeDefaultPadding` | spacing | Padding | `padding` on `.bricks-button` |
| `sizeSmPadding` | spacing | Padding | `padding` on `.bricks-button:where(.sm)` |
| `sizeSmTypography` | typography | Typography | `font` on `.bricks-button:where(.sm)` |
| `sizeMdPadding` | spacing | Padding | `padding` on `.bricks-button:where(.md)` |
| `sizeMdTypography` | typography | Typography | `font` on `.bricks-button:where(.md)` |
| `sizeLgPadding` | spacing | Padding | `padding` on `.bricks-button:where(.lg)` |
| `sizeLgTypography` | typography | Typography | `font` on `.bricks-button:where(.lg)` |
| `sizeXlPadding` | spacing | Padding | `padding` on `.bricks-button:where(.xl)` |
| `sizeXlTypography` | typography | Typography | `font` on `.bricks-button:where(.xl)` |

### Carousel

Section key: `carousel`

No typed controls extracted for this section. It uses the generic theme style control map.

### Code

Section key: `code`

Theme style controls for the "code" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `prettify` | select | Theme | — |

### Colors

Section key: `colors`

Theme style controls for the "colors" section. Default CSS selector: :where(:root)

| Key | Type | Label | CSS |
|---|---|---|---|
| `colorPrimary` | color | Primary color | `color` on `.bricks-color-primary`, `background-color` on `.bricks-background-primary` |
| `colorSecondary` | color | Secondary color | `color` on `.bricks-color-secondary`, `background-color` on `.bricks-background-secondary` |
| `colorLight` | color | Light color | `color` on `.bricks-color-light`, `background-color` on `.bricks-background-light` |
| `colorDark` | color | Dark color | `color` on `.bricks-color-dark`, `background-color` on `.bricks-background-dark` |
| `colorMuted` | color | Muted color | `color` on `.bricks-color-muted`, `background-color` on `.bricks-background-muted` |
| `colorBorder` | color | Border color | `border-color` on `*` |
| `colorInfo` | color | Info color | `color` on `.bricks-color-info`, `background-color` on `.bricks-background-info` |
| `colorSuccess` | color | Success color | `color` on `.bricks-color-success`, `background-color` on `.bricks-background-success` |
| `colorWarning` | color | Warning color | `color` on `.bricks-color-warning`, `background-color` on `.bricks-background-warning` |
| `colorDanger` | color | Danger color | `color` on `.bricks-color-danger`, `background-color` on `.bricks-background-danger` |

### Conditions

Section key: `conditions`

Theme style controls for the "conditions" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `conditions` | repeater | Style conditions | — |

### Container

Section key: `container`

Theme style controls for the "container" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-container`, `align-items` on `.brxe-container` |
| `_gridGap` | number | Gap | `gap` on `.brxe-container` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-container` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-container` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` on `.brxe-container` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` on `.brxe-container` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` on `.brxe-container` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` on `.brxe-container` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` on `.brxe-container` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` on `.brxe-container` |
| `_alignItemsGrid` | align-items | Align items | `align-items` on `.brxe-container` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` on `.brxe-container` |
| `_alignContentGrid` | align-items | Align content | `align-content` on `.brxe-container` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-container` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-container` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-container` |
| `width` | number | Width | `width` on `.brxe-container`, `width` on `.woocommerce main.site-main`, `width` on `#brx-content.wordpress` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-container`, `min-width` on `#brx-content.wordpress` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-container`, `max-width` on `#brx-content.wordpress` |
| `margin` | spacing | Margin | `margin` on `.brxe-container` |
| `padding` | spacing | Padding | `padding` on `.brxe-container` |

### Content

Section key: `content`

Theme style controls for the "content" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `contentMargin` | spacing | Margin | `margin` on `#brx-content`, `margin` on `.content-area` |
| `contentBlockquoteMargin` | spacing | Margin | `margin` on `blockquote` |
| `contentBlockquotePadding` | spacing | Padding | `padding` on `blockquote` |
| `contentBlockquoteBorder` | border | Border | `border` on `blockquote` |
| `contentBlockquoteTypography` | typography | Typography | `font` on `blockquote` |

### Contextual-spacing

Section key: `contextual-spacing`

No typed controls extracted for this section. It uses the generic theme style control map.

### Contextual Spacing

Section key: `contextualSpacing`

Theme style controls for the "contextualSpacing" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `contextualSpacingRemoveDefaultMargins` | select | Remove default margins | — |
| `contextualSpacingRemoveDefaultPadding` | select | Remove default padding | — |
| `contextualSpacingHeading` | number | Heading | `margin-block-start` |
| `contextualSpacingParagraph` | number | Paragraph | `margin-block-start` |
| `contextualSpacingFallback` | number | Fallback spacing | `margin-block-start` |
| `contextualSpacingCustomTarget` | repeater | Selector | `margin-block-start` |
| `contextualSpacingApplyTo` | text | contextualSpacingApplyTo | — |

### Counter

Section key: `counter`

Theme style controls for the "counter" section. Default CSS selector: .brxe-counter

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` |

### Css

Section key: `css`

No typed controls extracted for this section. It uses the generic theme style control map.

### Div

Section key: `div`

Theme style controls for the "div" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-div:where(:not(.brx-dropdown-content))`, `align-items` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_gridGap` | number | Gap | `gap` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-div` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-div` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_alignItemsGrid` | align-items | Align items | `align-items` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_alignContentGrid` | align-items | Align content | `align-content` on `.brxe-div:where(:not(.brx-dropdown-content))` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-div` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-div` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-div` |
| `width` | number | Width | `width` on `.brxe-div` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-div` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-div` |
| `margin` | spacing | Margin | `margin` on `.brxe-div` |
| `padding` | spacing | Padding | `padding` on `.brxe-div` |

### Divider

Section key: `divider`

Theme style controls for the "divider" section. Default CSS selector: .brxe-divider

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `border-top-width` on `.line` |
| `color` | color | Color | `border-top-color` on `&.horizontal .line`, `border-right-color` on `&.vertical .line`, `color` on `.icon i` |

### Elements

Section key: `elements`

No typed controls extracted for this section. It uses the generic theme style control map.

### Form

Section key: `form`

Theme style controls for the "form" section. Default CSS selector: .brxe-form

| Key | Type | Label | CSS |
|---|---|---|---|
| `labelTypography` | typography | Label typography | `font` on `.form-group label`, `font` on `.form-group .label` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder`, `font` on `select` |
| `fieldTypography` | typography | Typography | `font` on `.form-group input`, `font` on `select`, `font` on `textarea` |
| `fieldBackgroundColor` | color | Background color | `background-color` on `.form-group input`, `background-color` on `.flatpickr`, `background-color` on `select`, `background-color` on `textarea`, `background-color` on `.form-field-richtext + .tox-tinymce` |
| `fieldBorder` | border | Border | `border` on `.form-group input`, `border` on `.flatpickr`, `border` on `select`, `border` on `textarea`, `border` on `.form-field-richtext + .tox-tinymce`, `border` on `.bricks-button`, `border` on `.choose-files` |
| `fieldMargin` | spacing | Spacing | `padding` on `.form-group` |
| `fieldPadding` | spacing | Padding | `padding` on `.form-group input`, `padding` on `.flatpickr`, `padding` on `select`, `padding` on `textarea`, `padding` on `.form-field-richtext + .tox-tinymce .tox-edit-area__iframe` |
| `submitButtonPadding` | spacing | Padding | `padding` on `.bricks-button` |
| `submitButtonTypography` | typography | Typography | `font` on `.bricks-button` |
| `submitButtonBackgroundColor` | color | Background color | `background-color` on `.bricks-button` |
| `submitButtonBorder` | border | Border | `border` on `.bricks-button` |

### General

Section key: `general`

Theme style controls for the "general" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `siteLayout` | select | Site layout | — |
| `siteLayoutBoxedMaxWidth` | number | Boxed max. width | `max-width` on `.brx-boxed`, `max-width` on `.brx-boxed #brx-header.brx-sticky`, `margin-left` on `.brx-boxed #brx-header.brx-sticky`, `margin-right` on `.brx-boxed #brx-header.brx-sticky` |
| `contentBoxShadow` | box-shadow | Content box shadow | `box-shadow` on `.brx-boxed` |
| `contentBackground` | background | Content background | `background` on `.brx-boxed` |
| `siteBackground` | background | Site background | `background` on `html`, `background` on `body` |
| `siteBorder` | border | Site border | `border` on `.brx-boxed` |
| `elementMargin` | spacing | Element margin | `margin` on `[class*="brxe-"]:not(.brxe-section):not(.brxe-container):not(.brxe-div)` |
| `sectionMargin` | spacing | Root container margin | `margin` on `.brxe-container.root` |
| `sectionPadding` | spacing | Root container padding | `padding` on `.brxe-container.root:not(.stretch)`, `padding` on `.brxe-container.root.stretch > .brxe-container`, `padding` on `.brxe-container.root.stretch > .brxe-div` |
| `containerMaxWidth` | number | Root container width | `width` on `.brxe-container.root`, `width` on `.brxe-container.root.stretch > .brxe-container`, `width` on `.brxe-container.root.stretch > .brxe-div`, `width` on `.woocommerce main.site-main`, `width` on `#brx-content.wordpress` |
| `lightboxBackground` | background | Background | `background` on `.pswp .pswp__bg` |
| `lightboxCloseColor` | color | Close color | `color` on `.pswp.brx .pswp__top-bar button.pswp__button--close svg` |
| `lightboxCloseSize` | number | Close size | `width` on `.pswp.brx .pswp__top-bar button.pswp__button svg`, `height` on `.pswp.brx .pswp__top-bar button.pswp__button svg` |
| `lightboxWidth` | number | Width | — |
| `lightboxHeight` | number | Height | — |

### Heading

Section key: `heading`

Theme style controls for the "heading" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | HTML tag | — |
| `separator` | select | Separator | — |
| `separatorWidth` | number | Width | `width` on `.brxe-heading .separator`, `flex-grow` on `.brxe-heading .separator` |
| `separatorHeight` | number | Height | `border-top-width` on `.brxe-heading .separator` |
| `separatorSpacing` | number | Spacing | `gap` on `.brxe-heading.has-separator` |
| `separatorAlignItems` | align-items | Align | `align-items` on `.brxe-heading.has-separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.brxe-heading .separator` |
| `separatorColor` | color | Color | `border-top-color` on `.brxe-heading .separator` |
| `separatorMargin` | spacing | Margin | `margin` on `.brxe-heading .separator` |

### Icon-box

Section key: `icon-box`

Theme style controls for the "icon-box" section. Default CSS selector: .brxe-icon-box

| Key | Type | Label | CSS |
|---|---|---|---|
| `verticalAlign` | align-items | Icon align | `align-self` on `.icon` |
| `iconMargin` | spacing | Icon margin | `margin` on `.icon` |
| `iconPadding` | spacing | Icon padding | `padding` on `.icon` |
| `textAlign` | text-align | Text align | `text-align`, `align-self` on `.icon` |
| `iconSize` | number | Icon size | `font-size` on `.icon i` |
| `iconHeight` | number | Icon height | `height` on `.icon`, `line-height` on `.icon` |
| `iconWidth` | number | Icon width | `min-width` on `.icon` |
| `iconColor` | color | Icon color | `color` on `.icon`, `color` on `.icon a` |
| `iconBackgroundColor` | color | Icon background | `background-color` on `.icon` |
| `iconBorder` | border | Icon border | `border` on `.icon` |
| `iconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `.icon` |
| `typographyHeading` | typography | Heading typography | `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `typographyBody` | typography | Body typography | `font` on `.content` |
| `contentBackgroundColor` | color | Content background | `background-color` on `.content` |
| `contentBorder` | border | Content border | `border` on `.content` |
| `contentBoxShadow` | box-shadow | Content box shadow | `box-shadow` on `.content` |
| `contentMargin` | spacing | Content margin | `margin` on `.content` |
| `contentPadding` | spacing | Content padding | `padding` on `.content` |

### Image

Section key: `image`

Theme style controls for the "image" section. Default CSS selector: .brxe-image

| Key | Type | Label | CSS |
|---|---|---|---|
| `popupIcon` | icon | Icon | — |
| `popupIconBackgroundColor` | color | Icon background color | `background-color` on `.brxe-image .icon` |
| `popupIconBorder` | border | Icon border | `border` on `.brxe-image .icon` |
| `popupIconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `.brxe-image .icon` |
| `popupIconHeight` | number | Icon height | `line-height` on `.brxe-image .icon` |
| `popupIconWidth` | number | Icon width | `width` on `.brxe-image .icon` |
| `popupIconTypography` | typography | Icon typography | `font` on `.brxe-image .icon` |
| `caption` | select | Caption type | — |
| `captionCustomStyles` | checkbox | Custom styles | — |
| `captionMargin` | spacing | Margin | `margin` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionPadding` | spacing | Padding | `padding` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionPosition` | select | Position | `position` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)`, `position` on `.wp-block-image:has(.wp-element-caption:not(.wp-block-gallery *))` |
| `captionPositions` | dimensions | Position | `—` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBackgroundColor` | color | Background color | `background` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)`, `text-shadow` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBorder` | border | Border | `border` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |
| `captionTypography` | typography | Typography | `font` on `.brxe-image .bricks-image-caption-custom, .wp-element-caption:not(.wp-block-gallery *)` |

### Image-gallery

Section key: `image-gallery`

Theme style controls for the "image-gallery" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `layout` | select | Layout | — |
| `imageRatio` | text | Image ratio | `aspect-ratio` on `.image` |
| `columns` | number | Columns | — |
| `imageHeight` | number | Image height | `padding-top` on `.brxe-image-gallery .image` |
| `gutter` | number | Spacing | `--gutter` on `.brxe-image-gallery` |
| `captionMargin` | spacing | Margin | `margin` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionPadding` | spacing | Padding | `padding` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionPosition` | select | Position | `position` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `flex` on `.wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `display` on `.wp-block-gallery.has-nested-images figure.wp-block-image:has(figcaption):before` |
| `captionPositions` | dimensions | Position | `—` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `width` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBackgroundColor` | color | Background color | `background` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption`, `text-shadow` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBorder` | border | Border | `border` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |
| `captionTypography` | typography | Typography | `font` on `.brxe-image-gallery .bricks-image-caption, .wp-block-gallery.has-nested-images figure.wp-block-image figcaption.wp-element-caption` |

### Links

Section key: `links`

Theme style controls for the "links" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `cssSelectors` | textarea | Link | — |
| `typography` | typography | Typography | `font` |
| `background` | background | Background | `background` |
| `border` | border | Border | `border` |
| `padding` | spacing | Padding | `padding` |
| `textDecoration` | text-decoration | Text decoration | `text-decoration` |
| `transition` | text | Transition | `transition` |

### List

Section key: `list`

Theme style controls for the "list" section. Default CSS selector: .brxe-list

| Key | Type | Label | CSS |
|---|---|---|---|
| `itemMargin` | spacing | Margin | `margin` on `li` |
| `itemPadding` | spacing | Padding | `padding` on `li` |
| `itemOddBackground` | color | Odd background | `background-color` on `li:nth-child(odd)` |
| `itemEvenBackground` | color | Even background | `background-color` on `li:nth-child(even)` |
| `itemBorder` | border | Border | `border` on `li` |
| `itemAutoWidth` | checkbox | Auto width | `justify-content` on `.content`, `flex-grow` on `.separator` |
| `highlightBlock` | checkbox | Block | `display` on `li[data-highlight]::before` |
| `highlightLabelPadding` | spacing | Padding | `padding` on `li[data-highlight]::before` |
| `highlightLabelBackground` | color | Background | `background-color` on `li[data-highlight]::before` |
| `highlightLabelBorder` | border | Border | `border` on `li[data-highlight]::before` |
| `highlightLabelTypography` | typography | Typography | `font` on `li[data-highlight]::before` |
| `highlightContentPadding` | spacing | Padding | `padding` on `li[data-highlight] + div` |
| `highlightContentBackground` | color | Background | `background-color` on `li[data-highlight] + div` |
| `highlightContentBorder` | border | Border | `border` on `li[data-highlight] + div` |
| `highlightContentColor` | color | Text color | `color` on `li[data-highlight] + div .title`, `color` on `li[data-highlight] + div .meta`, `color` on `li[data-highlight] + div .description` |
| `titleMargin` | spacing | Margin | `margin` on `.title` |
| `titleTypography` | typography | Typography | `font` on `.title` |
| `metaMargin` | spacing | Margin | `margin` on `.meta` |
| `metaTypography` | typography | Typography | `font` on `.meta` |
| `descriptionTypography` | typography | Typography | `font` on `.description` |
| `separatorDisable` | checkbox | Disable | `display` on `.separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.separator` |
| `separatorWidth` | number | Width | `flex-basis` on `.separator` |
| `separatorHeight` | number | Height | `border-top-width` on `.separator` |
| `separatorColor` | color | Color | `border-top-color` on `.separator` |

### Nav-menu

Section key: `nav-menu`

Theme style controls for the "nav-menu" section. Default CSS selector: .brxe-nav-menu

| Key | Type | Label | CSS |
|---|---|---|---|
| `menuMargin` | spacing | Margin | `margin` on `.bricks-nav-menu > li` |
| `menuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu > li > a`, `padding` on `.bricks-nav-menu > li > .brx-submenu-toggle > *` |
| `menuAlignment` | direction | Alignment | `flex-direction` on `.bricks-nav-menu` |
| `menuTypography` | typography | Typography | `font` on `.bricks-nav-menu > li > a`, `font` on `.bricks-nav-menu > li > .brx-submenu-toggle` |
| `menuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .current-menu-item > a`, `font` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle` |
| `menuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .current-menu-item > a`, `border` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle` |
| `subMenuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu .sub-menu a`, `padding` on `.bricks-nav-menu .sub-menu button` |
| `subMenuTypography` | typography | Typography | `font` on `.bricks-nav-menu .sub-menu > li` |
| `subMenuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle` |
| `subMenuBackground` | background | Background | `background` on `.bricks-nav-menu .sub-menu .menu-item` |
| `subMenuBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu` |
| `subMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-nav-menu .sub-menu` |

### Popup

Section key: `popup`

No typed controls extracted for this section. It uses the generic theme style control map.

### Popups

Section key: `popups`

No typed controls extracted for this section. It uses the generic theme style control map.

### Post-content

Section key: `post-content`

Theme style controls for the "post-content" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.brxe-post-content` |

### Post-meta

Section key: `post-meta`

Theme style controls for the "post-meta" section. Default CSS selector: .brxe-post-meta

| Key | Type | Label | CSS |
|---|---|---|---|
| `padding` | spacing | Padding | `padding` on `.item` |
| `gutter` | number | Gap | `width` on `.separator` |
| `background` | color | Background | `background-color` on `.item` |
| `border` | border | Border | `border` on `.item` |
| `typography` | typography | Typography | `font` on `.item` |

### Post-navigation

Section key: `post-navigation`

Theme style controls for the "post-navigation" section. Default CSS selector: .brxe-post-navigation

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleTypography` | typography | Title typography | `font` on `.title` |
| `labelTypography` | typography | Label typography | `font` on `label` |
| `imageBorder` | border | Image border | `border` on `.image` |

### Post-taxonomy

Section key: `post-taxonomy`

Theme style controls for the "post-taxonomy" section. Default CSS selector: .brxe-post-taxonomy

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Margin | `margin` on `.bricks-button` |
| `padding` | spacing | Padding | `padding` on `.bricks-button` |
| `background` | color | Background | `background-color` on `.bricks-button` |
| `border` | border | Border | `border` on `.bricks-button` |
| `typography` | typography | Typography | `font` on `.bricks-button` |

### Post-title

Section key: `post-title`

Theme style controls for the "post-title" section. Default CSS selector: .brxe-post-title

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` |

### Pricing-tables

Section key: `pricing-tables`

Theme style controls for the "pricing-tables" section. Default CSS selector: .brxe-pricing-tables

| Key | Type | Label | CSS |
|---|---|---|---|
| `background` | background | Table background | `background` on `.pricing-table` |
| `headerPadding` | spacing | Padding | `padding` on `.pricing-table-header` |
| `headerBackgroundColor` | color | Background color | `background-color` on `.pricing-table-header` |
| `headerBorder` | border | Border | `border` on `.pricing-table-header` |
| `headerTitleTypography` | typography | Title typography | `font` on `.pricing-table-title` |
| `headerSubtitleTypography` | typography | Subtitle typography | `font` on `.pricing-table-subtitle` |
| `pricePadding` | spacing | Padding | `padding` on `.pricing-table-pricing` |
| `priceBackgroundColor` | color | Background color | `background-color` on `.pricing-table-pricing` |
| `priceBorder` | border | Border | `Border` on `.pricing-table-pricing` |
| `priceTypography` | typography | Price typography | `font` on `.pricing-table-price-prefix`, `font` on `.pricing-table-price`, `font` on `.pricing-table-price-suffix` |
| `priceMetaTypography` | typography | Meta typography | `font` on `.pricing-table-price-meta` |
| `priceOriginalTypography` | typography | Original price typography | `font` on `.pricing-table-original-price` |
| `featuresPadding` | spacing | Padding | `padding` on `.pricing-table-feature` |
| `featuresIconColor` | color | Icon color | `color` on `.pricing-table-feature i` |
| `featuresBackgroundColor` | color | Background color | `background-color` on `.pricing-table-feature` |
| `featuresBorder` | border | Border | `border` on `.pricing-table-feature` |
| `featuresTypography` | typography | Features typography | `font` on `.pricing-table-feature` |
| `footerPadding` | spacing | Padding | `padding` on `.pricing-table-footer` |
| `footerBackgroundColor` | color | Background color | `background-color` on `.pricing-table-footer` |
| `footerBorder` | border | Border | `border` on `.pricing-table-footer` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border` on `.bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `.bricks-button` |
| `additionalInfoTypography` | typography | Typography | `font` on `.pricing-table-additional-info` |
| `ribbonTextColor` | color | Text color | `color` on `.pricing-table-ribbon-title` |
| `ribbonBackgroundColor` | color | Background color | `background-color` on `.pricing-table-ribbon-title` |

### Progress-bar

Section key: `progress-bar`

Theme style controls for the "progress-bar" section. Default CSS selector: .brxe-progress-bar

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `height` on `.bar` |
| `barColor` | color | Bar color | `background-color` on `.bar span` |
| `barBackgroundColor` | color | Bar background color | `background-color` on `.bar` |
| `barBorder` | border | Bar border | `border` on `.bar` |
| `labelTypography` | typography | Label typography | `font` on `.label` |
| `percentageTypography` | typography | Percentage typography | `font` on `.percentage` |

### Related-posts

Section key: `related-posts`

Theme style controls for the "related-posts" section. Default CSS selector: .brxe-related-posts

| Key | Type | Label | CSS |
|---|---|---|---|
| `contentBackground` | color | Content background | `background-color` on `.post-content` |
| `contentPadding` | spacing | Content padding | `padding` on `.post-content` |

### Search

Section key: `search`

Theme style controls for the "search" section. Default CSS selector: .brxe-search

| Key | Type | Label | CSS |
|---|---|---|---|
| `inputBackgroundColor` | color | Input background | `background-color` on `input[type=search]` |
| `inputBorder` | border | Input border | `border` on `input[type=search]` |
| `iconBackgroundColor` | color | Icon background | `background-color` on `button` |
| `iconTypography` | typography | Icon typography | `font` on `button` |
| `iconWidth` | number | Icon width | `width` on `button` |

### Section

Section key: `section`

Theme style controls for the "section" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `_display` | select | Display | `display` on `.brxe-section`, `align-items` on `.brxe-section` |
| `_gridGap` | number | Gap | `gap` on `.brxe-section` |
| `_columnGap` | number | Column gap | `column-gap` on `.brxe-section` |
| `_rowGap` | number | Row gap | `row-gap` on `.brxe-section` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` on `.brxe-section` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` on `.brxe-section` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` on `.brxe-section` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` on `.brxe-section` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` on `.brxe-section` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` on `.brxe-section` |
| `_alignItemsGrid` | align-items | Align items | `align-items` on `.brxe-section` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` on `.brxe-section` |
| `_alignContentGrid` | align-items | Align content | `align-content` on `.brxe-section` |
| `_direction` | direction | Direction | `flex-direction` on `.brxe-section` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` on `.brxe-section` |
| `_alignItems` | align-items | Align cross axis | `align-items` on `.brxe-section` |
| `width` | number | Width | `width` on `.brxe-section` |
| `widthMin` | number | Min. width | `min-width` on `.brxe-section` |
| `widthMax` | number | Max. width | `max-width` on `.brxe-section` |
| `margin` | spacing | Margin | `margin` on `.brxe-section` |
| `padding` | spacing | Padding | `padding` on `.brxe-section` |

### Sidebar

Section key: `sidebar`

Theme style controls for the "sidebar" section. Default CSS selector: .brxe-sidebar

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Widget margin | `margin` on `.bricks-widget-wrapper` |
| `titleTypography` | typography | Widget title | `font` on `.bricks-widget-title`, `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `contentTypography` | typography | Content typography | `font` |
| `searchBackground` | color | Search background color | `background-color` on `input[type=search]` |

### Slider

Section key: `slider`

Theme style controls for the "slider" section. Default CSS selector: .brxe-slider

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleMargin` | spacing | Title margin | `margin` on `.title` |
| `titleTypography` | typography | Title typography | `font` on `.title` |
| `contentWidth` | number | Content width | `width` on `.slider-content` |
| `contentBackgroundColor` | color | Content background | `background-color` on `.slider-content` |
| `contentMargin` | spacing | Content margin | `margin` on `.slider-content` |
| `contentPadding` | spacing | Content padding | `padding` on `.slider-content` |
| `contentAlignHorizontal` | select | Content align horizontal | `justify-content` on `.swiper-slide` |
| `contentAlignVertical` | align-items | Content align vertical | `align-items` on `.swiper-slide` |
| `contentTextAlign` | text-align | Content text align | `text-align` on `.slider-content` |
| `contentTypography` | typography | Content typography | `font` on `.content` |
| `buttonStyle` | select | Style | — |
| `buttonSize` | select | Size | — |
| `buttonBackground` | color | Background | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border` on `.bricks-button` |
| `buttonBoxshadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-button` |
| `buttonTypography` | typography | Button typography | `color` on `.bricks-button` |
| `backgroundFilters` | filters | CSS Filters | `filter` on `.css-filter` |
| `backgroundPositionTop` | number | backgroundPositionTop | `top` on `.image` |
| `backgroundPositionRight` | number | Right | `right` on `.image` |
| `backgroundPositionBottom` | number | Bottom | `bottom` on `.image` |
| `backgroundPositionLeft` | number | Left | `left` on `.image` |

### Social-icons

Section key: `social-icons`

Theme style controls for the "social-icons" section. Default CSS selector: .brxe-social-icons

| Key | Type | Label | CSS |
|---|---|---|---|
| `margin` | spacing | Margin | `margin` on `li` |
| `padding` | spacing | Padding | `padding` on `li` |
| `backgroundColor` | color | Background color | `background-color` on `li` |
| `border` | border | Border | `border` on `li` |
| `typography` | typography | Typography | `font` on `li` |

### Svg

Section key: `svg`

Theme style controls for the "svg" section. Default CSS selector: .brxe-svg

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `height` |
| `width` | number | Width | `width` |
| `strokeWidth` | number | Stroke width | `stroke-width` on `*` |
| `stroke` | color | Stroke color | `stroke` on `*` |
| `fill` | color | Fill | `fill` on `*` |

### Tabs

Section key: `tabs`

Theme style controls for the "tabs" section. Default CSS selector: .brxe-tabs

| Key | Type | Label | CSS |
|---|---|---|---|
| `titlePadding` | spacing | Padding | `padding` on `.tab-title` |
| `titleTypography` | typography | Typography | `font` on `.tab-title` |
| `titleBackgroundColor` | color | Background | `background-color` on `.tab-title` |
| `titleBorder` | border | Border | `border` on `.tab-title` |
| `titleActiveTypography` | typography | Active typography | `font` on `.tab-title.brx-open` |
| `titleActiveBackgroundColor` | color | Active background | `background-color` on `.tab-title.brx-open` |
| `titleActiveBorder` | border | Active border | `border` on `.tab-title.brx-open` |
| `contentPadding` | spacing | Padding | `padding` on `.tab-content` |
| `contentTextAlign` | select | Text align | `text-align` on `.tab-content` |
| `contentColor` | color | Text color | `color` on `.tab-content` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.tab-content` |
| `contentBorder` | border | Border | `border` on `.tab-content` |

### Team-members

Section key: `team-members`

Theme style controls for the "team-members" section. Default CSS selector: .brxe-team-members

| Key | Type | Label | CSS |
|---|---|---|---|
| `memberGutter` | number | Gap | `gap` |
| `memberBorder` | border | Border | `border` on `.member` |
| `memberBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.member` |
| `memberTitleTypography` | typography | Title typography | `font` on `.title` |
| `memberSubtitleTypography` | typography | Subtitle typography | `font` on `.subtitle` |
| `memberDescriptionTypography` | typography | Description typography | `font` on `.description` |
| `imageBorder` | border | Image border | `border` on `.image` |
| `contentPadding` | spacing | Padding | `padding` on `.content` |
| `contentAlign` | select | Text align | `text-align` on `.content` |
| `contentBackgroundColor` | color | Background | `background-color` on `.member` |

### Testimonials

Section key: `testimonials`

Theme style controls for the "testimonials" section. Default CSS selector: .brxe-testimonials

| Key | Type | Label | CSS |
|---|---|---|---|
| `imageAlign` | select | Image align | `align-items` on `.repeater-item` |
| `imageSize` | number | Image size | `width` on `.image`, `height` on `.image` |
| `imageBorder` | border | Image border | `border` on `.image` |
| `typographyContent` | typography | Testimonial | `font` on `.testimonial-content-wrapper` |
| `typographyName` | typography | Name | `font` on `.testimonial-name` |
| `typographyTitle` | typography | Title | `font` on `.testimonial-title` |

### Text

Section key: `text`

Theme style controls for the "text" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typography` | typography | Typography | `font` on `.brxe-text`, `font` on `.brxe-text-basic` |

### Text-basic

Section key: `text-basic`

Theme style controls for the "text-basic" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | HTML tag | — |

### Typography

Section key: `typography`

Theme style controls for the "typography" section.

| Key | Type | Label | CSS |
|---|---|---|---|
| `typographyHtml` | number | HTML: font-size | `font-size` on `html` |
| `typographyBody` | typography | Body | `font` on `body` |
| `typographyHeadings` | typography | All headings | `font` on `h1, h2, h3, h4, h5, h6` |
| `typographyHeadingH1` | typography | Typography | `font` on `h1` |
| `h1Margin` | spacing | Margin | `margin` on `h1` |
| `typographyHeadingH2` | typography | Typography | `font` on `h2` |
| `h2Margin` | spacing | Margin | `margin` on `h2` |
| `typographyHeadingH3` | typography | Typography | `font` on `h3` |
| `h3Margin` | spacing | Margin | `margin` on `h3` |
| `typographyHeadingH4` | typography | Typography | `font` on `h4` |
| `h4Margin` | spacing | Margin | `margin` on `h4` |
| `typographyHeadingH5` | typography | Typography | `font` on `h5` |
| `h5Margin` | spacing | Margin | `margin` on `h5` |
| `typographyHeadingH6` | typography | Typography | `font` on `h6` |
| `h6Margin` | spacing | Margin | `margin` on `h6` |
| `typographyHero` | typography | Hero | `font` on `.bricks-type-hero` |
| `typographyLead` | typography | Lead | `font` on `.bricks-type-lead` |
| `focusOutline` | text | Focus outline | `outline` on `body.bricks-is-frontend :focus-visible`, `outline` on `@supports not selector(:focus-visible) { body.bricks-is-frontend :focus` |
| `blockquoteMargin` | spacing | Blockquote margin | `margin` on `blockquote` |
| `blockquotePadding` | spacing | Blockquote padding | `padding` on `blockquote` |
| `blockquoteBorder` | border | Blockquote border | `border` on `blockquote` |
| `blockquoteTypography` | typography | Blockquote typography | `font` on `blockquote` |

### Video

Section key: `video`

Theme style controls for the "video" section. Default CSS selector: .brxe-video

| Key | Type | Label | CSS |
|---|---|---|---|
| `previewImageFallback` | image | Fallback preview image | — |
| `boxShadow` | box-shadow | Box shadow | `box-shadow` |
| `overlay` | background | Overlay | `background` on `.bricks-video-overlay` |
| `overlayIcon` | icon | Icon | `—` on `.bricks-video-overlay-icon` |
| `overlayIconTypography` | typography | Icon typography | `font` on `.bricks-video-overlay-icon` |
| `customPlayer` | checkbox | Custom video player | — |
| `fileRestart` | checkbox | Restart | — |
| `fileRewind` | checkbox | Rewind | — |
| `fileFastForward` | checkbox | Fast forward | — |
| `fileSpeed` | checkbox | Speed | — |
| `filePip` | checkbox | Picture in picture | — |

### Wordpress

Section key: `wordpress`

Theme style controls for the "wordpress" section. Default CSS selector: .brxe-wordpress

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleBorder` | border | Widget title border | `border` on `.bricks-widget-title` |
| `titleTypography` | typography | Widget title typography | `font` on `.bricks-widget-title` |
| `contentTypography` | typography | Content typography | `font` on `ul` |
| `postsTitleTypography` | typography | Post title typography | `font` on `.post-title` |
| `postsMetaTypography` | typography | Post meta typography | `font` on `.post-meta` |

## Bricks 2.4.3 contextual spacing fields

Each `contextualSpacingCustomTarget` entry contains a `selector` and the spacing fields below. These fields use number controls with CSS units and variable support; they become available after a selector is set. The generated repeater schema leaves these nested entry fields generic.

| Entry key | CSS property |
|---|---|
| `marginStart` | `margin-block-start` |
| `marginEnd` | `margin-block-end` |
| `paddingStart` | `padding-inline-start` |
| `paddingEnd` | `padding-inline-end` |

---

# Page Settings Schema

Source: https://academy.bricksbuilder.io/developer/schema/settings/page/

*Schema for Bricks page settings controls*

## Controls

| Key | Type | Label |
|---|---|---|
| `bodyClasses` | text | CSS classes |
| `customCss` | code | Custom CSS |
| `customScriptsBodyFooter` | code | Body (footer) scripts |
| `customScriptsBodyHeader` | code | Body (header) scripts |
| `customScriptsHeader` | code | Header scripts |
| `disableLazyLoad` | checkbox | Disable lazy load |
| `documentTitle` | text | Document title |
| `footerDisabled` | checkbox | Disable footer |
| `headerDisabled` | checkbox | Disable header |
| `metaDescription` | textarea | Meta description |
| `metaKeywords` | text | Meta keywords |
| `metaRobots` | select | Meta robots |
| `onePageNavigation` | checkbox | Show navigation |
| `onePageNavigationItemBorder` | border | Border |
| `onePageNavigationItemBorderActive` | border | Border |
| `onePageNavigationItemBoxShadow` | box-shadow | Box shadow |
| `onePageNavigationItemBoxShadowActive` | box-shadow | Box shadow |
| `onePageNavigationItemColor` | color | Color |
| `onePageNavigationItemColorActive` | color | Color |
| `onePageNavigationItemHeight` | number | Height |
| `onePageNavigationItemHeightActive` | number | Height |
| `onePageNavigationItemSpacing` | number | Spacing |
| `onePageNavigationItemWidth` | number | Width |
| `onePageNavigationItemWidthActive` | number | Width |
| `popupDisabled` | checkbox | Disable popups |
| `postName` | text | Permalink |
| `postTitle` | text | Title |
| `scrollMargin` | number | Margin |
| `scrollPadding` | number | Padding |
| `scrollSnapAlign` | select | Align |
| `scrollSnapSelector` | text | Snapping elements selector |
| `scrollSnapStop` | select | Stop |
| `scrollSnapType` | select | Type |
| `sharingDescription` | text | Description |
| `sharingImage` | image | Image |
| `sharingTitle` | text | Title |

---

# Template Settings Schema

Source: https://academy.bricksbuilder.io/developer/schema/settings/template/

*Schema for Bricks template settings controls*

## Controls

| Key | Type | Label |
|---|---|---|
| `headerPosition` | select | Header location |
| `headerSticky` | checkbox | Sticky header |
| `headerStickyOnScroll` | checkbox | Sticky on scroll |
| `headerStickyScrollingBackground` | background | Scrolling background |
| `headerStickyScrollingBoxShadow` | box-shadow | Scrolling box shadow |
| `headerStickyScrollingColor` | color | Scrolling text color |
| `headerStickyScrollingColorHover` | color | Scrolling text color |
| `headerStickySlideUpAfter` | number | Slide up after |
| `headerStickyTransition` | text | Transition |
| `headerWidth` | number | Header width |
| `passwordProtectionBypassLoggedIn` | checkbox | Disable for logged-in users |
| `passwordProtectionEndDate` | datepicker | End date |
| `passwordProtectionPassword` | text | Password |
| `passwordProtectionSchedule` | checkbox | Schedule |
| `passwordProtectionSource` | select | Password source |
| `passwordProtectionStartDate` | datepicker | Start date |
| `popupAjax` | checkbox | Fetch content via AJAX |
| `popupAjaxLoaderAnimation` | select | Animation |
| `popupAjaxLoaderColor` | color | Color |
| `popupAjaxLoaderScale` | number | Scale |
| `popupAjaxLoaderSelector` | text | CSS selector |
| `popupAlignItems` | align-items | Align cross axis |
| `popupBackdropTransition` | text | Transition |
| `popupBackground` | background | Background |
| `popupBodyScroll` | checkbox | Scroll |
| `popupBreakpointMode` | select | popupBreakpointMode |
| `popupCloseOn` | select | Close on |
| `popupContentBackground` | background | Background |
| `popupContentBorder` | border | Border |
| `popupContentBoxShadow` | box-shadow | Box shadow |
| `popupContentHeight` | number | Height |
| `popupContentMaxHeight` | number | Max. height |
| `popupContentMaxWidth` | number | Max. width |
| `popupContentMinHeight` | number | Min. height |
| `popupContentMinWidth` | number | Min. width |
| `popupContentPadding` | spacing | Padding |
| `popupContentWidth` | number | Width |
| `popupDisableAutoFocus` | checkbox | Disable auto focus |
| `popupDisableAutoFocusOnClose` | checkbox | Disable auto focus on close |
| `popupDisableBackdrop` | checkbox | Disable backdrop |
| `popupInfoBoxWidth` | number | Width |
| `popupIsInfoBox` | checkbox | Info Box |
| `popupIsWoo` | checkbox | WooCommerce  |
| `popupJustifyConent` | justify-content | Align main axis |
| `popupLimitLocalStorage` | number | Across sessions |
| `popupLimitSessionStorage` | number | Per session |
| `popupLimitTimeStorage` | number | Show again after .. hours |
| `popupLimitWindow` | number | Per page load |
| `popupPadding` | spacing | Padding |
| `popupScrollToTop` | checkbox | Scroll to top |
| `popupShowAt` | select | popupShowAt |
| `popupShowOn` | select | popupShowOn |
| `popupZindex` | number | Z-index |
| `templateConditions` | repeater | Archive type |
| `templatePreviewAuthor` | select | Author |
| `templatePreviewPostId` | select | Single |
| `templatePreviewPostType` | select | Post type |
| `templatePreviewSearchTerm` | text | Search term |
| `templatePreviewTerm` | select | Term |
| `templatePreviewType` | select | Content type |
| `template_interactions` | repeater | Interactions |

---

# Accordion (Nestable) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/accordion-nested/

*Schema for Bricks Accordion (Nestable) element*

| Property | Value |
|---|---|
| `name` | accordion-nested |
| `category` | general |
| `tag` | div |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `expandItem` | text | Expand item indexes | — |
| `independentToggle` | checkbox | Independent toggle | — |
| `transition` | number | Transition | — |
| `faqSchema` | checkbox | FAQ schema | — |
| `titleHeight` | number | Min. height | `min-height` on `.accordion-title-wrapper` |
| `titleMargin` | spacing | Margin | `margin` on `.accordion-title-wrapper` |
| `titlePadding` | spacing | Padding | `padding` on `.accordion-title-wrapper` |
| `titleBackgroundColor` | color | Background color | `background-color` on `.accordion-title-wrapper` |
| `titleBorder` | border | Border | `border` on `.accordion-title-wrapper` |
| `titleTypography` | typography | Typography | `font` on `.accordion-title-wrapper`, `font` on `.accordion-title-wrapper .brxe-heading` |
| `titleActiveBackgroundColor` | color | Background color | `background-color` on `.brx-open .accordion-title-wrapper` |
| `titleActiveBorder` | border | Border | `border` on `.brx-open .accordion-title-wrapper` |
| `titleActiveTypography` | typography | Typography | `font` on `.brx-open .accordion-title-wrapper`, `font` on `.brx-open .accordion-title-wrapper .brxe-heading` |
| `contentMargin` | spacing | Margin | `margin` on `.accordion-content-wrapper` |
| `contentPadding` | spacing | Padding | `padding` on `.accordion-content-wrapper` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.accordion-content-wrapper` |
| `contentBorder` | border | Border | `border` on `.accordion-content-wrapper` |
| `contentTypography` | typography | Typography | `font` on `.accordion-content-wrapper` |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_content` | text | Content | `content` |
| `_margin` | spacing | Margin | `margin` |
| `_padding` | spacing | Padding | `padding` |
| `_width` | number | Width | `width` |
| `_widthMin` | number | Min. width | `min-width` |
| `_widthMax` | number | Max. width | `max-width` |
| `_height` | number | Height | `height` |
| `_heightMin` | number | Min. height | `min-height` |
| `_heightMax` | number | Max. height | `max-height` |
| `_aspectRatio` | text | Aspect ratio | `aspect-ratio` |
| `_position` | select | Position | `position` |
| `_top` | number | _top | `top` |
| `_right` | number | Right | `right` |
| `_bottom` | number | Bottom | `bottom` |
| `_left` | number | Left | `left` |
| `_zIndex` | number | Z-index | `z-index` |
| `_order` | number | _order | `order` |
| `_display` | select | Display | `display`, `align-items` |
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_gap` | number | Gap | `gap` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_useMasonry` | checkbox | %s layout | — |
| `_masonryColumn` | number | Columns | `--columns` |
| `_masonryGutter` | number | Spacing | `--gutter` |
| `_masonryHorizontalOrder` | checkbox | Horizontal order | — |
| `_masonryTransitionDuration` | number | Transition | — |
| `_masonryTransitionMode` | select | Reveal animation | — |
| `_typography` | typography | _typography | `font` |
| `_background` | background | _background | `background` |
| `_shapeDividers` | repeater | Custom shape | — |
| `_gradient` | gradient | _gradient | `background-image` |
| `_border` | border | Border | `border` |
| `_boxShadow` | box-shadow | Box shadow | `box-shadow` |
| `_transform` | transform | Transform | `transform` |
| `_transformOrigin` | text | Transform origin | `transform-origin` |
| `_motionElementParallax` | checkbox | Element parallax | — |
| `_motionElementParallaxSpeedX` | number | Horizontal speed | `--brx-motion-parallax-speed-x` |
| `_motionElementParallaxSpeedY` | number | Vertical speed | `--brx-motion-parallax-speed-y` |
| `_motionBackgroundParallax` | checkbox | Background parallax | — |
| `_motionBackgroundParallaxSpeed` | number | Background speed | `--brx-motion-background-speed` |
| `_motionStartVisiblePercent` | number | Parallax start point | — |
| `_cssCustom` | code | Custom CSS | — |
| `_cssClasses` | text | CSS classes | — |
| `_cssId` | text | CSS ID | — |
| `_cssFilters` | filters | CSS Filters | `filter` |
| `_cssTransition` | text | Transition | `transition` |
| `_attributes` | repeater | Name | — |
| `_scrollSnapType` | select | Type | `scroll-snap-type` on `html`, `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapAlign` | select | Align | `scroll-snap-align` on `.brxe-section` |
| `_scrollSnapStop` | select | Stop | `scroll-snap-stop` on `.brxe-section` |
