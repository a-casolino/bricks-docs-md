# Nav (Nestable) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/nav-nested/

*Schema for Bricks Nav (Nestable) element*

| Property | Value |
|---|---|
| `name` | nav-nested |
| `category` | general |
| `tag` | nav |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | text | HTML tag | — |
| `ariaLabel` | text | aria-label | — |
| `gap` | number | Gap | `gap` on `:where(.brx-nav-nested-items)` |
| `itemPadding` | spacing | Padding | `padding` on `:where(.brx-nav-nested-items > li > a)`, `padding` on `:where(.brx-nav-nested-items > li > .brxe-text-link:not(a))`, `padding` on `:where(.brx-nav-nested-items > li > .brxe-icon)`, `padding` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `padding` on `:where(.brx-nav-nested-items > li > .brx-submenu-toggle > *)`, `padding` on `&.brx-open :where(.brx-nav-nested-items > li > button.brx-toggle-div)` |
| `itemBackgroundColor` | color | Background color | `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\} > a)`, `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-text-link:not(a))`, `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-icon)`, `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle)` |
| `itemBorder` | border | Border | `border` on `:where(.brx-nav-nested-items > li\{pseudo\} > a)`, `border` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-text-link:not(a))`, `border` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-icon)`, `border` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `border` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle)` |
| `itemTypography` | typography | Typography | `font` on `:where(.brx-nav-nested-items > li\{pseudo\} > a)`, `font` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-text-link:not(a))`, `font` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-icon)`, `font` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `font` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle > *)` |
| `itemTransform` | transform | Transform | `transform` on `:where(.brx-nav-nested-items > li\{pseudo\} > a)`, `transform` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-text-link:not(a))`, `transform` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-icon)`, `transform` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `transform` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle)` |
| `itemTransition` | text | Transition | `transition` on `:where(.brx-nav-nested-items > li)`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\} > a)`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-text-link:not(a))`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brxe-icon)`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\}:has( > .brxe-svg))`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle)`, `transition` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle > *)` |
| `itemBackgroundColorActive` | color | Background color | `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\}) > [aria-current="page"]`, `background-color` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle).aria-current` |
| `itemBorderActive` | border | Border | `border` on `:where(.brx-nav-nested-items > li\{pseudo\}) > [aria-current="page"]`, `border` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle).aria-current` |
| `itemTypographyActive` | typography | Typography | `font` on `:where(.brx-nav-nested-items > li\{pseudo\}) > [aria-current="page"]`, `font` on `:where(.brx-nav-nested-items > li\{pseudo\} > .brx-submenu-toggle).aria-current > *` |
| `topLevelDropdownTextPadding` | spacing | Text padding | `padding` on `:where(.brx-nav-nested-items > li) > .brx-submenu-toggle > span` |
| `topLevelDropdownIconPadding` | spacing | Icon padding | `padding` on `:where(.brx-nav-nested-items > li) > .brx-submenu-toggle button` |
| `topLevelGap` | number | Gap | `gap` on `:where(.brx-nav-nested-items > li) > .brx-submenu-toggle` |
| `dropdownTextPadding` | spacing | Text padding | `padding` on `:where(.brx-submenu-toggle) span` |
| `iconPadding` | spacing | Icon padding | `padding` on `:where(.brx-submenu-toggle) button` |
| `iconGap` | number | Gap | `gap` on `:where(.brx-submenu-toggle)` |
| `iconPosition` | select | Icon position | `flex-direction` on `:where(.brx-submenu-toggle)`, `flex-direction` on `:where(.brx-submenu-toggle)` |
| `iconSize` | number | Icon size | `font-size` on `:where(.brx-submenu-toggle) button` |
| `iconColor` | color | Icon color | `color` on `:where(.brx-submenu-toggle) button` |
| `iconTransform` | transform | Icon transform | `transform` on `:where(.brx-submenu-toggle button > *)` |
| `iconTransformOpen` | transform | Icon transform | `transform` on `:where(.brx-submenu-toggle button)[aria-expanded="true"] > *` |
| `iconTransition` | text | Icon transition | `transition` on `:where(.brx-submenu-toggle button)[aria-expanded] > *` |
| `dropdownContentWidth` | number | Min. width | `min-width` on `:where(.brx-dropdown-content)` |
| `dropdownBackgroundColor` | color | Background color | `background-color` on `:where(.brx-dropdown-content)` |
| `dropdownBorder` | border | Border | `border` on `:where(.brx-dropdown-content)` |
| `dropdownBoxShadow` | box-shadow | Box shadow | `box-shadow` on `:where(.brx-dropdown-content)` |
| `dropdownTypography` | typography | Typography | `font` on `:where(.brx-dropdown-content)` |
| `dropdownTransform` | transform | Transform | `transform` on `:where(.brx-nav-nested-items > .brxe-dropdown > .brx-dropdown-content)` |
| `dropdownTransformOpen` | transform | Transform | `transform` on `:where(.brx-nav-nested-items > .brxe-dropdown).open > :where(.brx-dropdown-content)` |
| `dropdownTransition` | text | Transition | `transition` on `:where(.brx-dropdown-content)` |
| `dropdownZindex` | number | Z-index | `z-index` on `:where(.brxe-dropdown)` |
| `dropdownPadding` | spacing | Padding | `padding` on `:where(.brx-dropdown-content > li) > a`, `padding` on `:where(.brx-dropdown-content .brx-submenu-toggle > *)` |
| `dropdownItemBackground` | color | Background | `background-color` on `:where(.brx-dropdown-content) > li`, `background-color` on `:where(.brx-dropdown-content) .brx-submenu-toggle` |
| `dropdownItemBorder` | border | Border | `border` on `:where(.brx-dropdown-content > li:not(.brxe-dropdown))`, `border` on `:where(.brx-dropdown-content .brx-submenu-toggle)` |
| `dropdownItemTypography` | typography | Typography | `font` on `:where(.brx-dropdown-content > li) > a`, `font` on `:where(.brx-dropdown-content .brx-submenu-toggle > *)` |
| `dropdownItemTransition` | text | Transition | `transition` on `:where(.brx-dropdown-content > li)`, `transition` on `:where(.brx-dropdown-content > li) > a`, `transition` on `:where(.brx-dropdown-content) .brx-submenu-toggle`, `transition` on `&.brx-has-megamenu :where(.brx-dropdown-content > *)` |
| `multiLevel` | checkbox | Enable | — |
| `multiLevelBackText` | text | Back | — |
| `multiLevelBackTypography` | typography | Back | `font` on `:where(.brx-multilevel-back)` |
| `multiLevelBackBackground` | color | Back | `background-color` on `:where(.brx-multilevel-back)` |
| `mobileMenu` | select | mobileMenu | — |
| `mobileMenuCustomBreakpoint` | number | Custom breakpoint | — |
| `mobileMenuWidth` | number | Width | `width` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuHeight` | number | Height | `height` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuContentPadding` | spacing | Padding | `padding` on `&.brx-open :where(.brx-dropdown-content > *)` |
| `mobileMenuAlignItems` | align-items | Align items | `align-items` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuJustifyContent` | justify-content | Justify content | `justify-content` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuPosition` | dimensions | Position | `—` on `&.brx-open :where(.brx-nav-nested-items)`, `width` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuBackgroundColor` | color | Background color | `background-color` on `&.brx-open :where(.brx-nav-nested-items)` |
| `mobileMenuItemAlignItems` | align-items | Align items | `justify-content` on `&.brx-open :where(.brx-submenu-toggle)`, `justify-content` on `&.brx-open :where(.brx-nav-nested-items > li)`, `justify-content` on `&.brx-open :where(.brx-submenu-toggle)`, `justify-content` on `&.brx-open :where(.brx-nav-nested-items > li)`, `justify-content` on `&.brx-open :where(.brx-submenu-toggle)`, `justify-content` on `&.brx-open :where(.brx-nav-nested-items > li)`, `display` on `&.brx-open :where(li.menu-item)` |

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
