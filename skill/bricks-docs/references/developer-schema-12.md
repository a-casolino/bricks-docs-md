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

# Element Conditions Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/common/conditions/

*Full schema for element display conditions: condition keys, comparison operators, and the OR-of-AND data structure.*

Element display conditions control whether an element renders on the frontend. They are stored in the `_conditions` key inside any element's `settings` object.

## Data structure

Conditions use an OR-of-AND structure: the outer array contains OR groups, and each inner array contains AND items. The element renders if **any** OR group evaluates to true, and an OR group is true when **all** its AND items are true.

## `conditionItem` properties

Each condition item has the following properties:

| Property | Type | Required | Description |
|---|---|---|---|
| `id` | string \| integer | Yes | Unique identifier for this condition |
| `key` | string | Yes | Condition type (see enum below) |
| `compare` | string | Yes | Comparison operator (see table below) |
| `value` | any | Conditional | The value to compare against. Not needed when compare is `empty` or `empty_not`. |
| `dynamic_data` | string | No | Dynamic data tag to use as the value source |

### Example

```json
{
  "_conditions": [
    [
      { "id": "abc123", "key": "user_logged_in", "compare": "==", "value": true },
      { "id": "def456", "key": "user_role", "compare": "==", "value": "administrator" }
    ],
    [
      { "id": "ghi789", "key": "dynamic_data", "compare": "contains", "value": "sale", "dynamic_data": "{post_title}" }
    ]
  ]
}
```

This reads as: show the element if (user is logged in AND is an administrator) OR (the post title contains "sale").

## Condition keys

**General**
- `browser`
- `current_url`
- `date`
- `datetime`
- `dynamic_data`
- `featured_image`
- `operating_system`
- `referer`
- `time`
- `weekday`

**Post**
- `post_author`
- `post_date`
- `post_id`
- `post_parent`
- `post_status`
- `post_title`

**User**
- `user_id`
- `user_logged_in`
- `user_registered`
- `user_role`

**WooCommerce**
- `woo_checkout_login_step_needed`
- `woo_checkout_needs_shipping`
- `woo_checkout_needs_shipping_address`
- `woo_order_has_downloads`
- `woo_order_has_status`
- `woo_order_needs_shipping_address`
- `woo_order_withdrawal_screen`
- `woo_product_category`
- `woo_product_featured`
- `woo_product_new`
- `woo_product_purchased_by_user`
- `woo_product_rating`
- `woo_product_sale`
- `woo_product_sold_individually`
- `woo_product_stock_management`
- `woo_product_stock_quantity`
- `woo_product_stock_status`
- `woo_product_tag`
- `woo_product_type`

Available compare operators vary by condition key. For example, `post_id` supports math operators (`==`, `!=`, `>=`, `<=`, `>`, `<`), while `user_logged_in` only supports `==` and `!=`.

## Comparison operators

| Operator | Description |
|---|---|
| `==` | Equal (loose comparison, supports arrays via intersection) |
| `!=` | Not equal (loose comparison) |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `>` | Greater than |
| `<` | Less than |
| `contains` | String contains substring |
| `contains_not` | String does not contain substring |
| `empty` | Value is empty (no value field needed) |
| `empty_not` | Value is not empty (no value field needed) |

## Extensibility

Condition keys and comparison operators are filterable via PHP hooks:

- `bricks/conditions/groups`: add custom condition groups
- `bricks/conditions/options`: add custom condition keys with their own compare operators
- `bricks/conditions/result`: modify the boolean result of any individual condition evaluation

Third-party plugins can introduce additional condition keys beyond those listed above.

---

# Element Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/common/element/

*Canonical reference for a Bricks element: the envelope structure, settings layers, meta-settings, and selectors.*

Every element in Bricks uses the same envelope structure, regardless of type. Element-specific controls are documented in each [individual element schema](../../elements/accordion/); content areas (the flat arrays that hold elements) are documented in the [content area schema](../../general/content-area/).

## Element envelope

Every element object has these top-level fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique 6-character alphanumeric identifier (e.g. `"dlceeu"`) |
| `name` | string | Yes | Element type, matches the element schema filename (e.g. `"button"`, `"heading"`) |
| `parent` | string \| 0 | Yes | Parent element ID, or `0` for root-level elements |
| `children` | string[] | Yes | Ordered array of child element IDs |
| `settings` | object | Yes | All control values for this element (element-specific + inherited + meta) |
| `selectors` | array | No | Custom CSS selectors with scoped settings (since Bricks 2.0) |
| `label` | string | No | Custom label assigned by the user in the builder |
| `themeStyles` | array | No | Theme style overrides applied to this element |

## Settings: three layers

The `settings` object combines three layers of keys:

1. **Element-specific controls:** unique to each element type (e.g. `text`, `tag`, `link` on a button). Documented in each element's schema.
2. **Inherited CSS controls:** shared by all elements, prefixed with `_` (e.g. `_typography`, `_margin`, `_padding`, `_background`). These support responsive and pseudo-class variants via colon suffixes (e.g. `_typography:tablet_portrait:hover`). Documented in each element's schema under the `_`-prefixed keys.
3. **Meta-settings:** shared by all elements but not listed in individual element schemas. These control visibility, behavior, and class assignment. Documented below.

## Meta-settings

These keys can appear in any element's `settings` object. They are not included in per-element schemas to avoid duplication across 182+ elements.

### `_cssGlobalClasses`

Array of global class IDs applied to this element. Each ID references a global class defined in the [global classes](../../global/global-classes/) data.

```json
"_cssGlobalClasses": ["mmdqed", "xkatss"]
```

### `_conditions`

Element display conditions that control whether this element renders. Structured as an array of arrays: outer array is OR groups, inner arrays are AND items.

```json
"_conditions": [
  [
    { "id": "abc123", "key": "user_logged_in", "compare": "==", "value": true }
  ]
]
```

See the [Element Conditions](./conditions/) page for the full `conditionItem` schema, all 32 condition keys, and available comparison operators.

### `_interactions`

Array of interaction rules that trigger actions in response to events (click, scroll, hover, etc.). Each interaction specifies a trigger, action, and target.

```json
"_interactions": [
  {
    "id": "abc123",
    "trigger": "click",
    "action": "startAnimation",
    "target": "self"
  }
]
```

See the [Element Interactions](./interactions/) page for the full `interactionItem` schema, all triggers, actions, and sub-conditions.

### `_hideElementBuilder`

Boolean (default `false`). When `true`, the element is hidden on the builder canvas but still renders on the frontend.

### `_hideElementFrontend`

Boolean (default `false`). When `true`, the element is hidden on the frontend but remains visible in the builder.

### `_attributes`

Array of custom HTML attributes added to the element's root DOM node.

```json
"_attributes": [
  { "id": "abc123", "name": "data-aos", "value": "fade-up" }
]
```

## Selectors

The `selectors` array allows scoping control settings to arbitrary CSS selectors on an element (since Bricks 2.0). Each selector entry has its own `settings` object that follows the same structure as the element's main settings.

```json
"selectors": [
  {
    "id": "nopzhs",
    "selector": "#brxe-opxcoa h3",
    "settings": {
      "_typography": { "color": { "raw": "blue" } }
    },
    "label": "Heading within container"
  }
]
```

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Unique identifier for this selector entry |
| `selector` | string | Yes | CSS selector string (e.g. `".my-class"`, `"&::before"`, `"& > span"`) |
| `settings` | object | Yes | Control settings scoped to this selector |
| `label` | string | No | Display label in the builder UI |

### Selector item schema

```json
{
  "type": "object",
  "description": "Custom CSS selector on an element or global class (since Bricks 2.0). Allows scoping control settings to arbitrary CSS selectors.",
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for this selector entry"
    },
    "selector": {
      "type": "string",
      "description": "CSS selector string (e.g. \".my-class\", \"&::before\", \"& > span\")"
    },
    "settings": {
      "description": "Control settings scoped to this selector (same shape as element settings)",
      "_note": "Dynamic map of all settings for this element or class. Keys are element-specific control names (e.g. `text`, `style`) or inherited CSS setting keys, optionally suffixed with a breakpoint and/or pseudo-class using colon syntax (e.g. `_typography:tablet_portrait:hover`). See the individual element schemas for available control keys."
    },
    "label": {
      "type": "string",
      "description": "Optional display label for this selector in the builder UI"
    }
  },
  "required": [
    "id",
    "selector",
    "settings"
  ],
  "additionalProperties": false
}
```

## How this relates to individual element schemas

Each element schema (e.g. [button](../../elements/button/), [heading](../../elements/heading/)) documents the element-specific and inherited CSS controls that go into the `settings` object. The envelope fields (`id`, `name`, `parent`, `children`, `selectors`, `label`, `themeStyles`) and meta-settings (`_cssGlobalClasses`, `_conditions`, `_interactions`, etc.) documented on this page apply identically to every element type.

To construct a complete element, combine:
1. The envelope fields from this page
2. Element-specific controls from the individual element schema
3. Inherited CSS controls (the `_`-prefixed keys in the element schema)
4. Any applicable meta-settings from this page

---

# Element Interactions Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/common/interactions/

*Full schema for element interactions: triggers, actions, targets, animation settings, and sub-conditions.*

Element interactions define event-driven behavior: when a trigger fires, an action is executed on a target. They are stored in the `_interactions` key inside any element's `settings` object.

## Data structure

Interactions are a flat array of interaction items. Each item specifies a trigger event, the action to perform, and a target element or selector.

## `interactionItem` core properties

| Property | Type | Description |
|---|---|---|
| `id` | string \| integer | Unique identifier for this interaction |
| `trigger` | string | Event that fires this interaction (see triggers below) |
| `action` | string | Action to perform (see actions below) |
| `target` | string | Target reference (`"self"`, element ID, or selector context) |
| `targetSelector` | string | CSS selector for the target element |
| `delay` | string | Delay before executing the action (ms) |
| `runOnce` | boolean | If true, the interaction fires only once |

## Additional properties

These properties apply depending on the chosen action:

| Property | Type | Used with |
|---|---|---|
| `animationType` | string | `startAnimation` (animation type) |
| `animationId` | string | `startAnimation` (predefined animation ID) |
| `animationDelay` | string | `startAnimation` (animation delay) |
| `animationDuration` | string | `startAnimation` (animation duration) |
| `jsFunction` | string | `javascript` (function name to call) |
| `jsFunctionArgs` | array | `javascript` (arguments array: `[{ jsFunctionArg: "value" }]`) |
| `scrollToDelay` | string | `scrollTo` (delay before scrolling) |
| `scrollToOffset` | string | `scrollTo` (scroll offset in pixels) |
| `scrollOffset` | string | `scroll` trigger (scroll position threshold) |
| `rootMargin` | string | `enterView`/`leaveView` (IntersectionObserver root margin) |
| `templateId` | string | Template ID reference |
| `formId` | string | Form element ID |
| `ajaxQueryId` | string | AJAX query element ID |
| `offCanvasSelector` | string | `toggleOffCanvas` (offcanvas CSS selector) |
| `toggleOffCanvasInfo` | string | `toggleOffCanvas` (info field) |
| `filterElementId` | string | Query filter element ID |
| `infoBoxId` | string | Info box element ID |
| `loadMoreQuery` | string | `loadMore` (query element ID) |
| `targetFormSelector` | string | `clearForm` (form CSS selector) |
| `actionAttributeKey` | string | `setAttribute`/`removeAttribute`/`toggleAttribute` (attribute name) |
| `actionAttributeValue` | string | `setAttribute`/`toggleAttribute` (attribute value) |
| `disablePreventDefault` | boolean | Do not call `preventDefault()` on the trigger event |
| `storageType` | string | `storageAdd`/`storageRemove`/`storageCount` (storage type) |
| `popupContextId` | string | Popup context ID |
| `popupContextType` | string | Popup context type |
| `conditionsSep` | string | Visual separator for conditions UI |

### Example

```json
{
  "_interactions": [
    {
      "id": "abc123",
      "trigger": "click",
      "action": "startAnimation",
      "target": "self",
      "animationType": "fadeIn",
      "animationDuration": "500"
    },
    {
      "id": "def456",
      "trigger": "enterView",
      "action": "show",
      "target": "self",
      "rootMargin": "0px 0px -100px 0px",
      "runOnce": true
    }
  ]
}
```

## Triggers

**Element**
- `click`
- `mouseover`
- `focus`
- `blur`
- `mouseenter`
- `mouseleave`
- `enterView`
- `leaveView`
- `animationEnd`
- `ajaxStart`
- `ajaxEnd`
- `formSubmit`
- `formSuccess`
- `formError`

**Browser / Window**
- `scroll`
- `contentLoaded`
- `mouseleaveWindow`

**Query filters**
- `filterOptionEmpty`
- `filterOptionNotEmpty`

**WooCommerce**
- `wooAddedToCart`
- `wooAddingToCart`
- `wooRemovedFromCart`
- `wooUpdateCart`
- `wooCouponApplied`
- `wooCouponRemoved`

Popup templates have two additional triggers (`showPopup`, `hidePopup`) available via the `templateInteractionItem` variant in template settings.

## Actions

| Action | Description |
|---|---|
| `show` | Show element |
| `hide` | Hide element |
| `click` | Click element |
| `setAttribute` | Set an HTML attribute |
| `removeAttribute` | Remove an HTML attribute |
| `toggleAttribute` | Toggle an HTML attribute |
| `toggleOffCanvas` | Toggle an offcanvas panel |
| `loadMore` | Load more items (query loop) |
| `loadMoreGallery` | loadMoreGallery |
| `startAnimation` | Start a CSS animation |
| `scrollTo` | Scroll to an element |
| `javascript` | Execute a custom JavaScript function |
| `openAddress` | Open a map address |
| `closeAddress` | Close a map address |
| `clearForm` | Clear a form |
| `storageAdd` | Add item to browser storage |
| `storageRemove` | Remove item from browser storage |
| `storageCount` | Count items in browser storage |

## Interaction sub-conditions

Each interaction can optionally include sub-conditions that must be met before the action fires. These are stored in the `interactionConditions` array, with `interactionConditionsRelation` controlling whether conditions are combined with AND or OR logic.

| Property | Type | Description |
|---|---|---|
| `interactionConditions` | array | Array of `interactionConditionItem` objects |
| `interactionConditionsRelation` | string | `"and"` or `"or"` (default: `"and"`) |

### `interactionConditionItem` properties

| Property | Type | Description |
|---|---|---|
| `conditionType` | string | Type of condition check |
| `storageCompare` | string | Comparison operator for storage value |
| `storageCompareValue` | any | Value to compare storage against |
| `storageKey` | any | Browser storage key to check |
| `id` | string,integer | id |

### Example with sub-conditions

```json
{
  "id": "abc123",
  "trigger": "click",
  "action": "show",
  "target": "self",
  "interactionConditions": [
    {
      "conditionType": "storage",
      "storageKey": "user_preference",
      "storageCompare": "==",
      "storageCompareValue": "dark"
    }
  ],
  "interactionConditionsRelation": "and"
}
```
