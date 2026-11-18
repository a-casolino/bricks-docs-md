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