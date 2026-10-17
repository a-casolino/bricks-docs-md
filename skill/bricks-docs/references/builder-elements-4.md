# Related posts

Source: https://academy.bricksbuilder.io/builder/elements/single/related-posts/

*Displays posts related to the current post based on shared taxonomies.*

Displays posts related to the current post based on shared taxonomies.

## Settings

### Title
- **Title** (text) - Section title text.
- **HTML tag** (select) - HTML tag for title. Options: h2, h3, h4, h5, h6. Default: h2.
- **Margin** (spacing) - Title margin.
- **Typography** (typography) - Title typography.

### Query
- **Post type** (select) - Post type to query.
- **Max. related posts** (number) - Maximum number of related posts. Default: 3.
- **Order** (select) - Sort order. Default: Descending.
- **Order by** (select) - Sort criteria. Default: Random.
- **Common taxonomies** (select) - Taxonomies posts must share. Default: category, post_tag.

### Layout
- **Gap** (number) - Spacing between posts. Default: 30px.
- **Posts per row** (number) - Number of posts per row. Default: 3.

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes: `{post_title:link}`, `{post_date}`, `{post_excerpt:20}`.
  - **Dynamic data** (text) - Dynamic data expression.
  - **HTML tag** (select) - HTML tag for field. Default: div.
  - **Margin** (spacing) - Field margin.
  - **Padding** (spacing) - Field padding.
  - **Background color** (color) - Field background color.
  - **Border** (border) - Field border.
  - **Typography** (typography) - Field typography.

### Image
- **Disable** (checkbox) - Hide post images.
- **Aspect ratio** (text) - Image aspect ratio.
- **Image size** (select) - WordPress image size.
- **Position** (select) - Image position. Options: Top, Right, Bottom, Left. Default: Top.
- **Height** (number) - Image height.
- **Width** (number) - Image width.
- **Margin** (spacing) - Image margin.

### Content
- **Width** (number) - Content area width.
- **Padding** (spacing) - Content area padding.
- **Background color** (color) - Content area background color.
- **Overlay content** (checkbox) - Overlay content on image.
- **Horizontal alignment** (align-items) - Content horizontal alignment (overlay mode).
- **Vertical alignment** (justify-content) - Content vertical alignment (overlay mode).

> **Developer reference**
>
> See the [Related Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/related-posts/) for the full JSON schema of this element's settings and controls.

---

# Social sharing

Source: https://academy.bricksbuilder.io/builder/elements/single/social-sharing/

*Displays social media sharing buttons for the current post.*

Displays social media sharing buttons for the current post.

## Settings

- **Share via** (repeater) - Social media services to include. Default includes: Facebook, X, LinkedIn, WhatsApp, Pinterest, Telegram, VKontakte, Bluesky, Email.
  - **Service** (select) - Social media platform.
  - **Excerpt** (checkbox) - Include post excerpt in share (WhatsApp only).
  - **Icon** (icon) - Custom icon for the service.
  - **Background** (color) - Button background color.
  - **Color** (color) - Button text/icon color.
- **Use brand colors** (checkbox) - Apply default brand colors to buttons. Default: true.
- **Direction** (direction) - Layout direction for sharing buttons.
- **Open in new tab** (checkbox) - Open sharing links in new tabs.
- **Rel attribute** (text) - Link rel attribute. Default: "nofollow".

> **Developer reference**
>
> See the [Social Sharing Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-sharing/) for the full JSON schema of this element's settings and controls.

---

# Taxonomy

Source: https://academy.bricksbuilder.io/builder/elements/single/taxonomy/

*Displays taxonomy terms for the current post.*

Displays taxonomy terms for the current post.

## Settings

- **Taxonomy** (select) - Taxonomy to display terms from. Default: post_tag.
- **Disable link** (checkbox) - Remove links from taxonomy terms.
- **Separator** (text) - Text to display between terms.
- **Order by** (select) - Sort terms by criteria. Default: Name.
- **Order** (select) - Sort direction. Default: Ascending.
- **Size** (select) - Button size for terms.
- **Style** (select) - Button style for terms. Default: dark.
- **Spacing** (number) - Gap between terms. Default: 10px.
- **Icon** (icon) - Icon to display with each term.

> **Developer reference**
>
> See the [Taxonomy Schema](https://academy.bricksbuilder.io/developer/schema/elements/post-taxonomy/) for the full JSON schema of this element's settings and controls.

---

# Query results summary

Source: https://academy.bricksbuilder.io/builder/elements/query/query-results-summary/

*The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which.*

The Query Results Summary element, introduced in version 1.12.2, allows you to display a dynamic count of results within a query, helping users understand which items they are currently viewing in relation to the total number of results. This is particularly useful for search results, archive pages, and paginated lists where users navigate through multiple pages of content. It can be found in the elements panel under the "Query" category.

**Note:** If a third-party plugin disables Bricks Query history via the [`bricks/query/force_run`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-query-force_run/) hook, the results summary may display incorrect information.

## Compatibility

The **Query Results Summary** element works seamlessly with Bricks' native AJAX actions, including:

- AJAX Pagination
- Load More
- Infinite Scroll
- Query Filters

This ensures that the summary updates dynamically as users interact with query-based elements on the page.

Example:

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-example.png)

## Settings

![](https://academy.bricksbuilder.io/assets/query-results-summary-element-controls.png)

### Query

Select the **target query** for which the summary should be displayed.

### Format

Customize the summary text using placeholders:

- `%start%` – The index of the first item on the current page.
- `%end%` – The index of the last item on the current page.
- `%total%` – The total number of results.

Default format: `Results: %start% - %end% of %total% posts`

Example output: Results: 1 - 5 of 14 posts

### Text: One Result

Define a custom message when the query returns exactly **one** result to handle singular/plural differences.

Default text: One post found

### Text: No Results

Specify a custom message when the query returns **zero** results.

Default text: No posts found

> **Developer reference**
>
> See the [Query Results Summary Schema](https://academy.bricksbuilder.io/developer/schema/elements/query-results-summary/) for the full JSON schema of this element's settings and controls.

---

# Account - Addresses

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-addresses/

*Displays the customer addresses section inside My Account.*

Displays the customer addresses section inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Title** (separator)
- **Address** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Add payment method

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-add-payment-method/

*Displays the Add payment method endpoint content inside My Account templates.*

Displays the Add payment method endpoint content inside My Account templates.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Wrapper** (separator)
- **Payment Methods List** (separator)
- **Payment Method Item** (separator)
- **Label** (separator)
- **Custom Radio (Checked)** (separator)
- **Color** (color)
- **Payment Box** (separator)
- **Add Payment Method Button** (separator)
- **Margin** (spacing)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Downloads

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-downloads/

*Displays customer downloadable products inside My Account.*

Displays customer downloadable products inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Table** (separator)
- **Head** (separator)
- **Body** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit account

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-account/

*Displays the Edit account form inside My Account.*

Displays the Edit account form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Label typography** (typography)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Width** (number)
- **Gap** (number)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Edit address

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-edit-address/

*Displays the Edit address form inside My Account.*

Displays the Edit address form inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Hide** (checkbox)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Label typography** (typography)
- **Placeholder typography** (typography)
- **Field** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Login form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-login/

*Displays the WooCommerce My Account login form.*

Displays the WooCommerce My Account login form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Lost password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-lost-password/

*Displays the Lost password request form used in My Account flows.*

Displays the Lost password request form used in My Account flows.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Register form

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-register/

*Displays the WooCommerce account registration form.*

Displays the WooCommerce account registration form.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Generate password** (separator)
- **Typography** (typography)
- **Privacy policy** (separator)
- **Link** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Reset password

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-form-reset-password/

*Displays the Reset password form used after password reset link validation.*

Displays the Reset password form used after password reset link validation.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Disable** (checkbox)
- **Typography** (typography)
- **Align items** (align-items)
- **Width** (number)
- **Gap** (number)
- **Label typography** (typography)
- **Field** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background color** (color)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Orders

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-orders/

*Displays the customer orders table inside My Account.*

Displays the customer orders table inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Body - Heading** (separator)
- **Links** (separator)
- **Button** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Page v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/

*Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.*

Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

My Account page.

## Key settings

- **State** (radio) - Switches the builder preview between My Account endpoint states.
- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Navigation** style controls
- **Content** style controls

## States

- **Dashboard**
- **Orders**
- **View order**
- **Downloads**
- **Addresses**
- **Edit address**
- **Edit account**
- **Payment methods**
- **Add payment method**
- **Login**
- **Lost password**
- **Lost password (Confirmation)**
- **Reset password**
- **Order withdrawal** (requires WooCommerce 11.1 or later with Order Withdrawal enabled)

<div className="screenshot screenshot--control-panel">

![Account Page v2 State controls, including Order withdrawal and the Add missing states button.](https://academy.bricksbuilder.io/assets/account-page-v2-states-with-missing-state.webp)

</div>

## Generated structures

Each state can generate a complete starter block for that endpoint from **Insert a structure**.

Generated structures are appended to the current state content and do not overwrite existing content.

> **Note**
>
> Account Page v2 uses support elements for generated account forms and account orders pagination. Account orders, downloads, addresses, and order actions use v2 query loops and dynamic tags inside the matching account state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/account-v2-view-orders-structure-example.png)

## Add missing states

If an expected state element is missing, select **Account - Page v2** and click **Add missing states**. Bricks checks all currently available account states and appends any missing state elements without replacing existing states or their content. This can restore an unexpectedly missing state or add a state introduced after the page was built.

The button appears only when states are missing and your builder permissions allow adding elements. States that depend on a disabled WooCommerce feature are excluded. For an Account Page v2 inside a component, edit the component definition to repair its states.

Added states start empty. Select each added state and use **Insert a structure** to generate its starter content. This tool does not restore deleted custom layouts or refill existing empty states; generate content inside an empty state separately.

## Order withdrawal

This public state requires WooCommerce 11.1 or later with **Order Withdrawal** enabled under **WooCommerce > Settings > Advanced > Features**. It lets guests and logged-in customers enter, review, and confirm a withdrawal request.

Select **Order withdrawal (State)** and generate **Complete order withdrawal block** under **Insert a structure**. If the state is missing, use **Add missing states** first. The generated block includes **Your details**, **Review**, and **Confirmation** sections. All three appear together with sample data in the builder; their **Order withdrawal screen** conditions select the matching section on the frontend.

Keep the generated **Account order withdrawal form** wrappers, submit buttons, and screen conditions when customizing the layout. WooCommerce handles validation and submission. Use the [withdrawal dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-withdrawal-tags) to display submitted details. A missing or empty withdrawal state falls back to WooCommerce's native form.

Add a visible link using `{woo_url:order-withdrawal}` so customers can find the endpoint; WooCommerce does not add one automatically. A withdrawal request does not cancel an order or issue a refund.

## Field maintenance

The Edit address state can audit and sync generated account address fields against the current WooCommerce account address field registry.

Use the field maintenance actions after plugins or WooCommerce settings change account address fields:

- **Check address fields**
- **Generate missing fields**
- **Remove invalid fields**
- **Remove duplicate fields**

![](https://academy.bricksbuilder.io/assets/account-v2-sync-address-fields.png)

## Query loops and dynamic data

Account Page v2 supports WooCommerce v2 query loops for account orders, order actions, account downloads, and account addresses.

Use account and order tags such as `{woo_account_address_title}`, `{woo_account_address}`, `{woo_order_number}`, `{woo_order_view_url}`, `{woo_order_download_name}`, and `{woo_order_action_url}` in the matching state or query loop.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Account Page v2 structure.
- Review each state after setup so logged-in, logged-out, password reset, payment method, and order views all match your store design.
- Use the classic [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) workflow if you prefer separate endpoint templates.

---

# Account - Page

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page/

*Displays the full My Account layout including navigation and endpoint content.*

Displays the full My Account layout including navigation and endpoint content.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Align items** (align-items)
- **Justify content** (justify-content)
- **Background** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Item** (separator)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - Payment methods

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-payment-methods/

*Displays saved payment methods inside My Account.*

Displays saved payment methods inside My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Head** (separator)
- **Body** (separator)
- **Delete button** (separator)
- **Make default button** (separator)
- **Add payment method** (separator)
- **Background color** (color)
- **Border** (border)
- **Box shadow** (box-shadow)
- **Typography** (typography)
- **Padding** (spacing)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# Account - View order

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/account-view-order/

*Displays order details for a selected order in My Account.*

Displays order details for a selected order in My Account.

## Where this element works

My Account templates and My Account endpoint views.

## Key settings

- **Preview order ID** (number)
- **Hide** (checkbox)
- **Typography** (typography)
- **Mark** (separator)
- **Padding** (spacing)
- **Background color** (color)
- **Title** (separator)
- **Meta** (separator)
- **Description** (separator)
- **Table** (separator)

## Usage tips

- Use these elements in My Account templates or endpoint-specific templates.
- Verify each endpoint (orders, downloads, addresses, payment methods) so navigation and forms stay consistent.

---

# WooCommerce Breadcrumbs

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/breadcrumbs/

*Display WooCommerce breadcrumb navigation in Bricks and customize the home link, prefixes, suffixes, separators, and spacing.*

Displays WooCommerce breadcrumb navigation.

## Settings

- **Before** (text) - Text to display before breadcrumbs.

- **Home: URL** (text) - Custom URL for home link. Default: home URL.

- **Home: Label** (text) - Label for home link. Default: "Home".

- **Home: Icon** (icon) - Icon for home link.

- **Home: Gap** (number with units) - Gap between home icon and label.

- **Home: Icon Size** (number) - Size of home icon.

- **Hide label** (checkbox) - Hide home label when icon is present. Only available when Home: Icon is set.

- **Prefix** (text) - Text to display before each breadcrumb item.

- **Suffix** (text) - Text to display after each breadcrumb item.

### Separator

- **Type** (select) - Separator type. Options: Text, Icon. Default: Text.

- **Separator** (text) - Separator text. Default: "/". Only available when Type is not Icon.

- **Icon** (icon) - Separator icon. Only available when Type is Icon.

- **Icon typography** (typography) - Typography for separator icon. Only available when Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.

- **Gap** (number with units) - Gap between breadcrumb items.

- **Margin** (spacing) - Margin around separators.

---

# Cart totals

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-collaterals/

*Displays cart totals and related collateral content from the Cart page.*

Displays cart totals and related collateral content from the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **Disable cross sells** (checkbox)
- **Hide title** (checkbox)
- **Title** (typography)
- **Subtotal** (typography)
- **Total** (typography)
- **Table** (separator)
- **Margin** (spacing)
- **Padding** (spacing)
- **Border** (border)
- **Button** (separator)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-coupon/

*Displays the coupon input section for the Cart page.*

Displays the coupon input section for the Cart page.

## Where this element works

Cart page templates.

## Key settings

- **General** (separator)
- **Update cart via AJAX** (checkbox)
- **Direction** (direction)
- **Input** (separator)
- **Placeholder** (text)
- **Width** (number)
- **Background color** (color)
- **Border** (border)
- **Placeholder typography** (typography)
- **Button** (text)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart items

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-items/

*Displays the cart items table with product rows and quantity controls.*

Displays the cart items table with product rows and quantity controls.

## Where this element works

Cart page templates.

## Key settings

- **Disable link** (checkbox)
- **Header** (separator)
- **Hide** (checkbox)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)
- **Body** (separator)
- **Image** (separator)
- **Disable** (checkbox)
- **Width** (number)

## Usage tips

- Place cart elements in a dedicated Cart template to avoid empty output on non-cart pages.
- Keep spacing and table styling consistent across cart rows, totals, and coupon sections for better usability.

---

# Cart v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/

*Displays the WooCommerce cart page as editable Filled cart and Empty cart states.*

Displays the WooCommerce cart page as editable Filled cart and Empty cart states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Cart page.

## Key settings

- **State** (radio) - Switches the builder preview between Filled cart and Empty cart.

## States

- **Filled cart** - Used when the cart contains products.
- **Empty cart** - Used when the cart has no products.

The generated Cart v2 structure keeps both states as internal child elements, so you can edit each state from the Structure panel.

![](https://academy.bricksbuilder.io/assets/cart-v2-states.png)

## Generated structures

Each state can generate starter content from **Insert a structure**:

- **Complete cart block**
- **Complete empty cart block**

Generated structures are appended to the current state content and do not overwrite existing content.

![](https://academy.bricksbuilder.io/assets/cart-v2-state-insert-structure.png)

> **Note**
>
> Cart v2 uses the Cart form and Cart quantity support elements inside the Filled cart state. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/cart-v2-filled-cart-structure-example.png)

## Query loops and dynamic data

Use the **Cart contents** query loop for custom cart item rows. Cart v2 layouts can also use cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Cart v2 structure.
- Design both states so the cart page is complete whether the customer has products in the cart or not.
- Use the classic [Cart template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) if you prefer separate Cart and Empty Cart templates.

---

# Checkout login

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-login/

*Displays the returning customer login prompt on Checkout.*

Displays the returning customer login prompt on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Disable login message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout customer details

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-customer-details/

*Displays billing and shipping customer detail fields on Checkout.*

Displays billing and shipping customer detail fields on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Remove billing fields** (select)
- **Remove shipping fields** (select)
- **Title** (separator)
- **Hide** (checkbox)
- **Typography** (typography)
- **Labels** (separator)
- **Margin** (spacing)
- **Fields** (separator)
- **Placeholder typography** (typography)
- **Hide additional information** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout coupon

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-coupon/

*Displays the coupon prompt and form on the Checkout page.*

Displays the coupon prompt and form on the Checkout page.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Location** (select)
- **Toggleable form** (checkbox)
- **Text** (text)
- **Justify content** (justify-content)
- **Gap** (number)
- **Button** (separator)
- **Disable text** (checkbox)
- **Icon** (icon)
- **Icon typography** (typography)
- **Disable coupon message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order table

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-table/

*Displays the checkout order table with line items, totals, and taxes.*

Displays the checkout order table with line items, totals, and taxes.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order payment

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-payment/

*Displays available payment methods and payment actions on Checkout.*

Displays available payment methods and payment actions on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Label typography** (typography)
- **Description** (separator)
- **Typography** (typography)
- **Privacy** (separator)
- **Button** (separator)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout order review

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-order-review/

*Displays the order review section on Checkout.*

Displays the order review section on Checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Hide title** (checkbox)
- **Title** (text)
- **Title typography** (typography)
- **Subtitles typography** (typography)
- **Items** (separator)
- **Typography** (typography)
- **Padding** (spacing)
- **Border** (border)
- **Margin** (spacing)
- **Background** (color)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout thank you

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-thankyou/

*Displays the order received / thank you content after checkout.*

Displays the order received / thank you content after checkout.

## Where this element works

Checkout templates (and order-received context for thank-you flows).

## Key settings

- **Preview order ID** (number)
- **Hide message** (checkbox)
- **Margin** (spacing)
- **Padding** (spacing)
- **Background** (color)
- **Border** (border)
- **Typography** (typography)
- **Label typography** (typography)
- **Action buttons** (separator)
- **Gap** (number)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.

---

# Checkout v2

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/

*Displays the WooCommerce checkout page as editable Checkout, Login required, Pay, Thank you, and Order receipt states.*

Displays the WooCommerce checkout page as editable Checkout, Login required, Pay, Thank you, and Order receipt states.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

Checkout page.

## Key settings

- **State** (radio) - Switches the builder preview between checkout states.

## States

- **Checkout** - Customer details, order summary, payment options, and place order layout.
- **Login required** - Login screen shown when WooCommerce requires login before an order-related checkout screen.
- **Pay** - Payment screen for unpaid orders.
- **Thank you** - Order confirmation screen after checkout.
- **Order receipt** - Receipt screen for unpaid order links that no longer need payment.

![](https://academy.bricksbuilder.io/assets/checkout-v2-states.png)

## Generated structures

The Checkout state can generate these structures:

- **Complete checkout**
- **Billing fields**
- **Shipping fields**
- **Payment options**
- **Additional fields**
- **Order summary**
- **Place order**

When **Complete checkout** is selected, **Generate as multistep** creates a ready-made multistep checkout layout.

The **Billing fields** and **Complete checkout** structures also generate the account credential fields currently required by WooCommerce. Bricks places these fields inside a **Checkout account fields** wrapper so WooCommerce's account-creation settings control their frontend visibility.

The Login required, Pay, Thank you, and Order receipt states each provide a complete block for that state.

> **Note**
>
> Some Checkout v2 support elements, including generated form fields, checkout steps, step navigation items, payment options, and place order sections, rely on the correct Checkout v2 state context. If you cannot find a support element in the regular Elements panel, use **Insert a structure** and then edit the generated element in the Structure panel.

![](https://academy.bricksbuilder.io/assets/checkout-v2-structure-example.png)

## Payment section for free orders

In the **Checkout** state, payment methods are hidden when the cart does not require payment, such as after a coupon reduces the total to zero. They reappear when a shipping or coupon change makes payment necessary again.

The `brx-woo-payment-section` class lets the surrounding payment section, including its heading, hide and reappear with the payment methods. Newly generated **Payment options** and **Complete checkout** structures include this class on the **Payment Options** wrapper, including the multistep layout.

Existing checkout layouts are not updated automatically. If the class is missing, add it manually:

1. Edit the assigned Checkout page with Bricks and select the **Checkout** state.
2. In the Structure panel, select the wrapper containing the payment heading and **Payment options** element. In generated layouts, this is the **Payment Options** Block.
3. Open **Style > CSS > CSS classes** and add `brx-woo-payment-section` without a leading dot. Keep any existing classes, separated by spaces.
4. Keep the terms checkbox and **Place order** controls outside this wrapper so customers can still submit free orders. In a multistep layout, add the class to the payment section wrapper inside the step, rather than the entire Checkout step.
5. Save and test the checkout on the frontend with both a zero total and a total that requires payment.

Without this wrapper class, the payment methods still hide for free orders, but the surrounding heading and section can remain visible.

## Account creation during checkout

Checkout v2 follows the guest checkout and account creation settings under **WooCommerce > Settings > Accounts & Privacy**.

| Guest checkout | Account creation during checkout | Checkout behavior |
| --- | --- | --- |
| Enabled | Disabled | Guests can check out without account fields. |
| Enabled | Enabled | Guests can select **Create an account?** to reveal the required account fields. |
| Disabled | Enabled | Account creation is required. The account fields remain visible without the optional **Create an account?** checkbox. |
| Disabled | Disabled | Logged-out customers see the Checkout v2 **Login required** state. |

WooCommerce decides which credential fields are required:

| Generate account login | Send password setup link | Credential fields |
| --- | --- | --- |
| Enabled | Enabled | None |
| Disabled | Enabled | Username |
| Enabled | Disabled | Password |
| Disabled | Disabled | Username and password |

Generated username and password fields are required. Bricks reads these fields from WooCommerce's current checkout field registry, including fields added by third-party plugins, instead of assuming a fixed set.

The **Allow customers to create an account on the My Account page** setting applies to Account Page v2 registration and does not change account creation during Checkout v2.

## Multistep checkout

Use [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) when you want the Checkout state split into multiple steps.

You can create the multistep layout with the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) by choosing **Advanced multistep (v2)**, or generate it from the Checkout state by selecting **Complete checkout** and enabling **Generate as multistep**.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep.png)

The generated layout includes Checkout steps navigation, checkout step nav items, checkout step wrappers, and next/back interactions.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-structure-example.png)

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-frontend.png)

## Field maintenance

When order notes are disabled in WooCommerce, a saved Order notes field can remain visible in the builder while being hidden on the frontend. Remove unused notes elements or empty headings from **Additional fields**, keeping any fields used by checkout extensions.

Checkout v2 includes a **Sync checkout fields** control group with actions to compare generated fields with the site's current WooCommerce checkout fields:

- **Check checkout fields**
- **Generate missing fields**
- **Remove invalid fields**
- **Remove duplicate fields**

Use these after changing WooCommerce checkout fields or installing plugins that add checkout fields.

Field sync can report valid, missing, invalid, and duplicate generated fields. It can generate missing fields, remove generated fields that no longer exist in WooCommerce, remove duplicate generated fields, and update generated field labels and placeholders from the current WooCommerce field data.

The audit includes WooCommerce's `account` field section. Missing account fields are inserted into the **Checkout account fields** wrapper, while billing, shipping, and additional fields remain in their corresponding checkout sections.

Enabling **Generate account login** or **Send password setup link** does not remove the corresponding saved username or password element from an existing Checkout v2 structure. Until you run field sync, an element that WooCommerce no longer registers can still render as an optional field, but WooCommerce does not process its value because it generates that credential. Run **Check checkout fields**, then **Remove invalid fields**.

Checkout structures created with a Bricks 2.4 beta may contain a standalone **Create account** checkbox or may not contain the account wrapper. Regenerate the checkout structure or use the field sync actions after updating. Bricks creates the wrapper when missing account fields are generated and removes an obsolete standalone checkbox after the replacement wrapper and checkbox exist.

![](https://academy.bricksbuilder.io/assets/checkout-v2-sync-checkout-fields.png)

## Query loops, dynamic tags, and interactions

For saved Thank you layouts, see [Failed-order messages](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/#failed-order-messages) to replace a typed payment failure message with `{woo_order_failed_text}`.

Checkout v2 supports WooCommerce v2 query loops for applied coupons, fees, taxes, order items, order totals, order downloads, and customer notes.

It also adds checkout/order tags such as `{woo_checkout_current_step_number}`, `{woo_order_number}`, `{woo_order_total}`, `{woo_order_item_count}`, and `{woo_order_total_with_item_count}`.

For multistep checkout layouts, use the **Checkout step** interaction action to move to the next step, previous step, a specific step, or a specific checkout field.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Checkout v2 structure.
- Design every checkout state that customers can reach, especially Pay, Thank you, Order receipt, and Login required.
- Use the classic [Checkout template workflow](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/) if you prefer separate checkout templates.

---

# Dynamic fragment

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/

*Re-renders WooCommerce cart-dependent content after cart changes.*

Re-renders WooCommerce cart-dependent content after cart changes.

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Where this element works

WooCommerce-aware Bricks layouts, such as page content, headers, and footers that need to update after cart changes.

## Key settings

- **Insert a structure** (select) - Choose a generated starter structure.
- **Generate** (button) - Adds the selected structure to the element.

## Generated structures

- **Mini cart**
- **Free shipping progress**

Generated structures are appended to the current content and do not overwrite existing content.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-states.png)

## Usage tips

- Use Dynamic fragment for cart-dependent content outside the main Cart page, such as custom mini cart content, free shipping progress, or cart totals.
- Keep the fragment focused on content that needs to refresh after add-to-cart, remove-from-cart, or quantity changes.
- Keep the Dynamic fragment wrapper outside other query loops. A cart loop can be placed inside the fragment.

## Custom mini cart pattern

To build a lightweight custom mini cart:

1. Add a Dynamic fragment element where the mini cart should render.
2. Inside it, add a container and enable the **Cart contents** query loop.
3. Design the cart item row inside the loop.
4. Use cart item tags such as `{featured_image}`, `{woo_cart_product_name}`, `{woo_cart_quantity:value}`, `{woo_cart_subtotal}`, and `{woo_cart_remove_link:url}`.
5. Add cart total tags outside the loop but still inside the Dynamic fragment, such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-mini-cart-structure-example.png)

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete tag list.

## Refresh behavior

Dynamic fragment refreshes after WooCommerce cart, coupon, and checkout events such as add to cart, remove from cart, cart emptied, cart totals updated, checkout updated, and coupon apply/remove events.

After a refresh, Bricks reruns frontend functions and dispatches:

```js
document.body.addEventListener('bricks/woocommerce/fragments/refreshed', (event) => {
  console.log(event.detail.fragments)
})
```

This refresh event also covers initial synchronization and checkout recalculations that do not change cart items. For a custom success notice or popup, use the [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed) interaction trigger, available since Bricks 2.4. It runs after a confirmed AJAX addition, removal, or quantity change and the related UI updates finish.

## Limitations

- Dynamic fragment is frontend-only.
- Do not place the Dynamic fragment wrapper inside a query loop.
- Component instances are not supported.
- The source area must be header, content, or footer.

---

# Mini cart

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/mini-cart/

*Displays a mini cart icon with cart count and dropdown cart details.*

Displays a mini cart icon with cart count and dropdown cart details.

## Settings

- **Icon** (icon) - Cart icon. Default: ti-shopping-cart.
- **Icon typography** (typography) - Typography for cart icon. Only available when Icon is set.
- **Open on add to cart (AJAX)** (checkbox) - Open mini cart when products are added via AJAX.

### Cart count

- **Visibility** (select) - Show/hide cart count. Options: Hide (Always), Show (Always). Default: Hide if empty.
- **Background color** (color) - Cart count background color. Only available when Visibility is not Hide (Always).
- **Border** (border) - Cart count border settings. Only available when Visibility is not Hide (Always).
- **Typography** (typography) - Cart count typography. Only available when Visibility is not Hide (Always).
- **Transform** (transform) - Cart count transform. Only available when Visibility is not Hide (Always) and Off-Canvas is not Top or Bottom.
- **Height** (number with units) - Cart count height. Only available when Visibility is not Hide (Always).
- **Width** (number with units) - Cart count width. Only available when Visibility is not Hide (Always).
- **Top** (number with units) - Cart count top position. Only available when Visibility is not Hide (Always).
- **Right** (number with units) - Cart count right position. Only available when Visibility is not Hide (Always).
- **Bottom** (number with units) - Cart count bottom position. Only available when Visibility is not Hide (Always).
- **Left** (number with units) - Cart count left position. Only available when Visibility is not Hide (Always).

### Cart subtotal

- **Position** (select) - Subtotal position. Options: Right, Left.
- **Gap** (number with units) - Gap between icon and subtotal. Only available when Position is set.
- **Typography** (typography) - Subtotal typography. Only available when Position is set.

### Cart details

- **Hide** (checkbox) - Hide cart details dropdown.
- **Don't close on click outside mini cart** (checkbox) - Prevent auto-close on outside clicks. Only available when Hide is not checked.
- **Off-Canvas** (select) - Off-canvas position. Options: Top, Right, Bottom, Left. Only available when Hide is not checked.
- **Height** (number with units) - Cart details height. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Width** (number with units) - Cart details width. Default: 400px. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Image width** (number with units) - Product image width. Default: 60px. Only available when Hide is not checked.
- **Padding** (spacing) - Cart details padding. Only available when Hide is not checked.
- **Position** (dimensions) - Cart details position. Only available when Hide is not checked and Off-Canvas is Disabled.
- **Transform** (transform) - Cart details transform. Only available when Hide is not checked and Off-Canvas is not Top or Bottom.
- **Background** (color) - Cart details background color. Only available when Hide is not checked.
- **Border** (border) - Cart details border settings. Only available when Hide is not checked.
- **Box shadow** (box-shadow) - Cart details box shadow. Only available when Hide is not checked.
- **Typography (Title)** (typography) - Title typography. Only available when Hide is not checked.
- **Typography (Quantity)** (typography) - Quantity typography. Only available when Hide is not checked.

#### Buttons

- **Background color** (color) - Button background color. Only available when Hide is not checked.
- **Border** (border) - Button border settings. Only available when Hide is not checked.
- **Typography** (typography) - Button typography. Only available when Hide is not checked.

#### Close

- **Icon** (icon) - Close icon. Only available when Hide is not checked.
- **Typography** (typography) - Close typography. Only available when Hide is not checked and Icon is set. Excludes: font-family, font-weight, font-style, text-align, text-decoration, text-transform, line-height, letter-spacing.
- **Position** (dimensions) - Close position. Only available when Hide is not checked and Icon is set.
- **Padding** (spacing) - Close padding. Only available when Hide is not checked and Icon is set.
- **Background color** (color) - Close background color. Only available when Hide is not checked and Icon is set.
- **Border** (border) - Close border settings. Only available when Hide is not checked and Icon is set.

---

# Notice

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/notice/

*Displays WooCommerce system notices (success, info, and error messages).*

Displays WooCommerce system notices (success, info, and error messages).

## Where this element works

Shop/archive templates and WooCommerce pages where the related data exists.

## Key settings

- **Preview notice type** (select)

## Usage tips

- Keep notice styles highly readable so customers can quickly understand errors and confirmation messages.
- Check all notice types (success, info, error) in real cart and checkout scenarios.

---

# Products archive description

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-archive-description/

*Displays the description for WooCommerce product archives (shop page, categories, tags).*

Displays the description for WooCommerce product archives (shop page, categories, tags).

---

# Products filter

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-filter/

*Displays product filters for WooCommerce product listings.*

Displays product filters for WooCommerce product listings.

## Settings

- **Filters** (repeater) - Product filter configurations.
  - **Filter type** (select) - Type of filter. Options: Taxonomy, Product attribute, Other.
  - **Filter by** (select) - Specific filter to apply (depends on type).
  - **Filter input** (select) - Input type. Options: Dropdown, Checkbox, Radio list, Text list, Box list.
  - **Any option text** (text) - Text for "any" option. Default: "Any".
  - **Only parent terms** (checkbox) - Show only parent terms.
  - **Show empty terms** (checkbox) - Include terms with no products.
  - **Filter title** (text) - Title for the filter.
  - **Hide title** (checkbox) - Hide filter title.
  - **Collapse** (checkbox) - Make filter collapsible.
- **Spacing** (number) - Gap between filters. Default: 30px.

### Title
- **Margin** (spacing) - Title margin. Default: 0 0 15px 0.
- **Padding** (spacing) - Title padding.
- **Typography** (typography) - Title typography.
- **Background color** (color) - Title background color.

---

# Products orderby

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-orderby/

*Displays a dropdown to sort WooCommerce products.*

Displays a dropdown to sort WooCommerce products.

## Settings

- **Order by** (select) - Available sorting options. Multiple selection. Leave empty to use WooCommerce default list.

---

# Products pagination

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-pagination/

*Displays pagination for WooCommerce product listings.*

Displays pagination for WooCommerce product listings.

## Settings

- **Alignment** (align-items) - Pagination alignment.
- **Previous Icon** (icon) - Icon for previous page link.
- **Next Icon** (icon) - Icon for next page link.
- **End Size** (number) - How many numbers on either the start and the end list edges. Minimum: 1.
- **Mid Size** (number) - How many numbers to either side of the current page. Minimum: 1.

---

# Products total results

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-total-results/

*Displays the total number of products found and current result range.*

Displays the total number of products found and current result range.

---

# WooCommerce Template Hook

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/template-hook/

*Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.*

Renders output from a selected WooCommerce template hook so you can place WooCommerce hook content in your layout.

## Where this element works

Any WooCommerce template where the selected hook is executed.

## Key settings

- **Template** (select)
- **Hook** (select)
- **Show tips** (checkbox)

## Usage tips

- Pick hooks intentionally and avoid duplicating WooCommerce default output in the same area.
- If expected content does not appear, confirm the selected hook runs in the current template context.

---

# Products

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products/

*Displays WooCommerce products in a grid layout with customizable fields and widgets.*

Displays WooCommerce products in a grid layout with customizable fields and widgets.

## Settings

- **Columns** (number) - Number of columns. Range: 1-6. Default: 4. Supports breakpoints.
- **Gap** (number) - Spacing between products. Default: 30px.

### Query
- Product query controls (via Woocommerce_Helpers::get_product_query_controls).

### Fields
- **Content** (repeater) - Dynamic data fields to display. Default includes WooCommerce hooks and product fields like title, image, price, add to cart.
- **Link entire product** (checkbox) - Make entire product clickable if no field links exist.

### Widgets
- **Show Before Grid** (select) - Widgets to show before products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Show After Grid** (select) - Widgets to show after products grid. Options: Pagination, Result Count, Order by. Multiple selection.
- **Sort by options** (select) - Available sorting options. Default: Default sorting. Multiple selection.

---

# Nav menu

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/nav-menu/

*The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile.*

The Nav Menu element displays WordPress navigation menus with customizable styling and behavior. It supports mega menus, multilevel navigation, mobile responsiveness, and various animation effects.

## Settings

### Menu Selection

- **Menu (WordPress)** (select) - Select a WordPress navigation menu to display. Options are populated from available WordPress menus. Includes a link to manage menus in WordPress admin.

- **Alignment** (direction) - Layout direction of the menu. Controls `flex-direction` property for `.bricks-nav-menu` selector.

### Top level

- **Justify content** (justify-content) - Horizontal alignment of menu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Gap** (number with units) - Gap between menu items. Controls `gap` property for `.bricks-nav-menu` selector.

- **Margin** (spacing) - Margin around menu items. Controls `margin` property for `.bricks-nav-menu > li` selector.

- **Padding** (spacing) - Padding inside menu items. Controls `padding` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

- **Background** (background) - Background styling for menu items. Excludes video. Controls `background` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for menu items. Controls `border` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle` selectors.

- **Typography** (typography) - Font settings for top-level menu items. Controls `font` property for `.bricks-nav-menu > li > a` and `.bricks-nav-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Visual separator for active state controls.

- **Active background** (background) - Background styling for active/current page items. Controls `background` property for current menu item selectors including `.bricks-nav-menu > .current-menu-item > a`, `.bricks-nav-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active items. Controls `border` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active items. Controls `font` property for current menu item selectors including `.bricks-nav-menu .current-menu-item > a`, `.bricks-nav-menu .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for icon controls.

- **Icon (Sub menu)** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu > li.menu-item > .brx-submenu-toggle svg` selector.

- **Icon transform** (transform) - Transform settings for submenu icons when closed. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="false"] > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu > li.menu-item-has-children > .brx-submenu-toggle button[aria-expanded]` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .brx-submenu-toggle button` selector.

### Sub menu

- **Position: Static** (checkbox) - Enable to position submenus in document flow (e.g. inside offcanvas). Description: "Enable to position in document flow (e.g. inside offcanvas)."

- **Background** (background) - Background styling for sub-menus. Excludes video. Controls `background` property for `.bricks-nav-menu .sub-menu` selector.

- **Border** (border) - Border styling for sub-menus. Controls `border` property for `.bricks-nav-menu .sub-menu` selector.

- **Box shadow** (box-shadow) - Shadow effect for sub-menus. Controls `box-shadow` property for `.bricks-nav-menu .sub-menu` selector.

- **Transform** (transform) - Transform settings for sub-menus. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu` and `.bricks-nav-menu > li > .brx-megamenu` selectors.

- **Transform (Open)** (transform) - Transform settings for sub-menus when open. Controls `transform` property for `.bricks-nav-menu > li.open > .sub-menu` and `.bricks-nav-menu > li.open > .brx-megamenu` selectors.

#### Caret

- **Caret** (separator) - Separator for caret controls.

- **Size** (number with units) - Size of the caret (triangle pointer). Triggers re-render. Controls `border-width` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector.

- **Color** (color) - Color of the caret. Controls `border-bottom-color` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Transform** (transform) - Transform settings for the caret. Controls `transform` property for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

- **Position** (dimensions) - Position settings for the caret. Controls positioning properties for `.bricks-nav-menu > li > .sub-menu.caret::before` selector. Only available when caret size is set.

#### Item

- **Item** (separator) - Separator for submenu item controls.

- **Justify content** (justify-content) - Horizontal alignment of submenu items. Excludes space options. Controls `justify-content` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Padding** (spacing) - Padding inside submenu items. Controls `padding` property for `.bricks-nav-menu .sub-menu a` and `.bricks-nav-menu .sub-menu button` selectors.

- **Background** (background) - Background styling for submenu items. Controls `background` property for `.bricks-nav-menu .sub-menu .menu-item` selector.

- **Border** (border) - Border styling for submenu items. Controls `border` property for `.bricks-nav-menu .sub-menu > li` selector.

- **Typography** (typography) - Font settings for submenu items. Controls `font` property for `.bricks-nav-menu .sub-menu > li > a` and `.bricks-nav-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

#### Active State

- **Active** (separator) - Separator for submenu active state controls.

- **Active background** (background) - Background styling for active submenu items. Controls `background` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active border** (border) - Border styling for active submenu items. Controls `border` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle`, and ancestor selectors.

- **Active typography** (typography) - Typography settings for active submenu items. Controls `font` property for current submenu item selectors including `.bricks-nav-menu .sub-menu > .current-menu-item > a`, `.bricks-nav-menu .sub-menu > .current-menu-item > .brx-submenu-toggle > *`, and ancestor selectors.

#### Icon

- **Icon** (separator) - Separator for submenu icon controls.

- **Icon** (icon) - Icon for submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector.

- **Icon size** (number with units) - Size of submenu icons. Controls `height` and `width` properties for `.bricks-nav-menu .sub-menu .brx-submenu-toggle svg` selector, and `font-size` for `.bricks-nav-menu .sub-menu .brx-submenu-toggle i` selector.

- **Icon transform** (transform) - Transform settings for submenu icons. Controls `transform` property for `.bricks-nav-menu .sub-menu button > *` selector.

- **Icon transform (Open)** (transform) - Transform settings for submenu icons when open. Controls `transform` property for `.bricks-nav-menu .sub-menu button[aria-expanded="true"] > *` selector.

- **Icon typography** (typography) - Typography settings for submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle > a + button` selector.

- **Icon position** (select) - Position of submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around submenu toggle buttons. Controls `margin` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

- **Icon padding** (spacing) - Padding inside submenu toggle buttons. Controls `padding` property for `.bricks-nav-menu .sub-menu .brx-submenu-toggle button` selector.

### Mobile menu

- **Mobile menu** (separator) - Separator for mobile menu controls.

- **Hide at breakpoint** / **Show at breakpoint** (select) - Breakpoint at which to show/hide mobile menu. Options include all breakpoints plus "Always" and "Never". Default placeholder: "Mobile landscape". Triggers re-render.

- **Position** (select) - Position of mobile menu. Options: Right, Left. Default placeholder: "Left".

- **Top** (number with units) - Top position of mobile menu. Controls `top` property for `.bricks-mobile-menu-wrapper` selector.

- **Width** (number with units) - Width of mobile menu. Controls `width` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "300px".

- **Height** (number with units) - Height of mobile menu. Controls `height` property for `.bricks-mobile-menu-wrapper` selector.

- **Fade in** (checkbox) - Enable fade-in animation for mobile menu.

- **Vertical** (justify-content) - Vertical alignment of mobile menu content. Controls `justify-content` property for `.bricks-mobile-menu-wrapper` selector. Default placeholder: "Top".

- **Horizontal** (align-items) - Horizontal alignment of mobile menu content. Excludes stretch option. Controls `align-items` and `justify-content` properties for `.bricks-mobile-menu-wrapper` selector, and sets `width` to `auto` for `.bricks-mobile-menu-wrapper a`. Default placeholder: "Top".

- **Text align** (text-align) - Text alignment in mobile menu. Controls `text-align` property for `.bricks-mobile-menu-wrapper` selector.

- **Background** (background) - Background styling for mobile menu wrapper. Controls `background` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Background filters** (filters) - Background filters for mobile menu. Controls `filter` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Box shadow** (box-shadow) - Shadow effect for mobile menu. Controls `box-shadow` property for `.bricks-mobile-menu-wrapper:before` selector.

- **Overlay** (background) - Background styling for mobile menu overlay. Excludes video. Controls `background` property for `.bricks-mobile-menu-overlay` selector.

#### Top level

- **Top level** (separator) - Separator for mobile menu top-level controls.

- **Padding** (spacing) - Padding for top-level mobile menu items. Controls `padding` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors. Default placeholder: top 0, right 30, bottom 0, left 30.

- **Background** (color) - Background color for mobile menu items. Controls `background-color` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile menu items. Controls `background-color` property for `[aria-current="page"]` and `.bricks-mobile-menu > .current-menu-item > .brx-submenu-toggle` selectors.

- **Border** (border) - Border styling for mobile menu items. Controls `border` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle` selectors.

- **Border (Active)** (border) - Border styling for active mobile menu items. Controls `border` property for current menu item selectors.

- **Typography** (typography) - Font settings for mobile menu items. Excludes text-align. Controls `font` property for `.bricks-mobile-menu > li > a` and `.bricks-mobile-menu > li > .brx-submenu-toggle > *` selectors.

- **Typography (Active)** (typography) - Typography settings for active mobile menu items. Excludes text-align. Controls `font` property for various current menu item selectors.

#### Icon

- **Icon (Sub menu)** (icon) - Icon for mobile submenu toggles. Triggers re-render. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg` selector.

- **Close icon (Sub menu)** (icon) - Close icon for mobile submenu toggles. Triggers re-render. Only available when main icon is set. Controls SVG rendering for `.bricks-mobile-menu-wrapper .brx-submenu-toggle svg.close` selector.

- **Icon typography** (typography) - Typography settings for mobile submenu toggle buttons. Excludes font-family, font-weight, font-style, text-align, text-decoration, text-transform, and letter-spacing. Controls `font` property for `.bricks-mobile-menu > .menu-item-has-children .brx-submenu-toggle button` selector. Only available when icon is set.

- **Icon position** (select) - Position of mobile submenu icons. Options from icon position control options. Default placeholder: "Right".

- **Icon margin** (spacing) - Margin around mobile submenu toggle buttons. Controls `margin` property for `.bricks-mobile-menu .menu-item-has-children .brx-submenu-toggle button` selector.

#### Sub menu

- **Sub menu** (separator) - Separator for mobile submenu controls. Description: "Keep open while styling".

- **Padding** (spacing) - Padding for mobile submenu items. Controls `padding` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle > *` selectors.

- **Background** (color) - Background color for mobile submenu items. Controls `background-color` property for `.bricks-mobile-menu .sub-menu > .menu-item > a` and `.bricks-mobile-menu .sub-menu > .menu-item > .brx-submenu-toggle` selectors.

- **Background (Active)** (color) - Background color for active mobile submenu items. Controls `background-color` property for current submenu item selectors.

- **Border** (border) - Border styling for mobile submenu items. Controls `border` property for `.bricks-mobile-menu .sub-menu > .menu-item` selector.

- **Border (Active)** (border) - Border styling for active mobile submenu items. Controls `border` property for current submenu item selectors.

- **Typography** (typography) - Font settings for mobile submenu items. Controls `font` property for `.bricks-mobile-menu .sub-menu > li > a` and `.bricks-mobile-menu .sub-menu > li > .brx-submenu-toggle > *` selectors.

- **Active typography** (typography) - Typography settings for active mobile submenu items. Controls `font` property for current submenu item selectors.

#### Hamburger toggle

- **Hamburger toggle** (separator) - Separator for hamburger toggle controls.

- **aria-label** (text) - Accessibility label for hamburger toggle button. Default placeholder: "Open mobile menu".

- **Toggle width** (number with units) - Width of hamburger toggle bars. Controls `width` property for `.bricks-mobile-menu-toggle`, `.bricks-mobile-menu-toggle .bar-top`, `.bricks-mobile-menu-toggle .bar-center`, and `.bricks-mobile-menu-toggle .bar-bottom` selectors with `!important`.

- **Color** (color) - Color of hamburger toggle bars. Controls `color` property for `.bricks-mobile-menu-toggle` selector.

- **Hide close** (checkbox) - Hide hamburger toggle when mobile menu is open. Controls `display` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector (sets to `none` with `!important`).

- **Color close** (color) - Color of hamburger toggle when mobile menu is open. Controls `color` property for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector with `!important`.

- **Close position** (dimensions) - Position of hamburger toggle when mobile menu is open. Controls positioning properties for `&.show-mobile-menu .bricks-mobile-menu-toggle` selector.

### Mega menu

- **Enable** (checkbox) - Enable mega menu functionality.

- **CSS selector** (text) - CSS selector for mega menu positioning. Uses width & horizontal position of target node. Only available when mega menu is enabled.

- **Toggle on** (select) - How mega menus are triggered. Options: Click, Hover, Click or hover. Default placeholder: "Hover". Only available when mega menu is enabled.

- **Transition** (text) - Transition settings for mega menus. Supports dynamic data. Controls `transition` property for `.brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform** (transform) - Transform settings for mega menus. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu > .brx-megamenu` selector. Only available when mega menu is enabled.

- **Transform (Open)** (transform) - Transform settings for mega menus when open. Controls `transform` property for `.bricks-nav-menu > .brx-has-megamenu.open > .brx-megamenu` selector. Only available when mega menu is enabled.

### Multilevel

- **Enable** (checkbox) - Enable multilevel navigation functionality.

- **Back: Text** (text) - Text for back button in multilevel navigation. Only available when multilevel is enabled.

- **Back: Typography** (typography) - Typography settings for back button. Controls `font` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

- **Back: Background** (color) - Background color for back button. Controls `background-color` property for `.brx-multilevel-back` selector. Only available when multilevel is enabled.

> **Developer reference**
>
> See the [Nav Menu Schema](https://academy.bricksbuilder.io/developer/schema/elements/nav-menu/) for the full JSON schema of this element's settings and controls.

---

# Pagination

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/pagination/

*The Pagination element displays page navigation for query results with customizable styling.*

The Pagination element displays page navigation for query results with customizable styling.

## Settings

- **Query** (query-list) - Select which query this pagination controls.

- **Alignment** (justify-content) - Horizontal alignment of pagination links.

- **Height** (number with units) - Height of pagination buttons.

- **Width** (number with units) - Width of pagination buttons.

- **Spacing** (number with units) - Gap between pagination buttons. Default: 20px.

- **Background** (color) - Background color of pagination buttons.

- **Border** (border) - Border styling for pagination buttons.

- **Typography** (typography) - Font settings for pagination buttons.

### Current

- **Background** (color) - Background color of the current page button.

- **Border** (border) - Border styling for the current page button.

- **Typography** (typography) - Font settings for the current page button.

### Icons

- **Previous Icon** (icon) - Icon for the previous page button.

- **Next Icon** (icon) - Icon for the next page button.

### Miscellaneous

- **End Size** (number) - Number of page numbers shown at the start and end. Default: 1.

- **Mid Size** (number) - Number of page numbers shown on each side of current page. Default: 2.

> **Developer reference**
>
> See the [Pagination Schema](https://academy.bricksbuilder.io/developer/schema/elements/pagination/) for the full JSON schema of this element's settings and controls.

---

# Posts

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/posts/

*The Posts element displays a list or grid of posts with customizable query, layout, and styling options.*

The Posts element displays a list or grid of posts with customizable query, layout, and styling options.

## Settings

- **Query** (query) - Configure which posts to display with filters for post type, categories, tags, etc.

- **Link entire post** (checkbox) - Make the entire post card clickable.

### Layout

- **Layout** (select) - Display style. Options: `list`, `grid`, `masonry`, `metro`.

- **Columns** (number) - Number of columns in grid layout.

- **Spacing** (number with units) - Gap between posts.

- **Image height** (number with units) - Fixed height for images.

- **Image ratio** (text) - Aspect ratio for images.

### Image

- **Image size** (select) - Size of post images.

- **Image position** (select) - Position of images in post cards.

- **Image width** (number with units) - Custom image width.

- **Image height** (number with units) - Custom image height.

### Fields

- **Post title** (checkbox) - Display post titles.

- **Post title tag** (select) - HTML tag for titles.

- **Meta data** (checkbox) - Display post meta (date, author, etc.).

- **Meta data** (repeater) - Configure which meta fields to show.

- **Excerpt** (checkbox) - Display post excerpts.

- **Excerpt length** (number) - Number of words in excerpt.

- **Read more text** (text) - Custom read more link text.

### Content

- Typography and styling controls for post content.

### Overlay

- Overlay settings for post images.

### Filter

- **Filter** (checkbox) - Enable category/tag filtering.

- **Filter taxonomy** (select) - Which taxonomy to filter by.

- **Filter position** (select) - Where to display filters.

### Pagination

- **Pagination** (select) - Pagination type. Options: `none`, `numbers`, `load more`, `infinite scroll`.

- **Load more text** (text) - Text for load more button.

- **Loading text** (text) - Text shown while loading.

- **No more posts text** (text) - Text when no more posts available.

> **Developer reference**
>
> See the [Posts Schema](https://academy.bricksbuilder.io/developer/schema/elements/posts/) for the full JSON schema of this element's settings and controls.

---

# Search

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/search/

*Displays a search form with input field and submit button, or an icon that opens an overlay search.*

Displays a search form with input field and submit button, or an icon that opens an overlay search.

## Settings

- **Type** (select) - Choose between Input or Icon & Overlay. Default: Input.
- **aria-label** (text) - Accessibility label for overlay type. Required for overlay.
- **Action URL** (text) - URL where search form submits. Default: home URL.
- **Additional parameters** (repeater) - Hidden input fields added to search form.

### Input
- **Height** (number) - Input field height.
- **Width** (number) - Input field width.
- **Placeholder** (text) - Placeholder text. Default: "Search ...".
- **Placeholder color** (color) - Color of placeholder text.
- **Background color** (color) - Input background color.
- **Border** (border) - Input border settings.
- **Box shadow** (box-shadow) - Input box shadow.
- **Typography** (typography) - Input text typography.
- **Show label** (checkbox) - Display label above input. Default: false.
- **Label text** (text) - Text for input label.
- **Label typography** (typography) - Typography for input label.

### Button / Icon
- **aria-label** (text) - Accessibility label for button.
- **Text** (text) - Button text.
- **Icon** (icon) - Button icon.
- **Padding** (spacing) - Button padding.
- **Height** (number) - Button height.
- **Width** (number) - Button width.
- **Background color** (color) - Button background color.
- **Border** (border) - Button border settings.
- **Box shadow** (box-shadow) - Button box shadow.
- **Typography** (typography) - Button text typography.

### Overlay
- **Direction (Form)** (direction) - Flex direction of overlay form.
- **Gap** (number) - Gap between form elements.
- **Title** (text) - Overlay title. Default: "Search site".
- **Title tag** (text) - HTML tag for title. Default: h4.
- **Title typography** (typography) - Typography for overlay title.
- **Background** (background) - Overlay background.
- **Background: Overlay** (color) - Overlay background overlay color.
- **Button: Width** (number) - Overlay button width.
- **Button: Padding** (spacing) - Overlay button padding.
- **Button: Background color** (color) - Overlay button background color.
- **Button: Border** (border) - Overlay button border.
- **Button: Typography** (typography) - Overlay button typography.

> **Developer reference**
>
> See the [Search Schema](https://academy.bricksbuilder.io/developer/schema/elements/search/) for the full JSON schema of this element's settings and controls.

---

# Shortcode

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/shortcode/

*The Shortcode element executes WordPress shortcodes within your Bricks pages.*

The Shortcode element executes WordPress shortcodes within your Bricks pages.

## Settings

- **Shortcode** (textarea) - Enter the shortcode to execute, including the square brackets (e.g., `[gallery ids="72,73,74,75" columns="3"]`). Supports dynamic data.

- **Don't render in builder** (checkbox) - Show a placeholder instead of rendering the shortcode in the builder. Useful for shortcodes that slow down the builder or cause conflicts.

- **Placeholder: Width** (number with units) - Width of the placeholder when "Don't render in builder" is enabled.

- **Placeholder: Height** (number with units) - Height of the placeholder when "Don't render in builder" is enabled.

> **Developer reference**
>
> See the [Shortcode Schema](https://academy.bricksbuilder.io/developer/schema/elements/shortcode/) for the full JSON schema of this element's settings and controls.

---

# Sidebar

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/sidebar/

*Displays a WordPress sidebar with its widgets.*

Displays a WordPress sidebar with its widgets.

## Settings

- **Sidebar** (select) - Select which sidebar to display. Default: none.
- **Widget margin** (spacing) - Set the margin for widgets. Default: 0 0 40px 0.
- **Title typography** (typography) - Typography settings for widget titles.
- **Content typography** (typography) - Typography settings for widget content.
- **Search background color** (color) - Background color for search inputs in widgets.
- **Search border** (border) - Border settings for search inputs in widgets.

> **Developer reference**
>
> See the [Sidebar Schema](https://academy.bricksbuilder.io/developer/schema/elements/sidebar/) for the full JSON schema of this element's settings and controls.

---

# WordPress

Source: https://academy.bricksbuilder.io/builder/elements/wordpress/wordpress/

*The WordPress element displays various WordPress widgets with customizable styling.*

The WordPress element displays various WordPress widgets with customizable styling.

## Settings

- **Widget** (select) - Type of WordPress widget to display. Options: `archives`, `calendar`, `categories`, `pages`, `recent comments`, `recent posts`, `tag cloud`, `taxonomy`. Default: `posts`.

- **Icon** (icon) - Optional icon for the widget. Available for most widget types.

- **Icon typography** (typography) - Font settings for the icon.

### Widget-specific settings

- **Show count** (checkbox) - Display item counts. Available for archives, categories, tag cloud, taxonomy.

- **Sort by** (select) - Sort order for pages. Options: `page title`, `page date`, `page modified`, `page order`, `page ID`. Available for pages.

- **Include** (select) - Specific pages to include. Available for pages.

- **Exclude** (select) - Specific pages to exclude. Available for pages.

- **Number of comments** (number) - How many recent comments to show. Available for recent comments.

- **Number of posts** (number) - How many recent posts to show. Available for recent posts.

- **Direction** (direction) - Layout direction for posts. Available for recent posts.

- **Show date** (checkbox) - Display post dates. Available for recent posts.

- **Show featured image** (checkbox) - Display post thumbnails. Available for recent posts.

- **Featured image sizes** (select) - Size of featured images. Available for recent posts.

- **Featured image width** (text) - Custom width for images. Available for recent posts.

- **Featured image height** (text) - Custom height for images. Available for recent posts.

- **Post title typography** (typography) - Font settings for post titles. Available for recent posts.

- **Post meta typography** (typography) - Font settings for post meta. Available for recent posts.

- **Taxonomy** (select) - Which taxonomy to display. Available for tag cloud and taxonomy.

### Title

- **Title** (text) - Custom title for the widget.

- **HTML tag** (select) - HTML tag for the title. Options: `p`, `h1`-`h6`. Default: `h3`.

- **Border** (border) - Border styling for the title.

- **Typography** (typography) - Font settings for the title.

> **Developer reference**
>
> See the [WordPress Schema](https://academy.bricksbuilder.io/developer/schema/elements/wordpress/) for the full JSON schema of this element's settings and controls.
