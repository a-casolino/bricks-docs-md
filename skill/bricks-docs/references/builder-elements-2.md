# File

Source: https://academy.bricksbuilder.io/builder/elements/media/file/

*Add downloadable files and links in Bricks from the Media Library, external URLs, or dynamic data, with optional inline PDF previews.*

The File element displays a document as a linked file name, a download button, or both. PDF files can also appear in a browser-native inline preview.

The element is available in Bricks 2.4. Find it under **Elements > Media > File**.

![File element selected in the Bricks builder with the Source control and the File name, Download button, and PDF preview groups visible.](https://academy.bricksbuilder.io/assets/bricks-file-element-controls.webp)

## Choose the file source

Use the **Source** control to choose where the file comes from:

- **File**: Select a file from the WordPress Media Library. This is the default source.
- **External URL**: Enter the direct URL of a file hosted on this site or another site.
- **Dynamic data**: Select a file or media value from [dynamic data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/). In a template, each post can supply its own document through a custom field.

If a dynamic field returns more than one media item, the File element uses the first item.

## File name

The file name is shown as a link by default. It opens the file instead of forcing a download.

The **File name** group contains these controls:

- **Hide file name**: Removes the linked file name.
- **Custom file name**: Replaces the name from the Media Library or file URL. This control supports dynamic data.
- **Open in new tab**: Opens the file-name link in a new browser tab. It also applies to the fallback link inside a PDF preview.

When no custom name is set, Bricks uses the Media Library filename or extracts the filename from the URL.

## Download button

The download button is shown by default. Use the **Download button** group to change its label, size, style, outline, and circle settings, or enable **Hide download button**.

The filename link and download button have different purposes: the filename link opens the file, while the button uses the browser's download behavior. A browser or external file host can still open the file instead of downloading it.

## PDF preview

Bricks displays the preview when it recognizes the source as a PDF. A Media Library file is identified by its `application/pdf` MIME type. External and dynamic URLs are identified by a `.pdf` extension in the URL path.

An external URL without `.pdf` in its path is not treated as a PDF, even if the server returns PDF content.

The preview fills the element width and is 600px high by default. Its controls are in the **PDF preview** group:

- **Hide PDF preview**: Removes the inline preview. The file name and download button remain available unless you hide them separately.
- **Preview title**: Sets the accessible label for the embedded PDF. When left empty, Bricks generates a label from the file name.
- **Height**: Sets the preview height. Use [responsive editing](https://academy.bricksbuilder.io/builder/interface/responsive-editing/) to adjust it at different breakpoints.
- **Display**: Keep the preview inline at every viewport width, or use **Inline on desktop, hidden on mobile**.
- **Hide at breakpoint**: Chooses the viewport width at which the preview is hidden. This appears when **Inline on desktop, hidden on mobile** is selected. If you do not choose a breakpoint, Bricks uses the Mobile landscape breakpoint, with 767px as the fallback width.
- **Load PDF on click**: Delays loading the PDF until the visitor activates the preview placeholder.
- **Preview image**: Sets the image shown before a click. This appears when **Load PDF on click** is enabled.

With **Load PDF on click** enabled, Bricks uses the custom preview image first. If none is set, it uses a preview generated for the Media Library attachment when WordPress has one. Otherwise, the placeholder shows a PDF icon and the file name.

![File element showing the generated PDF preview image before the PDF loads.](https://academy.bricksbuilder.io/assets/bricks-file-element-load-pdf-before.webp)

![File element after loading the PDF in the browser-native inline viewer.](https://academy.bricksbuilder.io/assets/bricks-file-element-load-pdf-after.webp)

> **Keep a file link available**
>
> If the PDF preview is hidden at a breakpoint, its internal fallback link is hidden with it. Keep the file name or download button visible so visitors can still reach the document at that breakpoint.

## Example: A PDF from a custom field

Suppose each property post has a PDF brochure stored in a file field:

1. Add the File element to the property template.
2. Set **Source** to **Dynamic data**.
3. Select the brochure file field.
4. Enter a **Custom file name**, such as `{post_title} brochure`.
5. Enable **Load PDF on click** if you do not want the browser to request the PDF when the page first loads.
6. Add a **Preview image**, or let Bricks use the attachment preview when one is available.
7. Keep the file name or download button visible as the non-preview way to reach the brochure.

Open two property posts on the frontend. Each one displays the PDF stored on that post while keeping the same template layout.

## Browser behavior and document access

The File element uses the browser's built-in PDF support. The PDF toolbar, rendering, and print or download options can differ between browsers and devices.

Hiding a download button or browser controls does not secure the PDF. The visitor's browser still receives the file URL and file contents. Protect restricted documents at the server or application level before using them in the File element.

Non-PDF files do not receive an inline preview. They use the linked file name and download button.

---

# Image gallery

Source: https://academy.bricksbuilder.io/builder/elements/media/image-gallery/

*The Image Gallery element displays a collection of images in various layouts with optional lightbox functionality.*

The Image Gallery element displays a collection of images in various layouts with optional lightbox functionality.

## Settings

- **Images** (image-gallery) - Select and upload images for the gallery.

- **Layout** (select) - Gallery layout type. Options: `grid`, `masonry`, `metro`. Default: `grid`.

- **Columns** (number) - Number of columns in the grid. Minimum: 2. Default: 3. Not available for metro layout.

- **Spacing** (number with units) - Gap between images. Default: 0.

- **Image height** (number with units) - Fixed height for images. Not available for masonry or metro layouts.

- **Image ratio** (text) - Aspect ratio for images (e.g., 4/3, 16/9, 1/1). Not available for masonry or metro layouts.

- **Image caption** (checkbox) - Display image captions.

- **Link to** (select) - Link behavior for images. Options: `lightbox`, `attachment page`, `media file`, `custom URL`.

- **Custom links** (repeater) - Define custom URLs for each image. Only shown when "Link to" is set to "custom URL".

### Lightbox

- **Image size** (select) - Size of images in lightbox. Default: Full.

- **Image click action** (select) - Action when clicking images. Options: `zoom`, `zoom or close`, `toggle controls`, `next`, `close`. Default: `zoom`.

- **Animation** (select) - Lightbox transition animation.

- **Caption** (checkbox) - Show image captions in lightbox.

- **Thumbnail navigation** (checkbox) - Enable thumbnail navigation.

- **Thumbnail size** (number with units) - Size of thumbnails. Default: 60px.

- **Padding (px)** (dimensions) - Padding around the lightbox.

- **Lightbox: ID** (text) - Group images with the same ID together in the same lightbox.

- **Fetch priority** (select) - Image loading priority. Options: `high`, `low`, `auto`.

> **Developer reference**
>
> See the [Image Gallery Schema](https://academy.bricksbuilder.io/developer/schema/elements/image-gallery/) for the full JSON schema of this element's settings and controls.

---

# Instagram feed

Source: https://academy.bricksbuilder.io/builder/elements/media/instagram-feed/

*The Instagram feed element loads media from the Instagram Graph API using an access token saved in Bricks → Settings → API keys (instagramAccessToken). Without.*

The **Instagram feed** element loads media from the **Instagram Graph API** using an **access token** saved in **Bricks → Settings → API keys** (`instagramAccessToken`). Without a token, the element shows a placeholder asking you to connect the account.

Responses are **cached** in a transient to limit API calls; cache length is configurable.

## Requirements

Add a valid **Instagram access token** under **Bricks → Settings → API keys**. The element’s info message links there when the global token is missing.

## Layout

- **Columns** (number) — CSS grid columns for the list (`ul`). Placeholder: `3`. Valid range on the front end: `1–6`.

- **Posts** (number) — How many posts to request (min `1`, max `100`). Placeholder: `9`.

## Image

- **Object fit** (select) — Applied to `img`.

- **Aspect ratio** (text).

- **Height**, **Width** (number with units).

- **Gap** (number with units) — Gap on the `ul` grid.

- **Border** (border) — Image border.

- **Link** (checkbox) — Wrap each image in a link to the Instagram permalink.

## Carousel

Optional styling for the **carousel** badge on **CAROUSEL_ALBUM** items:

- **Icon** (icon), **Icon color** (color), **Icon size** (number with units), **Icon position** (dimensions).

## Video

Optional styling for the **video** play overlay on **VIDEO** items:

- **Icon** (icon), **Icon color** (color), **Icon size** (number with units), **Icon position** (dimensions).

## Caption

- **Enable** (checkbox) — Show the post caption below the image.

When enabled: **Background color**, **Border**, **Typography** on `.caption`.

## Follow

Optional “Follow us” row linking to `instagram.com/{username}`:

- **Text** (text) — Default mentions `@yourhandle`; replace with your copy or dynamic data.

- **Position** (select) — `top` or `bottom`.

- **Icon** (icon) — Default Instagram logo.

- **Typography** — `.follow` text.

## Cache

- **Duration** (select) — `30 minutes`, `1 hour`, `1 day`, or `1 week` (stored as seconds: `1800`, `3600`, `86400`, `604800`). Default placeholder: 1 hour.

> **Developer reference**
>
> See the [Instagram feed Schema](https://academy.bricksbuilder.io/developer/schema/elements/instagram-feed/) for the full JSON schema of this element's settings and controls.

---

# Logo

Source: https://academy.bricksbuilder.io/builder/elements/media/logo/

*The Logo element displays your site logo with support for regular, inverse, and dark-mode logo variants, custom dimensions, and fallback text.*

The Logo element displays your site logo and can switch between logo variants for dark mode and sticky headers.

## Settings

- **Logo** (image) - Select the main logo image from the media library. Minimum dimension should be twice the logo height/width for proper retina display. For SVG logos, set height and width in px values.

- **Logo inverse** (image) - Alternative logo image for sticky scrolling headers. Only available when the main logo is set.

- **Logo dark mode** (image) - Alternative logo image used when dark mode is active. Only available when the main logo is set.

- **Height** (number with units) - Logo height. Maximum: 400. Default: `auto`. Only available when logo is set.

- **Width** (number with units) - Logo width. Maximum: 999. Default: `auto`. Only available when logo is set.

- **Text** (text) - Fallback text displayed if logo image isn't set or available. Default: Site name from WordPress settings.

- **Loading** (select) - Image loading behavior. Options: `eager`, `lazy`. Default: `eager`.

- **Link to** (link) - Configure where the logo links. Default: Site home page.

## Logo variants

Logo variants are available starting in Bricks 2.4. Add them in the Logo element settings under **Logo variants**.

When [dark mode](https://academy.bricksbuilder.io/builder/features/color-manager/#using-dark-mode) is active and **Logo dark mode** is configured, Bricks swaps the main logo image for the dark-mode logo. If no dark-mode logo is configured, the main logo stays visible.

If the Logo element is inside a sticky header and **Logo inverse** is configured, the inverse logo is used while the header is scrolling. This takes priority over the dark-mode logo during the sticky scrolling state.

> **Developer reference**
>
> See the [Logo Schema](https://academy.bricksbuilder.io/developer/schema/elements/logo/) for the full JSON schema of this element's settings and controls.

---

# Slider (nestable)

Source: https://academy.bricksbuilder.io/builder/elements/media/slider-nested/

*The Nestable Slider element allows creating sliders with drag-and-drop nesting in the builder, using the Splide library.*

The Nestable Slider element allows creating sliders with drag-and-drop nesting in the builder, using the Splide library.

## Settings

- **Children** (nestable) - Drag and drop elements to create slider slides.

### Options

- **Options type** (select) - Use default settings or provide custom JSON options. Options: `default`, `custom`.

- **Custom options** (code) - JSON configuration for Splide slider. Only shown when options type is custom. Provide your own options in JSON format (learn more).

- **Type** (select) - Slider behavior. Options: `loop`, `slide`, `fade`. Default: `loop`.

- **Direction** (select) - Slide direction. Options: `left to right`, `right to left`, `vertical`. Supports breakpoints.

- **Keyboard** (select) - Keyboard navigation. Options: `off`, `focused`, `global`. Default: `global`. Supports breakpoints.

- **Auto height** (checkbox) - Adjust height to content. May cause layout shift. Using "Auto height" might lead to CLS (Cumulative Layout Shift).

- **Height** (number with units) - Fixed slider height. Default: 50vh. Not available when auto height is enabled. Supports breakpoints.

- **Spacing** (number with units) - Gap between slides. Default: 0. Supports breakpoints.

- **Start index** (number) - Initial slide index. Default: 0.

- **Items to show** (number) - Number of slides visible at once. Default: 1. Supports breakpoints. Not available for fade type.

- **Items to scroll** (number) - Number of slides to scroll at once. Default: 1. Supports breakpoints. Not available for fade type.

- **Speed in ms** (number) - Transition speed. Default: 400. Supports breakpoints.

- **Focus** (number) - Determines which slide should be active if the carousel has multiple slides in a page. Number/"center". Supports breakpoints.

#### Autoplay

- **Autoplay** (checkbox) - Enable automatic slide progression.

- **Pause on hover** (checkbox) - Pause autoplay when hovering over slider.

- **Pause on focus** (checkbox) - Pause autoplay when slider is focused.

- **Interval in ms** (number) - Time between slides. Default: 3000.

#### Rewind

Available when type is not "loop":

- **Rewind** (checkbox) - Enable rewind functionality.

- **Rewind by drag** (checkbox) - Allow rewinding by dragging.

- **Speed in ms** (number) - Rewind transition speed.

### Slide

- **Padding** (spacing) - Padding inside slides.

- **Align horizontal** (align-items) - Horizontal alignment of slide content. Options: `flex-start`, `center`, `flex-end`.

- **Align vertical** (justify-content) - Vertical alignment of slide content. Options: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`.

- **Background** (background) - Background styling for slides.

- **Border** (border) - Border styling for slides.

### Arrows

- **Show** (checkbox) - Display navigation arrows.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Color** (color) - Arrow icon color.

- **Size** (number with units) - Arrow icon size.

- **Text shadow** (text-shadow) - Text shadow for arrow icons.

#### Disabled

- **Background** (color) - Background color for disabled arrows.

- **Border** (border) - Border styling for disabled arrows.

- **Color** (color) - Icon color for disabled arrows.

- **Opacity** (number) - Opacity for disabled arrows (0-1).

#### Prev arrow

- **Prev arrow** (icon) - Custom icon for previous arrow.

- **Top** (number with units) - Top position. Default: 50%.

- **Right** (number with units) - Right position.

- **Bottom** (number with units) - Bottom position.

- **Left** (number with units) - Left position.

- **Transform** (transform) - CSS transform for previous arrow.

#### Next arrow

- **Next arrow** (icon) - Custom icon for next arrow.

- **Top** (number with units) - Top position. Default: 50%.

- **Right** (number with units) - Right position.

- **Bottom** (number with units) - Bottom position.

- **Left** (number with units) - Left position.

- **Transform** (transform) - CSS transform for next arrow.

### Pagination

- **Show** (checkbox) - Display pagination dots. Default: enabled.

- **Margin** (spacing) - Margin around pagination dots. Default: 5px on all sides.

- **Height** (number with units) - Dot height. Default: 10px.

- **Width** (number with units) - Dot width. Default: 10px.

- **Color** (color) - Dot color and background color.

- **Border** (border) - Border styling for dots.

#### Active

- **Height** (number with units) - Height for active dot.

- **Width** (number with units) - Width for active dot.

- **Color** (color) - Color for active dot.

- **Border** (border) - Border styling for active dot.

> **Developer reference**
>
> See the [Slider (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/slider-nested/) for the full JSON schema of this element's settings and controls.

---

# Carousel

Source: https://academy.bricksbuilder.io/builder/elements/media/carousel/

*The Carousel element displays images or posts in a swipeable carousel with customizable navigation and effects, using the Swiper library.*

The Carousel element displays images or posts in a swipeable carousel with customizable navigation and effects, using the Swiper library.

## Settings

- **Type** (select) - Content type. Options: `media`, `posts`. Default: `media`.

- **Images** (image-gallery) - Select images for the carousel. Only shown for media type.

- **Query** (query) - Configure which posts to display. Only shown for posts type.

### Settings

- **Adaptive height** (checkbox) - Adjust height to content.

- **Height** (number with units) - Fixed carousel height. Default: 300px. Not available when adaptive height is enabled.

- **Spacing** (number) - Spacing between slides in pixels. Default: 0.

- **Initial slide** (number) - Starting slide index. Default: 0.

- **Items to show** (number) - Number of slides visible at once. Default: 2. Supports breakpoints.

- **Items to scroll** (number) - Number of slides to advance per swipe. Default: 1. Supports breakpoints.

- **Effect** (select) - Transition effect. Options: `slide`, `fade`, `cube`, `coverflow`, `flip`. Default: `slide`.

- **Align items** (align-items) - Vertical alignment of slides. Only shown when adaptive height is enabled.

- **Loop** (checkbox) - Enable infinite loop. Default: true.

- **Center mode** (checkbox) - Center the active slide.

- **Disable lazy load** (checkbox) - Load all images immediately.

- **Autoplay** (checkbox) - Enable automatic sliding.

- **Pause on hover** (checkbox) - Pause autoplay on hover.

- **Stop on last slide** (checkbox) - Stop autoplay on last slide.

- **Autoplay delay in ms** (number) - Delay between slides in milliseconds. Default: 3000.

- **Animation speed in ms** (number) - Transition speed in milliseconds. Default: 300.

### Image

- **Hide image** (checkbox) - Hide images in post carousels.

- **Image size** (select) - Size of images.

- **Link to lightbox** (checkbox) - Open images in lightbox. Only for media type.

- **Image size** (select) - Size of images in lightbox.

- **Image click action** (select) - Action when clicking images. Options: `zoom`, `zoom-or-close`, `toggle-controls`, `next`, `close`. Default: `zoom`.

- **Animation** (select) - Lightbox animation type. Default: `zoom`.

- **Caption** (checkbox) - Show image captions in lightbox.

- **Thumbnail navigation** (checkbox) - Show thumbnail navigation in lightbox.

- **Thumbnail size** (number with units) - Size of thumbnails. Default: 60px.

- **Padding** (dimensions) - Lightbox padding in pixels.

### Fields

- **Fields** (repeater) - Configure which post fields to display. Each field has:
  - **Dynamic data** (text) - Dynamic data tag (e.g., `{post_title:link}`, `{post_excerpt:20}`).
  - **HTML tag** (select) - HTML tag for the field. Options: `div`, `p`, `h1`-`h6`. Default: `div`.
  - **Width** (number with units) - Field width.
  - **Margin** (spacing) - Field margin.
  - **Padding** (spacing) - Field padding.
  - **Background color** (color) - Field background color.
  - **Border** (border) - Field border styling.
  - **Typography** (typography) - Field text styling.
  - **Overlay** (checkbox) - Show field as overlay.

### Content

- **Alignment** (select) - Content alignment. Options: `top left`, `top center`, `top right`, `middle left`, `middle center`, `middle right`, `bottom left`, `bottom center`, `bottom right`.

- **Min. height** (number with units) - Minimum content height.

- **Margin** (spacing) - Content wrapper margin.

- **Padding** (spacing) - Content wrapper padding.

- **Background color** (color) - Content wrapper background color.

### Overlay

- **Show on hover** (checkbox) - Show overlay only on hover.

- **Fade in animation** (select) - Overlay animation. Options: `fade-in-up`, `fade-in-right`, `fade-in-down`, `fade-in-left`, `zoom-in`, `zoom-out`.

- **Alignment** (select) - Overlay alignment. Options: `top left`, `top center`, `top right`, `middle left`, `middle center`, `middle right`, `bottom left`, `bottom center`, `bottom right`.

- **Margin** (spacing) - Overlay margin.

- **Padding** (spacing) - Overlay padding.

- **Background color** (color) - Overlay background color.

- **Inner background color** (color) - Inner overlay background color.

## Arrows

- **Show arrows** (checkbox) - Display navigation arrows. Default: true.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Typography** (typography) - Arrow button text styling.

### Prev arrow

- **Prev arrow** (icon) - Previous arrow icon. Default: `ion-ios-arrow-back`.

- **Top** (number with units) - Previous arrow top position. Default: 50%.

- **Right** (number with units) - Previous arrow right position.

- **Bottom** (number with units) - Previous arrow bottom position.

- **Left** (number with units) - Previous arrow left position. Default: 50px.

### Next arrow

- **Next arrow** (icon) - Next arrow icon. Default: `ion-ios-arrow-forward`.

- **Top** (number with units) - Next arrow top position.

- **Right** (number with units) - Next arrow right position.

- **Bottom** (number with units) - Next arrow bottom position.

- **Left** (number with units) - Next arrow left position.

## Dots

- **Show dots** (checkbox) - Display pagination dots.

- **Dynamic dots** (checkbox) - Enable dynamic bullet pagination.

- **Vertical** (checkbox) - Display dots vertically.

- **Height** (number with units) - Dot height.

- **Width** (number with units) - Dot width.

- **Top** (number with units) - Dots container top position.

- **Right** (number with units) - Dots container right position.

- **Bottom** (number with units) - Dots container bottom position.

- **Left** (number with units) - Dots container left position.

- **Border** (border) - Dot border styling.

- **Color** (color) - Inactive dot color.

- **Active color** (color) - Active dot color.

- **Margin** (spacing) - Margin around individual dots. Default: 0px top, 5px right, 0px bottom, 0px left.

> **Developer reference**
>
> See the [Carousel Schema](https://academy.bricksbuilder.io/developer/schema/elements/carousel/) for the full JSON schema of this element's settings and controls.

---

# Slider

Source: https://academy.bricksbuilder.io/builder/elements/media/slider/

*The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library.*

The Slider element creates a full-width image slider with customizable slides containing titles, content, and buttons, using the Swiper library.

## Security scanner reports

Bricks 2.4 patches the legacy Swiper build used by the classic Slider element. The bundled asset is a Bricks-patched vendored Swiper 8 legacy build with the CVE-2026-27212 / GHSA-hmx5-qpq5-p643 mitigation backported.

Bricks keeps the Swiper 8 runtime behavior so existing sliders continue to behave as before, including loop configurations that depend on Swiper 8 duplicate slides. The public `bricks-swiper` script version is `bricks-cve-2026-27212-p1`, and the bundled file no longer reports stock `Swiper 8.4.4` in its header.

Some security scanners may still fingerprint the underlying minified Swiper 8 code and flag it. Use this VEX or exception note: `Bricks-patched vendored Swiper 8 legacy build with CVE-2026-27212 backport.`

## Settings

- **Slides** (repeater) - Add slider slides. Each slide has:
  - **Title** (text) - Slide title.
  - **Title Tag** (select) - HTML tag for title. Options: `h1`-`h6`. Default: `h3`.
  - **Content** (rich text) - Slide content.
  - **Button text** (text) - Call-to-action button text.
  - **Button style** (select) - Button style. Default: `light`.
  - **Button size** (select) - Button size.
  - **Button width** (number with units) - Button width.
  - **Button link** (link) - Button destination.
  - **Button background** (color) - Button background color.
  - **Button border** (border) - Button border styling.
  - **Button box shadow** (box-shadow) - Button shadow.
  - **Button typography** (typography) - Button text styling.
  - **Background** (background) - Slide background (color, image, gradient).
  - **Overlay** (color) - Overlay color over the background.

- **Slides to show** (number) - Number of slides visible at once. Default: 1.

- **Slides to scroll** (number) - Number of slides to advance per transition. Default: 1.

- **Spacing** (number) - Spacing between slides in pixels. Default: 0.

- **Height** (number with units) - Slider height. Default: 300px.

- **Effect** (select) - Transition effect. Options: `slide`, `fade`, `cube`, `coverflow`, `flip`. Default: `slide`.

- **Loop** (select) - Enable infinite loop. Options: `enable`, `disable`. Default: `enable`.

- **Center mode** (checkbox) - Center the active slide.

- **Disable lazy load** (checkbox) - Load all images immediately.

- **Autoplay** (checkbox) - Enable automatic sliding.

- **Pause on hover** (checkbox) - Pause autoplay on hover.

- **Stop on last slide** (checkbox) - Stop autoplay on the last slide.

- **Autoplay delay in ms** (number) - Delay between slides in milliseconds. Default: 3000.

- **Animation speed in ms** (number) - Transition speed in milliseconds. Default: 300.

### Title

- **Title margin** (spacing) - Margin around slide titles.

- **Title typography** (typography) - Font settings for slide titles.

### Content

- **Content width** (number with units) - Maximum width of slide content.

- **Content background** (color) - Background color for slide content.

- **Content typography** (typography) - Font settings for slide content.

- **Content margin** (spacing) - Margin around slide content.

- **Content padding** (spacing) - Padding inside slide content. Default: 30px top, 60px right, 30px bottom, 60px left.

- **Content align horizontal** (justify-content) - Horizontal alignment of content within slides.

- **Content align vertical** (align-items) - Vertical alignment of content within slides.

- **Content text align** (text-align) - Text alignment within slide content.

### Button

- **Button style** (select) - Global button style. Default: `light`.

- **Button size** (select) - Global button size.

- **Button width** (number with units) - Global button width.

- **Background** (color) - Global button background color.

- **Border** (border) - Global button border styling.

- **Box shadow** (box-shadow) - Global button shadow.

- **Typography** (typography) - Global button text styling.

### Background

- **Top** (number with units) - Background image top position.

- **Right** (number with units) - Background image right position.

- **Bottom** (number with units) - Background image bottom position.

- **Left** (number with units) - Background image left position.

## Arrows

- **Show arrows** (checkbox) - Display navigation arrows. Default: true.

- **Height** (number with units) - Arrow button height. Default: 50px.

- **Width** (number with units) - Arrow button width. Default: 50px.

- **Background** (color) - Arrow button background color.

- **Border** (border) - Arrow button border styling.

- **Typography** (typography) - Arrow button text styling.

### Prev arrow

- **Prev arrow** (icon) - Previous arrow icon. Default: `ion-ios-arrow-back`.

- **Top** (number with units) - Previous arrow top position. Default: 50%.

- **Right** (number with units) - Previous arrow right position.

- **Bottom** (number with units) - Previous arrow bottom position.

- **Left** (number with units) - Previous arrow left position. Default: 50px.

- **Transform** (transform) - Previous arrow transformations.

### Next arrow

- **Next arrow** (icon) - Next arrow icon. Default: `ion-ios-arrow-forward`.

- **Top** (number with units) - Next arrow top position.

- **Right** (number with units) - Next arrow right position.

- **Bottom** (number with units) - Next arrow bottom position.

- **Left** (number with units) - Next arrow left position.

- **Transform** (transform) - Next arrow transformations.

## Dots

- **Show dots** (checkbox) - Display pagination dots.

- **Dynamic dots** (checkbox) - Enable dynamic bullet pagination.

- **Vertical** (checkbox) - Display dots vertically.

- **Height** (number with units) - Dot height.

- **Width** (number with units) - Dot width.

- **Top** (number with units) - Dots container top position.

- **Right** (number with units) - Dots container right position.

- **Bottom** (number with units) - Dots container bottom position.

- **Left** (number with units) - Dots container left position.

- **Border** (border) - Dot border styling.

- **Color** (color) - Inactive dot color.

- **Active color** (color) - Active dot color.

- **Margin** (spacing) - Margin around individual dots.

> **Developer reference**
>
> See the [Slider Schema](https://academy.bricksbuilder.io/developer/schema/elements/slider/) for the full JSON schema of this element's settings and controls.

---

# SVG

Source: https://academy.bricksbuilder.io/builder/elements/media/svg/

*The SVG element displays SVG graphics from files, dynamic data, custom code, or icon sets.*

The SVG element displays SVG graphics from files, dynamic data, custom code, or icon sets.

## Settings

- **Source** (select) - SVG source type. Options: `file` (default), `dynamicData`, `code`, `iconSet`.

- **File** (svg upload) - Upload an SVG file from your computer. Available when source is "file".

- **Icon set** (icon) - Select an SVG from custom icon libraries. Available when source is "iconSet".

- **Dynamic data** (text with dynamic data) - Load SVG from dynamic data. Supported field types: File, Image, SVG code, URL. Available when source is "dynamicData".

- **Code** (code editor) - Paste SVG code directly. Only available to users with code execution permissions. Ensure SVG code is safe and doesn't contain malicious code. Consider using an SVG cleaner like svgomg.net. Available when source is "code".

### Styling

- **Height** (number with units) - SVG height.

- **Width** (number with units) - SVG width.

- **Stroke width** (number) - Width of SVG stroke lines. Minimum: 1.

- **Stroke color** (color) - Color of SVG stroke elements (excludes elements with `stroke="none"`).

- **Fill** (color) - Fill color for SVG shapes (excludes elements with `fill="none"`).

- **Link** (link) - Make the SVG clickable by adding a link.

> **Developer reference**
>
> See the [SVG Schema](https://academy.bricksbuilder.io/developer/schema/elements/svg/) for the full JSON schema of this element's settings and controls.

---

# Accordion (nestable)

Source: https://academy.bricksbuilder.io/builder/elements/general/accordion-nested/

*The Nestable Accordion element allows creating hierarchical collapsible content with drag-and-drop nesting in the builder.*

The Nestable Accordion element allows creating hierarchical collapsible content with drag-and-drop nesting in the builder.

## Settings

- **Children** (nestable) - Drag and drop elements to create accordion items. Each item can contain nested content. Set "ID" on items to open via anchor link (no spaces, no pound sign).

- **Expand item indexes** (text) - Comma-separated indexes of items to expand on page load (starting at 0).

- **Independent toggle** (checkbox) - Allow multiple items to be open simultaneously. Enable to open & close an item without toggling other items.

- **Transition (ms)** (number) - Animation duration for expanding/collapsing in milliseconds. Default: 200.

- **FAQ schema** (checkbox) - Generate FAQPage structured data (JSON-LD) for search engines.

### Title

- **Min. height** (number with units) - Minimum height for title areas. Default: 50px.

- **Margin** (spacing) - Margin around title wrappers.

- **Padding** (spacing) - Padding inside title wrappers.

- **Background color** (color) - Background color for title wrappers.

- **Border** (border) - Border styling for title wrappers.

- **Typography** (typography) - Typography settings for title text and headings.

#### Active Title

- **Background color** (color) - Background color for active/expanded title wrappers.

- **Border** (border) - Border styling for active/expanded title wrappers.

- **Typography** (typography) - Typography settings for active/expanded title text and headings.

### Content

- **Margin** (spacing) - Margin around content wrappers.

- **Padding** (spacing) - Padding inside content wrappers. Default: 15px top/bottom, 0px left/right.

- **Background color** (color) - Background color for content wrappers.

- **Border** (border) - Border styling for content wrappers.

- **Typography** (typography) - Typography settings for content text.

> **Developer reference**
>
> See the [Accordion (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/accordion-nested/) for the full JSON schema of this element's settings and controls.

---

# Alert

Source: https://academy.bricksbuilder.io/builder/elements/general/alert/

*The Alert element displays informational messages with different types and optional dismiss functionality.*

The Alert element displays informational messages with different types and optional dismiss functionality.

## Settings

- **Content** (rich text) - The alert message content. Supports dynamic data and rich text.

- **Type** (select) - The alert style type. Options: `info`, `success`, `warning`, `danger`, `muted`. Default: `info`.

- **Dismissable** (checkbox) - Adds a close button to allow users to dismiss the alert.

> **Developer reference**
>
> See the [Alert Schema](https://academy.bricksbuilder.io/developer/schema/elements/alert/) for the full JSON schema of this element's settings and controls.

---

# Animated typing

Source: https://academy.bricksbuilder.io/builder/elements/general/animated-typing/

*The Animated Typing element creates a typewriter effect that cycles through a list of strings with customizable timing and behavior.*

The Animated Typing element creates a typewriter effect that cycles through a list of strings with customizable timing and behavior.

## Settings

- **Tag** (select) - The HTML tag to use for the element. Options: `div`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`. Default: `div`.

- **Prefix** (text) - Text displayed before the animated strings. Default: "We ".

- **Suffix** (text) - Text displayed after the animated strings. Default: " for you!".

- **Strings** (repeater) - List of strings to cycle through. Each item has a **Text** field. Default: "design", "code", "launch".

### Settings

- **Type speed in ms** (number) - Speed of typing each character. Default: 55.

- **Back speed in ms** (number) - Speed of deleting each character. Default: 30.

- **Start delay in ms** (number) - Delay before starting the animation. Default: 500.

- **Back delay in ms** (number) - Delay before starting to delete. Default: 500.

- **Cursor character** (text) - Character used as the cursor. Default: "|".

- **Loop** (checkbox) - Repeat the animation indefinitely. Default: checked.

- **Shuffle** (checkbox) - Randomize the order of strings each cycle.

> **Developer reference**
>
> See the [Anim. Typing Schema](https://academy.bricksbuilder.io/developer/schema/elements/animated-typing/) for the full JSON schema of this element's settings and controls.

---

# Accordion

Source: https://academy.bricksbuilder.io/builder/elements/general/accordion/

*The Accordion element creates collapsible content sections with titles and expandable content.*

The Accordion element creates collapsible content sections with titles and expandable content.

## Settings

- **Accordion** (repeater) - Add accordion items. Each item has:
  - **Title** (text) - The clickable title of the accordion item.
  - **ID** (text) - Anchor ID for linking to the item (no spaces, no pound sign).
  - **Subtitle** (text) - Optional subtitle below the title.
  - **Content** (rich text) - The expandable content of the item.

- **Expand item indexes** (text) - Comma-separated indexes of items to expand on page load (starting at 0).

- **Independent toggle** (checkbox) - Allow multiple items to be open simultaneously. Enable to open & close an item without toggling other items.

- **Transition (ms)** (number) - Animation duration for expanding/collapsing in milliseconds. Default: 200.

- **FAQ schema** (checkbox) - Generate FAQPage structured data (JSON-LD) for search engines.

### Title

- **HTML tag** (select) - HTML tag for titles. Options: `div`, `h1`-`h6`. Default: `h3`.

- **Icon** (icon) - Icon for collapsed state. Default: right arrow (ion-ios-arrow-forward).

- **Icon typography** (typography) - Font settings for the collapsed icon.

- **Icon expanded** (icon) - Icon for expanded state. Default: down arrow (ion-ios-arrow-down).

- **Icon expanded typography** (typography) - Font settings for the expanded icon.

- **Icon position** (select) - Position of the icon relative to text. Default: Right.

- **Icon rotate in °** (number) - Rotation angle for the icon in degrees. Icon rotation for expanded accordion.

- **Margin** (spacing) - Margin around title wrappers.

- **Padding** (spacing) - Padding inside title wrappers.

- **Title typography** (typography) - Typography settings for title text.

- **Subtitle typography** (typography) - Typography settings for subtitle text.

- **Background color** (color) - Background color for title wrappers.

- **Border** (border) - Border styling for title wrappers.

- **Box shadow** (box-shadow) - Box shadow for title wrappers.

- **Active typography** (typography) - Typography settings for active/expanded title text.

- **Active background** (color) - Background color for active/expanded title wrappers.

- **Active border** (border) - Border styling for active/expanded title wrappers.

### Content

- **Margin** (spacing) - Margin around content wrappers.

- **Padding** (spacing) - Padding inside content wrappers.

- **Content typography** (typography) - Typography settings for content text.

- **Background color** (color) - Background color for content wrappers.

- **Border** (border) - Border styling for content wrappers.

> **Developer reference**
>
> See the [Accordion Schema](https://academy.bricksbuilder.io/developer/schema/elements/accordion/) for the full JSON schema of this element's settings and controls.

---

# Back to Top

Source: https://academy.bricksbuilder.io/builder/elements/general/back-to-top/

*The Back to Top element renders a button (default tag: button) that scrolls the visitor back to the top of the page. It is nestable: you typically place an Icon.*

The **Back to Top** element renders a button (default tag: `button`) that scrolls the visitor back to the top of the page. It is **nestable**: you typically place an **Icon** and/or **Text** element inside it (the defaults use an up-arrow icon and the label “Back to Top”).

## Settings

- **HTML tag** (text) — Root element tag. Default: `button`.

- **aria-label** (text) — Accessible name when the control has no visible descriptive text.

### Position

- **Position** (select) — CSS `position` (placeholder suggests `fixed`).
- **Top**, **Right**, **Bottom**, **Left** (number with units) — Position offsets.

### Misc

Bricks surfaces **z-index**, **gap** (space between nested children), and **CSS transition** on this element (moved from the default tabs).

- **Visible after** (number) — Show the button only after the user has scrolled this many pixels. If empty and **Visible on scroll up** is off, the button stays visible.
- **Visible on scroll up** (checkbox) — Show the button when the user scrolls upward.
- **Smooth scroll** (checkbox) — Smooth scroll to the top when activated.
- **Move focus to top** (checkbox) — Move keyboard focus to the top of the page after activation (accessibility).

> **Developer reference**
>
> See the [Back to Top Schema](https://academy.bricksbuilder.io/developer/schema/elements/back-to-top/) for the full JSON schema of this element's settings and controls.

---

# Breadcrumbs

Source: https://academy.bricksbuilder.io/builder/elements/general/breadcrumbs/

*Breadcrumbs are an essential part of website navigation, providing users with a clear path to navigate through the site hierarchy. They improve the overall user.*

Breadcrumbs are an essential part of website navigation, providing users with a clear path to navigate through the site hierarchy. They improve the overall user experience by helping users know their location within the site and easily navigate back to previous pages.

The Breadcrumbs element generates different breadcrumb items depending on the type of page being viewed.

It supports various page types, including single posts or pages (`is_singular()`), the homepage (`is_home()`), categories (`is_category()`), taxonomies (`is_tax()`), post type archives (`is_post_type_archive()`), tags (`is_tag()`), date archives (`is_date()`), author pages (`is_author()`), search results (`is_search()`), and error pages (`is_404()`).

![](https://academy.bricksbuilder.io/assets/breadcrumbs-element.png)

## Settings

- **Gap** (number with units) - Gap between breadcrumb items. Controls `gap` property.

### Structure

This section allows you to customize the structure of breadcrumb items. Currently it supports single pages and the date archive.

#### Date archive structure

![](https://academy.bricksbuilder.io/assets/date-archive-context.png)

#### Single page structure

![](https://academy.bricksbuilder.io/assets/breadcrumbs-structure-section.png)

By default, Bricks displays breadcrumb items as follows:

For posts:  
`Home` > `Parent categories (if any)` > `Category (if any)` > `Post parents (if any)` > `Current post`

For other post types:  
`Home` > `Post archives` > `Post parents (if any)` > `Current post`  
  
You can customize the breadcrumb structure for different post types. You can also group multiple post types together if you want them to share the same structure. Any post type not specifically defined in your custom structures will automatically use the default structure.

**Example 1:**  
For the Tanks post type singular page, I want to display the post type archive and the custom taxonomy as breadcrumb items.

![](https://academy.bricksbuilder.io/assets/structure-example-1.png)

![](https://academy.bricksbuilder.io/assets/result-example-1.png)

**Example 2:**  
For the products singular page, I want to display custom taxonomy as breadcrumb items.

![](https://academy.bricksbuilder.io/assets/structure-example-2.png)

![](https://academy.bricksbuilder.io/assets/result-example-2.png)

- **Post types** (repeater) - Define custom breadcrumb structures for specific post types.
  - **Post types** (select, multiple) - Select post types to apply this structure to. Options: registered post types. Default: Posts.
  - **Hide current post** (checkbox) - Hide the current post from breadcrumbs.
  - **Show parent posts** (checkbox) - Show parent posts in hierarchy.
  - **Show post type archive** (checkbox) - Show post type archive link.
  - **Show taxonomy** (checkbox) - Show taxonomy in breadcrumbs.
  - **Taxonomy slug** (text) - Taxonomy slug to display. Required when Show taxonomy is enabled. Default: "category".
  - **Taxonomy info** (info) - Only the first assigned term will be displayed. Only shown when Show taxonomy is enabled.
  - **Show parent terms** (checkbox) - Show parent terms in hierarchy. Only works if the first assigned term is a child term.

- **Date** (separator) - Date-related breadcrumb settings.

- **Add context** (checkbox) - Add context to dates on archive templates.

### Home

![](https://academy.bricksbuilder.io/assets/breadcrumbs-home-section.png)

In this section, you can customize the root item (home) of the breadcrumb trail. Adjust the URL, change the label text, select an icon, and determine the icon's position.

- **URL** (text) - Custom URL for home link. Default: home URL.

- **Text** (text) - Label for home link. Default: "Home".

- **Icon** (icon) - Icon for home link.

- **Icon: Gap** (number with units) - Gap between home icon and label. Controls `gap` property for `.item:has(> svg), .item:has(> i)` selector. Only available when Icon is set.

- **Icon: Position** (select) - Position of home icon. Options: Before, After. Default: Before. Only available when Icon is set.

- **Hide label** (checkbox) - Hide home label when icon is present. Only available when Icon is set.

### Separator

![](https://academy.bricksbuilder.io/assets/breadcrumbs-separator-section.png)

Here, you can modify the appearance and behavior of the separators between breadcrumb links, adjusting both display mode and styling.

- **Separator** (select) - Separator type. Options: Text, Icon, None. Default: Text.

- **Separator** (text) - Separator text. Default: "/". Only available when Separator is Text or empty.

- **Icon** (icon) - Separator icon. Only available when Separator is Icon.

- **Color** (color) - Separator color. Controls `color` property for `.separator` selector.

- **Size** (number with units) - Separator size. Controls `font-size` property for `.separator` selector.

### Item

![](https://academy.bricksbuilder.io/assets/breadcrumbs-item-section.png)

This section allows you to style each breadcrumb link.

- **Padding** (spacing) - Padding for breadcrumb items. Controls `padding` property for `.item` selector.

- **Background color** (color) - Background color for breadcrumb items. Controls `background-color` property for `.item` selector.

- **Border** (border) - Border settings for breadcrumb items. Controls `border` property for `.item` selector.

- **Typography** (typography) - Typography for breadcrumb items. Controls `font` property for `.item` selector.

### Current

![](https://academy.bricksbuilder.io/assets/breadcrumbs-current-section.png)

Use these settings to style the last item in the breadcrumb trail, which represents the current page or post.

- **Padding** (spacing) - Padding for current page item. Controls `padding` property for `.item[aria-current="page"]` selector.

- **Background color** (color) - Background color for current page item. Controls `background-color` property for `.item[aria-current="page"]` selector.

- **Border** (border) - Border settings for current page item. Controls `border` property for `.item[aria-current="page"]` selector.

- **Typography** (typography) - Typography for current page item. Controls `font` property for `.item[aria-current="page"]` selector.

> **Developer reference**
>
> See the [Breadcrumbs Schema](https://academy.bricksbuilder.io/developer/schema/elements/breadcrumbs/) for the full JSON schema of this element's settings and controls.

---

# Code

Source: https://academy.bricksbuilder.io/builder/elements/general/code/

*The Code element allows you to add and execute PHP, HTML, CSS, or JavaScript code with syntax highlighting and optional code execution.*

The Code element allows you to add and execute PHP, HTML, CSS, or JavaScript code with syntax highlighting and optional code execution.

## Settings

### Code Execution

Available only for users with code execution permissions:

- **Execute code** (checkbox) - Run the code on your site instead of displaying it. Only add code you consider safe.

- **Parse dynamic data** (checkbox) - Parse dynamic data tags within the code. Only available when execute code is enabled.

- **Suppress PHP errors** (checkbox) - Hide PHP errors from displaying. Add "brx_code_errors" as a URL parameter to show errors if needed. Only available when execute code is enabled.

- **Render without wrapper** (checkbox) - Render on the frontend without the div wrapper. Style tab settings won't apply when this is enabled. Only available when execute code is enabled.

### Code Editors

Available when code execution is disabled or not allowed:

- **PHP & HTML** (code editor) - PHP and HTML code editor with syntax highlighting. Supports dynamic data and variables. Default example includes HTML heading and PHP date output.

- **CSS** (code editor) - CSS code editor with syntax highlighting. CSS is automatically wrapped in style tags. Supports dynamic data and variables.

- **JavaScript** (code editor) - JavaScript code editor with syntax highlighting. JavaScript is automatically wrapped in script tags. Supports dynamic data.

### Syntax Highlighting

Available when code execution is disabled:

- **Theme** (select) - Code syntax highlighting theme. Options: `github` (light), `tomorrow` (light), `tomorrow-night` (dark), `tranquil-heart` (dark). Default: None. Can also be set globally via theme styles.

> **Developer reference**
>
> See the [Code Schema](https://academy.bricksbuilder.io/developer/schema/elements/code/) for the full JSON schema of this element's settings and controls.

---

# Countdown

Source: https://academy.bricksbuilder.io/builder/elements/general/countdown/

*The Countdown element displays a countdown timer to a specified date with customizable fields and actions.*

The Countdown element displays a countdown timer to a specified date with customizable fields and actions.

## Settings

- **Date** (datepicker) - The target date and time for the countdown.

- **Time zone** (select) - The time zone for the countdown calculation. Options include various UTC offsets. Default: UTC+00:00.

- **Date Reached** (select) - Action when the countdown reaches zero. Options: `countdown` (show countdown), `hide` (hide element), `text` (show custom text). Default: `countdown`.

- **Date Reached: Custom text** (text) - Custom text to display when the date is reached. Only shown when "Date Reached" is set to "text".

### Fields

- **Fields** (repeater) - Configure the countdown display fields. Each field has:
  - **Prefix** (text) - Text before the field value.
  - **Format** (text) - Format string using %D (days), %H (hours), %M (minutes), %S (seconds). Lowercase removes leading zeros. Default: "%D days", "%H hours", "%M minutes", "%S seconds".
  - **Suffix** (text) - Text after the field value.

- **Direction** (direction) - Flex direction for the fields container.

- **Align main axis** (justify-content) - Justify content alignment for fields.

- **Align cross axis** (align-items) - Align items for fields.

### Field

- **Direction** (direction) - Flex direction for individual fields.

- **Margin** (spacing) - Margin around individual fields. Default: 0 5px 0 0.

## Dynamic target dates

The Date control accepts a date returned by dynamic data. Bricks supports common date strings such as `YYYY-MM-DD HH:MM`, `YYYY-MM-DD`, and ISO 8601, plus Unix timestamps in seconds or milliseconds.

The dynamic tag must resolve to a plain date or timestamp. Place the Countdown inside a query loop or template to let each post or product resolve its own target date.

For a WooCommerce sale countdown, use the sale end date as the target. The Countdown tracks one date, so use element conditions when it should appear only after a sale starts or while a product is on sale. Bricks does not provide dedicated WooCommerce sale start and end date tags. Store the target in a custom field or provide it through a custom dynamic tag or helper that returns one of the supported formats.

> **Developer reference**
>
> See the [Countdown Schema](https://academy.bricksbuilder.io/developer/schema/elements/countdown/) for the full JSON schema of this element's settings and controls.

---

# Counter

Source: https://academy.bricksbuilder.io/builder/elements/general/counter/

*The Counter element animates a number from a starting value to an ending value with customizable prefix, suffix, and formatting.*

The Counter element animates a number from a starting value to an ending value with customizable prefix, suffix, and formatting.

## Settings

- **Count from** (text) - The starting number for the animation. Default: 0.

- **Count to** (text) - The ending number for the animation. Default: 1000.

- **Animation in ms** (number) - Duration of the counting animation in milliseconds. Default: 1000.

- **Typography** (typography) - Font settings for the counter number.

### Prefix

- **Prefix** (text) - Text displayed before the counter number.

- **Typography** (typography) - Font settings for the prefix text.

### Suffix

- **Suffix** (text) - Text displayed after the counter number.

- **Typography** (typography) - Font settings for the suffix text.

### Separator

- **Thousand separator** (checkbox) - Add thousand separators to the number.

- **Separator** (text) - Character used as the thousand separator. Default: ",". Only shown when "Thousand separator" is enabled.

> **Developer reference**
>
> See the [Counter Schema](https://academy.bricksbuilder.io/developer/schema/elements/counter/) for the full JSON schema of this element's settings and controls.

---

# Dropdown

Source: https://academy.bricksbuilder.io/builder/elements/general/dropdown/

*The Dropdown element is a nestable menu item: a toggle (link/text + optional icon button) with a dropdown panel (default inner structure is a Div with tag ul.*

The **Dropdown** element is a **nestable** menu item: a toggle (link/text + optional icon button) with a **dropdown panel** (default inner structure is a **Div** with tag `ul` and class `brx-dropdown-content` containing links). Use it inside [Nav (Nestable)](https://academy.bricksbuilder.io/builder/elements/general/nav-nested/) or similar structures.

Default HTML tag for the root is **`li`**. The script `bricksSubmenuPosition` handles positioning.

## Top-level

- **HTML tag** (text) — Root tag; validated in the builder. Placeholder: `li`.

- **Text** (text) — Label for the trigger. Default: “Dropdown”.

- **Link to** (link) — Optional link around the text (lightbox fields excluded).

- **Attribute: aria-label** (text) — Applied to the **toggle button** when an icon is present. Placeholder: “Toggle dropdown”.

## Icon

- **Icon** (icon) — If set, shown in the toggle **button** next to the text.

- **Icon padding** (spacing) — On `.brx-submenu-toggle button`.

- **Gap** (number with units) — Flex gap on `.brx-submenu-toggle`.

- **Icon position** (select) — Uses flex direction (`row-reverse` when set to place icon on the **left**).

- **Icon size** (number with units) — `font-size` on the button.

- **Icon color** (color).

- **Icon transform**, **Icon transform (Open)** (transform) — Default vs `aria-expanded="true"`.

- **Icon transition** (text) — CSS `transition` on the button.

## Caret

Optional triangle on the dropdown root (adds class `caret` when **Size** is set):

- **Size** (number with units) — `border-width` on `> .brx-dropdown-content::before`.

- **Color** (color) — `border-bottom-color` (when size ≠ 0).

- **Transform** (transform).

- **Position** (dimensions).

## Content

- **Position: Static** (checkbox) — Keeps the panel in document flow (e.g. inside [Offcanvas](https://academy.bricksbuilder.io/builder/elements/general/offcanvas/)). Static dropdowns **always toggle on click**, not hover.

- **Toggle on** (select) — `click`, `hover`, or `click or hover`. Hidden when **Static** is enabled (click only).

- **Min. width** (number with units) — On `.brx-dropdown-content`.

- **Transition** (text), **Transform**, **Transform (Open)** — Panel motion (`&.open > .brx-dropdown-content` for open state).

- **Background** (background), **Border**, **Box shadow**, **Typography** — Panel chrome on `.brx-dropdown-content`.

### Item

Row styling for direct links and submenu toggles inside the panel:

- **Justify content** (justify-content).

- **Padding** (spacing).

- **Background** (color), **Border** (border), **Typography**, **Transition** (text).

### Active

States matching `aria-current="page"` / `.aria-current`:

- **Background**, **Border**, **Typography**.

## Mega menu

- **Enable** (checkbox) — Full-width style mega panel (`brx-has-megamenu`); “covers entire available width” by default.

- **CSS selector (Horizontal)** (text) — Optional: align width/horizontal position to another node.

- **CSS selector (Vertical)** (text) — Optional: vertical alignment reference.

## Multilevel

- **Enable** (checkbox) — Shows one submenu level at a time; toggles on click; inner dropdowns inherit multilevel behavior.

- **Back: Text** (text) — Back control label (default “Back”).

- **Back: Typography**, **Back: Background** — `.brx-multilevel-back` styling.

> **Developer reference**
>
> See the [Dropdown Schema](https://academy.bricksbuilder.io/developer/schema/elements/dropdown/) for the full JSON schema of this element's settings and controls.

---

# Facebook page

Source: https://academy.bricksbuilder.io/builder/elements/general/facebook-page/

*The Facebook Page element embeds a Facebook page plugin with customizable display options.*

The Facebook Page element embeds a Facebook page plugin with customizable display options.

## Settings

- **Facebook page URL** (text) - The URL of the Facebook page to embed. Default: "https://facebook.com/facebook".

- **Height (px)** (number) - Height of the embedded page in pixels. Minimum: 70, Maximum: 500. Default: 500.

- **Width (px)** (number) - Width of the embedded page in pixels. Minimum: 180, Maximum: 500. Default: 340.

- **Tabs** (select) - Tabs to display on the page plugin. Options: `timeline`, `events`, `messages`. Multiple selection allowed.

- **Hide cover** (checkbox) - Hide the page cover photo.

- **Show friends' photos** (checkbox) - Display profile photos of the page's friends.

- **Hide CTA button** (checkbox) - Hide the call-to-action button.

- **Small header** (checkbox) - Use a smaller header size.

> **Developer reference**
>
> See the [Facebook Page Schema](https://academy.bricksbuilder.io/developer/schema/elements/facebook-page/) for the full JSON schema of this element's settings and controls.

---

# Form

Source: https://academy.bricksbuilder.io/builder/elements/general/form/

*Build forms, validate submissions, and run email, integration, authentication, post, and custom actions with the Form element.*

The Form element lets you build custom forms with the following form field types:

- Email
- Text
- Textarea
- Telephone
- Number
- URL
- Image (media library)
- Gallery (media library)
- Checkbox
- Select (dropdown)
- Radio
- Password
- Remember me
- Datepicker
- File upload
- Hidden

You can define **actions** triggered by form submissions like sending an email notification, redirecting to a certain page, communicating to SendGrid or Mailchimp servers, or user login/registration. If this is not enough, you can also develop your own actions.

The form element also integrates with [Google reCaptcha V3](#spam), [hCaptcha](https://www.hcaptcha.com/), and [Cloudflare Turnstile](https://www.cloudflare.com/products/turnstile/) to protect your sites from fraudulent activities, spam, and abuse. Supports dynamic data, and [form validation](#form-validation) through a new action hook.

## Actions {#actions}

Form actions run after the form has been submitted successfully.

You may set one or multiple actions for your form. Actions run in the sequence they have been selected, except for the "Redirect" action, which always runs at the very end.

For each selected action, a separate control group appears.

![Bricks Form element - email action settings](https://academy.bricksbuilder.io/assets/form-mail-action.jpg)

<figcaption>

Form element: email action settings

</figcaption>

### Conditional actions (@since 2.4) {#conditional-actions}

Use **Action conditions** to run a selected action only when submitted form data matches your rules. An action without an action rule always runs after a successful submission.

To add a rule:

1. Select every action the form may run under **Actions after successful form submit**.
2. Under **Action conditions**, click **Add action rule**.
3. Choose the **Action** to control. The list only includes actions selected for the current form.
4. Under **Run action if**, choose a form **Field** and a **Compare** operator.
5. Enter a **Value** when the selected operator requires one.
6. Add more conditions if needed, then set **Relation** to **And** or **Or**.

<div className="screenshot screenshot--control-panel">

![](https://academy.bricksbuilder.io/assets/form-action-conditions.webp)

</div>

The available comparison operators are:

| Operator             | The condition matches when                    |
| -------------------- | --------------------------------------------- |
| **is**               | A submitted value exactly matches **Value**.  |
| **is not**           | No submitted value exactly matches **Value**. |
| **contains**         | A submitted value contains **Value**.         |
| **does not contain** | No submitted value contains **Value**.        |
| **is empty**         | The field has no submitted value.             |
| **is not empty**     | The field has a submitted value.              |

For fields that can submit multiple values, such as checkboxes, Bricks checks each submitted value. Use **is empty** or **is not empty** when the presence of a selection matters more than its exact value.

#### Example: Subscribe only after consent

A contact form can always send an enquiry email while subscribing only people who select a marketing consent checkbox:

1. Add a checkbox field for marketing consent. Do not make it required if visitors must be able to submit the enquiry without subscribing.
2. Select both **Email** and **Mailchimp** under **Actions after successful form submit**.
3. Add an action rule and select **Mailchimp** as the action.
4. Under **Run action if**, select the consent checkbox and set **Compare** to **is not empty**.

The **Email** action has no rule, so it runs for every successful submission. **Mailchimp** runs only when the checkbox has a submitted value.

> **Note**
>
> Within one action rule, **And** requires every condition to match, while **Or** requires at least one condition to match. If you add multiple action rules for the same action, every rule must pass.

HTML fields are not available as condition fields because they do not submit values. File-field conditions include newly uploaded files and verified files retained by an **Update post** form. An incomplete rule, such as a missing field or required comparison value, does not run the action.

### Email {#email}

The email form action sends one email on form submission. By default, it is configured to send the email to the site administrator email containing all the form fields content.

You may customize the form email action with the following settings:

- **Subject**: The email subject
- **Send to email address**: Fill in the email recipients. You may choose to send the email to the website administrator or to a custom email address (it accepts multiple email addresses, separated by a comma)
- **From email address**: The email address that shows as the sender
- **From name**: The name that shows as the sender
- **Reply to email address**: In case the recipient replies to the email, this email will be used instead of the "From email address"
- **Email content**: In case you want to personalize the email content message. For the default message containing all the fields, leave this field empty.
- **Error message**: The message that will be presented to the site's user if the email fails for some reason.
- **HTML email**: Enable to send HTML formatted emails. Leave disabled to send a plain text email.

### Confirmation email {#confirmation-email}

Let the person who submitted a form know that you have received their email by automatically sending out a custom confirmation email whenever the form is submitted.

We highly recommend properly setting up SMTP to ensure the best possible email delivery from your website. There are plenty of free WordPress plugins available that let you configure this within a few minutes. A search for "WordPress SMTP" should bring up countless articles & plugins for it.

If the "From name" & "From email address" you have set under the "Confirmation Email" settings inside the Form element aren't used, you have to check if any plugin and/or custom code is overwriting/forcing another name & email address.

### Form dynamic fields {#dynamic-fields}

![](https://academy.bricksbuilder.io/assets/form-fields-ids.jpg)

<figcaption>

Field ID

</figcaption>

In certain scenarios, it could be useful to get some of the submitted form fields' content to populate the email action settings.

To use the submitted data in your form settings, you have copy & paste the unique field ID (which you'll find at the end of every form field) and wrap it in two curly brackets like this: `{{form_field_id}}`

Use those dynamic fields in the "Subject", "Email address", "Email content", "From name", and "From email" settings.

Use the `{{referrer_url}}` in the above fields to insert the URL of the page where the form was submitted.

To render all submitted fields in the "Email content" use the `{{all_fields}}` placeholder.

### User Login, Registration, Lost Password, and Reset Password {#login-registration}

These four actions allow you to build custom authentication forms without coding.

When selecting one of these actions, you have to map the form fields appropriately:

- **User login**: Map the form fields to "Login", "Password", and optionally the new "Remember me" checkbox.
- **User registration**: Map the form fields to "Email", "Password", "Username", and optionally "First/Last name". If you want to customize the default WordPress emails sent to the admin or new user upon registration, use the following hooks:
  - [`wp_new_user_notification_email`](https://developer.wordpress.org/reference/hooks/wp_new_user_notification_email/): Modify the email sent to the user.
  - [`wp_new_user_notification_email_admin`](https://developer.wordpress.org/reference/hooks/wp_new_user_notification_email_admin/): Modify the email sent to the site admin.
- **Lost password**: Map the form field to "Email" or "Username" to send reset instructions. If you want to customize the email content for password reset instructions, use the [`retrieve_password_message`](https://developer.wordpress.org/reference/hooks/retrieve_password_message/) filter.
- **Reset password**: Map the form field "password".

> **Note**
>
> When using **Lost password** or **Reset password** actions, you **do not need to configure an Email Action**. WordPress automatically handles sending the necessary emails using its default methods.

For detailed instructions on configuring custom authentication pages using the Form element, please visit the [Authentication Pages](https://academy.bricksbuilder.io/builder/features/custom-authentication-pages/) article.

#### Confirm a password

Since Bricks 2.4, a Password field can check that its value matches another Password field in the same form. Use this for registration or password reset forms:

1. Add two **Password** fields, labeled **Password** and **Confirm password**.
2. Copy the field ID shown at the end of the main Password field's settings.
3. Open the Confirm password field and enable **Mark as confirmation password**.
4. Paste the main field's ID into **Main password field ID**, without curly brackets or a `form-field-` prefix.
5. Set **Password mismatch error message** if you want to replace the default "Passwords do not match" message.
6. Map the authentication action's Password setting to the main field.

Bricks checks the values when the form is submitted. A mismatch prevents the form actions from running. Leaving **Main password field ID** empty skips the comparison, so always link the confirmation field to the correct field ID.

Matching and required-field validation are separate. Two empty optional fields pass the comparison. Enable **Required** on both fields when visitors must enter a password.

### Redirect {#redirect}

This form action redirects the user from the form page to a different page on your site. You may set the redirection to the admin area or to a custom URL and set the redirection to happen only after a specific period of time.

The Redirect form action is only triggered after all the other actions run successfully.

Since 1.10, Custom redirect URL field is supporting [Form dynamic field](#dynamic-fields) tag.

### Unlock password protection {#unlock-password-protection}

This form action is used to grant access to content protected by Bricks' password protection feature. You can map the relevant form field to “Password”, but if no field is mapped, the first password field in the form will be used by default.

For more detailed instructions on setting up password protection with forms, please refer to the [Password Protection article](https://academy.bricksbuilder.io/builder/features/password-protection/).

### Webhook (@since 2.0) {#webhook}

The **Webhook** form action, available since version 2.0, sends submitted form data to one or more external URLs.

Typical use cases include:

- Sending leads to CRMs like **Zoho**, **Hubspot**, or **Salesforce**
- Triggering **Zapier** or **Make** scenarios
- Storing form data in **Google Sheets** or external databases
- Notifying internal tools via a **custom API or Slack bot**

A webhook is simply an HTTP request sent when the form is submitted. You can control what data is sent, how it’s formatted, and whether errors should stop the form.

#### Setting: Endpoints

You can set up multiple webhook endpoints. Each has these options:

- **Name**: Label for this webhook (for your reference only)
- **Endpoint URL**: The URL to send form data to
- **Data format**: Choose how the data is sent:
  `JSON` or `Form data` (x-www-form-urlencoded)
- **Data**: Optional payload template using dynamic field tags
  Leave empty to send all form fields. Example:

```php
{ "name": "{{43f295}}", "email": "{{a5c626}}" }
```

**Headers**: Optional custom headers in JSON format. Example:

```php
{ "Authorization": "Bearer token" }
```

#### Setting: Max payload size (KB)

Set the max size of the request payload.
Default: `1024` (1 MB)

#### Setting: Rate limiting

- **Rate limiting**
  Enable to limit requests per hour
- **Max requests per hour**
  Set the limit (default: `60`)

#### Setting: Error handling

- **Continue on error**
  If enabled, form submission succeeds even if the webhook fails
- **Error message**
  Message shown if the webhook fails and "Continue on error" is off

**Example: Zapier**

To trigger a Zap from a form submission, follow these steps:

1. In [Zapier](https://zapier.com/), create a new Zap
2. Choose **Webhooks by Zapier** as the trigger
3. Select **Catch Hook**
4. Copy the webhook URL Zapier gives you

![](https://academy.bricksbuilder.io/assets/zapier-webhook-url.png)

1. In Bricks, edit your form and add a **Webhook** action
2. Paste the Zapier URL into the **Endpoint URL** field

![](https://academy.bricksbuilder.io/assets/bricks-webhook-zapier-url.png)

1. Set the **Data format** to `JSON` (recommended)
2. Optionally define the payload or leave it empty to send all fields
3. Save and test your form

For full setup instructions, see [Zapier’s webhook guide](https://help.zapier.com/hc/en-us/articles/8496288690317-Trigger-Zaps-from-webhooks).

### Create & update posts (@since 2.1)

It is also possible to create powerful frontend forms with Bricks using the "Create post" and "Update post" actions.

More information and examples can be found at [/builder/features/create-update-posts-on-the-frontend/](https://academy.bricksbuilder.io/builder/features/create-update-posts-on-the-frontend/)

### Custom {#custom-action}

The custom action will allow you to hook into the action `bricks/form/custom_action` and run your custom code.

Please ensure you have included the **Custom** in the "Actions after successful form submit" field on your form element when using this hook.

![](https://academy.bricksbuilder.io/assets/custom-action-form-element.png)

The action callback will receive the `$form` object which exposes the following methods to get the form settings, the form fields, and the form uploaded files (if needed):

**Settings**: `**$form->get_settings()**`

This method exposes an associative array with the form settings (fields and actions settings) similar to this:

```php
Array
(
    [fields] => Array
        (
            [0] => Array
                (
                    [type] => text
                    [label] => Name
                    [placeholder] => Your Name
                    [id] => 15bc57
                )

            [1] => Array
                (
                    [type] => email
                    [label] => Email
                    [placeholder] => Your Email
                    [required] => 1
                    [id] => 3db633
                )

            [2] => Array
                (
                    [type] => textarea
                    [label] => Message
                    [placeholder] => Your Message
                    [required] => 1
                    [id] => f65f2c
                )
            ...

        )

    [submitButtonStyle] => primary
    [actions] => Array
        (
            [0] => email
            ...
        )

    [successMessage] => Message successfully sent. We will get back to you as soon as possible.
    [emailSubject] => Contact form request
    [emailTo] => admin_email
    [fromName] => bricks
    [emailErrorMessage] => Submission failed. Please reload the page and try to submit the form again.
    [htmlEmail] => 1
    [mailchimpPendingMessage] => Please check your email to confirm your subscription.
    [mailchimpErrorMessage] => Sorry, but we could not subscribe you.
    [sendgridErrorMessage] => Sorry, but we could not subscribe you.
    ...
)

```

**Fields values**: `**$form->get_fields()**`

This method exposes an associative array with the submitted values for each form field, together with the post Id and the form Id:

```php
Array
(
    [form-field-15bc57] => John Doe
    [form-field-3db633] => john.doe@example.com
    [form-field-f65f2c] => Thank you for using Bricks!
    ...
    [postId] => 167
    [formId] => yrnkmt
    ...
    [referrer] => https://example.com/contact
)
```

**Submitted files**: `**$form->get_uploaded_files()**`

This method exposes an associative array with the properties of the submitted files, grouped by the form field Id:

> **Note**
>
> ['file'] => Physical saved location
> ['url'] => Might not be accessible if not save to media or save to custom directory.

```php
Array
(
    [form-field-sajbjc] => Array
        (
            [0] => Array
                (
                    [file] => /.../public/wp-content/uploads/2022/03/my-uploaded-file.png
                    [url] => https://example.com/wp-content/uploads/2022/03/my-uploaded-file.png
                    [type] => image/png
                )

            [1] => Array
                (
                    [file] => /.../public/wp-content/uploads/2022/03/my-other-file.png
                    [url] => https://example.com/wp-content/uploads/2022/03/my-other-file.png
                    [type] => image/png
                )
            ...

        )

)
```

**Example #1** Basic setup

```php
<?php
function my_form_custom_action( $form ) {
  // $fields = $form->get_fields();
  // $formId = $fields['formId'];
  // $postId = $fields['postId'];
  // $settings = $form->get_settings();
  // $files = $form->get_uploaded_files();

  // Perform some logic here...

  // Set result in case it fails
  $form->set_result([
    'action' => 'my_custom_action',
    'type'    => 'success', // or 'error' or 'info'
    'message' => esc_html__('Oh my custom action failed', 'bricks'),
  ]);
}
add_action( 'bricks/form/custom_action', 'my_form_custom_action', 10, 1 );
```

**Example #2** Trigger a second email after the form is submitted.

With the current Bricks version, you can only set one email notification. With this code snippet, you may trigger a second one.

```php
<?php
function my_form_custom_action_sending_email( $form ) {
  $fields = $form->get_fields();
  // $formId = $fields['formId'];
  // $postId = $fields['postId'];
  $settings = $form->get_settings();
  // $files = $form->get_uploaded_files();

  $to = 'recipient@example.com'; // Replace this
  $from = 'sender@example.com'; // Replace this
  $subject = 'Your Subject'; // Replace this

  if ( ! empty( $settings['emailContent'] ) ) {
    $message = $form->render_data( $settings['emailContent'] );
    $message = isset( $settings['htmlEmail'] ) ? nl2br( $message ) : $message;
  } else {
    $email = new Bricks\Integrations\Form\Actions\Email('email');
    $message = $email->get_default_message( $settings, $fields );
  }

  $headers[] = 'From: Your Name <'.$from.'>';
  $headers[] = 'Reply-to: '. $from;
  if ( isset( $settings['htmlEmail'] ) ) {
    $headers[] = 'Content-Type: text/html; charset=UTF-8' . "\r\n";
  }

  $result = wp_mail( $to, $subject, $message, $headers );

  // $form->set_result([
  //  'action' => 'my_custom_action',
  //  'type'    => 'success', // or 'error' or 'info'
  //  'message' => esc_html__('Oh my custom action failed', 'bricks'),
  // ]);
}
add_action( 'bricks/form/custom_action', 'my_form_custom_action_sending_email', 10, 1 );
```

<span id="custom-redirect-to-hidden-field"></span>

**Example #3** Custom redirect to a hidden field URL

In certain cases, you would like to redirect user to a page based on certain URL parameter values. In such scenario, you are not able to use `{url_parameter:key}` on the Custom redirect URL field. This is because the form was submitted in AJAX and the current page URL param will not be sent along the AJAX call.

**Method 1**
Since 1.10, Ridirect action is supporting dynamic form field. You can choose Redirect action and configure like this.

![](https://academy.bricksbuilder.io/assets/form-redirect-support-dynamic-field-tag.png)

**Method 2**
You can use Custom action with some PHP code for more complicated logic. You can first place the url parameter into a hidden field.

![](https://academy.bricksbuilder.io/assets/store-url-param-into-hidden-field.png)

<figcaption>

Store url parameter into hidden key, and choose Custom action

</figcaption>

Then choose Custom action, and follow below code as an example

```php
<?php
add_action( 'bricks/form/custom_action', 'redirect_to_my_key', 10, 1 );

function redirect_to_my_key( $form ) {
  $form_fields   = $form->get_fields();
  $form_id       = $form_fields['formId'];

  // Check if the form id is the one you want
  if( $form_id !== 'cyrozb' ) return;

  // oeckxw is the hidden field Id where I placed the {url_parameter:my_key}
  $my_key = isset( $form_fields['form-field-oecdxz'] ) ? $form_fields['form-field-oecdxz'] : '';

  if( $my_key ) {
    // Now you get the hidden field value and redirect to the page you want, for example:
    $redirect_to = get_site_url() . '/?key=' . $my_key;

    // If the hidden field value is a URL, just redirect to it instead of following my code
    // $redirect_to = $my_key;

    $form->set_result(
      [
        'action'          => 'my_custom_redirect', // This is the action name, you can set it to anything you want
        'type'            => 'redirect', // Must be set to 'redirect'
        'redirectTo'      => $redirect_to,
        'redirectTimeout' => 0 // Need to delay ? Set a timeout in milliseconds
      ]
    );
  }
}
```

### Custom form actions {#custom-form-actions}

Since Bricks 1.12.2, you can extend the functionality of Bricks forms by adding multiple **custom form actions**. This allows seamless integration with external services like CRMs, email marketing providers, notification systems, or any custom workflows you require.

To create custom actions, you use three key filters:

- **[`bricks/elements/{element_name}/controls`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-controls/)**: Add new actions and their settings to the form builder.
- **[`bricks/elements/{element_name}/control_groups`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-elements-element_name-control_groups/)**: Group settings for better organization in the builder.
- **[`bricks/form/action/{form_action}`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-form-action-form_action/)**: Handle the logic for the custom action when the form is submitted.

These filters give you complete control over how custom actions are configured and executed.

#### Example: Creating a custom Slack notification action

**1 - Add the action to form actions setting:**

```php
add_filter(
    'bricks/elements/form/controls',
    function( $controls ) {
        $controls['actions']['options']['slack-notification'] = esc_html__( 'Send to Slack', 'bricks' );

        $controls['slackFields'] = [
            'group'       => 'slack',
            'label'       => esc_html__( 'Fields to include', 'bricks' ),
            'type'        => 'select',
            'multiple'    => true,
            'options'     => [], // Auto-populated with form fields with 'map_fields' => true
            'map_fields'  => true,
            'description' => esc_html__( 'Select which form fields to include in the Slack notification', 'bricks' ),
        ];

        return $controls;
    }
);
```

**2 - Add a new control group:**

```php
add_filter(
    'bricks/elements/form/control_groups',
    function( $control_groups ) {
        $control_groups['slack'] = [
            'title' => esc_html__( 'Slack notification', 'bricks' ),
            'required' => [ 'actions', '=', 'slack-notification' ],
        ];

        return $control_groups;
    }
);
```

1.

**3 - Handle the action logic on form submission:**

```php
add_action(
    'bricks/form/action/slack-notification',
    function ( $form ) {
        $settings = $form->get_settings();
        $fields   = $form->get_fields();

        // Custom Slack notification implementation
    }
);
```

## Form validation {#form-validation}

Bricks 1.7.1 provides a new filter named `bricks/form/validate` that allows you to validate every form submission and return error messages if your custom validation fails. The first `$errors` param is an array with each item being an error message. And the second `$form` param is the instance of the form that has been submitted.

The following code example validates the submitted email address for the form field ID `7e30aa`.

If no user account with this email address exists on this site, the validation fails, an error message is displayed, and no email will be sent.

```php
add_filter( 'bricks/form/validate', function( $errors, $form ) {
  $form_settings = $form->get_settings();
  $form_fields   = $form->get_fields();
  $form_id       = $form_fields['formId'];

  // Skip validation: Form ID is not 'kfbqso'
  if ( $form_id !== 'kfbqso' ) {
    // Early return the $errors array if it's not target form
    return $errors;
  }

  // Get submitted field value of form field ID '7e30aa'
  $email_address = $form->get_field_value( '7e30aa' );

  // Error: Email from registered user (show error message, and don't send email)
  if ( ! email_exists( $email_address ) ) {
    // Add error message to the $errors message array
    $errors[] = esc_html__( 'This email address is not in our system, sorry.', 'bricks' );
  }

  // Make sure to always return the $errors array
  return $errors;
}, 10, 2 );.
```

## Immediate input validation {#input-validation}

![](https://academy.bricksbuilder.io/assets/form-error-message-582x1024.png)

<figcaption>

Form field: Error message

</figcaption>

Bricks has enhanced the form user experience by introducing the ability to display error messages immediately as soon as a field loses focus.

To utilize this feature:

1. Add an "Error Message" to a specific form field.
2. Upon losing focus, the form will evaluate the user input to determine if the "Error Message" should be displayed based on the following criteria:

- **Required:** Checks if mandatory fields have data.
- **Min/Max number:** Ensures entered numbers fall within a defined range.
- **Email:** Confirms the correctness of the email format.
- **URL:** Validates the structure of inputted URLs.

### Disabling immediate input validation

Sometimes, we don’t want error messages to appear immediately. Instead, we may want to display them only on specific events. This is now possible (@since 1.12) with the new **"Disable Form Validation"** control.

You can choose to disable validation on input, on blur, or both. However, the form will still be validated upon submission.

![](https://academy.bricksbuilder.io/assets/CleanShot-2024-12-17-at-11.38.32@2x.png)

## Pattern attribute validation {#pattern-validation}

With the new `pattern` attribute (`@since 2.0.2`), you can now validate form input natively before submission. Combined with the `title` attribute (also `@since 2.0.2`), you can display custom error messages directly from the browser. Make sure the "Don't use browser validation" toggle it not enabled.

The `pattern` attribute works with the following field types: `text`, `tel`, `email`, `url`, and `password`.

**Example:**
To require a simple phone number in the `###-###-###` format, you can use the pattern `^\d{3}-\d{3}-\d{3}$`.
Additionally, you can use the `title` attribute to guide users or show a helpful message if the input doesn’t match the pattern:

![](https://academy.bricksbuilder.io/assets/CleanShot-2025-07-30-at-15.38.08@2x.png)

## Spam protection (Google reCaptcha V3) {#spam}

The Bricks form element supports the latest [Google reCaptcha V3](https://developers.google.com/recaptcha/docs/v3) mechanism. To enable it, first, [create](https://g.co/recaptcha/v3) a site key and a site secret key and then add both in your admin area under "Bricks > Settings > API keys".

After adding the keys, enable the reCaptcha setting when editing the Form element in the builder under the "Spam Protection" control group.

If you still get a lot of spam, you might need to tweak the score threshold level. The threshold is configured to 0.5 by default. Google reCaptcha V3 API returns a value between 0.0 and 1.0, where 0.0 is very likely a bot, and 1.0 is very likely a human interaction. To increase the Bricks threshold, please use the following PHP snippet:

```php
add_filter( 'bricks/form/recaptcha_score_threshold', function( $score ) {
    // Bricks default is 0.5
    $score = 0.8;
    return $score;
}, 10, 1 );
```

Setting the threshold to 0.8 means Bricks will only accept form submissions with higher scores (more likely to be human interactions).

## Spam protection (hCaptcha) {#hcaptcha}

Bricks integrates with hCaptcha. To utilize it, add your hCaptcha Sitekey and hCaptcha Secret Key under "Bricks > Settings > API keys".

After adding the keys, enable the reCaptcha setting when editing the Form element in the builder under the "Spam Protection" control group. You'll find options to select either "Invisible" or "Visible" hCaptcha. For the "Visible" hCaptcha:

- **Theme:** Choose between a `dark` or `light` theme.
- **Size:** Pick from `compact` or `normal`.

For detailed setup instructions, refer to the [hCaptcha documentation](https://docs.hcaptcha.com/switch/#get-your-hcaptcha-sitekey-and-secret-key).

### Automated form testing

For automated tests on a staging or test site, use [hCaptcha's test keys](https://docs.hcaptcha.com/#integration-testing-test-keys). Test keys do not provide anti-bot protection and must not be used on a production form.

Keep production monitoring separate from the public form, for example by testing the same setup on staging or using a dedicated protected monitoring form.

## Spam Protection (Cloudflare Turnstile) {#turnstile}

Beginning with version 1.9.2, Bricks has introduced support for Cloudflare Turnstile. To leverage its capabilities, first, add your Cloudflare Turnstile site key & secret key under "Bricks > Settings > API keys".

After registering the necessary details, go to the Form element in the builder and look for the “Spam Protection” control group. Here, you can toggle the Cloudflare Turnstile setting on or off.

Once enabled, you will have the ability to customize the following:

- **Theme:** Select between a "dark", "light", or the default "auto" theme.
- **Size:** Opt for either "compact" or "normal".

For more details about getting your site key and secret key, refer to the [Cloudflare Turnstile documentation](https://developers.cloudflare.com/turnstile/get-started/).

## Honeypot {#honeypot}

![](https://academy.bricksbuilder.io/assets/bricks-1.12.2-form-field-honeypot.png)

Another spam protection layer, available since Bricks 1.12.2 is the ability to turn any form field (except "Files", "Remember me", "HTML" and "Hidden") into a honeypot field. This won't affect or interrupt actual website visitors, but it'll prevent bot form submissions if they fill out any of your honeypot fields.

## Customize the date picker field {#datepicker}

Bricks (1.5+) uses the [Flatpickr](https://flatpickr.js.org/) datetime picker javascript library, which can be extended, localized, or customized according to the [available options](https://flatpickr.js.org/options/).

To change the library initialization options, use the `bricks/element/form/datepicker_options` filter, like so:

```php
add_filter( 'bricks/element/form/datepicker_options', function( $options, $element ) {
    $options['locale'] = [
        'firstDayOfWeek' => 1 // Set Monday as the first week day
    ];

    return $options;
}, 10, 2 );
```

The filter callback function accepts two arguments:

- $options - an array of [Flatpickr options](https://flatpickr.js.org/options/)
- $element - the Bricks element object

### Localize the date picker strings {#datepicker-l10n}

Flatpickr supports [l10n](https://flatpickr.js.org/localization/) for a variety of languages. You would need to load the language package by placing the following instructions into the Bricks Settings > Custom Code > Body (footer) scripts:

```php
<script src="https://npmcdn.com/flatpickr/dist/l10n/XX.js"></script>

<script>
   window.flatpickr.localize(window.flatpickr.l10ns.XX)
</script>
```

Replace the XX with the language code you need (e.g. **de** for German, **pt** for Portuguese, ...).

If you need to adjust the language on a specific form, you would need to load the language package as explained in the first line of the code above but then you may use the Bricks filter to load the language for a specific form element

```php
add_filter( 'bricks/element/form/datepicker_options', function( $options, $element ) {
    if ( $element->id === 'abcdef' ) {
      // localize the form "abcdef" element
      $options['locale'] = 'XX';
    }

    return $options;
}, 10, 2 );
```

## Define options value & label {#options}

Starting at Bricks 1.10.2 you can define the value & label for the checkbox, radio, and select field types by separating the option through a colon (:) like this:

![](https://academy.bricksbuilder.io/assets/bricks-form-options-value-label.png)

## Integrations {#integrations}

The Form element integrates with Mailchimp & Sendgrid. Allowing you to add new contacts to your email lists. Make sure you've added your Mailchimp/Sendgrid API keys as described below.

When editing your form element, you have to select Mailchimp or Sendgrid under "Actions" so the form knows to add the submitted email address to your list.

Once you've selected the proper action, a new "Mailchimp" or "Sendgrid" control group should appear. There you have to select the list you want to add this new contact to and the "Email field" of your form that contains the email address.

### Mailchimp {#mailchimp}

The Mailchimp form action allows you to automatically communicate your form data (email, first name, and last name) to a Mailchimp list and group.

To use the Mailchimp action, you need to create a Mailchimp account and then [get an API key](https://mailchimp.com/help/about-api-keys/).

To use this form action, add the API key under "Bricks > Settings > API keys > Mailchimp API key".

### SendGrid {#sendgrid}

The SendGrid form action allows you to automatically communicate your form data (email, first name, and last name) to a SendGrid list.

To use the SendGrid action, you need to create a SendGrid account and then [get an API key](https://docs.sendgrid.com/ui/account-and-settings/api-keys#creating-an-api-key).

To use this form action, add the API key under "Bricks > Settings > API keys > SendGrid API key".

## How to create a multi-column form {#multi-column}

To create a multi-column form, we first need to set the "Width" of the form fields in percentage.

**Example: Two-column layout**

Creating a two-column form is as simple as setting the width of the individual form fields to 50%.

To add some spacing between our form fields, let's set the "Width" of the first two form fields in our example to 49%. Those fields now take up 98% of the horizontal width. Creating a 2% gap between our columns. Set the bottom "Spacing" value to "2%" to apply the same spacing in all directions.

Lastly, set the "Alignment" to "space-between" to ensure our fields horizontally align with the outer edges of our form.

![](https://academy.bricksbuilder.io/assets/form-element-multi-column-layout-1024x539.png)

<figcaption>

Two-column form layout

</figcaption>

---

# HTML

Source: https://academy.bricksbuilder.io/builder/elements/general/html/

*The HTML element outputs raw HTML from a single code field. In the theme it is marked deprecated (deprecated flag): prefer the Code element, blocks, or native.*

The **HTML** element outputs **raw HTML** from a single code field. In the theme it is marked **deprecated** (`deprecated` flag): prefer the [Code](https://academy.bricksbuilder.io/builder/elements/general/code/) element, blocks, or native elements for new layouts so you keep validation, security, and editor consistency.

It exists for **backward compatibility** and for the **Gutenberg** block mapping (`core/html`) when converting content.

## Settings

- **Raw HTML** (code) — HTML source, editor mode `text/html`. Default includes a sample heading and paragraph.

If the field is empty, the element shows a “No HTML markup defined” placeholder on the front end.

> **Developer reference**
>
> See the [HTML Schema](https://academy.bricksbuilder.io/developer/schema/elements/html/) for the full JSON schema of this element's settings and controls.

---

# Icon box

Source: https://academy.bricksbuilder.io/builder/elements/general/icon-box/

*The Icon Box element combines an icon with content in a flexible layout.*

The Icon Box element combines an icon with content in a flexible layout.

## Settings

- **Direction** (direction) - Layout direction of the icon and content.

- **Spacing** (number with units) - Gap between the icon and content.

### Icon

- **Icon** (icon) - The icon to display. Default: WordPress icon from Themify library.

- **Align** (align-items) - Vertical alignment of the icon.

- **Link** (link) - Make the icon clickable with a link.

- **Margin** (spacing) - Margin around the icon.

- **Padding** (spacing) - Padding inside the icon container.

- **Size** (number with units) - Font size of the icon.

- **Height** (number with units) - Height of the icon container.

- **Width** (number with units) - Minimum width of the icon container.

- **Color** (color) - Color of the icon.

- **Background color** (color) - Background color of the icon container.

- **Border** (border) - Border styling for the icon container.

- **Box shadow** (box-shadow) - Shadow effect for the icon container.

### Content

- **Content** (rich text) - The text content to display alongside the icon. Supports rich text and dynamic data.

- **Align** (align-items) - Vertical alignment of the content.

- **Margin** (spacing) - Margin around the content.

- **Padding** (spacing) - Padding inside the content container.

- **Heading typography** (typography) - Font settings for heading elements (h1-h6) in the content.

- **Body typography** (typography) - Font settings for the content text.

- **Background** (color) - Background color of the content container.

- **Border** (border) - Border styling for the content container.

- **Box shadow** (box-shadow) - Shadow effect for the content container.

> **Developer reference**
>
> See the [Icon Box Schema](https://academy.bricksbuilder.io/developer/schema/elements/icon-box/) for the full JSON schema of this element's settings and controls.
