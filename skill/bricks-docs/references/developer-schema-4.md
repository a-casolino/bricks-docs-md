# Divider Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/divider/

*Schema for Bricks Divider element*

| Property | Value |
|---|---|
| `name` | divider |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `height` | number | Height | `height` on `.line`, `border-top-width` on `&.horizontal .line` |
| `width` | number | Width | `width` on `&.horizontal .line`, `border-right-width` on `&.vertical .line` |
| `style` | select | Style | `border-top-style` on `&.horizontal .line`, `border-right-style` on `&.vertical .line` |
| `direction` | select | Direction | — |
| `justifyContent` | justify-content | Align | `justify-content` on `&.horizontal`, `align-self` on `&.vertical` |
| `color` | color | Color | `border-top-color` on `&.horizontal .line`, `border-right-color` on `&.vertical .line`, `color` on `.icon` |
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Typography | `font` on `.icon` |
| `iconAlignItems` | align-items | Align | `align-items` |
| `iconPosition` | select | Position | — |
| `iconSpacing` | number | Spacing | `gap` |
| `link` | link | Link | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Dropdown Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/dropdown/

*Schema for Bricks Dropdown element*

| Property | Value |
|---|---|
| `name` | dropdown |
| `category` | general |
| `tag` | li |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | text | HTML tag | — |
| `text` | text | Text | — |
| `link` | link | Link to | — |
| `ariaLabel` | text | Attribute | — |
| `icon` | icon | Icon | `—` on `.brx-submenu-toggle button > svg` |
| `iconPadding` | spacing | Icon padding | `padding` on `.brx-submenu-toggle button` |
| `gap` | number | Gap | `gap` on `.brx-submenu-toggle` |
| `iconPosition` | select | Icon position | `flex-direction` on `.brx-submenu-toggle`, `flex-direction` on `.brx-submenu-toggle` |
| `iconSize` | number | Icon size | `font-size` on `.brx-submenu-toggle button` |
| `iconColor` | color | Icon color | `color` on `.brx-submenu-toggle button` |
| `iconTransform` | transform | Icon transform | `transform` on `.brx-submenu-toggle button` |
| `iconTransformOpen` | transform | Icon transform | `transform` on `.brx-submenu-toggle button[aria-expanded="true"]` |
| `iconTransition` | text | Icon transition | `transition` on `.brx-submenu-toggle button` |
| `caretSize` | number | Size | `border-width` on `> .brx-dropdown-content::before` |
| `caretColor` | color | Color | `border-bottom-color` on `> .brx-dropdown-content::before` |
| `caretTransform` | transform | Transform | `transform` on `> .brx-dropdown-content::before` |
| `caretPosition` | dimensions | Position | `—` on `> .brx-dropdown-content::before` |
| `static` | checkbox | Position | — |
| `toggleOn` | select | Toggle on | — |
| `contentWidth` | number | Min. width | `min-width` on `.brx-dropdown-content` |
| `contentTransition` | text | Transition | `transition` on `> .brx-dropdown-content` |
| `contentTransform` | transform | Transform | `transform` on `> .brx-dropdown-content` |
| `contentTransformOpen` | transform | Transform | `transform` on `&.open > .brx-dropdown-content` |
| `contentBackground` | background | Background | `background` on `.brx-dropdown-content` |
| `contentBorder` | border | Border | — |
| `contentBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-dropdown-content` |
| `contentTypography` | typography | Typography | `font` on `.brx-dropdown-content` |
| `contentItemJustifyContent` | justify-content | Justify content | `justify-content` on `.brx-dropdown-content > li > a`, `justify-content` on `.brx-submenu-toggle`, `width` on `.brx-dropdown-content > li > a`, `width` on `.brx-submenu-toggle a` |
| `contentItemPadding` | spacing | Padding | `padding` on `.brx-dropdown-content > li > a`, `padding` on `.brx-dropdown-content > li\{pseudo\} > .brx-submenu-toggle`, `padding` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBackground` | color | Background | `background-color` on `.brx-dropdown-content > li > a`, `background-color` on `.brx-dropdown-content .brx-submenu-toggle`, `background-color` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBorder` | border | Border | `border` on `.brx-dropdown-content > li > a`, `border` on `.brx-dropdown-content .brx-submenu-toggle`, `border` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemTypography` | typography | Typography | `font` on `.brx-dropdown-content > li\{pseudo\} > a`, `font` on `.brx-dropdown-content > li\{pseudo\} > .brx-submenu-toggle > *`, `font` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemTransition` | text | Transition | `transition` on `.brx-dropdown-content > li`, `transition` on `.brx-dropdown-content > li > a`, `transition` on `.brx-dropdown-content .brx-submenu-toggle`, `transition` on `&.brx-has-megamenu .brx-dropdown-content > *` |
| `contentItemBackgroundActive` | color | Background | `background-color` on `.brx-dropdown-content > li [aria-current="page"]`, `background-color` on `.brx-dropdown-content > li .aria-current`, `background-color` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `contentItemBorderActive` | border | Border | `border` on `.brx-dropdown-content > li [aria-current="page"]`, `border` on `.brx-dropdown-content > li .aria-current`, `border` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `contentItemTypographyActive` | typography | Typography | `font` on `.brx-dropdown-content > li [aria-current="page"]`, `font` on `.brx-dropdown-content > li .aria-current`, `font` on `&.brx-has-megamenu .brx-dropdown-content [aria-current="page"]` |
| `megaMenu` | checkbox | Enable | — |
| `megaMenuWidth` | number | Width | `--brx-mega-menu-width` |
| `megaMenuAlignment` | select | Alignment | `--brx-mega-menu-align` |
| `megaMenuSelector` | text | CSS selector | — |
| `megaMenuSelectorVertical` | text | CSS selector | — |
| `multiLevel` | checkbox | Enable | — |
| `multiLevelBackText` | text | Back | — |
| `multiLevelBackTypography` | typography | Back | `font` on `.brx-multilevel-back` |
| `multiLevelBackBackground` | color | Back | `background-color` on `.brx-multilevel-back` |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Facebook Page Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/facebook-page/

*Schema for Bricks Facebook Page element*

| Property | Value |
|---|---|
| `name` | facebook-page |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `href` | text | Facebook page URL | — |
| `height` | number | Height | — |
| `width` | number | Width | — |
| `tabs` | select | Tabs | — |
| `hideCover` | checkbox | Hide cover | — |
| `profilePhotos` | checkbox | Show friends\ | — |
| `hideCta` | checkbox | Hide CTA button | — |
| `smallHeader` | checkbox | Small header | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# File Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/file/

*Schema for Bricks File element*

| Property | Value |
|---|---|
| `name` | file |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `source` | select | Source | — |
| `file` | file | file | — |
| `external` | text | external | — |
| `useDynamicData` | text | useDynamicData | — |
| `hideFileName` | checkbox | Hide file name | — |
| `customFileName` | text | Custom file name | — |
| `openInNewTab` | checkbox | Open in new tab | — |
| `hideDownloadButton` | checkbox | Hide download button | — |
| `downloadButtonText` | text | Text | — |
| `buttonSize` | select | Size | — |
| `buttonStyle` | select | Style | — |
| `buttonCircle` | checkbox | Circle | — |
| `buttonOutline` | checkbox | Outline | — |
| `hidePdfPreview` | checkbox | Hide PDF preview | — |
| `previewTitle` | text | Preview title | — |
| `previewHeight` | number | Height | `height` on `.file-preview-wrap` |
| `previewDisplay` | select | Display | — |
| `previewHideBreakpoint` | select | Hide at breakpoint | — |
| `previewLoadOnInteraction` | checkbox | Load PDF on click | — |
| `previewImage` | image | Preview image | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Active Filters Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-active-filters/

*Schema for Bricks Filter - Active filters element*

| Property | Value |
|---|---|
| `name` | filter-active-filters |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `excludeIds` | text | Exclude filter IDs | — |
| `buttonPadding` | spacing | Padding | `padding` on `.bricks-button` |
| `buttonGap` | number | Gap | `gap` |
| `buttonSize` | select | Size | — |
| `buttonStyle` | select | Style | — |
| `buttonCircle` | checkbox | Circle | — |
| `buttonOutline` | checkbox | Outline | — |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border-color` on `.bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `.bricks-button` |
| `icon` | icon | Icon | — |
| `iconColor` | color | Color | `color` on `.bricks-button i`, `fill` on `.bricks-button svg path` |
| `iconSize` | number | Size | `font-size` on `.bricks-button .icon` |
| `iconGap` | number | Gap | `gap` on `.bricks-button` |
| `iconPosition` | select | Position | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Checkbox Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-checkbox/

*Schema for Bricks Filter - Checkbox element*

| Property | Value |
|---|---|
| `name` | filter-checkbox |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterSource` | select | Source | — |
| `sourceFieldType` | select | Field type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Meta key | — |
| `fieldCompareOperator` | select | Compare | — |
| `fieldCompareType` | select | Compare type | — |
| `wpPostField` | select | Field | — |
| `wpUserField` | select | Field | — |
| `wpTermField` | select | Field | — |
| `filterTaxonomy` | select | Taxonomy | — |
| `filterTaxonomyOrderBy` | select | Order by | — |
| `filterTaxonomyOrderMetaKey` | text | Order meta key | — |
| `filterTaxonomyOrder` | select | filterTaxonomyOrder | — |
| `filterTermInclude` | select | filterTermInclude | — |
| `filterTermExclude` | select | filterTermExclude | — |
| `filterTermTopLevel` | checkbox | Top level terms only | — |
| `filterIncludeChildrenCount` | checkbox | Count | — |
| `filterHierarchical` | checkbox | Hierarchical | — |
| `filterAutoCheckChildren` | checkbox | Auto toggle child terms | — |
| `filterHierarchyCollapsible` | checkbox | Enable expand/collapse | — |
| `filterHierarchyShowExpanded` | checkbox | Show expanded | — |
| `filterHierarchyExpandIcon` | icon | Expand icon | — |
| `filterHierarchyCollapseIcon` | icon | Collapse icon | — |
| `filterHierarchyIconTypography` | typography | Icon typography | `font` on `.brx-hierarchy-toggle, .brx-hierarchy-toggle-spacer` |
| `filterHierarchyIconGap` | number | Icon gap | `--brx-hierarchy-toggle-gap` |
| `filterChildIndentation` | text | Indent | — |
| `filterChildIndentationGap` | number | Indent | `margin-inline-start` on `[class*="depth-"]:not([class*="depth-0"])` |
| `filterMultiLogic` | select | Multiple options | — |
| `filterGroupLabel` | text | Group label | — |
| `filterHideEmpty` | checkbox | Hide empty | — |
| `filterHideCount` | checkbox | Hide count | — |
| `filterCountNoBracket` | checkbox | Hide count bracket | — |
| `labelMapping` | select | Label | — |
| `customLabelMapping` | repeater | Label | — |
| `populatedOptionsOrderBy` | select | Order by | — |
| `populatedOptionsOrder` | select | populatedOptionsOrder | — |
| `displayMode` | select | Mode | — |
| `optionsGap` | number | Option | `--brx-options-gap` |
| `buttonOptionsGap` | number | Option | `--brx-btn-options-gap` |
| `optionsTypography` | typography | Option | `font` on `.brx-option-text` |
| `countAlignEnd` | checkbox | Count | — |
| `countTypography` | typography | Count | `font` on `.brx-option-count` |
| `buttonSize` | select | Size | — |
| `buttonStyle` | select | Style | — |
| `buttonCircle` | checkbox | Circle | — |
| `buttonOutline` | checkbox | Outline | — |
| `buttonBackgroundColor` | color | Background color | `background-color` on `&[data-mode="button"] .bricks-button` |
| `buttonBorder` | border | Border | `border-color` on `&[data-mode="button"] .bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `&[data-mode="button"] .bricks-button` |
| `buttonActiveBackgroundColor` | color | Background color | `background-color` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `buttonActiveBorder` | border | Border | `border-color` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `buttonActiveTypography` | typography | Typography | `font` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `limitOptions` | number | Visible options limit | — |
| `showMoreText` | text | Show more | — |
| `showLessText` | text | Show less | — |
| `showMoreButtonSize` | select | Size | — |
| `showMoreButtonStyle` | select | Style | — |
| `showMoreButtonCircle` | checkbox | Circle | — |
| `showMoreButtonOutline` | checkbox | Outline | — |
| `showMoreButtonBackgroundColor` | color | Background color | `background-color` on `.brx-show-more-less-button` |
| `showMoreButtonBorder` | border | Border | `border-color` on `.brx-show-more-less-button` |
| `showMoreButtonTypography` | typography | Typography | `font` on `.bricks-button.brx-show-more-less-button` |
| `filterDefaultValue` | text | Default value | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Datepicker Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-datepicker/

*Schema for Bricks Filter - Datepicker element*

| Property | Value |
|---|---|
| `name` | filter-datepicker |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterSource` | select | Source | — |
| `sourceFieldType` | select | Field type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Meta key | — |
| `fieldCompareOperator` | select | Compare | — |
| `wpPostField` | select | Field | — |
| `wpUserField` | select | Field | — |
| `wpTermField` | select | Field | — |
| `filterTaxonomyOrderBy` | select | Order by | — |
| `filterTaxonomyOrderMetaKey` | text | Order meta key | — |
| `filterTaxonomyOrder` | select | filterTaxonomyOrder | — |
| `filterTermInclude` | select | filterTermInclude | — |
| `filterTermExclude` | select | filterTermExclude | — |
| `filterTermTopLevel` | checkbox | Top level terms only | — |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `filterDefaultValue` | text | Default value | — |
| `filterDefaultMin` | text | Start date | — |
| `filterDefaultMax` | text | End date | — |
| `enableTime` | checkbox | Enable time | — |
| `isDateRange` | checkbox | Date range | — |
| `customFieldEndKey` | text | End date meta key | — |
| `useMinMax` | checkbox | Min/max date | — |
| `placeholder` | text | Placeholder | — |
| `placeholderTypography` | typography | Placeholder typography | `font` on `input::placeholder` |
| `l10n` | text | Language | — |
| `dateFormat` | text | Datepicker format | — |
| `icon` | icon | Icon | — |
| `iconColor` | color | Icon color | `color` on `.icon` |
| `iconSize` | number | Icon size | `font-size` on `.icon` |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Radio Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-radio/

*Schema for Bricks Filter - Radio element*

| Property | Value |
|---|---|
| `name` | filter-radio |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterAction` | select | Action | — |
| `filterSource` | select | Source | — |
| `sourceFieldType` | select | Field type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Meta key | — |
| `fieldCompareOperator` | select | Compare | — |
| `fieldCompareType` | select | Compare type | — |
| `wpPostField` | select | Field | — |
| `wpUserField` | select | Field | — |
| `wpTermField` | select | Field | — |
| `filterTaxonomy` | select | Taxonomy | — |
| `filterTaxonomyOrderBy` | select | Order by | — |
| `filterTaxonomyOrderMetaKey` | text | Order meta key | — |
| `filterTaxonomyOrder` | select | filterTaxonomyOrder | — |
| `filterTermInclude` | select | filterTermInclude | — |
| `filterTermExclude` | select | filterTermExclude | — |
| `filterTermTopLevel` | checkbox | Top level terms only | — |
| `filterIncludeChildrenCount` | checkbox | Count | — |
| `filterHierarchical` | checkbox | Hierarchical | — |
| `filterChildIndentation` | text | Indent | — |
| `filterChildIndentationGap` | number | Indent | `margin-inline-start` on `[class*="depth-"]:not([class*="depth-0"])` |
| `filterGroupLabel` | text | Group label | — |
| `filterHideEmpty` | checkbox | Hide empty | — |
| `filterHideCount` | checkbox | Hide count | — |
| `filterCountNoBracket` | checkbox | Hide count bracket | — |
| `filterHideAllOption` | checkbox | Hide "All" option | — |
| `filterLabelAll` | text | Label | — |
| `labelMapping` | select | Label | — |
| `customLabelMapping` | repeater | Label | — |
| `populatedOptionsOrderBy` | select | Order by | — |
| `populatedOptionsOrder` | select | populatedOptionsOrder | — |
| `sortOptions` | repeater | Sort options | — |
| `perPageOptions` | text | Options | — |
| `displayMode` | select | Mode | — |
| `optionsGap` | number | Option | `--brx-options-gap` |
| `buttonOptionsGap` | number | Option | `--brx-btn-options-gap` |
| `optionsTypography` | typography | Option | `font` on `.brx-option-text` |
| `countAlignEnd` | checkbox | Count | — |
| `countTypography` | typography | Count | `font` on `.brx-option-count` |
| `buttonSize` | select | Size | — |
| `buttonStyle` | select | Style | — |
| `buttonCircle` | checkbox | Circle | — |
| `buttonOutline` | checkbox | Outline | — |
| `buttonBackgroundColor` | color | Background color | `background-color` on `&[data-mode="button"] .bricks-button` |
| `buttonBorder` | border | Border | `border-color` on `&[data-mode="button"] .bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `&[data-mode="button"] .bricks-button` |
| `buttonActiveBackgroundColor` | color | Background color | `background-color` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `buttonActiveBorder` | border | Border | `border-color` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `buttonActiveTypography` | typography | Typography | `font` on `&[data-mode="button"] .bricks-button.brx-option-active` |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `limitOptions` | number | Visible options limit | — |
| `showMoreText` | text | Show more | — |
| `showLessText` | text | Show less | — |
| `showMoreButtonSize` | select | Size | — |
| `showMoreButtonStyle` | select | Style | — |
| `showMoreButtonCircle` | checkbox | Circle | — |
| `showMoreButtonOutline` | checkbox | Outline | — |
| `showMoreButtonBackgroundColor` | color | Background color | `background-color` on `.brx-show-more-less-button` |
| `showMoreButtonBorder` | border | Border | `border-color` on `.brx-show-more-less-button` |
| `showMoreButtonTypography` | typography | Typography | `font` on `.bricks-button.brx-show-more-less-button` |
| `filterDefaultValue` | text | Default value | — |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Range Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-range/

*Schema for Bricks Filter - Range element*

| Property | Value |
|---|---|
| `name` | filter-range |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterSource` | select | Source | — |
| `sourceFieldType` | select | Field type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Meta key | — |
| `wpPostField` | select | Field | — |
| `wpUserField` | select | Field | — |
| `wpTermField` | select | Field | — |
| `filterTaxonomyOrderBy` | select | Order by | — |
| `filterTaxonomyOrderMetaKey` | text | Order meta key | — |
| `filterTaxonomyOrder` | select | filterTaxonomyOrder | — |
| `filterTermInclude` | select | filterTermInclude | — |
| `filterTermExclude` | select | filterTermExclude | — |
| `filterTermTopLevel` | checkbox | Top level terms only | — |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `filterDefaultMin` | text | Minimum | — |
| `filterDefaultMax` | text | Maximum | — |
| `disableAutoMinMax` | checkbox | Disable auto min/max value | — |
| `displayMode` | select | Mode | — |
| `step` | number | step | — |
| `decimalPlaces` | number | Decimal places | — |
| `labelThousandSeparator` | checkbox | Thousand separator | — |
| `labelSeparatorText` | text | Separator | — |
| `labelMin` | text | Min | — |
| `labelMax` | text | Max | — |
| `labelDirection` | direction | Direction | `flex-direction` on `.min-max-wrap > *, .value-wrap > *` |
| `labelGap` | number | Gap | `gap` on `.value-wrap > span`, `gap` on `.min-max-wrap > div` |
| `labelTypography` | typography | Typography | `font` on `.label` |
| `placeholderMin` | text | Placeholder | — |
| `placeholderMax` | text | Placeholder | — |
| `inputBackgroundColor` | color | Background color | `background-color` on `.min-max-wrap input` |
| `inputBorder` | border | Border | `border` on `.min-max-wrap input` |
| `inputTypography` | typography | Typography | `font` on `.min-max-wrap input` |
| `inputWidth` | number | Width | `width` on `.min-max-wrap input` |
| `inputUseCustomStepper` | checkbox | Custom stepper | — |
| `inputCustomStepperButtonGap` | number | Gap | `gap` on `.min-max-wrap.has-custom-stepper .brx-stepper` |
| `inputCustomStepperInputGap` | number | Gap | `margin-inline-start` on `.min-max-wrap.has-custom-stepper .brx-stepper` |
| `inputCustomStepperButtonBackgroundColor` | color | Button | `background-color` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `inputCustomStepperButtonBorder` | border | Button | `border` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `inputCustomStepperButtonTypography` | typography | Button | `font` on `.min-max-wrap.has-custom-stepper .brx-stepper-button` |
| `sliderSpacing` | number | Spacing | `padding-top` on `.double-slider-wrap`, `margin-top` on `.double-slider-wrap .value-wrap` |
| `sliderBarHeight` | number | Bar | `border-width` on `.double-slider-wrap .slider-wrap .slider-base`, `border-width` on `.double-slider-wrap .slider-wrap .slider-track` |
| `sliderBarColor` | color | Bar | `border-color` on `.double-slider-wrap .slider-wrap .slider-base` |
| `sliderBarColorActive` | color | Bar | `border-color` on `.double-slider-wrap .slider-wrap .slider-track`, `border-color` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `border-color` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbSize` | number | Thumb | `width` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `width` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb`, `height` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `height` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb`, `border-radius` on `:scope > .double-slider-wrap input[type="range"]::-moz-range-thumb`, `border-radius` on `:scope > .double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBackgroundColor` | color | Thumb | `background-color` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `background-color` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBorderFull` | border | Thumb | `border` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `border` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |
| `sliderThumbBoxShadow` | box-shadow | Thumb | `box-shadow` on `.double-slider-wrap input[type="range"]::-moz-range-thumb`, `box-shadow` on `.double-slider-wrap input[type="range"]::-webkit-slider-thumb` |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Geolocation Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-geolocation/

*Schema for Bricks Filter - Geolocation element*

| Property | Value |
|---|---|
| `name` | filter-geolocation |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `sourceFieldType` | select | Object type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Location field | — |
| `geoCoordinateSource` | select | Coordinate format | — |
| `geoLatitudeKey` | text | Latitude meta key | — |
| `geoLongitudeKey` | text | Longitude meta key | — |
| `geoCoordinatesKey` | text | Coordinates meta key | — |
| `geoOrderByDistance` | checkbox | Sort results by distance | — |
| `geoPersistUrl` | checkbox | Save location in URL | — |
| `geoUseDefaultLocation` | checkbox | Use default location | — |
| `geoSearchByAddress` | checkbox | Search by address | — |
| `geoLabel` | text | Label | — |
| `geoHideLabel` | checkbox | Hide label | — |
| `geoAddressPlaceholder` | text | Address placeholder | — |
| `geoAddressAutocomplete` | checkbox | Address autocomplete | — |
| `geoAutocompleteCountryCodes` | text | Country codes | — |
| `geoAutocompleteAreaMode` | select | Autocomplete map area | — |
| `geoHideSearchButton` | checkbox | Hide search button | — |
| `geoSearchButtonText` | text | Search button text | — |
| `geoSearchByDeviceLocation` | checkbox | Search by device location | — |
| `geoLocateButtonDisplay` | select | Button content | — |
| `geoLocateButtonText` | text | Button text | — |
| `geoLocateClearText` | text | Clear button text | — |
| `geoLocateButtonIcon` | icon | Location icon | — |
| `geoLocateClearIcon` | icon | Clear icon | — |
| `geoLocateIconPosition` | select | Icon position | — |
| `geoDefaultRadius` | number | Default radius | — |
| `geoUnit` | select | Distance unit | — |
| `geoUnitLabelFormat` | select | Unit label format | — |
| `geoEnableRadiusSelect` | checkbox | Radius dropdown | — |
| `geoRadiusLabel` | text | Radius label | — |
| `geoHideRadiusLabel` | checkbox | Hide radius label | — |
| `geoRadiusOptions` | repeater | Radius options | — |
| `choicesJs` | checkbox | Enhanced radius dropdown | — |
| `choicesPosition` | select | Dropdown position | — |
| `geoMapId` | query-list | Map | — |
| `geoSearchOnDrag` | checkbox | Search on map drag | — |
| `geoSearchOnDragMode` | select | Map search behavior | — |
| `geoSearchOnDragDefault` | checkbox | Checked by default | — |
| `geoSearchOnDragLabel` | text | Checkbox label | — |
| `geoSearchOnDragPosition` | select | Checkbox position | — |
| `geoSearchOnDragDelay` | number | Search delay | — |
| `geoRadiusFillColor` | color | Radius fill color | `--brx-geo-radius-fill-color` |
| `geoRadiusStrokeColor` | color | Radius border color | `--brx-geo-radius-stroke-color` |
| `geoMarkerColor` | color | Origin marker color | `--brx-geo-marker-color` |
| `geoMarkerImage` | image | Origin marker image | — |
| `geoMarkerWidth` | number | Marker width | — |
| `geoMarkerHeight` | number | Marker height | — |
| `geoControlsDirection` | direction | Direction | `flex-direction` on `.brx-filter-geolocation__controls` |
| `geoControlsWrap` | select | Wrap | `flex-wrap` on `.brx-filter-geolocation__controls` |
| `geoControlsAlignItems` | align-items | Align items | `align-items` on `.brx-filter-geolocation__controls` |
| `geoGap` | number | Gap | `gap` on `.brx-filter-geolocation__controls` |
| `geoLabelTypography` | typography | Typography | `font` on `.brx-filter-geolocation__label` |
| `geoLabelSpacing` | number | Spacing | `margin-bottom` on `.brx-filter-geolocation__label` |
| `geoAddressWidth` | number | Width | `width` on `.brx-filter-geolocation__address-wrap` |
| `geoAddressMinHeight` | number | Min. height | `min-height` |
| `geoAddressPadding` | dimensions | Padding | `padding` on `.brx-filter-geolocation__address`, `padding` on `.brx-filter-geolocation__autocomplete::part(input)` |
| `geoAddressBackground` | background | Background | `background` |
| `geoAddressBorder` | border | Border | `border` |
| `geoAddressBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `geoAddressTypography` | typography | Typography | `font`, `font` on `.brx-filter-geolocation__autocomplete::part(input)` |
| `geoAddressPlaceholderTypography` | typography | Placeholder typography | `font` on `.brx-filter-geolocation__address::placeholder, .brx-filter-geolocation__autocomplete::part(input)::placeholder` |
| `geoClearIcon` | icon | Icon | — |
| `geoClearIconColor` | color | Icon color | `color` on `.brx-filter-geolocation__clear-icon` |
| `geoClearIconSize` | number | Icon size | `font-size` on `.brx-filter-geolocation__clear-icon` |
| `geoClearIconInset` | number | Icon inset | `inset-inline-end` on `.brx-filter-geolocation__clear-icon` |
| `geoSearchWidth` | number | Width | `width` on `.brx-filter-geolocation__search` |
| `geoSearchPadding` | dimensions | Padding | `padding` on `.brx-filter-geolocation__search` |
| `geoSearchBackground` | background | Background | `background` on `.brx-filter-geolocation__search` |
| `geoSearchBorder` | border | Border | `border` on `.brx-filter-geolocation__search` |
| `geoSearchBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-filter-geolocation__search` |
| `geoSearchTypography` | typography | Typography | `font` on `.brx-filter-geolocation__search` |
| `geoRadiusWidth` | number | Width | `width` on `.brx-filter-geolocation__radius-wrap` |
| `geoRadiusPadding` | dimensions | Padding | `padding` on `.brx-filter-geolocation__radius` |
| `geoRadiusBackground` | background | Background | `background` on `.brx-filter-geolocation__radius` |
| `geoRadiusBorder` | border | Border | `border` on `.brx-filter-geolocation__radius` |
| `geoRadiusBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-filter-geolocation__radius` |
| `geoRadiusTypography` | typography | Typography | `font` on `.brx-filter-geolocation__radius` |
| `geoLocateWidth` | number | Width | `width` on `.brx-filter-geolocation__locate` |
| `geoLocatePadding` | dimensions | Padding | `padding` on `.brx-filter-geolocation__locate` |
| `geoLocateBackground` | background | Background | `background` on `.brx-filter-geolocation__locate` |
| `geoLocateBorder` | border | Border | `border` on `.brx-filter-geolocation__locate` |
| `geoLocateBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-filter-geolocation__locate` |
| `geoLocateTypography` | typography | Typography | `font` on `.brx-filter-geolocation__locate` |
| `geoLocateIconColor` | color | Icon color | `color` on `.brx-filter-geolocation__locate .icon` |
| `geoLocateIconSize` | number | Icon size | `font-size` on `.brx-filter-geolocation__locate .icon` |
| `geoLocateIconGap` | number | Icon gap | `gap` on `.brx-filter-geolocation__locate` |
| `geoDisableStatusMessages` | checkbox | Hide status messages | — |
| `geoStatusTypography` | typography | Typography | `font` on `.brx-filter-geolocation__status` |
| `geoStatusMargin` | spacing | Margin | `margin` on `.brx-filter-geolocation__status:not(:empty):not(.screen-reader-text)` |
| `geoStatusPadding` | spacing | Padding | `padding` on `.brx-filter-geolocation__status:not(:empty):not(.screen-reader-text)` |
| `choicesPadding` | text | Padding | `--choices-inner-padding` on `.brx-filter-geolocation__radius-wrap` |
| `choicesBackgroundColor` | color | Background | `--choices-bg-color` on `.brx-filter-geolocation__radius-wrap` |
| `choicesBorderBase` | text | Border (Base) | `--choices-base-border` on `.brx-filter-geolocation__radius-wrap` |
| `choicesBorderColor` | color | Border color | `--choices-keyline-color` on `.brx-filter-geolocation__radius-wrap`, `border-color` on `.bricks-choices__inner, .bricks-choices__list--dropdown`, `border-color` on `.bricks-choices.is-focused .bricks-choices__inner, .bricks-choices.is-open .bricks-choices__inner, .bricks-choices.is-open .bricks-choices__list--dropdown` |
| `choicesBorderRadius` | number | Border radius | `--choices-border-radius` on `.brx-filter-geolocation__radius-wrap` |
| `choicesFontSize` | number | Font size | `--choices-font-size` on `.brx-filter-geolocation__radius-wrap` |
| `choicesTextColor` | color | Text color | `--choices-brx-text-color` on `.brx-filter-geolocation__radius-wrap` |
| `choicesArrowColor` | color | Arrow color | `--choices-text-color` on `.brx-filter-geolocation__radius-wrap` |
| `choicesItemPadding` | text | Padding | `--choices-dropdown-item-padding` on `.brx-filter-geolocation__radius-wrap` |
| `choicesDropdownBackground` | color | Background | `--choices-bg-color-dropdown` on `.brx-filter-geolocation__radius-wrap` |
| `choicesHighlightBackground` | color | Highlight: Background | `--choices-highlighted-color` on `.brx-filter-geolocation__radius-wrap` |
| `choicesHighlightTextColor` | color | Highlight: Text color | `--choices-brx-highlighted-text-color` on `.brx-filter-geolocation__radius-wrap` |
| `choicesDisabledBackground` | color | Disabled: Background | `--choices-brx-bg-color-disabled` on `.brx-filter-geolocation__radius-wrap` |
| `choicesDisabledTextColor` | color | Disabled: Text color | `--choices-brx-text-color-disabled` on `.brx-filter-geolocation__radius-wrap` |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Search Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-search/

*Schema for Bricks Filter - Search element*

| Property | Value |
|---|---|
| `name` | filter-search |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `filterDefaultValue` | text | Default value | — |
| `filterInputDebounce` | number | Debounce | — |
| `filterMinChars` | number | Min. characters | — |
| `filterEnterAction` | select | Enter action | — |
| `filterEnterTriggerSubmit` | checkbox | Trigger Filter Submit interactions | — |
| `redirectTo` | text | Redirect to | — |
| `newTab` | checkbox | Open in new tab | — |
| `searchCriteriaCustom` | checkbox | Custom search criteria | — |
| `useWeightScore` | checkbox | Use weight score | — |
| `searchPostMatchAnyWord` | checkbox | Match any word | — |
| `searchPostFields` | checkbox | Search post fields | — |
| `searchPostQuery` | repeater | Post fields | — |
| `searchPostMeta` | checkbox | Search post meta fields | — |
| `searchPostMetaKeys` | repeater | Post meta keys | — |
| `searchPostTerms` | checkbox | Search post terms | — |
| `searchPostTaxonomies` | repeater | Taxonomies | — |
| `searchTermFields` | checkbox | Search term fields | — |
| `searchTermQuery` | repeater | Term fields | — |
| `searchTermMeta` | checkbox | Search term meta fields | — |
| `searchTermMetaKeys` | repeater | Term meta keys | — |
| `searchUserFields` | checkbox | Search user fields | — |
| `searchUserQuery` | repeater | User fields | — |
| `searchUserMeta` | checkbox | Search user meta fields | — |
| `searchUserMetaKeys` | repeater | User meta keys | — |
| `placeholder` | text | Placeholder | — |
| `placeholderTypography` | typography | Placeholder typography | `font` on `input::placeholder` |
| `label` | text | Label | — |
| `labelTypography` | typography | Label typography | `font` on `label` |
| `icon` | icon | Icon | — |
| `iconColor` | color | Icon color | `color` on `.icon` |
| `iconSize` | number | Icon size | `font-size` on `.icon` |

## Bricks 2.4 search submission settings

These query-filter settings are available when Query Filters are enabled. Use the controls above to configure the Enter-key behavior below.

| Key | Type | Values and behavior |
| --- | --- | --- |
| `filterEnterAction` | string | `default` for AJAX search, or `redirect` for Redirect to URL. Omitted values use AJAX search. Requires `filterQueryId`. |
| `filterEnterTriggerSubmit` | boolean | Opt into Filter Submit start/end interactions for an Enter-key AJAX search. Default: `false`. |
| `redirectTo` | string | Destination URL for `filterEnterAction: "redirect"`. Active filters for the target query become URL parameters. Empty values fall back to AJAX search. |
| `newTab` | boolean | Open the configured redirect in a new tab. Default: `false`. |

See [Filter Search](https://academy.bricksbuilder.io/builder/elements/filter/filter-search/#search-with-enter) for setup and Enter-key behavior.

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Select Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-select/

*Schema for Bricks Filter - Select element*

| Property | Value |
|---|---|
| `name` | filter-select |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterNiceName` | text | URL parameter | — |
| `filterApplyOn` | select | Apply on | — |
| `filterAction` | select | Action | — |
| `filterSource` | select | Source | — |
| `sourceFieldType` | select | Field type | — |
| `fieldProvider` | select | Provider | — |
| `customFieldKey` | text | Meta key | — |
| `fieldCompareOperator` | select | Compare | — |
| `fieldCompareType` | select | Compare type | — |
| `wpPostField` | select | Field | — |
| `wpUserField` | select | Field | — |
| `wpTermField` | select | Field | — |
| `filterTaxonomy` | select | Taxonomy | — |
| `filterTaxonomyOrderBy` | select | Order by | — |
| `filterTaxonomyOrderMetaKey` | text | Order meta key | — |
| `filterTaxonomyOrder` | select | filterTaxonomyOrder | — |
| `filterTermInclude` | select | filterTermInclude | — |
| `filterTermExclude` | select | filterTermExclude | — |
| `filterTermTopLevel` | checkbox | Top level terms only | — |
| `filterIncludeChildrenCount` | checkbox | Count | — |
| `filterHierarchical` | checkbox | Hierarchical | — |
| `filterChildIndentation` | text | Indent | — |
| `filterMultiLogic` | select | Multiple options | — |
| `filterHideEmpty` | checkbox | Hide empty | — |
| `filterHideCount` | checkbox | Hide count | — |
| `filterLabelAll` | text | Label | — |
| `labelMapping` | select | Label | — |
| `customLabelMapping` | repeater | Label | — |
| `populatedOptionsOrderBy` | select | Order by | — |
| `populatedOptionsOrder` | select | populatedOptionsOrder | — |
| `sortOptions` | repeater | Sort options | — |
| `perPageOptions` | text | Options | — |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `filterDefaultValue` | text | Default value | — |
| `placeholder` | text | Selection placeholder | — |
| `choicesJs` | checkbox | Enhanced select | — |
| `choicesPosition` | select | Dropdown position | — |
| `choicesSearch` | checkbox | Enable search | — |
| `choicesSearchBackground` | color | Background color | `background-color` on `input[type="search"]` |
| `choicesSearchPlaceholder` | text | Search placeholder | — |
| `choicesSearchInputTypography` | typography | Input | `font` on `.bricks-choices__input` |
| `choicesSearchInputPadding` | text | Input | `--choices-brx-search-input-padding` |
| `choicesNoResultsText` | text | No results | — |
| `choicesNoChoicesText` | text | No choices | — |
| `enableMultiple` | checkbox | Multiple options | — |
| `choicesPillGap` | number | Pill | `--choices-multiple-item-margin` |
| `choicesPillBackground` | color | Pill | `--choices-primary-color` |
| `choicesPillBorder` | border | Pill | `border` on `.bricks-choices__list--multiple .bricks-choices__item` |
| `choicesPillTypography` | typography | Pill | `font` on `.bricks-choices__list--multiple .bricks-choices__item` |
| `choicesPadding` | text | Padding | `--choices-inner-padding` |
| `choicesBackgroundColor` | color | Background | `--choices-bg-color` |
| `choicesBorderBase` | text | Border (Base) | `--choices-base-border` |
| `choicesBorderColor` | color | Border color | `--choices-keyline-color`, `border-color` on `.bricks-choices__inner, .bricks-choices__list--dropdown`, `border-color` on `.bricks-choices.is-focused .bricks-choices__inner, .bricks-choices.is-open .bricks-choices__inner, .bricks-choices.is-open .bricks-choices__list--dropdown` |
| `choicesBorderRadius` | number | Border radius | `--choices-border-radius` |
| `choicesFontSize` | number | Font size | `--choices-font-size` |
| `choicesTextColor` | color | Text color | `--choices-brx-text-color` |
| `choicesArrowColor` | color | Arrow color | `--choices-text-color` |
| `choicesItemPadding` | text | Padding | `--choices-dropdown-item-padding` |
| `choicesDropdownBackground` | color | Background | `--choices-bg-color-dropdown` |
| `choicesHighlightBackground` | color | Highlight: Background | `--choices-highlighted-color` |
| `choicesHighlightTextColor` | color | Highlight: Text color | `--choices-brx-highlighted-text-color` |
| `choicesDisabledBackground` | color | Disabled: Background | `--choices-brx-bg-color-disabled` |
| `choicesDisabledTextColor` | color | Disabled: Text color | `--choices-brx-text-color-disabled` |
| `choicesSearchTypography` | typography | Placeholder: Typography | `font` on `.bricks-choices__placeholder`, `font` on `.bricks-choices__input::placeholder` |
| `choicesPlaceholderOpacity` | number | Placeholder: Opacity | `--choices-placeholder-opacity` |

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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

# Filter - Submit / Reset Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/filter-submit/

*Schema for Bricks Filter - Submit / Reset element*

| Property | Value |
|---|---|
| `name` | filter-submit |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filterQueryId` | query-list | Target query | — |
| `filterDefinitionId` | filter-definition-manager | Global filter | — |
| `filterActivePrefix` | text | Prefix | — |
| `filterActiveSuffix` | text | Suffix | — |
| `filterActiveTitle` | text | Title | — |
| `filterButtonType` | select | Action | — |
| `excludeIds` | text | Exclude filter IDs | — |
| `redirectTo` | text | Redirect to | — |
| `newTab` | checkbox | Open in new tab | — |
| `hideOnNoFilter` | checkbox | Hide if no active filter | — |
| `text` | text | Text | — |
| `size` | select | Size | — |
| `style` | select | Style | — |
| `circle` | checkbox | Circle | — |
| `outline` | checkbox | Outline | — |
| `icon` | icon | Icon | — |
| `iconColor` | color | Icon color | `color` on `.icon`, `fill` on `.icon` |
| `iconSize` | number | Icon size | `font-size` on `.icon` |
| `gap` | number | Gap | `gap` |
| `direction` | direction | Direction | `flex-direction` |

## Bricks 2.4 reset exclusions

The `excludeIds` query-filter setting is a comma-separated string of Bricks filter element IDs, for example `"q1w2e3,mn9456"`. It is available with a target query (`filterQueryId`) and the Reset action (`filterButtonType: "reset"`).

Reset preserves these filters' values. With `hideOnNoFilter: true`, excluded filters are ignored when deciding whether the reset button should remain visible. This setting is independent of the Active Filters element's display exclusions.

See [Filter Submit / Reset](https://academy.bricksbuilder.io/builder/elements/filter/filter-submit/#preserve-a-search-while-resetting-refinements) for a search-and-refinements example.

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
| `_columns` | text | Columns | `columns` |
| `_columnGap` | number | Column gap | `column-gap` |
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
