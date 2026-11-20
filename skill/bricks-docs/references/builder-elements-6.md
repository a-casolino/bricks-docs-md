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

# Products archive description

Source: https://academy.bricksbuilder.io/builder/elements/woocommerce/products-archive-description/

*Displays the description for WooCommerce product archives (shop page, categories, tags).*

Displays the description for WooCommerce product archives (shop page, categories, tags).

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
