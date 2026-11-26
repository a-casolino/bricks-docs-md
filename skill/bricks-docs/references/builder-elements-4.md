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

## Customize the Checkout state

https://youtu.be/xD0ihyBFErQ

Everything inside the Checkout state is a regular Bricks element. Each form field is its own **WooCommerce form field** element with **Label**, **Hide label**, and **Placeholder** settings, so you can move, group, and lay out fields like any other elements.

The layout from the Woo Setup Wizard also uses the Bricks **Notice**, **Checkout coupon**, and **Checkout login** elements. Enable them under **Bricks > Settings > WooCommerce**, next to **Enable advanced modular elements**.

Common changes after generating the checkout:

- **Collapse the login form:** Select **Checkout login** and enable **Toggleable form**. Returning customers then see a single "Returning customer? Click here to login" line that opens the form.
- **Remove a field:** Select the **Checkout** state and choose the field under **Remove unwanted fields** > **Billing** or **Shipping**. This removes it from WooCommerce's checkout fields. Delete the field's element in the Structure panel as well. In Bricks 2.4.3, the element otherwise still renders as an optional field, and WooCommerce ignores anything customers type into it.
- **Reorder fields:** Drag field elements in the Structure panel. The generated layout places **Billing: Apartment** after the email field, so you may want to move it below **Billing: Street address**.
- **Style all fields at once:** Use the **Style** groups on the **Checkout** state, such as **Input / Textarea / Select** for borders and corners, instead of styling each field. The searchable Country and State dropdowns have their own **Select2** groups, so give them the same border.
- **Style the button:** Select **Checkout place order** to set the button's background, text color, and border radius.
- **Show the order number:** Click **Switch**, choose the **Thank you** state, and add `{woo_order_number}` to its heading, for example `Thank you! Order #{woo_order_number} is confirmed`. The builder previews a sample order, so the number only appears on real orders.

The builder preview of the Checkout state uses a sample cart and shows sample notices and hook placeholders such as `{do_action:woocommerce_...}`. They do not appear on the frontend. Test the result on the frontend with a real cart.

### Floating labels

The **Floating label** style (Checkout state > **Style**) places field labels inside the fields and moves them up when a field has a value. The Woo Setup Wizard enables it for the Checkout and Login required states. Keep the field labels visible for it to work.

In Bricks 2.4.3, when the store sells to a single country, the Country field renders as a plain select and its floating label overlaps the selected country. Until this is fixed, add this rule under **Bricks > Settings > Custom code > Custom CSS**:

```css
.bricks-floating-label .brxe-woocommerce-form-field:has(> .woocommerce-input-wrapper > select:not(.select2-hidden-accessible)) > label {
  top: 10px;
  transform: scale(.75);
  transform-origin: left top;
}
```

## Shipping option labels

> **Note**
>
> The customized shipping-label behavior and Bricks filters described below are available since Bricks 2.4.5.

The **Shipping options** element displays the available shipping methods for each package. An ordinary rate shows the method name as its primary label and the formatted price or **Free** as its secondary label.

When a plugin or custom callback changes `woocommerce_cart_shipping_method_full_label` and supplies usable label content, Bricks displays that complete label once as the primary label. Safe HTML is preserved. For example, a customized label containing **Pickup points: $19.90** appears once, without an additional **Pickup points** name or separate price. If the customization contains no text or meaningful image alternative text, Bricks keeps the method name as the primary label.

Select **Shipping options** in the Structure panel to style its labels:

- **Label** controls style the primary label, including a customized full label.
- **Secondary label** controls style the separate price or other secondary content, when present.

Review existing checkout layouts that styled a plugin's full label through **Secondary label**. The customized full label now uses **Label** styles.

Developers can customize each label independently with [`bricks/woocommerce/shipping_options/primary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-primary_label/) and [`bricks/woocommerce/shipping_options/secondary_label`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-woocommerce-shipping_options-secondary_label/). Both receive the label HTML, the calculated `WC_Shipping_Rate`, and the Shipping options element instance. These filters change the displayed labels without changing the calculated shipping charge or selected rate.

The secondary filter receives an empty string when a customized full label supplies the primary label. Return separate secondary content if needed, or an empty string to omit it. Bricks only adds the input's `aria-describedby` link when a secondary label is rendered.

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

Use these after changing WooCommerce checkout fields, for example the **Company name**, **Address line 2**, or **Phone** field in **Appearance > Customize > WooCommerce > Checkout**, or after installing or removing plugins that change checkout fields. The layout does not follow those changes by itself, because every field is its own element.

https://youtu.be/caoSy6gGefE

Select the **Checkout** state and click **Check checkout fields**. Bricks compares the field elements in the state with the checkout fields WooCommerce currently uses and lists them as missing, invalid, or duplicate. Invalid field elements are also marked in red in the Structure panel. The **Generate missing fields**, **Remove invalid fields**, and **Remove duplicate fields** buttons appear once the check has found something to fix.

- **Generate missing fields** adds an element for each missing field. Billing, shipping, and additional fields are added at the top of the Checkout state, not inside their sections. Drag each one into place in the Structure panel, for example below **Billing: Last name**. A shipping field left at the top also shows when the customer does not ship to a different address.
- **Remove invalid fields** deletes field elements that WooCommerce no longer uses, such as Phone after the field is set to **Hidden**.
- **Remove duplicate fields** deletes extra elements for the same field.

New elements copy the field's current label and placeholder from WooCommerce. Field sync does not update the labels or placeholders of existing field elements.

In Bricks 2.4.3, a removed field can stay visible in the builder canvas even though the Structure panel no longer lists it. Save and reload the builder; the canvas then matches the frontend.

The audit includes WooCommerce's `account` field section. Missing account fields are inserted into the **Checkout account fields** wrapper.

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

https://youtu.be/Q6wYRAvVN0Y

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

- Use Dynamic fragment for cart-dependent content outside the main Cart page, such as a [custom mini cart](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/), free shipping progress, or cart totals.
- Keep the fragment focused on content that needs to refresh after add-to-cart, remove-from-cart, or quantity changes.
- Keep the Dynamic fragment wrapper outside other query loops. A cart loop can be placed inside the fragment.

## Free shipping progress

The **Free shipping progress** structure adds a Progress Bar that shows how much more the cart needs for free shipping. Place the Dynamic fragment where shoppers see it on every page, for example a bar at the top of the header template, so it updates as products are added.

- **Minimum amount:** Bricks reads it from WooCommerce. It is the **Minimum order amount** of the **Free shipping** method in the shipping zone that matches the cart, with **Free shipping requires** set to a minimum order amount (alone or combined with a coupon). Change it in **WooCommerce > Settings > Shipping**, not in Bricks. If several free shipping methods match, Bricks uses the one with the smallest remaining amount.
- **Cart amount:** the cart subtotal minus coupon discounts, unless **Apply minimum order rule before coupon discount** is enabled on the free shipping method.
- **Label:** `Add {woo_free_shipping_remaining} more for free shipping`.
- **Value:** `{woo_free_shipping_progress:value}`, a number from 0 to 100 (the percentage of the minimum the cart has reached).
- **Conditions:** the bar only renders while a minimum exists (`{woo_free_shipping_min_amount:value}` is not 0) and the cart is below it (`{woo_free_shipping_progress:value}` is less than 100).

Once the cart reaches the minimum, the bar is hidden. The structure has no message for that state. To show one, add an element such as Basic Text inside the same Dynamic fragment and give it the condition **Dynamic data** `{woo_free_shipping_progress:value}` `==` `100`.

![Builder showing a Dynamic fragment in the header template with the generated Free shipping progress bar and a Basic Text "Your order ships free" with a condition that shows it when the free shipping progress equals 100.](https://academy.bricksbuilder.io/assets/dynamic-fragment-free-shipping-reached-condition.webp)

The Builder canvas previews a sample cart, so the bar can show "Add $0.00 more" and the conditions are not applied there. Check the real amounts on the frontend with products in the cart.

## Custom mini cart

For a mini cart, add a Dynamic fragment inside an Offcanvas in the header template and generate the **Mini cart** structure. A second Dynamic fragment in the header holds the cart icon and item count, so the count updates too. [Create a custom mini cart with Dynamic fragment](https://academy.bricksbuilder.io/integrations/woocommerce/create-custom-mini-cart-dynamic-fragment/) walks through the full setup, including the interactions that open the panel.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/) for the cart tags you can use inside the fragment.

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

Since Bricks 2.5, use a Notice element in a non-AJAX popup with the [Coupon error interaction](https://academy.bricksbuilder.io/builder/features/interactions/#coupon-error) to show the returned coupon error. Follow the [WooCommerce Notice setup](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-notices/#woocommerce-notice-element) before placing the element.

---

# Mini cart

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/mini-cart/

*Displays a mini cart icon with cart count and dropdown cart details.*

Displays a mini cart icon with cart count and dropdown cart details.

## Settings

- **Icon** (icon) - Cart icon. Default: ti-shopping-cart.
- **Icon typography** (typography) - Typography for cart icon. Only available when Icon is set.
- **Open on add to cart (AJAX)** (checkbox) - Open mini cart when products are added via AJAX.

### Hide an empty cart (since 2.5)

Enable **Hide if empty** to hide the entire Mini cart element on the frontend when the cart has no products. It remains visible in the Builder so you can edit it. This is separate from **Cart count > Visibility**, which only controls the count badge. The element updates after AJAX cart changes.

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

### Custom empty cart template (since 2.5)

To show a custom empty state in the cart details instead:

1. Create and publish a **Section** template containing the empty-cart message or layout.
2. Select the Mini cart and open **Content > Cart details**.
3. Leave **Hide** off and select the Section under **Empty cart template**.
4. Enable **Preview empty state** to inspect the template in the Builder. This preview setting does not change the visitor's cart.
5. Save and test the frontend with an empty cart, then add and remove a product.

Leave **Hide if empty** off if visitors should be able to open this empty state. An unpublished, empty, or non-Section template cannot be used. Avoid placing the Mini cart inside the same Section template selected as its empty state.

<div className="screenshot screenshot--control-panel">

![Mini cart controls with Hide if empty off, an Empty cart template selected, and Preview empty state enabled.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mini-cart-empty-panel.webp)

</div>

The selected Section replaces the default empty-cart message:

![An empty Mini cart displays a custom message and an Explore the collection button.](https://academy.bricksbuilder.io/assets/builder/release-2.5/mini-cart-empty-result.webp)

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

# Products orderby

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-orderby/

*Displays a dropdown to sort WooCommerce products.*

Displays a dropdown to sort WooCommerce products.

## Settings

- **Order by** (select) - Available sorting options. Multiple selection. Leave empty to use WooCommerce default list.

---

# Products total results

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-total-results/

*Displays the total number of products found and current result range.*

Displays the total number of products found and current result range.

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

- **Suppress PHP errors** (checkbox) - Hide caught PHP error diagnostics for this element. An authorized user can add `brx_code_errors=1` to the page URL to override suppression. This parameter does not grant permission to view diagnostics. Only available when execute code is enabled.

- **Render without wrapper** (checkbox) - Render on the frontend without the div wrapper. Style tab settings won't apply when this is enabled. Only available when execute code is enabled.

### Code Editors

Use these editors to enter the code to display or execute:

- **PHP & HTML** (code editor) - PHP and HTML code editor with syntax highlighting. Supports dynamic data and variables. Default example includes HTML heading and PHP date output.

- **CSS** (code editor) - CSS code editor with syntax highlighting. CSS is automatically wrapped in style tags. Supports dynamic data and variables.

- **JavaScript** (code editor) - JavaScript code editor with syntax highlighting. JavaScript is automatically wrapped in script tags. Supports dynamic data.

### Syntax Highlighting

Available when code execution is disabled:

- **Theme** (select) - Code syntax highlighting theme. Options: `github` (light), `tomorrow` (light), `tomorrow-night` (dark), `tranquil-heart` (dark). Default: None. Can also be set globally via theme styles.

## Inspect PHP execution errors {#php-errors}

Since Bricks 2.5, a caught PHP exception, parse error, or PHP `Error` can appear as a red diagnostic on the affected Code element. The notice contains the error type and message.

To inspect it, open the Builder or view the frontend while logged in with the Bricks **Execute code** capability and code execution enabled. Anonymous visitors and users without that permission do not receive these diagnostic details. This also applies to frontend AJAX and REST renders.

If **Suppress PHP errors** is enabled, turn it off while diagnosing the element, or add `brx_code_errors=1` to the page URL. The URL parameter only overrides suppression after the permission check; it does not expose errors to an unauthorized visitor.

Fix the PHP, sign the changed code, and render the element again. A successful evaluation clears the previous diagnostic. When execution fails, Bricks discards partial output from that evaluation rather than displaying it alongside the error. PHP warnings, notices, and deprecations are not converted into these caught-error diagnostics.

For errors in a PHP Query Editor rather than a Code element, see [Query editor (PHP)](https://academy.bricksbuilder.io/builder/dynamic-content/query-loop/#query-editor).

## Component properties {#component-properties}

Since Bricks 2.5, a Code element inside a component can display that instance's property values in its HTML output. Enable **Execute code** and **Parse dynamic data**, then use the copied property tag in the **PHP & HTML** editor:

```html
<p>Book {prop.title} today.</p>
```

Property tags are resolved in the rendered HTML after PHP execution. They are not substituted into PHP source, the CSS or JavaScript editors, script/style blocks, or executable HTML attributes. When code execution is disabled, the element displays the tag as part of the code snippet.

For PHP logic, call `bricks_get_component_property()` with the reference key. It returns the typed value, or a `WP_Error` when the property cannot be resolved. Check the result and escape it for the output context:

```php
<?php
$title = bricks_get_component_property( 'title' );

if ( ! is_wp_error( $title ) && is_scalar( $title ) ) {
    echo '<p>' . esc_html( (string) $title ) . '</p>';
}
?>
```

The PHP accessor requires **Execute code** and the usual code permissions and signature. It does not require **Parse dynamic data**. Both approaches need an active component instance. See [Properties as Dynamic Data](https://academy.bricksbuilder.io/builder/features/components/#property-dynamic-data) for reference keys and supported property fields.

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

- **Width** (since Bricks 2.5) — Set the mega panel width directly, such as `900px`, `80%`, a CSS variable, or a `clamp()` value. Leave empty to use the full horizontal reference width. Percentages are measured against that reference.

- **Alignment** (since Bricks 2.5) — Position a custom-width panel at the left, center, or right of the horizontal reference area. Default: Left.

- **CSS selector (Horizontal)** (text) — Optional: choose the horizontal reference element. Leave empty to use the page body.

- **CSS selector (Vertical)** (text) — Optional: vertical alignment reference.

Width and alignment support responsive breakpoint values. See [Set a custom mega menu width](https://academy.bricksbuilder.io/builder/features/menu-builder/#mega-menu-width) for examples.

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
