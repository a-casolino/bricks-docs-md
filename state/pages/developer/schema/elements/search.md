*Schema for Bricks Search element*

| Property | Value |
|---|---|
| `name` | search |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `searchType` | select | Type | — |
| `actionURL` | text | Action URL | — |
| `additionalParams` | repeater | Additional parameters | — |
| `inputHeight` | number | Height | `height` on `input[type=search]` |
| `inputWidth` | number | Width | `width` on `input[type=search]` |
| `placeholder` | text | Placeholder | — |
| `placeholderColor` | color | Placeholder color | `color` on `input[type=search]::placeholder` |
| `inputBackgroundColor` | color | Background color | `background-color` on `input[type=search]` |
| `inputBorder` | border | Border | `border` on `input[type=search]` |
| `inputBoxShadow` | box-shadow | Box shadow | `box-shadow` on `input[type=search]` |
| `inputTypography` | typography | Typography | `font` on `input[type=search]` |
| `showLabel` | checkbox | Show label | — |
| `labelText` | text | Label text | — |
| `labelTypography` | typography | Label typography | `typography` on `label` |
| `buttonAriaLabel` | text | aria-label | — |
| `buttonText` | text | Text | — |
| `icon` | icon | Icon | — |
| `buttonPadding` | spacing | Padding | `padding`, `padding` |
| `iconHeight` | number | Height | `height`, `min-height`, `height`, `min-height` |
| `iconWidth` | number | Width | `width`, `min-width`, `width`, `min-width` |
| `iconBackgroundColor` | color | Background color | `background-color`, `background-color` |
| `iconBorder` | border | Border | `border`, `border` |
| `iconBoxShadow` | box-shadow | Box shadow | `box-shadow`, `box-shadow` |
| `iconTypography` | typography | Typography | `font`, `font` |
| `overlayOpenAriaLabel` | text | aria-label | — |
| `overlayOpenIcon` | icon | Icon | — |
| `overlayOpenIconSize` | number | Icon size | `font-size` on `$overlay_open_selector > *` |
| `overlayOpenIconColor` | color | Icon color | `color` on `$overlay_open_selector > *`, `fill` on `$overlay_open_selector > *`, `stroke` on `$overlay_open_selector > *` |
| `overlayOpenPadding` | spacing | Padding | `padding` |
| `overlayOpenHeight` | number | Height | `height`, `min-height` |
| `overlayOpenWidth` | number | Width | `width`, `min-width` |
| `overlayOpenBackgroundColor` | color | Background color | `background-color` |
| `overlayOpenBorder` | border | Border | `border` |
| `overlayOpenBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `overlayFormDirection` | direction | Direction | `flex-direction` on `.bricks-search-overlay form` |
| `overlayFormGap` | number | Gap | `gap` on `.bricks-search-overlay form` |
| `hideSearchOverlayTitle` | checkbox | Hide title | — |
| `searchOverlayTitle` | text | Title | — |
| `searchOverlayTitleTag` | text | Title tag | — |
| `searchOverlayTitleTypography` | typography | Title typography | `font` on `.title` |
| `searchOverlayBackground` | background | Background | `background` on `.bricks-search-overlay` |
| `searchOverlayBackgroundOverlay` | color | Background | `background-color` on `.bricks-search-overlay:after` |
| `overlaySubmitAriaLabel` | text | aria-label | — |
| `overlaySubmitText` | text | Text | — |
| `overlaySubmitIcon` | icon | Icon | — |
| `overlaySubmitIconSize` | number | Icon size | `font-size` on `.bricks-search-overlay button[type="submit"] > *` |
| `overlaySubmitIconColor` | color | Icon color | `color` on `.bricks-search-overlay button[type="submit"] > *`, `fill` on `.bricks-search-overlay button[type="submit"] > *`, `stroke` on `.bricks-search-overlay button[type="submit"] > *` |
| `overlayIconWidth` | number | Width | `width` on `.bricks-search-overlay button[type="submit"]`, `min-width` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonHeight` | number | Height | `height` on `.bricks-search-overlay button[type="submit"]`, `min-height` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonPadding` | spacing | Padding | `padding` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonBackground` | color | Background color | `background-color` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonBorder` | border | Border | `border` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-search-overlay button[type="submit"]` |
| `overlayButtonTypography` | typography | Typography | `font` on `.bricks-search-overlay button[type="submit"]` |
| `overlayCloseAriaLabel` | text | aria-label | — |
| `overlayCloseIcon` | icon | Icon | — |
| `overlayCloseIconSize` | number | Icon size | `font-size` on `.bricks-search-overlay > .close` |
| `overlayCloseIconColor` | color | Icon color | `color` on `.bricks-search-overlay > .close`, `color` on `.bricks-search-overlay > .close > *`, `fill` on `.bricks-search-overlay > .close`, `fill` on `.bricks-search-overlay > .close > *`, `stroke` on `.bricks-search-overlay > .close`, `stroke` on `.bricks-search-overlay > .close > *` |
| `overlayCloseWidth` | number | Width | `width` on `.bricks-search-overlay > .close`, `min-width` on `.bricks-search-overlay > .close` |
| `overlayCloseHeight` | number | Height | `height` on `.bricks-search-overlay > .close`, `min-height` on `.bricks-search-overlay > .close` |
| `overlayClosePadding` | spacing | Padding | `padding` on `.bricks-search-overlay > .close` |
| `overlayCloseBackgroundColor` | color | Background color | `background-color` on `.bricks-search-overlay > .close` |
| `overlayCloseBorder` | border | Border | `border` on `.bricks-search-overlay > .close` |
| `overlayCloseBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-search-overlay > .close` |

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