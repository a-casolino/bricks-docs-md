*The Offcanvas element is a nestable panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding.*

The **Offcanvas** element is a **nestable** panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding a [Toggle](https://academy.bricksbuilder.io/builder/elements/general/toggle/) elsewhere on the page that targets this Offcanvas (see the in-element info link to the menu builder article).

The default structure includes an inner **Block** (`.brx-offcanvas-inner`) for your content—often with starter **Text** and a **Toggle** labeled for closing—and a second **Block** acting as the **Backdrop** (`.brx-offcanvas-backdrop`), which you can remove if you do not want a backdrop.

https://youtu.be/Lhyh52twZoE

## Settings

- **Direction** (select) — `top`, `right`, `bottom`, or `left`. Default: left.

- **Effect** (select) — `slide` or `offset`.

- **Close on** (select) — `backdrop` (click), `esc`, `none`, or default: backdrop and ESC.

- **Width**, **Height** (number with units) — Size of the inner panel (`.brx-offcanvas-inner`).

- **Transition: Duration** (number with units) — Open/close animation; set to `0s` to disable.

- **Transition: Timing function** (text) — Easing, e.g. `cubic-bezier(0.25, 0, 0.25, 1)`.

- **aria-label** (text) — Root dialog label; defaults to “Offcanvas”.

- **Keep open while styling** (checkbox) — Builder helper class `brx-open` to keep the panel open while designing.

- **No scroll (body)** (checkbox) — Prevents body scrolling while open.

- **Scroll to top** (checkbox) — Scrolls to top when the Offcanvas opens.

- **Disable auto focus** (checkbox) — Skips auto-focusing the first focusable element when opening.

- **Open on page load** (checkbox) — Opens on the front end when the page loads (not applied in the builder).

## Build a mobile menu

This example replaces the menu element's built-in mobile menu with an Offcanvas, so the phone menu can have its own design and extra content such as contact details.

1. Open the header template, select the header section, and add an **Offcanvas**. It is hidden on the canvas until you select it.
2. Turn on **Keep open while styling**. Without it, the panel closes as soon as you select an element inside it.
3. Set **Direction**, **Width**, and **No scroll (body)** to suit the design, for example `Right` and `86%`.
4. Replace the starter Basic Text with your menu, for example a [Nav Menu](https://academy.bricksbuilder.io/builder/elements/wordpress/nav-menu/) element that uses the same WordPress menu as the desktop header. Set its **Show at breakpoint** to `Never`, so it always shows the links instead of its own menu button.
5. Add a **Toggle** to the header. Select the Offcanvas, hover the **b** icon at the top of the panel, and click **#** (Copy: CSS ID). Paste the ID into the Toggle's **CSS selector**.
6. On the Toggle's **Style** tab, set **Display** (Layout group) to `none` on desktop. Switch to the breakpoint where the menu should change, for example Tablet portrait, set the Toggle's Display to `flex`, and set the desktop menu's Display to `none`. Smaller breakpoints inherit both settings.
7. Save. Keep open while styling is a Builder helper: it is not saved and does not affect the frontend.

![Builder with the header template open: the Offcanvas is selected with Direction Right, Width 86%, and No scroll (body) on. The Structure panel shows the Offcanvas with Content (Toggle (Close), Nav Menu, Contact) and Backdrop.](https://academy.bricksbuilder.io/assets/offcanvas-builder-mobile-menu.webp)

<div className="screenshot screenshot--control-panel">

![Toggle settings with the Offcanvas CSS ID pasted into CSS selector. Attribute and Value keep their defaults, class and brx-open.](https://academy.bricksbuilder.io/assets/offcanvas-toggle-css-selector.webp)

</div>

> **Note**
>
> Without a CSS selector, a Toggle opens the first Offcanvas on the page. This includes the Toggles inside a [Nav (Nestable)](https://academy.bricksbuilder.io/builder/elements/general/nav-nested/) when the page also has an Offcanvas, for example one in the header template. Give each Toggle a CSS selector when a page has more than one element to toggle.

## Opening, closing, and keyboard focus

A Toggle opens the Offcanvas by adding the class `brx-open` to it. While the Offcanvas is open:

- Focus moves to the first focusable element inside it. Turn on **Disable auto focus** to skip this. If the close Toggle is the first element in Content, focus lands on it.
- **Tab** and **Shift+Tab** stay inside the panel: from the last focusable element, Tab wraps back to the first.
- With **No scroll (body)** on, the page behind the panel does not scroll.
- The Toggle that opened it has `aria-expanded="true"`.

The Offcanvas closes on a click on the backdrop, on **Esc**, or with a Toggle inside it. **Close on** limits this to the backdrop or Esc, or turns both off. When it closes, focus returns to the Toggle that opened it. While closed, the panel is hidden, so its links cannot be reached with Tab.

> **Developer reference**
>
> See the [Offcanvas Schema](https://academy.bricksbuilder.io/developer/schema/elements/offcanvas/) for the full JSON schema of this element's settings and controls.