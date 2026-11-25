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

# Checkbox Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/checkbox/

*Value schema for checkbox control type*

---

# Button Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/button/

*UI-only control, no stored value*

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

*Value schema for dimensions control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `top` | string | Top spacing value with unit |
| `right` | string | Right spacing value with unit |
| `bottom` | string | Bottom spacing value with unit |
| `left` | string | Left spacing value with unit |

---

# Editor Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/editor/

*Rich text/HTML content*

---

# Direction Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/direction/

*Value schema for direction control type*

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

# Filter Definition Manager Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/filter-definition-manager/

*Global filter ID, or an empty string for a local filter*

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

# Justify Content Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/justify-content/

*Value schema for justify-content control type*

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

*Element ID of the target query loop*

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

*Selected option key*

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

# Text Shadow Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text-shadow/

*Value schema for text-shadow control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `values` | object | — |
| `color` | any | Color value in various formats |

---

# Text Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/text/

*Value schema for text control type*

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

# Textarea Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/textarea/

*Value schema for textarea control type*

---

# Typography Control Schema

Source: https://academy.bricksbuilder.io/developer/schema/controls/typography/

*Value schema for typography control type*

## Properties

| Property | Type | Description |
|---|---|---|
| `font-family` | string | — |
| `fallback` | string | Font stack appended to font-family, e.g. "Arial, sans-serif" |
| `font-size` | string | — |
| `font-weight` | string \| integer | — |
| `font-style` | string | One of: `normal`, `italic`, `oblique` |
| `line-height` | string | — |
| `letter-spacing` | string | — |
| `text-align` | string | One of: `left`, `center`, `right`, `justify` |
| `text-transform` | string | One of: `none`, `uppercase`, `lowercase`, `capitalize` |
| `text-decoration` | string | — |
| `color` | any | Color value in various formats |
| `font-variants` | array | Font variants to load (theme style Body and All headings typography only). Not output as CSS. |
| `font-variation-settings` | string | — |
| `white-space` | string | — |
| `text-wrap` | string | — |
| `text-shadow` | object | Text shadow settings |

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

# Template Settings Schema

Source: https://academy.bricksbuilder.io/developer/schema/settings/template/

*Schema for Bricks template settings controls*

## Controls

| Key | Type | Label |
|---|---|---|
| `footerReveal` | checkbox | Reveal effect |
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
| `searchCriteriaCustom` | checkbox | Custom search criteria |
| `searchPostFields` | checkbox | Search post fields |
| `searchPostMatchAnyWord` | checkbox | Match any word |
| `searchPostMeta` | checkbox | Search post meta fields |
| `searchPostMetaKeys` | repeater | Post meta keys |
| `searchPostQuery` | repeater | Post fields |
| `searchPostTaxonomies` | repeater | Taxonomies |
| `searchPostTerms` | checkbox | Search post terms |
| `templateConditions` | repeater | Archive type |
| `templatePreviewAuthor` | select | Author |
| `templatePreviewPostId` | select | Single |
| `templatePreviewPostType` | select | Post type |
| `templatePreviewSearchTerm` | text | Search term |
| `templatePreviewTerm` | select | Term |
| `templatePreviewType` | select | Content type |
| `template_interactions` | repeater | Interactions |
| `useWeightScore` | checkbox | Use weight score |

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
| `adaptiveHeight` | checkbox | Adaptive height | — |
| `height` | number | Height | `height` on `.image`, `height` on `.overlay-wrapper` |
| `gutter` | number | Spacing (px) | — |
| `initialSlide` | number | Initial slide | — |
| `slidesToShow` | number | Items to show | — |
| `slidesToScroll` | number | Items to scroll | — |
| `effect` | select | Effect | — |
| `alignItems` | align-items | Align items | `align-items` on `.swiper-wrapper` |
| `infinite` | checkbox | Loop | — |
| `centerMode` | checkbox | Center mode | — |
| `disableLazyLoad` | checkbox | Disable lazy load | — |
| `autoplay` | checkbox | Autoplay | — |
| `pauseOnHover` | checkbox | Pause on hover | — |
| `stopOnLastSlide` | checkbox | Stop on last slide | — |
| `autoplaySpeed` | number | Autoplay delay in ms | — |
| `speed` | number | Animation speed in ms | — |
| `imageDisable` | checkbox | Hide image | — |
| `imageSize` | select | Image size | — |
| `imageLightbox` | checkbox | Link to lightbox | — |
| `imageLightboxSize` | select | Image size | — |
| `lightboxImageClick` | select | Image click action | — |
| `lightboxAnimationType` | select | Animation | — |
| `lightboxCaption` | checkbox | Caption | — |
| `lightboxCaptionPosition` | select | Caption position | — |
| `lightboxThumbnails` | checkbox | Thumbnail navigation | — |
| `lightboxThumbnailSize` | number | Thumbnail size | — |
| `lightboxPadding` | dimensions | Padding | — |
| `lightboxId` | text | Lightbox | — |
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

# Div Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/div/

*Schema for Bricks Div element*

| Property | Value |
|---|---|
| `name` | div |
| `category` | layout |
| `tag` | div |
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
