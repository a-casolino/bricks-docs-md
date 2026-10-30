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
| `radioCheckedColor` | color | Color | `background-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before`, `border-color` on `ul.woocommerce-PaymentMethods .woocommerce-PaymentMethod input.input-radio:checked + label::before` |
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

# Account - Edit Address Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-edit-address/

*Schema for Bricks Account - Edit address element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-edit-address |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `titleHide` | checkbox | Hide | `display` on `> form > h2` |
| `titleMargin` | spacing | Margin | `margin` on `> form > h2` |
| `titlePadding` | spacing | Padding | `padding` on `> form > h2` |
| `titleBackgroundColor` | color | Background color | `background-color` on `> form > h2` |
| `titleBorder` | border | Border | `border` on `> form > h2` |
| `titleBoxShadow` | box-shadow | Box shadow | `box-shadow` on `> form > h2` |
| `titleTypography` | typography | Typography | `font` on `> form > h2` |
| `labelTypography` | typography | Label typography | `font` on `label[for]` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder`, `font` on `select` |
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

# Account - Login Form Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-login/

*Schema for Bricks Account - Login form element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-login |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `rememberMeDisable` | checkbox | Disable | — |
| `rememberMeTypography` | typography | Typography | `font` on `.woocommerce-form-login__rememberme` |
| `lostPasswordDisable` | checkbox | Disable | — |
| `lostPasswordTypography` | typography | Typography | `font` on `.woocommerce-LostPassword a` |
| `fieldsAlignItems` | align-items | Align items | `align-items` |
| `fieldsWidth` | number | Width | `width` on `.password-input, .woocommerce-Input` |
| `fieldsGap` | number | Gap | `gap` |
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

# Account - Lost Password Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-lost-password/

*Schema for Bricks Account - Lost password element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-lost-password |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `messageDisable` | checkbox | Disable | `display` on `form > p:first-child` |
| `messageTypography` | typography | Typography | `font` on `form > p:first-child` |
| `fieldsAlignItems` | align-items | Align items | `align-items` |
| `fieldsWidth` | number | Width | `width` on `.password-input, .woocommerce-Input` |
| `fieldsGap` | number | Gap | `gap` |
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

# Account - Register Form Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-register/

*Schema for Bricks Account - Register form element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-register |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `generatePasswordTypography` | typography | Typography | `font` on `.generate-password-text` |
| `privacyPolicyTypography` | typography | Typography | `font` on `.woocommerce-privacy-policy-text` |
| `privacyPolicyLink` | typography | Link | `font` on `.woocommerce-privacy-policy-text a` |
| `fieldsAlignItems` | align-items | Align items | `align-items` |
| `fieldsWidth` | number | Width | `width` on `.password-input, .woocommerce-Input` |
| `fieldsGap` | number | Gap | `gap` |
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

# Account - Reset Password Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/woocommerce-account-form-reset-password/

*Schema for Bricks Account - Reset password element*

| Property | Value |
|---|---|
| `name` | woocommerce-account-form-reset-password |
| `category` | woocommerce_account |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `messageDisable` | checkbox | Disable | `display` on `form > p:first-child` |
| `messageTypography` | typography | Typography | `font` on `form > p:first-child` |
| `fieldsAlignItems` | align-items | Align items | `align-items` |
| `fieldsWidth` | number | Width | `width` on `.password-input, .woocommerce-Input` |
| `fieldsGap` | number | Gap | `gap` |
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
