# WooCommerce advanced modular elements

Source: https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/

*Set up and customize WooCommerce cart, checkout, account, and cart-dependent content with the Bricks 2.4 advanced modular workflow.*

Starting in Bricks 2.4, the WooCommerce integration includes an advanced modular workflow for the store areas that usually require the most setup: Cart, Checkout, and My Account.

WooCommerce v2 lets you build these system pages from editable Bricks elements, protected state containers, predefined structures, dynamic data, query loops, conditions, and interactions.

In the classic setup, screens such as empty cart, checkout payment, order received, account orders, account downloads, and password reset are handled through separate Bricks templates or WooCommerce endpoints. In the v2 setup, those screens live as states on the assigned WooCommerce page, so you can switch between them in the builder and edit them in one place.

![](https://academy.bricksbuilder.io/assets/woo-v2-state-filled-cart.png)

![](https://academy.bricksbuilder.io/assets/woo-v2-state-empty-cart.png)

> **Note**
>
> Advanced modular elements are experimental. Enable them under **Bricks > Settings > WooCommerce > Enable advanced modular elements**.
>
> ![](https://academy.bricksbuilder.io/assets/woo-advanced-modular-setting.png)

## What changes in v2

The v2 workflow is useful when you want more control over WooCommerce system pages without recreating WooCommerce logic from scratch.

- Build Cart, Checkout, and My Account pages with editable Bricks elements.
- Edit template or endpoint-style views as page states directly on the assigned WooCommerce page.
- Preview states such as filled/empty cart, checkout/pay/thank-you, and account orders/downloads while editing.
- Insert predefined complete blocks and smaller section blocks.
- Keep generated checkout and account address fields aligned with WooCommerce field definitions.
- Refresh cart-dependent content with the [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/).
- Use new WooCommerce v2 [query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/).
- Build [multistep checkout flows](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) with checkout step elements and interactions.

## When to use this workflow

Use the advanced modular workflow when you want a more guided setup and a single editing place for each WooCommerce page.

| Workflow | Best for |
| --- | --- |
| **Standard (v1)** | Existing sites that already use WooCommerce shortcode pages and Bricks WooCommerce templates, or stores that prefer separate templates for each WooCommerce screen. |
| **Advanced (v2)** | New or redesigned Cart, Checkout, and My Account pages where you want editable page states, generated structures, and v2 dynamic data directly on the assigned page. |

The classic template workflow remains supported. You can keep using the existing Cart, Empty Cart, Checkout, Thank You, Pay, Order Receipt, and Account template types.

For guided setup checks and presets, use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/). The wizard can set up classic WooCommerce layouts without advanced modular elements enabled. V2 setup types are disabled until advanced modular elements are enabled.

## Predefined structures

Cart, Checkout, and Account Page v2 states can generate complete starter layouts or smaller WooCommerce sections through **Insert a structure**.

![](https://academy.bricksbuilder.io/assets/woo-v2-insert-structure-cart.png)

Generated structures are site-aware where needed. For checkout, checkout account credentials, and account address forms, Bricks reads the WooCommerce field definitions that exist at generation time and turns them into editable Bricks form field elements. After generation, you can style, move, reorder, and place those fields like regular Bricks elements.

> **Note**
>
> Some WooCommerce v2 support elements are generated-only or context-specific. If you do not see a v2 support element in the regular Elements panel, create it through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/). After generation, the element appears in the Structure panel and can be edited inside its v2 state.

> **Note**
>
> Checkout fields can change after a layout is generated. For example, a plugin may add a VAT field, remove a company field, change labels and placeholders, or add an account field. Use field sync after installing, removing, or reconfiguring plugins that modify WooCommerce checkout or account address fields.

Field sync can report valid, missing, invalid, and duplicate generated fields. It can generate missing fields, remove invalid or duplicate generated fields, and update labels and placeholders from the current WooCommerce field data.

Checkout v2 and several Account v2 form states also include a **Floating label style** option for supported generated fields. Review third-party fields manually because plugin-generated fields can use different markup.

## V2 element groups

The main parent elements are:

- [Cart v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/)
- [Checkout v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/)
- [Account Page v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/)

V2 layouts can also include support elements that only make sense inside their matching WooCommerce state or generated structure.

Bricks 2.4 registers these advanced modular support elements:

| Area | Registered support elements |
| --- | --- |
| Cart v2 | Cart form, Cart quantity |
| Checkout v2 | Checkout steps navigation, Checkout step nav item, Checkout step, Shipping options, Payment options, WooCommerce form field, WooCommerce form submit, Checkout account fields, Checkout billing address, Checkout shipping address, Checkout order summary, Checkout place order |
| Account Page v2 | WooCommerce login form, Account register form, Account lost password form, Account reset password form, Account orders pagination, Account edit address form, Account edit account form, Account order withdrawal form (when Order Withdrawal is enabled) |
| Cart-dependent content | Dynamic fragment |

Some support elements are generated-only. Create them through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), then edit them from the Structure panel.

## Cart v2

The [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/) is added to the assigned Cart page. It contains two states:

- **Filled cart** for carts that contain products.
- **Empty cart** for carts with no products.

Use the **State** control while editing to switch the builder preview between these states. Each state can contain custom layouts and generated structures, such as the complete cart block or complete empty cart block.

## Checkout v2

The [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/) is added to the assigned Checkout page. It contains these states:

- Checkout
- Login required
- Pay
- Thank you
- Order receipt

Use the **State** control to design each checkout screen from one page. The checkout state can generate complete checkout structures or smaller sections such as billing fields, shipping fields, payment options, additional fields, order summary, and place order.

Checkout v2 also includes checkout field maintenance actions to help compare generated fields with the site's current WooCommerce checkout fields.

Generated billing and complete checkout structures include a **Checkout account fields** wrapper. It follows WooCommerce's guest checkout, account creation, username generation, and password setup settings. See [Checkout v2 account creation](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#account-creation-during-checkout) for the settings matrix and field sync behavior.

The **Login required** state is used when WooCommerce requires a customer to log in before viewing order-related checkout screens, such as pay, receipt, or thank you flows for a registered customer order.

For multistep layouts, see [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

## Account Page v2

The [Account Page v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/) is added to the assigned My Account page. It keeps the account navigation and endpoint content together.

It includes states for the common My Account endpoints:

- Dashboard
- Orders
- View order
- Downloads
- Addresses
- Edit address
- Edit account
- Payment methods
- Add payment method
- Login
- Lost password
- Lost password confirmation
- Reset password
- Order withdrawal (WooCommerce 11.1 or later, with Order Withdrawal enabled)

Use the **State** control to switch between endpoint previews while editing. Each state can contain generated starter content that you can customize in the builder.

## Dynamic Fragment

The [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) re-renders itself and its children after WooCommerce cart changes.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-mini-cart-structure-example.png)

Use it for cart-dependent content outside the main Cart page, such as:

- Custom mini cart content
- Free shipping progress
- Cart totals or subtotal displays

The element includes generated structures for **Mini cart** and **Free shipping progress**. For custom mini carts, wrap the mini cart in Dynamic fragment, add a child loop using the `wooCart` query type, and use cart tags such as `{woo_cart_product_name}`, `{woo_cart_quantity:value}`, `{woo_cart_subtotal}`, and `{woo_cart_remove_link:url}` inside the loop.

Keep the Dynamic fragment wrapper outside other query loops. The cart loop should be a child of the fragment.

Dynamic fragment is frontend-only. It can refresh when it is rendered from the header, content, or footer area, but it does not refresh inside query loop instances or component instances.

## Query loops, dynamic tags, conditions, and interactions

WooCommerce v2 adds query loops for applied coupons, fees, taxes, order items, order totals, order downloads, order customer notes, account orders, account order actions, account downloads, and account addresses.

It also adds dynamic tags for cart totals, free shipping progress, WooCommerce URLs, account addresses, order data, order items, order totals, order actions, downloads, and customer notes.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

Bricks 2.4 also adds WooCommerce conditions for shipping/order visibility and interactions for Dynamic fragment refreshes and checkout step changes.

## Existing WooCommerce templates

Bricks 2.4 also improves WooCommerce order-related template handling. Logged-out customers can still get Bricks layouts for Thank You, Order Receipt, and Order Pay flows when WooCommerce requires login for a non-guest order.

Classic templates and v2 page states can coexist on the same site, but each WooCommerce area should use one setup approach at a time to avoid confusion.

## Caveats

- Advanced modular elements must be enabled before you can add or edit v2 elements.
- V2 page rendering still follows WooCommerce page routing. Cart v2 and Checkout v2 render through the assigned WooCommerce cart and checkout pages.
- WooCommerce block content on assigned WooCommerce pages is not compatible with the v2 setup. The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can replace the page content with the matching v2 structure.
- Protected state elements are required children of their v2 parent elements. Do not remove them manually.
- Predefined structures are authored with the default Bricks breakpoint keys. Review responsive styling on sites with custom breakpoints.
- Third-party checkout fields may need manual review after generation or field sync.

---

# Cart (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/cart/

*Build and customize the WooCommerce cart in Bricks, including the classic shortcode/template workflow and the Cart v2 advanced modular workflow.*

## Overview

The Cart page is a special WooCommerce page, created by default during WooCommerce installation and assigned under **WooCommerce > Settings > Advanced**.

Starting in Bricks 2.4, you can choose between two Cart building workflows:

- **Cart v2 workflow**: Build the assigned Cart page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/).
- **Cart v1 workflow**: Keep the classic WooCommerce cart shortcode on the assigned Cart page and customize the output with separate Bricks Cart and Empty Cart templates.

Use Cart v2 for new builds or redesigns where you want to edit the filled and empty cart states in one place. Use Cart v1 for existing sites that already rely on the classic shortcode/template setup.

The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can check or create either workflow. The same v2 data tools can also be used with [Dynamic fragment](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) to build cart-dependent header content such as a custom mini cart.

## Cart v2 workflow

With advanced modular elements enabled, Cart v2 keeps the filled cart and empty cart screens as editable states on the assigned Cart page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose **Advanced (v2)** to replace the assigned Cart page content with the [Cart v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/) and generated state structure.

Cart v2 includes two states:

- **Filled cart** for carts that contain products.
- **Empty cart** for carts with no products.

Each state can generate starter content through **Insert a structure**. Use **Complete cart block** for the Filled cart state and **Complete empty cart block** for the Empty cart state. Generated structures are appended to the current state content, so you can insert a starter block and then move, style, or remove the generated elements.

Cart v2 is the recommended workflow when you want to design the Cart page directly, switch between filled and empty previews in one place, and use the v2 cart dynamic tags. The classic shortcode/template workflow below is still useful for existing sites that already use separate **WooCommerce - Cart** and **WooCommerce - Empty Cart** templates.

> **Note**
>
> Some Cart v2 support elements, such as the cart form wrapper and cart quantity controls, are generated-only or context-specific. If you cannot find a support element in the regular Elements panel, create it through **Insert a structure** or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), then edit it from the Structure panel.

Cart v2 layouts can use the **Cart contents** query loop and cart total tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`.

For the complete element reference, see [Cart v2](https://academy.bricksbuilder.io/builder/elements/woocommerce/cart-v2/). For all new WooCommerce v2 query loops and dynamic tags, see [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#cart-tags).

## Cart v1 workflow

The classic Cart workflow renders the WooCommerce `[woocommerce_cart]` shortcode on the assigned Cart page, then uses Bricks WooCommerce template types to customize the filled and empty cart screens.

> **Note**
>
> Remove the Gutenberg Cart block if it is located within your Cart Page. Instead, replace it with `[woocommerce_cart]` or use a Shortcode element if you edit the Cart page with Bricks.

![](https://academy.bricksbuilder.io/assets/remove-gutenberg-cart-blocks.png)

For the Cart v1 workflow, place the `[woocommerce_cart]` shortcode directly on the Cart page, or edit the Cart page with Bricks and use a Shortcode element with `[woocommerce_cart]` as its content. Bricks offers two template types to customize the cart:

- **WooCommerce - Cart**: Rendered when the cart contains products.
- **WooCommerce** - **Empty** **Cart**: Rendered when the cart is empty.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-templates-cart.png)

> **Note**
>
> The "Cart" and "Empty Cart" template types are only visible if you have the WooCommerce plugin installed and active. These templates are used inside the WooCommerce Cart shortcode logic and **they do not support template conditions (they are automatically rendered on the correct page)**.

By default, the cart in the Bricks theme will be shown as in the image below. You'll notice there are typically two different zones: the cart items table & the cart totals:

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-blocks.png)

If you want to customize this screen, you'll need to create a **WooCommerce - Cart** template type.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#cart-template-hooks) if you are using third-party plugins.

## Cart template {#cart-template}

You would set the **WooCommerce - Cart** template type to customize the Cart page (used when the cart contains products).

When opening this template with Bricks you'll see three new elements (specific for this template type):

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-elements.png)

<figcaption>

The specific Bricks elements to be used inside the "WooCommerce - Cart" template type

</figcaption>

### Cart items

Render the cart contents table. With this element, you'll be able to hide different parts of the table, style the table elements and the buttons, and hide the coupon input (so you could set it separately using the **Cart Coupon** element). For custom layout, check the section down below [Cart contents loop](#loop).

### Cart totals

Renders the cart totals zone. With this element, you could hide the cart cross-sells, style the totals table, and style the button.

### Cart Coupon

Render the coupon input. Use this element if you don't want to have the coupon input attached to the cart items table. With this element, you could style the input and the apply coupon button

## Empty cart template {#empty-cart-template}

You would set the **WooCommerce - Empty Cart** template type to customize how the cart page renders when the cart is empty.

By default, the empty cart shows a message and a button to return to the shop page.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-empty-cart-screen.png)

To customize this screen you need to create a **WooCommerce - Empty Cart** template type where you could place the required elements and configure as needed.

## Cart contents loop {#loop}

Bricks 1.4 introduced the **Cart Contents** query loop. This query loops through all visible products in the cart, enabling [Dynamic Data tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/#dynamic-data) for cart item data such as the product name (post title), product image (featured image), price, description, SKU, and more. This query loop is intended for cart-content layouts and is not restricted to the Cart page.

This allows you to build your own cart items widget. In Bricks 2.4, the same `wooCart` query loop is also useful inside a [Dynamic fragment](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/) for custom mini cart layouts that refresh after cart changes. Bricks 2.4 also adds separate title, item data, unit price, and savings output for custom cart rows.

### Build your own cart items element inside the cart page {#custom-cart-contents-loop}

By default, the list of products inside the cart appears displayed on a table layout. This happens in the default WooCommerce cart template or when using the Bricks Cart Items element.

To create a different layout for the cart products list, you'll need to add a container with a query loop, and set it to **Cart Contents**. Inside this container you may use the following dynamic data tags. The cart-specific tags were introduced in Bricks 1.5.3; product SKU and GTIN support inside this loop was added in Bricks 2.4.

> **Note**
>
> In order to make your custom cart loop work, you must add `woocommerce-cart-form__cart-item cart_item` CSS class on the loop itself and add `woocommerce-cart-form__contents` CSS class on the parent of looping div.

![](https://academy.bricksbuilder.io/assets/bricks-woo-cart-loop-css-class.png)

<figcaption>

CSS classes needed for WooCommerce JS works in cart page

</figcaption>

![](https://academy.bricksbuilder.io/assets/cart-contents-query-loop.png)

<figcaption>

Cart Contents query loop

</figcaption>

- `{woo_cart_product_name}` - Renders the linked product name together with cart item metadata and other legacy WooCommerce output.
- `{woo_cart_product_title}` - Renders the product title without cart item metadata. Use `:plain` to remove the link.
- **Cart item data** element - Renders variation attributes and compatible extension-provided item data separately from the product title.
- `{woo_cart_remove_link}` - Renders the anchor tag with the link to remove the product from the cart. By default, uses an "x" in the anchor content. Remember to add `product-remove` CSS class on the element that holding this dynamic tag. Do **NOT** use on Rich text element or additional `` tag will cause the AJAX not working.
- `{woo_product_price}` - This tag shows the product price. But when used inside of the Cart Contents loop it doesn't show the sale price.
- `{woo_cart_item_price}` - Renders the current unit price and includes WooCommerce sale-price markup when discounted. Use `:value` for the unformatted current unit price.
- `{woo_cart_item_save}` - Renders the product savings for the full cart item quantity. Use `:value` for the unformatted savings amount or `:percentage` for the numeric discount percentage.
- `{woo_product_sku}` - Returns the product SKU for the current cart item. (@since 2.4)
- `{woo_product_gtin}` - Returns the product GTIN for the current cart item. (@since 2.4)
- `{woo_cart_quantity}` - Renders the input field to add/remove the product quantity inside of the cart.
- `{woo_cart_quantity:value}` - Outputs the cart item quantity as text.
- `{woo_cart_subtotal}` - Renders the product price subtotal (price x quantity)
- `{woo_cart_update}` - Renders the update cart button and nonce. Use this outside the cart item loop but inside the cart form.

Bricks 2.4 also adds cart total and checkout tags such as `{woo_cart_items_count}`, `{woo_cart_order_subtotal}`, `{woo_cart_order_total}`, `{woo_cart_shipping_method}`, `{woo_free_shipping_remaining}`, and `{woo_free_shipping_progress}`. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#cart-totals-and-checkout-tags) for the complete list.

For a custom mini cart, wrap the mini cart in the [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/), add a child element with the **Cart contents** query loop, and place cart item tags inside that loop. Put total tags outside the loop but still inside the Dynamic fragment wrapper.

To complete this component, you have to wrap the products loop inside a `form` tag in order to use the product quantity input fields. To do that, wrap the container loop inside of another container (or div, or block) and set the HTML tag to `custom` and then insert `form` in the Custom tag input field.

![](https://academy.bricksbuilder.io/assets/bricks-container-form-cart-items.png)

<figcaption>

Wrap the products loop with a form container

</figcaption>

> **Note**
>
> **IMPORTANT**: Using Bricks 1.10.2+ you have explicitly allow the `form` HTML tag programmatically. Please follow the instructions at [/developer/hooks/filters/filter-bricks-allowed_html_tags/](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-allowed_html_tags/)

This form container, in order to work properly with the WooCommerce scripts needs the following configurations:

- Add the custom class `woocommerce-cart-form` (Style > CSS > CSS classes)
- Add custom attributes: method = `post` and action = `{post_url}`

![](https://academy.bricksbuilder.io/assets/example-form-container.png)

<figcaption>

Example Form container

</figcaption>

![](https://academy.bricksbuilder.io/assets/bricks-cart-form-attributes-2.png)

![](https://academy.bricksbuilder.io/assets/bricks-cart-form-attributes.png)

To add the update cart button, there's also another dynamic data tag `{woo_cart_update}` that you'll need to add inside of the form container (but outside of the loop). This will generate a button with the proper settings to update the cart.

---

# Checkout (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/checkout/

*Build and customize the WooCommerce checkout in Bricks, including the classic template workflow and the Checkout v2 advanced modular workflow.*

## Overview

The Checkout page is a special WooCommerce page, created by default during WooCommerce installation and assigned under **WooCommerce > Settings > Advanced**.

Starting in Bricks 2.4, you can choose between two Checkout building workflows:

- **Checkout v2 workflow**: Build the assigned Checkout page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/).
- **Checkout v1 workflow**: Keep the classic WooCommerce checkout shortcode on the assigned Checkout page and customize the output with separate Bricks Checkout, Thank You, Pay, and Order Receipt templates.

Use Checkout v2 for new builds or redesigns where you want to edit checkout, payment, thank-you, receipt, and login-required states in one place. Use Checkout v1 for existing sites that already rely on the classic shortcode/template setup.

The [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) can check or create either workflow.

## Checkout v2 workflow

With advanced modular elements enabled, Checkout v2 keeps the checkout, pay, thank-you, order receipt, and login-required screens as editable states on the assigned Checkout page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose:

- **Advanced (v2)** for a complete one-page checkout structure.
- **Advanced multistep (v2)** for a ready-made [multistep checkout structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

Checkout v2 can generate complete checkout blocks or smaller sections such as billing fields, shipping fields, payment options, order summary, and place order. Generated checkout fields are editable Bricks elements, so you can move, style, and reorder them after generation.

For existing Checkout v2 layouts, check that the payment section wrapper has the `brx-woo-payment-section` class. Add it manually if it is missing so the payment heading and methods hide together for free orders. Keep terms and Place order controls outside that wrapper. See [Checkout v2 payment section for free orders](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#payment-section-for-free-orders) for the steps.

Use Checkout v2 field sync after installing or reconfiguring plugins that change WooCommerce checkout fields. Field sync can find missing, invalid, and duplicate generated fields, generate missing fields, remove invalid or duplicate fields, and update labels or placeholders from WooCommerce.

Checkout v2 also adds query loops and dynamic tags for applied coupons, fees, taxes, order items, order totals, order downloads, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the complete reference.

The **Login required** state is used when WooCommerce requires a customer to log in before viewing order-related checkout screens. Bricks 2.4 also improves logged-out Thank you, Order receipt, and Order pay handling for non-guest orders.

## Checkout v1 workflow

The classic Checkout workflow renders the WooCommerce `[woocommerce_checkout]` shortcode on the assigned Checkout page, then uses Bricks WooCommerce template types to customize the checkout-related screens.

> **Note**
>
> Remove the Gutenberg Checkout block if it is located within your Checkout Page. Instead, replace it with `[woocommerce_checkout]` or use a Shortcode element if you edit the Checkout page with Bricks.

![](https://academy.bricksbuilder.io/assets/remove-gutenberg-checkout-block.png)

For the Checkout v1 workflow, place the `[woocommerce_checkout]` shortcode directly on the Checkout page, or edit the Checkout page with Bricks and use a Shortcode element with `[woocommerce_checkout]` as its content. Bricks offers four template types to customize the checkout workflow:

- WooCommerce - Checkout
- WooCommerce - Thank you
- WooCommerce - Pay
- WooCommerce - Order receipt

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-templates.png)

> **Note**
>
> The "WooCommerce - Checkout", "WooCommerce - Pay", "WooCommerce - Thank you", and "WooCommerce - Order receipt" template types are only visible if you have the WooCommerce plugin installed and active. These templates are used inside the WooCommerce checkout shortcode logic and **they do not support template conditions (they are automatically rendered on the correct page)**.

## Checkout template {#checkout-template}

The default checkout page consists of a two-columns layout: one column with the billing and shipping details form and another one with the order summary + a button to proceed with the order.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-screen.png)

<figcaption>

Bricks default WooCommerce default checkout screen

</figcaption>

Use the **WooCommerce - Checkout** template type to change the appearance of this first checkout screen.

When editing this template with Bricks you’ll see two new elements (specific to this template type):

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-elements.png)

### Checkout customer details

The checkout customer details element renders the billing and shipping details form.

You'll be able to remove/hide some of the non-required fields (e.g. Company name) and style the form fields.

### Checkout order review

The checkout order review element renders the order summary, the available payment methods, and the button to place the order. Using this element, you'll be able to style its different parts.

### Remove the checkout coupon form {#remove-coupon-form}

If you have enabled the use of coupons in the WooCommerce general settings you'll notice a blue coupon form on the top of the checkout form page. If you want to remove this form from the checkout page you may hide it using custom CSS or adding the following code to your child theme:

```php
remove_action( 'woocommerce_before_checkout_form', 'woocommerce_checkout_coupon_form', 10 );
```

### Checkout Coupon & Checkout Login elements {#checkout-coupon-login}

Starting at version 1.11.1 you have greater control over the location and design of the checkout coupon & login by enabling and using the following two checkout elements:

- [Checkout Coupon element](https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-coupon/)
- [Checkout Login element](https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login/)

## Thank you template {#thank-you-template}

After placing an order, and depending on the payment workflow, you'll get to the "Thank you" screen.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-checkout-thank-you.png)

<figcaption>

The Bricks default **Thank You** screen

</figcaption>

To style this screen, you'd create a Bricks template of type **WooCommerce - Thank you**. And insert the **Checkout Thank You** element to customize the thank you message, and modify the styles of the different components of the order details.

### Failed-order messages

The classic Checkout Thank You element supports WooCommerce's `woocommerce_thankyou_order_failed_text` filter. Checkout v2 uses `{woo_order_failed_text}` for the failed-order message in newly generated Thank you blocks.

To use the filtered message in an existing Checkout v2 layout:

1. Open the assigned Checkout page in Bricks and select its **Thank you** state.
2. Find the message element inside the **Order failed** block.
3. Replace its text with `{woo_order_failed_text}` and save.

Keep the block's conditions, payment retry link, styling, and hooks. See [Failed-order text](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#failed-order-text) for filter and preview behavior.

## Pay template {#pay-template}

For the situation where the visitor gets a link to pay for an unpaid order, there's a special checkout screen that contains the order summary, the available payment gateways, and the button to pay for the order.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-form-pay-default-471x1024.png)

<figcaption>

Default pay form screen with the representation of the Bricks elements

</figcaption>

If you would like to customize this screen you'd need to add a **WooCommerce - Pay** template type where you'll have access to two new elements: the **Checkout order table** and the **Checkout order payment** both with style controls to customize the look and feel.

## Order receipt {#order-receipt-template}

For the situation where the visitor gets a link to the unpaid order receipt, the checkout workflow triggers the `checkout/order-receipt.php` template, which by default will look like this:

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-order-receipt-default.png)

If you would like to customize this template you could add the Bricks **WooCommerce - Order receipt **template type and inside the builder, you'll have access to the order-specific Dynamic Data tags such as:

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-order-dynamic-data-tags.png)

`{woo_order_id}` - Returns the order id

`{woo_order_number}` - Returns the order number

`{woo_order_date}` - Returns the order date

`{woo_order_total}` - Returns the order total

`{woo_order_payment_title}` - Returns the order payment method name

`{woo_order_email}` - Returns the email address registered with the order

> **Note**
>
> **NOTE:** These Dynamic Data tags will also work inside the **WooCommerce - Thank you** template type.

Bricks 2.4 adds additional order tags and order-aware query loops for v2 layouts, including order items, totals, downloads, actions, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#order-tags).

---

# Create a custom mini cart with Dynamic fragment

Source: https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/

*Build a WooCommerce mini cart that refreshes after cart changes using Dynamic fragment, the Cart contents query loop, and cart dynamic tags.*

Use the Dynamic fragment element when you need cart-dependent content outside the main Cart page, such as a custom mini cart in a header Offcanvas, dropdown, or popup.

Dynamic fragment re-renders itself and its children after WooCommerce cart changes. For a mini cart, place the cart item loop and cart totals inside the fragment so product rows, quantities, subtotal, and buttons stay current after add-to-cart, remove, and quantity changes.

> **Note**
>
> Dynamic fragment requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Common setup

Mini carts are usually added to a header template and shown in an Offcanvas:

- The header contains the cart icon and cart count.
- The cart icon toggles the Offcanvas.
- The Offcanvas contains the generated mini cart structure.

Place the generated mini cart in a dropdown or popup for smaller layouts. Use an Offcanvas when you want more room for product rows, quantity controls, totals, and checkout actions.

## Create the Offcanvas mini cart

1. Open the header template or page where the mini cart should appear.
2. Add an **Offcanvas** element.
3. Inside the Offcanvas content area, add a **Dynamic fragment** element.
4. In the Dynamic fragment controls, go to **Insert a structure**.
5. Select **Mini cart**.
6. Click **Generate**.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart.png)

Bricks appends the generated structure inside the Dynamic fragment. It does not replace existing child elements.

## What Bricks generates

The generated Mini cart structure already includes the cart item layout, totals, and buttons. You do not need to add these manually unless you want to change the design or content.

Inside the Dynamic fragment, Bricks creates:

- A **Details wrapper** that contains the mini cart content.
- A **Cart loop** using the **Cart contents** query type.
- A cart row inside the loop with product image, product title, product price, product excerpt, item data, quantity control, remove icon, and line subtotal.
- An empty-cart message from the Cart contents query loop.
- A separate block after the Cart loop for the subtotal and action buttons.
- A condition on that subtotal/actions block so it only shows when the Cart loop has more than `0` results.
- **View Cart** and **Checkout** buttons using WooCommerce URL dynamic data.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-mini-cart-structure-example.png)

## What the generated structure uses

The generated cart row uses WooCommerce cart tags inside the **Cart contents** loop.

Common row tags:

| Tag or element | Use |
| --- | --- |
| `{featured_image}` | Product image. |
| `{woo_cart_product_title:plain}` | Product title as plain text, without variation metadata. |
| **Cart item data** | Variation attributes and compatible extension-provided item data. |
| `{woo_cart_quantity}` | Quantity input. |
| `{woo_cart_quantity:value}` | Quantity number as text. |
| `{woo_cart_subtotal}` | Line subtotal. |
| `{woo_cart_remove_link:url}` | Remove URL for a link or icon. |

For a custom row, use `{woo_cart_item_price}` when you need the formatted unit price with sale-price markup. `{woo_cart_item_save}` returns the quantity-aware product savings and can be used in a condition through `{woo_cart_item_save:value}`.

The subtotal and buttons are outside the Cart contents loop, but still inside the Dynamic fragment. The generated structure uses:

| Element              | Dynamic data                |
| -------------------- | --------------------------- |
| Subtotal amount      | `{woo_cart_order_subtotal}` |
| View Cart button URL | `{woo_url:cart}`            |
| Checkout button URL  | `{woo_url:checkout}`        |

The generated remove icon uses `{woo_cart_remove_link:url}` as its link URL. Keep the `product-remove` CSS class on the remove element so WooCommerce cart behavior can target it.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-subtotal-condition.png)

## Add a header cart icon

In the header template, add a second Dynamic fragment near the navigation for the cart icon and count. This fragment only needs to contain the small cart trigger, not the full mini cart.

Inside that header Dynamic fragment:

1. Add an Icon element and choose a cart icon.
2. Add a Text Basic element for the cart count.
3. Set the count text to `{woo_cart_items_count}`.
4. Position the count as a small badge on the cart icon.
5. Add an element condition to the count so it only shows when `{woo_cart_items_count}` is greater than `0`.
6. Add an interaction to the cart icon:
   - **Trigger**: Click
   - **Action**: Toggle offcanvas
   - **Offcanvas: CSS selector**: the target Offcanvas element ID, such as `#brxe-evudao`

Because the icon and count are inside Dynamic fragment, the count updates after cart changes. Keep the rest of the header outside the Dynamic fragment unless it also depends on cart data.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-header-mini-cart-trigger.png)

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-header-mini-cart-trigger-interaction.png)

## Open the Offcanvas after add to cart

You can open the mini cart Offcanvas when a product is added through AJAX.

On the Offcanvas element, add an interaction:

- **Trigger**: Added to cart
- **Action**: Toggle offcanvas
- **Offcanvas: CSS selector**: the Offcanvas element ID

Add a condition to the Offcanvas if you do not want this behavior on checkout. For example, show the Offcanvas only when the current URL does not contain `{woo_url:checkout}`.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-interaction.png)

Keep **Added to cart** for this interaction if the Offcanvas should toggle only after an addition. The [Bricks cart contents changed](https://academy.bricksbuilder.io/builder/features/interactions/#cart-contents-changed) trigger, available since Bricks 2.4, also runs after successful AJAX quantity changes and removals. Using it with **Toggle offcanvas** would toggle the mini cart during those updates too.

## Preview the refresh behavior

Dynamic fragment refreshes on the frontend after WooCommerce cart events such as add to cart, remove from cart, cart emptied, cart totals updated, checkout updated, and coupon apply/remove events.

The **Bricks dynamic fragments refreshed** interaction signals that fragment content has been replaced. It can run during initial synchronization or checkout recalculation without a cart item change. To show a custom “Cart updated” confirmation, use **Bricks cart contents changed**, which waits for a confirmed item change and the related UI updates to finish.

To test the mini cart:

1. Open the frontend page that contains the mini cart.
2. Add a product to the cart.
3. Confirm the mini cart updates without reloading the page.
4. Confirm the header cart count updates.
5. Click the cart icon and confirm the Offcanvas opens.
6. Remove the item or change quantity if your layout includes quantity controls.
7. Confirm the row count, subtotal, and buttons still render correctly.

![](https://academy.bricksbuilder.io/assets/dynamic-fragment-offcanvas-mini-cart-frontend-added-to-cart.png)

## Limits

- Dynamic fragment is frontend-only.
- Keep the Dynamic fragment wrapper outside other query loops. The Cart contents loop can be inside the fragment.
- Component instances are not supported.
- The fragment must render from the header, content, or footer area.
- Keep the fragment focused on cart-dependent content. Static header, menu, or layout elements do not need to be inside it.

## Related

- [Dynamic fragment element](https://academy.bricksbuilder.io/builder/elements/woocommerce/dynamic-fragment/)
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)

---

# Element: Checkout Coupon

Source: https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-coupon/

*Use the Bricks Checkout Coupon element inside WooCommerce checkout templates to render and style the coupon form.*

This Checkout coupon element, available @since 1.11.1, allows you to display the coupon field in various locations on the checkout page, making it easy for customers to apply discount codes during their purchase.

In previous versions, you couldn’t control the location of the checkout coupon. Additionally, styling options were limited, and adjustments required custom CSS. With this new, dedicated checkout coupon element you now have greater control over placement and design.

To use this element, first enable it under **`Bricks > Settings > WooCommerce`** by turning on **`Enable Bricks WooCommerce "Checkout coupon" element`**.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-coupon-setting.png)

> **Note**
>
> WooCommerce **`Enable the use of coupon codes`** must also be active under **WooCommerce > Settings > General**. When the Bricks Checkout Coupon element is enabled, the native WooCommerce checkout coupon form is removed, so add this element where you want the coupon form to appear.

> **Note**
>
> **Note:** This element is specifically designed for the Checkout page and will only work when placed on the **Checkout template** or the Checkout page itself, depending on your design requirements.

**Key Controls**

**Location:**

- By default, the **Checkout Coupon** element will appear where it’s placed in the layout. However, you can choose alternative positions, such as: Before Order Review Heading, After Order Review Heading, Before Payment
- Custom location settings only apply on the actual frontend (Checkout page). To ensure correct placement, add this element at the top of your Checkout template.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-coupon-element-controls.png)

![](https://academy.bricksbuilder.io/assets/element-location-example.png)

You can set the form to be toggle-able, hiding it by default and revealing it only when the toggle is clicked, for a cleaner layout.

---

# Creating dynamic WooCommerce archive pages

Source: https://academy.bricksbuilder.io/integrations/woocommerce/creating-dynamic-woocommerce-archive-pages/

*Create dynamic WooCommerce archive pages in Bricks with product queries, archive templates, and WooCommerce-specific dynamic data.*

By following this tutorial, you will be able to create a custom WooCommerce archive template that can show product categories and products.

At the same time you can also use the **Shop page display** option and **Category page display** option to control when to show categories or products.

![](https://academy.bricksbuilder.io/assets/woocommerce-product-catalog-options.png)

<figcaption>

Appearance > Customize > WooCommerce > Product Catalog

</figcaption>

![](https://academy.bricksbuilder.io/assets/dynamic-woo-archive-result.gif)

<figcaption>

Example result

</figcaption>

## Step 1: Products & Product Categories Preparation

Ensure your product categories created included subcategories as well. Add some products and assigned them to different product categories. Best if you can add some images for each category, we will output them in the template too.

![](https://academy.bricksbuilder.io/assets/woocommerce-data-prepared-1024x643.png)

## Step 2: Create WooCommerce Archive

Remember to select the correct template type (**WooCommerce - Product archive**)
If you are not familiar with the Bricks product archive, you can learn more about them [here](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/).

![](https://academy.bricksbuilder.io/assets/woo-archive-template.png)

Set the conditions for the template in Settings > Template Settings > Conditions so it will be applied when browsing the WooCommerce shop page and product categories & tags archive pages.

![](https://academy.bricksbuilder.io/assets/woo-archive-template-conditions.png)

You have to create 2 different query loops and we will use condition to dynamically render them in actual frontend. In below example, 2 sections were created. 1 for the product categories loop, and another 1 for the products loop.

![](https://academy.bricksbuilder.io/assets/2-sections-for-2-loops.png)

## Step 3: Product Categories Section

> **Note**
>
> Important: You must enable code execution when using echo dynamic tag. Please also ensure the function names added in the `bricks/code/echo_function_names` hook. Reference: [Code Review](https://academy.bricksbuilder.io/builder/features/code-review/)

To show product categories dynamically, you will need to use `get_queried_object_id()` PHP function on Parent field. Simply use Bricks echo dynamic tag and set `{echo:get_queried_object_id}` on Parent field like below.

![](https://academy.bricksbuilder.io/assets/product-categories-loop-settings.png)

Additionally, we will also use `woocommerce_get_loop_display_mode()` PHP function from WooCommerce to conditionally display this section.

`woocommerce_get_loop_display_mode()` will return either **products**, **subcategories**, or **both** (in string) based on your settings.

![](https://academy.bricksbuilder.io/assets/woocommerce_get_loop_display_mode.png)

Let's set the condition on the categories section like this:

Use `{echo:woocommerce_get_loop_display_mode}` != products

![](https://academy.bricksbuilder.io/assets/product-categories-section-condition-settings.png)

<figcaption>

This section will show if you are not selecting Show products

</figcaption>

Here are the settings for the looping images and text of my example.`{woo_product_cat_image}` to output the category image. `{term_name:link}` to output the category text with link

![](https://academy.bricksbuilder.io/assets/looping-term-settings.png)

## Step 4: Products Section

Query settings for products are pretty straightforward, just control how many posts per page will do.

![](https://academy.bricksbuilder.io/assets/products-loop-settings.png)

Let's set the condition on the products section like this:

Use `{echo:woocommerce_get_loop_display_mode}` != subcategories

![](https://academy.bricksbuilder.io/assets/products-condition-settings-01.png)

<figcaption>

Products section will shows if you are not selecting Show subcategories / Show categories

</figcaption>

Here are the settings for the looping product for your reference. (Only focus on the dynamic tag I used instead of the style)

![](https://academy.bricksbuilder.io/assets/looping-product-settings.png)

![](https://academy.bricksbuilder.io/assets/product-structure.png)

In case your product has multiple product categories checked, but you wish to output the first checked category only so the green box wouldn't be too long, you can use this simple custom function. Just replace the `{post_terms_product_cat}` with `{echo:product_first_category_name}`

```php
// Place in your child theme functions.php
// Returns the first category name of a product
function product_first_category_name() {
	global $product;
	if( $product && is_a( $product, 'WC_Product' ) ) {
		// Get the product categories
		$terms = get_the_terms( $product->get_id(), 'product_cat' );

		$cats = [];

		// Loop through the categories, and add them to the $cats array
		foreach( $terms as $term ) {
			$cats[] = $term->name;
		}

		// Return the first category
		if( ! empty($cats) ) {
			ob_start();
			echo $cats[0];
			return ob_get_clean();
		}
	}
}

```

## Check Result

Now, your shop page and product category pages should be able to work as expected. You can always control when to display the product categories section and products section via the settings in the WordPress dashboard under **Appearance > Customize > WooCommerce > Product Catalog**

![](https://academy.bricksbuilder.io/assets/dynamic-woo-archive-final-result.gif)

<figcaption>

Custom WooCommerce Archive Template

</figcaption>

---

# Element: Checkout Login

Source: https://academy.bricksbuilder.io/integrations/woocommerce/element-checkout-login/

*Use the Bricks Checkout Login element inside WooCommerce checkout templates to render and style the returning-customer login prompt.*

The Checkout Login element allows for a convenient login option directly on the checkout page, enabling returning customers to sign in before completing their purchase.

This feature becomes available once you've enabled **`Enable log-in during checkout`** under **`WooCommerce > Settings > Accounts & Privacy`**.

In previous versions, the placement of the checkout login form was fixed, and styling options were limited, requiring custom CSS for adjustments. Now, you can control both placement and appearance.

![](https://academy.bricksbuilder.io/assets/woocommerce-enable-login-during-checkout.png)

To use this element, activate it under **`Bricks > Settings > WooCommerce`** by toggling on **`Enable Bricks WooCommerce "Checkout login" element`**.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-login-setting.png)

> **Note**
>
> When the Bricks Checkout Login element is enabled, the native WooCommerce checkout login form is removed. Add this element where you want the returning-customer login prompt to appear. The WooCommerce **`Enable log-in during checkout`** setting must stay enabled; on the frontend, the element does not render for users who are already logged in.

> **Note**
>
> **Note:** This element is specifically intended for the Checkout page. Place it within the **Checkout template** or directly on the Checkout page, depending on your design needs.

**Key Controls**

**Location:**

- By default, the **Checkout Login** element will appear where it’s placed in the layout. However, you can choose alternative positions, such as: Before Order Review Heading, After Order Review Heading, Before Payment.
- Custom location settings only apply on the frontend. To ensure the login form appears in the desired location, add this element at the beginning of your Checkout template.

![](https://academy.bricksbuilder.io/assets/woocommerce-checkout-login-element-controls.png)

![](https://academy.bricksbuilder.io/assets/element-location-example.png)

You can set the form to be toggle-able, hiding it by default and revealing it only when the toggle is clicked, for a cleaner layout.

---

# How to Create Product Quick View with Bricks

Source: https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks/

*Create a WooCommerce product quick view in Bricks so shoppers can preview products without leaving the current listing page.*

## Step 1: Design a Popup Template for Quick View

Begin by designing the popup template that will be used for the Quick View functionality. Incorporate essential elements such as the Product Gallery, Product Rating, Product Price, and Add to Cart button.

Additionally, consider including a WooCommerce Notice element within the popup to display any notifications or confirmations directly to the user after an add-to-cart action.

It's crucial to implement the appropriate template hooks, similar to those used in a standard single product page. If you're unfamiliar with template hooks, we recommend reviewing [this article](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) for further guidance.

Below is an example of a WooCommerce Quick View Popup design:

![](https://academy.bricksbuilder.io/assets/woo-quick-view-design-example.png)

## Step 2: Configure Popup settings

To proceed, ensure that you have enabled the **"WooCommerce Quick View"** (@since 1.10.2) and **"Fetch content via AJAX"** options in **Settings > Template Settings > Popup**.

Enabling the **AJAX loader** will enhance the user experience by providing a smoother interaction with the Quick View Popup.

> **Note**
>
> Do not set any template condition for the popup template as we will embed it in the Products loop.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-popup-control.png)

## Step 3: Create a Product Query Loop

Proceed by creating a Product query loop on a new page or within your Shop page template. Insert the necessary elements according to your specific requirements.

Include the appropriate [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/) within the loop to ensure that any WooCommerce third-party plugins can effectively apply their logic within your Product query loop.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-query-loop-example.png)

## Step 4: Insert Popup template and Configure Interaction to Trigger Quick View Popup

Within the product query loop, insert a Template element and select the popup template you created in Step 1.

For a cleaner HTML structure, you may choose to enable the "Render without wrapper" option.

![](https://academy.bricksbuilder.io/assets/woo-quick-view-template-element-location.png)

![](https://academy.bricksbuilder.io/assets/woo-quick-view-popup-template-element.png)

Instead of using the Add to Cart element within the loop, utilize a Button element.

To ensure this button triggers the Quick View popup, configure the interaction as shown in the following screenshot:

![](https://academy.bricksbuilder.io/assets/woo-quick-view-button-interaction.png)

## Summary

By following these steps, you've successfully implemented a Quick View Popup feature using Bricks.

This enhancement not only improves the user experience by allowing visitors to quickly access product details without navigating away from the current page, but it also provides a seamless integration with WooCommerce.

Remember, fine-tuning the design and interaction settings can further optimize the effectiveness of the Quick View feature, ensuring it meets your specific needs and enhances your overall site performance.

---

# WooCommerce

Source: https://academy.bricksbuilder.io/integrations/woocommerce/

*Build WooCommerce shop, product, cart, checkout, account, and notice experiences with Bricks templates, elements, and integration guides.*

Bricks includes dedicated WooCommerce elements and template workflows so you can build the full storefront experience visually while still working with WooCommerce data and hooks.

## WooCommerce guides

- [WooCommerce Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/) for the main workflow
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) for the Bricks 2.4 Cart, Checkout, and My Account v2 workflow
- [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) for guided WooCommerce setup checks and presets
- [Checkout v2 multistep checkout](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/) for the multistep checkout workflow
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the v2 data reference
- [Product Archive](https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/) for shop and archive layouts
- [Single Product](https://academy.bricksbuilder.io/integrations/woocommerce/single-product/) for product detail pages
- [Product Quick View](https://academy.bricksbuilder.io/integrations/woocommerce/how-to-create-product-quick-view-with-bricks/) for quick-view popup workflows
- [Product Variation Swatches](https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches/) for color, image, and label swatches
- [Cart](https://academy.bricksbuilder.io/integrations/woocommerce/cart/) for cart layouts
- [Checkout](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/) for checkout flows
- [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) for account templates
- [WooCommerce Template Hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/) for hook-aware template work
- [WooCommerce Notices](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/) for notice styling and output

---

# Checkout v2 multistep checkout

Source: https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/

*Create and customize a multistep WooCommerce checkout with Checkout v2, checkout step elements, navigation, validation, and interactions.*

Checkout v2 can split the WooCommerce checkout form into multiple editable steps while keeping the native WooCommerce checkout form and submission flow in place.

Use this workflow when you want a guided checkout experience with separate sections for account login, customer details, shipping, extras, order review, and payment.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-frontend.png)

> **Note**
>
> Checkout v2 multistep checkout requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## Create a multistep checkout

You can create a multistep Checkout v2 layout in either of these ways:

- Go to [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/), choose the Checkout area, then select **Advanced multistep (v2)**.
- Edit the assigned Checkout page with Bricks, select the Checkout v2 **Checkout** state, choose **Complete checkout** under **Insert a structure**, enable **Generate as multistep**, then click **Generate**.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep.png)

The generated structure adds the checkout form sections, checkout step wrappers, step navigation, and next/back interactions for a complete starter flow.

## Generated structure

A multistep checkout uses these generated support elements:

- **Checkout steps navigation**: Displays the step navigation list.
- **Checkout step nav item**: One navigation item inside the steps navigation.
- **Checkout step**: Wraps the content for one checkout step.
- **Checkout account fields**, **Checkout billing address**, **Checkout shipping address**, **Payment options**, **Place order**, and other generated checkout support elements.

Some of these support elements are generated-only or context-specific. If you do not see them in the regular Elements panel, create them through **Insert a structure** instead. After generation, you can select, style, move, and edit them in the Structure panel like other Bricks elements.

![](https://academy.bricksbuilder.io/assets/checkout-v2-multistep-structure-example.png)

## Step order and navigation

Checkout step order follows the order of the **Checkout step** elements in the Structure panel. The first step is the initial step.

Navigation items mirror the checkout steps by order. If a checkout step is conditional, add the same condition to the matching navigation item so the visible navigation and visible steps stay aligned.

For the Shipping step, use **Checkout : Needs shipping** with a value of **Yes** on both the step and its navigation item. Use **Checkout : Needs shipping address** only on the **Ship to another address** control and shipping-address fields. A cart can still require shipping methods when WooCommerce is set to use the billing address for shipping.

Newly generated complete checkout structures include these conditions. If the layout was generated earlier or customized, review the Shipping step, navigation item, and address-field conditions manually because preset changes do not rewrite existing page content.

Each Checkout step has these controls:

- **Step ID**: Used by navigation, interactions, and direct step jumps.
- **Step label**: Used as the step label.
- **Allow direct entry**: Lets the customer jump to this step even if previous steps have not been reached.
- **Validate before leave**: Requires the current step to pass checkout field validation before moving forward.
- **Auto focus first field**: Focuses the first available field when the step becomes active.

Use stable, readable step IDs such as `customer-info`, `shipping`, `order-review`, or `payment` when you plan to target a step with interactions.

## Account Login step visibility

The generated complete multistep structure adds **Checkout : Login step needed** conditions to the Account Login navigation item, the Account Login step, and the Customer info Back button.

- Logged-out customer and **Enable log-in during checkout** enabled: Account Login is the first step, and Customer info includes a Back button.
- Logged-out customer and **Enable log-in during checkout** disabled: Account Login is not rendered. Customer info becomes the first step and has no Back button.
- Logged-in customer: Account Login and the Customer info Back button are not rendered.

If you build a custom multistep structure, apply the same **Checkout : Login step needed** condition to all three elements. Keeping the navigation item, step, and Back button under the same condition prevents an empty first step or a Back button with no previous step.

Account creation fields follow the WooCommerce checkout settings separately from the Account Login step. See [Checkout v2 account creation](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#account-creation-during-checkout).

## Step buttons and interactions

Generated multistep layouts use regular Bricks buttons with the **Checkout step** interaction action.

The action can:

- Move to the next step.
- Move to the previous step.
- Go to a specific step by Step ID.
- Go to a specific checkout field by field key or field ID, such as `billing_postcode`.
- Scroll the target step or field into view.

![](https://academy.bricksbuilder.io/assets/interaction-checkout-step-action.png)

Use the **Bricks checkout step changed** interaction trigger when you need to run another action after the active checkout step changes.

## Step numbers

For the navigation element, enable **Show step number** on **Checkout steps navigation** to render step numbers with CSS.

Inside custom headings or labels, use `{woo_checkout_current_step_number}` to output the current step number dynamically.

## Validation

Enable **Validate before leave** on a Checkout step when the customer must complete required fields before moving forward.

Backward navigation is always allowed. Forward navigation checks the current step only when **Validate before leave** is enabled.

Free orders do not require a payment method selection. Required terms still apply, and orders that require payment must have a selected payment method.

WooCommerce notices can still link to invalid fields. The checkout step script can route the customer to the step that contains the field and focus it.

## Payment section for free orders

The generated **Payment Options** wrapper uses `brx-woo-payment-section` to hide the payment heading and methods when the cart does not require payment. If this class is missing from an existing or custom layout, add it manually under **Style > CSS > CSS classes** on that wrapper, without a leading dot.

Keep the terms checkbox, step buttons, and **Place order** controls outside the wrapper. Apply the class to the payment section inside the Checkout step, rather than the entire step. See [Checkout v2 payment section for free orders](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#payment-section-for-free-orders) for the full steps.

## Recommended review

After generating the multistep layout:

- Test the checkout as a guest and as a logged-in customer.
- Test with **Enable log-in during checkout** both enabled and disabled.
- Test optional and required account creation with WooCommerce username and password generation enabled and disabled.
- Test products that require shipping and products that do not require shipping.
- Review conditional steps, such as account login and shipping.
- Confirm the final payment step contains the payment options, terms, and place order button.
- Test a zero-total order, then change shipping or remove a coupon so payment is required. Confirm the payment section reappears and the terms and Place order controls stay available in both cases.
- Test required field validation and WooCommerce notices.
- Review mobile spacing for the step navigation and buttons.

## Related docs

- [Checkout v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/)
- [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)
- [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/)

---

# Product Archive (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/product-archive-woocommerce/

*Build WooCommerce product archive templates in Bricks for shop, category, tag, and other archive views.*

> **Note**
>
> The template type "WooCommerce – Product Archive" is only visible if WooCommerce is installed & active.

Create a template of type "WooCommerce – Product Archive" in Bricks to design your product archive pages (product categories, tags, attributes, etc.).

To create this template, go to the Bricks templates screen and add a new template. Then select the template type **"WooCommerce – Product Archive"** from the top-right dropdown:

![](https://academy.bricksbuilder.io/assets/woocommerce-template-type-product-archive.png)

Click "Publish" or "Save Draft". Then "Edit with Bricks" to open the builder.

It is also possible to create/edit this and other templates in the Bricks editor interface by clicking on the Folders icon or pressing CMD / CTRL + SHIFT + L.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#product-archive-template-hooks) if you are using third-party plugins.

## Product Archive Elements {#elements}

![](https://academy.bricksbuilder.io/assets/woocommerc-product-archive-elements-580x1024.png)

### Archive title

There is no specific element to add a heading to the product archive.

To add a heading to this template you could use the Post Title element or add a Heading element with the `{archive_title}` tag.

### Breadcrumbs

Use the breadcrumbs element to output the navigation links from "Home", and higher level categories until the content displayed in the page.

This element uses the WooCommerce breadcrumbs default engine to generate each part of the breadcrumbs path.

### Products archive description

The products archive description will render the product category (or any other product taxonomy term) description.

If used in a template that renders the **Shop** page, it will output the page content (from the Gutenberg/blocks editor).

### Products

This is the main element to list products in a grid. You have controls to customize the style and layout, tweak the query, and select which content (fields) you want to show for each product.

This element interconnects with the **Products Filter**, **Products Pagination**, **Products Orderby** and the **Products Total Results** elements.

This means that the query results will be conditioned by the filters and the orderby conditions and it will also impact the pagination and the total results elements output.

The query used inside the products element to generate the grid of products will merge the query arguments from the element with the default WooCommerce query in the case the page rendered is the product archive or the product taxonomy archive (product category or product tag). This means that if you are seeing a certain product category archive page you only get a list of products from that category.

### Products filter

The products filter element allows you to add query filters to the page so the visitor could search/narrow down the list of products presented.

This element contains three filter types:

- **Taxonomy**: filter the list by one or multiple taxonomy terms.
- **Product attributes**: filter the list by product attributes like size, color or any other custom attribute used.
- **Others**: Special set of filters like a product **price dual-range slider**, a** stars rating** filter, a status **stock** filter or a simple **search** input. In this set, you will also find a **Reset filters** option which you would set to add a reset product filters button.

When using the taxonomy or product attributes filters, you may select different filter inputs, like a dropdown, a set of checkboxes, a radio list, a text list, or a box list.

### Products pagination

List of page links that allow the visitor to navigate through the different products' list pages.

### Products orderby

Adds a dropdown to the layout where the visitor could change the order of the products in the presented list. The default sort options are by popularity, by average rating, by latest, and by price (low to high and high to low). This list uses the WooCommerce default list and it can be extended using the WooCommerce hooks or third-party plugins.

### Products total results

Use this element to output the number of results returned by the current products query.

---

# Product Variation Swatches (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/product-variation-swatches/

*Integrate WooCommerce product variation swatches with Bricks and understand how they behave inside builder templates.*

Bricks 2.0 introduces **Product variation swatches**, giving you more control over how product attribute options (i.e. color, size, pattern) appear on the frontend.

Instead of dropdowns, you can now display your product variations as **color swatches, image buttons, or custom labels**, creating a more visual and intuitive shopping experience.

This feature integrates directly into the **Add to cart** element, letting you style variation swatches exactly how you want, without the need for extra plugins.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-before-1024x637.png)

<figcaption>

Before Product Variation Swatches

</figcaption>

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-after-1024x637.png)

<figcaption>

After Product Variation Swatches

</figcaption>

## Enable product variation swatches

To get started, go to **Bricks > Settings > WooCommerce > Enable product variation swatches**.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-enable.png)

Once enabled, you’ll be able to customize variation swatches directly from your product attribute settings.

## Assign a swatch type to product attributes

Go to **Products > Attributes**, and click "Edit" on an existing attribute (or create a new one).

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-edit-attribute.png)

You’ll see a new **Swatch type** setting with the following options:

- **None (default)**: Standard WooCommerce behavior (dropdowns)
- **Color**: Displays swatches using color values
- **Label**: Displays custom text labels for each term
- **Image**: Displays swatches using images from your media library

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-attribute-settings.png)

**Example:** Use the "Color" swatch type to show red and blue color boxes, or choose "Label" for size options like S, M, L.

### Set a fallback value (optional)

While editing the attribute, you can also set a **Fallback value**. This fallback will be used if a specific term doesn't have its own swatch value.

For **Image** swatches, Bricks checks images in this order:

1. The image assigned to the individual term.
2. The matching product variation image, if **Use product variation image** is enabled for the attribute.
3. The attribute fallback image.

## Assign swatch values to individual terms

Next, click **Configure terms** for the attribute you just edited.

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-configure-terms.png)

Then, click **Edit** on a specific term (like “Red” or “Large”).

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-edit-term.png)

For each term, you’ll see a new input that matches the swatch type:

- **Color** → Choose a color
- **Image** → Select or upload an image
- **Label** → Add custom text

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-term-settings.png)

These values are what will be shown on the frontend in the Add to cart element.

## Style swatches in the Add to cart element

Variation swatches are rendered inside the **Add to cart** element, as long as your product uses attributes with a swatch type.

To style them:

1. Select the **Add to cart** element (e.g in your single product template)
2. Open the new **Variation swatches** group in the element settings

![](https://academy.bricksbuilder.io/assets/bricks-woo-variation-swatches-add-to-cart.png)

From there, you can adjust the size, spacing, borders, active states, tooltips, and more.

## Unavailable variation options

Bricks follows the availability state of the hidden WooCommerce variation dropdown. When WooCommerce disables an option for the current attribute combination, Bricks adds the `disabled` class and `aria-disabled="true"` to the matching swatch.

You can style unavailable swatches with custom CSS:

```css
.bricks-variation-swatches li.disabled,
.bricks-variation-swatches li[aria-disabled="true"] {
  opacity: 0.45;
  text-decoration: line-through;
}
```

There is no separate Bricks setting that forces every out-of-stock option to be hidden or disabled. If a swatch does not receive the disabled state, check the product's stock settings and the exact variation combination in WooCommerce first.

That's it. With variation swatches, you can now turn standard variation dropdowns into polished, interactive product selectors, designed your way, directly in the Bricks builder.

---

# Single Product (WooCommerce)

Source: https://academy.bricksbuilder.io/integrations/woocommerce/single-product/

*Build WooCommerce single product templates in Bricks and customize the main product layout, data, and related elements.*

> **Note**
>
> The template type "WooCommerce - Single Product" is only visible if WooCommerce is installed & active.

Create a template of type "WooCommerce - Single product" in Bricks to design an individual layout for the single products page.

To create this template, go to the Bricks templates screen and add a new template. Then select the template type **"WooCommerce - Single Product"** from the top-right dropdown:

![](https://academy.bricksbuilder.io/assets/WooCommerce-Template-Type-Single-Product.png)

Click "Publish" or "Save Draft". Then "Edit with Bricks" to open the builder.

It is also possible to create/edit this and other templates in the Bricks editor interface by clicking on the Folders icon or pressing CMD / CTRL + SHIFT + L.

> **Note**
>
> Please remember to add [template hooks](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-template-hooks/#single-product-template-hooks) if you are using third-party plugins.

## Single Product Elements {#elements}

When editing a "Single Product" template you'll find the "Products" elements at the very top of the elements panel:

![](https://academy.bricksbuilder.io/assets/woocommerc-single-product-elements-379x1024.png)

### Product title

The product title renders the title of the product.

### Product gallery

The product gallery element displays the product images defined in the product image and in the product gallery meta boxes.

*To disable the image zoom or lightbox, go to "Bricks > Settings > WooCommerce > Single Product".*

### Product short description

Renders the content of the Product short description editor.

### Product price

Renders the product price. If the product is on sale, you could hide the regular price.

### Product stock

Displays the number of products in stock. You can replace the number of products in stock with a custom message for "in", "low", or "out of stock".

### Product meta

Use the product meta element to display product data like the SKU, the product categories or tags, or any other WooCommerce metadata. Use [Dynamic Data](https://academy.bricksbuilder.io/builder/dynamic-content/dynamic-data/) to pull the values.

### Product rating

Shows the product's rating on a scale of 1 to 5 stars.

### Product content

Renders the product's main content as written in the WordPress editor.

### Add to cart

This element adds an "Add to cart" button to trigger the addition of this element to the cart. With this element, you may style the product variations inputs, the product stock, the quantity input, and the look & feel of the button itself.

### Related products

Shows a list of products that have the same product categories and tags of the main product displayed in the page.

### Product reviews

Renders the product reviews and review form as a standalone element. Do not use the Product reviews element together with the Product tabs element on the same page, as Product tabs can also output reviews.

### Product additional information

Renders the list of product attributes. This information will also be part of the product tabs element.

### Product tabs

Renders a section with the default tabs: Description, Additional Information, and Reviews. Other tabs might be added by third-party plugins.

### Product up/cross-sells

The product up/cross-sells element renders linked product recommendations. You can set it to show **Up-sells**, **Cross-sells**, or **Cart Cross-sells** (by default, it lists up-sell products).

![](https://academy.bricksbuilder.io/assets/woocommerce-product-upsells.png)

<figcaption>

WooCommerce product editor screen - Linked Products

</figcaption>

---

# Woo Setup Wizard

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/

*Create or repair Bricks WooCommerce shop, product, cart, checkout, and account layouts with guided setup checks and presets.*

The Woo Setup Wizard helps you check, create, and repair the main WooCommerce layouts used by Bricks.

Go to **Bricks > Woo Setup Wizard** to review the current setup status for the store. The wizard checks the Shop, Single product, Cart, Checkout, and My Account areas, then shows the available setup actions for each area.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard.png)

The wizard is not dependent on **Enable advanced modular elements**. It can set up the classic WooCommerce builder workflow without that setting. Advanced v2 setup types may appear in the wizard, but they stay disabled until advanced modular elements are enabled under **Bricks > Settings > WooCommerce > Enable advanced modular elements**.

## When to use it

Use the wizard when you want Bricks to review the WooCommerce setup and create the expected page or template structure for you.

- Set up WooCommerce pages after installing Bricks on a new store.
- Repair a Cart, Checkout, or My Account page that is missing the expected Bricks content.
- Replace WooCommerce block content with Bricks page content.
- Create the classic Bricks WooCommerce templates for shop, product, cart, checkout, or account areas.
- Create Cart v2, Checkout v2, or Account Page v2 structures for the assigned WooCommerce pages.
- Review whether existing published WooCommerce templates may conflict with a selected setup.

> **Caution**
>
> The wizard can replace Bricks page content, clear WooCommerce block markup from the assigned page, switch the page editor mode to Bricks, create Bricks templates, or draft existing published WooCommerce templates for the same area. Review the setup summary before running an action on an existing store.

## Areas checked

The wizard checks these WooCommerce areas:

- **Shop**: shop page and product archive template setup.
- **Single product**: single product template setup.
- **Cart**: assigned Cart page, classic cart templates, and Cart v2 page structure.
- **Checkout**: assigned Checkout page, classic checkout templates, and Checkout v2 page structure.
- **My Account**: assigned My Account page, classic account templates, and Account Page v2 page structure.

## Setup types

Each area can offer one or more setup types, depending on the selected WooCommerce area and whether advanced modular elements are enabled.

| Area | Setup types |
| --- | --- |
| Shop | Standard (v1) |
| Single product | Standard (v1) |
| Cart | Standard (v1), Advanced (v2) |
| Checkout | Standard (v1), Advanced (v2), Advanced multistep (v2) |
| My Account | Standard (v1), Advanced (v2) |

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-advanced-off.png)

**Standard (v1)** creates or repairs the classic Bricks WooCommerce workflow. This setup uses the assigned WooCommerce page together with the traditional Bricks WooCommerce template types or shortcode-based page content.

**Advanced (v2)** replaces the assigned WooCommerce page content with the matching v2 parent element and generated state structure. Use it for Cart, Checkout, and My Account pages when you want to edit related WooCommerce screens as states on one page.

**Advanced multistep (v2)** is available for Checkout. It creates a Checkout v2 page with a ready-made [multistep checkout structure](https://academy.bricksbuilder.io/integrations/woocommerce/multistep-checkout-v2/).

## Status checks

The wizard reports missing, incomplete, or incompatible setup details before you run an action.

Common checks include:

- Required WooCommerce page is not assigned.
- Assigned WooCommerce page was deleted.
- Assigned page is still edited with the WordPress editor instead of Bricks.
- Assigned page contains WooCommerce block content.
- Required v2 parent element is missing from the assigned page.
- Required v2 states are missing. My Account v2 includes Order withdrawal only when the WooCommerce feature is enabled.
- Required v2 state elements are empty.
- Existing published WooCommerce templates may conflict with the selected setup.
- Classic setup is missing expected WooCommerce shortcodes or template types.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-errors.png)

The wizard does not create or assign missing WooCommerce pages. If a page is not assigned, assign it first in the WooCommerce settings, then return to **Bricks > Woo Setup Wizard**.

## What setup can change

Depending on the selected area and setup type, the wizard can:

- Write Bricks page content to the assigned WooCommerce page.
- Clear WordPress `post_content` when it contains WooCommerce block markup.
- Set the assigned page editor mode to Bricks.
- Create Bricks WooCommerce templates from presets.
- Draft existing published WooCommerce templates for the same template type when they would conflict.
- Generate external CSS files when file-based CSS generation is enabled.
- Ask for overwrite confirmation when the target page already contains Bricks data.

![](https://academy.bricksbuilder.io/assets/woo-setup-wizard-confirmation.png)

## Before running setup

Review the setup summary before confirming any action.

- Confirm the correct WooCommerce pages are assigned in the WooCommerce settings.
- Duplicate or export important pages and templates on existing stores.
- Check whether the selected setup edits pages, templates, or both.
- Review whether existing WooCommerce templates will be drafted.
- If the site uses custom breakpoints, review responsive styles after setup. Presets are authored with the default Bricks breakpoint keys, such as `mobile_landscape` and `mobile_portrait`.

## After setup

Open the generated page or template in Bricks and review the result.

- For classic layouts, confirm the expected WooCommerce template types and shortcodes are in place.
- For Cart v2, review the Filled cart and Empty cart states.
- For Checkout v2, review Checkout, Login required, Pay, Thank you, and Order receipt states.
- For Advanced multistep Checkout v2, test the checkout step navigation and interactions.
- For Account Page v2, review the account navigation, login, password, address, order, download, and edit account states. Include Order withdrawal when enabled.
- Test the live Cart, Checkout, and My Account flows with WooCommerce products and customer sessions.

## Related docs

- [WooCommerce Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-builder/)
- [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/)
- [Cart](https://academy.bricksbuilder.io/integrations/woocommerce/cart/)
- [Checkout](https://academy.bricksbuilder.io/integrations/woocommerce/checkout/)
- [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/)

---

# WooCommerce Account Builder

Source: https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/

*Customize WooCommerce account-area screens in Bricks with the classic Account builder templates or the Account Page v2 advanced modular workflow.*

Bricks 1.9 introduces the My Account builder, which lets you customize the account area of your WooCommerce site.

This includes the My Account page (logged-in), the account login/register/lost & reset password pages (shown when not logged-in), and all My Account endpoints (e.g., Orders, Downloads, etc.).

> **Note**
>
> Starting in Bricks 2.4, you can also build the My Account page directly with [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) and the [Account Page v2 element](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/). The classic account template workflow below is still supported.

> **Note**
>
> **IMPORTANT:** In order to ensure that all your customizations to the WooCommerce My Account templates are properly applied, it is imperative that you complete the "[My Account Page (logged in)](#my-account-page)" step.

## Account Page v2 workflow

With advanced modular elements enabled, Account Page v2 keeps the account wrapper, navigation, login state, password states, and account endpoint states together on the assigned My Account page.

Use the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) and choose **Advanced (v2)** to replace the assigned My Account page content with the Account Page v2 element and generated state structure.

Account Page v2 includes states for:

- Dashboard
- Orders
- View order
- Downloads
- Addresses
- Edit address
- Edit account
- Payment methods
- Add payment method
- Login
- Lost password
- Lost password confirmation
- Reset password
- Order withdrawal (WooCommerce 11.1 or later, with Order Withdrawal enabled)

Each state can generate a complete starter block through **Insert a structure**. Address and account forms use editable Bricks form field elements, so you can style and reorder them after generation.

The Account edit-address state has its own field sync because WooCommerce account address editing and checkout use different field contexts. Use it after plugins or WooCommerce settings change address fields.

Account Page v2 also adds query loops and dynamic tags for account orders, order actions, account downloads, account addresses, order data, downloads, and customer notes. See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags).

### Endpoints added by plugins

Account Page v2 provides editable states for the built-in WooCommerce account routes listed above. An endpoint registered by another plugin does not appear automatically as an additional editable state in the builder.

WooCommerce account endpoints are routes on the assigned My Account page, not separate WordPress pages. A plugin that registers an endpoint and its output callback correctly can still render its content through WooCommerce on that page, but Bricks does not provide a dedicated Account Page v2 state for designing that endpoint.

If a plugin endpoint is blank on the frontend, temporarily test the My Account page with WooCommerce's default account output or without the Account Page v2 element. If it remains blank, check the plugin's endpoint registration. If it works only without Account Page v2, include the plugin name and endpoint slug when contacting Bricks support.

## My Account Page (logged in) {#my-account-page}

To design your My Account page (navigation + content wrapper), **please edit your "My Account" page directly**. You'll find a dedicated "Account Page" element that you can add and adjust its settings to your liking.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-my-account-page-1.png)

<figcaption>

Custom My Account page using the "Account - Page" element

</figcaption>

> **Note**
>
> **IMPORTANT:** If you have the *"Enable Bricks WooCommerce "Notice" element"* Bricks setting enabled, please make sure that you have added the "Notice" element to your account page or to all account templates individually. So the notifications when submitting the account forms (e.g., address, reset password, etc.) are displayed.

Starting in Bricks 2.4, the classic **Account - Page** element supports WooCommerce's native Order Withdrawal flow for guests and logged-in customers when the WooCommerce feature is enabled; use the [Account Page v2 Order withdrawal state](https://academy.bricksbuilder.io/builder/elements/woocommerce/account-page-v2/#order-withdrawal) to customize its layout.

## Account - Login / Register {#my-account-login-register}

The login form is displayed when a not-logged-in visitor views the My Account page. And the registration form, if you have the *"Allow customers to create an account on the "My account" page"* WooCommerce setting enabled.

You can design your account login/registration layout by creating a new template type "WooCommerce - Account - Login".

When editing this template, you'll find dedicated elements for the **"Account - Login form"** & **"Account - Register form"** as shown in the screenshot below:

You should also check the **Account creation** settings located at *WooCommerce > Settings > Accounts & Privacy* section to control what form to be displayed via **Account - Register form** element.

![](https://academy.bricksbuilder.io/assets/woocommerce-account-creation-settings.png)

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-account-login-register.png)

<figcaption>

Custom account login/register template

</figcaption>

> **Note**
>
> **IMPORTANT:** Ensure you have inserted a Basic Text element with `{do_action:woocommerce_before_customer_login_form}` before your Login and Register form. And another Basic Text element with `{do_action:woocommerce_after_customer_login_form}` after the forms.

![](https://academy.bricksbuilder.io/assets/woocommerce-do-action-account-login.png)

<figcaption>

Example do_action location. Before and after the login/register forms.

</figcaption>

## Account - Lost / reset password {#my-account-lost-reset-password}

The WooCommerce account builder in Bricks also provides the following dedicated templates and elements for the lost & reset password pages:

| **Account page** | **Template type** | **Elements** |
| --- | --- | --- |
| Lost password | WooCommerce - Account - Lost password | Account - Lost password |
| Lost password confirmation | WooCommerce - Account - Lost password (Confirmation) | Displayed after submitting the lost password form. No special elements.<br /><br />Example:<br />*A password reset email has been sent to the email address on file for your account, but may take several minutes to show up in your inbox. Please wait at least 10 minutes before attempting another reset.* |
| Reset password | WooCommerce - Account - Reset password | Account - Reset password |

## Templates for specific account endpoints {#my-account-endpoints}

Designing the account content area for individual account endpoints (Orders, Downloads, etc.) is possible by creating templates of the corresponding template type.

In the example below, we created a "WooCommerce - Account - Orders" template, to which we then added the "Account - Orders" that we styled a bit.

![](https://academy.bricksbuilder.io/assets/bricks-woocommerce-account-orders-1024x384.png)

> **Note**
>
> When editing the template for an account endpoint (Orders, Downloads, etc.), the drag & drop area is located inside the account content area. Offering a better preview in the builder than just rendering an empty canvas without the account navigation.

The process of creating those account endpoint templates is the same for all other WooCommerce account template types.

## Account template types & elements

| **Template type** | **Endpoint** | **Element** |
| --- | --- | --- |
| WooCommerce - Account - Dashboard | `/` | - |
| WooCommerce - Account - Orders | `orders/` | Account - Orders |
| WooCommerce - Account - View order | `view-order/{order_id}/` | Account - View order |
| WooCommerce - Account - Downloads | `downloads/` | Account - Downloads |
| WooCommerce - Account - Payment methods | `payment-methods/` | Account - Payment methods |
| WooCommerce - Account - Add payment method | `add-payment-method/` | Account - Add payment method |
| WooCommerce - Account - Addresses | `edit-address/` | Account - Addresses |
| WooCommerce - Account - Edit address | `edit-address/billing/`<br />`edit-address/shipping/` | Account - Edit address |
| WooCommerce - Account - Edit account | `edit-account/` | Account - Edit account |
