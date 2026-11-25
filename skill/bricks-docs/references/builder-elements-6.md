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
