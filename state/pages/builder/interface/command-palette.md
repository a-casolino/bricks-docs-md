*Use the Bricks Command Palette to run common actions, navigate faster, and insert element structures with keyboard-driven workflows.*

The **Command Palette**, introduced in Bricks 2.0, lets you open Builder tools, find content, and insert element structures from the keyboard.

https://youtu.be/gOVNlRvsYc8

## How to launch it

Click the command `⌘` icon in the builder toolbar or use the default `CMD/CTRL + K` keyboard shortcut to open the Command Palette, which appears as an overlay, allowing you to type and filter commands across four scopes. In Bricks 2.5, you can change the opening shortcut under **Manage → Keyboard shortcuts**. The navigation and insertion keys inside the palette remain fixed. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/).

## Scope: Builder {#builder}

Navigate to key parts of the builder from a growing list of targets such as classes, variables, templates, theme styles, settings, etc.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-builder.png)

## Scope: Post Types {#post-types}

This scope lets you browse the registered post types your builder capability can access, create new posts when your user can edit posts, or duplicate existing posts.

Besides "All" and "Template (Bricks)", a post type gets its own tab only when Bricks is enabled for it under **Bricks > Settings > General > Post types** and your role can access it in the builder. "All" searches every public post type.

To create a post, select the post type tab, type the title, and click "Create". Bricks adds the post as a draft. Click a result to open it in the builder. `CMD/CTRL` + click opens it in a new browser tab. Posts of a type that is not enabled for Bricks open in the WordPress editor in a new tab.

The scope auto-selects the post type that you are currently editing. So if you are editing a Bricks template the "Template (Bricks)" post type will be selected. If you edit a "Page", then "Page" is selected and so on.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-post-types.png)

## Scope: Components {#components}

Type `*` at the start of the search to switch to Components. Search for a component and select it to insert it into the current page, when your builder permissions allow component insertion.

## Scope: Elements {#elements}

Use the **Elements** scope to insert one element or a nested structure in a single action. Save structures you use repeatedly so you can insert them again without retyping the expression.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-scope-elements.png)

### Insert single element

To insert a single element simply type its name, such as "Section", then `ARROW`-navigate to it in the elements list, and insert it by pressing `ENTER` or just click on the element name.

### Insert element structure

Each element starts with an **@** symbol.

The element name that the command bar requires is displayed in square brackets in the results list:

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-element-name.png)

<figcaption>

Text link element command: `@text-link`

</figcaption>

### Supported operators

Use the following operators to define nested structure, siblings, a multiplier, or to move back up one nesting level.

| Symbol | Meaning |
| --- | --- |
| `@` | Bricks element name (e.g. `@heading`) |
| `>` | Nest inside |
| `+` | Insert element as sibling |
| `*` | How often to insert the element |
| `^` | Move one level up before inserting the next element |
| `.class-name` | Assign a global class to the preceding element (since 2.5) |
| `#custom-id` | Set a custom CSS ID on the preceding element (since 2.5) |

### Add classes and custom IDs {#classes-and-ids}

Since Bricks 2.5, append class names and a custom ID directly to an element name, without spaces:

```text
@section#contact > @container.card-grid > @block#card.card * 2
```

This inserts a Section with custom ID `contact`, a child Container using the global class `card-grid`, and two Blocks using the global class `card`. The Blocks receive custom IDs `card` and `card-2`. Because the expression supplies a Container directly below the Section, Bricks does not insert an extra automatic Container. A Section expression without that explicit Container keeps its normal automatic Container.

The shorter expression `@block#card.card * 2` creates two Blocks with the same global class and distinct custom IDs:

![The Command Palette Elements scope with @block#card.card * 2 entered and Insert available.](https://academy.bricksbuilder.io/assets/builder/release-2.5/palette-expression.webp)

<div className="screenshot screenshot--control-panel">

![The second Block selected with custom ID card-2 and the card global class assigned.](https://academy.bricksbuilder.io/assets/builder/release-2.5/palette-class-result.webp)

</div>

For each `.class-name`, Bricks reuses the global class with that exact name. If it does not exist, Bricks creates an empty global class when your user has permission to create classes. A name such as `card-grid` does not generate a grid layout by itself; define that class's styles or reuse an existing styled class.

Assigning classes requires **Assign/unassign global classes** permission. Creating missing classes also requires **Create global classes** permission. Without assignment permission, class suffixes are not applied. With assignment permission but no creation permission, existing classes can be used and missing ones are skipped. If a matching class is in the trash, restore it in the Class Manager before trying to create it again.

Combine classes as `@block.card.featured`, or combine an ID and classes as `@block#contact-card.card.featured`. These are native global-class assignments, not entries in the **Style > CSS > CSS classes** text field. See [Global CSS Classes](https://academy.bricksbuilder.io/builder/styling/global-css-classes/) for editing them.

When an ID repeats within the same insertion command, Bricks adds numeric suffixes such as `-2` and `-3`. This numbering does not check IDs already on the page or IDs inserted by a separate command. Keep custom IDs unique when reusing saved structures.

### Element structure example

`@section * 2 > @heading + @text + @button`
This creates the following structure *(two times because of the multiplier: `* 2`)*:

- `Section`
 └ `Container`
   ├ `Heading`
   ├ `Text`
   └ `Button`

Bricks adds the Container inside every Section automatically, so you don't type `@container` after `@section`.

### Quick element insertion

> **Note**
>
> After selecting an element from the search results, its name is added to your query with the `@` prefix, allowing you to quickly build complex queries:

1. Type `@` to activate insertion mode
2. Select an element (e.g., "section")
3. Type `>` for a child element
4. Continue building your structure
5. Insert your element structure
  - Click the "Insert" button that appears next to your query
  - Press `CMD/CTRL + ENTER`

If no element is selected, Bricks adds the structure at the end of the page or template.

### Save element structures

Instead of typing out your favorite structures by hand every time, you can save them by clicking the "Save" button next to the command bar. Your structures are stored in this browser's `localStorage`, so they are local to that browser/profile and are not synced between users or devices.

![](https://academy.bricksbuilder.io/assets/bricks-2.0-command-palette-saved-element-structures.png)

<figcaption>

List of saved element structures

</figcaption>

To insert a saved structure, open the "Select element structure" dropdown in the Elements scope and pick it. To delete a structure, mouseover the structure item in the list, and click the "Delete" icon.

## Scope: Components {#components}

This scope lists the components on your site. Select a component to insert an instance of it, the same way you insert a single element. The scope is available when your role can insert components.

## Keyboard shortcuts

| **Keyboard shortcut** | **Action** |
| --- | --- |
| `CMD/CTRL + K` | Open/close the command palette |
| `ESC` | Close the command palette |
| `TAB > ENTER` (to enter selected scope) | Navigate between search and scopes |
| `#` (as the first character in the search input) | Enter scope “Builder” |
| `/` (as the first character in the search input) | Enter scope “Post Types” |
| `+` or `@` (as the first character in the search input) | Enter scope “Elements” |
| `*` (as the first character in the search input) | Enter scope “Components” |
| `CMD/CTRL + ENTER` | Insert the element structure typed in scope “Elements” |
| `/` followed by a post-type index | Navigate to a specific post type |
| `ARROW UP/DOWN` + ENTER | Navigate to a search result and open it |

## Notes

Bricks remembers your last selected scope, even after builder reload (stored in your localStorage).

The "Pages" panel remains available from the builder toolbar. The Command Palette is an additional fast way to browse, create, duplicate, and open posts.

The docs entry is also accessible from the "Builder" scope.