# Product Title Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/product-title/

*Schema for Bricks Product title element*

| Property | Value |
|---|---|
| `name` | product-title |
| `category` | woocommerce_product |
| `tag` | h1 |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tag` | select | HTML tag | — |
| `prefix` | text | Prefix | — |
| `prefixBlock` | checkbox | Prefix block | — |
| `suffix` | text | Suffix | — |
| `suffixBlock` | checkbox | Suffix block | — |
| `linkToProduct` | checkbox | Link to product | — |

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

# Product Up/Cross-Sells Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/product-upsells/

*Schema for Bricks Product up/cross-sells element*

| Property | Value |
|---|---|
| `name` | product-upsells |
| `category` | woocommerce_product |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `type` | select | Type | — |
| `headingText` | text | Heading | — |
| `headingTypography` | typography | Heading typography | `font` on `.up-sells > h2`, `font` on `.cross-sells > h2` |
| `count` | number | Max. products | — |
| `columns` | number | Columns | `grid-template-columns` on `.products` |
| `gap` | number | Gap | `gap` on `.products` |
| `orderby` | select | Order by | — |
| `order` | select | order | — |
| `buttonMargin` | spacing | Margin | `margin` on `.button` |
| `buttonAlign` | align-items | Align | `align-self` on `.button` |
| `buttonPadding` | spacing | Padding | `padding` on `.button` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.button` |
| `buttonBorder` | border | Border | `border` on `.button` |
| `buttonTypography` | typography | Typography | `font` on `.button` |

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

# Progress Bar Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/progress-bar/

*Schema for Bricks Progress Bar element*

| Property | Value |
|---|---|
| `name` | progress-bar |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `bars` | repeater | Label | `background-color` on `.bar span` |
| `height` | number | Height | `height` |
| `barSpacing` | number | Spacing | `gap` |
| `showPercentage` | checkbox | Show percentage | — |
| `barColor` | color | Bar color | `background-color` on `.bar span` |
| `barBackgroundColor` | color | Bar background color | `background-color` on `.bar` |
| `barBorder` | border | Bar border | `border` on `.bar` |
| `labelTypography` | typography | Label typography | `font` on `.label` |
| `percentageTypography` | typography | Percentage typography | `font` on `.percentage` |

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

# Rating Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/rating/

*Schema for Bricks Rating element*

| Property | Value |
|---|---|
| `name` | rating |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `rating` | number | Rating | — |
| `maxRating` | number | Max. rating | — |
| `gap` | number | Gap | `gap` |
| `icon` | icon | Icon | — |
| `iconColorFull` | color | Icon color | `color` on `.icon.full-color` |
| `iconColorEmpty` | color | Icon color | `color` on `.icon.empty-color` |
| `iconSize` | number | Icon size | `font-size` on `.icon` |
| `schema` | checkbox | Generate review schema | — |
| `schemaType` | text | Required | — |
| `schemaName` | text | Required | — |
| `reviewAuthor` | text | Optional | — |
| `schemaProperties` | repeater | Additional item reviewed properties | — |
| `schemaReviewProperties` | repeater | Additional review properties | — |

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

# Query Results Summary Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/query-results-summary/

*Schema for Bricks Query Results Summary element*

| Property | Value |
|---|---|
| `name` | query-results-summary |
| `category` | query |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `queryId` | query-list | Query | — |
| `statsFormat` | text | Format | — |
| `oneResultText` | text | Text | — |
| `noResultsText` | text | Text | — |

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

# Related Posts Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/related-posts/

*Schema for Bricks Related posts element*

| Property | Value |
|---|---|
| `name` | related-posts |
| `category` | single |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `title` | text | Title | — |
| `titleTag` | select | HTML tag | — |
| `titleMargin` | spacing | Margin | `margin` on `.related-posts-title` |
| `titleTypography` | typography | Typography | `font` on `.related-posts-title` |
| `post_type` | select | Post type | — |
| `count` | number | Max. related posts | — |
| `order` | select | order | — |
| `orderby` | select | Order by | — |
| `taxonomies` | select | Common taxonomies | — |
| `gap` | number | Gap | `gap` on `ul` |
| `columns` | number | Posts per row | `grid-template-columns` on `ul`, `grid-auto-flow` on `ul` |
| `content` | repeater | Dynamic data | `margin` |
| `noImage` | checkbox | Disable | — |
| `imageSize` | select | Image size | — |
| `imagePosition` | select | Position | — |
| `imageHeight` | number | Height | `height` on `img` |
| `imageWidth` | number | Width | `width` on `img` |
| `imageMargin` | spacing | Margin | `margin` on `figure` |
| `contentWidth` | number | Width | `width` on `.post-content` |
| `contentPadding` | spacing | Padding | `padding` on `.post-content` |
| `contentBackground` | color | Background color | `background-color` on `.post-content` |
| `overlay` | checkbox | Overlay content | — |
| `overlayAlignItems` | align-items | Horizontal alignment | `align-items` on `.post-content` |
| `overlayJustifyContent` | justify-content | Vertical alignment | `justify-content` on `.post-content` |

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

# Section Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/section/

*Schema for Bricks Section element*

| Property | Value |
|---|---|
| `name` | section |
| `category` | layout |
| `tag` | section |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `disableLazyLoad` | checkbox | Disable lazy load | — |
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
| `_columns` | text | Columns | `columns` |
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

# Search Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/search/

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

---

# Shortcode Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/shortcode/

*Schema for Bricks Shortcode element*

| Property | Value |
|---|---|
| `name` | shortcode |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `shortcode` | textarea | Shortcode | — |
| `showPlaceholder` | checkbox | Don\ | — |
| `placeholderWidth` | number | Placeholder | — |
| `placeholderHeight` | number | Placeholder | — |

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

# Sidebar Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/sidebar/

*Schema for Bricks Sidebar element*

| Property | Value |
|---|---|
| `name` | sidebar |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `sidebar` | select | Sidebar | — |
| `margin` | spacing | Widget margin | `margin` on `.bricks-widget-wrapper` |
| `titleTypography` | typography | Title typography | `font` on `.bricks-widget-title`, `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `contentTypography` | typography | Content typography | `font` |
| `searchBackground` | color | Search background color | `background-color` on `input[type=search]` |
| `searchBorder` | border | Search border | `border` on `input[type=search]` |

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

# Slidercarousel Elementbricks (Nestable) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/slider-nested/

*Schema for Bricks Slidercarousel elementbricks (Nestable) element*

| Property | Value |
|---|---|
| `name` | slider-nested |
| `category` | media |
| `tag` | div |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `optionsType` | select | Options type | — |
| `options` | code | Custom options | — |
| `type` | select | Type | — |
| `direction` | select | Direction | — |
| `keyboard` | select | Keyboard | — |
| `autoHeight` | checkbox | Auto height | — |
| `height` | number | Height | — |
| `gap` | number | Spacing | — |
| `start` | number | Start index | — |
| `perPage` | number | Items to show | — |
| `perMove` | number | Items to scroll | — |
| `speed` | number | Speed in ms | — |
| `focus` | number | Focus | — |
| `autoplay` | checkbox | Autoplay | — |
| `pauseOnHover` | checkbox | Pause on hover | — |
| `pauseOnFocus` | checkbox | Pause on focus | — |
| `interval` | number | Interval in ms | — |
| `autoScroll` | checkbox | Auto scroll | — |
| `autoScrollSpeed` | number | Speed | — |
| `autoScrollPauseOnHover` | checkbox | Pause on hover | — |
| `autoScrollPauseOnFocus` | checkbox | Pause on focus | — |
| `playbackControl` | checkbox | Show playback control | — |
| `playbackControlPosition` | select | Position | `position` on `> .bricks-slider-playback` |
| `rewind` | checkbox | Rewind | — |
| `rewindByDrag` | checkbox | Rewind by drag | — |
| `rewindSpeed` | number | Speed in ms | — |
| `slidePadding` | spacing | Padding | `padding` on `> .splide__track > .splide__list > .splide__slide` |
| `slideAlignHorizontal` | align-items | Align horizontal | `align-items` on `> .splide__track > .splide__list > .splide__slide` |
| `slideAlignVertical` | justify-content | Align vertical | `justify-content` on `> .splide__track > .splide__list > .splide__slide` |
| `slideBackground` | background | Background | `background` on `> .splide__track > .splide__list > .splide__slide` |
| `slideBorder` | border | Border | `border` on `> .splide__track > .splide__list > .splide__slide` |
| `arrows` | checkbox | Show | — |
| `arrowHeight` | number | Height | `height` on `> .splide__arrows > .splide__arrow` |
| `arrowWidth` | number | Width | `width` on `> .splide__arrows > .splide__arrow` |
| `arrowBackground` | color | Background | `background-color` on `> .splide__arrows > .splide__arrow` |
| `arrowBorder` | border | Border | `border` on `> .splide__arrows > .splide__arrow` |
| `arrowColor` | color | Color | `color` on `> .splide__arrows > .splide__arrow`, `fill` on `> .splide__arrows > .splide__arrow\{pseudo\} svg` |
| `arrowSize` | number | Size | `font-size` on `> .splide__arrows > .splide__arrow`, `height` on `> .splide__arrows > .splide__arrow svg`, `width` on `> .splide__arrows > .splide__arrow svg`, `min-height` on `> .splide__arrows > .splide__arrow`, `min-width` on `> .splide__arrows > .splide__arrow` |
| `arrowTextShadow` | text-shadow | Text shadow | `text-shadow` on `> .splide__arrows > .splide__arrow` |
| `arrowDisabledBackground` | color | Background | `background-color` on `> .splide__arrows > .splide__arrow:disabled` |
| `arrowDisabledBorder` | border | Border | `border` on `> .splide__arrows > .splide__arrow:disabled` |
| `arrowDisabledColor` | color | Color | `color` on `> .splide__arrows > .splide__arrow:disabled`, `fill` on `> .splide__arrows > .splide__arrow:disabled svg` |
| `arrowDisabledOpacity` | number | Opacity | `opacity` on `> .splide__arrows > .splide__arrow:disabled` |
| `prevArrow` | icon | Prev arrow | `—` on `> .splide__arrows > .splide__arrow--prev > *` |
| `prevArrowTop` | number | prevArrowTop | `top` on `> .splide__arrows > .splide__arrow--prev` |
| `prevArrowRight` | number | Right | `right` on `> .splide__arrows > .splide__arrow--prev` |
| `prevArrowBottom` | number | Bottom | `bottom` on `> .splide__arrows > .splide__arrow--prev` |
| `prevArrowLeft` | number | Left | `left` on `> .splide__arrows > .splide__arrow--prev` |
| `prevArrowTransform` | transform | Transform | `transform` on `> .splide__arrows > .splide__arrow--prev` |
| `nextArrow` | icon | Next arrow | `—` on `> .splide__arrows > .splide__arrow--next > *` |
| `nextArrowTop` | number | nextArrowTop | `top` on `> .splide__arrows > .splide__arrow--next` |
| `nextArrowRight` | number | Right | `right` on `> .splide__arrows > .splide__arrow--next` |
| `nextArrowBottom` | number | Bottom | `bottom` on `> .splide__arrows > .splide__arrow--next` |
| `nextArrowLeft` | number | Left | `left` on `> .splide__arrows > .splide__arrow--next` |
| `nextArrowTransform` | transform | Transform | `transform` on `> .splide__arrows > .splide__arrow--next` |
| `pagination` | checkbox | Show | — |
| `paginationSpacing` | spacing | Margin | `margin` on `> .splide__pagination .splide__pagination__page` |
| `paginationHeight` | number | Height | `height` on `> .splide__pagination .splide__pagination__page` |
| `paginationWidth` | number | Width | `width` on `> .splide__pagination .splide__pagination__page` |
| `paginationColor` | color | Color | `color` on `> .splide__pagination .splide__pagination__page`, `background-color` on `> .splide__pagination .splide__pagination__page` |
| `paginationBorder` | border | Border | `border` on `> .splide__pagination .splide__pagination__page` |
| `paginationHeightActive` | number | Height | `height` on `> .splide__pagination .splide__pagination__page.is-active` |
| `paginationWidthActive` | number | Width | `width` on `> .splide__pagination .splide__pagination__page.is-active` |
| `paginationColorActive` | color | Color | `color` on `> .splide__pagination .splide__pagination__page.is-active`, `background-color` on `> .splide__pagination .splide__pagination__page.is-active` |
| `paginationBorderActive` | border | Border | `border` on `> .splide__pagination .splide__pagination__page.is-active` |
| `paginationTop` | number | paginationTop | `top` on `> .splide__pagination`, `bottom` on `> .splide__pagination` |
| `paginationRight` | number | Right | `right` on `> .splide__pagination`, `left` on `> .splide__pagination`, `transform` on `> .splide__pagination` |
| `paginationBottom` | number | Bottom | `bottom` on `> .splide__pagination` |
| `paginationLeft` | number | Left | `left` on `> .splide__pagination`, `right` on `> .splide__pagination`, `transform` on `> .splide__pagination` |

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

# Slidercarousel Elementbricks Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/slider/

*Schema for Bricks Slidercarousel elementbricks element*

| Property | Value |
|---|---|
| `name` | slider |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `items` | repeater | Slides | `width` on `.bricks-button` |
| `slidesToShow` | number | Items to show | — |
| `slidesToScroll` | number | Items to scroll | — |
| `gutter` | number | Spacing (px) | — |
| `height` | number | Min. height | `min-height` on `.swiper-slide` |
| `effect` | select | Effect | — |
| `swiperLoop` | select | Loop | — |
| `speed` | number | Animation speed in ms | — |
| `disableLazyLoad` | checkbox | Disable lazy load | — |
| `autoplay` | checkbox | Autoplay | — |
| `pauseOnHover` | checkbox | Pause on hover | — |
| `autoplaySpeed` | number | Autoplay delay in ms | — |
| `titleMargin` | spacing | Title margin | `margin` on `.slider-content .title` |
| `titleTypography` | typography | Title typography | `font` on `.title` |
| `contentWidth` | number | Content width | `width` on `.slider-content` |
| `contentBackgroundColor` | color | Content background | `background-color` on `.slider-content` |
| `contentTypography` | typography | Content typography | `font` on `.content` |
| `contentMargin` | spacing | Content margin | `margin` on `.slider-content` |
| `contentPadding` | spacing | Content padding | `padding` on `.slider-content` |
| `contentAlignHorizontal` | justify-content | Content align horizontal | `justify-content` on `.swiper-slide` |
| `contentAlignVertical` | align-items | Content align vertical | `align-items` on `.swiper-slide` |
| `contentTextAlign` | text-align | Content text align | `text-align` on `.slider-content` |
| `buttonStyle` | select | Button style | — |
| `buttonSize` | select | Button size | — |
| `buttonWidth` | number | Button width | `width` on `.bricks-button` |
| `buttonBackground` | color | Background | `background-color` on `.bricks-button` |
| `buttonBorder` | border | Border | `border` on `.bricks-button` |
| `buttonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-button` |
| `buttonTypography` | typography | Typography | `font` on `.bricks-button` |
| `backgroundPositionTop` | number | backgroundPositionTop | `top` on `.image` |
| `backgroundPositionRight` | number | Right | `right` on `.image` |
| `backgroundPositionBottom` | number | Bottom | `bottom` on `.image` |
| `backgroundPositionLeft` | number | Left | `left` on `.image` |
| `arrows` | checkbox | Show arrows | — |
| `arrowHeight` | number | Height | `height` on `.swiper-button` |
| `arrowWidth` | number | Width | `width` on `.swiper-button` |
| `arrowBackground` | color | Background | `background-color` on `.swiper-button` |
| `arrowBorder` | border | Border | `border` on `.swiper-button` |
| `arrowTypography` | typography | Typography | `font` on `.swiper-button` |
| `prevArrow` | icon | Prev arrow | `—` on `.bricks-swiper-button-prev > *` |
| `prevArrowTop` | number | Top | `top` on `.bricks-swiper-button-prev` |
| `prevArrowRight` | number | Right | `right` on `.bricks-swiper-button-prev` |
| `prevArrowBottom` | number | Bottom | `bottom` on `.bricks-swiper-button-prev` |
| `prevArrowLeft` | number | Left | `left` on `.bricks-swiper-button-prev` |
| `prevArrowTransform` | transform | Transform | `transform` on `.bricks-swiper-button-prev` |
| `nextArrow` | icon | Next arrow | `—` on `.bricks-swiper-button-next > *` |
| `nextArrowTop` | number | Top | `top` on `.bricks-swiper-button-next` |
| `nextArrowRight` | number | Right | `right` on `.bricks-swiper-button-next` |
| `nextArrowBottom` | number | Bottom | `bottom` on `.bricks-swiper-button-next` |
| `nextArrowLeft` | number | Left | `left` on `.bricks-swiper-button-next` |
| `nextArrowTransform` | transform | Transform | `transform` on `.bricks-swiper-button-next` |
| `dots` | checkbox | Show dots | — |
| `dotsDynamic` | checkbox | Dynamic dots | — |
| `dotsVertical` | checkbox | Vertical | `flex-direction` on `.swiper-pagination-bullets` |
| `dotsHeight` | number | Height | `height` on `.swiper-pagination-bullet` |
| `dotsWidth` | number | Width | `width` on `.swiper-pagination-bullet` |
| `dotsTop` | number | Top | `top` on `.bricks-swiper-container + .swiper-pagination-bullets` |
| `dotsRight` | number | Right | `right` on `.bricks-swiper-container + .swiper-pagination-bullets`, `left` on `.bricks-swiper-container + .swiper-pagination-bullets`, `transform` on `.bricks-swiper-container + .swiper-pagination-bullets` |
| `dotsBottom` | number | Bottom | `bottom` on `.bricks-swiper-container + .swiper-pagination-bullets` |
| `dotsLeft` | number | Left | `left` on `.bricks-swiper-container + .swiper-pagination-bullets`, `transform` on `.bricks-swiper-container + .swiper-pagination-bullets` |
| `dotsBorder` | border | Border | `border` on `.swiper-pagination-bullet` |
| `dotsColor` | color | Color | `background-color` on `.swiper-pagination-bullet`, `color` on `.swiper-pagination-bullet` |
| `dotsActiveColor` | color | Active color | `background-color` on `.swiper-pagination-bullet-active`, `color` on `.swiper-pagination-bullet-active` |
| `dotsSpacing` | spacing | Margin | `margin` on `.swiper-pagination-bullet` |

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

# Icon List Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/social-icons/

*Schema for Bricks Icon List element*

| Property | Value |
|---|---|
| `name` | social-icons |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `icons` | repeater | Icons | `color` on `.icon` |
| `iconColor` | color | Icon | `color` on `.icon` |
| `iconSize` | number | Icon | `font-size` on `.icon`, `height` on `svg`, `width` on `svg` |
| `direction` | direction | Direction | `flex-direction` |
| `alignIcons` | align-items | Align items | `align-items` |
| `justifyIcons` | justify-content | Justify content | `justify-content` |
| `gap` | number | Spacing | `gap` |
| `gapItem` | number | Spacing | `gap` |

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

# Slot Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/slot/

*Schema for Bricks Slot element*

| Property | Value |
|---|---|
| `name` | slot |
| `category` | general |
| `tag` | div |
| `nestable` | true |

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

# Tabs (Nestable) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/tabs-nested/

*Schema for Bricks Tabs (Nestable) element*

| Property | Value |
|---|---|
| `name` | tabs-nested |
| `category` | general |
| `tag` | div |
| `nestable` | true |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `direction` | direction | Direction | `flex-direction` |
| `openTabOn` | select | Open tab on | — |
| `accordionLayoutAtBreakpoint` | select | Accordion layout at breakpoint | — |
| `openTab` | text | Open tab index | — |
| `titleWidth` | number | Width | `width` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titleMargin` | spacing | Margin | `margin` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titlePadding` | spacing | Padding | `padding` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titleBackgroundColor` | color | Background | `background-color` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titleBorder` | border | Border | `border` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titleTypography` | typography | Typography | `font` on `> .tab-menu .tab-title, > .tab-content > .tab-title` |
| `titleActiveBackgroundColor` | color | Background color | `background-color` on `> .tab-menu .tab-title.brx-open, > .tab-content > .tab-title.brx-open` |
| `titleActiveBorder` | border | Border | `border` on `> .tab-menu .tab-title.brx-open, > .tab-content > .tab-title.brx-open` |
| `titleActiveTypography` | typography | Typography | `font` on `> .tab-menu .tab-title.brx-open, > .tab-content > .tab-title.brx-open` |
| `contentMargin` | spacing | Margin | `margin` on `> .tab-content` |
| `contentPadding` | spacing | Padding | `padding` on `&:not([data-brx-tabs-nested-accordion]) > .tab-content`, `padding` on `&[data-brx-tabs-nested-accordion] > .tab-content > .tab-pane` |
| `contentColor` | color | Text color | `color` on `> .tab-content` |
| `contentBackgroundColor` | color | Background color | `background-color` on `> .tab-content` |
| `contentBorder` | border | Border | `border` on `> .tab-content` |

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

# SVG Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/svg/

*Schema for Bricks SVG element*

| Property | Value |
|---|---|
| `name` | svg |
| `category` | media |
| `tag` | svg |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `source` | select | Source | — |
| `file` | svg | file | — |
| `iconSet` | icon | SVG icon | — |
| `dynamicData` | text | Dynamic data | — |
| `code` | code | Code | — |
| `height` | number | Height | `height` |
| `width` | number | Width | `width` |
| `strokeWidth` | number | Stroke width | `stroke-width` on `*` |
| `stroke` | color | Stroke color | `stroke` on `:not([stroke="none"])` |
| `fill` | color | Fill | `fill` on `:not([fill="none"])` |
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
