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
