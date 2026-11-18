*Edit Bricks designs responsively across breakpoints and adjust layout, spacing, and element settings for smaller screens.*

What looks great on a large desktop screen usually needs some refinement for smaller devices. This typically involves applying smaller font sizes, margins, paddings, column width/stacking, or hiding certain elements on smaller devices.

Bricks provides the following four breakpoints out-of-the-box:

| **Breakpoint** | **@media query** |
| --- | --- |
| Desktop | Base breakpoint |
| Tablet portrait | &lt; 992px |
| Mobile landscape | &lt; 768px |
| Mobile portrait | &lt; 478px |

Styles set on the base breakpoint are inherited by all other breakpoints.

Once you've finished styling a page on the base breakpoint (desktop), make sure to view & adjust the styling on the other breakpoints too.

## Background videos at different breakpoints {#responsive-background-video}

Since Bricks 2.5, background videos on **Section**, **Container**, **Block**, and **Div** elements can use different URLs and playback settings at each breakpoint. Open **Style > Background** on the element or its global class.

Set the video on the base breakpoint, then switch to another breakpoint to change only the settings it needs. The URL, aspect ratio, scale, start and end times, **Play once**, poster, and YouTube/Vimeo options inherit through breakpoints. Inherited settings appear as placeholders; entering a value creates a local override. Clear a local value to use the inherited setting again.

Use **Background video** to choose:

- **Enable**: Play the resolved video at this breakpoint.
- **No video**: Show the element's normal background instead. Set a background image or color if needed.

For example, use a wide video at Desktop, enter a shorter video URL at Tablet portrait, and choose **No video** at Mobile portrait. Bricks loads the matching breakpoint's video and stops the previous video when the breakpoint changes. This applies to uploaded videos, YouTube, and Vimeo.

At Tablet portrait, the video URL is a local override while playback settings such as **Start time (s)** remain inherited:

<div className="screenshot screenshot--control-panel">

![Tablet portrait Background video controls with a local Video URL and an inherited Start time of 0.](https://academy.bricksbuilder.io/assets/builder/release-2.5/video-tablet-panel.webp)

</div>

At Mobile portrait, **No video** leaves the normal background visible:

<div className="screenshot screenshot--control-panel">

![Mobile portrait Background video set to No video.](https://academy.bricksbuilder.io/assets/builder/release-2.5/video-mobile-panel.webp)

</div>

### Existing background videos

Updating Bricks does not activate previously ignored breakpoint-specific video URLs. Existing videos keep their previous output until you intentionally edit a video setting. The first edit switches that element or class to responsive video settings. Bricks uses the previously rendered video and playback behavior as the starting point, then applies your edit.

Older videos may have a **Start play at** restriction. That restriction survives the first edit; changing the legacy video URL alone does not remove it. To allow playback at a restricted breakpoint, explicitly choose **Background video > Enable** there. A poster can still appear below the old playback threshold.

Entering a new URL at another breakpoint also enables video there if it inherited **No video**. Choose **No video** again if you want that breakpoint to keep its normal background.

Class videos are inherited rather than copied into each element. Editing a class video does not switch an element's own untouched legacy video to responsive behavior. Check elements with their own video separately after changing a shared class.

To view & edit the styles for a specific breakpoint simply click on its breakpoint icon located in the center of the builder toolbar. Or use the default [keyboard shortcut](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) `CMD/CTRL + B`.

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-in-builder-breakpoint-mobile-landscape-1024x576.jpg)

<figcaption>

Editing in the "Mobile landscape" breakpoint

</figcaption>

Next to the breakpoint icons are inputs for width ("W"), height ("H"), and scale (%).

## Inherited background images {#inherited-background-images}

Since Bricks 2.5, an inherited background image appears as a dimmed preview under **Style > Background**. Its remove button and image-size selector stay hidden until you select an image at the current breakpoint, creating a local override.

## Custom Breakpoints {#custom-breakpoints}

To start using custom breakpoints, you first have to enable them in your WordPress dashboard under `Bricks > Settings > General > Custom breakpoints`:

![](https://academy.bricksbuilder.io/assets/bricks-enable-custom-breakpoints.jpg)

Once enabled, you can access the **breakpoint manager** in the builder by clicking the three-dotted icon in the builder toolbar (next to the first breakpoint icon):

![](https://academy.bricksbuilder.io/assets/bricks-1.5.1-breakpoint-manager-default-breakpoints.jpg)

<figcaption>

Breakpoint Manager (open via the three-dotted icon in the builder toolbar)

</figcaption>

### Editing a breakpoint

Clicking the pencil icon brings up the editing options of the selected breakpoint:

![](https://academy.bricksbuilder.io/assets/bricks-edit-default-breakpoint.jpg)

<figcaption>

Editing the default "Tablet portrait" breakpoint

</figcaption>

You can edit the following breakpoint properties:

| **Property** | **Description** |
| --- | --- |
| Label | Used when hovering over the breakpoint icon in the builder toolbar |
| Width (px) | @media query min-width/max-width value (depending on the base breakpoint) |
| Width (Builder) | Width is used when switching to the breakpoint in the builder |
| Icon | Used as the breakpoint icon in the builder toolbar |
| Base breakpoint | Set breakpoint as base breakpoint |
| *Key* | *Not customizable (used to store & identify breakpoint settings)* |

The most common action is to customize the widths of the default (mobile) breakpoints. The following screenshot shows you the "Tablet portrait" with a custom width of 1023px:

![](https://academy.bricksbuilder.io/assets/bricks-edit-breakpoint-width.jpg)

That means any styles set on the "Tablet portrait" breakpoint will apply to devices with a width of less than 1024px.

### Creating new breakpoints

You can create as many additional custom breakpoints as you want. Although, it is recommended to customize the widths of the default mobile breakpoints to your liking before utilizing more breakpoints.

You should rarely need more than one or two additional breakpoints on top of the default ones.

Clicking the "+" (plus) icon in the breakpoint manager's header launches the breakpoint creator form.

The following screenshot shows how we created a  new breakpoint named "Large" with a width of 1400px:

![](https://academy.bricksbuilder.io/assets/bricks-create-new-breakpoint.jpg)

<figcaption>

Creating a new breakpoint

</figcaption>

Once you click "Create" your newly created breakpoint should appear in the breakpoint manager (alongside a "CUSTOM" label) & in the builder toolbar like this:

![](https://academy.bricksbuilder.io/assets/bricks-custom-breakpoint-large-created.jpg)

<figcaption>

Breakpoint manager with new custom breakpoint

</figcaption>

As we've set the width of this new breakpoint to 1400px, it shows as the first breakpoint, as it is now the largest of our breakpoints. The Desktop (base breakpoint) has a default width of 1279px.

### Pausing a custom breakpoint

You can pause any of your custom breakpoints by toggling the checkbox at the right-hand side of the breakpoint manager:

![](https://academy.bricksbuilder.io/assets/bricks-pause-custom-breakpoint.jpg)

<figcaption>

Pausing custom breakpoint "Large"

</figcaption>

Pausing a custom breakpoint allows you to skip generating the styles for it on the frontend, while still retaining the styles you've set throughout your site without having to delete them one by one. Which, on a full-built-out site, can go into thousands of settings.

### Resetting a default breakpoint

To restore the default values of a default breakpoint, click on the "reset" icon (next to the pencil) icon.

### Resetting all breakpoints

Clicking the "gear" icon in the breakpoint manager header opens up the "Reset: Breakpoints" action. Clicking this button removes all your breakpoint edits (default & custom breakpoints) from the database.

> **Note**
>
> **Breakpoint-specific settings performed on an element or the Theme Styles are not deleted. Please choose desktop or mobile-first at the very beginning.**

![](https://academy.bricksbuilder.io/assets/bricks-reset-all-breakpoints.jpg)

### Understanding the base breakpoint

The base breakpoint doesn't have a @media query. So all styles set on the base breakpoint apply to all screen widths.

That is why, by default, any styles set on the "Desktop" breakpoint are visible on any other breakpoint. Unless you specify a style on a specific breakpoint. Then the breakpoint-specific rule precedes the base breakpoint style.

When editing a breakpoint, you can set it as the "Base breakpoint". Then all styles set on this new base breakpoint are inherited up & down the breakpoint chain.

In the following screenshot, you can see that the "Tablet portrait" breakpoint has been set as the base breakpoint.

The yellow dot, lines, and arrows next to the breakpoint icons should help to visualize the style inheritance:

![](https://academy.bricksbuilder.io/assets/bricks-custom-base-breakpoint.jpg)

<figcaption>

Changed base breakpoint to "Tablet portrait"

</figcaption>

### Mobile-first design {#mobile-first}

Styling in Bricks, by default, happens from the largest breakpoint down to "Tablet portrait" > "Mobile landscape" and "Mobile portrait".

Utilise a so-called `**mobile-first**` design approach by setting the smallest breakpoint as the base breakpoint.

The following screenshot shows the "Mobile portrait" (our smallest breakpoint) set as the base breakpoint. We now use the mobile-first approach. Also indicated by the "MOBILE FIRST" label in the breakpoint manager header:

![](https://academy.bricksbuilder.io/assets/bricks-mobile-first.jpg)

<figcaption>

Mobile-first design in Bricks

</figcaption>

You'll also notice that the order of the breakpoints is reversed and now starts at the smallest breakpoint. You can now start to design your pages starting at the smallest breakpoint.

### Regenerating (Bricks) CSS files

Whenever you customize the width of a default breakpoint, Bricks automatically updates any Bricks CSS files (like frontend.min.css, etc.) that contain media queries for this breakpoint.

If you experience that your breakpoint widths on the front end are not correctly applied, please regenerate your Bricks CSS files by clicking the "Regenerate CSS files" button under `Bricks > Settings > General > Custom breakpoints`.

## Breakpoint data attribute {#breakpoint-data-attribute}

Since Bricks 2.5, the **Breakpoint data attribute** setting exposes the active breakpoint key for use in custom CSS and JavaScript. Enable it under **Bricks > Settings > General > Breakpoint data attribute**, then save your settings. It is disabled by default and works with both default and custom breakpoints.

When enabled, Bricks adds `data-brx-breakpoint` to the page's `<body>` element on the frontend and in the Builder canvas. For example:

```html
<body data-brx-breakpoint="mobile_portrait">
```

The value updates when the viewport crosses a breakpoint boundary.

### Breakpoint keys and matching

The attribute contains one breakpoint key at a time. It uses the smallest matching `max-width` breakpoint or the largest matching `min-width` breakpoint. The base breakpoint key applies only when no other enabled breakpoint matches. Paused custom breakpoints are excluded.

The default keys are `desktop`, `tablet_portrait`, `mobile_landscape`, and `mobile_portrait`. Custom breakpoints use their own keys. Renaming a breakpoint's label does not change its key or the attribute value. Inspect the page's `<body>` element in your browser's developer tools to check the active key.

This value does not list every breakpoint whose styles apply. For example, `mobile_portrait` can be active while the element still inherits styles from the base and larger breakpoints.

### Target a breakpoint in CSS

Add a rule like this to your [custom CSS](https://academy.bricksbuilder.io/builder/features/custom-code/):

```css
body[data-brx-breakpoint="mobile_portrait"] .product-card {
  gap: 0.75rem;
}
```

This rule applies only while `mobile_portrait` is the active key. With the default desktop-first configuration, a selector for `tablet_portrait` does not also match the two mobile ranges. Use a media query when a rule should apply across several ranges.

### Read the active key in JavaScript

After Bricks initializes the page, read the current key with:

```js
const activeBreakpoint = document.body.dataset.brxBreakpoint;
```

This reads the value at that moment. Read it again when your code needs the current breakpoint.

The attribute requires JavaScript and is added during page initialization. It is absent when the setting is disabled or Bricks' JavaScript has not run. Use media queries for styles that must apply before JavaScript runs or when JavaScript is unavailable.

## Responsive control indicator {#responsive-control-indicator}

In Bricks 1.11.1, we introduced the responsive control indicator which helps you see which controls can have different values at different breakpoints. We provide multiple options for when to show this indicator to suit different preferences. You can adjust these under `Bricks > Settings > Builder > Control panel > Responsive control indicator`:

- **Show if any value exists (Default)**: Displays if a control has any value set across breakpoints.
- **Show if non-base breakpoint value exists**: Shows only if a control’s value differs from the base breakpoint.
- **Show on all responsive controls**: Displays on all responsive controls, regardless of values.
- **Disable**.

![](https://academy.bricksbuilder.io/assets/bricks-responsive-control-indicator.png)