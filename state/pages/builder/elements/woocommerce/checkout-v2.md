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