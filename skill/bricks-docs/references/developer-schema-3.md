# Form Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/form/

*Schema for Bricks Form element*

| Property | Value |
|---|---|
| `name` | form |
| `category` | general |
| `tag` | form |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `fields` | repeater | Set options as %s | `font` on `.password-toggle .show-password i` |
| `requiredAsterisk` | checkbox | Show required asterisk | — |
| `disableRequiredAsteriskInPlaceholder` | checkbox | Disable required asterisk in placeholder | — |
| `showLabels` | checkbox | Show labels | — |
| `labelTypography` | typography | Label typography | `font` on `label`, `font` on `.label` |
| `placeholderTypography` | typography | Placeholder typography | `font` on `::placeholder`, `font` on `select` |
| `disableFormValidationOn` | select | Disable form validation | — |
| `disableBrowserValidation` | checkbox | Don\ | — |
| `validateAllFieldsOnSubmit` | checkbox | Validate all fields on submit | — |
| `fieldMargin` | spacing | Spacing | `padding` on `.form-group:not(.submit-button-wrapper):not(.message):not(.captcha)` |
| `fieldPadding` | spacing | Padding | `padding` on `.form-group input`, `padding` on `.flatpickr`, `padding` on `select`, `padding` on `textarea`, `padding` on `.form-field-richtext + .tox-tinymce .tox-edit-area__iframe` |
| `horizontalAlignFields` | justify-content | Alignment | `justify-content` |
| `fieldBackgroundColor` | color | Background color | `background-color` on `.form-group input`, `background-color` on `.flatpickr`, `background-color` on `select`, `background-color` on `textarea`, `background-color` on `.form-field-richtext + .tox-tinymce` |
| `fieldBorder` | border | Border | `border` on `.form-group input`, `border` on `.flatpickr`, `border` on `select`, `border` on `textarea`, `border` on `.form-field-richtext + .tox-tinymce`, `border` on `.bricks-button:not([type=submit])`, `border` on `.choose-files` |
| `fieldTypography` | typography | Typography | `font` on `.form-group input`, `font` on `select`, `font` on `textarea` |
| `submitButtonText` | text | Text | — |
| `submitButtonSize` | select | Size | — |
| `submitButtonStyle` | select | Style | — |
| `submitButtonWidth` | number | Width | `width` on `.submit-button-wrapper` |
| `submitButtonMargin` | spacing | Margin | `margin` on `.submit-button-wrapper` |
| `submitButtonTypography` | typography | Typography | `font` on `.bricks-button` |
| `submitButtonBackgroundColor` | color | Background | `background-color` on `.bricks-button` |
| `submitButtonBorder` | border | Border | `border` on `button[type=submit].bricks-button` |
| `submitButtonIcon` | icon | Icon | `—` on `button[type=submit] svg` |
| `submitButtonAriaLabel` | text | aria-label | — |
| `submitButtonIconPosition` | select | Icon position | — |
| `actions` | select | Actions after successful form submit | — |
| `actionConditions` | repeater | Action conditions | — |
| `successMessage` | text | Success message | — |
| `noticeCloseAfter` | number | Close after | — |
| `noticeCloseButton` | checkbox | Close button | — |
| `emailSubject` | text | Subject | — |
| `emailTo` | select | Send to email address | — |
| `emailToCustom` | text | Send to custom email address | — |
| `emailBcc` | text | BCC email address | — |
| `fromEmail` | text | From email address | — |
| `fromName` | text | From name | — |
| `replyToEmail` | text | Reply to email address | — |
| `emailContent` | textarea | Email content | — |
| `emailErrorMessage` | text | Error message | — |
| `htmlEmail` | checkbox | HTML email | — |
| `webhooks` | repeater | Endpoints | — |
| `webhookMaxSize` | number | Max payload size | — |
| `webhookRateLimit` | checkbox | Rate limiting | — |
| `webhookRateLimitRequests` | number | Max requests per hour | — |
| `webhookErrorIgnore` | checkbox | Continue on error | — |
| `webhookErrorMessage` | text | Error message | — |
| `confirmationEmailSubject` | text | Subject | — |
| `confirmationEmailTo` | text | Send to email address | — |
| `confirmationFromEmail` | text | From email address | — |
| `confirmationFromName` | text | From name | — |
| `confirmationReplyToEmail` | text | Reply to email address | — |
| `confirmationEmailContent` | textarea | Email content | — |
| `confirmationEmailHTML` | checkbox | HTML email | — |
| `redirectAdminUrl` | checkbox | Redirect to admin area | — |
| `redirect` | text | Custom redirect URL | — |
| `redirectTimeout` | number | Redirect after (ms) | — |
| `mailchimpDoubleOptIn` | checkbox | Double opt-in | — |
| `mailchimpList` | select | List | — |
| `mailchimpGroups` | select | Groups | — |
| `mailchimpEmail` | select | Field | — |
| `mailchimpFirstName` | select | First name | — |
| `mailchimpLastName` | select | Last name | — |
| `mailchimpPendingMessage` | text | Pending message | — |
| `mailchimpErrorMessage` | text | Error message | — |
| `sendgridList` | select | List | — |
| `sendgridEmail` | select | Field | — |
| `sendgridFirstName` | select | Field | — |
| `sendgridLastName` | select | Field | — |
| `sendgridPendingMessage` | text | Pending message | — |
| `sendgridErrorMessage` | text | Error message | — |
| `loginName` | select | Field | — |
| `loginPassword` | select | Field | — |
| `loginRemember` | select | Field | — |
| `loginErrorMessage` | text | Error message | — |
| `registrationEmail` | select | Field | — |
| `registrationPassword` | select | Field | — |
| `registrationPasswordMinLength` | number | Password min. length | — |
| `registrationUserName` | select | Field | — |
| `registrationFirstName` | select | Field | — |
| `registrationLastName` | select | Field | — |
| `registrationRole` | select | Role | — |
| `registrationAutoLogin` | checkbox | Auto log in user | — |
| `registrationWPNotification` | checkbox | Send WordPress notification | — |
| `lostPasswordEmailUsername` | select | Field | — |
| `resetPasswordNew` | select | Field | — |
| `createPostType` | select | Post type | — |
| `createPostErrorMessage` | text | Error message | — |
| `createPostDisableCapabilityCheck` | checkbox | Disable capability checks | — |
| `createPostTitle` | select | Post title | — |
| `createPostContent` | select | Post content | — |
| `createPostExcerpt` | select | Post excerpt | — |
| `createPostFeaturedImage` | select | Featured image | — |
| `createPostStatus` | select | Post status | — |
| `createPostMeta` | repeater | Post meta | — |
| `createPostTaxonomies` | repeater | Taxonomies | — |
| `updatePostId` | select | Post to update | — |
| `updatePostErrorMessage` | text | Error message | — |
| `updatePostDisableCapabilityCheck` | checkbox | Disable capability checks | — |
| `updatePostTitle` | select | Post title | — |
| `updatePostContent` | select | Post content | — |
| `updatePostExcerpt` | select | Post excerpt | — |
| `updatePostFeaturedImage` | select | Featured image | — |
| `updatePostStatus` | select | Post status | — |
| `updatePostMeta` | repeater | Post meta | — |
| `updatePostTaxonomies` | repeater | Taxonomies | — |
| `enableRecaptcha` | checkbox | reCAPTCHA (Google) | — |
| `enableTurnstile` | checkbox | Turnstile (Cloudflare) | — |
| `turnstileSize` | select | Turnstile:  | — |
| `turnstileTheme` | select | Turnstile:  | — |
| `turnstileInitialization` | select | Turnstile:  | — |
| `turnstileViewportDistance` | number | Viewport distance | — |
| `turnstileExecution` | select | Turnstile:  | — |
| `turnstileAppearance` | select | Turnstile:  | — |
| `turnstileLabel` | text | Turnstile:  | — |
| `enableHCaptcha` | select | hCaptcha | — |
| `hCaptchaSize` | select | hCaptcha:  | — |
| `hCaptchaTheme` | select | hCaptcha:  | — |
| `submissionFormName` | text | Form name | — |
| `submissionSaveIp` | checkbox | Save IP address | — |
| `submissionMaxEntries` | number | Max. entries | — |
| `submissionMaxEntriesErrorMessage` | text | Error message | — |
| `submissionDupEntries` | repeater | Compare with | — |
| `submissionDupEntriesErrorMessage` | text | Error message | — |
| `passwordProtectionPassword` | select | Field | — |
| `passwordProtectionErrorMessage` | text | Error message | — |

## Bricks 2.4.3 registration roles

The `registrationRole` options exclude roles with administrative, user management, unfiltered HTML or Builder capabilities. Choose an eligible role from the Builder's current options; the generated schema does not enumerate this runtime-filtered role list.

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

# Heading Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/heading/

*Schema for Bricks Heading element*

| Property | Value |
|---|---|
| `name` | heading |
| `category` | basic |
| `tag` | h3 |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `text` | text | text | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |
| `type` | select | Type | — |
| `style` | select | Style | — |
| `link` | link | Link to | — |
| `separator` | select | Separator | — |
| `separatorWidth` | number | Width | `width` on `.separator`, `flex-grow` on `.separator`, `width` |
| `separatorHeight` | number | Height | `border-top-width` on `.separator`, `height` on `.separator` |
| `separatorSpacing` | number | Spacing | `gap` on `&.has-separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.separator` |
| `separatorAlignItems` | align-items | Align | `align-items` on `&.has-separator` |
| `separatorColor` | color | Color | `border-top-color` on `.separator` |

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

# HTML Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/html/

*Schema for Bricks HTML element*

| Property | Value |
|---|---|
| `name` | html |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `html` | code | Raw HTML | — |

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

# Icon Box Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/icon-box/

*Schema for Bricks Icon Box element*

| Property | Value |
|---|---|
| `name` | icon-box |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `direction` | direction | Direction | `flex-direction` |
| `gap` | number | Spacing | `gap` |
| `icon` | icon | Icon | — |
| `verticalAlign` | align-items | Align | `align-self` on `.icon` |
| `link` | link | Link | — |
| `iconMargin` | spacing | Margin | `margin` on `.icon` |
| `iconPadding` | spacing | Padding | `padding` on `.icon` |
| `iconSize` | number | Size | `font-size` on `.icon i` |
| `iconHeight` | number | Height | `height` on `.icon`, `line-height` on `.icon` |
| `iconWidth` | number | Width | `min-width` on `.icon` |
| `iconColor` | color | Color | `color` on `.icon`, `color` on `.icon a` |
| `iconBackgroundColor` | color | Background color | `background-color` on `.icon` |
| `iconBorder` | border | Border | `border` on `.icon` |
| `iconBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.icon` |
| `content` | editor | content | — |
| `contentMargin` | spacing | Margin | `margin` on `.content` |
| `contentPadding` | spacing | Padding | `padding` on `.content` |
| `contentAlign` | align-items | Align | `align-self` on `.content` |
| `typographyHeading` | typography | Heading typography | `font` on `h1`, `font` on `h2`, `font` on `h3`, `font` on `h4`, `font` on `h5`, `font` on `h6` |
| `typographyBody` | typography | Body typography | `font` on `.content` |
| `contentBackgroundColor` | color | Background | `background-color` on `.content` |
| `contentBorder` | border | Border | `border` on `.content` |
| `contentBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.content` |

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

# Icon Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/icon/

*Schema for Bricks Icon element*

| Property | Value |
|---|---|
| `name` | icon |
| `category` | basic |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `icon` | icon | Icon | — |
| `iconColor` | color | Color | `color`, `fill` |
| `iconSize` | number | Size | `font-size` |
| `link` | link | Link | — |
| `isAccordionIcon` | checkbox | isAccordionIcon | — |
| `accordionTitleIconState` | select | Show | — |
| `accordionTitleIconTransform` | transform | Transform | `--brx-icon-transform` |
| `accordionTitleIconTransition` | text | Transition | `transition` |

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

# Image Gallery Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/image-gallery/

*Schema for Bricks Image gallery element*

| Property | Value |
|---|---|
| `name` | image-gallery |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `items` | image-gallery | Images | — |
| `layout` | select | Layout | — |
| `columns` | number | Columns | `--columns` |
| `gutter` | number | Spacing | `--gutter` |
| `imageHeight` | number | Image height | `height` on `.image` |
| `imageRatio` | text | Image ratio | `aspect-ratio` on `.image` |
| `caption` | checkbox | Image caption | — |
| `link` | select | Link to | — |
| `linkCustom` | repeater | Custom links | — |
| `lightboxImageSize` | select | Image size | — |
| `lightboxImageClick` | select | Image click action | — |
| `lightboxAnimationType` | select | Animation | — |
| `lightboxCaption` | checkbox | Caption | — |
| `lightboxThumbnails` | checkbox | Thumbnail navigation | — |
| `lightboxThumbnailSize` | number | Thumbnail size | — |
| `lightboxPadding` | dimensions | Padding | — |
| `lightboxId` | text | Lightbox | — |
| `fetchpriorityAttribute` | select | Fetch priority | — |
| `loadingAttribute` | select | Loading | — |
| `loadMoreInitial` | number | Initial items | — |
| `loadMoreStep` | number | Items per load | — |
| `loadMoreInfiniteScroll` | checkbox | Infinite scroll | — |
| `loadMoreInfiniteScrollDelay` | number | Infinite scroll delay | — |
| `loadMoreInfiniteScrollOffset` | number | Infinite scroll offset | — |

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

# Image Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/image/

*Schema for Bricks Image element*

| Property | Value |
|---|---|
| `name` | image |
| `category` | basic |
| `tag` | figure |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `image` | image | Image | — |
| `tag` | select | HTML tag | — |
| `customTag` | text | Custom tag | — |
| `sources` | repeater | Sources | — |
| `altText` | text | Custom alt text | — |
| `caption` | select | Caption type | — |
| `captionCustom` | text | Custom caption | — |
| `loading` | select | Loading | — |
| `showTitle` | checkbox | Show title | — |
| `stretch` | checkbox | Stretch | `width` |
| `popupOverlay` | color | Image Overlay | `background-color` on `&\{pseudo\}.overlay::before` |
| `link` | select | link | — |
| `lightboxImageSize` | select | Image size | — |
| `lightboxWidth` | number | Width | — |
| `lightboxHeight` | number | Height | — |
| `lightboxAnimationType` | select | Animation | — |
| `lightboxCaption` | checkbox | Caption | — |
| `lightboxId` | text | ID | — |
| `lightboxCropped` | checkbox | Cropped | — |
| `lightboxPadding` | dimensions | Padding | — |
| `newTab` | checkbox | Open in new tab | — |
| `url` | link | url | — |
| `lightboxAriaLabel` | text | aria-label | — |
| `lightboxTitle` | text | title | — |
| `popupIconDisable` | checkbox | Disable icon | — |
| `popupIcon` | icon | Icon | — |
| `popupIconBackgroundColor` | color | Icon background color | `background-color` on `&\{pseudo\} .icon` |
| `popupIconBorder` | border | Icon border | `border` on `&\{pseudo\} .icon` |
| `popupIconBoxShadow` | box-shadow | Icon box shadow | `box-shadow` on `&\{pseudo\} .icon` |
| `popupIconTypography` | typography | Icon typography | `font` on `&\{pseudo\} .icon` |
| `popupIconHeight` | number | Icon height | `line-height` on `&\{pseudo\} .icon` |
| `popupIconWidth` | number | Icon width | `width` on `&\{pseudo\} .icon` |
| `popupIconTransition` | text | Icon transition | `transition` on `&\{pseudo\} .icon` |
| `mask` | select | Mask | — |
| `maskCustom` | image | maskCustom | — |
| `maskSize` | select | Size | — |
| `maskSizeCustom` | number | Custom size | — |
| `maskPosition` | select | Position | — |
| `maskRepeat` | select | Repeat | — |

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

# List Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/list/

*Schema for Bricks List element*

| Property | Value |
|---|---|
| `name` | list |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `items` | repeater | List items | — |
| `itemJustifyContent` | justify-content | Justify content | `justify-content` on `.content`, `justify-content` on `.description` |
| `itemAlignItems` | align-items | Align items | `align-items` on `.content`, `align-items` on `.description` |
| `itemMargin` | spacing | Margin | `margin` on `li` |
| `itemPadding` | spacing | Padding | `padding` on `li` |
| `itemOddBackground` | color | Odd background | `background-color` on `li:nth-child(odd)` |
| `itemEvenBackground` | color | Even background | `background-color` on `li:nth-child(even)` |
| `itemBorder` | border | Border | `border` on `li` |
| `itemAutoWidth` | checkbox | Auto width | `justify-content` on `.content`, `flex-grow` on `.separator` |
| `highlightBlock` | checkbox | Block | `display` on `li[data-highlight]::before` |
| `highlightLabelPadding` | spacing | Padding | `padding` on `li[data-highlight]::before` |
| `highlightLabelBackground` | color | Background | `background-color` on `li[data-highlight]::before` |
| `highlightLabelBorder` | border | Border | `border` on `li[data-highlight]::before` |
| `highlightLabelTypography` | typography | Typography | `font` on `li[data-highlight]::before` |
| `highlightContentPadding` | spacing | Padding | `padding` on `li[data-highlight] .content` |
| `highlightContentBackground` | color | Background | `background-color` on `li[data-highlight] .content` |
| `highlightContentBorder` | border | Border | `border` on `li[data-highlight] .content` |
| `highlightContentColor` | color | Text color | `color` on `li[data-highlight] .content .title`, `color` on `li[data-highlight] .content .meta`, `color` on `li[data-highlight] .content .description` |
| `icon` | icon | Icon | — |
| `iconAfterTitle` | checkbox | After title | — |
| `iconWidth` | number | Width | `width` on `.icon` |
| `iconHeight` | number | Height | `height` on `.icon` |
| `iconSize` | number | Size | `font-size` on `.icon`, `height` on `.icon svg`, `width` on `.icon svg` |
| `iconColor` | color | Color | `color` on `.icon` |
| `iconBackgroundColor` | color | Background color | `background-color` on `.icon` |
| `iconBorder` | border | Border | `border` on `.icon` |
| `iconBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.icon` |
| `titleMargin` | spacing | Margin | `margin` on `.title` |
| `titleTag` | text | HTML tag | — |
| `titleTypography` | typography | Typography | `font` on `.title` |
| `metaMargin` | spacing | Margin | `margin` on `.meta` |
| `metaTypography` | typography | Typography | `font` on `.meta` |
| `descriptionTypography` | typography | Typography | `font` on `.description` |
| `separatorDisable` | checkbox | Disable | `display` on `.separator` |
| `separatorStyle` | select | Style | `border-top-style` on `.separator` |
| `separatorWidth` | number | Width | `flex-basis` on `.separator`, `flex-grow` on `.separator` |
| `separatorHeight` | number | Height | `border-top-width` on `.separator` |
| `separatorColor` | color | Color | `border-top-color` on `.separator` |

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

# Instagram Feed Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/instagram-feed/

*Schema for Bricks Instagram feed element*

| Property | Value |
|---|---|
| `name` | instagram-feed |
| `category` | media |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `columns` | number | Columns | `grid-template-columns` on `ul` |
| `numberOfPosts` | number | Posts | — |
| `imageObjectFit` | select | Object fit | `object-fit` on `img` |
| `imageAspectRatio` | text | Aspect ratio | `aspect-ratio` on `img` |
| `imageHeight` | number | Height | `height` on `img` |
| `imageWidth` | number | Width | `width` on `img` |
| `imageGap` | number | Gap | `gap` on `ul` |
| `imageBorder` | border | Border | `border` on `img` |
| `imageLink` | checkbox | Link | — |
| `carouselIcon` | icon | Icon | — |
| `carouselIconColor` | color | Icon color | `color` on `.brx-icon.carousel` |
| `carouselIconSize` | number | Icon size | `height` on `.brx-icon.carousel svg`, `width` on `.brx-icon.carousel svg`, `font-size` on `.brx-icon.carousel` |
| `carouselIconPosition` | dimensions | Icon position | — |
| `videoIcon` | icon | Icon | — |
| `videoIconColor` | color | Icon color | `color` on `.brx-icon.video` |
| `videoIconSize` | number | Icon size | `height` on `.brx-icon.video svg`, `width` on `.brx-icon.video svg`, `font-size` on `.brx-icon.video` |
| `videoIconPosition` | dimensions | Icon position | — |
| `caption` | checkbox | Enable | — |
| `captionBackground` | color | Background color | `background-color` on `.caption` |
| `captionBorder` | border | Border | `border` on `.caption` |
| `captionTypography` | typography | Typography | `font` on `.caption` |
| `followText` | text | Text | — |
| `followPosition` | select | Position | — |
| `followIcon` | icon | Icon | `—` on `.follow-icon` |
| `followTypography` | typography | Typography | `font` on `.follow` |
| `cacheDuration` | select | Duration | — |

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

# Map Connector Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/map-connector/

*Schema for Bricks Map Connector element*

| Property | Value |
|---|---|
| `name` | map-connector |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `latitude` | text | Latitude | — |
| `longitude` | text | Longitude | — |
| `address` | text | Address | — |
| `infoBoxTemplateId` | select | Info Box | — |

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

# Map (Leaflet) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/map-leaflet/

*Schema for Bricks Map (Leaflet) element*

| Property | Value |
|---|---|
| `name` | map-leaflet |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `layers` | repeater | Name | — |
| `markers` | repeater | Coordinates | — |
| `markerIcon` | image | Icon | — |
| `markerIconHeight` | number | Icon | — |
| `markerIconWidth` | number | Icon | — |
| `height` | number | Height | `height` |
| `center` | text | Map center | — |
| `zoom` | number | Zoom level | — |
| `minZoom` | number | Zoom level | — |
| `maxZoom` | number | Zoom level | — |
| `zoomSnap` | number | Zoom | — |
| `zoomDelta` | number | Zoom | — |
| `doubleClickZoom` | select | Zoom | — |
| `scrollWheelZoom` | select | Zoom | — |
| `boxZoom` | checkbox | Box Zoom | — |
| `zoomControl` | checkbox | Zoom Control | — |
| `attributionControl` | checkbox | Attribution Control | — |
| `closePopupOnClick` | checkbox | Close popup on click | — |
| `dragging` | checkbox | Dragging | — |
| `trackResize` | checkbox | Track resize | — |

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

# Logo Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/logo/

*Schema for Bricks Logo element*

| Property | Value |
|---|---|
| `name` | logo |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `logo` | image | Logo | — |
| `logoInverse` | image | Logo inverse | — |
| `logoDark` | image | Logo dark mode | — |
| `logoHeight` | number | Height | `height` on `.bricks-site-logo` |
| `logoWidth` | number | Width | `width` on `.bricks-site-logo` |
| `logoText` | text | Text | — |
| `logoLoading` | select | Loading | — |
| `logoUrl` | link | Link to | — |

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

# Map (Google) Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/map/

*Schema for Bricks Map (Google) element*

| Property | Value |
|---|---|
| `name` | map |
| `category` | general |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `address` | text | Address | — |
| `addresses` | repeater | Addresses | — |
| `infoBoxTemplateId` | select | Info Box | — |
| `syncQuery` | query-list | syncQuery | — |
| `mapNoResultsText` | text | Text | — |
| `markerCluster` | checkbox | Cluster | — |
| `markerClusterBgColor` | color | Cluster | `fill` on `.brx-map-cluster` |
| `markerClusterTextColor` | color | Cluster | `fill` on `.brx-map-cluster text` |
| `markerType` | select | Type | — |
| `googleMapId` | text | Map ID | — |
| `mapCenterLat` | text | Latitude | — |
| `mapCenterLng` | text | Longitude | — |
| `mapCenterAddress` | text | Address | — |
| `renderMode` | select | Render mode | — |
| `localization` | checkbox | Use page locale | — |
| `height` | number | Height | `height` |
| `zoom` | number | Zoom level | — |
| `type` | select | Map type | — |
| `loading` | select | Loading | — |
| `style` | select | Map style | — |
| `customStyle` | code | Custom map style | — |
| `disableInitialFitBounds` | checkbox | Disable initial fit map | — |
| `fitMapOnMarkersChange` | checkbox | Fit map on markers change | — |
| `scrollwheel` | checkbox | Scroll | — |
| `draggable` | checkbox | Draggable | — |
| `fullscreenControl` | checkbox | Fullscreen Control | — |
| `mapTypeControl` | checkbox | Map Type Control | — |
| `streetViewControl` | checkbox | Street View Control | — |
| `disableDefaultUI` | checkbox | Disable Default UI | — |
| `disableClickPOI` | checkbox | Disable clickable POI | — |
| `zoomControl` | checkbox | Zoom Control | — |
| `minZoom` | number | Zoom level | — |
| `maxZoom` | number | Zoom level | — |

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

# Nav Menu Schema

Source: https://academy.bricksbuilder.io/developer/schema/elements/nav-menu/

*Schema for Bricks Nav Menu element*

| Property | Value |
|---|---|
| `name` | nav-menu |
| `category` | wordpress |
| `tag` | div |
| `nestable` | false |

## Controls

| Key | Type | Label | CSS |
|---|---|---|---|
| `menu` | select | Menu | — |
| `ariaLabel` | text | ARIA label | — |
| `menuAlignment` | direction | Alignment | `flex-direction` on `.bricks-nav-menu` |
| `menuJustifyContent` | justify-content | Justify content | `justify-content` on `.bricks-nav-menu > li > a`, `justify-content` on `.bricks-nav-menu > li > .brx-submenu-toggle` |
| `menuGap` | number | Gap | `gap` on `.bricks-nav-menu` |
| `menuMargin` | spacing | Margin | `margin` on `.bricks-nav-menu > li` |
| `menuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu > li > a`, `padding` on `.bricks-nav-menu > li > .brx-submenu-toggle > *` |
| `menuBackground` | background | Background | `background` on `.bricks-nav-menu > li\{pseudo\} > a`, `background` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle` |
| `menuBorder` | border | Border | `border` on `.bricks-nav-menu > li\{pseudo\} > a`, `border` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle` |
| `menuTypography` | typography | Typography | `font` on `.bricks-nav-menu > li\{pseudo\} > a`, `font` on `.bricks-nav-menu > li\{pseudo\} > .brx-submenu-toggle > *` |
| `menuActiveBackground` | background | Active background | `background` on `.bricks-nav-menu > .current-menu-item > a`, `background` on `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, `background` on `.bricks-nav-menu > .current-menu-parent > a`, `background` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle`, `background` on `.bricks-nav-menu > .current-menu-ancestor > a`, `background` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `menuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .current-menu-item > a`, `border` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-nav-menu > .current-menu-parent > a`, `border` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle`, `border` on `.bricks-nav-menu > .current-menu-ancestor > a`, `border` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `menuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .current-menu-item > a`, `font` on `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu > .current-menu-parent > a`, `font` on `.bricks-nav-menu > .current-menu-parent > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu > .current-menu-ancestor > a`, `font` on `.bricks-nav-menu > .current-menu-ancestor > .brx-submenu-toggle > *` |
| `menuIcon` | icon | Icon | `—` on `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` |
| `menuIconTransform` | transform | Icon transform | `transform` on `.bricks-nav-menu button[aria-expanded="false"] > *` |
| `menuIconTransformOpen` | transform | Icon transform | `transform` on `.bricks-nav-menu button[aria-expanded="true"] > *` |
| `menuIconTypography` | typography | Icon typography | `font` on `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle\{pseudo\} button[aria-expanded]` |
| `menuIconPosition` | select | Icon position | — |
| `menuIconMargin` | spacing | Icon margin | `margin` on `.bricks-nav-menu .brx-submenu-toggle button` |
| `menuIconPadding` | spacing | Icon padding | `padding` on `.bricks-nav-menu .brx-submenu-toggle button` |
| `submenuStatic` | checkbox | Position | — |
| `subMenuBackgroundList` | background | Background | `background` on `.bricks-nav-menu .sub-menu` |
| `subMenuBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu` |
| `subMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-nav-menu .sub-menu` |
| `subMenuTransform` | transform | Transform | `transform` on `.bricks-nav-menu > li > .sub-menu`, `transform` on `.bricks-nav-menu > li > .brx-megamenu` |
| `subMenuTransformOpen` | transform | Transform | `transform` on `.bricks-nav-menu > li.open > .sub-menu`, `transform` on `.bricks-nav-menu > li.open > .brx-megamenu` |
| `caretSize` | number | Size | `border-width` |
| `caretColor` | color | Color | `border-bottom-color` |
| `caretTransform` | transform | Transform | `transform` |
| `caretPosition` | dimensions | Position | — |
| `subMenuJustifyContent` | justify-content | Justify content | `justify-content` on `.bricks-nav-menu .sub-menu a`, `justify-content` on `.bricks-nav-menu .sub-menu button` |
| `subMenuPadding` | spacing | Padding | `padding` on `.bricks-nav-menu .sub-menu a`, `padding` on `.bricks-nav-menu .sub-menu button` |
| `subMenuBackground` | background | Background | `background` on `.bricks-nav-menu .sub-menu .menu-item` |
| `subMenuItemBorder` | border | Border | `border` on `.bricks-nav-menu .sub-menu > li` |
| `subMenuTypography` | typography | Typography | `font` on `.bricks-nav-menu .sub-menu > li\{pseudo\} > a`, `font` on `.bricks-nav-menu .sub-menu > li\{pseudo\} > .brx-submenu-toggle > *` |
| `subMenuActiveBackground` | background | Active background | `background` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `background` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `subMenuActiveBorder` | border | Active border | `border` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `border` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `subMenuActiveTypography` | typography | Active typography | `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > a`, `font` on `.bricks-nav-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle > *` |
| `subMenuIcon` | icon | Icon | `—` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle\{pseudo\} svg` |
| `subMenuIconSize` | number | Icon size | `height` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg`, `width` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg`, `font-size` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` |
| `subMenuIconTransform` | transform | Icon transform | `transform` on `.bricks-nav-menu .sub-menu button > *` |
| `subMenuIconTransformOpen` | transform | Icon transform | `transform` on `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` |
| `subMenuIconTypography` | typography | Icon typography | `font` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a\{pseudo\} + button` |
| `subMenuIconPosition` | select | Icon position | — |
| `subMenuIconMargin` | spacing | Icon margin | `margin` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` |
| `subMenuIconPadding` | spacing | Icon padding | `padding` on `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` |
| `mobileMenu` | select | mobileMenu | — |
| `mobileMenuAriaLabel` | text | ARIA label | — |
| `mobileMenuCustomBreakpoint` | number | Custom breakpoint | — |
| `mobileMenuPosition` | select | Position | — |
| `mobileMenuTop` | number | mobileMenuTop | `top` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuWidth` | number | Width | `width` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuHeight` | number | Height | `height` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuFadeIn` | checkbox | Fade in | — |
| `mobileMenuAlignment` | justify-content | Vertical | `justify-content` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuAlignItems` | align-items | Horizontal | `align-items` on `.bricks-mobile-menu-wrapper`, `justify-content` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle`, `width` on `.bricks-mobile-menu-wrapper a` |
| `mobileMenuTextAlign` | text-align | Text align | `text-align` on `.bricks-mobile-menu-wrapper` |
| `mobileMenuBackground` | background | Background | `background` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuBackgroundFilters` | filters | Background filters | `filter` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuBoxShadow` | box-shadow | Box shadow | `box-shadow` on `.bricks-mobile-menu-wrapper:before` |
| `mobileMenuOverlay` | background | Overlay | `background` on `.bricks-mobile-menu-overlay` |
| `mobileMenuPadding` | spacing | Padding | `padding` on `.bricks-mobile-menu > li > a`, `padding` on `.bricks-mobile-menu > li > .brx-submenu-toggle > *` |
| `mobileMenuItemBackground` | color | Background | `background-color` on `.bricks-mobile-menu > li > a`, `background-color` on `.bricks-mobile-menu > li > .brx-submenu-toggle` |
| `mobileMenuItemBackgroundActive` | color | Background | `background-color` on `.bricks-mobile-menu > li > a[aria-current="page"]`, `background-color` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` |
| `mobileMenuBorder` | border | Border | `border` on `.bricks-mobile-menu > li > a`, `background-color` on `.bricks-mobile-menu > li > .brx-submenu-toggle` |
| `mobileMenuActiveBorder` | border | Border | `border` on `.bricks-mobile-menu > .current-menu-item > a`, `border` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-mobile-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `mobileMenuTypography` | typography | Typography | `font` on `.bricks-mobile-menu > li > a`, `font` on `.bricks-mobile-menu > li > .brx-submenu-toggle > *` |
| `mobileMenuActiveTypography` | typography | Typography | `font` on `.bricks-mobile-menu [aria-current="page"]`, `font` on `.bricks-mobile-menu [aria-current="page"] + button`, `font` on `.bricks-mobile-menu > .current-menu-item > a`, `font` on `.bricks-mobile-menu > .current-menu-parent > a`, `font` on `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle > *`, `font` on `.bricks-mobile-menu > .current-menu-parent > .brx-submenu-toggle > *` |
| `mobileMenuIcon` | icon | Icon | `—` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` |
| `mobileMenuCloseIcon` | icon | Close icon | `—` on `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` |
| `mobileMenuIconTypography` | typography | Icon typography | `font` on `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` |
| `mobileMenuIconPosition` | select | Icon position | — |
| `mobileMenuIconMargin` | spacing | Icon margin | `margin` on `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` |
| `mobileSubMenuPadding` | spacing | Padding | `padding` on `.bricks-mobile-menu .sub-menu > .menu-item > a`, `padding` on `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` |
| `mobileSubMenuItemBackground` | color | Background | `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > a`, `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` |
| `mobileSubMenuItemBackgroundActive` | color | Background | `background-color` on `.bricks-mobile-menu .sub-menu > .menu-item > a[aria-current="page"]`, `background-color` on `.bricks-mobile-menu .sub-menu .current-menu-item > .brx-submenu-toggle` |
| `mobileSubMenuBorder` | border | Border | `border` on `.bricks-mobile-menu .sub-menu > .menu-item` |
| `mobileSubMenuBorderActive` | border | Border | `border` on `.bricks-mobile-menu .sub-menu > .current-menu-item > a`, `border` on `.bricks-mobile-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, `border` on `.bricks-mobile-menu .sub-menu > .current-menu-ancestor > .brx-submenu-toggle` |
| `mobileSubMenuTypography` | typography | Typography | `font` on `.bricks-mobile-menu .sub-menu > li > a`, `font` on `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` |
| `mobileSubMenuActiveTypography` | typography | Active typography | `font` on `.bricks-mobile-menu .sub-menu > .current-menu-item > a`, `font` on `.bricks-mobile-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *` |
| `mobileMenuToggleAriaLabel` | text | aria-label | — |
| `mobileMenuToggleWidth` | number | Toggle width | `width` on `.bricks-mobile-menu-toggle`, `width` on `.bricks-mobile-menu-toggle .bar-top`, `width` on `.bricks-mobile-menu-toggle .bar-center`, `width` on `.bricks-mobile-menu-toggle .bar-bottom` |
| `mobileMenuToggleColor` | color | Color | `color` on `.bricks-mobile-menu-toggle` |
| `mobileMenuToggleHide` | checkbox | Hide close | `display` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `mobileMenuToggleColorClose` | color | Color close | `color` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `mobileMenuToggleClosePosition` | dimensions | Close position | `—` on `&.show-mobile-menu .bricks-mobile-menu-toggle` |
| `megaMenu` | checkbox | Enable | — |
| `megaMenuSelector` | text | CSS selector | — |
| `megaMenuToggleOn` | select | Toggle on | — |
| `megaMenuTransition` | text | Transition | `transition` on `.brx-megamenu` |
| `megaMenuTransform` | transform | Transform | `transform` on `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` |
| `megaMenuTransformOpen` | transform | Transform | `transform` on `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu`, `transform` on `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` |
| `multiLevel` | checkbox | Enable | — |
| `multiLevelBackText` | text | Back | — |
| `multiLevelBackTypography` | typography | Back | `font` on `.brx-multilevel-back` |
| `multiLevelBackground` | color | Back | `background-color` on `.brx-multilevel-back` |

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
