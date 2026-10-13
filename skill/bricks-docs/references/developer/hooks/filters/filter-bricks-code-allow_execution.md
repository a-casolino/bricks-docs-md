# Filter: bricks/code/allow_execution

Source: https://academy.bricksbuilder.io/developer/hooks/filters/filter-bricks-code-allow_execution/

*An alternative to the Disable code execution setting under Bricks > Settings > Builder Access. You can use this PHP filter to disable/enable code execution.*

An alternative to the **Disable code execution** setting under `Bricks > Settings > Builder Access`. You can use this PHP filter to disable/enable code execution programmatically.

![](https://academy.bricksbuilder.io/assets/disallow-code-execution-hook.png)

```php
add_filter( 'bricks/code/allow_execution', function( $allow ) {
  // Only allows to return false to disable code execution programmatically
  return false;
} );
```
