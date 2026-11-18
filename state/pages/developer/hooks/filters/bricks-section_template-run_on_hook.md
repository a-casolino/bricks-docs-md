*Control whether a Section template is injected at an action hook using custom PHP logic, such as checking a post's custom field.*

Since Bricks 2.5, use `bricks/section_template/run_on_hook` to control whether a [Section template is injected at an action hook](https://academy.bricksbuilder.io/builder/features/an-intro-to-templates/#hook). For example, require a custom field to have a particular value before showing a promotional section.

Bricks evaluates the template's saved conditions first, then passes the decision to this filter before registering the template's styles and rendering callback.

## Parameters

The filter receives five arguments:

| Parameter | Type | Description |
| --- | --- | --- |
| `$run_hook` | `bool` | Whether the saved conditions allow this template to run at this hook and priority. |
| `$template_id` | `int` | The Section template's post ID. |
| `$hook_name` | `string` | The destination action hook name, such as `bricks_before_footer`. |
| `$hook_priority` | `int` | The destination action's priority. Defaults to `10` when no priority is saved. |
| `$conditions` | `array` | The template conditions grouped for this hook name and priority, including any include and exclude conditions in that group. |

Return a boolean:

- Return `$run_hook` to preserve the existing decision.
- Return `false` to prevent injection for this template, hook name, and priority.
- Return `true` to allow injection even if the saved conditions did not match, including when an exclude condition matched.

The filter only runs for existing hook assignments on Section templates. Returning `true` does not create a hook assignment for a template without one.

## Example: Require a custom field

This example shows a Section template before the footer only on individual posts or pages whose `section_allowed` custom field contains `yes`.

1. Edit a Section template and open **Settings > Template Settings > Conditions**.
2. Add an **Entire website** condition, set **Hook: Name** to `bricks_before_footer`, and set **Hook: Priority** to `10`.
3. Add the following PHP to your child theme's `functions.php` or a custom plugin. Replace `123` with the Section template's ID.
4. Set the `section_allowed` custom field to `yes` on a post or page, then view it on the frontend.

```php
add_filter( 'bricks/section_template/run_on_hook', function( $run_hook, $template_id, $hook_name, $hook_priority, $conditions ) {
  // Leave other templates, hooks, and priorities unchanged.
  if ( (int) $template_id !== 123 || $hook_name !== 'bricks_before_footer' || $hook_priority !== 10 ) {
    return $run_hook;
  }

  // Preserve saved conditions and limit the custom-field check to singular pages.
  if ( ! $run_hook || ! is_singular() ) {
    return false;
  }

  $post_id = get_queried_object_id();

  return get_post_meta( $post_id, 'section_allowed', true ) === 'yes';
}, 10, 5 );
```

For this assignment, a missing field or any value other than `yes` prevents injection. Other hook names and priorities on the same template keep their existing decisions. If you add exclude conditions to this assignment, the example preserves them.

The `10` in `}, 10, 5 );` is the priority of your filter callback. `$hook_priority` is the priority of the destination action configured in the template condition. The final `5` tells WordPress to pass all five filter arguments.

## Execution timing and scope

The filter runs for each template, hook name, and priority group during hook assignment. On a normal frontend request, Bricks assigns templates on the WordPress `wp` action at priority `20`. Register your filter before that point, as the example above does.

Use data available during hook assignment. The filter does not run each time the destination action fires, so it cannot make a separate decision for each item in a loop rendered later. If Bricks reassigns hooked templates after the request context changes, the filter runs again for those assignments.

Returning `false` skips the style registration and rendering callback for that assignment. It does not prevent the same template from being rendered through another assignment, the Template element, or a shortcode. Hook injection is skipped inside the builder; check the result on the frontend.

Section hook assignments use a separate condition evaluator from template scoring. Use this filter for hook-injected Section templates and [`bricks/screen_conditions/scores`](https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-screen_conditions-scores/) for template and theme style scoring.