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

---

# Icon list

Source: https://academy.bricksbuilder.io/builder/elements/general/icon-list/

*The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links.*

The Icon List element creates a list of social media icons or custom icons with customizable styling, labels, and links.

## Settings

- **Icons** (repeater) - Add and configure icons. Each icon has:
  - **Icon** (icon) - Icon selection. Default: `ion-logo-twitter`.
  - **Icon: Color** (color) - Individual icon color.
  - **Icon: Size** (number with units) - Individual icon size.
  - **Label** (text) - Text label for the icon.
  - **Label: Size** (number with units) - Label text size.
  - **Color** (color) - Text color for the icon/label combination.
  - **Background** (color) - Background color for the icon item.
  - **Link** (link) - Link destination for the icon.

- **Icon: Color** (color) - Global icon color for all icons.

- **Icon: Size** (number with units) - Global icon size for all icons.

### Alignment

- **Direction** (direction) - Layout direction. Options: `row`, `column`.

- **Align items** (align-items) - Vertical alignment of icons. Options: `flex-start`, `center`, `flex-end`, `baseline`.

- **Justify content** (justify-content) - Horizontal alignment of icons. Options: `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly`.

- **Spacing (Items)** (number with units) - Spacing between icon items. Default: 0.

- **Spacing (Item)** (number with units) - Internal spacing within each icon item. Default: 5px.

> **Developer reference**
>
> See the [Icon List Schema](https://academy.bricksbuilder.io/developer/schema/elements/social-icons/) for the full JSON schema of this element's settings and controls.

---

# Map Connector

Source: https://academy.bricksbuilder.io/builder/elements/general/map-connector/

*The Map Connector works with the Google Map element when Sync with query is enabled. Place one Map Connector inside each item of the query loop that should.*

The **Map Connector** works with the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element when **Sync with query** is enabled. Place **one Map Connector inside each item** of the query loop that should produce a marker.

It renders an invisible **`<template>`** node that stores latitude, longitude, and/or address plus optional **Info Box** popup template data and **per-item marker overrides**. The Map reads these nodes to build markers when the query updates (pagination, filters, load more, etc.).

See [Map → Sync with query](https://academy.bricksbuilder.io/builder/elements/general/map/#sync-with-query) for the full workflow.

## Settings

- **Latitude** (text) — Use dynamic data from the looped post (placeholder shows Berlin-area example).

- **Longitude** (text).

- **Address** (text) — Alternative to coordinates; may geocode via Google when coordinates are not set.

An **error** info appears when all three are empty—Bricks expects at least one source of location via dynamic tags.

### Info Box (Popup)

- **Info Box: Template (Popup)** (select) — Popup template with **Template Settings → Popup → Info Box (Map)** enabled.

- **Info** — Reminds you to enable the Info Box option on the popup template.

### Markers

An **info** control notes that **Marker: Type** (text vs image) is configured on the **Map** element, while fields here **override** that map’s defaults for **this** loop item.

On the connector, Bricks only exposes marker fields that are **not** flagged `mainOnly` in the shared map-marker control set—so you set **per-loop values**, not the global marker typography or image dimensions (those stay on the **Map** element):

- **Label** (text) — Screen reader label (`aria-label`) for the marker.

- **Marker: Text** — **Text** field for the default text marker.

- **Marker: Text (Active)** — **Text** field for the active text marker.

- **Marker: Image** — **Icon** (image) for the default image marker.

- **Marker: Image (Active)** — **Icon** (image) for the active image marker.

> **Developer reference**
>
> See the [Map Connector Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-connector/) for the full JSON schema of this element's settings and controls.

---

# Map (Leaflet)

Source: https://academy.bricksbuilder.io/builder/elements/general/map-leaflet/

*Map (Leaflet) (map-leaflet) embeds an interactive map using Leaflet and tile layers (default: OpenStreetMap). Unlike the Google Map element, it does not use the.*

**Map (Leaflet)** (`map-leaflet`) embeds an interactive map using **Leaflet** and **tile layers** (default: **OpenStreetMap**). Unlike the Google [Map](https://academy.bricksbuilder.io/builder/elements/general/map/) element, it does **not** use the Google Maps JavaScript API—use this when you want OSM-style tiles or custom tile URLs without Google.

The element is **not draggable** in the builder (`draggable = false`) to avoid conflicts with map interaction. It enqueues `bricks-leaflet` scripts and styles.

## Layers

**Layers** (repeater) — Each layer:

- **Name** (text) — e.g. `OpenStreetMap`.
- **URL** (text) — Tile URL template with `{z}`, `{x}`, `{y}` placeholders.
- **Min Zoom**, **Max Zoom** (number).
- **Error Tile URL** (text).
- **Attribution** (text).

Default repeater row uses OpenStreetMap’s standard tile URL.

## Markers

**Markers** (repeater):

- **Coordinates** (text) — `latitude, longitude` (comma-separated). Supports dynamic data.
- **Label** (text) — Builder-only helper to tell markers apart.
- **Icon** (image) — Per-marker image; **Height** / **Width** (px) when set.
- **Popup (Text)** (editor) — Popup content for that marker.

### Marker (Default)

Global defaults when a marker has no custom icon:

- **Icon** (image), **Icon: Height (px)**, **Icon: Width (px)**.

## Map

- **Height** (number with units) — Map container height. Default placeholder: `300px`. Triggers reload when changed.

- **Map center** (text) — `latitude, longitude`.

- **Zoom level (Initial)** (number).

- **Zoom level (Min)**, **Zoom level (Max)** (number).

- **Zoom: Snap**, **Zoom: Delta** (number).

- **Zoom: Double-click** (select) — Enabled, Enabled (Center), or Disabled.

- **Zoom: Scroll wheel** (select) — Same options.

- **Box Zoom** (checkbox).

- **Zoom Control** (checkbox).

- **Attribution Control** (checkbox).

- **Close popup on click** (checkbox).

- **Dragging** (checkbox).

- **Track resize** (checkbox) — See [Leaflet map options](https://leafletjs.com/reference.html#map).

> **Developer reference**
>
> See the [Map (Leaflet) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map-leaflet/) for the full JSON schema of this element's settings and controls.

---

# Map

Source: https://academy.bricksbuilder.io/builder/elements/general/map/

*The Map element in Bricks allows you to display Google Maps with a range of capabilities, from showing a single location to dynamically rendering multiple.*

The **Map** element in Bricks allows you to display Google Maps with a range of capabilities, from showing a single location to dynamically rendering multiple markers based on queries.

You can get started quickly by adding a Google Maps API key. Follow this guide to set it up: [How to set up your Google Maps API key](https://academy.bricksbuilder.io/integrations/how-to-set-up-your-google-maps-api-key/).

Without an API key, the Map element is still functional but limited to displaying **a single marker** only.

![](https://academy.bricksbuilder.io/assets/map-without-google-maps-api.png)

To ensure a marker is shown, simply enter a pair of coordinates (latitude and longitude, separated by a comma) in the **Address** field.

## Choose how the map renders

With an API key saved, **Render mode** lets you choose **Google Maps JavaScript API** (the default) or **Iframe embed**. Use Iframe embed when the map only needs a single address and you do not need API-only features such as multiple markers, clustering, query syncing, or custom Info Boxes. The iframe mode does not load the Google Maps JavaScript API for that map. Set its **Loading** option to `lazy` (the default) or `eager`.

Without an API key, the map uses the single-address iframe mode automatically. The Render mode selector appears only when an API key is saved.

## Displaying multiple addresses

To unlock advanced features such as multiple locations, clustering, and custom Info Boxes, save a valid **Google Maps API key** and use the **Google Maps JavaScript API** render mode. You will then see more controls on the element.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-addresses.png)

Bricks supports three address input modes:

### 1) Static

Manually define multiple locations using the "Addresses" **Repeater** control of the Map element. This mode supports only the default Google Maps Info Box.

### 2) Query loop

Use this mode when map addresses to feed the map with addresses/coordinates from a query.

For example, if you have a **custom post type** like "Properties" where each property contains an address, enabling the Query loop allows you to show markers of all property addresses on the map. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-query-loop.png)

You can also define a [custom Info Box](#info-box-popup-template) using a popup template.

In our example above, we selected the custom post type `property`, where each address is stored in a custom field (ACF). Providing the latitude & longitude coordinates will be more accurate than a physical address.

### 3) Sync with query

Ideal for use cases where the map is shown alongside a dynamic query loop such as a directory, Sync with query allows the map to update live with the query as users interact via **AJAX Pagination**, **Load More**, or **Query Filters**.

This mode requires adding a [Map Connector](#map-connector-element) element inside the target query loop.

It also supports [custom Info Boxes](#info-box-popup-template) using popup templates.

**Example setup:** You want to display a query loop on the same page as your map and connect the two. If this query loop uses **AJAX Pagination**, **Query Filters**, or **Load More**, enabling Sync with query allows the map markers to update dynamically in real-time as users interact with those features.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query.png)

**Map markers update according to query results**:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-map-sync-with-query-filters.png)

## Markers

![](https://academy.bricksbuilder.io/assets/markers-control.png)

### Cluster markers

Enable this option to automatically group nearby markers into a cluster. `(@since 2.0)`

![](https://academy.bricksbuilder.io/assets/cluster-markers.png)

## General Settings

### Map ID

![](https://academy.bricksbuilder.io/assets/map_id-control.png)

Enter your **Google Maps ID** (available in your Google Cloud Console) to enable the latest Maps features `(@since 2.0)`  
When set:

- Bricks uses Google's modern `AdvancedMarker` API.
- Map styles are managed via your Google Console (style settings in Bricks are disabled).
- Deprecated browser console warnings are avoided.

### Map Center

![](https://academy.bricksbuilder.io/assets/map-center-control.png)

Set the default center point of the map. Particularly useful when using **Sync with query**—if the synced query returns no results, the map will reset to this center point. `(@since 2.0)`

### Others

![](https://academy.bricksbuilder.io/assets/general-settings.png)

## Map Connector (element)

**The Map Connector element `(@since 2.0)` is required when using Sync with query.**

Place it inside the target query loop that you want to sync with your map. It generates an invisible `<template>` node containing location data, which is then read by the map to dynamically render the markers.

**Note:** It's strongly recommended to provide **latitude and longitude** values whenever available. If you rely solely on addresses and require geocoding every time markers are rendered, you may incur charges from the Google Maps Platform Geocoding API.

![](https://academy.bricksbuilder.io/assets/map-connector.png)

You can also define the Info Box (popup template) that should show when a marker is clicked. Make sure the selected popup template has the **"Info Box (Map)"** option enabled in its settings.

## Info Box (Popup template)

Introduced in version 2.0, the **Info Box (Map)** option is available in Popup template settings.

![](https://academy.bricksbuilder.io/assets/infobox-popup.png)

- Once enabled, the popup will display with a default width of 300px in the builder and remove the backdrop for preview.
- You can customize the design of the Info Box in the builder.
- Supports **Fetch content via AJAX**.
- Supports **AJAX loader** animation when loading dynamically.
- It is recommended to set **Populate Content** to the post or term being looped so dynamic data displays correctly in the builder.

![](https://academy.bricksbuilder.io/assets/infobox-popup-preview.png)

## Map Interactions

Two new map interaction actions are introduced in Bricks 2.0:

- Open address (Map)
- Close address (Map)

![](https://academy.bricksbuilder.io/assets/interaction.png)

Use cases:

- Use a button or element inside the query loop to **open** the Info Box for the corresponding marker.
- Add a close icon inside the Info Box popup to allow users to manually **close** it.

These interactions provide greater control and flexibility over how Info Boxes behave in dynamic mapping scenarios.

When an Info Box opens, Bricks adds the `infobox-opened` class to the interaction elements associated with that marker. The class is removed when the Info Box closes. You can use this class to style the open state or a parent element that contains the interaction element:

```css
.looping-div:has(.infobox-opened) {
  background-color: blue;
}
```

## Resolving Google Maps Script Conflicts with Other Plugins

If you're using a plugin like Fluent Form, which may enqueue the Google Maps script on the same page, this can result in a JavaScript conflict because the script cannot be loaded twice.

To prevent this issue, you can dequeue Bricks' Google Maps script and trigger the `bricksMap()` function manually after a short delay, ensuring the Fluent Forms map script has loaded first:

```php
add_action( 'wp_enqueue_scripts', function() {
  if ( is_page( 1567 ) ) {
    wp_deregister_script( 'bricks-google-maps' );
  }
}, 999 );

add_action( 'wp_footer', function() {
  if ( is_page( 1567 ) ) {
    echo '<script>
      document.addEventListener("DOMContentLoaded", function() {
        setTimeout(function() {
          bricksMap();
        }, 1000); // Adjust delay if needed
      });
    </script>';
  }
}, 999 );
```

Replace `1567` with your actual page ID. Adjust the delay as necessary to ensure the Fluent Forms map script has fully loaded before `bricksMap()` runs.

## Settings

### Addresses

- **Addresses** (repeater) - Add map locations. Each address has:
  - **Latitude** (text) - Latitude coordinate. Placeholder: `52.5164154966524`.
  - **Longitude** (text) - Longitude coordinate. Placeholder: `13.377643715349544`.
  - **Address** (text) - Address for geocoding (alternative to coordinates). Placeholder: `Berlin, Germany`.
  - **Info Box template** (select) - Template for infobox popup.
  - **Title** (text) - Infobox title.
  - **Subtitle** (text) - Infobox subtitle.
  - **Content** (textarea) - Infobox content.
  - **Images** (image-gallery) - Images for infobox.
  - **Width** (number) - Infobox width. Placeholder: `300`.
  - **Label** (text) - Screen reader label for accessibility.
  - **Marker: Text** (text) - Text marker content. Placeholder: `Marker`.
  - **Marker: Text (Active)** (text) - Active text marker content. Placeholder: `Marker`.
  - **Marker: Image** (image) - Image marker.
  - **Marker: Image (Active)** (image) - Active image marker.

### Query loop

- **Has loop** (checkbox) - Enable query loop for dynamic addresses.
- **Query** (query) - Configure which posts to display.
- **Info Box: Template** (select) - Template for infobox popup in query loop.

### Sync with query

- **Sync with query** (query-list) - Connect to existing query loop for dynamic markers.
- **Text: No results** (text) - Message when no locations found. Placeholder: `No locations found`.

### Markers

- **Cluster: Markers** (checkbox) - Enable marker clustering.
- **Cluster: Background color** (color) - Cluster background color.
- **Cluster: Text color** (color) - Cluster text color.

- **Marker** (separator) - Global marker settings.
- **Type** (select) - Marker type. Options: `image`, `text`. Default: `image`.

#### Marker: Text

- **Max. width** (number with units) - Maximum text marker width.
- **Typography** (typography) - Text marker font settings.
- **Background color** (color) - Text marker background.
- **Border** (border) - Text marker border styling.
- **Box shadow** (box-shadow) - Text marker shadow.
- **Padding** (spacing) - Text marker padding.

#### Marker: Text (Active)

- **Typography** (typography) - Active text marker font settings.
- **Background color** (color) - Active text marker background.
- **Border** (border) - Active text marker border styling.
- **Box shadow** (box-shadow) - Active text marker shadow.
- **Padding** (spacing) - Active text marker padding.

#### Marker: Image

- **Marker** (image) - Default marker image.
- **Height** (number) - Marker height in pixels. Placeholder: `40`.
- **Width** (number) - Marker width in pixels. Placeholder: `40`.
- **Border** (border) - Marker border styling.
- **Box shadow** (box-shadow) - Marker shadow.

#### Marker: Image (Active)

- **Marker (Active)** (image) - Active marker image.
- **Height** (number) - Active marker height in pixels. Placeholder: `40`.
- **Width** (number) - Active marker width in pixels. Placeholder: `40`.
- **Border** (border) - Active marker border styling.
- **Box shadow** (box-shadow) - Active marker shadow.

### Map

- **Map ID** (text) - Google Maps ID from Cloud Console for advanced features.
- **Render mode** (select) - With an API key saved, choose Google Maps JavaScript API or Iframe embed. Default: Google Maps JavaScript API.
- **Loading** (select) - For iframe rendering, choose `lazy` or `eager`. Default: `lazy`.

#### Map center

- **Latitude (Center)** (text) - Map center latitude. Placeholder: `52.5164154966524`.
- **Longitude (Center)** (text) - Map center longitude. Placeholder: `13.377643715349544`.
- **Address (Center)** (text) - Map center address. Placeholder: `Berlin, Germany`.

#### General settings

- **Height** (number with units) - Map container height. Placeholder: `300px`.
- **Zoom level** (number) - Initial map zoom level. Range: 0-20. Placeholder: `12`.
- **Map type** (select) - Map style. Options: `roadmap`, `satellite`, `hybrid`, `terrain`. Default: `roadmap`.
- **Map style** (select) - Predefined map styles. Requires roadmap type.
- **Custom map style** (code) - JSON code for custom styling from Snazzy Maps.
- **Apply: Custom map style** (apply) - Apply custom style changes.
- **Fit map on markers change** (checkbox) - Auto-adjust view when markers change.
- **Scroll** (checkbox) - Enable scroll wheel zooming. Default: true.
- **Draggable** (checkbox) - Enable map dragging. Default: true.
- **Fullscreen Control** (checkbox) - Show fullscreen button.
- **Map Type Control** (checkbox) - Show map type selector.
- **Street View Control** (checkbox) - Show street view button. Default: true.
- **Disable Default UI** (checkbox) - Hide all default controls.
- **Disable clickable POI** (checkbox) - Disable clicking on points of interest.
- **Zoom Control** (checkbox) - Show zoom controls. Default: true.
- **Zoom level (Min)** (number) - Minimum zoom level.
- **Zoom level (Max)** (number) - Maximum zoom level.

### No API Key Mode

When no Google Maps API key is configured, the element falls back to Google Maps Embed API with limited functionality:

- **Address** (text) - Single address for embedded map. Placeholder: `Berlin, Germany`.
- **Loading** (select) - Loading behavior. Options: `eager`, `lazy`. Default: `lazy`.

> **Developer reference**
>
> See the [Map (Google) Schema](https://academy.bricksbuilder.io/developer/schema/elements/map/) for the full JSON schema of this element's settings and controls.

---

# Nav (Nestable)

Source: https://academy.bricksbuilder.io/builder/elements/general/nav-nested/

*The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports.*

The Nav (Nestable) element creates hierarchical navigation menus with dropdown functionality, multilevel support, and mobile-responsive behavior. It supports nested menu structures and can be used to build complex navigation systems.

## Settings

### HTML Tag & Accessibility

- **HTML tag** (text) - HTML tag for the navigation element. Supports dynamic data. Default placeholder: `nav`. Validates HTML tag format.

- **aria-label** (text) - Accessibility label for the navigation. Supports dynamic data. Default placeholder: "Menu".

### Top Level (Item)

- **Gap** (number with units) - Gap between top-level navigation items. Controls `gap` property for `.brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of top-level items. Deprecated since version 1.10. Description suggests using "Align items" under "Mobile menu" instead. Direction: row. Excludes space options.

- **Padding** (spacing) - Padding for top-level navigation items. Controls `padding` property for multiple selectors including `.brx-nav-nested-items > li > a`, text links, icons, SVG elements, and submenu toggles.

- **Background color** (color) - Background color for top-level items. Controls `background-color` property for links, text links, icons, SVG elements, and submenu toggles.

- **Border** (border) - Border styling for top-level items. Controls `border` property for links, text links, icons, SVG elements, and submenu toggles.

- **Typography** (typography) - Typography settings for top-level items. Controls `font` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transform** (transform) - Transform settings for top-level items. Controls `transform` property for links, text links, icons, SVG elements, and submenu toggles.

- **Transition** (text) - Transition settings for top-level items. Supports dynamic data. Controls `transition` property for list items, links, text links, icons, SVG elements, submenu toggles, and submenu toggle children.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Background color** (color) - Background color for active/current page items. Controls `background-color` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Border** (border) - Border styling for active items. Controls `border` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current` selectors.

- **Typography** (typography) - Typography settings for active items. Controls `font` property for `[aria-current="page"]` and `.brx-submenu-toggle.aria-current > *` selectors.

#### Dropdown (Top Level Only)

- **Dropdown** (separator) - Separator for top-level dropdown controls. Description: "Only applies to top level dropdown elements."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle > span` selector.

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-nav-nested-items > li > .brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-nav-nested-items > li > .brx-submenu-toggle` selector.

### Dropdown

#### Text

- **Text** (separator) - Separator for dropdown text controls. Description: "Control dropdown element text."

- **Text padding** (spacing) - Padding for dropdown text. Controls `padding` property for `.brx-submenu-toggle span` selector (applies to all dropdowns).

#### Icon

- **Icon** (separator) - Separator for dropdown icon controls. Description: "Edit dropdown to set icon individually."

- **Icon padding** (spacing) - Padding for dropdown icons. Controls `padding` property for `.brx-submenu-toggle button` selector.

- **Gap** (number with units) - Gap between text and icon in dropdown toggles. Controls `gap` property for `.brx-submenu-toggle` selector.

- **Icon position** (select) - Position of the dropdown icon. Options from icon position control options. Default placeholder: "Right". Controls `flex-direction` property for `.brx-submenu-toggle` selector (sets to `row-reverse` when left).

- **Icon size** (number with units) - Size of the dropdown icon. Controls `font-size` property for `.brx-submenu-toggle button` selector.

- **Icon color** (color) - Color of the dropdown icon. Controls `color` property for `.brx-submenu-toggle button` selector.

- **Icon transform** (transform) - Transform settings for dropdown icons. Controls `transform` property for `.brx-submenu-toggle button > *` selector (targets icon only).

- **Icon transform (Open)** (transform) - Transform settings for dropdown icons when open. Controls `transform` property for `.brx-submenu-toggle button[aria-expanded="true"] > *` selector (targets icon only).

- **Icon transition** (text) - Transition settings for dropdown icons. Supports dynamic data. Controls `transition` property for `.brx-submenu-toggle button[aria-expanded] > *` selector (targets icon only). Uses `!important` to override other transitions.

#### Content

- **Content** (separator) - Separator for dropdown content controls. Description: "Sub menu, mega menu, or multilevel area."

- **Min. width** (number with units) - Minimum width for dropdown content. Controls `min-width` property for `.brx-dropdown-content` selector. Triggers re-render.

- **Background color** (color) - Background color for dropdown content. Controls `background-color` property for `.brx-dropdown-content` selector.

- **Border** (border) - Border styling for dropdown content. Controls `border` property for `.brx-dropdown-content` selector.

- **Box shadow** (box-shadow) - Box shadow for dropdown content. Controls `box-shadow` property for `.brx-dropdown-content` selector.

- **Typography** (typography) - Typography settings for dropdown content. Controls `font` property for `.brx-dropdown-content` selector.

- **Transform** (transform) - Transform settings for dropdown content. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown > .brx-dropdown-content` selector.

- **Transform (Open)** (transform) - Transform settings for dropdown content when open. Controls `transform` property for `.brx-nav-nested-items > .brxe-dropdown.open > .brx-dropdown-content` selector.

- **Transition** (text) - Transition settings for dropdown content. Supports dynamic data. Controls `transition` property for `.brx-dropdown-content` selector.

- **Z-index** (number) - Z-index for dropdown elements. Controls `z-index` property for `.brxe-dropdown` selector. Default placeholder: 1001.

#### Item

- **Item** (separator) - Separator for dropdown item controls.

- **Padding** (spacing) - Padding for dropdown items. Controls `padding` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content :where(.brx-submenu-toggle > *)` selectors.

- **Background** (color) - Background color for dropdown items. Controls `background-color` property for `.brx-dropdown-content > li` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for dropdown items. Controls `border` property for `.brx-dropdown-content > li:not(.brxe-dropdown)` and `.brx-dropdown-content .brx-submenu-toggle` selectors.

- **Typography** (typography) - Typography settings for dropdown items. Controls `font` property for `.brx-dropdown-content > li > a` and `.brx-dropdown-content .brx-submenu-toggle > *` selectors.

- **Transition** (text) - Transition settings for dropdown items. Supports dynamic data. Controls `transition` property for dropdown content items, links, submenu toggles, and megamenu elements.

#### Multilevel

- **Multilevel** (separator) - Separator for multilevel controls. Description: "Show only active dropdown. Toggle on click. Inner dropdowns inherit multilevel."

- **Enable** (checkbox) - Enable multilevel dropdown functionality.

- **Back: Text** (text) - Text for the back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for the back button. Only available when multilevel is enabled. Controls `font` property for `.brx-multilevel-back` selector.

- **Back: Background** (color) - Background color for the back button. Only available when multilevel is enabled. Controls `background-color` property for `.brx-multilevel-back` selector.

### Mobile Menu

- **Mobile menu** (separator) - Separator for mobile menu controls. Description: "Insert "Toggle" element after "Nav items" to show/hide your mobile menu."

- **Keep open while styling** (checkbox) - Keep mobile menu open during styling in the builder. Adds `brx-open` class. Not saved as setting.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Width** (number with units) - Width of the mobile menu. Controls `width` property for `&.brx-open .brx-nav-nested-items` selector.

- **Height** (number with units) - Height of the mobile menu. Controls `height` property for `&.brx-open .brx-nav-nested-items` selector.

- **Padding (Dropdown)** (spacing) - Padding for dropdown content in mobile view. Controls padding for `&.brx-open .brx-dropdown-content > *` selector. Description: "Used to create visual hierarchy between nested dropdowns."

- **Align items** (align-items) - Vertical alignment of mobile menu items. Controls `align-items` property for `&.brx-open .brx-nav-nested-items` selector.

- **Justify content** (justify-content) - Horizontal alignment of mobile menu items. Controls `justify-content` property for `&.brx-open .brx-nav-nested-items` selector.

- **Position** (dimensions) - Position settings for the mobile menu. Controls multiple position properties.

- **Background color** (color) - Background color for the mobile menu. Controls `background-color` property for mobile menu selectors.

#### Item

- **Item** (separator) - Separator for mobile menu item controls.

- **Align items** (align-items) - Vertical alignment of mobile menu items. Excludes `stretch` option. Controls `align-items` property for various mobile menu item selectors.

> **Developer reference**
>
> See the [Nav (Nestable) Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-nested/) for the full JSON schema of this element's settings and controls.

---

# Offcanvas

Source: https://academy.bricksbuilder.io/builder/elements/general/offcanvas/

*The Offcanvas element is a nestable panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding.*

The **Offcanvas** element is a **nestable** panel that slides (or offsets) in from a chosen edge of the viewport. Typical use: mobile navigation. Bricks suggests adding a [Toggle](https://academy.bricksbuilder.io/builder/elements/general/toggle/) elsewhere on the page that targets this Offcanvas (see the in-element info link to the menu builder article).

The default structure includes an inner **Block** (`.brx-offcanvas-inner`) for your content—often with starter **Text** and a **Toggle** labeled for closing—and a second **Block** acting as the **Backdrop** (`.brx-offcanvas-backdrop`), which you can remove if you do not want a backdrop.

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

> **Developer reference**
>
> See the [Offcanvas Schema](https://academy.bricksbuilder.io/developer/schema/elements/offcanvas/) for the full JSON schema of this element's settings and controls.

---

# Pie chart

Source: https://academy.bricksbuilder.io/builder/elements/general/pie-chart/

*The Pie Chart element displays a circular progress chart with customizable percentage, colors, and content.*

The Pie Chart element displays a circular progress chart with customizable percentage, colors, and content.

## Settings

- **Percentage** (number) - The percentage value to display (0-100). Default: 60.

- **Chart size in px** (number) - Diameter of the chart in pixels. Default: 160.

- **Line width in px** (number) - Thickness of the progress line. Default: 8.

- **Line cap** (select) - Style of the line ends. Options: `butt`, `round`, `square`. Default: `square`.

- **Content** (select) - What to display in the center. Options: `percent`, `icon`, `text`. Default: `percent`.

- **Icon** (icon) - Icon to display in the center. Only shown when Content is set to "icon".

- **Text** (text) - Custom text to display in the center. Only shown when Content is set to "text".

- **Bar color** (color) - Color of the progress bar. Default: Primary theme color.

- **Track color** (color) - Color of the background track. Default: Light background color.

- **Scale length in px** (number) - Length of the scale marks.

- **Scale color** (color) - Color of the scale marks. Only shown when Scale length is set.

> **Developer reference**
>
> See the [Pie Chart Schema](https://academy.bricksbuilder.io/developer/schema/elements/pie-chart/) for the full JSON schema of this element's settings and controls.
