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