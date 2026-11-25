# Tabs Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/tabs/

*Schema for Bricks Tabs element*

| Property | Value |
|---|---|
| `name` | tabs |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tabs` | repeater | Icon | — |
| `layout` | select | Layout | — |
| `accordionLayoutAtBreakpoint` | select | Accordion layout at breakpoint | — |
| `openTabOn` | select | Open tab on | — |
| `openTab` | text | Open tab index | — |
| `titleGrow` | checkbox | Stretch | `flex-grow` on `.tab-title` |
| `titleHorizontal` | justify-content | Align | `justify-content` on `.tab-menu` |
| `titlePadding` | spacing | Padding | `padding` on `.tab-title` |
| `titleBackgroundColor` | color | Background | `background-color` on `.tab-title` |
| `titleBorder` | border | Border | `border` on `.tab-title` |
| `titleTypography` | typography | Typography | `font` on `.tab-title` |
| `titleActiveBackgroundColor` | color | Active background | `background-color` on `.tab-title.brx-open` |
| `titleActiveBorder` | border | Active border | `border` on `.tab-title.brx-open` |
| `titleActiveTypography` | typography | Active typography | `font` on `.tab-title.brx-open` |
| `contentPadding` | spacing | Padding | `padding` on `.tab-content .tab-pane` |
| `contentTextAlign` | text-align | Text align | `text-align` on `.tab-content` |
| `contentColor` | color | Text color | `color` on `.tab-content` |
| `contentBackgroundColor` | color | Background color | `background-color` on `.tab-content` |
| `contentBorder` | border | Border | `border` on `.tab-content` |

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

# Team Members Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/team-members/

*Schema for Bricks Team members element*

| Property | Value |
|---|---|
| `name` | team-members |
| `category` | general |
| `tag` | ul |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `items` | repeater | Image | — |
| `membersPerRow` | number | Columns | `grid-template-columns`, `grid-auto-flow` |
| `memberGutter` | number | Gap | `gap` |
| `contentBackgroundColor` | color | Background | `background-color` on `.member` |
| `contentBorder` | border | Border | `border` on `.member` |
| `contentBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.member` |
| `imagePosition` | select | Image position | — |
| `imageRatio` | text | Image ratio | `aspect-ratio` on `.image` |
| `imageWidth` | number | Width | `width` on `.image` |
| `imageMargin` | spacing | Margin | `margin` on `.image` |
| `imageBorder` | border | Border | `border` on `.image` |
| `contentPadding` | spacing | Padding | `padding` on `.content` |
| `contentAlign` | text-align | Text align | `text-align` on `.content` |
| `memberTitleTag` | select | Title tag | — |
| `memberTitleTypography` | typography | Title typography | `font` on `.title` |
| `memberSubtitleTypography` | typography | Subtitle typography | `font` on `.subtitle` |
| `memberDescriptionTypography` | typography | Description typography | `font` on `.description` |

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

# Testimonials Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/testimonials/

*Schema for Bricks Testimonials element*

| Property | Value |
|---|---|
| `name` | testimonials |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `items` | repeater | Content | — |
| `initialSlide` | number | Initial slide | — |
| `slidesToShow` | number | Items to show | — |
| `slidesToScroll` | number | Items to scroll | — |
| `gutter` | number | Spacing (px) | — |
| `alignItems` | justify-content | Align items | `justify-content` on `.repeater-item` |
| `textAlign` | text-align | Text align | `text-align` |
| `effect` | select | Effect | — |
| `infinite` | checkbox | Loop | — |
| `random` | checkbox | Random order | — |
| `centerMode` | checkbox | Center mode | — |
| `disableLazyLoad` | checkbox | Disable lazy load | — |
| `autoplay` | checkbox | Autoplay | — |
| `pauseOnHover` | checkbox | Pause on hover | — |
| `autoplaySpeed` | number | Autoplay delay in ms | — |
| `speed` | number | Animation speed in ms | — |
| `imageAlign` | align-items | Image align | `align-items` on `.repeater-item` |
| `imagePosition` | select | Image position | — |
| `imageSize` | number | Image size | `width` on `.image`, `height` on `.image` |
| `imageBorder` | border | Image border | `border` on `.image` |
| `imageBoxShadow` | box-shadow | Image box shadow | `box-shadow` on `.image` |
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
| `nextArrow` | icon | Next arrow | `—` on `.bricks-swiper-button-next > *` |
| `nextArrowTop` | number | Top | `top` on `.bricks-swiper-button-next` |
| `nextArrowRight` | number | Right | `right` on `.bricks-swiper-button-next` |
| `nextArrowBottom` | number | Bottom | `bottom` on `.bricks-swiper-button-next` |
| `nextArrowLeft` | number | Left | `left` on `.bricks-swiper-button-next` |
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
| `typographyContent` | typography | Testimonial | `font` on `.testimonial-content-wrapper` |
| `typographyName` | typography | Name | `font` on `.testimonial-name` |
| `typographyTitle` | typography | Title | `font` on `.testimonial-title` |

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

# Template Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/template/

*Schema for Bricks Template element*

| Property | Value |
|---|---|
| `name` | template |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `template` | select | Template | — |
| `noRoot` | checkbox | Render without wrapper | — |

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

# Basic Text Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/text-basic/

*Schema for Bricks Basic Text element*

| Property | Value |
|---|---|
| `name` | text-basic |
| `category` | basic |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `text` | textarea | text | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |
| `link` | link | Link to | — |
| `wordsLimit` | number | Words limit | — |
| `readMore` | text | Read more | — |

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

# Text Link Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/text-link/

*Schema for Bricks Text link element*

| Property | Value |
|---|---|
| `name` | text-link |
| `category` | basic |
| `tag` | a |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `text` | text | text | — |
| `link` | link | Link to | — |
| `icon` | icon | Icon | `—` on `&\{pseudo\} .icon > svg` |
| `iconSize` | number | Size | `font-size` on `&\{pseudo\} .icon > i`, `width` on `&\{pseudo\} .icon > svg`, `height` on `&\{pseudo\} .icon > svg` |
| `iconWidth` | number | Width | `width` on `&\{pseudo\} .icon` |
| `iconHeight` | number | Height | `height` on `&\{pseudo\} .icon` |
| `iconColor` | color | Color | `color` on `&\{pseudo\} .icon`, `fill` on `&\{pseudo\} .icon` |
| `iconBackground` | color | Background color | `background-color` on `&\{pseudo\} .icon` |
| `iconBorder` | border | Border | `border` on `&\{pseudo\} .icon`, `overflow` on `&\{pseudo\} .icon` |
| `iconPosition` | select | Position | `flex-direction` |
| `gap` | number | Gap | `gap` |

## Bricks 2.4.3 icon control visibility

The `iconSize`, `iconWidth`, `iconHeight`, `iconBackground` and `iconBorder` controls are available for both font icons and SVG icons. The `iconColor` control remains conditional on a font icon. The generated schema records conditional controls with `hasRequired`; it does not include their complete Builder visibility rules.

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

# Rich Text Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/text/

*Schema for Bricks Rich text element*

| Property | Value |
|---|---|
| `name` | text |
| `category` | basic |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `text` | editor | text | — |
| `type` | select | Type | — |
| `style` | select | Style | — |
| `wordsLimit` | number | Words limit | — |
| `readMore` | text | Read more | — |

## Inherited CSS controls

Shared CSS controls available on all elements. Keys are prefixed with `_` and support responsive/pseudo-class variants via colon syntax (e.g. `_typography:tablet_portrait:hover`).

| Key | Type | Label | CSS |
|---|---|---|---|
| `_typography` | typography | _typography | `font` |
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

# Toggle - Mode Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/toggle-mode/

*Schema for Bricks Toggle - Mode element*

| Property | Value |
|---|---|
| `name` | toggle-mode |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `icon` | icon | Icon | — |
| `iconColor` | color | Color | `color` on `.toggle.light > *`, `fill` on `.toggle.light > *` |
| `iconSize` | number | Size | `font-size` on `.toggle.light > *` |
| `iconDark` | icon | Icon | — |
| `iconDarkColor` | color | Color | `color` on `.toggle.dark > *`, `fill` on `.toggle.dark > *` |
| `iconDarkSize` | number | Size | `font-size` on `.toggle.dark > *` |
| `ariaLabel` | text | aria-label | — |

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

# Toggle Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/toggle/

*Schema for Bricks Toggle element*

| Property | Value |
|---|---|
| `name` | toggle |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `icon` | icon | Icon | — |
| `iconColor` | color | Color | `color`, `fill` |
| `iconSize` | number | Size | `font-size` |
| `animation` | select | Animation | — |
| `ariaLabel` | text | aria-label | — |
| `toggleSelector` | text | CSS selector | — |
| `toggleAttribute` | text | Attribute | — |
| `toggleValue` | text | Value | — |
| `barScale` | number | Scale | `--brxe-toggle-scale` |
| `barHeight` | number | Height | `--brxe-toggle-bar-height` on `.brxa-inner` |
| `barRadius` | number | Radius | `--brxe-toggle-bar-radius` on `.brxa-inner` |
| `barColor` | color | Color | `color` on `.brxa-wrap` |

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

# Video Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/video/

*Schema for Bricks Video element*

| Property | Value |
|---|---|
| `name` | video |
| `category` | basic |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `videoType` | select | Source | — |
| `iframeTitle` | text | Iframe title | — |
| `aspectRatio` | select | Aspect ratio | `aspect-ratio` |
| `objectFit` | select | Object fit | `object-fit` on `video` |
| `youTubeId` | text | YouTube video ID/URL | — |
| `youtubeAutoplay` | checkbox | Autoplay | — |
| `youtubeControls` | checkbox | Controls | — |
| `youtubeLoop` | checkbox | Loop | — |
| `youtubeMute` | checkbox | Mute | — |
| `youtubeRel` | checkbox | Related videos from other channels | — |
| `youtubeDoNotTrack` | checkbox | Do not track | — |
| `youtubeStart` | number | Start time [s] | — |
| `youtubeEnd` | number | End time [s] | — |
| `youtubeDisableFullscreenButton` | checkbox | Disable fullscreen button | — |
| `youtubeDisableKeyboard` | checkbox | Disable keyboard controls | — |
| `youtubeLanguage` | text | Interface language | — |
| `youtubeCcLang` | text | Captions language | — |
| `youtubeCcLoad` | checkbox | Show captions by default | — |
| `youtubeColor` | select | Progress bar color | — |
| `youtubeHideAnnotationsByDefault` | checkbox | Hide video annotations by default | — |
| `youtubePlaysinline` | checkbox | Play inline | — |
| `vimeoId` | text | Vimeo video ID/URL | — |
| `vimeoHash` | text | Vimeo privacy hash | — |
| `vimeoAutoplay` | checkbox | Autoplay | — |
| `vimeoLoop` | checkbox | Loop | — |
| `vimeoMute` | checkbox | Mute | — |
| `vimeoByline` | checkbox | Byline | — |
| `vimeoTitle` | checkbox | Title | — |
| `vimeoPortrait` | checkbox | User portrait | — |
| `vimeoDoNotTrack` | checkbox | Do not track | — |
| `vimeoColor` | color | Color | — |
| `previewImage` | select | previewImage | — |
| `previewImageCustom` | image | previewImageCustom | — |
| `previewImageSize` | select | Image size | — |
| `media` | video | Media | — |
| `fileUrl` | text | Video file URL | — |
| `useDynamicData` | text | useDynamicData | — |
| `filePreload` | select | Preload | — |
| `fileAutoplay` | checkbox | Autoplay | — |
| `fileLoop` | checkbox | Loop | — |
| `fileMute` | checkbox | Mute | — |
| `fileInline` | checkbox | Play inline | — |
| `fileControls` | checkbox | Controls | — |
| `fileControlNoDownload` | checkbox | Disable | — |
| `fileControlNoFullscreen` | checkbox | Disable | — |
| `fileControlNoRemotePlayback` | checkbox | Disable | — |
| `videoPoster` | image | Poster | — |
| `overlay` | background | Overlay | `background` on `.bricks-video-overlay` |
| `overlayIcon` | icon | Icon | — |
| `overlayAriaLabel` | text | aria-label | — |
| `overlayIconTypography` | typography | Icon typography | `font` on `.bricks-video-overlay-icon` |
| `overlayIconPadding` | spacing | Icon padding | `padding` on `.bricks-video-overlay-icon` |
| `overlayIconBackgroundColor` | color | Icon background color | `background-color` on `.bricks-video-overlay-icon` |
| `overlayIconBorder` | border | Icon border | `border` on `.bricks-video-overlay-icon` |
| `overlayIconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `.bricks-video-overlay-icon` |

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

# Account - Downloads Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-downloads/

*Schema for Bricks Account - Downloads element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-downloads |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `tableBackgroundColor` | color | Background color | `background-color` on `.woocommerce-table--order-downloads` |
| `tableBorder` | border | Border | `border` on `.woocommerce-table--order-downloads` |
| `tableBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-table--order-downloads` |
| `tableTypography` | typography | Typography | `font` on `.woocommerce-table--order-downloads` |
| `theadPadding` | spacing | Padding | `padding` on `thead th, tbody td::before` |
| `theadBackgroundColor` | color | Background color | `background-color` on `thead th, tbody td::before` |
| `theadBorder` | border | Border | `border` on `thead th, tbody td::before` |
| `theadTypography` | typography | Typography | `font` on `thead th, tbody td::before` |
| `tbodyPadding` | spacing | Padding | `padding` on `tbody td` |
| `tbodyBackgroundColor` | color | Background color | `background-color` on `tbody td` |
| `tbodyBorder` | border | Border | `border` on `tbody td` |
| `tbodyTypography` | typography | Typography | `font` on `tbody td` |
| `tbodyLinksMargin` | spacing | Margin | `margin` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksPadding` | spacing | Padding | `padding` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBackgroundColor` | color | Background color | `background-color` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBorder` | border | Border | `border` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksBoxShadow` | box-shadow | Box shadow | `box-shadow` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `tbodyLinksTypography` | typography | Typography | `font` on `tbody td a:not(.woocommerce-MyAccount-downloads-file.button)` |
| `buttonPadding` | spacing | Padding | `padding` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBorder` | border | Border | `border` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-MyAccount-downloads-file.button` |
| `buttonTypography` | typography | Typography | `font` on `.woocommerce-MyAccount-downloads-file.button` |

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

# Account - Addresses Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-addresses/

*Schema for Bricks Account - Addresses element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-addresses |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `addressesDirection` | direction | Direction | `flex-direction` on `.woocommerce-Addresses` |
| `addressesGap` | number | Gap | `gap` on `.woocommerce-Addresses` |
| `wrapperMargin` | spacing | Margin | `margin` on `.woocommerce-Address` |
| `wrapperPadding` | spacing | Padding | `padding` on `.woocommerce-Address` |
| `wrapperBackgroundColor` | color | Background color | `background-color` on `.woocommerce-Address` |
| `wrapperBorder` | border | Border | `border` on `.woocommerce-Address` |
| `wrapperBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-Address` |
| `wrapperTypography` | typography | Typography | `font` on `.woocommerce-Address` |
| `titleMargin` | spacing | Margin | `margin` on `.woocommerce-Address-title h2` |
| `titlePadding` | spacing | Padding | `padding` on `.woocommerce-Address-title h2` |
| `titleBackgroundColor` | color | Background color | `background-color` on `.woocommerce-Address-title h2` |
| `titleBorder` | border | Border | `border` on `.woocommerce-Address-title h2` |
| `titleBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-Address-title h2` |
| `titleTypography` | typography | Typography | `font` on `.woocommerce-Address-title h2` |
| `editLinkMargin` | spacing | Margin | `margin` on `.edit` |
| `editLinkPadding` | spacing | Padding | `padding` on `.edit` |
| `editLinkBackgroundColor` | color | Background color | `background-color` on `.edit` |
| `editLinkBorder` | border | Border | `border` on `.edit` |
| `editLinkBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.edit` |
| `editLinkTypography` | typography | Typography | `font` on `.edit` |
| `addressMargin` | spacing | Margin | `margin` on `address` |
| `addressPadding` | spacing | Padding | `padding` on `address` |
| `addressBackgroundColor` | color | Background color | `background-color` on `address` |
| `addressBorder` | border | Border | `border` on `address` |
| `addressBoxShadow` | box-shadow | Box shadow | `box-shadow` on `address` |
| `addressTypography` | typography | Typography | `font` on `address` |

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

# Account - Add Payment Method Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-add-payment-method/

*Schema for Bricks Account - Add payment method element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-add-payment-method |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `wrapperMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods` |
| `wrapperPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods` |
| `wrapperBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods` |
| `wrapperBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods` |
| `wrapperBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods` |
| `wrapperTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods` |
| `listMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods` |
| `listPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods` |
| `listBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods` |
| `listBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods` |
| `listBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods` |
| `listTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods` |
| `itemMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `itemTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod` |
| `labelMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `labelTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods li.woocommerce-PaymentMethod label` |
| `radioCheckedColor` | color | Color | `background-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before`, `border-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before` |
| `paymentBoxMargin` | spacing | Margin | `margin` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxPadding` | spacing | Padding | `padding` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBackgroundColor` | color | Background color | `background-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBorder` | border | Border | `border` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxBoxShadow` | box-shadow | Box shadow | `box-shadow` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `paymentBoxTypography` | typography | Typography | `font` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentBox` |
| `buttonMargin` | spacing | Margin | `margin` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonPadding` | spacing | Padding | `padding` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBackgroundColor` | color | Background color | `background-color` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBorder` | border | Border | `border` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.woocommerce-Payment .form-row .woocommerce-Button` |
| `buttonTypography` | typography | Typography | `font` on `.woocommerce-Payment .form-row .woocommerce-Button` |

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

# Account Edit Account Form Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-edit-account-form/

*Schema for Bricks Account edit account form element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-edit-account-form |
| `category` | woocommerce_account |
| `tag` | form |
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

# Account - Edit Account Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-edit-account/

*Schema for Bricks Account - Edit account element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-edit-account |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `labelTypography` | typography | Label typography | `font` on `label[for]` |
| `fieldsInputMargin` | spacing | Margin | `margin` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputPadding` | spacing | Padding | `padding` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBackgroundColor` | color | Background color | `background-color` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBorder` | border | Border | `border` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputBoxShadow` | box-shadow | Box shadow | `box-shadow` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `fieldsInputTypography` | typography | Typography | `font` on `input, .woocommerce-Input, .select2-selection.select2-selection--single` |
| `submitButtonWidth` | number | Width | `width` on `button[type=submit]` |
| `submitButtonMargin` | spacing | Margin | `margin` on `button[type=submit]` |
| `submitButtonPadding` | spacing | Padding | `padding` on `button[type=submit]` |
| `submitButtonBackgroundColor` | color | Background color | `background-color` on `button[type=submit]` |
| `submitButtonBorder` | border | Border | `border` on `button[type=submit]` |
| `submitButtonBoxShadow` | box-shadow | Box shadow | `box-shadow` on `button[type=submit]` |
| `submitButtonTypography` | typography | Typography | `font` on `button[type=submit]` |
| `fieldsetGap` | number | Gap | `gap` on `fieldset` |
| `fieldsetMargin` | spacing | Margin | `margin` on `fieldset` |
| `fieldsetPadding` | spacing | Padding | `padding` on `fieldset` |
| `fieldsetBackgroundColor` | color | Background color | `background-color` on `fieldset` |
| `fieldsetBorder` | border | Border | `border` on `fieldset` |
| `fieldsetBoxShadow` | box-shadow | Box shadow | `box-shadow` on `fieldset` |
| `fieldsetTypography` | typography | Typography | `font` on `fieldset` |

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

# Account Edit Address Form Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-edit-address-form/

*Schema for Bricks Account edit address form element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-edit-address-form |
| `category` | woocommerce_account |
| `tag` | form |
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
