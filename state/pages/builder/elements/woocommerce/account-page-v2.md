*Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.*

Displays the WooCommerce My Account page as editable endpoint states with shared account navigation.

https://youtu.be/M1ZZLgnZOjM

> **Note**
>
> This element requires **Bricks > Settings > WooCommerce > Enable advanced modular elements**. The generated states also use the Bricks WooCommerce Notice element, so enable **Enable Bricks WooCommerce "Notice" element** on the same tab.

## Set up the account page

1. Go to **Bricks > Settings > WooCommerce**, enable **Enable advanced modular elements** and **Enable Bricks WooCommerce "Notice" element**, and save.
2. Open **Bricks > Woo Setup Wizard** and choose **My account**. **Advanced (v2)** is selected by default.
3. Click **Setup** and confirm that the existing page content will be replaced.

The wizard adds **Account - Page v2** to the assigned My Account page with a generated structure for every state. See [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) for the other options.

## Where this element works

My Account page.

## Key settings

- **State** (radio) - Switches the builder preview between My Account endpoint states.
- **Direction** (direction)
- **Gap** (number)
- **Disable navigation** (checkbox)
- **Navigation** - Direction, Align items, Justify content, Gap, Border, and Box shadow for the menu; Background, Item padding, Border, Box shadow, and Typography for each item; Active background, Border, Box shadow, and Typography for the current item.
- **Content** - Padding, Background, Border, Box shadow, and Typography for the content area.

Navigation and Content styles apply to every logged-in state at once. Set **Direction** to row to place the menu beside the content, then set the navigation **Direction** to column for a sidebar menu.

The navigation is not shown on the **Login**, **Lost password**, **Lost password (Confirmation)**, **Reset password**, and **Order withdrawal** states.

## Navigation items

The menu items come from the WooCommerce account endpoints. To remove an item, for example **Downloads** in a store without downloadable products, go to **WooCommerce > Settings > Advanced**, clear the endpoint's slug under **Account endpoints**, and save.

## Builder preview

- **Orders** and **View order** use the orders of the account you are logged in with. If that account has no orders, the canvas shows the generated dynamic tags and the empty orders message. Customers see their own orders on the frontend.
- Sample WooCommerce notices (error, success, and info) appear above the states in the builder so you can style them. They are not shown to customers.

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

The Edit address state uses one set of address fields for billing and shipping, so the elements are named without a prefix, for example **Address: Company name**. **Check address fields** compares them with the billing and shipping address fields WooCommerce currently uses. The other buttons appear once the check has found something to fix.

**Generate missing fields** adds the new elements at the top of the Edit address state, outside the edit address form. Drag each one into the **Address field wrapper**, for example below **Address: Last name**, so it renders inside the form.

In Bricks 2.4.3, a field removed with **Remove invalid fields** can stay in the builder canvas until you reload the builder. For the Phone field, the canvas keeps showing "Field not available for the current address." The Structure panel is already correct, and the field is gone from the page once you save.

See [Checkout v2 field maintenance](https://academy.bricksbuilder.io/builder/elements/woocommerce/checkout-v2/#field-maintenance) for the same workflow on the checkout.

![](https://academy.bricksbuilder.io/assets/account-v2-sync-address-fields.png)

## Query loops and dynamic data

Account Page v2 supports WooCommerce v2 query loops for account orders, order actions, account downloads, and account addresses.

Use account and order tags such as `{woo_account_address_title}`, `{woo_account_address}`, `{woo_order_number}`, `{woo_order_view_url}`, `{woo_order_download_name}`, and `{woo_order_action_url}` in the matching state or query loop.

See [WooCommerce v2 query loops and dynamic tags](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-v2-query-loops-dynamic-tags/#account-tags) for the complete reference.

## Usage tips

- Use [WooCommerce advanced modular elements](https://academy.bricksbuilder.io/integrations/woocommerce/advanced-modular-elements/) or the [Woo Setup Wizard](https://academy.bricksbuilder.io/integrations/woocommerce/woo-setup-wizard/) to create the recommended Account Page v2 structure.
- Review each state after setup so logged-in, logged-out, password reset, payment method, and order views all match your store design.
- Floating labels are available for the account forms in the Edit address, Edit account, Login, Lost password, Reset password, and Order withdrawal states. The Edit account and Edit address forms generated by the Woo Setup Wizard have them turned on.
- WooCommerce form buttons, such as **Save changes**, **Log in**, and **Register**, do not pick up your theme's button styles. Style them in the element settings or with a global class.
- Use the classic [WooCommerce Account Builder](https://academy.bricksbuilder.io/integrations/woocommerce/woocommerce-account-builder/) workflow if you prefer separate endpoint templates.