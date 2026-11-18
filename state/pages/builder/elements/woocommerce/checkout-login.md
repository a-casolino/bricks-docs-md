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
- **Icon expanded** (icon, since 2.5) - Alternate icon while the toggleable form is open.
- **Icon expanded typography** (typography, since 2.5) - Styling for the expanded icon.
- **Transition (ms)** (number, since 2.5) - Opening and closing duration when **Toggleable form** is enabled. Set `0` for an immediate change.
- **Disable login message** (checkbox)

## Usage tips

- Use checkout elements only in Checkout templates so forms and order data render correctly.
- Test logged-in and guest checkout flows after styling changes to ensure all states remain usable.