# Custom Code

Source: https://academy.bricksbuilder.io/builder/features/custom-code/

*Add custom CSS, JavaScript, and PHP in Bricks, understand where each code type runs, and manage it safely.*

Bricks allows you to add custom code (CSS, JavaScript, HTML, and PHP) to different parts of your website.

https://www.youtube.com/watch?v=oJNm1AFgAGU

## Where custom code can be added

Bricks has several custom-code locations. Choose the smallest location that matches what you need:

- **Global CSS and scripts**: Use this for code that should load across the entire site.
- **Page-specific CSS and scripts**: Use this for code that should load only on one page or template.
- **Element-specific CSS**: Use this for CSS tied to one element or global class.
- **Code element**: Use this when you need to place PHP/HTML, CSS, or JavaScript at a specific point in the page output.

Executable PHP and SVG code are security-sensitive. They only run when code execution is enabled, the current user has code execution capability, and the saved code has a valid code signature.

## Global CSS and JavaScript

You can add global **Custom CSS** and **Custom JavaScript** under **Bricks > Settings > Custom code**.

Global Custom CSS is added at the end of the document `<head>`.

Custom scripts can be added in three document locations:

- **Header scripts**: Added right before the closing `</head>` tag.
- **Body (header) scripts**: Added right after the opening `<body>` tag.
- **Body (footer) scripts**: Added right before the closing `</body>` tag.

Wrap JavaScript entered in the global script fields in `<script>` tags. These fields are intended for items such as analytics snippets, third-party embeds, and other site-wide scripts.

## Page-Specific CSS and JavaScript

To apply custom CSS and JavaScript to a specific page or template, edit it with Bricks and open **Settings > Page Settings > Custom Code**. Code entered there is scoped to the page or template you are editing instead of the entire site.

## Element-Specific Custom CSS {#custom-css}

![](https://academy.bricksbuilder.io/assets/bricks-1.9.1-custom-css-root-placeholder-591x1024.png)

Extend the styles of any element and global class by adding your own custom CSS to it.

First, select the element you want to style. Then open the **Style** tab and expand the **CSS** control group.

Use the `%root%` placeholder to target the element or global class you are currently editing. Bricks automatically converts `%root%` to the element ID or global class selector.

Keyboard shortcut to insert `%root%`: type `r` and press `TAB`.

Example:

```css
%root% {
  border: 1px solid red;
}
```

### CSS code completion via Emmet

You can use CSS abbreviations to write your CSS faster. Instead of writing `margin: 10px`, type `m10` and press `TAB`.

[https://docs.emmet.io/css-abbreviations/](https://docs.emmet.io/css-abbreviations/)

## Bi-directional CSS Sync

Introduced in Bricks 2.4, Bi-directional CSS Sync keeps an element's or global class's Custom CSS synchronized with the corresponding Bricks style controls.

https://www.youtube.com/watch?v=jZZA42hcS-U

Enable this experimental feature under **Bricks > Settings > Builder > CSS Sync**.

Change a supported property in the CSS editor, and its corresponding style control updates automatically. Changes made through a style control are written back to Custom CSS. Unrelated or unsupported CSS remains untouched.

CSS Sync respects the active breakpoint and pseudo-class. If the same property is defined in Custom CSS and a style control, Custom CSS takes precedence in the builder and on the frontend.

## Code Element (PHP, HTML, CSS, JS) {#code-element}

The **Code** element lets you place PHP/HTML, CSS, and JavaScript at a specific location in the page output.

By default, code entered in the Code element is displayed as a formatted code snippet. To execute PHP/HTML output instead, enable the element's **Execute code** setting.

The Code element has separate editors for:

- **PHP and HTML**: Can be rendered as a code snippet or executed when **Execute code** is enabled.
- **CSS**: Automatically wrapped in `<style>` tags when executed, unless you already include style tags.
- **JavaScript**: Automatically wrapped in `<script>` tags when executed, unless you already include script tags.

### Enable code execution

To execute Code element PHP/HTML, first enable **Code execution** under **Bricks > Settings > Custom code**.

Code execution has two layers:

- The global **Enable code execution** setting must be enabled.
- The user must have the Bricks **Execute code** capability, either through their role or an individual user-profile override.

If code execution is disabled, or if your user does not have the capability, Bricks does not show the executable controls and displays a "Code execution not allowed" notice.

![](https://academy.bricksbuilder.io/assets/bricks-builder-code-execution-1024x803.png)

<figcaption>

Code execution enabled for the Administrator role

</figcaption>

Make sure to only enable code execution for users and roles you trust.

Code execution can also be disabled by code using the `bricks/code/disable_execution` filter. Older sites may still use the deprecated `bricks/code/allow_execution` filter set to `false`; that also disables execution.

### Code signatures

Executable code only runs when code execution is enabled and the saved code has a valid code signature. Regenerate code signatures whenever your WordPress salts or secret keys change.

Code signatures apply to executable Bricks code such as Code element PHP/HTML, SVG element source code, Query editor code, component query properties, and global query records. Changing signed code invalidates the old signature until the code is signed again.

See [Code signatures](https://academy.bricksbuilder.io/builder/features/code-signatures/) for signing workflows, global regeneration, and the dangerous automatic signing constants.

### How to add PHP and HTML code to your element {#execute}

![](https://academy.bricksbuilder.io/assets/bricks-builder-code-element-execution.png)

<figcaption>

Code Element: Executing HTML and PHP code

</figcaption>

1. Add a **Code** element to the canvas.
2. Enter PHP/HTML in the **PHP and HTML** editor.
3. Enable **Execute code**.
4. Review the code.
5. Click the **Sign code** icon at the top-right of the code editor, or use `CMD/CTRL + R`.
6. Save the page.

When **Execute code** is enabled, Bricks verifies the code signature before running the PHP/HTML. If the signature is missing or invalid, Bricks renders an error placeholder instead of executing the code.

The Code element also has optional execution settings:

- **Parse dynamic data**: Parses Bricks dynamic data inside the executable PHP/HTML.
- **Suppress PHP errors**: Hides caught error diagnostics for the element. Adding `brx_code_errors=1` overrides suppression only for an authorized user; it does not grant diagnostic access. See [Inspect PHP execution errors](https://academy.bricksbuilder.io/builder/elements/general/code/#php-errors) for permissions and frontend behavior.
- **Render without wrapper**: Outputs the executed result without the Code element wrapper on the frontend.

## Security checklist

Before enabling or signing executable code:

- Grant code execution to the fewest trusted users possible.
- Prefer page-specific or element-specific CSS/JS when PHP is not needed.
- Review the code before signing it.
- Re-sign code after editing it.
- Regenerate signatures after changing WordPress salts.
- Run a Code review before global signature regeneration.

### HTML Code Completion via Emmet

You can use abbreviations to generate your HTML structures much faster via a familiar CSS-based syntax.

**Abbreviation:** `#header` (+ TAB key)

**Generates:**

```html
<div id="header"></div>
```

**Abbreviation:** `h$[title=item$]{Header $}*3`

**Generates:**

```html
<h1 title="item1">Header 1</h1>
<h2 title="item2">Header 2</h2>
<h3 title="item3">Header 3</h3>
```

[https://docs.emmet.io/cheat-sheet/](https://docs.emmet.io/cheat-sheet/)

---

# Element Conditions

Source: https://academy.bricksbuilder.io/builder/features/element-conditions/

*Use Bricks element conditions to show or hide content based on post data, user state, query results, and other runtime rules.*

Element Conditions let you define one or multiple conditions for any element. Only if those conditions are met is the element rendered on the front end.

Conditions are validated server-side and are meant to filter out/not load an element based on data (post, user, dynamic data, date & time, etc.).

Not rendering an element means **the element HTML doesn't exist in the source code**.

https://youtu.be/w8DW0VH-4pc

This is perfect for restricting content to logged-in users or users with a specific role (e.g., membership sites) to hide time-sensitive information according to a certain weekday/date/time, according to dynamic data, etc.

Element conditions are display logic. They are useful for hiding interface, marketing, membership, or product-state content, but they are not a replacement for server-side permissions around truly sensitive data, downloads, or actions. For example, hiding a download button removes the link from the page, but anyone who already has the file URL can still open the file. Protect private files and actions with your membership, file protection, or permission setup.

If you need full programmatic power to define your element conditions, use the [bricks/element/render](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-element-render/) Bricks filter.

## Accessing conditions

When editing an element, click the "Conditions" (toggle) icon in the panel header to open/close the element conditions interface. You'll see the "Conditions" toggle icon in the structure panel if an element has conditions. Click the icon to jump right into the conditions interface for this element.

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-toggle.png)

## How element conditions work

At least one set of conditions must be fulfilled to render the element. This means all conditions inside a condition "set" must be evaluated to be true.

So there is an OR relationship between condition sets and an AND relationship between conditions inside a set.

> **Note**
>
> Element conditions are evaluated when each element renders on the frontend. In the builder dynamic area, Bricks renders elements even when their conditions would fail, so you can keep editing them. Inside a query loop, conditions run with the current loop object, so they can show or hide that element per loop item. Use query settings or filters when you need to remove items from the query result set itself.

To add your first set of conditions, click the "+" icon next to the "Conditions" title:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-add-condition.png)

We now have one set with one condition. Every condition consists of the following three properties:

- **Key** (post ID, user role, date, dynamic data, etc.)
- **Comparison operand** (==, !=, >, &lt;, contains, before, after, etc.)
- **Value** (numeric, text, checkbox, select option(s), etc.)

Built-in condition groups include:

- **Post**: post ID, title, parent, status, author, date, and featured image.
- **User**: login state, user ID, registration date, and role.
- **Date & time**: weekday, date, time, and datetime. These use the WordPress site timezone.
- **WooCommerce**: product type, sale/new/stock states, stock quantity, stock management, sold individually, purchased by current user, featured status, rating, product categories, and product tags. This group is available when WooCommerce is active.
- **Other**: cookie, inner content, dynamic data, browser, operating system, current URL, and referrer URL.

The **Current URL** condition includes query parameters. Browser, operating system, and referrer checks depend on request headers, so treat them as convenience targeting rules rather than trusted security checks.

Let's say we want to show an element only to logged-in users. We'd create the following condition:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-user-is-logged-in.png)

This element is only rendered when the person viewing this page is logged in.

Non-logged-in guests, bots, crawlers, etc., will not be able to see this element (as it's not in the source code).

## Conditions indicator

Notice the highlighted "Conditions" icon in the screenshot above. It's a great indicator to see at a glance if the element you are editing has any conditions (without having to open the conditions interface).

The "Conditions" (toggle) icon is also visible next to an element in the structure panel to quickly scan for element conditions on your page. A click on it brings you right into the conditions interface.

## Checking multiple conditions

Between a set of conditions exists an **OR** relation. And conditions within a set have an **AND** relation.

Let's create a second set of conditions (by clicking the "+" icon at the top-right again) to illustrate this.

The condition in this new set is fulfilled (true) if the post title is "Account".

As there is an OR relation between condition sets, the element is rendered if (1) the user is logged in **OR** (2) the title of the post/page being viewed is "Account".

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-groups.png)

## Combining AND & OR conditions

Let's extend the conditions for this element by checking if the logged-in user has been registered before the 1st of Jan 2022.

As there is an AND relation between conditions inside a set, click the "+" button on the bottom-right of the first condition to add another condition to this first set:

![](https://academy.bricksbuilder.io/assets/bricks-render-conditions-and-or.png)

You'll also notice the vertical "**AND**" label between conditions inside a set.

And the horizontal "**OR**" label between condition sets.

This visualizes the element conditions logic.

### Repeat shared conditions in every set {#repeat-shared-conditions}

Bricks checks each set on its own. Inside a set, it stops at the first condition that fails and moves on to the next set. A condition in one set does not apply to the other sets.

If a requirement applies in every case, add it to each set. For example, a "Download recipe card" button should appear for logged-in visitors, or on recipes that are free for everyone, but only when the recipe actually has a card file:

- **Set 1**: User login **is** Logged in, AND Dynamic data `{acf_recipe_card}` **is not empty**
- **Set 2**: Dynamic data `{acf_card_access}` **==** `Everyone`, AND Dynamic data `{acf_recipe_card}` **is not empty**

Without the card check in the second set, a free recipe without a card file would still render the button.

## Show content only when a field has a value {#empty-fields}

A single post template often contains sections that only some posts can fill, such as a video, a download, or a "Chef's tip" box. Without a condition, posts that leave the field empty still render the section's heading and an empty player or box.

Add a **Dynamic data** condition to the section, pick the field, and set the comparison to **is not empty**. Leave the value empty. The section then renders only on posts where the field has content.

<div className="screenshot screenshot--control-panel">

![Conditions panel for a Section named Video with one condition: Dynamic data, {acf_recipe_video}, is not empty.](https://academy.bricksbuilder.io/assets/element-conditions-dynamic-data-is-not-empty.webp)

</div>

**is empty** and **is not empty** are available for the **Dynamic data** condition. They check whether the rendered output of the tag is an empty string, so a field that was never filled in counts as empty, the same as a field that was cleared. Use **is empty** to show fallback content in the posts that have no value.

## Comparison behavior

Except for [Cookie conditions](#cookie), `==` and `!=` comparisons use PHP-style loose comparison and convert common boolean-like values such as `true`, `false`, `1`, `0`, and empty strings before comparing. Numeric comparisons (`>`, `<`, `>=`, `<=`) compare the resolved values directly.

For multi-select values such as user roles, post statuses, WooCommerce product categories, and product tags, `is` matches if any selected value overlaps. `is not` matches when there is no overlap.

The `contains` and `does not contain` comparisons are string checks. Use them for text-like values such as post titles, dynamic data output, URLs, and referrers. Both return false when the checked value is empty, so a `does not contain` condition hides the element on posts where the field has no value. Add a separate set with **is empty** if those posts should still show the element.

If you leave the comparison empty, the condition uses `==`.

### How to compare dynamic data against the value {#dynamic-data}

> **Note**
>
> The element conditions, by default, compare against the label.

Certain dynamic data provider fields allow you to specify the value & label (e.g., [ACF true false](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/#acf), Metabox checkbox list, radio, select, etc.).

To compare against the value instead, you can use the `:value` filter like this:

![](https://academy.bricksbuilder.io/assets/bricks-1.5.7-dynamic-data-value-filter.png)

In the example above, the condition is fulfilled when the Metabox checkbox list has the `blue` value selected. Without the `:value` filter, the condition would compare against the checkbox option label.

### Hide empty component content

In Bricks 2.5, the component **Create properties from content** workflow can add connected **Dynamic data → is not empty** conditions for selected content. The check uses the resolved property value, including its default. Clearing an instance's text value therefore does not hide the element if its default still contains text. See [Hide If Empty in Components](https://academy.bricksbuilder.io/builder/features/components/#hide-if-empty) for setup and button, image, and rich-text behavior.

## Hide a wrapper when its content is empty {#inner-content}

Since Bricks 2.5, use **Inner content** to show or hide a parent based on the rendered output of a selected descendant. For example, hide a Related posts section, including its heading and background, when its query has no results.

1. Build the wrapper and add the query element inside it. Give the query a clear label in the Structure panel, such as **Related posts**.
2. Select the outer wrapper and open **Conditions**.
3. Add a condition and choose **Inner content** from **Other**.
4. Choose **is not empty** to show the wrapper when content is available, or **is empty** to show an empty state.
5. Under **Select element**, choose the descendant whose output should control the wrapper.
6. Save and check the frontend with both matching and empty query results.

<div className="screenshot screenshot--control-panel">

![The Related posts wrapper with Inner content set to is not empty and targeting its Journal card descendant.](https://academy.bricksbuilder.io/assets/builder/release-2.5/inner-content-panel.webp)

</div>

Only descendants are available, including nested children and content placed in component slots. To target an element inside a component definition, edit that component. The condition does not select unrelated elements elsewhere on the page.

### What counts as empty?

Bricks evaluates the selected element's final rendered HTML after its own conditions and render filters. No output, whitespace-only output, and a single empty wrapper such as `<div></div>` count as empty. Empty query-pagination markers and the Posts element's empty layout scaffolding are ignored.

An image, text, a no-results message, or nested HTML can make the result non-empty. This is an output check, not a visibility check: hiding content with CSS does not make its HTML empty. If a query has a no-results message, that message counts as content, so clear it when you want the outer wrapper to disappear completely.

If the selected target repeats in a query loop, **is not empty** passes when any rendered instance produces content. Other conditions in the same set still use **AND**, and separate sets still use **OR**.

### Moving, copying, and previewing

The Builder keeps the wrapper visible and editable. Check the frontend to confirm the condition's effect.

If the selected target is deleted or moved outside the wrapper, Bricks treats it as empty and the selector shows an element-not-found entry. Select another descendant to repair the condition. Duplicating or pasting a complete structure updates its target references. When pasting conditions alone, the target is retained only if it is still a descendant of the destination.

## Cookie conditions {#cookie}

Since Bricks 2.5, the **Cookie** condition can check whether a named cookie is present or compare its value. Use it to tailor content to a visitor preference already stored by your site.

1. Select the element and open **Conditions**.
2. Add a condition and choose **Cookie** in the **Other** group.
3. Enter the exact **Cookie name**, such as `audience`. Enter the name itself, without dynamic data tags.
4. Choose a comparison. For **is** or **is not**, enter the value to compare, such as `returning`.

| Comparison | The condition passes when |
| --- | --- |
| **exists** | The named cookie is present, including an empty value or `0`. |
| **does not exist** | The named cookie is absent. |
| **is** | The cookie exists and its value exactly matches the comparison value. |
| **is not** | The cookie exists and its value differs from the comparison value. |

Cookie value comparisons are case-sensitive: `returning` and `Returning` are different values. **is not** does not match a missing cookie. To include visitors without that cookie, add a separate OR condition set using **does not exist**.

For example, a welcome-back message with **Cookie**, name `audience`, comparison **is**, and value `returning` renders only when the request contains that value. The condition reads the cookie; it does not create or update it.

<div className="screenshot screenshot--control-panel">

![Cookie condition with the cookie name audience, comparison is, and value returning.](https://academy.bricksbuilder.io/assets/builder/element-conditions/cookie-condition.webp)

</div>

Bricks evaluates the cookie on the server when rendering the page. After changing a browser cookie, load the page again to evaluate the new value. As with other element conditions, the Builder keeps the element visible for editing.

If a full-page cache serves the page, configure it to vary by the relevant cookie or exclude that page from caching. Otherwise visitors can receive cached content produced for a different cookie value. Cookie conditions are for content targeting; use login and permission checks to protect restricted content.

## WooCommerce checkout and order conditions {#woocommerce}

Bricks 2.4 adds WooCommerce conditions for checkout and order-aware layouts:

- **Checkout : Login step needed**
- **Checkout : Needs shipping**
- **Checkout : Needs shipping address**
- **Checkout : Order has status**
- **Order : Needs shipping address**
- **Order : Has downloads**

Use these conditions inside WooCommerce v2 checkout, pay, thank-you, order receipt, account view-order, and other order-aware layouts when content should only appear for a matching checkout or order state.

**Checkout : Login step needed** is **Yes** only for a logged-out customer when **WooCommerce > Settings > Accounts & Privacy > Enable log-in during checkout** is enabled. The generated [Checkout v2 multistep structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/#account-login-step-visibility) uses it to keep the Account Login navigation item, step, and Customer info Back button in sync.

**Checkout : Needs shipping** checks whether the non-empty cart contains products that require shipping. Use it for shipping methods and any Checkout v2 section or step that customers need to access to choose a shipping method.

**Checkout : Needs shipping address** checks whether WooCommerce needs a separate shipping address. This can return **No** when WooCommerce is set to force shipping to the billing address, even though the cart still requires shipping and customers still need to choose a shipping method.

For a Checkout v2 layout, apply **Checkout : Needs shipping** to the Shipping options wrapper. In a multistep layout, apply the same condition to both the Shipping step and its matching navigation item. Apply **Checkout : Needs shipping address** only to the **Ship to another address** control and shipping-address fields.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#conditions) for the related WooCommerce v2 data reference.

### Order withdrawal screen

With advanced modular elements and WooCommerce Order Withdrawal enabled, use **Order withdrawal screen** inside the [Account Page v2 withdrawal state](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/#order-withdrawal). Compare with **Your details**, **Review**, or **Confirmation** using **is** or **is not**. The generated structure includes these conditions. They control frontend output; all three sections remain visible in the builder.

## Element Conditions API {#api}

The following information is intended for developers who wish to extend the default element conditions interface programmatically (`@since 1.8.4`).

The custom element condition should resemble the following example:

![](https://academy.bricksbuilder.io/assets/custom-condition-in-bricks.png)

<figcaption>

Builder: New condition group with "Post type" option

</figcaption>

### Step 1: Add condition group via filter:  bricks/conditions/groups {#bricks-conditions-groups}

```php
add_filter( 'bricks/conditions/groups', 'add_my_condition_group' );
function add_my_condition_group( $groups ) {
  // Ensure your group name is unique (best to prefix it)
  $groups[] = [
    'name'  => 'my_group',
    'label' => esc_html__( 'My Group', 'my-plugin' ),
  ];

  return $groups;
}
```

### Step 2: Add condition options via filter: bricks/conditions/options {#bricks-conditions-lists}

In this example, create a new condition to compare the current page post type with the user's value. The compare control is a dropdown with "is" and "is not" options. The value field type is a `text` input.

```php
add_filter( 'bricks/conditions/options', 'add_my_custom_condition' );
function add_my_custom_condition( $options ) {
  // Ensure key is unique, and that group exists
  $options[] = [
    'key'   => 'my_post_type',
    'label' => esc_html__( 'Post Type (New)', 'my-plugin' ),
    'group' => 'my_group',
    'compare' => [
      'type'        => 'select',
      'options'     =>  [
        '==' => esc_html__( 'is', 'my-plugin' ),
        '!=' => esc_html__( 'is not', 'my-plugin' ),
      ],
      'placeholder' => esc_html__( 'is', 'my-plugin' ),
    ],
    'value'   => [
      'type'        => 'text',
    ],
  ];

  return $options;
}
```

![](https://academy.bricksbuilder.io/assets/custom-condition-in-bricks-example01.png)

<figcaption>

Expected result: New condition in the builder

</figcaption>

### Step 3: Execute your logic to return a Boolean result via filter: bricks/conditions/result {#bricks-conditions-result}

Based on your custom logic, return `true` or `false` for your condition. Bricks take care of the `OR` and `AND` conditions.

In this example, we check if the current post type matches the user value.

If the condition is met, return `true`.

You can access the `$condition` variable, which has been set inside the builder.

```php
add_filter( 'bricks/conditions/result', 'run_my_custom_condition', 10, 3 );
function run_my_custom_condition( $result, $condition_key, $condition ) {
  // If $condition_key is not 'my_post_type', we return the $render as it is
  if ( $condition_key !== 'my_post_type' ) {
    return $result;
  }

  // Now you can perform your logic by using the $condition variable
  // $condition['compare'] is the compare operator, might be empty
  // $condition['value'] is the user value, might be empty

  // In my example, if compare is empty, we set it to '==' as default
  $compare    = isset( $condition['compare'] ) ? $condition['compare'] : '==';
  $user_value = isset( $condition['value'] ) ? $condition['value'] : '';

  $condition_met = false;

  // Get the current post type of the page
  $current_post_type = get_post_type();

  switch( $compare ) {
    case '==': // "is"
      $condition_met = $current_post_type === $user_value;
      break;
    case '!=': // "is not"
      $condition_met = $current_post_type !== $user_value;
      break;
  }

  return $condition_met;
}
```

If you have added multiple options under the same group, you can target them like this:

```php
add_filter( 'bricks/conditions/result', 'run_my_custom_condition', 10, 3 );
function run_my_custom_condition( $result, $condition_key, $condition ) {

  $condition_options = \Bricks\Conditions::$options;
  $registered_condition = null;

  foreach ( $condition_options as $option ) {
    if ( isset( $option['key'] ) && $option['key'] === $condition_key ) {
      $registered_condition = $option;
      break;
    }
  }

  if ( ! $registered_condition || $registered_condition['group'] !== 'my_group' ) {
    return $result;
  }
  // Now you can perform your logic by using the $condition variable
  // $condition['compare'] is the compare operator, might be empty
  // $condition['value'] is the user value, might be empty

  $condition_met= false;

  switch( $condition_key ) {
    case 'my_condition_option_1':
      // Example
      $condition_met = execute_my_logic_1( $condition );
      break;
    case 'my_condition_option_2':
      // Example
      $condition_met = execute_my_logic_2( $condition );
      break;
  }

  return $condition_met;
}
```

---

# Global Elements

Source: https://academy.bricksbuilder.io/builder/features/global-elements/

*Review legacy global elements in Bricks, convert them to components, and understand why new reusable work should use Components instead.*

> **Note**
>
> **Global elements are deprecated since Bricks 2.0. Use Components for new reusable builder structures, and convert existing global elements as soon as possible.**

Global elements remain visible for sites that already use them, but they are now a legacy feature. New reusable work should be created as [Components](https://academy.bricksbuilder.io/builder/features/components/), not as global elements.

## Review existing global elements

To find existing global element instances:

1. Go to `Bricks > Settings > General`.
2. Scroll to **Global elements** under the **Convert** section.
3. Start the global-elements review to retrieve a list of global element instances.

From there, review the affected pages and templates before converting, unlinking, or deleting anything.

## Convert to components

Use the converter under `Bricks > Settings > General > Convert` to convert global elements to components.

Bricks can convert global elements individually or in bulk. Nestable global elements cannot always be converted directly to components; in those cases, unlink them manually in the builder or use the converter flow that unlinks nestable global elements.

After conversion, delete the remaining global elements from the builder's elements panel.

## When to use templates instead

If you need to reuse a larger section or layout pattern without linked shared editing, save it as a template and insert it where needed. For linked reusable structures, use Components.

---

# Global Import / Export

Source: https://academy.bricksbuilder.io/builder/features/global-import-export/

*Move Bricks global builder data between sites with one ZIP package, including styles, structure, templates, settings, and related dependencies.*

Global Import / Export lets you move selected Bricks global data between sites through one ZIP package.

Use it when you want to transfer a starter design system, reuse global classes and variables across projects, move components or templates with their dependencies, or back up global builder data before major changes.

https://www.youtube.com/watch?v=YTsRaQ8-Q-Y

## Where to Open It

In the builder, open **Settings** and click **Import / Export**.

You can also open the command palette and run **Manage: Import / Export**.

## What You Can Transfer

Global Import / Export supports these data types:

| Type           | What is included                                                                 |
| -------------- | -------------------------------------------------------------------------------- |
| Theme styles   | Selected theme styles                                                            |
| Classes        | Selected global classes and class categories                                     |
| Variables      | Selected global variables and variable categories                                |
| Color palettes | Selected colors and their palette categories                                     |
| Breakpoints    | The breakpoint configuration, including default and custom breakpoints           |
| Components     | Selected components                                                              |
| Templates      | Selected templates                                                               |
| Custom fonts   | Selected custom font families                                                    |
| Icons          | Selected custom icon sets, their SVG files, and disabled state for exported sets |
| Queries        | Selected global queries and query categories                                     |
| Filters (Bricks 2.5) | Selected global filter definitions and their categories                    |
| Settings       | Supported Bricks settings tabs from the WordPress dashboard                      |

Supported settings tabs include **General**, **Templates**, **Builder**, **Performance**, **Maintenance mode**, **API keys**, **Custom code**, and **WooCommerce**.

Settings transfer is limited to supported, non-security or sensitive settings. It does not replace the full WordPress database or every Bricks option.

## Before You Export

Before creating a package, decide what the target site should receive.

For a starter site or design system, you may want to export shared color palettes, theme styles, global classes, variables, fonts, custom icon sets, breakpoints, and reusable components. For a smaller handoff, select only the specific templates, components, queries, or settings needed for that project.

Review names before exporting. Clear labels for classes, variables, templates, components, and categories make the import review easier to understand on the target site.

If the target site already has a design system, be careful with shared items such as global classes, variables, breakpoints, and theme styles. Replacing them can affect existing layouts.

![](https://academy.bricksbuilder.io/assets/bricks-global-import-export-screen.webp)

## Export a Package

1. Open **Import / Export**.
2. Make sure **Export** is selected.
3. Select one or more data types from the left sidebar.
4. Select the items you want to include.
5. Click **Export bundle**.

Bricks downloads a ZIP package. The ZIP contains a `manifest.json` file, JSON files for the selected data, and supported assets for selected custom fonts or custom icon sets.

Use the search field, categories, and select/deselect controls to narrow large lists before exporting.

## Import a Package

1. Open **Import / Export**.
2. Select **Import**.
3. Upload or drag in a Bricks transfer ZIP package.
4. Review the package contents.
5. Select the data types and items to import.
6. Review conflicts, warnings, and dependencies.
7. Click **Import bundle**.

![](https://academy.bricksbuilder.io/assets/bricks-global-import-mode.webp)

Bricks inspects the package before applying changes. The review screen shows which items are ready to import, which items conflict with existing data, and which selected conflicts will be skipped or replaced.

Nothing is imported until you click **Import bundle**. Use the review step to deselect items you do not need, check warnings, and decide how conflicts should be handled.

Bricks only imports selected items that your current user is allowed to import. If a package contains data types you cannot access, those items are not available to import.

The unified importer also accepts supported JSON exports from individual managers, such as classes, variables, global queries, global filters (Bricks 2.5), color palettes, theme styles, components, templates, settings, and icon manager data. Bricks wraps those JSON files into the same review flow so you can check conflicts before applying the import.

## Conflict Handling

When imported data matches existing data on the site, Bricks marks it as a conflict.

The default behavior is **Keep existing**. In that case, the conflicting item is skipped and the existing local item remains unchanged.

Choose **Replace** only for items you intentionally want to overwrite. You can set the conflict behavior for selected conflicts in bulk or per item.

![](https://academy.bricksbuilder.io/assets/bricks-global-import-conflict-resolution.webp)

Common conflicts include:

- A color with the same variable name.
- A theme style with the same label.
- A global class or variable with the same name.
- A custom font with the same ID or family.
- An icon set with the same name or ID.
- Breakpoints that differ from the current site configuration.
- A global query, global filter, or component with the same ID.
- A template with the same title and template type.

## Dependencies

Components and templates can depend on global classes, variables, and other components. Bricks adds those dependencies to the package manifest and marks them in the import review.

Before importing a component or template, check its dependency preview. Select the dependency classes, variables, and components that should come with it, especially when the target site does not already have the same design system.

If a dependency already exists on the target site, review the conflict before replacing it. Replacing a shared class or variable can affect existing layouts on that site.

![](https://academy.bricksbuilder.io/assets/bricks-global-import-dependencies.webp)

Dependencies can be included even when you did not select the full **Classes**, **Variables**, or **Components** type for export. This helps components and templates keep the styles and component definitions they rely on without forcing you to transfer every global class, variable, or component from the source site.

When a template uses Bricks components, Bricks includes the required component definitions in the template export. If the package does not include a separate **Components** transfer type, Bricks imports missing embedded component definitions while importing the template and keeps existing local components unchanged.

## Global Filters {#global-filters}

Starting with **Bricks 2.5**, select **Filters** to transfer [global filter definitions](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters) and their categories. Generated filter indexes stay on their own site. Check the destination's taxonomies, fields, and plugin data, then allow any required indexing to finish.

An imported definition with an existing ID is a conflict. Use **Keep existing** to skip it or **Replace** to update the saved definition. Replacing a definition's type is blocked while elements still use it.

Definitions can be transferred separately, but templates, components, and cross-site clipboard content that still reference a global filter are blocked. Unlink the filter elements on the source site and save before exporting or copying them. Import the destination definitions, select them on the imported elements, and check each element's target query.

The Filter manager also accepts JSON and ZIP files, but imports there stay unsaved until you save the builder. In the manager, same-ID definitions of the same type replace the current definitions; same-ID definitions with a different type are skipped. The unified **Import bundle** action applies the selected imports through its conflict review flow.

![Global Import / Export reviewing a Product categories filter conflict, with Keep existing and Replace choices available before importing.](https://academy.bricksbuilder.io/assets/global-filters-import-review.webp)

## Template Images

When importing templates, Bricks can import supported image assets into the Media Library.

Select **Import images** when you want template images copied into the target site. Leave it disabled when the target site should keep the image references from the package.

Template image import only applies to supported images referenced by the imported templates. It is not a full Media Library migration.

## Settings Notes

Settings are transferred by supported Bricks settings tab. This makes settings transfer useful for copying builder configuration between similar sites, but it is not a replacement for a site backup or migration tool.

Review imported settings carefully on production sites. **API keys** are hidden in the preview, and **Custom code** settings can affect the frontend or builder as soon as they are applied.

Settings and custom builder access capabilities require the WordPress `manage_options` capability.

## Permissions and Sensitive Data

Global Import / Export follows [builder permissions](https://academy.bricksbuilder.io/builder/interface/builder-access/).

Access depends on the data type:

- Color palettes require **Edit color palettes**.
- Theme styles require **Access theme styles**.
- Classes require **Access class manager**. Importing classes also requires permission to create or edit global classes.
- Variables require **Access variable manager**.
- Custom fonts require **Access font manager**. Importing custom fonts also requires permission to upload files.
- Icon manager requires **Access icon manager**. Importing custom icon sets also requires permission to upload files and upload SVGs.
- Breakpoints require **Access breakpoints manager**.
- Global queries require **Access query manager**.
- Global filters require **Access filter manager** (Bricks 2.5).
- Components require **Import/export components**.
- Templates require **Import/export templates**.
- Settings and custom capabilities require the WordPress `manage_options` capability.

Sensitive data needs extra care. Settings such as API keys and custom code are marked during review, and API key values are hidden in the preview. Code-bearing component and template data is also guarded by code execution permissions.

Only import a package from a source you trust. Review settings, custom code, templates, components, and dependencies before replacing existing data.

### Importing executable code {#executable-code}

Since Bricks 2.5, the manual **Global Import / Export** flow can import executable template, component, and global-query data when:

- Your user has the Bricks **Execute code** capability as well as the permissions for the selected data types.
- **Enable code execution** is active under **Bricks > Settings > Custom code**, and execution is not disabled by a filter.
- Code signature generation is unlocked.

The authenticated Builder import verifies the request and signs supported imported code on the destination site. This applies to code-bearing fields such as executable Code elements and PHP Query Editors; it does not make untrusted code safe. Review the selected package before importing it. See [Code signatures](https://academy.bricksbuilder.io/builder/features/code-signatures/) for signature settings and restrictions.

Page-level header and body scripts have a separate WordPress **`unfiltered_html`** requirement. Execute code permission alone does not authorize importing those scripts.

An AI or MCP import uses a separate authorization path. The connected user's Execute code capability alone does not allow PHP authoring. Supported PHP imports also require the PHP abilities opt-in and its additional safeguards, including `BRICKS_ENABLE_PHP_ABILITIES`, application-password authentication, `manage_options`, enabled code execution, and unlocked signing. See [Enable PHP abilities](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/#optional-enable-php-execution). Enabling PHP abilities is not required merely to use the manual Builder import flow.

## After Importing

Check the imported data in its manager:

- Open the [Style Manager](https://academy.bricksbuilder.io/builder/features/style-manager/) for theme styles, classes, variables, and colors.
- Open the [Font Manager](https://academy.bricksbuilder.io/builder/styling/font-manager/) for custom fonts.
- Open the [Icon Manager](https://academy.bricksbuilder.io/builder/features/icon-manager/) for custom icon sets.
- Open the breakpoint manager for breakpoints.
- Open [Query Manager](https://academy.bricksbuilder.io/builder/dynamic-content/global-queries-query-manager/) for global queries.
- Open **Browser > Filter manager** for global filters (Bricks 2.5).
- Open [Components](https://academy.bricksbuilder.io/builder/features/components/) for imported components.
- Open [Templates](https://academy.bricksbuilder.io/builder/templates/) for imported templates.
- Open **Bricks > Settings** for imported settings.

For templates and components, also check whether global classes, variables, custom fonts, custom icon sets, images, queries, and site-specific data exist on the target site. A package can move Bricks data, but it cannot create missing post types, taxonomies, API credentials, or third-party plugin data.

## Troubleshooting

### I Do Not See a Data Type or Item

The current user may not have permission to access that data type, or the source site may not have any exportable items of that type.

### An Item Was Skipped

Skipped items are usually caused by conflicts set to **Keep existing**, deselected items, or unavailable permissions. Reopen the package, review the item, and choose **Replace** only when you want to overwrite the existing local item.

### An Imported Template Looks Different

Check whether the target site has the required global classes, variables, custom fonts, images, queries, custom fields, post types, taxonomies, and plugin data. Importing the template does not automatically recreate everything the source site used outside the supported Bricks data.

### The ZIP Is Not Accepted

Use a ZIP package created by Bricks Global Import / Export. The package must contain the expected manifest and data files, and it must fit within the server upload limits for the target site.

If you are importing an older JSON export from an individual manager, upload the original JSON file in the relevant import flow. Bricks supports selected legacy manager JSON formats, but unsupported or edited JSON files are rejected.

---

# HTML & CSS to Bricks

Source: https://academy.bricksbuilder.io/builder/features/html-css-to-bricks/

*Convert existing HTML and CSS into Bricks layouts more efficiently by using the builder structure, classes, and styling tools.*

Building a layout in Bricks based on a web layout library or AI-generated layouts usually means building it from scratch, element by element. This feature changes that workflow. You can now paste HTML or CSS directly into the builder to create native elements and styles instantly.

https://www.youtube.com/watch?v=Jxib7wc_1SU

## Configuration

You can control how Bricks handles pasted code in the settings.

**Path:** `Bricks > Settings > Builder > HTML & CSS to Bricks`

- **Enabled (confirm on paste):** A dialog appears asking for permission to convert the code on paste.
- **Enabled (no confirm on paste):** Bricks converts the code automatically on paste.
- **Disabled**

## Paste requirements

HTML & CSS to Bricks reads your clipboard through the browser Clipboard API. Open the builder in a secure context, such as HTTPS or a local origin that your browser recognizes as trustworthy.

If you use LocalWP or another local domain, enable and trust its SSL certificate, then open the builder over HTTPS before testing the paste action. If pasting has no visible effect, allow clipboard access for the site in your browser settings, reload the builder, and retry with the HTML example below.

## How it works

When you paste HTML or CSS, the builder identifies the content type and initiates a conversion process.

### HTML conversion

Bricks parses the HTML and maps standard tags to native elements.

- `<section>` becomes a Section element.
- `<div>` becomes a Div.
- `<h1>` through `<h6>` become Headings.
- `<img>` becomes an Image.

### Global classes & variables

The converter identifies classes in your code and creates corresponding Bricks global classes and global variables.

- **Mapped styles:** Properties like margin, padding, and typography are applied directly to the Bricks UI controls.
- **Custom CSS:** Properties that do not have a dedicated UI control are added to the element's Custom CSS area.
- **Variables:** Any variables defined in `:root` are converted into Bricks Global Variables.

### Responsive class styles

When a class uses a simple `@media (max-width: ...)` rule that exactly matches a configured Bricks breakpoint, supported declarations can become native controls at that breakpoint. For example, a `.card` padding rule at the site's mobile breakpoint can appear under that breakpoint's padding controls. Declarations without a matching control remain in Custom CSS. Compound or nested media conditions, unmatched widths, and rules whose source order cannot be represented by Bricks breakpoint order stay in Custom CSS rather than being applied at the wrong breakpoint.

## Example: HTML with a global class

Copy both the HTML and CSS, then paste them into the builder:

```html
<section class="feature">
  <h2>Built for client work</h2>
  <p>Start with a native Bricks structure, then refine it in the builder.</p>
</section>

<style>
  :root {
    --feature-space: 2rem;
  }

  .feature {
    padding: var(--feature-space);
    background-color: #f4f4f4;
  }
</style>
```

Bricks creates native Section, Heading, and text elements. It also creates the `feature` global class and the `--feature-space` global variable. Supported declarations are mapped to builder controls; remaining declarations stay in custom CSS.

## Example: CSS-only paste

Paste CSS by itself when the structure already exists and you only need classes or variables:

```css
:root {
  --card-radius: 12px;
}

.card {
  border-radius: var(--card-radius);
  padding: 1.5rem;
}
```

Bricks creates the variable and global class. Apply the new `card` class to an element from the builder.

## Security

Bricks will not execute JavaScript or load external stylesheets automatically upon pasting until reviewed.

Any detected scripts or external links are placed inside a **Code** element. You must manually review, sign, and save these elements before they are executed.

For example, pasting `<script>console.log('Ready')</script>` creates a Code element. The script remains inactive until a user with permission reviews and signs it.

### Imports through AI abilities

When an AI client imports HTML or CSS through Bricks abilities, Bricks checks the target and the connected user's permissions. Disallowed content is omitted automatically. A one-call import can apply the retained content and returns a prominent partial result with every omitted element and the reason it was omitted. An explicit preview is also available.

If the retained tree is empty or invalid, the import is rejected. A nonempty replacement is also rejected when source content was omitted or invalid, because it could remove existing content incompletely.

HTML and CSS imports do not grant PHP access. Without `unfiltered_html`, HTML is limited to WordPress safe post HTML (KSES). CSS follows the relevant style and resource permissions. JavaScript requires WordPress `unfiltered_html` and permission to edit the target. Code elements keep their existing **Execute code** permission, global code execution setting, and signing requirements. The abilities do not bypass those requirements. PHP in supported Code fields requires the separate PHP abilities opt-in and its signing safeguards. See [AI Abilities and Skills](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/#optional-enable-php-execution).

## Notes

- **Refinement:** The conversion provides a structural foundation. Because your site has existing theme styles and theme or plugin CSS, the output may require further manual adjustments to match the source perfectly.
- **Permissions:** You must have the [user permission](https://academy.bricksbuilder.io/builder/interface/builder-access/#custom) to "Create global classes" for the converter to generate styles correctly.
- **CSS-only paste:** If you paste only CSS, Bricks will generate the global classes and variables.
- **Missing class styles:** Confirm that your role can create global classes. Without that permission, the converter cannot create the class records used by the imported CSS.

---

# Icon Manager

Source: https://academy.bricksbuilder.io/builder/features/icon-manager/

*Manage icon sets in Bricks, add custom packs, and control which icons are available inside the builder.*

Bricks 2.0 introduces the **Icon Manager**, a new feature for uploading and managing your own custom SVG icon sets directly inside the builder. The Icon Manager makes it easy to create and maintain a consistent icon system across your site.

![](https://academy.bricksbuilder.io/assets/bricks-icon-manager.png)

## Accessing the Icon Manager

To open the Icon Manager, go to **Settings > Icon Manager** in the builder toolbar, or click the **gear icon** within any icon control.

This opens a popup where you can manage both built-in and custom icon sets.

Access to the Icon Manager depends on the `Access icon manager` builder permission. Uploading SVG icons also requires SVG upload capability, and uploaded SVG files are sanitized. If an SVG cannot be sanitized, WordPress will reject the upload.

## Core functionalities

### Upload and manage custom icon sets

You can create your own icon sets by uploading a collection of SVG files. Each icon set is organized by name and can include as many icons as needed.

- **Create a new icon set** by entering a new name in the "Create icon set" field and click save
- **Upload SVG files** individually or in bulk from the WordPress media library
- Each icon in the set becomes available in all icon controls

#### Enable or disable icon sets

To keep your icon selection streamlined, you can disable any icon set, including built-in ones (i.e. FontAwesome). Disabled sets won't appear in the icon picker, but any icons already used on the page will still display and render as expected.

---

# Features

Source: https://academy.bricksbuilder.io/builder/features/

*Explore Bricks features such as components, interactions, popups, templates, custom code, search criteria, and workflow tools.*

Bricks features extend the core page-building workflow with reusable systems, interaction tooling, template workflows, and advanced frontend and content capabilities.

## Featured areas

- [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) and [Site Versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) for pending changes, [Review Links](https://academy.bricksbuilder.io/builder/interface/review-links/), and [Explore and Compare](https://academy.bricksbuilder.io/builder/interface/explore-alternatives/)

- [Lazy Loading](https://academy.bricksbuilder.io/builder/features/lazy-loading/) for background, image, page, and site-level loading controls
- [Templates](https://academy.bricksbuilder.io/builder/templates/) for the main template workflow and related reference pages
- [Global Data Revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) for recovering recorded shared-item changes

- [Components](https://academy.bricksbuilder.io/builder/features/components/) for reusable structures and nested component workflows
- [Interactions](https://academy.bricksbuilder.io/builder/features/interactions/) for triggers, animations, and action-based behaviors
- [Popup Builder](https://academy.bricksbuilder.io/builder/features/popup-builder/) for modal, slide-in, and notification-bar patterns
- [Custom Code](https://academy.bricksbuilder.io/builder/features/custom-code/) for adding and organizing custom code in Bricks
- [Search Criteria](https://academy.bricksbuilder.io/builder/features/search-criteria/) for frontend search configuration
- [Menu Builder](https://academy.bricksbuilder.io/builder/features/menu-builder/) for custom desktop and mobile navigation
- [Maintenance Mode](https://academy.bricksbuilder.io/builder/features/maintenance-mode/) for maintenance and coming-soon screens
- [Password Protection](https://academy.bricksbuilder.io/builder/features/password-protection/) for gated frontend content
- [Nestable Slider](https://academy.bricksbuilder.io/builder/features/nestable-slider-instance/) for per-instance slider customization

---

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
