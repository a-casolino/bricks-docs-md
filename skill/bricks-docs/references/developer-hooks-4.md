# Filter: bricks/terms/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-terms-query_vars/

*Bricks terms query variables can be manipulated before the query runs like so:*

Bricks terms query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = 23; // Exclude term id 23

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_Term_Query](https://developer.wordpress.org/reference/classes/wp_term_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)

## Example 1: Exclude the current term from the query {#exclude-current-term}

Inside a term archive page, to exclude the current term from the query:

```php
// Exclude current term from the terms query loop on term archive pages.
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'uxtkgn' ) {
        return $query_vars;
    }

    $query_vars['exclude'] = get_queried_object_id();

    return $query_vars;
}, 10, 4 );
```

where `uxtkgn` is the Bricks ID of the element on which query loop is enabled.

## Example 2: Get terms assigned to a post {#get-terms-assigned-to-a-post}

In this example, we would like to get only the terms assigned to a specific post ID (the same as the WordPress function [`wp_get_object_terms()`](https://developer.wordpress.org/reference/functions/wp_get_object_terms/) output):

```php
add_filter( 'bricks/terms/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    if ( $element_id !== 'mjvhur' ) {
        return $query_vars;
    }

    $query_vars['object_ids'] = get_the_ID();

    return $query_vars;
}, 10, 4 );
```

---

# Filter: bricks/setup/control_options

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-setup-control_options/

*Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:*

Bricks offers a WordPress filter to add or remove control options. The control options are used throughout Bricks and allow you to manage the options of the:

- Template Types (e.g. Header, Footer, Single, Section...)
- Background position, repeat, attachment or size
- Button sizes
- Button or Heading styles
- Border styles
- Font weight and style
- CSS position
- Query types (e.g. Posts, Terms, Users, ..)
- Query order by, compare, operator and value type
- Image Sizes
- Taxonomies
- User roles

To manage any of these options or add new ones, use the WP hook `bricks/setup/control_options` like so:

```php
add_filter( 'bricks/setup/control_options', function( $control_options ) {
    $control_options['templateTypes']['my_template_type'] = esc_html__( 'My Template Type', 'my-plugin' );

    return $control_options;
} );
```

Note: the above example adds a new template type. To learn about other Bricks controls, visit the [Controls section](https://academy.bricksbuilder.io/developer/controls/).

---

# Filter: bricks/use_duplicate_content

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-use_duplicate_content/

*Duplicate content is available for all users with the editpost capability. Use this feature to duplicate any post or page containing Bricks data to ensure.*

Duplicate content is available for all users with the `edit_post` capability. Use this feature to duplicate any post or page containing Bricks data to ensure Bricks IDs are not duplicated. The duplicate option is also available for posts without Bricks data, allowing you to duplicate standard posts without the need for a third-party plugin.

![](https://academy.bricksbuilder.io/assets/bricks-duplicate-content-setting-example.png)

In **Bricks > Settings**, you can configure the duplicate content behavior:

![](https://academy.bricksbuilder.io/assets/bricks-duplicate-content-setting.png)

**Enable**: Duplicate content is available for all posts.
**Disable globally**: Duplicate content is disabled for all posts.
**Disable for WordPress Data**: Duplicate content is disabled for posts that do not use Bricks data.

This `bricks/use_duplicate_content` hook provides an additional layer of customization, enabling you to implement more complex logic based on your specific requirements. `(@since 1.12)`

## Parameters

**`$use`** *(bool)*

- The current decision on whether duplicate content is allowed. Default is based on settings and user capabilities.

**`$post_id`** *(int)*

- The ID of the post being checked.

**`$setting`** *(string)*

- The value in Bricks > Settings. Which can be `enable`, `disabled_all`, or `disable_wp`

## Return Value

This filter expects a boolean value:

- `true` to allow duplicate content for the particular post.
- `false` to disallow duplicate content for the particular post.

## Example Usage

Follow setting logic + ensure the user is admin

```php
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Only allow if current has user administrative privileges
  $has_admin_cap = current_user_can( 'manage_options' );

  // Fulfilled the condition
  return $use && $has_admin_cap;
}, 10, 3 );
```

Follow setting logic + exclude post type for ACF or MB

```php
add_filter( 'bricks/use_duplicate_content', function( $use, $post_id, $settings ) {
  // Check if the post type is 'acf-field-group' or 'mb-post-type
  $post_type = get_post_type( $post_id );
  $exclude_post_types = [ 'acf-field-group', 'mb-post-type' ];

  // Fulfilled the condition
  return $use && ! in_array( $post_type, $exclude_post_types, true );
}, 10, 3 );
```

---

# Filter: bricks/users/query_vars

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-users-query_vars/

*Bricks users query variables can be manipulated before the query runs like so:*

Bricks users query variables can be manipulated before the query runs like so:

```php
add_filter( 'bricks/users/query_vars', function( $query_vars, $settings, $element_id, $element_name ) {
    $query_vars['exclude'] = [ 2, 5 ]; // Exclude users id 2 and 5

    return $query_vars;
}, 10, 4 );
```

The filter callback receives three arguments:

- `$query_vars` an associative array used to feed the [WP_User_Query](https://developer.wordpress.org/reference/classes/wp_user_query/) class
- `$settings` an associative array containing the element settings set in the builder
- `$element_id` is a string containing the unique element ID
- `$element_name` is a string containing the element name (`@since 1.11.1`)

---

# Filter: builder/settings/{type}/controls_data

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-builder-settings-type-controls_data/

*Register custom controls for the Bricks Page Settings or Template Settings panels in the builder.*

This filter allows you to add new controls to the Page Settings or Template Settings panels in the builder.

To manage the **Template Settings** controls use the `builder/settings/template/controls_data` hook like so:

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

To manage the **Page Settings** controls use the `builder/settings/page/controls_data` hook like so:

```php
add_filter( 'builder/settings/page/controls_data', function( $data ) {
  // Do something

  return $data;
} );
```

**Example: Add a control to select the user roles in the author archive template type template condition**

```php
add_filter( 'builder/settings/template/controls_data', function( $data ) {
  // Get all the site user roles
  $all_roles = wp_roles()->roles;

  $roles = [];

  foreach ( $all_roles as $role => $role_data ) {
    $roles[ $role ] = $role_data['name'];
  }

  // Add control to select the user roles for an author archive template type
  $data['controls']['templateConditions']['fields']['archiveAuthorRoles'] = [
    'type'        => 'select',
    'label'       => esc_html__( 'Author roles', 'bricks' ),
    'options'     => $roles,
    'multiple'    => true,
    'placeholder' => esc_html__( 'Select role', 'bricks' ),
    'description' => esc_html__( 'Leave empty to apply template to all roles.', 'bricks' ),
    'required'    => [ 'archiveType', '=', 'author' ],
  ];

  return $data;
} );
```

---

# Filter: bricks/builder/color_palette

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-color-palette/

*Place and customize the following filter to display a different default color palette for the color control.*

Place and customize the following filter to display a different default color palette for the color control.

```php
add_filter( 'bricks/builder/color_palette', function( $colors ) {
  // Option #1: Add an individual color
    $colors[] = [
      'hex' => '#3ce77b',
      'rgb' => 'rgba(60, 231, 123, 0.56)',
    ];

  // Option #2: Override entire color palette
  $colors = [
    ['hex' => '#3ce77b'],
    ['hex' => '#f1faee'],
    ['hex' => '#a8dadc'],
    ['hex' => '#457b9d'],
    ['hex' => '#1d3557'],
  ];

  return $colors;
} );
```

---

# Filter: bricks/builder/save_messages

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-save-messages/

*Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.*

Place and customize the following filter to display different save message every time you manually save your progress when editing with Bricks.

```php
add_filter( 'bricks/builder/save_messages', function( $messages ) {
  // Option #1: Append individual save message to existing message collection
    $messages[] = 'Yasss';

  // Option #2: Replace all existing builder save messages
    $messages = [
      'Done',
      'Cool',
      'High five!',
    ];

  return $messages;
} );
```

---

# Filter: bricks/builder/standard_fonts

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-standard-fonts/

*Place and customize the following filter to display a different set of web-safe fonts in the typography control.*

Place and customize the following filter to display a different set of web-safe fonts in the typography control.

```php
add_filter( 'bricks/builder/standard_fonts', function( $standard_fonts ) {
  // Option #1: Add individual standard font
  $standard_fonts[] = 'Verdana';

  // Option #2: Replace all standard fonts
  $standard_fonts = [
    'Georgia',
    'Times New Roman',
    'Verdana',
  ];

  return $standard_fonts;
} );
```

---

# Filter Hooks

Source: https://academy.bricksbuilder.io/developer/hooks/filters/

*Documented Bricks filter hooks for builder settings, rendering, queries, authentication, code execution, and frontend behavior.*

These are all documented Bricks filter hooks:
