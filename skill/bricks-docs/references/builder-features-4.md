# Interactions

Source: https://academy.bricksbuilder.io/builder/features/interactions/

*Create interactive behaviors in Bricks with triggers, actions, targets, conditions, animations, browser storage, query events, forms, popups, maps, and WooCommerce events.*

Interactions, available since Bricks 1.6, let you run an action when something happens on the front end. A simple interaction can show a hidden element on click. A more advanced interaction can listen for a query AJAX event, check browser storage, fetch an AJAX popup with the right post context, or call a custom JavaScript function.

https://youtu.be/weFimInMJPE

An interaction has three main parts:

- **Trigger**: the event Bricks listens for, such as click, content loaded, scroll, enter viewport, form success, or query AJAX end.
- **Action**: the behavior Bricks runs, such as show, hide, toggle a class, scroll to an element, open a popup, load more results, or run a JavaScript function.
- **Target**: the element affected by the action. Depending on the action, the target can be the same element, a CSS selector, or a popup template.

> **Note**
>
> Interactions run on the front end, not inside the builder canvas. Use preview or the published page to test timing, selectors, popup behavior, browser storage, and AJAX flows.

> **Note**
>
> You can define interactions on global classes instead of individual elements. Bricks merges global-class interactions into the element output, which is useful for repeated behaviors such as reusable buttons, close icons, or toggles.

## Accessing interactions {#access}

When editing an element, click the "Interactions" toggle icon in the panel header to open or close the element interactions interface.

![](https://academy.bricksbuilder.io/assets/element-interactions-toggle.png)

If an element has interactions, the same icon appears in the structure panel. Click the icon to open that element's interactions.

## Adding interactions {#add}

Click the "+" icon next to the "Interactions" title to add an interaction. You can add multiple interactions to the same element. Clicking the title of a specific interaction lets you rename it.

![](https://academy.bricksbuilder.io/assets/element-interactions-add.png)

Each interaction receives its own ID. Bricks uses this ID internally, and you can copy it when another interaction needs to listen for a specific animation-end event.

![](https://academy.bricksbuilder.io/assets/element-interactions-add-first.png)

## Triggers {#trigger}

The **Trigger** determines when the interaction runs.

### Element triggers {#element-triggers}

Element triggers listen on the source element:

- Click
- Hover
- Focus
- Blur
- Mouse enter
- Mouse leave
- Enter viewport
- Leave viewport
- [Copy successful / Copy failed](#copy-result-triggers) (since Bricks 2.5)
- [Animation end](#animation-end)
- [Query AJAX loader: Start / End](#query-ajax-loader)
- [Filter Submit: Start / End](#filter-submit-triggers)
- [Form Submit](#trigger-form-submit), [Form Success](#trigger-form-success), [Form Error](#trigger-form-error)

**Hover** listens for the browser's `mouseover` event, which fires again each time the pointer moves onto a child element. **Mouse enter** fires once when the pointer enters the element. Use Mouse enter with Mouse leave when an interaction should run once per visit, such as showing and hiding a tooltip.

Click interactions call `event.preventDefault()` by default. Since Bricks 2.0, you can enable **Disable: preventDefault** for a click interaction if the clicked element should keep its normal browser behavior, such as following a link.

### Viewport triggers {#viewport-triggers}

**Enter viewport** and **Leave viewport** watch the interaction's source element. Since Bricks 2.4, both triggers include **Element visibility**, which sets how much of that element must cross the viewport boundary:

- `0%`: Enter viewport runs when any part of the element becomes visible. Leave viewport runs when the element is no longer visible.
- `50%`: Enter viewport runs when half of the element is visible. Leave viewport runs after the element has reached that amount and its visible area drops below half.
- `100%`: Enter viewport runs when the whole element is visible. Leave viewport runs when it is no longer fully visible.

The default is `0%`. Values between `0` and `100` are supported.

An element must fit inside the active viewport area to reach `100%`. Use a lower value for elements that are taller or wider than that area.

**Enter viewport** also supports **Root margin** since Bricks 2.0. Root margin changes the active viewport boundary, while Element visibility controls how much of the source element must cross that boundary. For example, a bottom root margin of `0px 0px -50% 0px` moves the lower boundary to the middle of the viewport. Leave viewport does not use Root margin.

<div className="screenshot screenshot--control-panel">

![Enter viewport interaction with Element visibility set to 50% and the Root margin field visible.](https://academy.bricksbuilder.io/assets/bricks-interactions-element-visibility.webp)

</div>

The source element remains the element that Bricks observes. To animate or modify another element when the source crosses the boundary, choose **CSS selector** as the interaction [target](#targets) and enter that element's selector.

### Browser and window triggers {#browser-window-triggers}

Browser/window triggers are not tied to a single element event:

- Scroll
- Content loaded
- Mouse leave window

The scroll trigger accepts a scroll offset. Bricks supports pixel values, percentage values based on the document height, and `vh` values based on the viewport height. Content loaded accepts a delay such as `500ms` or `1s`.

The **Run only once** control is available for most triggers, but not for Content loaded.

### Query filter triggers {#query-filter-triggers}

When Query Filters are enabled, Bricks adds:

- Filter: Empty
- Filter: Not empty

These triggers listen for a specific filter element ID. You can enter the raw Bricks ID, `#id`, or `#brxe-id`; Bricks normalizes it before comparing.

Supported filter types are:

- Active filters
- Checkbox
- Datepicker
- Radio
- Range
- Search
- Select

For Active filters, Checkbox, Radio, and Select, Bricks checks whether options or values are available. Select excludes the placeholder option, and Checkbox/Radio exclude the "All" option. For Datepicker and Search, Bricks checks whether the current value is empty. For Range, Bricks checks whether the selected range differs from the filter's min/max values.

> **Note**
>
> Use Filter: Empty and Filter: Not empty together when you are toggling visibility. If you only hide an element on empty, you usually need the matching not-empty interaction to show it again after the next filter update.

### WooCommerce triggers {#woocommerce-triggers}

When WooCommerce is active, Bricks adds WooCommerce interaction triggers:

- Added to cart
- Adding to cart
- Removed from cart
- Bricks cart contents changed
- Cart updated
- Coupon applied
- Coupon error (since Bricks 2.5)
- Coupon removed
- Bricks dynamic fragments refreshed
- Bricks checkout step changed

The classic WooCommerce triggers listen for WooCommerce frontend jQuery events. **Bricks cart contents changed**, **Bricks dynamic fragments refreshed**, and **Bricks checkout step changed** listen for Bricks custom events and are available since Bricks 2.4.

#### Coupon error {#coupon-error}

Since Bricks 2.5, **Coupon error** runs when a coupon application fails on the cart or checkout. Use it to open a popup or run another interaction action. A successful application does not run this trigger.

To display the returned error in a popup:

First enable the [WooCommerce Notice element](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/#woocommerce-notice-element) under **Bricks > Settings > WooCommerce**. This replaces native WooCommerce notices, so follow that guide to place notices wherever your store needs them.

1. Create a [popup](https://academy.bricksbuilder.io/builder/features/popup-builder/) containing a WooCommerce Notice element and a close button. Keep AJAX loading disabled for this popup.
2. Set the popup's template conditions so it is available on the cart or checkout page.
3. On an element rendered on that page, add an interaction with **Trigger: Coupon error**, **Action: Show element**, and **Target: Popup**. Select your popup.
4. Save and test an invalid coupon on the frontend. For the Cart coupon element, enable its AJAX behavior.

<div className="screenshot screenshot--control-panel">

![Coupon error interaction configured with the Show element action, Popup target, and a selected popup.](https://academy.bricksbuilder.io/assets/woocommerce-coupon-error-interaction.webp)

</div>

The Notice element displays WooCommerce's returned message, such as an invalid or already-applied coupon. The trigger does not provide a text placeholder for inserting the error into an ordinary Text element, or separate triggers for individual failure reasons.

Leave **Run only once** disabled if the popup should open after every failed attempt. Test a second failure after closing the popup to check both the message and reopening behavior.

#### Bricks cart contents changed {#cart-contents-changed}

Use **Bricks cart contents changed** to show a custom notice or popup after a successful AJAX addition, removal, or quantity change. It covers cart, Checkout v2, mini-cart, and Cart contents loop updates handled by Bricks and WooCommerce, including loops inside Dynamic fragments.

The trigger runs after the server confirms an item change and the related cart, checkout, and fragment updates finish. A change that needs several refresh requests produces one notification. Separate confirmed changes each produce a notification, even when their refreshes are combined.

It does not run for:

- Initial page loading or synchronization of cached cart content.
- Submitting a quantity without changing its value.
- Failed requests or failed related UI refreshes.
- Coupon, shipping, address, or totals-only recalculations.

WooCommerce must be active. This trigger does not require **Enable advanced modular elements** or a Dynamic fragment on the page. It listens for supported AJAX cart updates, so a normal page reload or a custom third-party cart request is not a guaranteed trigger.

Choose the trigger that matches the behavior you need:

| Trigger | When to use it |
| --- | --- |
| **Bricks cart contents changed** | Show a confirmation after an item is added, removed, or its quantity changes successfully. |
| **Added to cart** | Respond only to an AJAX addition, such as toggling a mini-cart Offcanvas. |
| **Cart updated** | Respond to WooCommerce's `updated_cart_totals` event. This is not a general confirmation of every cart item change, particularly in checkout. |
| **Bricks dynamic fragments refreshed** | Run an action after Dynamic fragment content is replaced. This can also happen on initial synchronization or checkout recalculation without an item change. |

To show a “Cart updated” popup:

1. Create a [popup template](https://academy.bricksbuilder.io/builder/features/popup-builder/) containing your confirmation message and a close control.
2. On an element that renders on the relevant pages, open **Interactions** and add an interaction.
3. Set **Trigger** to **Bricks cart contents changed**.
4. Set **Action** to **Show element** and **Target** to **Popup**, then select your popup template.
5. Leave **Run only once** disabled if the popup should appear after each confirmed change.

Test on the frontend by adding an item, changing its quantity, and removing it. Close the popup between changes. Reload the page or change only a checkout address to confirm the popup stays closed.

## Actions {#action}

The **Action** is what Bricks runs after the trigger passes any conditions.

Available actions:

- Show element
- Hide element
- Click element
- [Set text](#set-text) (since Bricks 2.5)
- [Copy to clipboard](#copy-to-clipboard) (since Bricks 2.5)
- Set attribute
- Remove attribute
- Toggle attribute
- [Toggle offcanvas](#toggle-offcanvas)
- Load more (Query loop)
- Load more (Image Gallery)
- [Start animation](#animation-start)
- [Scroll to](#scroll-to)
- [Slider playback](#slider-playback) (since Bricks 2.5)
- [JavaScript (Function)](#javascript)
- Open address (Map)
- Close address (Map)
- Clear form
- Checkout step
- Browser storage: Add
- Browser storage: Remove
- Browser storage: Count

Show and Hide can target regular elements or popup templates. For regular elements, Bricks changes the inline `display` style. For popups, Bricks calls the popup open/close logic.

Show element removes an inline `display: none`. If the element is still hidden after that, for example by a class, Bricks sets `display: block`. A flex or grid element then loses its layout. In that case, toggle a class with **Toggle attribute** (key `class`) and set the hidden and visible states in that class instead.

Set, Remove, and Toggle attribute work on the selected target. If the attribute key is `class`, Bricks adds, removes, or toggles class names via `classList`; otherwise it sets or removes the attribute itself.

The **Click element** action calls `.click()` on each target element. This is useful when you want one UI control to trigger another existing control.

The **Clear form** action clears inputs, textareas, selects, checkboxes, radios, and visible file results. Hidden inputs are not cleared. If the interaction is triggered by Form Submit, Form Success, or Form Error, Bricks clears the matching form. Otherwise, you can provide a target form selector; if no selector is provided, Bricks clears all forms on the page.

Map actions are available since Bricks 2.0. Use **Open address (Map)** and **Close address (Map)** when working with Map/Info Box popups and address interactions. Starting with **Bricks 2.5**, these actions also support [Map (Leaflet)](https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/#info-boxes).

To load more listing items and update their map markers, target the results loop containing [Map Connectors](https://academy.bricksbuilder.io/builder/elements/general/map-connector/) with **Load more (Query loop)**, then select that loop under the map's **Sync with query** setting.

## Targets {#targets}

Most actions use one of these target modes:

- **Self**: run on the source element.
- **CSS selector**: run on every element matching the selector.
- **Popup**: run on a selected popup template.

For target fields that accept an element selector or ID, use the copy button beside the field, then right-click the target element in the canvas or Structure panel and choose the offered copy action. Selector fields copy the element's CSS ID with `#`; form and filter event fields copy its internal Bricks ID. Press Esc to leave this mode without copying.

Some actions do not use the standard target control because they have their own target field or no target at all. Examples include Load more, Browser storage, Toggle offcanvas, Map actions, and Clear form.

A CSS selector matches every element on the page that fits it. Inside a query loop, an interaction on one card with the selector `.save-button` changes the button on every card. Use **Self** when the change belongs to the element that was clicked: each loop item then keeps its own state. On the front end, elements inside a query loop don't get their automatic `#brxe-` ID unless you set a CSS ID yourself, so a copied CSS ID matches nothing there. Target loop elements by class instead.

When a popup interaction is inside a query loop, Bricks first tries to match the popup by both the selected popup template ID and the current loop item ID. If no loop-specific popup is found, it falls back to the popup template ID.

## Run only once {#run-only-once}

Enable **Run only once** when the interaction should only run one time during the current page lifecycle. For normal element events, Bricks uses a one-time event listener. For document-level events such as form, AJAX, popup, filter, or WooCommerce events, Bricks tracks and removes the interaction after it runs.

Run only once is page-local. It is not stored across page loads. Use [Browser storage actions](#browser-storage) and [interaction conditions](#conditions) if you need a persistent or session-based rule.

## Action: Slider playback {#slider-playback}

Since Bricks 2.5, **Slider playback** controls autoplay and auto scroll on a [Slider (nestable)](https://academy.bricksbuilder.io/builder/elements/media/slider-nested/). Set **Playback** to **Pause**, **Resume**, or **Toggle** (the default).

For example, to pause a row of reviews from a separate button:

1. Add a Button and set its **HTML tag** to `button`. Give it a label such as “Pause reviews”.
2. Add an interaction with **Trigger → Click** and **Action → Slider playback**.
3. Set **Playback** to **Pause**.
4. Set **Target** to **CSS selector** and copy the slider's CSS selector into the field.

<div className="screenshot screenshot--control-panel">

![A Button interaction configured to pause the review slider using its CSS selector.](https://academy.bricksbuilder.io/assets/builder/release-2.5/slider-playback-interaction.webp)

</div>

Add a second button with **Playback → Resume** if visitors need a separate way to start movement again. **Toggle** switches between paused and playing. The interaction does not update a custom button's text; the slider's [native Playback control](https://academy.bricksbuilder.io/builder/elements/media/slider-nested/#playback-control) provides changing Pause/Play labels.

Test on the frontend. Autoplay and auto scroll remain stationary in the Builder, and playback stays off for visitors who request reduced motion.

## Action: Copy to clipboard {#copy-to-clipboard}

> **Note**
>
> Copy to clipboard, Copy successful, Copy failed, and Set text are available since Bricks 2.5.

Use **Copy to clipboard** to let visitors copy a coupon code, address, link, or other text. Add an interaction to a Button or another clickable element, set **Trigger** to **Click**, and choose **Copy to clipboard** as the action.

The **Source** control has two options:

| Source | What gets copied |
| --- | --- |
| **Custom text** (default) | The content of the **Text** field, including [dynamic data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/). |
| **Element text** | The text of the first element matching **Target selector**. Leave the selector empty to copy the text of the element that owns the interaction. |

For example, enter `SAVE20` as Custom text to copy a coupon code. In a post query loop, enter `{post_url}` to copy the clicked item's URL. Dynamic copy text is resolved for each rendered query item, including when the interaction comes from a global class.

Element text is read when the action runs. It includes descendant text, but not HTML tags. It does not read an input's current value or a link's `href`; use Custom text with dynamic data to copy a URL that differs from the link label.

**Target selector** searches the whole page and uses only the first match. A shared class inside a query loop does not automatically select the clicked item's content. Use dynamic Custom text for item-specific values, or leave the selector empty when the interaction's own element contains the text to copy.

Test copying on the frontend over HTTPS and use a direct visitor click. The browser must support and allow clipboard writing. If clipboard access is unavailable or denied, or an Element text selector is invalid or matches nothing, Bricks runs **Copy failed**.

### Copy result triggers {#copy-result-triggers}

Add result interactions to the same element that owns the Copy to clipboard action:

- **Copy successful** runs after the browser confirms that the text was copied.
- **Copy failed** runs when copying fails.

Use these triggers to show a message, update text, or open a popup. A separate Click interaction that displays “Copied” can run before copying finishes, so use **Copy successful** for confirmation feedback.

Bricks does not add a notification automatically. Leave **Run only once** disabled if the feedback should update after each copy attempt.

### Example: Copy a coupon code with feedback

1. Add a Button labeled “Copy coupon” and a Basic Text element for the result message. Give the message element the CSS ID `copy-status`.
2. Keep the message element visible and add the custom attribute `role` with the value `status` so assistive technology can announce text changes.
3. On the Button, add **Click → Copy to clipboard**, select **Custom text**, and enter `SAVE20`.
4. Add another interaction to the Button: **Copy successful → Set text**. Enter `Copied: %copyText%`, choose **CSS selector** as the target, and enter `#copy-status`.
5. Add **Copy failed → Set text**, targeting the same message element, with the text “Could not copy. Select the coupon code and copy it manually.” Keep the coupon code visible on the page for this fallback.

Preview the page, click the Button, and paste into a text field to check the copied value. The result message should change only after the copy attempt finishes.

## Action: Set text {#set-text}

Since Bricks 2.5, **Set text** replaces the target element's contents with the value of its **Text** field. Use **Self** to update the interaction's own element or **CSS selector** to update matching elements.

Text is inserted as plain text. HTML markup is displayed literally, and existing child elements are removed. Target a dedicated message element rather than a container holding buttons, icons, or other content.

With **Copy successful** or **Copy failed**, `%copyText%` inserts the copied or attempted text. It becomes empty if copying failed before the source text could be read. With other triggers, `%copyText%` remains literal text.

## Action: Scroll to {#scroll-to}

Use **Scroll to** to move the page to the target element. The action supports:

- **Offset (px)**: subtracts pixels from the target position.
- **Delay (ms)**: waits before scrolling. Bricks uses a small delay by default so the DOM can update first.

![](https://academy.bricksbuilder.io/assets/bricks-interactions-scroll-to-action.png)

In this example, after the "Posts Query" AJAX call finishes, the page scrolls to the element with the CSS selector `#my-grid-wrapper`, waiting `500` milliseconds first.

## Action: Checkout step {#checkout-step}

The Checkout step action is available for [WooCommerce Checkout v2 multistep layouts](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

It can move the checkout flow to:

- Next step
- Previous step
- A specific step
- A specific checkout field

Enable **Scroll into view** when the action should scroll the target step or field into view after the step changes.

Checkout v2 also adds the **Bricks checkout step changed** trigger, which runs after the active checkout step changes. See [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) for the full setup workflow and [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#interactions) for the related WooCommerce events.

## Action: Toggle offcanvas {#toggle-offcanvas}

Since Bricks 1.11, interactions can toggle an Offcanvas element from any element. Set the action to **Toggle offcanvas** and provide the Offcanvas CSS selector, such as `#brxe-off123`.

![](https://academy.bricksbuilder.io/assets/new-toggle-offcanvas-interaction-action.png)

Do not apply this action directly to the Toggle element itself.

## Browser storage {#browser-storage}

Browser storage actions let an interaction write, remove, or count a key:

- **Window storage**: stored on `window`; resets on page load.
- **Session storage**: stored in `sessionStorage`; normally resets when the browser tab/session ends.
- **Local storage**: stored in `localStorage`; persists until cleared.

The storage actions use the same **Key** field as attribute actions:

- **Browser storage: Add** writes the configured value to the key.
- **Browser storage: Remove** removes the key.
- **Browser storage: Count** reads the key as a number, defaults to `0`, increments it by one, and stores the result.

Storage is especially useful with [interaction conditions](#conditions). For example, one interaction can count how many times a button was clicked, while another interaction only runs when that count is greater than `2`.

Interaction fields accept dynamic data, so a key can be unique per post, for example `saved-{post_id}` on a button inside a query loop.

### Example: Remember a saved state after reload {#example-remember-state}

A save button on each card of a query loop can keep its state in the visitor's browser. Write the saved look as CSS for a class such as `is-saved` (for example, a filled icon), then add four interactions to the button:

1. **Click**, **Toggle attribute**, key `class`, value `is-saved`, target **Self**. This switches the look.
2. **Click**, **Browser storage: Count**, type **Local storage**, key `saved-{post_id}`. The first click stores `1`, the second click `2`.
3. **Click**, **Browser storage: Remove**, type **Local storage**, key `saved-{post_id}`, with the condition **Local storage** `saved-{post_id}` `>=` `2`. The second click removes the key again, so the next click starts at `1`.
4. **Content loaded**, **Set attribute**, key `class`, value `is-saved`, target **Self**, with the condition **Local storage** `saved-{post_id}` **Exists**. This marks the saved buttons again after a reload.

Keep the interactions in this order. Interactions on the same trigger run one after another, and each condition is checked when its interaction runs. Two interactions that add and remove the same key on one click would undo each other.

The saved state is stored in the visitor's browser, not in a user account. It is not shared between browsers or devices.

## Action: JavaScript (Function) {#javascript}

Since Bricks 1.9.5, interactions can execute your own JavaScript functions.

> **Note**
>
> Only functions available from the global `window` scope can be executed.

Define your functions globally:

```php
<script>
window.myHelperFunctions = {}

myHelperFunctions.myCall = () => {
  console.log('myCall executed')
}

myHelperFunctions.nestedFn = {
  fn1: () => {
    console.log('fn1 executed')
  },
  fn2: () => {
    console.log('fn2 executed')
  }
}

function toggleMiniCart() {
  const run = () => {
    document.querySelector('.bricks-woo-toggle').dispatchEvent(new Event('click'))
  }

  setTimeout(run, 100)
}
</script>
```

Enter the function name in the **Function name (JavaScript)** field without parentheses and without `window.`:

- `myHelperFunctions.myCall`
- `myHelperFunctions.nestedFn.fn1`
- `myHelperFunctions.nestedFn.fn2`
- `toggleMiniCart`

You cannot execute `run()` from the example above because it is scoped inside `toggleMiniCart()`, not on `window`.

> **Note**
>
> If your target is a CSS selector that matches multiple elements, Bricks executes the function once per target.

### JavaScript function arguments {#custom-javascript-arguments}

Use the **Arguments** repeater to pass values to your function. The `%brx%` placeholder passes a Bricks object with interaction context:

- `source`: the source element that triggered the interaction.
- `targets`: the array of resolved target elements.
- `target`: the current target element for this function call.

![](https://academy.bricksbuilder.io/assets/bricks-interaction-action-javascript-function.png)

```php
function playOrPauseVideo(brxParam, postId) {
  const target = brxParam?.target || false

  if (!target) {
    return
  }

  const video = target.querySelector('video')

  if (!video || !video.play || !video.pause) {
    return
  }

  if (video.paused) {
    video.play()
  } else {
    video.pause()
  }
}
```

## Interaction conditions {#conditions}

Interaction conditions let an interaction run only when browser storage matches your rules. Conditions support:

- Window storage
- Session storage
- Local storage

Each condition checks a storage key with one of these comparisons:

- Exists
- Not exists
- `==`
- `!=`
- `>=`
- `<=`
- `>`
- `<`

For numeric comparisons, Bricks converts the stored value and comparison value to numbers. Non-numeric values become `0` for those comparisons.

The **Relation** setting controls whether all conditions must pass or whether any condition can pass:

- **And**: every condition must be true.
- **Or**: at least one condition must be true.

![](https://academy.bricksbuilder.io/assets/bricks-interaction-conditions.png)

The example above runs when `window.some_key` equals `some_value`.

## Animations {#animations}

Bricks uses [Animate.css](https://animate.style/) for interaction animations.

### Action: Start animation {#animation-start}

Set action to **Start animation** and choose an animation type, duration, and optional delay.

Since Bricks 2.5, **Animation repetitions** controls how many times the animation plays. Leave it empty for one play, or enter a positive whole number such as `3` for three plays. Enter `-1` or `infinite` for continuous playback.

A finite animation runs **Animation end** after its final repetition. An infinite animation never reaches that event. Use a finite value when another interaction depends on completion, or when an exit animation must finish before a popup closes.

![](https://academy.bricksbuilder.io/assets/bricks-interaction-start-animation.png)

When the target is a popup, Bricks applies the animation to `.brx-popup-content`. If the animation name includes `In`, Bricks opens the popup. If a popup content animation includes `Out`, Bricks closes the popup after the animation ends.

### Popup animation behavior {#popup-animation}

Popups handle open and close animations directly. To open or close a popup after an animation, set the interaction action to **Start animation** and choose an animation ending in `In` or `Out`.

You do not need a second interaction that listens for the animation-end trigger only to open or close the popup.

![](https://academy.bricksbuilder.io/assets/popup-special-consideration.png)

### Trigger: Animation end {#animation-end}

Since Bricks 1.8.4, **Animation end** can run another interaction after a Start animation action finishes.

![](https://academy.bricksbuilder.io/assets/bricks-interaction-animation-end-trigger.png)

Use **Target interaction ID** to listen for a specific Start animation interaction. If you leave it empty, Bricks looks for the previous Start animation interaction in the same interaction group.

If the target ID points to the current interaction, or to an interaction that is not a Start animation action, Bricks ignores it.

![](https://academy.bricksbuilder.io/assets/how-target-interaction-id-works.png)

In this example, interaction `uzfgcm` runs after the `xyyyeh` animation ends.

You can also listen for the same JavaScript event:

<span id="bricks-animation-end-code"></span>

```php
document.addEventListener('bricks/animation/end/xyyyeh', (event) => {
  const element = event.detail.el || false

  if (!element) {
    return
  }

  // Your logic here
})
```

## Query AJAX loader triggers {#query-ajax-loader}

Query AJAX loader triggers were introduced in Bricks 1.9. They listen to Bricks AJAX start/end events for a selected query ID.

> **Note**
>
> Bricks AJAX includes Infinite Scroll, Load More, AJAX pagination, and Query Filter requests.

Use **Query AJAX loader (Start)** to run an action before a query AJAX request starts, and **Query AJAX loader (End)** to run an action after it completes.

Use the Filter Submit triggers for AJAX submissions from a Filter - Submit element or an Enter-key search with **Trigger Filter Submit interactions** enabled.

##### Example: Apply opacity during AJAX loading

1. Create a grid layout for your query loop and add a custom class that sets opacity to `0.5`.
2. Add one interaction to apply the class when AJAX starts.
3. Add another interaction to remove the class when AJAX ends.

![](https://academy.bricksbuilder.io/assets/query-ajax-loader-trigger-01custom-css.png)

![](https://academy.bricksbuilder.io/assets/query-ajax-loader-trigger-02-interactions.png)

You can also listen to the underlying JavaScript events:

<span id="bricks-ajax-start-end-code"></span>

```php
document.addEventListener('bricks/ajax/start', (event) => {
  const queryId = event.detail.queryId || false

  if (!queryId) {
    return
  }

  // Your logic here
})
```

## Filter Submit triggers {#filter-submit-triggers}

Filter Submit triggers were introduced in Bricks 2.4. They listen to AJAX submissions from the [Filter - Submit element](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#filter-submit-reset-element) for a selected query ID. They also run when a visitor presses Enter in a [Filter - Search element](https://academy.bricksbuilder.io/builder/elements/filter/filter-search/#search-with-enter) with **Trigger Filter Submit interactions** enabled. Ordinary typing does not run these triggers.

- **Filter Submit (Start)** runs after Bricks updates the selected filter values and before the AJAX filter request starts.
- **Filter Submit (End)** runs after the AJAX filter request finishes.

Select the target query in the **Query** control. Bricks only runs the interaction when the event's `queryId` matches that selected query.

These triggers are useful when filters are placed inside an Offcanvas on mobile. Add a **Filter Submit (End)** interaction that closes the Offcanvas, and it will run after the submitted filter results have finished loading. Use **Filter Submit (Start)** if the Offcanvas should close as soon as the visitor clicks Submit.

Filter Submit triggers only run for AJAX filter submissions that refresh the current page results. They do not run when the Submit or Search element redirects to another URL.

The underlying JavaScript events are documented in [Custom JavaScript events in Bricks](https://academy.bricksbuilder.io/developer/guides/custom-javascript-events-in-bricks/#filter-submit-event-sequence).

## Form triggers {#form}

Since Bricks 1.9.2, interactions can listen to Bricks form events.

![](https://academy.bricksbuilder.io/assets/form-new-interactions.png)

<figcaption>

Triggers: Form Submit, Form Success, Form Error

</figcaption>

### Trigger: Form Submit {#trigger-form-submit}

Form Submit runs after Bricks has prepared the form data and before the AJAX form request is sent.

```php
document.addEventListener('bricks/form/submit', (event) => {
  const elementId = event.detail.elementId
  const formData = event.detail.formData

  console.log('Element ID:', elementId)
  console.log('Form Data:', formData)
})
```

### Trigger: Form Success {#trigger-form-success}

Form Success runs after a successful form AJAX response.

```php
document.addEventListener('bricks/form/success', (event) => {
  const elementId = event.detail.elementId
  const formData = event.detail.formData
  const res = event.detail.res

  // Your logic here
})
```

### Trigger: Form Error {#trigger-form-error}

Form Error runs after an error form AJAX response.

```php
document.addEventListener('bricks/form/error', (event) => {
  const elementId = event.detail.elementId
  const formData = event.detail.formData
  const res = event.detail.res

  // Your logic here
})
```

When configuring a form trigger in the Interactions panel, provide the Form ID. Bricks accepts values such as `abcde`, `#abcde`, or `#brxe-abcde` and compares them against the form element ID.

## Trigger: Filter: Empty / Not Empty {#trigger-filter-empty-or-not-empty}

Filter: Empty and Filter: Not Empty were introduced in Bricks 1.11 and are available when the Query Filters feature is active.

![](https://academy.bricksbuilder.io/assets/interaction-filter-empty-not-empty.png)

Use them to hide, show, or otherwise update UI around filter elements whose options or values become empty after the initial page load or after a query filter AJAX update.

**Filter: Empty** runs when:

- Active filters have no rendered content.
- Checkbox, Radio, or Select has no available options, excluding "All" or placeholder options.
- Datepicker or Search has an empty current value.
- Range is still at its min/max default.

**Filter: Not Empty** runs when:

- Active filters have rendered content.
- Checkbox, Radio, or Select has available options.
- Datepicker or Search has a current value.
- Range differs from its min/max default.

![](https://academy.bricksbuilder.io/assets/interaction-filter-empty-not-empty-example.png)

Example: If a Filter - Select returns no options, hide its wrapper to avoid an empty control. Add the matching Not Empty interaction to show the wrapper again when options return.

## Popup example {#example-open-modal}

To open a newsletter popup from a footer button:

1. Create a Popup template named "Newsletter popup".
2. Set the popup template conditions to the pages where the popup should be available, such as Entire website.
3. Add a button in the footer.
4. Add a Click interaction to the button.
5. Set the target to Popup, select the Newsletter popup template, and use Show element.

![](https://academy.bricksbuilder.io/assets/element-interactions-example-click.png)

Now the button opens that popup wherever the popup template is rendered.

## Example: Show custom tooltip on hover {#example-tooltip}

Create a hidden tooltip element, such as a Div with the class `.my-tooltip`, near an Icon element.

![](https://academy.bricksbuilder.io/assets/custom-tooltip-1.png)

Add two interactions to the Icon:

- Hover or Mouse enter: show `.my-tooltip`.
- Mouse leave: hide `.my-tooltip`.

![](https://academy.bricksbuilder.io/assets/element-interactions-custom-tooltip.png)

The result can look like this:

![](https://academy.bricksbuilder.io/assets/tooltip.gif)

## Example: Create a toggle button {#example-toggle-button}

You can build a custom toggle button with two Icon elements inside a Div.

![](https://academy.bricksbuilder.io/assets/open-close.gif)

Add a custom class `.toggle-button` to the wrapper Div and use CSS like this:

```php
%root% .toggle-close-icon {
  display: none;
}

%root%.is-open .toggle-open-icon {
  display: none;
}

%root%.is-open .toggle-close-icon {
  display: block;
}
```

Give the default icon the class `.toggle-open-icon`, and the active icon the class `.toggle-close-icon`.

Then add interactions:

- On the default icon, add class `is-open` to the wrapper.
- On the active icon, remove class `is-open` from the wrapper.

![](https://academy.bricksbuilder.io/assets/interaction-default-icon.png)

![](https://academy.bricksbuilder.io/assets/element-interaction-active-icon.png)

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
