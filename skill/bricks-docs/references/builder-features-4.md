# Lazy Loading

Source: https://academy.bricksbuilder.io/builder/features/lazy-loading/

*Control lazy loading for background images and videos, individual images, or an entire Bricks page or site.*

Lazy loading delays loading media until it is needed near the visible part of the page. For a hero background that visitors see as soon as the page opens, disable lazy loading on that element so Bricks does not wait for it to enter the viewport.

Bricks 2.5 adds **Disable lazy load** to the background controls of Section, Container, Block, and Div elements. The setting applies to both background images and background videos. Global and page-level lazy-loading opt-outs also cover background videos in Bricks 2.5.

## Native image loading in Bricks 2.5

On WordPress 6.4 or newer, Bricks 2.5 uses the browser's native image lazy loading by default. Images keep their real `src` and `srcset`; the browser decides when images with `loading="lazy"` are fetched. Bricks preserves explicit loading and fetch-priority decisions, and does not force every leading image to load lazily.

If custom code depends on the previous placeholder images or `data-src` attributes, enable **Bricks > Settings > Performance > Use JavaScript lazy loading for images**. WordPress versions earlier than 6.4 continue using the JavaScript loader automatically. Background images, background videos, and iframes still use JavaScript loading.

**Lazy load offset** applies to HTML images only when the JavaScript image loader is active. It does not change the browser's native loading distance.

## Disable lazy loading for one background

1. Select the **Section**, **Container**, **Block**, or **Div** that has the background.
2. Open **Style > Background**.
3. Enable **Disable lazy load**.
4. Save and check the page on the frontend.

<div className="screenshot screenshot--control-panel">

![Background control group showing Disable lazy load and its description: Load background images and videos immediately.](https://academy.bricksbuilder.io/assets/background-disable-lazy-load.webp)

</div>

The checkbox is off by default. Enabling it bypasses Bricks' lazy loading for that element's background images and starts its background video initialization without waiting for the element to become visible. This includes file-based videos and YouTube or Vimeo backgrounds. Video playback still depends on the browser's autoplay rules and the video provider.

For example, enable it on a hero Section with a background image, while leaving it off on Sections further down the page. Apply the setting to the element that owns the background. It does not disable lazy loading for every image or video inside that element.

### Why is the checkbox missing?

Bricks hides the background checkbox when lazy loading is already disabled globally or for the current page. In that case, the background already bypasses Bricks' lazy loading. Check the settings below before looking for the element control.

## Disable lazy loading for a page or site

| Scope | Setting |
| --- | --- |
| Current page | In the builder, open **Page Settings > General > Disable lazy load**. |
| Entire site | In WordPress, open **Bricks > Settings > Performance > Disable lazy loading**. |

These settings disable Bricks' built-in lazy loading for images, videos, background images, and background videos in their scope. Use the element control when only one background needs to load immediately.

See [Page Settings](https://academy.bricksbuilder.io/builder/interface/page-settings/#general-settings) and [Bricks Settings](https://academy.bricksbuilder.io/builder/setup/settings/#disable-lazy-loading) for the wider settings context.

## Image and Logo elements

The [Image](https://academy.bricksbuilder.io/builder/elements/basic/image/) and [Logo](https://academy.bricksbuilder.io/builder/elements/media/logo/) elements have a separate **Loading** control with `lazy` and `eager` options. Choose `eager` when the image should load without native lazy loading.

These controls set the HTML image's `loading` attribute and remain available when Bricks' global or page-level lazy loading is disabled. CSS background images do not support that native attribute; use **Style > Background > Disable lazy load** for them.

## Preload a background image

Since Bricks 2.5, enable **Preload** beside the selected image under **Style > Background** when an important background is visible as soon as the page opens, such as a hero image. Bricks adds an image preload hint with high fetch priority and uses responsive media conditions for breakpoint-specific backgrounds.

Dynamic background images inside query loops are not preloaded. Use this selectively. Preloading below-the-fold backgrounds competes with resources needed for the initial view. The control is unavailable for pseudo-class states and background contexts that are hidden on initial load, such as popup backgrounds. A viewport background configured for preloading bypasses Bricks' background lazy loader.

<div className="screenshot screenshot--control-panel">

![A Section's Background controls with a selected image and Preload enabled.](https://academy.bricksbuilder.io/assets/builder/release-2.5/background-preload-panel.webp)

</div>

## Check loading on the frontend

Test on the frontend rather than relying on the builder preview. In your browser's developer tools, open the Network panel, disable the cache, and reload at the top of the page. Compare media requests before and after scrolling to the background.

The **Lazy load offset** in **Bricks > Settings > Performance** controls how early Bricks' JavaScript lazy loader starts loading images and background images. Its default is **300px**. This offset does not control native browser image loading or when background videos load.

If a background image loads before you scroll to it, also check its **Preload** option. A background image configured for viewport preloading bypasses background lazy loading. Disabling lazy loading alone does not add an image preload hint.

---

# Maintenance Mode

Source: https://academy.bricksbuilder.io/builder/features/maintenance-mode/

*Set up maintenance mode in Bricks, choose what visitors see, and control access while you work on the site.*

Bricks 1.9.4 introduces the **Maintenance Mode** feature. A straightforward way to manage your site's availability during updates or construction.

https://youtu.be/df7nzqiv32s

![](https://academy.bricksbuilder.io/assets/bricks-settings-maintenance-mode-2-0.png)

Maintenance Mode runs on the frontend only. It does not replace the WordPress admin, and it does not block the Bricks builder.

## How to enable Maintenance Mode

1. Log in to the WordPress dashboard.
2. Navigate to Bricks > Settings > Maintenance mode.

Here, you'll find several settings to configure:

- **Mode selection**: Choose `Disabled`, `Maintenance`, or `Coming soon`. "Maintenance" mode (HTTP status code 503) indicates that your site is temporarily unavailable, signaling search engines to come back later. "Coming soon" mode (HTTP status code 200) indicates that your site is available for search engine indexing.
- **Template** *(optional)*: Assign a custom single template for your maintenance or coming soon mode.
  - **Render header** *(optional)*: Enable this setting if you want the active Bricks header to render with the maintenance or coming soon template. This is **disabled by default**.
  - **Render footer** *(optional)*: Enable this setting if you want the active Bricks footer to render with the maintenance or coming soon template. This is **disabled by default**.
  - **Render popups** *(optional)*: Enable this setting if you want Bricks popups to be rendered on the maintenance or coming soon template. This is **disabled by default**.
- **Bypass maintenance**: Customize access settings for different user roles.
- **Exclude posts/pages** *(since 2.0)*: Select specific pages or posts where Maintenance Mode should **not** be applied.

If no template is selected, or the selected template is not published or has no Bricks data, Bricks renders a simple default page with a `Maintenance` or `Coming soon` heading.

## When maintenance mode applies

Maintenance mode is skipped for:

- WordPress admin requests.
- Bricks builder requests.
- The Bricks custom login page, if one is configured.
- Logged-in users who can bypass maintenance.
- Posts or pages selected under **Exclude posts/pages**.

If none of those bypasses apply, Bricks serves the maintenance response. In **Maintenance** mode, Bricks sends HTTP status `503`. In **Coming soon** mode, Bricks sends HTTP status `200`.

When maintenance mode is active, Bricks also removes the canonical tag and does not output Bricks Open Graph meta tags for the maintenance response.

## Check what visitors see

Because logged-in users bypass maintenance mode by default, the site looks unchanged while you are logged in. Inside the WordPress admin, the admin bar shows a **Mode: Maintenance** (or **Mode: Coming soon**) label while the mode is active. The label links to the **Maintenance mode** settings tab.

To see what visitors get, open the site in a private browser window where you are not logged in.

To switch maintenance mode off, set **Mode** to `Disabled` and save the settings.

## Custom maintenance templates

The selected maintenance template replaces the requested page content while maintenance mode is applied. The normal search, archive, and error templates are disabled for that response.

Header and footer rendering are off by default and must be enabled with **Render header** and **Render footer**. Popups are also off by default and only load when **Render popups** is enabled, or when the current user can bypass maintenance.

For multilingual sites, Bricks resolves the selected maintenance template through WPML or Polylang when those integrations are active.

## Configuring role-based access

In the "Bypass maintenance" setting:

1. Select from the dropdown menu: `Logged-in users` allows all logged-in users to bypass maintenance mode; `Logged-in users with role` provides a more granular control.
2. If `Logged-in users with role` is selected, checkboxes will appear to enable or disable maintenance mode bypass for specific roles such as Editor, Author, Contributor, etc.

Administrators can bypass maintenance by default. If no custom role selection is enabled, logged-in users can bypass maintenance mode.

## Individual user access settings

To configure access on an individual user level:

1. From the WordPress dashboard, go to "Users".
2. Click to edit a specific user's profile.
3. In the user profile, find and adjust the "Bypass Maintenance" setting.

The individual user setting can explicitly enable or disable maintenance bypass for that user. This takes precedence over the role-based setting and over the default administrator/logged-in behavior.

<span id="filters"></span>

**Filters:**

- [/developer/hooks/filters/filter-bricks-maintenance-should_apply/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-maintenance-should_apply/)

---

# Media Browser

Source: https://academy.bricksbuilder.io/builder/features/media-browser/

*Search, upload, organize, inspect, repair, and select WordPress media from the Bricks Builder Browser.*

The **Media Browser**, introduced in Bricks 2.4, adds media selection and management to the [Builder Browser](https://academy.bricksbuilder.io/builder/features/builder-browser/). It works with attachments in the WordPress Media Library, so files uploaded or edited in either interface remain available in both.

Use the Media Browser to:

- Select files for Image, Image Gallery, Video, Audio, SVG, and File controls.
- Search and filter attachments by their metadata and file properties.
- Upload local files or import public files from URLs.
- Edit attachment details without leaving the builder.
- Select multiple attachments for metadata, download, folder, image-size, and deletion actions.
- Find and resolve common accessibility and file problems with Media Health.

![](https://academy.bricksbuilder.io/assets/media-browser-main-view.webp)

## Open the Media Browser

Open the Builder Browser from the folder icon in the builder toolbar, then select **Media**.

The Media Browser can also open as a picker when you choose or change a file in a supported builder control. The picker limits results to the type accepted by the control. For example, an Audio control shows audio files, while an SVG control only shows SVG files.

Image Gallery opens in multi-select mode. Image, Video, Audio, SVG, and File controls select one attachment at a time. Existing control values are preselected when you reopen the picker.

To confirm a selection in the Bricks picker, click **Insert** or press the default `CMD / CTRL + ENTER`. In Bricks 2.5, you can change this combination under **Manage → Keyboard shortcuts**. It applies to picker selection, not standalone media management. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

### Choose the media picker

Go to **Bricks > Settings > Builder > Media > Media picker** and choose:

- **Bricks: Media browser (Default)**: Opens the Bricks interface in supported media controls.
- **WordPress: Media library**: Opens the standard WordPress media picker.

This setting changes the interface, not where the files are stored. Both options use the WordPress Media Library.

## Browse, search, and filter media

Use the sidebar to switch between all media, images, video, audio, Trash, and Media Health. If a compatible media-folder integration is active, folders also appear in the sidebar.

The layout control provides grid, masonry, and list views. Media defaults to 50 results per page. Open the settings popover to change the number of results from 1 to 100 and choose whether attachment details open beside the results or in an overlay.

### Adjust thumbnails and visible details

Open the **More** menu above the results to adjust the Media view. **Thumbnail size** and **Thumbnail fit** are available since Bricks 2.4.6:

- **Thumbnail size**: Choose **Small**, **Medium**, or **Large** in grid view. The default is **Medium**.
- **Thumbnail fit**: Choose **Cropped** to fill each grid thumbnail or **Fitted** to see the whole image without cropping. The default is **Cropped**. This changes the Browser preview, not the attachment or its frontend display.
- **Image dimensions** (since Bricks 2.5): Show each image's width and height in the result metadata. This is off by default and is available across grid, masonry, and list views.

These preferences are remembered in your browser for the current user. Thumbnail size and fit apply only to grid view.

![Media Browser grid showing complete portrait and landscape images, with Thumbnail size set to Medium, Thumbnail fit set to Fitted, and Image dimensions enabled in More.](https://academy.bricksbuilder.io/assets/builder/release-2.5/media-thumbnail-settings.webp)

<div className="screenshot screenshot--control-panel">

![More menu with Medium thumbnail size, Fitted thumbnail fit, and Image dimensions enabled.](https://academy.bricksbuilder.io/assets/builder/release-2.5/media-thumbnail-menu-detail.webp)

</div>

### Search and filter results

Search checks the attachment ID, file name, title, caption, description, and alternative text.

The filter panel includes:

- Media type and MIME subtype.
- Uploader.
- Attached or unattached status. Featured images count as attached.
- Upload date range.
- Minimum and maximum width, height, and file size.
- Images with missing alternative text.
- Media Health status.

Width and height filters appear for compatible image and video types. The missing-alt filter only applies to images. The filter button shows the number of active filters, and **Clear all** removes them.

![](https://academy.bricksbuilder.io/assets/media-browser-filters.webp)

## Upload media

Click the upload icon in the Media Browser to open the upload workspace.

### Drop images directly onto a control

Since Bricks 2.5, you can drop a local image onto an **Image** selector or its preview to upload and select it without opening the Media Browser. Dropping onto an existing image replaces that control's selection; it does not replace the original Media Library attachment.

This requires WordPress upload permission and a control that is not using dynamic data. WordPress file-type and upload-size restrictions still apply.

### Upload local files

Drop files into the workspace or click **Browse files**. You can stage and upload multiple files in one batch.

Before a local file is uploaded, you can change its file name without changing the extension. Bricks checks the current WordPress upload directory for conflicts. If the name already exists, rename the file or accept the unique name suggested by WordPress.

Existing attachments cannot be renamed from this workflow. Changing an existing file name could break stored URLs and references.

### Drop images onto an Image Gallery

Since Bricks 2.5, for an **Image Gallery** control, drop one or more images to append them to the selected gallery. Hold **Shift** while dropping to replace the entire selection. A replacement is applied only when every file in the batch uploads successfully. If one fails, the current gallery selection stays unchanged; retry the failed uploads from the error message.

This requires WordPress upload permission and a control that is not using dynamic data. WordPress file-type and upload-size restrictions still apply.

<div className="screenshot screenshot--control-panel">

![Image Gallery control during a file drag, showing Add images and Hold Shift to replace.](https://academy.bricksbuilder.io/assets/builder/release-2.5/gallery-drop-panel.webp)

</div>

### Import files from URLs

Select **From URL**, then enter one public HTTP or HTTPS file URL per line. Bricks downloads the files into the WordPress Media Library. WordPress upload permissions, allowed file types, and upload-size limits still apply.

### Upload destinations

Open the destination folder before adding files or URLs to the upload queue. Each queued file keeps the folder selected when it was added, even if you browse to another folder before uploading or retry a failed upload.

From Bricks 2.4.4, both local uploads and URL imports support folders from custom media-folder providers as well as HappyFiles.

For custom providers, **No folder assignment** means Bricks has not requested a destination folder. The provider's default upload behavior applies, so the file may still be assigned to a folder. HappyFiles shows **Uncategorized** when no folder is selected.

A provider can also exclude an individual folder from automatic upload assignment, for example a virtual grouping called Collections. Uploads queued there show **No folder assignment** and follow the provider's defaults. This does not prevent uploads into its child folders.

### Edit uploaded files

After an upload completes, you can edit its title, alternative text, caption, and description. Changes to an individual attachment save after you leave the edited field. Select several completed uploads to apply metadata changes in bulk.

For a completed upload, choose **View in library** to find the attachment even if the current folder or filters would hide it. **Remove from list** only clears the upload workspace entry; the attachment stays in the Media Library.

When an intended folder assignment cannot be confirmed, use **Retry folder assignment** on that upload. This retries the assignment on the existing attachment without uploading another copy. From Bricks 2.4.4, this also works with custom media-folder providers.

Completed uploads also offer **Move** when a compatible folder integration is available, plus **Trash** or **Delete permanently** according to the site's Media Trash setting. These actions change the Media Library attachment and require the relevant attachment permissions. A successful Trash or Delete action removes the entry from the upload list.

When Media Health is enabled, images can also be marked **Decorative** during upload. This clears their alternative text and excludes them from the missing-alt check.

If you started the upload from a media control, compatible files can be inserted directly into that control. An uploaded file that does not match the control remains in the Media Library but cannot be inserted into that control.

![](https://academy.bricksbuilder.io/assets/media-browser-upload-screen.webp)

## Inspect and edit an attachment

In the standalone Media Browser, click an attachment to open **Attachment details**. Depending on the Browser setting and available space, the inspector opens beside the results or in an overlay.

The inspector provides:

- A preview for supported images, video, audio, and PDF files.
- File name, dimensions, file size, upload date, author, and generated image sizes.
- Editable title, alternative text, caption, and description.
- A **Decorative** toggle for images.
- Copy URL and download actions.
- Previous and next navigation through the current results, including other result pages.
- Available Trash, restore, and permanent-delete actions.

Metadata changes save when you leave a changed field. Bricks waits for pending saves before closing the inspector or moving to another attachment.

> **Note**
>
> The **Decorative** flag classifies an attachment for Media Health and clears its stored alternative text. It does not add `aria-hidden`, change an Image or SVG element's frontend markup, or override an element's custom alternative text. Decide whether an image is decorative in the context where it is used.

## Select and manage multiple attachments

In the standalone Media Browser, use the selection controls on attachment cards to start a bulk selection. You can select the current page, then use **Select all matching items** to include every result from the current search and filters. Individual items can still be excluded.

Available bulk actions depend on your WordPress permissions and the selected attachments:

- **Edit metadata**: Change selected metadata fields and mark images as decorative.
- **Download**: Prepare the selected files as an archive.
- **Move**: Assign the files to a folder when a compatible folder integration is active.
- **Regenerate image sizes**: Rebuild registered image sizes for selected images.
- **Trash** or **Delete permanently**: Remove attachments after a usage review.

Bulk work is processed in batches. If part of an action fails or is interrupted, the results identify completed, skipped, and failed items and offer a retry when the action can continue.

![](https://academy.bricksbuilder.io/assets/media-browser-bulk-edit.webp)

## Trash and permanent deletion

When WordPress Media Trash is enabled, attachments must first be moved to **Trash**. Open Trash from the Media sidebar to restore a file or delete it permanently. If Media Trash is disabled, the Media Browser offers permanent deletion directly.

WordPress disables Media Trash by default. To enable it, edit the `wp-config.php` file in the root of your WordPress installation and add this line before `/* That's all, stop editing! Happy publishing. */`:

```php
define( 'MEDIA_TRASH', true );
```

Media Trash also requires `EMPTY_TRASH_DAYS` to be greater than `0`. See the [WordPress Core attachment deletion documentation](https://developer.wordpress.org/reference/functions/wp_delete_attachment/) for how WordPress handles Trash and permanent deletion.

Before moving attachments to Trash or deleting them permanently, Bricks checks for detected uses and lists affected locations. You must review and acknowledge detected references before continuing with files that are in use.

The usage check covers attachment IDs stored in:

- Saved Bricks elements and page settings.
- Featured images.
- Global classes and theme styles.
- Components.

It does not detect every possible reference. URL-only references, Custom CSS, Code elements, Gutenberg or Classic Editor content, custom fields, unsaved changes, other sites, and external systems are outside the check. Review important files manually before permanent deletion.

> **Caution**
>
> Deleting an attachment permanently removes its files. Any reference the usage check did not find may become a broken image or download.

## Organize media with folders

Media folders require a compatible integration. Bricks 2.4 includes support for <a href="https://happyfiles.io/" target="_blank" rel="noopener noreferrer">HappyFiles</a>.

When the integration and your permissions allow it, you can:

- Browse all media, uncategorized media, and nested folders.
- Create, rename, move, and delete folders.
- Drag attachments or a selection into a folder.
- Move selected attachments with the bulk action.
- Upload files directly into the active folder.

Open a subfolder from the folder sidebar or from the child folders shown above the media results. Attachment file names are available when you hover over an item or focus it with the keyboard.

Deleting a folder does not delete its attachments. Their relationship to that folder is removed. Files without another folder become uncategorized, and child folders move to the deleted folder's parent.

![](https://academy.bricksbuilder.io/assets/media-browser-folders-via-happyfiles-integration.webp)

## Check media with Media Health

Media Health audits attachments in the background and groups them by issue. Open **Health** in the Media sidebar to see the scan status, issue counts, decorative images, and attachments that passed all enabled checks.

The available checks are:

- **Missing alt text**: Images with empty alternative text that are not marked decorative.
- **Broken files**: Local original files that are missing, unreadable, or empty.
- **Missing image sizes**: Eligible registered sizes missing from attachment metadata or local storage.
- **Oversized files**: Original files above the configured threshold for their media type.
- **Obsolete formats**: Files whose extensions match the configured list.

If an offload service removes local originals, its integration can use the [`bricks/media_browser/health/file_status` filter](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-media-browser-health-file-status/) to classify file availability. This changes the health status check; it does not download remote files or make local repair actions available.

Select an issue to inspect the attachment and use the available resolution:

- Add alternative text, mark the image decorative, or ignore the missing-alt finding.
- Generate missing image sizes or regenerate every registered size.
- Optimize an oversized image or replace another oversized file.
- Convert an obsolete image or replace another obsolete file type.
- Replace or relink a broken file, then recheck it.
- Ignore a finding and restore it later if no change is required.

File replacement preserves the attachment ID and editorial metadata, such as title, caption, and alternative text. Replacing, relinking, or optimizing an attachment can affect every location that uses it, so Bricks shows detected usage before applying the change.

### Preserve file URLs during repairs

An in-place repair must preserve the attachment's current upload path and file URL. Choose a replacement in the same compatible format as the original. For example, replacing a JPEG with another JPEG can preserve its URL; replacing it with a WebP file would require a different extension and is blocked.

The same restriction applies to relinking, optimization, and conversion. Bricks rejects an in-place action that changes the upload path, even if the usage check finds no references. Stored URLs in content or external systems may be outside that check.

For a format conversion, use a copy action when offered to create a separate attachment, then select that attachment in the locations that should use it. Otherwise, upload the new file as a separate attachment. Creating a copy does not update existing references to the original.

![](https://academy.bricksbuilder.io/assets/media-browser-media-health.webp)

### Configure Media Health

Go to **Bricks > Settings > Builder > Media**. Media Health and all five checks are enabled by default.

The default oversized-file thresholds are:

| Media type | Default threshold |
| ---------- | ----------------: |
| Images     |              1 MB |
| Fonts      |            0.5 MB |
| Documents  |              5 MB |
| Audio      |             10 MB |
| Video      |             50 MB |

Set a threshold to `0` to disable oversized-file warnings for that media type.

The default obsolete extension list is `bmp,tif,tiff`. Enter extensions without leading dots, separated by commas. An empty list disables obsolete-format findings while leaving the other health checks active.

Changing the enabled checks, thresholds, or obsolete extensions updates the Media Health policy. Attachments are checked again against the current policy.

## Permissions

The Media Browser follows WordPress attachment capabilities:

- Upload actions require permission to upload files.
- Metadata, download, regeneration, move, and repair actions require permission to edit the affected attachments.
- Trash, restore, and permanent deletion require permission to delete the affected attachments.
- Site-wide Media Health auditing requires permission to edit attachments uploaded by other users.

Users can inspect attachments they are allowed to see even when they cannot edit or delete them. Bulk actions are only offered when every selected attachment supports the action.

---

# Menu Builder

Source: https://academy.bricksbuilder.io/builder/features/menu-builder/

*Build fully custom navigation menus in Bricks with template-driven layouts, dynamic menus, and responsive behavior.*

Bricks 1.8 introduced a completely new, fully responsive, accessible, and highly customizable suite of elements to create nav menus/site navigations in Bricks.

https://www.youtube.com/watch?v=1GbJx0JnDDE

The new menu builder consists of 5 new elements (listed below), which you can mix, match, and configure to your liking to design all kinds of desktop & mobile menus.

There are some best practices to be aware of to ensure proper accessibility & styling. So please take the time to go over the information below to get a solid understanding of this new, powerful tool.

### Nav (nestable) {#nav-nestable}

This new nestable element contains both your desktop & mobile menu.

As with any other nestable element, you can now add any element to your menus in Bricks and are no longer limited to the old "flat" Nav menu.

There is a built-in setting for selecting the breakpoint at which you want to show your mobile menu. The mobile menu uses the same markup & elements as the desktop menu. It's just optimized & styled for mobile devices & small screens.

You can also design mobile menus with completely different content/elements by using the new Offcanvas & Toggle elements. Both of which we'll explore later on.

### Text link {#text-link}

A simple, but super handy new element to create simple nav menu text links (plus an icon if needed). This is much better than turning a Basic Text element into a link. You can, of course, use the Text link anywhere else on your site.

### Dropdown (nestable) {#dropdown}

Use the new Dropdown element to create fully accessible sub-menus. Which you can nest as many levels as you want by adding dropdowns within dropdowns. You can also choose when to trigger a dropdown (on hover, click, or both).

The little dropdown arrow next to the dropdown text/link lets you always toggle the Dropdown via the keyboard (on SPACE or ENTER press) for accessibility.

Enable **Mega menu** on a Dropdown to create a nestable mega panel. Use the available page width, set a custom width, or align it to another element on the page.

You can even create multilevel mobile menus where only the active dropdown slides into the view.

We also got settings to easily design custom dropdown carets.

### Toggle {#toggle}

The main purpose of this new, fully-accessible "hamburger" toggle icon/button is to show/hide your mobile menu and/or Offcanvas elements.

You can choose from various animation effects, and even set your own custom toggle icon.

Without a "CSS selector", a Toggle opens the first Offcanvas on the page. Only when the page has no Offcanvas does it toggle the Nav (Nestable) it is placed in. So if a page has an Offcanvas (for example in the header template) and a Nav (Nestable) mobile menu, or several Offcanvas elements, enter the target's "CSS selector" in the Toggle.

You can use it for so much more, though. As it provides settings to toggle any HTML attribute of any element on your page.

Similar triggers can be achieved via [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/). But the Toggle comes with built-in accessibility & menu builder logic that makes the whole toggle process so much faster, easier, and better.

### Offcanvas (nestable) {#offcanvas}

Being nestable, the new Offcanvas element lets you create unique mobile menus with completely different content from your desktop menu. You can populate the Offcanvas with any elements you like, and are not limited to menus, though.

The Offcanvas comes with two effects: slide-in (default) & offset, and can be toggled (open/close) through the "Toggle" element. It's super simple as you can see in the [Offcanvas set up](#mobile-menu-offcanvas) section down below.

Starting at Bricks 1.11, [the new "Toggle Offcanvas" interaction](https://academy.bricksbuilder.io/builder/features/interactions/#toggle-offcanvas), lets you toggle your Offcanvas from any element.

## Default menu structure {#menu-structure}

When adding a **Nav (Nestable)** element to the canvas it is populated with 2 Nav links, 1 Dropdown, and 2 Toggle elements (to show & hide the mobile menu).

![](https://academy.bricksbuilder.io/assets/bricks-1.8-nav-nestable-default-structure.png)

Being a nestable element, you can add any Bricks element inside your menu.

The "Nav items" Block is a special element that can't be deleted individually as it holds all top-level menu items, and serves as the mobile menu wrapper. The same goes for the "Content" Div inside the Dropdown element, which contains all dropdown content.

All top-level menu items are automatically wrapped in a `li` HTML tag for accessibility. The "Nav items" uses an `ul` tag. The same goes for the "Dropdown structure.

## Default mobile menu structure {#mobile-menu}

By default, the mobile menu becomes visible at the "Mobile landscape" breakpoint. Meaning instead of displaying the top-level menu items, a (hamburger) Toggle becomes visible that opens the mobile menu when you click on it. You can, of course, select any other breakpoint to start showing your mobile menu when editing your Nav nestable element.

> **Note**
>
> **IMPORTANT**: Make sure you are editing the "Mobile menu" and "Nav items" element settings on the breakpoint at which the mobile menu starts to display at (default: Mobile landscape).

![](https://academy.bricksbuilder.io/assets/bricks-1.8-nav-nestable-mobile-menu-toggle.png)

The Toggle element labeled "Toggle (Open: Mobile)" opens the mobile menu (highlighted in the screenshot above).

You can choose from various animations that are performed on the Toggle when clicked.

The "Toggle (Close: Mobile)" element is located inside the "Nav items" (the mobile menu wrapper).

## Mega menus {#mega-menu}

Creating mega menus with Bricks couldn't be easier. Just "Enable" the mega menu setting when editing the "Dropdown" element of your choice.

By default, the Dropdown Content covers the entire available (viewport) width like this:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-dropdown-mega-menu.png)

You can also define a "CSS selector" whose width & horizontal position the mega menu will adjust to. The following screenshot uses the element `id` of its outer Container:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-dropdown-mega-menu-css-selector.png)

### Set a custom mega menu width {#mega-menu-width}

Since Bricks 2.5, open the Dropdown's **Mega menu** group and set **Width** directly, for example to `900px`, `80%`, or `clamp(20rem, 80%, 60rem)`. You do not need an extra element just to define a width. These settings are also available in the **Nav Menu** element's **Mega menu** group.

**Width** uses the horizontal reference area:

- Leave **CSS selector (Horizontal)** empty to use the page body.
- Enter a selector, such as `#site-header-container`, to use that element's width and horizontal position.
- Percentage widths use the reference area's width. For example, `80%` of a 1000px reference area is 800px.
- Leave **Width** empty to retain the reference area's full width.

When a custom width is set, choose **Alignment > Left**, **Center**, or **Right** to place the panel within that reference area. The default is **Left**. Width and alignment can be adjusted at responsive breakpoints.

For a centered panel occupying most of the page width, leave the horizontal selector empty, set **Width** to `80%`, and choose **Center**. Preview narrower screen widths as well. In a Nav (Nestable) mobile drawer, the panel returns to the drawer layout instead of retaining a fixed desktop width.

<div className="screenshot screenshot--control-panel">

![Dropdown Mega menu enabled with Width set to 80%, Alignment set to Center, and no horizontal reference selector.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mega-menu-panel.webp)

</div>

![An open mega menu panel occupies 80% of the page width with equal space on its left and right.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mega-menu-result.webp)

The Dropdown "Content" is just a Div element. Allowing you to can create any mega menu layout:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-dropdown-mega-menu-three-columns.png)

<figcaption>

A simple three-column mega menu

</figcaption>

### WordPress mega menu {#wp-mega-menu}

You can also add mega menus to your WordPress menu by enabling the "Mega menu" setting of your  "Nav menu" element like this:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-nav-menu-mega-menu.png)

Next, create your mega menu using a new template (template type: section).

Then, go to "Appearance > Menus" and expand the top-level menu item you want to display this mega menu under, and select your mega menu template from the "Mega menu" options:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-wordpress-mega-menu.png)

Your mega menu template now appears when you hover over this menu item on the frontend.

## Multilevel dropdown menus {#multilevel}

Creating multilevel dropdowns is just as easy. Simply enable the "Multilevel" setting on an individual Dropdown or directly on the "Nav nestable" element so it gets applied to all your Dropdowns.

"Multilevel" means that only the active Dropdown Content is visible. This is especially useful for dropdown menus with a lot of items or for dropdowns with multiple nested Dropdowns, as they most likely overflow the viewport. Especially on mobile.

A customizable "back" link can also be set, which is displayed as the first item of every Dropdown level.

As only the active Dropdown is visible, the multilevel dropdown automatically toggles on click, not hover.

You also only have to enable "Multilevel" at the root level of your Dropdown. All sub Dropdowns have multilevel capability out-of-the-box.

### WordPress multilevel menus {#wp-multilevel}

Bricks 1.8 lets you turn your WordPress sub menus into multilevel menus too. Simply enable the "Multilevel" setting of your "Nav menu" element, and then activate the "Multilevel" setting of your WordPress menu items under "Appearance > Menus" like this:

![](https://academy.bricksbuilder.io/assets/bricks-1.8-wordpress-multilevel-menu.png)

## Static (position) dropdown menus {#dropdown-static}

![](https://academy.bricksbuilder.io/assets/bricks-1.8-menu-builder-dropdown-position-static.png)

By default, the dropdown content is positioned `absolute`. Taking it out over the document flow. Which is the expected/desired in a desktop menu.

But when, for example, the Dropdown is placed inside an Offcanvas you most likely don't want this behaviour.

Instead you want to show the dropdown content on click and positioned right underneath the dropdown toggle & in the normal document flow.

To accomplish that simply enable the "Position: Static" setting when editing the Dropdown of your choice.

## WordPress dropdown menus {#wordpress-menu}

To use a WordPress menu inside your custom nav nestable, add the "Nav menu" element inside your Dropdown > Content element. Then edit it, and select the WordPress menu you'd like to display inside your dropdown.

![](https://academy.bricksbuilder.io/assets/bricks-1.8-nav-menu-inside-dropdown.png)

This means every WordPress menu you create for your nav nestable should hold the menu items you want to display inside a specific dropdown.

We have chosen this approach as it lets you take full advantage of the nav nestable customisation options, while still being able to control your menu via WordPress.

You can style this WordPress menu by editing the "Dropdown" it's been places in, or if you wish to style it like the entire menu you can tweak the "Dropdown" settings of your "Nav nestable".

## Unique mobile menus (Offcanvas + Toggle) {#mobile-menu-offcanvas}

Use the new Offcanvas element to create unique mobile menus. Or any other content you want to slide into view via the Toggle element.

Let's start by adding an Offcanvas element to our page.

> **Note**
>
> Make sure you position the Offcanvas element outside the "Nav (nestable)". Otherwise, the Toggle logic of those two togglable elements can interfere. **We position it AFTER our "Nav nestable". **

As we don't use the default mobile menu view of the Nav nestable, we can delete the "Toggle (Close: Mobile)" element.

We'll use the "Toggle (Open: Mobile)" element to open our Offcanvas element. Simply copy the Offcanvas element ID from the panel, edit the "Toggle (Open: Mobile)" element, and paste it under the "CSS selector" setting.

![](https://academy.bricksbuilder.io/assets/bricks-1.8-offcanvas-add-element-id-to-toggle-open.png)

<figcaption>

Toggle: "CSS selector" setting containing our Offcanvas element ID

</figcaption>

Save your changes, and head to the front end. A click on the Toggle icon should open your Offcanvas.

As the Offcanvas is a nestable element, you can add any layouts & elements inside of it.

The Offcanvas comes prepopulated with a close Toggle. Clicking outside the Offcanvas (on the backdrop) or pressing Esc also closes it. For focus and keyboard behavior, see [Offcanvas](https://academy.bricksbuilder.io/builder/elements/general/offcanvas/#opening-closing-and-keyboard-focus).

When editing the Offcanvas in the builder make sure to enable the "Keep open while styling" setting, so the Offcanvas does not disappear when you edit different elements.

![](https://academy.bricksbuilder.io/assets/bricks-1.8-offcanvas-element-keep-open-while-styling.png)

<figcaption>

Offcanvas: Enable the "Keep open while styling" setting while editing the Offcanvas content

</figcaption>

## Non-fullscreen mobile menus {#mobile-menu-non-fullscreen}

To show the default mobile menu without it covering the full screen, edit your Nav (nestable) and set the "Height" under "Mobile menu" to `fit-content`.

This way the height of your mobile menu automatically grows or shrinks according to its content.

![](https://academy.bricksbuilder.io/assets/bricks-1.8-menu-builder-mobile-height-fit-content.png)

Then set the "Position" of your "Mobile menu" to your liking, (see screenshot above) so it doesn't cover the Toggle.

As the "Nav items" element serves as the mobile menu wrapper, you can edit it to set your mobile menu padding, background, etc. Make sure you perform those styling changes on the breakpoint at which your mobile menu starts to show, so those styles only apply to the mobile, and not the desktop menu.

Now that the mobile menu no longer covers the entire screen, you can probably remove the "Toggle (Close: Mobile)" element that Bricks adds by default.

Bonus tip: To prevent the mobile menu from covering your Toggle, which might happen on certain screen sizes & positioning, edit the Toggle element and set it's `z-index` under "Style > Layout > Z-index" to a value of `1001` or more.

---

# Nestable Slider: Customization via JavaScript

Source: https://academy.bricksbuilder.io/builder/features/nestable-slider-instance/

*Customize individual Nestable Slider instances in Bricks with JavaScript while keeping the main slider reusable.*

Bricks introduced the Nestable Slider in version 1.5, utilizing the [SplideJS](https://splidejs.com/) library.

This article is intended for developers, walking you through how to access and customize the Splide instance.

All initialized Splide instances are stored and can be accessed through `window.bricksData.splideInstances`.

You must first identify the Nestable Slider element's unique ID to retrieve the appropriate instance from the variable. You can find this ID within the builder when editing this element or through your browsers' developer tools.

![](https://academy.bricksbuilder.io/assets/how-to-get-nestable-slider-id.png)

According to the example above, I can access my Splide Instance through `window.bricksData.splideInstances['rrbqsp']`

> **Note**
>
> If you have assigned a custom CSS ID to the Slider, please note that this ID is not the same as the element ID. In such cases, you should obtain the correct element ID through your browser's developer tools.

## Update Nestable Slider options via JavaScript {#update-slider-options}

Objective: Update `noDrag` option for all Nestable Sliders on the current page.

```php
<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Define a function to update the no-drag option for all splide instances on the page
  const updateNoDragOption = () => {
    for( const splideId in window.bricksData.splideInstances ) {
      const splideInstance = window.bricksData.splideInstances[splideId]
      if ( splideInstance ) {
        // Tell Splide that any elements with .no-drag class is not draggable
        splideInstance.options = { noDrag : '.no-drag' }
      }
    }
  }

  // Need some delay for Bricks to init the sliders
  setTimeout(updateNoDragOption, 250)
})
</script>
```

## Custom navigation arrows outside the slider {#custom-arrows}

Objective: Implement custom navigation buttons located outside of the Nestable Slider.

![](https://academy.bricksbuilder.io/assets/slider-structure-example.png)

Please set unique classes for your buttons. We assigned the `my-prev` and `my-next` CSS classes in our example.

![](https://academy.bricksbuilder.io/assets/assign-css-classes-to-custom-slider-buttons.png)

Next, place a Code element and write some simple JavaScript. Remember to turn **ON **the Execute code checkbox. (Arrows for the Slider remained **OFF**)

![](https://academy.bricksbuilder.io/assets/slider-arrows-off.png)

![](https://academy.bricksbuilder.io/assets/code-element-for-custom-navigation.png)

```php
<script>
document.addEventListener('DOMContentLoaded', (event) => {
  // Give some times for Bricks to init the sliders
  setTimeout(() => {
    // Please replace rrbqsp to your Slider element ID !!NOT CSS ID!!
    const mySlider = window.bricksData?.splideInstances['rrbqsp'] || false
    // Please replace the button classes to suit your scenario
    const myPrevBtn = document.querySelector('.my-prev')
    const myNextBtn = document.querySelector('.my-next')

    if (mySlider && myPrevBtn && myNextBtn) {
      // Add click event handlers for your custom buttons
      myPrevBtn.addEventListener('click', function () {
        mySlider.go('-1') // go() function by SplideJS
      })
      myNextBtn.addEventListener('click', function () {
        mySlider.go('+1') // go() function by SplideJS
      })
    }
  }, 250)
})
</script>

```

---

# Password Protection

Source: https://academy.bricksbuilder.io/builder/features/password-protection/

*Protect Bricks content with password gates, understand how the feature works, and customize the related templates and hooks.*

Bricks 1.11.1 introduces a Bricks-native Password Protection feature, giving you a simple yet powerful way to secure content across your website without needing extra plugins.

Whether you want to lock down individual pages, posts, broader areas like custom post types, or even the entire website, you can create custom templates that control access with ease.

Customize the password entry experience, schedule when protection is active, and manage everything directly within Bricks.

https://youtu.be/PJ5R_XOyfRo

> **Note**
>
> Password protection controls Bricks-rendered frontend output. For sensitive data, use stricter security controls such as proper authentication, authorization, and file access rules.

## How to set up password protection

1. Enable this feature under `Bricks > Settings > General > Password Protection` and save. The **Password protection** template type is only available while this setting is on.
2. **Create a password protection template**
  - From the WordPress dashboard, navigate to `Bricks > Templates` and create a new template.
  - Under **Template type**, select **Password protection**.
  - Bricks fills the empty template with a starting layout: a heading, a line of text, and a form with a password field and an **Unlock** button. The form already uses the **Unlock password protection** action.
3. **Configure password protection settings**
  - Click **Edit with Bricks** to customize the template.
  - To access the password protection settings, go to `Settings > Template settings > Password protection`.
  - Available settings include:
    - **Password source:** Select how passwords are managed. Options are **Template password**, **Post password**, or **Template & post password**. See details on each method in the [password source options](#password-source-options) section below.
    - **Password:** Set the password for template-wide protection. This field is only available if the **Password source** is set to **Template password** or **Template & post password**.
    - **Disable for logged-in users:** Allow logged-in visitors to bypass the template password.
    - **Schedule:** Schedule when the template password protection is active.
      - **Start date:** Set the date and time when protection begins.
      - **End date:** Set the date and time when protection ends.

The older **Disable header**, **Disable footer**, and **Disable popups** controls are deprecated and should not be treated as ordinary controls for new password-protection templates.

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-settings.png)

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-settings-group.png)

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-settings-1.png)

4. **Set template conditions**
  - Set [the template conditions](https://academy.bricksbuilder.io/builder/features/template-settings/#template-conditions) under `Settings > Template settings > Conditions` to define where this template applies.
  - For more dynamic control, use the [`bricks/password_protection/is_active`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-is_active/) filter to customize when the template should be active or bypassed.
  - Password protection does not restrict direct access to media files, even when the template applies to the entire website. The web server delivers uploaded files without loading WordPress, so anyone with a file URL can open it. Since Bricks 2.4.6, the **Media** post type is no longer offered in password protection template conditions. Existing conditions that already include it are kept.

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-template-conditions.png)

5. **Add form element for unlocking**
  - Add a **Form Element** to the password protection template.
  - Add an **Unlock password protection** form action. This action will allow users to unlock the protected content by entering the correct password.
  - Add a password field. In the form action settings, choose that password field. If no field is selected, Bricks uses the first password field in the form.
  - You can customize the form action error message. The default error is `Incorrect password.`

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-form-action.png)

Password protection templates have priority over other matching content templates. When an active password protection template matches the current page, Bricks renders that template as the content template until the visitor unlocks the content or the protection is otherwise bypassed.

With a wrong password, the form shows its error message and the page stays locked. With the correct template password, the form shows its success message, and about a second later the page reloads with the protected content.

## Password source options {#password-source-options}

The behavior of the password protection feature depends on the selected **password source** option. Below are details on how each option works and instructions for setup:

### Template password

Selecting **Template password** applies the password set in the template settings to all pages or posts that meet the template conditions. No further configuration is needed on individual posts. Simply:

- Set the password in `Settings > Template settings > Password protection > Password`.
- Define the template conditions under `Settings > Template settings > Conditions` to specify where this template will apply.

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-template-password.png)

For any content matching these conditions, the password form will be automatically rendered, restricting access to those pages.

When a visitor enters the correct template password, Bricks stores a hashed password cookie named `brx_pp_` plus the WordPress cookie hash. The cookie is checked against the template password, so one unlock covers every page the template protects. The cookie is HTTP-only, uses the current SSL state, and expires after 10 days by default. You can customize the expiry with the [`bricks/password_protection/cookie_expires`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/) filter.

### Post password

When **Post password** is selected, this template customizes the default WordPress password protection form but requires individual post-level password settings.

To protect content using the **Post password** method:

1. Enable password protection on each post or page through the WordPress editor.
2. Set a password directly on the individual post or page (or through quick edit).
3. The template conditions will control where the custom password form appearance applies, but protection is managed at the post level.

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-wp-editor.png)

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-post-password.png)

For post passwords, Bricks uses the WordPress password-protected post flow. The Bricks form posts to the WordPress `postpass` action, and WordPress decides whether the current post still requires a password. Template password, logged-in bypass, and schedule controls are not used when the source is **Post password**.

### Template & post password

The **Template & post password** option uses the template password by default. However, if an individual post password is set, it will take precedence.

Setup process:

1. Enter a password in **Password protection > Password**.
2. Define template conditions as needed to apply the password protection across relevant content.
3. For any posts with an individual password set, that password will override the template password.

![](https://academy.bricksbuilder.io/assets/bricks-password-protection-template-and-post-password.png)

This setup provides flexibility by allowing individual content to have unique passwords while maintaining general protection for all content under the template.

## Scheduling and bypass behavior

The schedule applies to template-password protection. If no schedule is enabled, template-password protection is active whenever the template conditions match. If a start date is set, protection starts after that time. If an end date is set, protection stops after that time. The Start date and End date controls are labeled UTC+0, so enter schedule times in UTC+0.

**Disable for logged-in users** bypasses template-password protection for any logged-in visitor. If the matched post is protected with a WordPress post password and this bypass is enabled through a template-password source, Bricks also skips the WordPress password requirement for logged-in users.

If a password protection template has no template password and the source is not **Post password**, Bricks does not render the template as a password gate.

## Template parts and popups

Password protection templates can hide the normal header, footer, and popups through the deprecated **Disable header**, **Disable footer**, and **Disable popups** settings. These controls are kept for backwards compatibility.

For new templates, prefer designing the password protection template itself as the complete gate the visitor should see. If an older template has those settings enabled, Bricks will remove the matching header/footer/popup template parts while the password protection template is active.

### Password protection filters: {#filters}

- [/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-cookie-expires/)
- [/developer/hooks/filters/filter-bricks-password_protection-is_active/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-password_protection-is_active/)

---

# Popup Builder

Source: https://academy.bricksbuilder.io/builder/features/popup-builder/

*Build popups in Bricks with popup templates, template conditions, popup settings, interactions, limits, AJAX rendering, looping context, JavaScript helpers, and popup events.*

The Popup Builder lets you create fully custom popups in Bricks. A popup is a Bricks template with the template type **Popup**. Bricks renders the popup HTML on the front end, keeps it hidden by default, and opens or closes it through [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/) or JavaScript.

Use popups for modals, newsletter forms, exit-intent offers, quick views, map info boxes, and contextual content in query loops.

https://youtu.be/R9isNzCSO_A

## Create a popup template {#create-popup-template}

Create a new template and choose the **Popup** template type.

![](https://academy.bricksbuilder.io/assets/popup-template-type.png)

Save the template, then edit it with Bricks.

Popup templates look different from normal page templates:

- The canvas shows only the popup: the content box in the middle, over the dimmed backdrop.
- Template Settings includes a **Popup** group next to **Conditions** and **Populate Content**.

![](https://academy.bricksbuilder.io/assets/popup-template-type-screen.png)

Build the popup body like any other Bricks layout: add sections, containers, forms, buttons, icons, images, or dynamic data to the canvas.

## Popup availability and template conditions {#popup-template-conditions}

Template conditions decide where Bricks renders a popup template. Open **Settings > Template Settings > Conditions** and choose the pages where the popup should be available.

![](https://academy.bricksbuilder.io/assets/popup-condition.png)

For example, a newsletter popup that can open from the global footer usually needs a condition such as Entire website. A product quick-view popup may only need to be available on shop or product archive pages.

If a popup is not rendered on the current page, an interaction cannot open it because there is no popup element in the DOM. If a page has **Disable popups** enabled in Page Settings, Bricks does not render page popups.

You can render multiple popup templates on the same page.

## Popup settings {#popup-settings}

Popup-specific settings are under **Settings > Template Settings > Popup**.

![](https://academy.bricksbuilder.io/assets/popup-settings.png)

Theme Styles also have a Popup control group for site-wide defaults. It covers the popup's styling, the backdrop, the content box and the breakpoint display. Behavior settings such as **Close on**, AJAX and the popup limit are only available in the template settings of each popup.

The main popup settings include:

- **Padding**: padding on the popup wrapper.
- **Align main axis** and **Align cross axis**: position the popup content inside the viewport.
- **Close on**: by default (placeholder **Backdrop & ESC**), a click on the backdrop and the ESC key both close the popup. Choose **Backdrop (Click)**, **ESC (Key)**, or **None** to change that.
- **Z-index**: controls popup stacking.
- **Scroll (body)**: allow the page body to scroll while the popup is open. If disabled, Bricks adds `no-scroll` to the body while the popup is open.
- **Scroll to top**: scroll popup content to the top when opening.
- **Disable auto focus**: prevent Bricks from focusing the first focusable element inside the popup.
- **Disable auto focus on close**: prevent Bricks from moving focus back to the element that was focused before the popup opened.
- **Info Box (Map)**: use this popup template as the info box of a map element.
- **Fetch content via AJAX**: render popup content on demand instead of in the initial DOM.
- **AJAX loader**: choose a loader animation and optional selector, color, and scale for AJAX popups.
- **Breakpoints**: choose where the popup is allowed to display.
- **Backdrop**: **Disable backdrop**, the backdrop **Background**, and its **Transition**.
- **Content**: style the `.brx-popup-content` wrapper.
- **Popup limit**: restrict how often the popup can open.

On the front end, Bricks traps keyboard focus inside open popups, restores focus after closing, supports ESC/backdrop closing according to the **Close on** setting, and emits popup JavaScript events.

> **Note**
>
> Clicking outside the popup or pressing ESC only closes the popup if the **Close on** setting includes that behavior. If you set Close on to None, add your own close interaction or JavaScript.

## Popup interactions {#popup-interactions}

Further down the popup settings panel, the **Interactions** group lets the popup react to events. Popup template interactions use the same interaction system as elements, plus two popup-specific triggers:

- **Show popup**: runs after this popup opens.
- **Hide popup**: runs after this popup closes.

Use these triggers when the popup itself should run follow-up actions, such as starting an animation, setting storage, or updating another element after the popup has opened or closed.

> **Note**
>
> For **Hide popup**, target a CSS selector rather than the popup directly. The trigger runs after the popup has already closed.

Most popups are opened by an interaction on another element. For example, add a Click interaction to a Button, set **Target** to Popup, select the popup template, and use **Show element**.

A common automatic popup uses **Content loaded**:

![](https://academy.bricksbuilder.io/assets/bricks-popup-builder-interaction-content-loaded-465x1024.png)

If no popup interaction exists on the popup itself and no other element interaction opens the popup, the popup stays hidden.

## Popup open and close lifecycle {#popup-lifecycle}

When Bricks opens a popup, it follows this front-end flow:

1. Resolve the popup element by template ID or element node.
2. Check popup limits.
3. Check popup breakpoint rules.
4. Remove the `hide` class.
5. Add `no-scroll` to the body unless body scroll is allowed.
6. Fetch AJAX popup content if the popup is configured for AJAX.
7. Insert AJAX content into `.brx-popup-content`, if content was fetched.
8. Emit `bricks/ajax/popup/loaded`, only for AJAX content that was inserted.
9. Emit `bricks/popup/open`.
10. Increment the popup counters.

When Bricks closes a popup, it adds the `hide` class, removes `no-scroll` from the body if no other non-body-scroll popup is open, and emits `bricks/popup/close`.

This lifecycle matters for custom code:

- Listen to `bricks/ajax/popup/loaded` when you need newly fetched AJAX popup DOM to exist.
- Listen to `bricks/popup/open` when you need the popup to be open.
- Listen to `bricks/popup/close` when you need cleanup after close.

## Popup limit {#limit}

By default, a popup can open every time it is triggered. Use **Settings > Template Settings > Popup > Popup limit** to restrict how often it opens.

Bricks checks limits before opening the popup. Once a limit is reached, the popup does not open and the open event is not emitted.

The limit applies to every way of opening the popup: an automatic trigger, a click on a button, or `bricksOpenPopup()`. Use limits for popups that open on their own. A popup that a visitor opens with a button stops opening once its limit is reached.

There are four popup limit controls:

| Limit type | Browser storage | Description |
| --- | --- | --- |
| Per page load | `window.brx_popup_{id}_total` | Resets after the page reloads. |
| Per session | `sessionStorage.brx_popup_{id}_total` | Resets when the browser session/tab storage is cleared. |
| Across sessions | `localStorage.brx_popup_{id}_total` | Persists until local storage is cleared. |
| Show again after .. hours | `localStorage.brx_popup_{id}_lastShown` | Stores the last shown timestamp and waits the configured number of hours before allowing another open. |

![](https://academy.bricksbuilder.io/assets/bricks-1.6-popup-limit.png)

The page-load, session, and across-session counters increment each time the popup is successfully opened. The hour-based setting stores the last shown timestamp when the popup passes its limit check.

## Popup breakpoints {#popup-breakpoints}

Popup breakpoint settings control whether a popup is allowed to display at the current viewport width.

Bricks supports two modes:

- **Start display at breakpoint**: show the popup at or above the selected breakpoint width.
- **Display on breakpoints**: show the popup only inside the selected breakpoint ranges.

If the current viewport does not match the popup breakpoint rule, Bricks does not open the popup.

## Closing a popup {#closing-popup}

You can close a popup in several ways:

- Use the popup **Close on** setting for backdrop click and/or ESC.
- Add a close icon or button inside the popup and give it a Hide element interaction targeting the popup.
- Use a reusable close element that targets `.brx-popup`.
- Call `bricksClosePopup()` from JavaScript.

### Example: Add popup close icon {#example-close-icon}

Add an Icon element to your popup. Set its cursor to pointer under **Styles > Layout > Misc**.

> **Tip**
>
> An icon can't be reached with the keyboard. To make the close control keyboard accessible, use a Button element instead and set its **HTML tag** to `button`. Without a link, a Button element renders as a `span` by default.

Open the Icon element's Interactions panel and add:

- Trigger: Click
- Target: Popup
- Popup: the current popup
- Action: Hide element

![](https://academy.bricksbuilder.io/assets/popup-close-icon-interaction.png)

If you want to reuse the same close icon in different popups, create it as a [Component](https://academy.bricksbuilder.io/builder/features/components/). Then use:

- Target: CSS selector
- CSS selector: `.brx-popup`
- Action: Hide element

![](https://academy.bricksbuilder.io/assets/popup-global-close-icon-interaction.png)

## JavaScript helper functions and events {#events-functions}

Bricks exposes popup helper functions and custom events on the front end.

### Open or close a popup via JavaScript {#popup-js-functions}

Use `bricksOpenPopup` and `bricksClosePopup` to open or close Bricks popups.

Both functions accept a popup template ID or a popup element node:

```php
bricksOpenPopup(3321)
bricksClosePopup(3321)
```

```php
const popup = document.querySelector('.brx-popup[data-popup-id="3321"]')

bricksOpenPopup(popup)
bricksClosePopup(popup)
```

### Example: Open popup by selector {#open-popup-by-selector}

```php
document.querySelectorAll('.brxe-heading, .my-custom-selector').forEach((el) => {
  el.addEventListener('click', () => {
    bricksOpenPopup(3321)
  })
})
```

### Listen to popup open or close events {#popup-js-events}

Use `bricks/popup/open` and `bricks/popup/close` to run code when a popup opens or closes.

<span id="bricks-popup-open-close-code"></span>

```php
document.addEventListener('bricks/popup/open', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 popup is opened')
  }
})

document.addEventListener('bricks/popup/close', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 popup is closed')
  }
})
```

Use `event.detail.popupId` and `event.detail.popupElement`. The property is `detail`, not `details`.

## Popup inside query loop {#query-loop}

You can add a popup inside a query loop with the **Template** element. Inside the popup template, dynamic data can reference the current loop item.

The example below shows a Quick View button inside a product query loop. The button uses an interaction to show the selected Quick View popup.

![](https://academy.bricksbuilder.io/assets/bricks-1.6-popup-inside-query-loop-1024x403.jpg)

For Bricks 1.7.1 and newer, Bricks can build loop-specific popup HTML for query loop popups. For older versions, do not set the interaction on the Query Loop div itself; set it on an element inside the loop item.

![](https://academy.bricksbuilder.io/assets/query-loop-popup-template-interaction-structure.png)

<figcaption>

Example layout structure to trigger a looping popup for Bricks versions earlier than 1.7.1

</figcaption>

### Example: Open a looping popup by query element ID and loop index {#open-looping-popup-by-query-element-id-and-loop-index}

If a looping popup is already rendered on the page, you can target it by its query element ID and loop index:

```php
document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const queryId = 'vfiqrn'
    const targetPopup = document.querySelector(
      `.brx-popup[data-popup-loop="${queryId}"][data-popup-loop-index="7"]`
    )

    bricksOpenPopup(targetPopup)
  }, 200)
})
```

The small delay is useful in custom code elements because it gives Bricks frontend globals and popup markup time to initialize.

## AJAX popup {#ajax}

AJAX popups were introduced in Bricks 1.9.4. Enable **Fetch content via AJAX** when you want Bricks to keep the initial DOM lighter and fetch popup content only when the popup opens.

This is especially useful for popups inside query loops, where rendering every popup's full content on initial page load can be expensive.

![](https://academy.bricksbuilder.io/assets/ajax-popup-controls-in-popup-template.png)

When AJAX is enabled:

- The popup wrapper is rendered on the page.
- `.brx-popup-content` starts empty outside the builder preview.
- Bricks fetches the content from the REST endpoint when the popup opens.
- Returned HTML and dynamic CSS are inserted into `.brx-popup-content`.
- Additional nested popup HTML can be appended to the body if the AJAX content contains looping AJAX popups.

AJAX popup rendering supports post, term, and user context. Dynamic data that does not have a stable object ID, such as some repeater rows, cannot always be resolved as an AJAX popup context.

### Query loops inside AJAX popups (since 2.5) {#ajax-query-loops}

Query loops inside an AJAX popup support **Load more**, **Infinite scroll** and AJAX pagination. Pagination links point to the page that opened the popup, not to the popup request, and query filters inside the popup keep working. The selected page is restored when the popup is reopened or the page is reloaded.

Each popup query keeps its own post, term, or user context instead of inheriting the context of the page that opened it.

### AJAX popup context settings {#ajax-context-settings}

When an interaction opens a popup, Bricks exposes context controls for AJAX popups:

![](https://academy.bricksbuilder.io/assets/context-controls-in-interactions-ui.png)

Bricks tries to infer the current context automatically. Inside normal post, term, and user loops, this often works. In nested query loops, component instances, custom field repeaters, or more complex dynamic data setups, automatic context can be wrong or unavailable.

Use these fields when dynamic data in the AJAX popup renders empty or from the wrong object:

- **Context type**: Post, Term, or User.
- **Context ID**: the object ID to render dynamic data against.

You can use dynamic data such as `{post_id}`, `{term_id}`, or a custom field value that resolves to a post, term, or user ID.

![](https://academy.bricksbuilder.io/assets/example-for-woo-product-quick-view-setup.png)

<figcaption>

A looping product quick-view popup structure in Bricks

</figcaption>

> **Note**
>
> Do not use a repeater row number as popup context. AJAX popup context expects an object Bricks can resolve, such as a post, term, or user.

### Open an AJAX popup with context in JavaScript {#open-ajax-popup}

Since Bricks 1.9.4, `bricksOpenPopup` accepts three parameters:

- `object`: popup ID or popup element node.
- `timeout`: timeout in milliseconds used by popup animation/counter logic.
- `additionalParams`: AJAX popup context data.

```php
bricksOpenPopup(
  1190,
  0,
  {
    popupContextId: 668,
    popupContextType: 'post'
  }
)

bricksOpenPopup(
  2350,
  0,
  {
    popupContextId: 39,
    popupContextType: 'term'
  }
)
```

For users, the Interactions panel usually handles these parameters. Use JavaScript when you are opening popups from custom scripts.

### AJAX popup events {#ajax-events}

AJAX popups emit three AJAX-specific events:

- `bricks/ajax/popup/start`: emitted before the AJAX popup request is made.
- `bricks/ajax/popup/end`: emitted after the AJAX popup request finishes.
- `bricks/ajax/popup/loaded`: emitted after fetched popup content is inserted into the DOM.

Each event uses `event.detail.popupId` and `event.detail.popupElement`.

```php
document.addEventListener('bricks/ajax/popup/loaded', (event) => {
  const popupId = event.detail.popupId
  const popupElement = event.detail.popupElement

  if (popupId == 3321) {
    console.log('3321 AJAX popup content DOM loaded')
  }
})
```

The AJAX popup open sequence is:

1. `bricks/ajax/popup/start`
2. `bricks/ajax/popup/end`
3. `bricks/ajax/popup/loaded`
4. `bricks/popup/open`

`bricks/ajax/popup/loaded` only fires when AJAX content is inserted. Non-AJAX popups emit `bricks/popup/open` directly after opening.

## Popup setup examples {#popup-setup-examples}

### Example: Show popup when the mouse leaves the browser window {#example-mouse-leaves}

After creating the popup template and layout, open **Settings > Template Settings > Popup**, scroll to Interactions, and add a **Mouse leave window** interaction that shows the popup.

![](https://academy.bricksbuilder.io/assets/popup-builder-mouse-leave-open.png)

For a real exit-intent popup, combine this with popup limits or browser storage conditions so the popup does not appear too often.

### Example: Show popup before a date/time {#example-date-time}

Template conditions decide where the popup template is available. Element Conditions can decide whether the popup content renders.

To show a popup only before a specific date, add an [Element Condition](https://academy.bricksbuilder.io/builder/features/element-conditions/) to the outermost popup element.

![](https://academy.bricksbuilder.io/assets/bricks-popup-builder-element-conditions-1536x624.png)

If that condition is not fulfilled, Bricks does not render the popup content and skips the popup HTML. A trigger that targets that popup has no popup element to open on the page.

### Example: Use popup open/close as triggers {#example-popup-open-close-trigger}

Popup template interactions can react after the popup opens or closes.

For example:

1. Open **Settings > Template Settings > Popup > Interactions**.
2. Add a **Show popup** trigger.
3. Set the action to Browser storage: Count.
4. Store a key such as `newsletter_popup_opened`.

You can then use interaction conditions elsewhere to check that key and adjust page behavior.

---

# Remote Components

Source: https://academy.bricksbuilder.io/builder/features/remote-components/

*Share Bricks components between sites, review their dependencies, and import updates from the Component Manager.*

Remote Components let one Bricks site expose selected components and another Bricks site import them from the Component Manager. Use this for component libraries that you maintain across client sites, staging sites, or related projects.

Remote Components are available in Bricks 2.4. Both sites need Bricks 2.4 or later for remote component browsing and dependency-complete imports.

A remote import creates a local component. It does not keep a live connection to the source site, but Bricks records where the component came from so a later import can detect and apply source changes.

## Before You Start

You need:

- A **source site** that contains the components you want to share.
- A **destination site** where you want to import them.
- A non-Plain WordPress permalink structure on the source site.
- Permission to configure Bricks settings on both sites.
- The required [builder permissions](#permissions) for the user importing the component.

## 1. Expose Components on the Source Site

On the source site:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **My components**, enable **My components access**.
3. If needed, choose components under **Exclude components**.
4. Configure the shared **Remote access** controls.
5. Save the settings.

![Remote component access and shared remote access settings in Bricks](https://academy.bricksbuilder.io/assets/remote-components-source-access-settings.webp)

### Exclude Components

Components selected under **Exclude components** do not appear in the remote catalog.

Bricks also blocks the import of any component that depends on an excluded component. For example, if a Card component contains an excluded Button component, the Card may appear in the catalog, but the destination site cannot import it until the Button is allowed or removed from the Card.

### Restrict Remote Access

The **Remote access** settings apply to both remote templates and remote components:

- **Whitelist URLs** allows only the listed destination sites to connect. Enter one URL per line. Leave it empty to allow requests from any site that meets the other access requirements.
- **Password protection** requires destination sites to send the same password. Use the password generator or enter your own value.

Enabling **My components access** without a whitelist or password allows other Bricks sites that know the source URL to browse the exposed component catalog.

## 2. Add the Source to the Destination Site

On the destination site:

1. Go to **Bricks > Settings > Templates & components**.
2. Find **Remote libraries** and click **Add**.
3. Enter the source site's full **URL**.
4. Enter a **Name** to control how the source appears in the builder. This is optional.
5. If the source uses password protection, enter its **Remote access** password.
6. Save the settings.

The same remote-library entry can provide templates, components, or both, depending on what the source site exposes.

![A configured HappyFiles remote library on the destination Bricks site](https://academy.bricksbuilder.io/assets/remote-components-remote-library-settings.webp)

## 3. Browse the Remote Component Library

Open the builder, click the folder icon to open the [Builder Browser](https://academy.bricksbuilder.io/builder/features/builder-browser/), and select **Components**.

Use the **Source** dropdown to switch from **My components** to a configured remote site. Remote libraries appear only when the current user has **Access remote components** permission.

For a remote source, you can:

- Search by component name.
- Filter by category.
- Switch between grid and list view.
- Click **Refresh** to request the catalog again.
- Click **Load more** when the catalog has additional pages.
- View source-provided component thumbnails.

![A HappyFiles remote component library open in the Bricks Builder Browser](https://academy.bricksbuilder.io/assets/remote-components-builder-browser.webp)

If the source cannot be reached or does not support Remote Components, the Component Manager shows the returned source error instead of a component list.

## 4. Review and Import a Component

Click the import icon on a remote component. Bricks first inspects the package and opens a review for the component and any related design-system data.

Save pending component, global class, global variable, and color changes before importing. Bricks blocks the import when these local changes are unsaved so it does not overwrite a newer in-memory design system with an older saved version.

The review can include:

- Nested components.
- Global classes and their categories.
- Global variables, their categories, and variables referenced by other variables.
- Color palettes containing referenced colors.

Matching local dependencies are skipped automatically. You can skip the Global classes, Global variables, or Color palettes step. The skipped group is not added. When you skip global classes, Bricks also removes those class assignments from the imported component. Review the component after using **Skip**.

Referenced images hosted on the configured source site are downloaded to the destination Media Library when the importing user can upload files. Images from other hosts are left unchanged.

![The Global classes step of the remote component import review](https://academy.bricksbuilder.io/assets/remote-components-import-review.webp)

### Name Conflicts

If an unrelated local component already has the same name, Bricks asks for a name for the imported component and suggests one based on the remote-source name. The local component is left unchanged.

Nested components with conflicting names are renamed during the import. Their references are remapped to the imported local copies.

### Previously Imported Components

Bricks tracks each imported component by its remote source and remote component ID.

- If the remote package is unchanged, Bricks reports that the component is already imported.
- If the remote component or one of its nested components changed, the review marks the existing local copy for replacement.
- Replacing a previously imported component keeps its local identity, so existing instances use the updated definition.

Local components that merely share the same name are not treated as previous imports. Provenance, not the label, controls repeat-import behavior.

After a successful import, Bricks returns to **My components**, refreshes the affected components and design-system data, and highlights the imported component.

On a multisite installation configured to use main-site components, the import uses that shared component store instead of creating a separate child-site copy.

Bricks validates the package before writing it and prevents concurrent remote imports. If an import fails after changes begin, Bricks restores the saved component and design-system data.

## What Does Not Transfer Automatically

The package includes the component graph and the referenced Bricks design-system data listed above. Some site-specific features need attention on the destination site.

Bricks shows portability warnings when it detects items such as:

- Query or Global Query settings.
- Icons.
- Executable code.
- Dynamic data.
- Custom fonts.
- Element types that the destination site does not support.

A warning does not always block the import. It tells you to verify the imported component against the destination site's plugins, content model, fonts, icon sets, queries, and code permissions.

Code signatures from the source are not trusted. Bricks removes source signatures and runs imported code through the destination site's normal signing and code-permission flow. Users without code-execution permission receive redacted code-sensitive settings.

### Missing Global Classes

If a component references a global class ID that no longer exists on the source site, the review shows the missing ID and blocks the normal import.

Fix the source component before trying again:

1. Edit the component on the source site.
2. Remove or replace the missing class reference.
3. Save the component and design-system data.
4. Refresh the remote library on the destination site.
5. Import the component again.

Skipping the Global classes step skips every class listed in that step, not only the missing class. Bricks removes those class assignments from the imported component.

## Permissions

Remote component operations combine separate [builder permissions](https://academy.bricksbuilder.io/builder/interface/builder-access/#components):

| Task | Required permissions |
| --- | --- |
| See configured remote sources and browse their catalogs | **Access remote components** |
| Import a component from a remote source | **Access remote components** and **Import/export components** |
| Insert the imported local component onto a page | **Insert components** |
| Insert a remote template that contains components | **Access remote templates**, **Insert templates**, **Access remote components**, **Import/export components**, and **Insert components** |
| Save a remote template to My Templates when it contains components | **Access remote templates**, **Import/export templates**, **Access remote components**, and **Import/export components** |

Administrators have full builder access. Other users need a custom builder capability with the permissions required for their workflow.

## Troubleshooting

### A Remote Site Is Missing From the Source Dropdown

- Confirm the remote library is saved under **Bricks > Settings > Templates & components**.
- Confirm the current user has **Access remote components** permission.
- Reload the builder after saving the settings.

### The Source Loads, but No Components Appear

- Enable **My components access** on the source site.
- Check whether the components are selected under **Exclude components**.
- Confirm the destination URL matches the source whitelist exactly after URL normalization.
- Confirm the destination has the current **Remote access** password.
- Confirm both sites run Bricks 2.4 or later.

### An Import Says the Component Depends on an Excluded Component

Allow the nested dependency under **Exclude components**, or remove that nested component from the component you are sharing. Bricks will not create an incomplete component graph.

### Bricks Asks You to Save Changes First

Save the current component, class, variable, and color changes, then start the import again. If another import changed the saved design system while the review was open, inspect the component again to create a current import plan.

For local component creation, properties, variants, slots, and instance behavior, see [Components](https://academy.bricksbuilder.io/builder/features/components/). For sharing templates between sites, see [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/).

---

# Remote Templates

Source: https://academy.bricksbuilder.io/builder/features/remote-templates/

*Connect Bricks sites, browse shared template libraries, and transfer templates with their component dependencies.*

Remote Templates let you browse and insert templates from another Bricks installation without exporting and importing files manually.

The workflow has two sides:

- The **source site** exposes selected templates through its remote library.
- The **destination site** adds that site under **Remote libraries** and accesses its templates from the Builder Browser.

## 1. Expose Templates on the Source Site

On the site that contains the templates:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **My templates**, enable **My templates access**.
3. Use **Exclude templates** to hide any templates that should not be shared.
4. Configure the shared **Remote access** controls.
5. Save the settings.

![Bricks Templates and components settings with My templates access enabled and Exclude templates visible](https://academy.bricksbuilder.io/assets/bricks-settings-remote-templates-access.webp)

The **Remote access** settings apply to remote templates and remote components:

- **Whitelist URLs** restricts access to the listed destination sites. Enter one URL per line.
- **Password protection** requires destination sites to provide the same password.

If both fields are empty, any Bricks site that knows the source URL can request the templates exposed by **My templates access**.

The source site's WordPress permalink structure must not be set to **Plain**.

![](https://academy.bricksbuilder.io/assets/permalink-structure-not-plain-type-for-remote-templates-01.png)

## 2. Add a Remote Site on the Destination Site

On the site where you want to use the templates:

1. Go to **Bricks > Settings > Templates & components**.
2. Under **Remote libraries**, click **Add**.
3. Enter the source site's full **URL**.
4. Optionally enter a **Name**. Bricks shows this instead of the URL in source dropdowns.
5. Enter the source site's **Remote access** password, if it uses one.
6. Save the settings.

You can add multiple remote sites. The same entry can provide templates, components, or both.

![Remote libraries settings with Name, URL, and Password fields](https://academy.bricksbuilder.io/assets/bricks-settings-remote-libraries.webp)

## 3. Browse Remote Templates

Open the builder, click the folder icon, and select **Templates** in the [Builder Browser](https://academy.bricksbuilder.io/builder/features/builder-browser/).

Choose the remote site under **Source**. You can search the library, filter its templates, switch between grid and list view, and use **Reload** to request the source again.

The current user needs **Access remote templates** permission to see configured remote sites.

![Builder Browser Templates view with HappyFiles selected as the remote source](https://academy.bricksbuilder.io/assets/bricks-browser-remote-templates.webp)

## Insert a Remote Template

Click **Insert** to add the template to the current canvas. The **Replace content** control decides whether Bricks replaces the current canvas or adds the template to it.

Use **Import images** to download eligible template and component images to the destination Media Library. Leave it disabled to use placeholder images where the normal template import flow supports them.

When the remote template includes related design-system data, Bricks may open additional reviews for theme styles, color palettes, variables, global classes, or Style Manager settings.

Remote code signatures are not trusted. Bricks removes source signatures, and users without code-execution permission do not receive executable Code, SVG, or custom-query settings from the remote template.

### Templates That Use Components

In Bricks 2.4 and later, inserting a remote template also requests the components used by that template. The dependency package includes nested components and their referenced global classes, variable categories and variables, and color palettes.

Bricks remaps the template to the imported local component and design-system IDs before inserting it. Save pending component, class, variable, and color changes before starting the insert.

If a component from this source was imported before and changed remotely, Bricks asks whether to replace the local component before inserting the template. Replacing it updates the existing local component definition and its instances.

If the template depends on a component excluded from remote access on the source site, Bricks blocks the dependency package instead of inserting an incomplete component graph.

## Import to Templates

Click **Import to templates** on a non-local template to save it into **My Templates** instead of inserting it directly onto the current canvas.

For a configured Bricks remote site, Bricks first localizes supported component and design-system dependencies, then passes the template through the regular template import flow. The current user needs **Import/export templates** permission.

## Compatibility With Older Remote Sites

Bricks 2.4 introduces a versioned remote-library package for templates with component dependencies.

When a configured source does not support that package protocol, Bricks falls back to the legacy Remote Templates response. The template can still use the older insertion workflow, but the legacy response does not provide the dependency-complete component package. Update the source site before sharing templates that use components.

## Permissions

Remote template operations use separate builder permissions:

| Task                                                                 | Required permissions                                                                                                     |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| See configured remote sites                                          | **Access remote templates**                                                                                              |
| Insert a remote template without component dependencies              | **Access remote templates** and **Insert templates**                                                                     |
| Save a remote template under My Templates                            | **Access remote templates** and **Import/export templates**                                                              |
| Insert a remote template with component dependencies                 | The insert permissions above, plus **Access remote components**, **Import/export components**, and **Insert components** |
| Import a remote template with component dependencies to My Templates | The template import permissions above, plus **Access remote components** and **Import/export components**                |

See [Builder Access & Capabilities](https://academy.bricksbuilder.io/builder/interface/builder-access/) for assigning these permissions.

## Fetching and Caching

Bricks keeps fetched template data outside the WordPress database. Remote template data can be cached in the builder browser for up to seven days per source. Use **Reload** when you need the source again before that cache expires.

Remote-library capability checks and component catalogs use shorter server-side caches. In the Component Manager, **Refresh** bypasses those short caches and requests the source again.

## Troubleshooting

### A Remote Site Does Not Appear

- Confirm the remote library row is saved under **Templates & components**.
- Confirm the current user has **Access remote templates** permission.

### A Remote Site Appears but Does Not Load

Check the source site:

- **My templates access** is enabled.
- Permalinks are not set to **Plain**.
- The destination site's URL is included under **Whitelist URLs**, when used.
- The password saved on the destination matches **Remote access > Password protection**.
- The expected templates are not selected under **Exclude templates**.

### A Template With Components Cannot Be Inserted

- Save pending component, class, variable, and color changes on the destination.
- Confirm the user has the required component permissions.
- Confirm every component dependency is available and not excluded on the source.
- Update the source to Bricks 2.4 or later if it only supports the legacy template response.

For the template library controls and local template actions, see [Template Library](https://academy.bricksbuilder.io/builder/features/template-library/).
