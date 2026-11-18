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