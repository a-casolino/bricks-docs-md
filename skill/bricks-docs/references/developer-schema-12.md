# Woocommerce Item Data Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-item-data/

*Schema for Bricks Woocommerce Item Data element*

| Property | Value |
|---|---|
| `name` | woocommerce-item-data |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `showLabels` | checkbox | Show labels | — |
| `labelSuffix` | text | Label suffix | — |
| `showSeparators` | checkbox | Show separators | — |
| `separatorText` | text | Separator | — |
| `layoutDirection` | direction | Direction | `flex-direction` |
| `layoutWrap` | select | layoutWrap | `flex-wrap` |
| `layoutJustifyContent` | justify-content | Justify content | `justify-content` |
| `layoutAlignItems` | align-items | Align items | `align-items` |
| `layoutRowGap` | number | Row gap | `row-gap` |
| `layoutColumnGap` | number | Column gap | `column-gap` |
| `itemDirection` | direction | Direction | `flex-direction` on `.\{$class_prefix\}__item` |
| `itemAlignItems` | align-items | Align items | `align-items` on `.\{$class_prefix\}__item` |
| `itemGap` | number | Gap | `gap` on `.\{$class_prefix\}__item` |
| `labelWidth` | number | Width | `width` on `.\{$class_prefix\}__label` |
| `labelFlexGrow` | number | Flex grow | `flex-grow` on `.\{$class_prefix\}__label` |
| `labelFlexShrink` | number | Flex shrink | `flex-shrink` on `.\{$class_prefix\}__label` |
| `valueWidth` | number | Width | `width` on `.\{$class_prefix\}__value` |
| `valueFlexGrow` | number | Flex grow | `flex-grow` on `.\{$class_prefix\}__value` |
| `valueFlexShrink` | number | Flex shrink | `flex-shrink` on `.\{$class_prefix\}__value` |
| `separatorTypography` | typography | Typography | `font` on `.\{$class_prefix\}__separator` |
| `separatorMargin` | spacing | Margin | `margin` on `.\{$class_prefix\}__separator` |
| `itemPadding` | spacing | Padding | `padding` on `.\{$class_prefix\}__item` |
| `itemBackgroundColor` | color | Background color | `background-color` on `.\{$class_prefix\}__item` |
| `itemBorder` | border | Border | `border` on `.\{$class_prefix\}__item` |
| `itemBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.\{$class_prefix\}__item` |
| `labelMargin` | spacing | Margin | `margin` on `.\{$class_prefix\}__label` |
| `labelPadding` | spacing | Padding | `padding` on `.\{$class_prefix\}__label` |
| `labelBackgroundColor` | color | Background color | `background-color` on `.\{$class_prefix\}__label` |
| `labelBorder` | border | Border | `border` on `.\{$class_prefix\}__label` |
| `labelBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.\{$class_prefix\}__label` |
| `labelTypography` | typography | Typography | `font` on `.\{$class_prefix\}__label` |
| `valueMargin` | spacing | Margin | `margin` on `.\{$class_prefix\}__value` |
| `valuePadding` | spacing | Padding | `padding` on `.\{$class_prefix\}__value` |
| `valueBackgroundColor` | color | Background color | `background-color` on `.\{$class_prefix\}__value` |
| `valueBorder` | border | Border | `border` on `.\{$class_prefix\}__value` |
| `valueBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.\{$class_prefix\}__value` |
| `valueTypography` | typography | Typography | `font` on `.\{$class_prefix\}__value` |

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

# Notice Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-notice/

*Schema for Bricks Notice element*

| Property | Value |
|---|---|
| `name` | woocommerce-notice |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `previewType` | select | Preview notice type | — |

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

# Order Item Data Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-order-item-data/

*Schema for Bricks Order item data element*

| Property | Value |
|---|---|
| `name` | woocommerce-order-item-data |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

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

# Payment Options Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-payment-options/

*Schema for Bricks Payment options element*

| Property | Value |
|---|---|
| `name` | woocommerce-payment-options |
| `category` | woocommerce_checkout |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `wrapperDirection` | direction | Direction | `flex-direction` on `.brx-payment-options__control` |
| `wrapperJustifyContent` | justify-content | Justify content | `justify-content` on `.brx-payment-options__control` |
| `wrapperAlignItems` | align-items | Align items | `align-items` on `.brx-payment-options__control` |
| `wrapperGap` | number | Gap | `gap` on `.brx-payment-options__control` |
| `optionGap` | number | Gap | `gap` on `.brx-payment-options__label-group` |
| `optionHoverBackgroundColor` | color | Hover background color | `background-color` on `.brx-payment-options__option:hover` |
| `optionCheckedBackgroundColor` | color | Background color | `background-color` on `.brx-payment-options__option:has(> input[type="radio"]:checked)` |
| `optionCheckedBorder` | border | Border | `border` on `.brx-payment-options__option:has(> input[type="radio"]:checked)` |
| `optionCheckedBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-payment-options__option:has(> input[type="radio"]:checked)` |
| `labelTypography` | typography | Typography | `font` on `.brx-payment-options__label` |
| `labelCheckedTypography` | typography | Typography | `font` on `.brx-payment-options__option > input[type="radio"]:checked ~ .brx-payment-options__option-layout .brx-payment-options__label` |
| `secondaryTypography` | typography | Typography | `font` on `.brx-payment-options__secondary-label` |
| `secondaryCheckedTypography` | typography | Typography | `font` on `.brx-payment-options__option > input[type="radio"]:checked ~ .brx-payment-options__option-layout .brx-payment-options__secondary-label` |
| `contentTypography` | typography | Typography | `font` on `.brx-payment-options__content` |
| `noticeTypography` | typography | Typography | `font` on `.brx-payment-options__empty` |
| `optionMargin` | spacing | Margin | `margin` on `.brx-payment-options__option` |
| `optionPadding` | spacing | Padding | `padding` on `.brx-payment-options__option` |
| `optionBackgroundColor` | color | Background color | `background-color` on `.brx-payment-options__option` |
| `optionBorder` | border | Border | `border` on `.brx-payment-options__option` |
| `optionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-payment-options__option` |
| `contentMargin` | spacing | Margin | `margin` on `.brx-payment-options__content` |
| `contentPadding` | spacing | Padding | `padding` on `.brx-payment-options__content` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.brx-payment-options__content` |
| `contentBorder` | border | Border | `border` on `.brx-payment-options__content` |
| `contentBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-payment-options__content` |

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

# Products Archive Description Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products-archive-description/

*Schema for Bricks Products archive description element*

| Property | Value |
|---|---|
| `name` | woocommerce-products-archive-description |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

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

# Mini Cart Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-mini-cart/

*Schema for Bricks Mini cart element*

| Property | Value |
|---|---|
| `name` | woocommerce-mini-cart |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Icon typography | `font` on `.mini-cart-link i` |
| `openMiniCartOnAddedToCart` | checkbox | Open on add to cart (AJAX) | — |
| `cartCount` | select | Visibility | `display` on `.cart-count` |
| `cartCountBackground` | color | Background color | `background-color` on `.cart-count` |
| `cartCountBorder` | border | Border | `border` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountTypography` | typography | Typography | `font` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountTransform` | transform | Transform | `transform` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountHeight` | number | Height | `height` on `.cart-count` |
| `cartCountWidth` | number | Width | `width` on `.cart-count` |
| `cartCountTop` | number | cartCountTop | `top` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountRight` | number | Right | `right` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountBottom` | number | Bottom | `bottom` on `.mini-cart-link .cart-icon .cart-count` |
| `cartCountLeft` | number | Left | `left` on `.mini-cart-link .cart-icon .cart-count` |
| `subtotalPosition` | select | Position | `flex-direction` on `.mini-cart-link` |
| `subtotalGap` | number | Gap | `gap` on `.mini-cart-link` |
| `subtotalTypography` | typography | Typography | `font` on `.mini-cart-link .cart-subtotal` |
| `hideCartDetails` | checkbox | Hide | — |
| `skipClickOutside` | checkbox | Don\ | — |
| `cartDetailsOffCanvas` | select | Off-Canvas | — |
| `cartDetailsHeight` | number | Height | `height` on `.cart-detail` |
| `cartDetailsWidth` | number | Width | `width` on `.cart-detail` |
| `cartDetailsImageWidth` | number | Image width | `width` on `.cart-detail img` |
| `cartDetailsPadding` | spacing | Padding | `padding` on `.cart-detail .widget_shopping_cart_content` |
| `cartDetailsPosition` | dimensions | Position | `—` on `.cart-detail` |
| `cartDetailsTransform` | transform | Transform | `transform` on `.cart-detail` |
| `cartDetailsBackground` | color | Background | `background-color` on `.cart-detail` |
| `cartDetailsBorder` | border | Border | `border` on `.cart-detail` |
| `cartDetailsBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.cart-detail` |
| `cartDetailsTypography` | typography | Typography | `font` on `.woocommerce-mini-cart-item a:not(.remove)` |
| `cartDetailsTypographyQuantity` | typography | Typography | `font` on `.cart-detail .woocommerce-mini-cart-item .quantity` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.cart-detail .woocommerce-mini-cart__buttons .button` |
| `buttonBorder` | border | Border | `border` on `.cart-detail .woocommerce-mini-cart__buttons .button` |
| `buttonTypography` | typography | Typography | `font` on `.cart-detail .woocommerce-mini-cart__buttons .button` |
| `cartDetailsCloseIcon` | icon | Icon | — |
| `cartDetailsCloseTypography` | typography | Typography | `font` on `.bricks-mini-cart-close > *` |
| `cartDetailsClosePosition` | dimensions | Position | `—` on `.bricks-mini-cart-close` |
| `cartDetailsClosePadding` | spacing | Padding | `padding` on `.bricks-mini-cart-close` |
| `cartDetailsCloseBackgroundColor` | color | Background color | `background-color` on `.bricks-mini-cart-close` |
| `cartDetailsCloseBorder` | border | Border | `border` on `.bricks-mini-cart-close` |

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

# Products Filter Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products-filter/

*Schema for Bricks Products filter element*

| Property | Value |
|---|---|
| `name` | woocommerce-products-filter |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `filters` | repeater | Filter type | `font` on `.filter .stars a` |
| `spacing` | number | Spacing | `gap` |
| `titleMargin` | spacing | Margin | `margin` on `.title` |
| `titlePadding` | spacing | Padding | `padding` on `.title` |
| `titleTypography` | typography | Typography | `font` on `.title .title-tag` |
| `titleBackgroundColor` | color | Background color | `background-color` on `.title` |
| `titleBorder` | border | Border | `border` on `.title` |
| `iconExpanded` | icon | Icon expanded | — |
| `iconCollapsed` | icon | Icon collapsed | — |
| `iconTypography` | typography | Icon typography | `font` on `.toggle` |
| `iconPosition` | select | Icon position | `flex-direction` on `.title` |

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

# Products Orderby Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products-orderby/

*Schema for Bricks Products orderby element*

| Property | Value |
|---|---|
| `name` | woocommerce-products-orderby |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `orderby` | select | Order by | — |

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

# Products Pagination Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products-pagination/

*Schema for Bricks Products pagination element*

| Property | Value |
|---|---|
| `name` | woocommerce-products-pagination |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `justifyContent` | align-items | Alignment | `align-self` |
| `prevIcon` | icon | Previous icon | — |
| `nextIcon` | icon | Next icon | — |
| `endSize` | number | End Size | — |
| `midSize` | number | Mid Size | — |

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

# Products Total Results Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products-total-results/

*Schema for Bricks Products total results element*

| Property | Value |
|---|---|
| `name` | woocommerce-products-total-results |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

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

# Products Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-products/

*Schema for Bricks Products element*

| Property | Value |
|---|---|
| `name` | woocommerce-products |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `columns` | number | Columns | `grid-template-columns` on `.products` |
| `gap` | number | Gap | `gap` on `.products` |
| `linkProduct` | checkbox | Link entire product | — |
| `beforeGrid` | select | Show Before Grid | — |
| `afterGrid` | select | Show After Grid | — |
| `sortbyOptions` | select | Sort by options | — |

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

# Shipping Options Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-shipping-options/

*Schema for Bricks Shipping options element*

| Property | Value |
|---|---|
| `name` | woocommerce-shipping-options |
| `category` | woocommerce_checkout |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `showPackageTitle` | checkbox | Show package title | — |
| `emptyMessage` | text | Empty message | — |
| `controlFlexDirection` | direction | Direction | `flex-direction` on `.brx-shipping-options__control` |
| `controlJustifyContent` | justify-content | Justify content | `justify-content` on `.brx-shipping-options__control` |
| `controlAlignItems` | align-items | Align items | `align-items` on `.brx-shipping-options__control` |
| `controlGap` | number | Gap | `gap` on `.brx-shipping-options__control` |
| `packageTitleTypography` | typography | Title typography | `font` on `.brx-shipping-options__package-title` |
| `packageTitleColor` | color | Title color | `color` on `.brx-shipping-options__package-title` |
| `optionGap` | number | Gap | `gap` on `.brx-shipping-options__label-group` |
| `optionHoverBackgroundColor` | color | Hover background color | `background-color` on `.brx-shipping-options__option:hover` |
| `optionCheckedBackgroundColor` | color | Background color | `background-color` |
| `optionCheckedBorder` | border | Border | `border` |
| `optionCheckedBoxShadow` | box-shadow | Box shadow | `box-shadow` |
| `labelTypography` | typography | Typography | `font` on `.brx-shipping-options__label` |
| `labelColor` | color | Color | `color` on `.brx-shipping-options__label` |
| `labelCheckedTypography` | typography | Typography | `font` |
| `labelCheckedColor` | color | Color | `color` |
| `secondaryTypography` | typography | Typography | `font` on `.brx-shipping-options__secondary-label` |
| `secondaryColor` | color | Color | `color` on `.brx-shipping-options__secondary-label` |
| `secondaryCheckedTypography` | typography | Typography | `font` |
| `secondaryCheckedColor` | color | Color | `color` |
| `packageMargin` | spacing | Margin | `margin` on `.brx-shipping-options__package` |
| `packagePadding` | spacing | Padding | `padding` on `.brx-shipping-options__package` |
| `packageBackgroundColor` | color | Background color | `background-color` on `.brx-shipping-options__package` |
| `packageBorder` | border | Border | `border` on `.brx-shipping-options__package` |
| `packageBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-shipping-options__package` |
| `optionMargin` | spacing | Margin | `margin` on `.brx-shipping-options__option` |
| `optionPadding` | spacing | Padding | `padding` on `.brx-shipping-options__option` |
| `optionBackgroundColor` | color | Background color | `background-color` on `.brx-shipping-options__option` |
| `optionBorder` | border | Border | `border` on `.brx-shipping-options__option` |
| `optionBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.brx-shipping-options__option` |

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

# WordPress Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/wordpress/

*Schema for Bricks WordPress element*

| Property | Value |
|---|---|
| `name` | wordpress |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `type` | select | Widget | — |
| `icon` | icon | Icon | — |
| `iconTypography` | typography | Icon typography | `font` on `.bricks-widget-wrapper i` |
| `showCount` | checkbox | Show count | — |
| `sortBy` | select | Sort by | — |
| `include` | select | Include | — |
| `exclude` | select | Exclude | — |
| `commentsNumber` | number | Number of comments | — |
| `postsNumber` | number | Number of posts | — |
| `direction` | direction | Direction | `flex-direction` on `&.posts a` |
| `postsDate` | checkbox | Show date | — |
| `postsFeaturedImage` | checkbox | Show featured image | — |
| `postsFeaturedImageSize` | select | Featured image sizes | — |
| `postsImageWidth` | text | Featured image width | `width` on `img` |
| `postsImageHeight` | text | Featured image height | `height` on `img` |
| `postsTitleTypography` | typography | Post title typography | `font` on `.post-title` |
| `postsMetaTypography` | typography | Post meta typography | `font` on `.post-meta` |
| `taxonomy` | select | Taxonomy | — |
| `title` | text | Title | — |
| `titletag` | select | HTML tag | — |
| `titleBorder` | border | Border | `font` on `.bricks-widget-title` |
| `titleTypography` | typography | Typography | `font` on `.bricks-widget-title` |

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

# WooCommerce Template Hook Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-template-hook/

*Schema for Bricks WooCommerce Template Hook element*

| Property | Value |
|---|---|
| `name` | woocommerce-template-hook |
| `category` | woocommerce |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `template` | select | Template | — |
| `singleProductHook` | select | Hook | — |
| `shopHook` | select | Hook | — |
| `showTips` | checkbox | Show tips | — |

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
