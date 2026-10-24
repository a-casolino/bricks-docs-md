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

# Align Items Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/align-items/

*Value schema for align-items control type*

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

# Dimensions Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/dimensions/

*Unknown control type: dimensions*

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

# Direction Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/direction/

*Value schema for direction control type*

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

# Number Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/number/

*Value schema for number control type*

---

# Query List Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/query-list/

*Unknown control type: query-list*

---

# Justify Content Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/justify-content/

*Value schema for justify-content control type*

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

# Text Align Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text-align/

*Value schema for text-align control type*

---

# Text Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text/

*Value schema for text control type*

---

# Text Shadow Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text-shadow/

*Value schema for text-shadow control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `values` | array | — |

---

# Textarea Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/textarea/

*Value schema for textarea control type*

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

---

# Accordion Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/accordion/

*Schema for Bricks Accordion element*

| Property | Value |
|---|---|
| `name` | accordion |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `accordions` | repeater | Title | — |
| `expandItem` | text | Expand item indexes | — |
| `independentToggle` | checkbox | Independent toggle | — |
| `transition` | number | Transition | — |
| `faqSchema` | checkbox | FAQ schema | — |
| `titleTag` | select | HTML tag | — |
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Icon typography | `font` on `.accordion-title\{pseudo\} .icon` |
| `iconExpanded` | icon | Icon expanded | — |
| `iconExpandedTypography` | typography | Icon expanded typography | `font` on `.accordion-title\{pseudo\} .icon.expanded` |
| `iconPosition` | select | Icon position | — |
| `iconRotate` | number | Icon rotate in ° | `transform:rotate` on `.brx-open .title + .icon` |
| `titleMargin` | spacing | Margin | `margin` on `.accordion-title-wrapper` |
| `titlePadding` | spacing | Padding | `padding` on `.accordion-title-wrapper` |
| `titleTypography` | typography | Title typography | `font` on `.accordion-title\{pseudo\} .title` |
| `subtitleTypography` | typography | Subtitle typography | `font` on `.accordion-subtitle` |
| `titleBackgroundColor` | color | Background color | `background-color` on `.accordion-title-wrapper` |
| `titleBorder` | border | Border | `border` on `.accordion-title-wrapper` |
| `titleActiveBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.accordion-title-wrapper` |
| `titleActiveTypography` | typography | Active typography | `font` on `.brx-open .title` |
| `titleActiveBackgroundColor` | color | Active background | `background-color` on `.brx-open .accordion-title-wrapper` |
| `titleActiveBorder` | border | Active border | `border` on `.brx-open .accordion-title-wrapper` |
| `contentMargin` | spacing | Margin | `margin` on `.accordion-content-wrapper` |
| `contentPadding` | spacing | Padding | `padding` on `.accordion-content-wrapper` |
| `contentTypography` | typography | Content typography | `font` on `.accordion-content-wrapper` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.accordion-content-wrapper` |
| `contentBorder` | border | Border | `border` on `.accordion-content-wrapper` |

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

---

# Alert Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/alert/

*Schema for Bricks Alert element*

| Property | Value |
|---|---|
| `name` | alert |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `content` | editor | content | — |
| `type` | select | Type | — |
| `dismissable` | checkbox | Dismissable | — |

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

---

# Anim. Typing Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/animated-typing/

*Schema for Bricks Anim. Typing element*

| Property | Value |
|---|---|
| `name` | animated-typing |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | Tag | — |
| `prefix` | text | Prefix | — |
| `suffix` | text | Suffix | — |
| `strings` | repeater | Strings | — |
| `typeSpeed` | number | Type speed in ms | — |
| `backSpeed` | number | Back speed in ms | — |
| `startDelay` | number | Start delay in ms | — |
| `backDelay` | number | Back delay in ms | — |
| `cursorChar` | text | Cursor character | — |
| `loop` | checkbox | Loop | — |
| `shuffle` | checkbox | Shuffle | — |

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

---

# Audio Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/audio/

*Schema for Bricks Audio element*

| Property | Value |
|---|---|
| `name` | audio |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `source` | select | Source | — |
| `file` | audio | File | — |
| `external` | text | external | — |
| `useDynamicData` | text | useDynamicData | — |
| `titleCustom` | text | Custom title | — |
| `artist` | checkbox | Show artist | — |
| `title` | checkbox | Show title | — |
| `autoplay` | checkbox | Autoplay | — |
| `loop` | checkbox | Loop | — |
| `tag` | select | Tag | — |
| `preload` | select | Preload | — |
| `theme` | select | Theme | — |

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

---

# Back To Top Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/back-to-top/

*Schema for Bricks Back to Top element*

| Property | Value |
|---|---|
| `name` | back-to-top |
| `category` | general |
| `tag` | button |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | text | HTML tag | — |
| `ariaLabel` | text | aria-label | — |
| `position` | select | Position | `position` |
| `positionTop` | number | positionTop | `top` |
| `positionRight` | number | Right | `right` |
| `positionBottom` | number | Bottom | `bottom` |
| `positionLeft` | number | Left | `left` |
| `visibleAfter` | number | Visible after | — |
| `visibleOnScrollUp` | checkbox | Visible on scroll up | — |
| `smoothScroll` | checkbox | Smooth scroll | — |
| `moveFocusToTop` | checkbox | Move focus to top | — |

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

---

# Block Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/block/

*Schema for Bricks Block element*

| Property | Value |
|---|---|
| `name` | block |
| `category` | layout |
| `tag` | div |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `link` | link | Link | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_gridItemColumnSpan` | text | Grid column | `grid-column` |
| `_gridItemRowSpan` | text | Grid row | `grid-row` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_display` | select | Display | `display`, `align-items` |
| `_gridGap` | number | Gap | `gap` |
| `_columnGap` | number | Column gap | `column-gap` |
| `_rowGap` | number | Row gap | `row-gap` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` |
| `_alignItemsGrid` | align-items | Align items | `align-items` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` |
| `_alignContentGrid` | align-items | Align content | `align-content` |
| `_flexWrap` | select | Flex wrap | `flex-wrap` |
| `_direction` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_order` | number | _order | `order` |
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
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_gap` | number | Gap | `gap` |
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

---

# Breadcrumbs Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/breadcrumbs/

*Schema for Bricks Breadcrumbs element*

| Property | Value |
|---|---|
| `name` | breadcrumbs |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `gap` | number | Gap | `gap` |
| `singularStructure` | repeater | Post types | — |
| `showDateContext` | checkbox | Add context | — |
| `homeURL` | text | URL | — |
| `homeLabel` | text | Text | — |
| `homeIcon` | icon | Icon | — |
| `hideIconGap` | number | Icon | `gap` on `.item:has(> svg), .item:has(> i)` |
| `homeIconPosition` | select | Icon | — |
| `hideHomeLabel` | checkbox | Hide label | — |
| `separatorType` | select | Separator | — |
| `separatorText` | text | Separator | — |
| `separatorIcon` | icon | Icon | — |
| `separatorColor` | color | Color | `color` on `.separator` |
| `separatorSize` | number | Size | `font-size` on `.separator` |
| `itemPadding` | spacing | Padding | `padding` on `.item` |
| `itemBackgroundColor` | color | Background color | `background-color` on `.item` |
| `itemBorder` | border | Border | `border` on `.item` |
| `itemTypography` | typography | Typography | `font` on `.item` |
| `currentItemPadding` | spacing | Padding | `padding` on `.item[aria-current="page"]` |
| `currentItemBackgroundColor` | color | Background color | `background-color` on `.item[aria-current="page"]` |
| `currentItemBorder` | border | Border | `border` on `.item[aria-current="page"]` |
| `currentItemTypography` | typography | Typography | `font` on `.item[aria-current="page"]` |

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

---

# Button Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/button/

*Schema for Bricks Button element*

| Property | Value |
|---|---|
| `name` | button |
| `category` | basic |
| `tag` | span |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `text` | text | text | — |
| `tag` | text | HTML tag | — |
| `size` | select | Size | — |
| `style` | select | Style | — |
| `circle` | checkbox | Circle | — |
| `outline` | checkbox | Outline | — |
| `link` | link | Link type | — |
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Typography | `font` on `i` |
| `iconPosition` | select | Position | — |
| `iconGap` | number | Gap | `gap` |
| `iconSpace` | checkbox | Space between | `justify-content` |

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

---

# Carousel Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/carousel/

*Schema for Bricks Carousel element*

| Property | Value |
|---|---|
| `name` | carousel |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `type` | select | Type | — |
| `items` | image-gallery | Images | — |
| `query` | query | Query | — |
| `alignItems` | align-items | Align items | `align-items` on `.swiper-wrapper` |
| `imageDisable` | checkbox | Hide image | — |
| `imageSize` | select | Image size | — |
| `imageLightbox` | checkbox | Link to lightbox | — |
| `imageLightboxSize` | select | Image size | — |
| `lightboxImageClick` | select | Image click action | — |
| `lightboxAnimationType` | select | Animation | — |
| `lightboxCaption` | checkbox | Caption | — |
| `lightboxThumbnails` | checkbox | Thumbnail navigation | — |
| `lightboxThumbnailSize` | number | Thumbnail size | — |
| `lightboxPadding` | dimensions | Padding | — |

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

---

# Code Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/code/

*Schema for Bricks Code element*

| Property | Value |
|---|---|
| `name` | code |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `executeCode` | checkbox | Execute code | — |
| `parseDynamicData` | checkbox | Parse dynamic data | — |
| `supressPhpErrors` | checkbox | Suppress PHP errors | — |
| `noRoot` | checkbox | Render without wrapper | — |
| `code` | code | code | — |
| `cssCode` | code | cssCode | — |
| `javascriptCode` | code | javascriptCode | — |
| `prettify` | select | Theme | — |

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

---

# Container Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/container/

*Schema for Bricks Container element*

| Property | Value |
|---|---|
| `name` | container |
| `category` | layout |
| `tag` | div |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `link` | link | Link | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_gridItemColumnSpan` | text | Grid column | `grid-column` |
| `_gridItemRowSpan` | text | Grid row | `grid-row` |
| `_gridItemJustifySelf` | align-items | Justify self | `justify-self` |
| `_display` | select | Display | `display`, `align-items` |
| `_gridGap` | number | Gap | `gap` |
| `_columnGap` | number | Column gap | `column-gap` |
| `_rowGap` | number | Row gap | `row-gap` |
| `_gridTemplateColumns` | text | Grid template columns | `grid-template-columns` |
| `_gridTemplateRows` | text | Grid template rows | `grid-template-rows` |
| `_gridAutoColumns` | text | Grid auto columns | `grid-auto-columns` |
| `_gridAutoRows` | text | Grid auto rows | `grid-auto-rows` |
| `_gridAutoFlow` | select | Grid auto flow | `grid-auto-flow` |
| `_justifyItemsGrid` | justify-content | Justify items | `justify-items` |
| `_alignItemsGrid` | align-items | Align items | `align-items` |
| `_justifyContentGrid` | justify-content | Justify content | `justify-content` |
| `_alignContentGrid` | align-items | Align content | `align-content` |
| `_flexWrap` | select | Flex wrap | `flex-wrap` |
| `_direction` | direction | Direction | `flex-direction` |
| `_alignSelf` | align-items | Align self | `align-self` |
| `_justifyContent` | justify-content | Align main axis | `justify-content` |
| `_alignItems` | align-items | Align cross axis | `align-items` |
| `_flexGrow` | number | Flex grow | `flex-grow` |
| `_flexShrink` | number | Flex shrink | `flex-shrink` |
| `_flexBasis` | text | Flex basis | `flex-basis` |
| `_order` | number | _order | `order` |
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
| `_visibility` | select | Visibility | `visibility` |
| `_overflow` | text | Overflow | `overflow` |
| `_opacity` | number | Opacity | `opacity` |
| `_cursor` | select | Cursor | `cursor` |
| `_isolation` | select | Isolation | `isolation` |
| `_mixBlendMode` | select | Mix blend mode | `mix-blend-mode` |
| `_pointerEvents` | text | Pointer events | `pointer-events` |
| `_perspective` | number | Perspective | `perspective` |
| `_perspectiveOrigin` | text | Perspective origin | `perspective-origin` |
| `_flexDirection` | direction | Direction | `flex-direction` |
| `_gap` | number | Gap | `gap` |
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

---

# Countdown Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/countdown/

*Schema for Bricks Countdown element*

| Property | Value |
|---|---|
| `name` | countdown |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `date` | datepicker | Date | — |
| `timezone` | select | Time zone | — |
| `action` | select | Date Reached | — |
| `actionText` | text | Date Reached | — |
| `fields` | repeater | Prefix | — |
| `flexDirectionFields` | direction | Direction | `flex-direction` |
| `justifyContent` | justify-content | Align main axis | `justify-content` |
| `alignItems` | align-items | Align cross axis | `align-items` |
| `flexDirection` | direction | Direction | `flex-direction` on `.field` |
| `gutter` | spacing | Margin | `margin` on `.field` |
| `typography` | typography | Typography | `font` |
| `typographyPrefix` | typography | Typography | `font` on `.prefix` |
| `typographySuffix` | typography | Typography | `font` on `.suffix` |

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

---

# Counter Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/counter/

*Schema for Bricks Counter element*

| Property | Value |
|---|---|
| `name` | counter |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `countFrom` | text | Count from | — |
| `countTo` | text | Count to | — |
| `duration` | number | Animation in ms | — |
| `countTypography` | typography | Typography | `font` on `.count` |
| `prefix` | text | Prefix | — |
| `prefixTypography` | typography | Typography | `font` on `.prefix` |
| `suffix` | text | Suffix | — |
| `suffixTypography` | typography | Typography | `font` on `.suffix` |
| `thousandSeparator` | checkbox | Thousand separator | — |
| `separatorText` | text | Separator | — |

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
