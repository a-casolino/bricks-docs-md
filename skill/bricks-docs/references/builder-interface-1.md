# Builder Mode (Custom)

Source: https://academy.bricksbuilder.io/builder/interface/builder-mode/

*Customize the Bricks builder color scheme with custom builder-mode CSS variables.*

Starting with Bricks 1.3.7 you can customize the builder mode (color scheme) to your liking by tweaking a few CSS variables.

You first have to set the "Builder Mode" under Bricks → Settings → Builder to "Custom" and save your settings.

The following new setting called "Builder Mode (Custom)" should now appear:

![Builder Mode: Custom](https://academy.bricksbuilder.io/assets/bricks-setting-builder-mode-custom-1024x721.png)

Below you can find a starter CSS snippet with commonly customized builder CSS variables. Bricks 2.x defines additional variables for classes, components, status colors, muted colors, and the canvas scrollbar, so use this as a starting point and override any extra variables your custom mode needs.

```php
[data-builder-mode=custom] {
  --builder-bg: #f6f4f2;
  --builder-bg-2: #efebe6;
  --builder-bg-3: #e7e1da;
  --builder-bg-4: #dbd2c8;
  --builder-bg-accent: #EED8FD;

  --builder-color: #2e271e;
  --builder-color-description: #76634c;
  --builder-color-accent: #7209B7;
  --builder-color-accent-inverse: #fff;

  --builder-color-knob: #c8baaa;
  --builder-border-color: #d8cec2;
  --builder-placeholder-opacity: .33;

  --builder-color-class: #2b6cb0;
  --builder-bg-class: #d8e8f6;
  --builder-color-component: #6b46c1;
  --builder-bg-component: #eadcf8;
  --builder-color-info: #006c9c;
  --builder-bg-info: #d9f1ff;
  --builder-color-danger: #b42318;
  --builder-bg-danger: #ffe4e2;
  --builder-color-success: #027a48;
  --builder-bg-success: #dcfae6;
  --builder-color-muted: #7a6f63;
  --builder-bg-muted: #e2ddd6;

  --builder-canvas-scrollbar-thumb: #c8baaa;
  --builder-canvas-scrollbar-thumb_hover: #76634c;
  --builder-canvas-scrollbar-track: #efebe6;

  --bricks-tooltip-bg:   #16130f;
  --bricks-tooltip-text: #f6f4f2;
}
```

If you copy the CSS above, paste it into your "Builder Mode (Custom)" setting, and save your settings, your builder should look like this:

![](https://academy.bricksbuilder.io/assets/bricks-screenshot-builder-mode-custom-1024x576.png)

<figcaption>

Bricks builder with a custom color scheme (mode)

</figcaption>

### Resources

- Color palettes: [https://coolors.co/palettes/trending](https://coolors.co/palettes/trending)
- Color palettes: [https://colorhunt.co](https://colorhunt.co)
- Generate color shades & tints: [https://www.colorhexa.com](https://www.colorhexa.com)

Note: In custom builder mode, Code element's background color changes to a light color scheme.

---

# Builder Access & Capabilities

Source: https://academy.bricksbuilder.io/builder/interface/builder-access/

*Control who can access Bricks and which builder capabilities are available for different WordPress roles.*

Bricks gives you full control over who can access the builder, and what actions they're allowed to perform. You can either assign a **predefined capability**, or create your own **custom capability** that allows only the specific permissions you enable for it.

This gives you complete freedom and control to tailor the builder experience to any roles (i.e. content editor, designer, client, etc.) depending on what they should be able to do.

![](https://academy.bricksbuilder.io/assets/bricks-settings-builder-access.png)

## Access levels

There are two ways to manage builder access:

1. Use one of the predefined capabilities: **Full access**, **Edit content**, or **No access**
2. Create your own custom builder capability with detailed permission control

### Predefined capabilities

- **Full access**: Grants access to all features and permissions in the Bricks builder.
- **Edit content**: Limits the user to content editing only. Layout, styling, and structural controls are disabled. More specifically, this includes the following permissions:
  - Access revisions
  - Set component properties (instance)
  - Access content (HTML) settings
  - Edit all elements
  - Edit all Bricks-enabled post types
- **No access**: Blocks access to the Bricks builder entirely.

## Creating a custom capability {#custom}

If you need precise control over the actions a user or role should be able to perform, you can create your very own custom builder capability, following the steps outlines below.

1. Go to **Bricks > Settings > Builder access**
2. Under **Builder capabilities**, click **Add new capability**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-add-custom-capability.png)

Inside the capability popup, you can:

- Give the capability a name & a description
- Enable exactly the permissions you want to grant

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-permissions.png)

Once created, you can assign this capability to specific users or user roles.

## Assigning capabilities

You can assign any builder capability, whether predefined or custom:

- To a **user role**, under **Bricks > Settings > Builder access > Builder access**

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-custom-capabilities.png)

- To a **specific user**, by editing their WordPress user profile

![](https://academy.bricksbuilder.io/assets/bricks-builder-edit-user-profile.png)

![](https://academy.bricksbuilder.io/assets/bricks-builder-access-user-settings.png)

This gives you flexibility to apply permissions globally or individually.

## Drafts and site versions {#drafts-and-versions}

With [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) enabled, users need WordPress permission to edit the page and Bricks access for that page's post type to open its page draft. A page draft can be opened by other users with the same required access; it is not private to its creator.

[Site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) span multiple pages. Opening or creating them requires Builder access and WordPress permission to edit other users' posts (`edit_others_posts`). Existing Builder permissions still control the actions available inside either kind of draft.

Publishing checks the rights required for all included changes, including page and template settings, shared data, and code execution. Having access to a draft does not grant permission to publish every change someone else added to it.

[Review links](https://academy.bricksbuilder.io/builder/interface/review-links/) provide a separate, view-only preview for people without an editor login. They do not give reviewers Builder access or permission to edit or publish.

## Available permissions

When editing a capability, the following permissions are available and grouped by category:

### Post types {#post-types}

Choose which post types can be edited using Bricks.

### General {#general}

- Access breakpoints manager
- Access page settings
- Access template settings
- Access revisions
- Delete revisions
- Access font manager
- Access icon manager
- Access query manager
- Access filter manager (Bricks 2.5)
- Customize builder interface
- Manage builder interface profiles
- Manage global elements (only if legacy Global Elements exist)

**Access filter manager** permits creating, editing, organizing, deleting, importing, and exporting [global filters](https://academy.bricksbuilder.io/builder/dynamic-content/query-filters/#global-filters). This includes editing shared controls on linked elements. Users without it can select an existing compatible global filter and edit local settings such as the target query and presentation.

### Templates {#templates}

- Create templates
- Edit templates
- Delete templates
- Insert templates
- Access remote templates
- Import/export templates

### Global styles & settings {#styles-setting}

- Access theme styles
- Access color manager
- Access variable manager
- Access class manager
- Create global classes
- Edit global classes
- Assign/unassign global classes
- Delete global classes
- Lock/unlock global classes
- Copy/paste global class styles
- Access pseudos & selectors

### Components {#components}

- Access remote components
- Insert components
- Edit properties (instance)
- Edit components
- Create components
- Delete components
- Import/export components

Remote workflows combine these permissions instead of using one broad access flag:

| Workflow | Required permissions |
| --- | --- |
| Browse a configured remote component library | **Access remote components** |
| Import a remote component | **Access remote components** and **Import/export components** |
| Insert an imported component | **Insert components** |
| Insert a remote template without components | **Access remote templates** and **Insert templates** |
| Insert a remote template with component dependencies | **Access remote templates**, **Insert templates**, **Access remote components**, **Import/export components**, and **Insert components** |
| Save a remote template to My Templates | **Access remote templates** and **Import/export templates** |
| Save a remote template with component dependencies to My Templates | The template import permissions above, plus **Access remote components** and **Import/export components** |

See [Remote Templates](https://academy.bricksbuilder.io/builder/features/remote-templates/) for the corresponding template setup.

### Element editing & styling {#element-edit-style}

- Access content (HTML) settings
- Access style (CSS) settings
- Access query loop builder
- Access element hide
- Access element conditions
- Access element interactions
- Duplicate elements
- Delete elements
- Move elements
- Copy/paste elements
- Copy/paste element styles
- Copy/paste element conditions
- Copy/paste element interactions
- Copy/paste element attributes
- Pin/unpin elements

### Edit elements {#edit-elements}

Controls general editing of existing elements.

_Note: Requires access to content and/or style settings._

### Add elements {#add-elements}

Define which elements can be inserted.

---

# Command Palette

Source: https://academy.bricksbuilder.io/builder/interface/command-palette/

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

---

# Context Menu

Source: https://academy.bricksbuilder.io/builder/interface/context-menu/

*Use the Bricks context menu for quick element actions such as edit, clone, delete, structure moves, and style copy and paste.*

The Bricks context menu gives you quick access to actions for the selected element. It is especially useful for copying, pasting, duplicating, deleting, hiding, wrapping, converting, and saving reusable layout pieces.

To open it, right-click an element on the canvas or in the Structure panel.

https://youtu.be/7HpRF6jRSlc

## How the context menu selects an element

Right-clicking an element makes that element active and opens the Element panel.

The Bricks context menu is hidden in Preview mode. It also does not open from the Elements library panel, because that panel is for inserting new elements, not editing existing ones.

## Action availability

The context menu is dynamic. It changes based on:

- The current user's builder permissions.
- Whether one element or multiple elements are selected.
- Whether the selected element is nestable.
- Whether the selected element is cloneable or deletable.
- Whether the selected element is a Component instance or Component root.
- Whether the selected element is a legacy Global Element.
- Whether the clipboard currently contains Bricks data that can be pasted.

If an action is missing, it is usually because the current selection, permissions, or clipboard state does not support it.

## Main actions

| Action | What it does | Important limits |
| --- | --- | --- |
| Copy | Copies the selected element or selected elements. | Requires copy/paste element permission. |
| Paste | Pastes copied Bricks elements when the clipboard contains element data. | Requires copy/paste element permission. |
| Duplicate | Clones the active element. | Hidden for active Component roots and unavailable for elements marked as not cloneable. |
| Delete | Deletes the active element. In bulk mode, deletes the selected elements. | Hidden for active Component roots and unavailable for elements marked as not deletable. |
| Hide element | Toggles hide settings for builder, frontend, or both. | Requires access to element hide. |
| Insert | Inserts a Container, Block, or Div inside the selected layout element. Hold Cmd/Ctrl to switch to **Insert after**. | Available for nestable elements. |
| Wrap | Wraps the selected element or selected sibling elements in the configured wrapper type (Block by default). Use the adjacent icons to choose another type. Section is offered only for top-level elements. | In bulk mode, selected elements must share the same parent. |
| Unwrap | Removes a selected nestable wrapper and moves its children up to the wrapper's parent. | Requires a nestable element with children. |
| Convert | Converts Section, Container, Block, and Div layout elements to another layout type where allowed. | Only applies to layout elements. |
| Save as Component | Opens the Components workflow for the selected element. | Hidden in bulk mode, while editing Components, or for Component/legacy Global Element selections. Shown but disabled for Template and Filter elements. |
| Save as Template | Saves a nestable element as a Template. | Not available in bulk mode or while editing Components. |
| Edit Component | Opens a Component instance for editing. | Requires Component permissions. |
| Unlink Component | Converts a Component instance into regular local elements after confirmation. | Requires Component permissions. |
| Unlink Global Element | Unlinks a legacy Global Element when one exists. | Requires legacy Global Element access. |

## Copy sub-actions

The Copy row can show extra icons for more specific data:

| Copy icon/action | Copied data |
| --- | --- |
| CSS ID | The element's rendered CSS ID, including `#`. |
| Bricks ID | The internal Bricks element ID. |
| Query ID | The query ID for a selected query loop element. In Component loop contexts, this can include the instance ID. |
| Styles | Element ID styles, or active global class styles if a class is active. |
| Conditions | Element conditions. |
| Interactions | Element interactions. |
| Classes | Assigned global classes. |
| Attributes | Custom attributes. |

These actions are permission-gated. For example, copying attributes requires copy/paste element attributes permission, while copying conditions requires copy/paste element conditions permission.

## Paste sub-actions

The Paste row changes based on the clipboard data. Bricks shows only paste actions that match the current clipboard source.

| Paste action | Behavior |
| --- | --- |
| Styles | Pastes copied element styles or global class styles to the selected target. |
| Conditions | Appends copied conditions to the existing element conditions and generates new condition IDs. |
| Interactions | Appends copied interactions to the existing element interactions and generates new interaction IDs. |
| Attributes | Replaces the target element's copied custom attributes and generates new attribute IDs. |
| Classes | Merges copied global classes into the target element's existing classes without duplicates. |

Pasting styles can target one selected element or multiple selected elements. When multiple elements are selected, Bricks applies the paste operation to the selected elements.

## Bulk editing behavior

The context menu supports bulk editing, but not every action is available for multiple selected elements.

Bulk editing works best for:

- Copying selected elements.
- Deleting selected elements.
- Hiding selected elements.
- Wrapping selected sibling elements with the same parent.
- Pasting shared styles.
- Applying copied classes, conditions, interactions, or attributes where supported.

Bulk editing has important limits:

- Save as Component and Save as Template are not shown in bulk mode.
- Some copy sub-actions are disabled in bulk mode.
- Wrap requires all selected elements to share the same parent.
- Unwrap only works when the selected nestable elements contain children and the selected set does not include those children.

## Insert, wrap, unwrap, and convert

The context menu can create or reshape layout structure without dragging from the Elements panel.

### Insert

Insert adds a Container, Block, or Div inside the selected layout element, as its last child. The default insert type can be controlled by builder settings. Hold Cmd (macOS) or Ctrl (Windows) while the menu is open and the action changes to **Insert after**, which adds the new element after the selection instead.

### Wrap

Wrap places the selected element, or selected sibling elements, inside a new wrapper. Clicking **Wrap** uses the wrapper type selected in builder settings (Block by default). Use the icons next to it to choose another wrapper type. Section is only offered when the selected elements sit at the top level of the page.

Use wrap when you already built content but need an additional layout layer.

### Unwrap

Unwrap removes a selected nestable wrapper and moves its children to the wrapper's parent. It preserves child order as much as the current hierarchy allows.

Use unwrap carefully. It changes structure, not only styling.

### Convert

Convert changes one layout wrapper type into another, such as Container to Block or Div to Container. It is available for Section, Container, Block, and Div when the selected structure can be converted.

Section conversion is restricted to root-level contexts because sections are top-level layout wrappers.

## Components, templates, and legacy Global Elements

Use **Save as Component** when the selected element should become reusable and editable through the Components system.

Use **Save as Template** when the selected nestable element should become a reusable template that can be inserted later.

Legacy [Global Elements](https://academy.bricksbuilder.io/builder/features/global-elements/) can still be unlinked from the context menu when they exist. For new reusable content, use [Components](https://academy.bricksbuilder.io/builder/features/components/) or Templates.

## Permission notes

Context menu actions follow the same Builder Access permission model as the rest of the builder. A user might be able to open the context menu but not see specific actions.

Common permission-gated actions include:

- Copy/paste elements
- Copy/paste styles
- Copy/paste conditions
- Copy/paste interactions
- Copy/paste attributes
- Hide element
- Duplicate elements
- Delete elements
- Create Components
- Edit Components
- Create Templates
- Manage legacy Global Elements

Review [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/) when a user reports that a context-menu action is missing.

## Troubleshooting

- **The Bricks context menu does not open:** Make sure you are not in Preview mode and that you are right-clicking an existing canvas or Structure element.
- **Paste action is missing:** Copy the matching Bricks data first. The paste menu only shows actions that match the clipboard data.
- **Copy/paste behaves differently in Safari:** Safari can be stricter about clipboard access, so perform copy and paste from direct user gestures.
- **Save as Component is missing or disabled:** Check permissions and make sure you are not bulk editing, editing an active Component, selecting a Component or legacy Global Element, or selecting a Template or Filter element.
- **Wrap is missing or disabled:** Confirm the selected elements share the same parent and can be wrapped in the current hierarchy.

---

# Builder Interface Customiser and Profiles

Source: https://academy.bricksbuilder.io/builder/interface/builder-interface-customiser-profiles/

*Customize the Bricks builder workspace, save reusable interface profiles, and assign layouts to roles or users.*

The Builder Interface Customiser lets you adjust the Bricks builder workspace to match the way you work.

You can add, hide and move toolbar items, dock the Control panel and Structure, place Pinned controls in the bottom dock, and save layouts as profiles for different users or roles.

This changes the builder workspace only. It does not change frontend output, templates, elements, or page data.

https://www.youtube.com/watch?v=iIUmLZQp_CY

## Requirements

Builder interface customization is available in Bricks 2.4.

The Builder interface entry appears when the current user can customize the builder interface or manage builder interface profiles. Administrators with full builder access can use both by default.

Use [Builder access](https://academy.bricksbuilder.io/builder/interface/builder-access/) to grant these permissions to other roles:

- **Customize builder interface**: Lets the user save and reset their own builder interface preferences.
- **Manage builder interface profiles**: Lets the user create, load, rename, overwrite, delete, import, and export builder interface profiles.

Site admins can disable the customiser globally under `Bricks -> Settings -> Builder -> Builder interface` by enabling **Disable builder interface customiser**.

## Open the Builder interface

Open the builder, then use either of these entry points:

- Open the builder settings panel and click **Builder interface**.
- Open the [Command Palette](https://academy.bricksbuilder.io/builder/interface/command-palette/) and choose **Builder interface** from the Builder scope.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-popup.webp)

## Workspace layout

The Builder interface popup controls the main workspace areas.

### Control panel and Structure

Use the **Control panel** and **Structure** settings to dock each panel to the **Left**, **Right**, or **Bottom**.

When the Control panel and Structure are assigned to the same side dock, Bricks displays them next to each other instead of stacking both panels in the same area.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-control-structure-panels.webp)

### Pinned controls

Pinned controls can stay inside the control panel or move to the bottom dock.

When **Pinned controls** is set to **Bottom**, the popup shows a **Pinned controls layout** section. Use it to set the number of columns and optional column widths. Bricks supports up to six pinned-control columns.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-pinned-controls.webp)

### Bottom dock

The bottom dock can contain:

- Control panel
- Structure
- Pinned controls

Items in the bottom dock appear as tabs. You can reorder those tabs while editing the builder interface.

When more than one item is assigned to the bottom dock, the popup shows a **Bottom dock layout** section. Use it to set the number of bottom dock columns and optional CSS widths for each column. The maximum number of columns matches the number of items currently assigned to the bottom dock.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-bottom-dock.webp)

## Toolbar layout

The toolbar can be placed on the **Top**, **Right**, **Bottom**, or **Left** edge of the builder.

Each toolbar edge has three groups:

- **Start**
- **Center**
- **End**

Drag toolbar items between these groups to change their order and placement. Bricks keeps the breakpoint controls together as one locked cluster.

### Toolbar items

The **Toolbar items** section contains optional items you can drag into the toolbar. This includes repeatable toolbar dividers and custom **Insert element** shortcuts.

An Insert element shortcut can insert a selected element or component directly from the toolbar.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-toolbar-items.webp)

### Hidden items

Drag optional toolbar items into **Hidden items** to remove them from the visible toolbar. Use the restore button on a hidden item to bring it back.

Required toolbar items cannot be hidden. In Bricks 2.4, **Elements**, **Structure**, **Preview**, and **Save** are required.

## Keyboard shortcuts

In Bricks 2.5, the **Keyboard shortcuts** section lets you include shortcut customizations with the current Builder Interface settings or profile.

1. Click **Manage** in the Keyboard shortcuts section.
2. Change the combinations you want to include, then click **Save** to return to the Builder Interface popup.
3. Click **Save** to keep the current interface settings for your account, or use **Save as** / **Overwrite** in Profiles to save them with a reusable profile.

![The Keyboard shortcuts section in Builder Interface with its Manage button.](https://academy.bricksbuilder.io/assets/keyboard-shortcuts/builder-interface-keyboard-shortcuts.webp)

Shortcuts saved in an assigned profile take priority over personal shortcut preferences. The profile controls only the commands it defines; those bindings show the profile name and are read-only in the personal shortcut manager. Personal combinations for other commands remain available, unless they conflict with a managed command. Removing the profile restores the retained personal preferences.

Use **Manage → Keyboard shortcuts** from the toolbar when you only want to change your personal shortcuts. See [Keyboard Shortcuts](https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/) for remapping, conflicts, import/export, and the default combinations.

## Save or reset your layout

Click **Save** to store the current builder interface for your user account.

Click **Reset** to remove your saved builder interface preferences and return to the resolved default layout. In Bricks 2.5, this also clears your personal keyboard shortcut overrides. The reset keeps pinned control groups where possible, so frequently used pinned groups are not lost just because the workspace layout was reset.

If the popup shows an unsaved-changes message, save before closing the popup if you want to keep the layout.

## Profiles

Builder interface profiles save a complete builder interface layout that can be reused.

In the **Profiles** section, you can:

- **Load** an existing profile into the current popup.
- **Save as** a new profile from the current layout.
- **Overwrite** the selected profile.
- **Rename** the selected profile.
- **Delete** the selected profile.

Profiles are useful when different people need different builder workspaces. For example, a designer might use a wide control panel and visible Structure panel, while a content editor might use fewer toolbar items and a simplified bottom dock.

> **Note**
>
> Bricks applies profiles after personal builder interface preferences. If a setting exists in both places, the assigned profile wins. Use profile assignments when you want a role or user to consistently receive a specific builder workspace.

Saving a profile does not assign it automatically. Assign profiles under Builder access after creating them.

## Assign profiles to roles or users

After creating profiles, assign them under `Bricks -> Settings -> Builder access -> Builder interface profile`.

Each WordPress role can use:

- **Default**
- Any saved builder interface profile

You can override the role assignment for a specific person by editing that user's WordPress profile and selecting a **Builder interface profile**.

![](https://academy.bricksbuilder.io/assets/builder-interface-profiles-user-roles.webp)

If a user has multiple roles with different profile assignments, Bricks uses the first matching role assignment from the user's role list.

Deleting a profile removes any role and user assignments that pointed to that profile.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-profiles.webp)

## Import and export

Open the import/export icon in the Builder interface popup to move layouts between sites or browsers.

![](https://academy.bricksbuilder.io/assets/bricks-builder-interface-import-export.webp)

You can export or import:

- Current builder interface settings
- The selected profile
- All profiles

Importing builder interface settings overrides the current builder interface settings. Importing profiles does not import role or user assignments.

When imported profiles conflict with existing profile IDs, Bricks lets you overwrite, import as a copy, or skip each profile. Conflicting profiles are skipped by default until you choose another option.

## Reset another user's preferences

Admins can reset another user's saved builder interface preferences from that user's WordPress profile.

In the user's WordPress profile, find **Builder interface** and click **Reset builder interface**. This removes that user's custom builder interface preferences, including personal keyboard shortcuts in Bricks 2.5, and restores the default or assigned profile settings on the next builder load.

## Troubleshooting

- **The Builder interface entry is missing:** Check that the user has **Customize builder interface** or **Manage builder interface profiles**, and that **Disable builder interface customiser** is not enabled.
- **A user's saved layout does not appear after reload:** Check whether a builder interface profile is assigned to the user's role or user account. Assigned profiles override personal preferences.
- **A toolbar item will not hide:** Required toolbar items cannot be hidden.
- **A profile is missing after deletion:** Deleting a profile also removes role and user assignments for that profile.
- **Profile assignments did not move during import:** Importing profiles does not import role or user assignments. Assign the profiles again under **Builder access**.

---

# Drafts

Source: https://academy.bricksbuilder.io/builder/interface/drafts/

*Save pending changes to a Bricks page, preview them against the live site, and review them before publishing.*

Bricks 2.5 drafts let you save changes to an existing page and its templates before making them live. Use a page draft for one page, or a named [site version](https://academy.bricksbuilder.io/builder/interface/site-versions/) when work spans several pages.

Drafts are **experimental** and disabled by default.

> **Shared items and live pages**
>
> Reusable items that do not affect live content become available across the site immediately. Changes that affect live content stay in the draft until you publish. See [what stays in the draft](#shared-data) for examples and the rules for shared styles.

## Enable drafts

1. In WordPress, open **Bricks > Settings > Builder**.
2. Under **Drafts**, select **Enable drafts** and save the settings.
3. Reload the Builder.

![Experimental Drafts settings with Enable drafts and Enable review links checked.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/drafts-settings.webp)

A version switcher appears just before **Save** in the toolbar. It shows **Live** when you are editing the live version, **Draft** for a page draft, or the name of an open site version.

## Save a page as a draft {#save-as-draft}

1. Open the page in Bricks. You can make your edits before creating the draft.
2. Open the **Live** menu next to Save.
3. Select **Save page as draft**. The label follows the post type, such as **Save post as draft** or **Save template as draft**.
4. Bricks switches to **Draft** and saves your unsaved changes into it. Continue editing and use **Save** as usual.

There is one active page draft per page. If the page already has a draft, select **Draft** in the version menu to continue working on it.

![The Atelier North page open in Draft, with Discard, Publish, and the unchanged Save control in the toolbar.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/draft-builder.webp)

### What Save does

| Current version | Save behavior |
| --- | --- |
| **Live** | Saves directly to the page and shared data, using the normal conflict checks. Changes to a published page can appear to visitors immediately. |
| **Draft** | Saves the page's pending changes into its Bricks draft, subject to the shared-data rules below. |
| A named **site version** | Saves into that version, which can include several pages. |

Enabling drafts does not change Live saves into draft saves. Check the version switcher before saving.

A **Bricks page draft** is separate from a **WordPress draft post**. The former holds pending Bricks changes; the latter is a post whose publication status is Draft. Creating a Bricks draft does not change the WordPress post's status.

## What stays in the draft {#shared-data}

When you create a new class in a draft using the style controls, it becomes available immediately in the site's class library. You can use it on other pages and templates as you work. Adding the class to the library does not apply it to existing live pages.

For example, create a `.service-card` class for a card in your page draft. You can immediately assign it to a card on another page or template, without publishing the first page's draft.

If you edit a class that live pages already use, its changes stay in the draft until you publish. Saving those changes directly to the shared class would also change the pages visitors see. Your draft shows the edited class; live pages keep its published styles.

Bricks checks whether an item affects live content. Edits to an existing class that no live content uses are shared immediately too.

| Change | Behavior |
| --- | --- |
| Page content, page settings, and templates edited within the draft | Held until you publish the draft. Publishing a template change affects every page where that template applies. |
| Theme Styles, breakpoints, and Style Manager settings | Held until you publish, because these can affect the site without an individual page reference. |
| Classes, components, variables, palettes, queries, filters, icons, or fonts already used on the live site | Changes are held until you publish. |
| Reusable items that do not affect live content, including new classes and components | Saved immediately to the site's shared library, ready to use on other pages and templates. |

Classes containing custom CSS that targets elements outside the class stay in the draft even when the class is new or unused. That CSS could change live pages without the class being assigned to them.

If Bricks cannot establish that sharing an item is safe, it keeps the change in the draft. Private and scheduled content also counts when checking usage. The save notice tells you which items were shared immediately and which stayed in the draft.

A draft keeps the changes you make, rather than freezing the whole site. Items you have not changed continue to follow the live site. A later live update can therefore appear in your draft preview.

### Boundaries

Drafts cover supported Bricks design changes. They are not a copy of the WordPress installation or database:

- Media uploads and changes to the Media Library are shared. Uploading a file while working in a draft does not make that file private.
- New WordPress posts and changes made outside the draft's Bricks workflow are not staged by the page draft. This includes block editor edits, plugin settings, and external systems.
- Builder preferences, such as pinned elements and favorite fonts, are not pending design changes.
- An action that Bricks cannot support in a draft is refused with a message asking you to open the live version.

## Preview and compare

Save the draft, then open its version menu and choose **Compare with live**. This opens the draft and live page together. See [Explore and compare](https://academy.bricksbuilder.io/builder/interface/explore-alternatives/) for comparison controls and alternatives.

A normal draft preview requires a logged-in user with permission to edit that draft. To show it to someone without a login, enable and create a [review link](https://academy.bricksbuilder.io/builder/interface/review-links/). Copying the Builder or preview URL alone does not grant access.

## Publish a draft {#publish}

1. While editing **Draft**, click **Publish** beside the version switcher.
2. Review **Pages and templates** and **Shared styles**. Bricks saves any remaining unsaved draft edits before loading this review.
3. Resolve any conflicts, then click **Publish draft**.
4. Wait for confirmation. The Builder returns to **Live** and the page draft closes.

On narrower screens, **Publish draft…** and **Discard draft…** move into the version menu. At smaller widths, the switcher shows a version icon instead of its text label; its tooltip still identifies the current context.

![Publish draft review listing the Services page and the service-card class used on a live page.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/draft-publish.webp)

Shared styles can affect more than the page you are editing. Review them before publishing: a component, class, or Theme Style may be used throughout the site.

### If live changed while you worked

Bricks compares the pending changes with the current live site. When both sides changed an item differently, choose **Your draft** or **The live version** for that conflict. When page content can be combined, the dialog asks only about conflicting elements and combines the other changes.

Publishing stays blocked until the conflicts have choices. If the draft or live data changes again during review, Bricks can require another review. Keeping the live version leaves that item as it is on the live site.

These publish decisions are separate from [conflicts while saving shared data](https://academy.bricksbuilder.io/builder/interface/save-publish/#save-conflicts) between open Builder sessions.

### Undo a publish

When a publish changes live data, Bricks keeps the values it replaced. Click **Undo** in the published confirmation, or open **Manage versions…** and find the recent entry under **Undo a publish**.

Undo restores those replaced values; it is not a restore of the entire site. If someone changed those values again, undo can stop with a conflict instead of replacing their later work. Save or discard any unsaved Live edits before undoing.

For one class, variable, component, or another supported shared item, [Global data history](https://academy.bricksbuilder.io/builder/interface/global-data-history/) offers a separate way to restore an earlier value.

## Discard a draft

Click **Discard** beside the version switcher and confirm. Bricks removes the draft's pending changes and opens the live page.

If the draft created shared items that are still unused, Bricks offers **Discard, keep them** or **Discard and delete them**. It checks for usage before deleting them, including references from other open drafts.

Discarding does not undo edits to existing unused shared items that were already saved live. Those changes were outside the draft's pending changes.

## Return later or move to another page

Opening a page with an active page draft automatically opens that draft for users who can edit it. Select **Live** in the version menu when you deliberately want to work on the live page. That explicit choice is kept when the Builder reloads the same live context.

A page draft stays with its page and the templates you edit within it. Navigating to an unrelated page leaves that page draft; the destination opens in its own context, including its own draft if present. Use a [site version](https://academy.bricksbuilder.io/builder/interface/site-versions/) when those pages need to share the same pending changes.

Before switching versions or navigating away, Bricks saves unsaved draft edits and stops the switch if saving fails. Switching from Live with unsaved changes asks for confirmation before replacing them, so save those edits first if you need them.

## Access and availability

A page draft is not restricted to its creator. Other logged-in users who can edit the page and use Bricks on it can open the same draft. Their existing Builder permissions still control which changes they may make.

Publishing also checks the permissions needed for every included change, such as page settings, templates, shared styles, and executable code. If the draft contains changes you cannot publish, ask someone with those permissions to publish it. See [Builder access](https://academy.bricksbuilder.io/builder/interface/builder-access/#drafts-and-versions).

Active drafts remain available until published or discarded. Finished draft records and publish undo points are removed after 30 days by default, measured from their last update. Developers can adjust this period with [`bricks/drafts/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-drafts-keep_days/).

Turning off **Enable drafts** makes draft contexts unavailable; a save from an already open draft is refused instead of becoming a Live save. Open Live to continue, or re-enable drafts to resume the pending work.

---

# Adding & Editing Elements

Source: https://academy.bricksbuilder.io/builder/interface/editing-elements/

*Add elements to the canvas, edit their settings, and understand the main element editing workflow in Bricks.*

Elements are the building blocks of a Bricks layout. This article explains how elements are added, selected, nested, styled, reset, copied, and edited in single-element and bulk-edit workflows.

## Element mental model

A Bricks layout is an element tree. Every element has:

- A type, such as Section, Heading, Image, Button, or Form.
- A unique Bricks ID.
- Optional children if the element can contain other elements.
- A parent, unless it is a root element.
- Settings, which store content, styles, classes, conditions, interactions, custom attributes, and other element-level data.

Root elements sit at the top of the page content. Nested elements sit inside another element. The canvas shows the visual result; the Structure panel shows the actual hierarchy.

## Add an element

Open the Elements panel, then drag an element onto the canvas or into the Structure panel.

Where the element lands depends on the current drop target:

- Drop onto a nestable element to place the new element inside it.
- Drop between siblings to place the new element at that position.
- Drop at root level to create a top-level element.

You can also add layout elements from the [Context Menu](https://academy.bricksbuilder.io/builder/interface/context-menu/) when an existing nestable element is selected.

## Layout elements

The current layout elements are **Section**, **Container**, **Block**, and **Div**.

Use them as structural wrappers:

- **Section**: Common top-level page section.
- **Container**: Common content-width wrapper.
- **Block**: Generic block-level wrapper.
- **Div**: Generic wrapper with fewer layout assumptions.

Not every element can contain children. Elements that can contain children are nestable. Non-nestable elements, such as many content elements, can be moved, styled, copied, or deleted, but they cannot be used as parents.

## Select and edit an element

Click an element on the canvas or in the Structure panel to select it. The panel switches to the selected element and shows its controls.

> **Note**
>
> You can edit text directly on the canvas by clicking on it and typing. Select text portions with your mouse to reveal the text formatting toolbar with styling options such as bold, italic, and links.

The panel header shows the selected element label. You can rename the label to make the Structure panel easier to scan. The label is for builder organization and does not change the HTML tag or frontend text by itself.

The panel can also show quick actions for hide settings, conditions, interactions, Components, and legacy Global Elements depending on the selected element and your permissions.

## Content controls

Content controls affect the element's markup, data, and behavior. Examples include an Image element's image source, a Button element's link, a Heading element's text, or a Form element's fields and actions.

The screenshot below shows Content controls for the Image element:

![Panel: Content (Tab)](https://academy.bricksbuilder.io/assets/bricks-academy-panel-content-tab-1024x576.png)

<figcaption>

Element Image: Content Tab

</figcaption>

Content controls are not only for visible text. They can also control semantic tags, attributes, query settings, form behavior, media sources, links, and dynamic data.

## Style controls

Style controls affect the CSS Bricks generates for the selected element, active class, active selector, active pseudo state, and active breakpoint.

Style controls are commonly grouped into:

- Layout
- Typography
- Background
- Border / Box Shadow
- Gradient / Overlay
- Shape Dividers
- Transform
- CSS

![Panel: Style (Tab)](https://academy.bricksbuilder.io/assets/bricks-academy-panel-style-tab-1024x576.png)

<figcaption>

Element Image: Style Tab

</figcaption>

Before changing styles, check which selector is active at the top of the panel:

- If the element ID is active, styles apply only to that element.
- If a global class is active, styles apply to that class everywhere it is used.
- If a pseudo selector is active, styles apply to that selector state.
- If a breakpoint is active, responsive style values are stored for that breakpoint.

This is the most important styling habit in Bricks: select the target first, then change the control.

## Classes, selectors, and responsive edits

The selector area above the Content/Style tabs controls whether you are styling the element ID, a global class, or a selector/pseudo state.

Use global classes for reusable styling. Use the element ID for one-off styling. Use selectors and pseudo classes when styling states or child selectors.

Responsive edits are controlled by the active breakpoint in the toolbar. A control indicator can show when a control has a value at the active breakpoint or another breakpoint, depending on your builder settings.

## Bulk editing

You can select multiple elements with Cmd/Ctrl or Shift selection. Bulk editing is useful for shared style changes, class assignment, moving, hiding, deleting, and some context-menu actions.

Bulk editing has limits:

- Bricks calculates the settings shared by the selected elements.
- If selected elements have different values, the shared control can appear empty.
- Editing a shared setting applies that change to the selected elements.
- If different element types are selected, Bricks shows only the Style tab.
- Some actions are disabled in bulk mode, such as saving as a Component or Template.
- Bulk wrapping only works when selected elements share the same parent.

Use bulk editing for broad, predictable operations. For content-heavy edits, edit one element type at a time.

## Hide, conditions, and interactions

Element-level hide settings, conditions, and interactions are opened from the element panel header when available.

- **Hide element** can hide an element in the builder, on the frontend, or both.
- **Conditions** control whether the element should render for the current request.
- **Interactions** attach frontend behavior to triggers and actions.

These panels are permission-gated. If you cannot see them, check [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/).

## Components and locked editing states

When you select a Component instance, Bricks shows instance controls and exposed properties instead of treating every nested element as local page content. To edit the Component definition, enter Component editing mode.

Some elements may also be disabled through the Element Manager or unavailable because their element type no longer exists. In those cases, Bricks shows a notice instead of normal controls.

Legacy Global Elements can still appear on existing sites. Bricks marks them as deprecated and recommends Components for new reusable content.

## How To Reset Controls

Controls that have a stored value show a small indicator next to the control label or group label. Hover the indicator to reveal the reset action.

You can reset:

- A single control.
- A control group, such as Typography.
- Element ID styles.
- Active class styles, if you are styling a class and it is not locked.

Resetting style controls removes the stored style values for the current target. It does not remove content such as text, links, form fields, or image selections.

When styling a global class, resetting styles affects that class, not only the selected element.

## Copy & Paste Styles

To copy and paste element styles, right-click an element on the canvas or in the Structure panel to reveal the context menu. Use **Copy Styles**, then select the target element and use **Paste Styles**.

Style paste respects the copied style data and the current target:

- Pasting element styles applies copied style settings to the target element.
- Pasting global class styles applies copied class style settings when a class is the active target.
- Shape dividers, custom CSS, and other complex style controls are handled as style data when supported.

For more copy and paste actions, including classes, conditions, interactions, and attributes, use the [Context Menu](https://academy.bricksbuilder.io/builder/interface/context-menu/).

## Practical editing checklist

Before making a change, confirm:

- The correct element is selected.
- The correct selector is active: element ID, class, or pseudo selector.
- The correct breakpoint is active.
- You are editing Content for markup/data changes or Style for CSS changes.
- You are not accidentally editing a Component definition when you meant to edit an instance.
- You have saved before testing frontend behavior.

---

# Start Editing With Bricks

Source: https://academy.bricksbuilder.io/builder/interface/editing-with-bricks/

*Start editing with Bricks by understanding the builder layout, canvas behavior, and the basic flow for working on a page.*

This article explains how to open the Bricks builder, what each main area of the interface does, and how editing with Bricks relates to rendering the page on the frontend.

## Before you open the builder

Bricks shows builder entry points when the current post can be edited with Bricks:

- The current user has permission to use the builder.
- The post type is enabled for Bricks.
- The post can be edited by the current user.

Bricks checks the license when the builder opens. If the license is not valid, Bricks redirects to the [license screen](https://academy.bricksbuilder.io/builder/license/license-and-updates/) instead of loading the builder.

Go to **Bricks -> Settings** and select the post types you want to edit with Bricks:

![](https://academy.bricksbuilder.io/assets/bricks-settings-post-types.png)

> **Note**
>
> While you can enable Bricks for blog posts, most sites work better when posts are written in the WordPress editor and displayed through a Bricks template. Use Bricks for the layout, and use WordPress for the editorial content.

## Open the builder

You can open the builder from several places in WordPress.

### Posts list

Hover over a supported post, page, or custom post type in the WordPress dashboard and click **Edit with Bricks**:

![](https://academy.bricksbuilder.io/assets/docs-edit-with-bricks-button.png)

### Post edit screen

When editing an existing post or creating a new one, click **Edit with Bricks** in the Bricks editor area:

![](https://academy.bricksbuilder.io/assets/bricks-post-edit-screen-1024x576.png)

### Frontend admin bar

When you are logged in and viewing the page on the frontend, use the WordPress admin bar. The Bricks menu can open the current page, the active header template, the active content template, the active footer template, or the Templates screen when those links apply to the current page.

If the **Edit with Bricks** link is missing, check the current user's builder permissions and make sure the post type is enabled under **Bricks -> Settings**.

## Edit with Bricks vs render with Bricks

Editing with Bricks opens the visual builder. Rendering with Bricks controls which content source the frontend uses.

A post can have WordPress editor content, Bricks data, or both. The **Render with Bricks** / **Render with WordPress** option in the admin bar switches the editor mode for the current post. If a post is set to render with WordPress, its Bricks data remains stored, but the frontend uses the WordPress content instead.

Bricks templates are different. Templates are Bricks documents by definition, so the editor mode toggle does not apply to them.

Use the render mode deliberately:

- Choose **Render with Bricks** when the page itself is built in Bricks.
- Choose **Render with WordPress** when the page should use normal WordPress content, usually with a Bricks template controlling the surrounding layout.
- Do not use the render toggle as a content backup system. It only chooses the frontend render source.

If a page is rendered with Bricks, the post list shows a **- Bricks** status after the title:

![](https://academy.bricksbuilder.io/assets/bricks-post-screen-post-status.png)

<figcaption>

Post status "Bricks" shows you that a page is rendered with Bricks

</figcaption>

## Delete Bricks data

The admin bar and post edit screen can show a **Delete Bricks data** button when this option is enabled in **Bricks -> Settings**.

This removes Bricks-generated data from the current post, including page content, page settings, header/footer data, editor mode, and template type metadata. Treat it as destructive. Use it only when you want the post to stop using its stored Bricks layout data.

## Builder anatomy

The builder is made of four main working areas.

### Toolbar

The toolbar runs across the top of the builder. It gives you access to global builder actions and mode switches, including:

- Style Manager
- Pages panel
- Templates
- Settings
- Command Palette
- Elements and Components
- Breakpoints
- Preview width, height, and scale
- Reload canvas
- Undo and redo
- Preview and save actions

Which buttons you see depends on your permissions and global builder settings. For example, template actions require template permissions, and the breakpoints manager requires breakpoint access.

### Panel

The left panel changes depending on what you are doing. It can show the element library, the selected element controls, page/template settings, revisions, pages, or other manager views.

The panel can be resized and minimized. When an element is selected, the panel shows the element label, element actions, class/selector controls, and the relevant Content and Style controls.

### Finding another page {#pages-panel}

Open **Pages** from the builder toolbar and choose the post type you want to browse. Since Bricks 2.5, results load in batches as you scroll. Use the search field to find a title anywhere in the available results, including pages that have not loaded into the list yet.

Use the star beside a result to add or remove a favorite. Favorites are kept separately for each post type and saved in your browser. They can include pages outside the first batch of results. The current search also applies to the favorites list.

Save your current changes before opening another page. If loading fails, use the panel's retry control.

### Canvas

The canvas is the live visual preview of the current page. It renders the Bricks layout in an iframe, so selecting and editing elements feels close to editing the frontend output.

The canvas can be reloaded from the toolbar. Reloading is useful after changing settings that need a fresh render, or when external scripts, query data, or dynamic content affect the preview.

### Structure panel

The Structure panel shows the element tree. It is the safest place to understand nesting, select hard-to-click elements, move elements, and work with deeply nested layouts.

Use the Structure panel whenever the canvas view is visually crowded, an element is hidden, or you need to confirm parent-child relationships.

In Bricks 2.5, use **Search structure** to find elements by name, text, ID, class, and more. The funnel button filters elements by features such as query loops, conditions, and interactions. Clear the search and filters before dragging elements in the panel. See [Structure Panel Search and Filters](https://academy.bricksbuilder.io/builder/interface/structure-panel-search/).

Since Bricks 2.5, the Structure panel can show HTML tags beside element labels. Choose **Icons**, **HTML tags**, or **Icons and HTML tags** under **Bricks > Settings > Builder > Structure panel > Element display** and save the settings. This helps you distinguish, for example, a heading rendered as `h2` from a wrapper rendered as `div`.

The displayed tag follows the root rendered on the canvas. If no rendered root is available, Bricks falls back to the element icon. Component and slot indicators remain available.

<div className="screenshot screenshot--control-panel">

![Structure panel showing icons and HTML tags for a Section, a div Container, an h3 Heading, and a Basic Text paragraph.](https://academy.bricksbuilder.io/assets/builder/structure-panel/structure-panel-icons-html-tags.webp)

</div>

## First successful edit workflow

Use this workflow when creating or editing a normal page:

1. Enable the page post type under **Bricks -> Settings**.
2. Create or open the page in WordPress.
3. Click **Edit with Bricks**.
4. Open the Elements panel and add a layout element, such as a Section or Container.
5. Add content elements inside the layout.
6. Select an element on the canvas or in the Structure panel.
7. Edit its Content controls for markup and data.
8. Edit its Style controls for design.
9. Switch breakpoints and adjust responsive styles where needed.
10. Save the builder.
11. Preview the page and confirm it is rendered with Bricks.

## Common builder states

### Preview mode

Preview mode hides the normal editing controls so you can inspect the layout. While previewing, builder editing actions such as the custom context menu are disabled.

### Unsaved changes

The builder tracks history and unsaved changes. Use save before leaving the builder, switching important context, or testing frontend-only behavior.

### Unsupported post type

If a post type is not enabled for Bricks, Bricks redirects you back to WordPress admin instead of opening the builder. Enable the post type under **Bricks -> Settings** or use a Bricks template for that content type.

### Missing permissions

Users can have full access, content-editing access, or custom permission sets. Missing permissions can hide toolbar buttons, element categories, manager popups, settings panels, and editing controls. Review [Builder Access](https://academy.bricksbuilder.io/builder/interface/builder-access/) if a user can open the builder but cannot see or edit a specific area.

### Login or license redirects

If the builder detects that the current browser session is no longer logged in, it redirects to the login page. If the license is not valid, Bricks redirects to the [license screen](https://academy.bricksbuilder.io/builder/license/license-and-updates/).

## Troubleshooting checklist

- **No Edit with Bricks button:** Check post type support, user permissions, and whether the current user can edit the post.
- **The page opens in WordPress instead of Bricks:** Confirm the page has Bricks data or switch the admin bar render mode to **Render with Bricks**.
- **Builder opens but controls are missing:** Check builder permissions and whether the selected element is disabled.
- **Canvas looks stale:** Reload the canvas from the toolbar.
- **Page looks different on the frontend:** Save the builder, confirm render mode, and test outside preview mode.

---

# Explore Alternatives and Compare

Source: https://academy.bricksbuilder.io/builder/interface/explore-alternatives/

*Preview alternative copy and styles, compare drafts with the live site, and apply a chosen combination before publishing.*

Explore lets you try prepared alternatives, such as two headlines or several accent colors, on a draft. Compare shows up to four views of the same page so you can inspect different combinations, [page drafts](https://academy.bricksbuilder.io/builder/interface/drafts/), [site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/), or the live site together.

## Requirements

Explore and Compare are available in Bricks 2.5 with **Enable drafts** turned on under **Bricks → Settings → Builder**. Drafts are experimental and disabled by default.

You need an active draft or site version that your account can edit. The **Explore alternatives** entry appears only when that version already contains alternatives. **Compare with live** works without alternatives.

Alternative groups are currently created through [Bricks abilities](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/), for example by a connected AI assistant using `bricks/create-alternatives`. The Builder provides the interface for previewing and applying those groups; it does not have controls for creating groups or writing their choices manually.

## Prepare alternatives

Each **group** represents one decision, such as Headline or Accent color. Each **choice** contains proposed changes to existing element settings, global class settings, or variable values. You can select one choice per group and combine choices from different groups.

For example, ask a connected assistant:

> In the page's draft, prepare two headline alternatives and two accent-color alternatives. Keep the existing elements. Put headlines and colors in separate groups so I can mix them, and give me the Explore and Compare links.

The assistant can use an existing page draft, create one if needed, or work in a specified site version. Preparing alternatives saves the options for review without applying their proposed changes.

## Open Explore or Compare

While editing a draft or site version, open the version menu beside Save:

- Choose **Explore alternatives** to preview its groups in one view.
- Choose **Compare with live** to open the version and live page together.

These views open over the Builder. If the current draft has unsaved edits, Bricks saves them into the draft before opening the view. Click **Close** to return to editing.

In **Manage versions**, select a version and click **Compare**. An editor can also open an Explore or Compare link returned by the connected assistant. These editor links require a login and permission to edit the version; use a [review link](#review-links) for someone without an account.

<div className="screenshot screenshot--control-panel">

![The compact draft menu with Publish, Discard, Compare with live, and Explore alternatives.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/draft-menu.webp)

</div>

## Try a combination

The options panel shows the active view's groups. Select a choice under each group you want to change. Choose **As drafted** to show that group's current saved draft values without an alternative applied.

For example, select the second Headline and the first Accent color. The page preview shows that combination. Switching choices previews their effect without saving those choices to the draft or publishing them.

![Explore showing independent Headline and Accent color groups with Room to grow and Terracotta selected.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/explore-alternatives.webp)

If a view has no alternative groups, the options panel is hidden. You can still compare its page with another view.

## Compare views {#compare}

Click **Add view** to copy the active view and its current choices. Then use the version selector in each view's header to choose the page's **Draft**, an available named site version, or **Live site**.

Click a view's header to make it active. Its border is highlighted, and the options panel changes to the groups belonging to that view's version. Each view keeps its own combination. Changing one view's version clears its previous alternative selections.

For example, compare:

| View | Version | Alternatives |
| --- | --- | --- |
| 1 | Live site | Current published page |
| 2 | Autumn services | Clear direction headline, Forest accent |
| 3 | Autumn services | Room to grow headline, Terracotta accent |

The selectors offer drafts and site versions you can edit. A page draft belongs to its own page; another page's draft is not offered for this comparison. Site versions show the current page within that version.

![Live site compared with two Autumn services combinations, with the third view active and its own choices shown.](https://academy.bricksbuilder.io/assets/builder/drafts-and-versions/compare-views.webp)

Up to four views are supported. Use **Expand** to inspect one at a larger size, then **Show all views** to return. The × button removes a view from the comparison without deleting its draft or site version.

### Responsive previews and scrolling

The breakpoint buttons use the site's configured Bricks breakpoints. Choosing a width changes every view together. Each page renders at that width and scales down to fit its available space, so a desktop page can remain a desktop preview inside a narrow comparison pane.

Scroll one page view to move the others to the same vertical position. Switching alternative choices keeps the view's scroll position where the new content allows it. Pages with different heights may not line up exactly.

## Apply a combination {#apply}

Select the view containing the combination you want, then click **Apply to draft**. Bricks applies that view's selected choices to its own draft or site version. Groups left on **As drafted** keep their current values. Applying requires the same permissions as editing the affected page, classes, or variables directly.

Applying does not publish the page. Close the view to return to the Builder. If you applied choices to a different site version, select that version in the toolbar to continue editing it. Use the draft or site version's publishing workflow when it is ready.

Shared classes and variables follow the [drafts shared-data rules](https://academy.bricksbuilder.io/builder/interface/drafts/#shared-data): changes affecting live content stay in the draft until publication. Updates that do not affect live content are shared across the site immediately, ready to use on other pages and templates. Applying alternatives uses the same rules.

After applying, **As drafted** shows the updated draft. Selecting it does not undo a combination you already applied. If Bricks reports that the alternatives changed since you opened them, reload the view and review the current choices before applying again.

## Review links {#review-links}

With [review links](https://academy.bricksbuilder.io/builder/interface/review-links/) enabled, you can share a draft or site version with someone who does not have a WordPress login. When it contains alternatives, the review panel includes **Explore alternatives**.

Reviewers can switch options and add views to inspect combinations within the shared version. Their view has no version selector and no **Apply to draft** button. They cannot publish, save a preferred combination, or submit comments through the review link. Ask them to send their feedback separately.

For recovering an earlier saved class, variable, component, or other shared item, use [Global data history](https://academy.bricksbuilder.io/builder/interface/global-data-history/).

---

# Keyboard Shortcuts

Source: https://academy.bricksbuilder.io/builder/interface/keyboard-shortcuts/

*Customize Bricks keyboard shortcuts, restore defaults, share your settings, and use shortcuts with Builder Interface profiles.*

Keyboard shortcuts let you save, open panels, edit elements, and move through the builder without reaching for the toolbar. In Bricks 2.5, you can change, remove, restore, import, and export those shortcuts.

`CMD` means Command on macOS. Use `CTRL` on Windows and Linux. The shortcuts below show the Bricks defaults; your personal settings or an assigned [Builder Interface profile](https://academy.bricksbuilder.io/builder/interface/builder-interface-customiser-profiles/) can change them.

## Open Keyboard shortcuts

Open **Manage** in the builder toolbar, then click **Keyboard shortcuts**. It is also available from the [Command Palette](https://academy.bricksbuilder.io/builder/interface/command-palette/).

<div className="screenshot screenshot--control-panel">

![The builder settings list with Keyboard shortcuts directly below Filter Manager.](https://academy.bricksbuilder.io/assets/keyboard-shortcuts/keyboard-shortcuts-settings.webp)

</div>

The manager lists commands by category. Search for an action or shortcut, or select a category such as **Workspace**, **Editing**, or **Elements**. Each row shows the action, its context, the source of its shortcut, and the current key combination.

![The Keyboard shortcuts manager with category filters, current bindings, and Remove and Reset controls.](https://academy.bricksbuilder.io/assets/keyboard-shortcuts/keyboard-shortcuts-manager.webp)

Changing your personal shortcuts requires the **Customize builder interface** permission. See [Builder access](https://academy.bricksbuilder.io/builder/interface/builder-access/) for role and user permissions.

## Change a shortcut

For example, to change the Preview shortcut:

1. Search for **Preview**.
2. Click its current shortcut. The button shows **Press shortcut keys**.
3. Press your preferred combination, such as `CMD / CTRL + ALT + U`.
4. Click **Save**.

The new shortcut is saved for your WordPress user account on this site. Reload the builder and press the new combination to toggle Preview.

![Preview remapped to Command, Option, and U.](https://academy.bricksbuilder.io/assets/keyboard-shortcuts/keyboard-shortcuts-remap.webp)

Press `ESC` to stop recording a combination. `TAB` also leaves recording and moves focus to the next control. **Cancel** closes the manager without saving your changes.

### Remove or restore a shortcut

- Click the **Remove** (trash) icon to disable that command's shortcut. The action remains available through its normal builder controls.
- Click the **Reset** icon beside a command to remove your override and inherit its default again.
- Click **Reset** in the footer to clear all your shortcut overrides.

Click **Save** to keep removals or resets. Resetting shortcuts does not reset your toolbar or panel layout. If restoring a default would create a conflict, change the other conflicting shortcut first.

### Conflicts and reserved keys

Bricks rejects combinations that would trigger conflicting commands. The message names the conflicting command, and the existing shortcut stays unchanged. Choose a different combination or change the other command first.

![A conflict message explains that the attempted Save shortcut is already used by Command palette.](https://academy.bricksbuilder.io/assets/keyboard-shortcuts/keyboard-shortcuts-conflict.webp)

Some combinations are reserved for browser, operating-system, or accessibility behavior. For example, you cannot assign a global command to `CMD / CTRL + L`, which focuses the browser address bar, or to an unmodified letter. `ESC` and `TAB` keep their built-in behavior.

A warning can appear for combinations used by text editing or browser printing. Read the warning before choosing **Use anyway**. Text and code editors keep their own editing behavior where needed, so a canvas shortcut can behave differently while you are typing in an input or editor. Copy, Paste, Undo, and Redo act on text while a text editor owns the focus.

## Shortcut sources and profiles

Bricks resolves shortcut settings in this order:

1. Bricks defaults.
2. Site defaults.
3. Your personal preferences.
4. An assigned Builder Interface profile.

An assigned profile takes priority for the commands it defines. Those rows show the profile name and are read-only in your personal shortcut manager. Other commands remain customizable when your permissions allow it.

If a profile uses a combination assigned to another command in your preferences, Bricks suppresses the conflicting lower-priority shortcut. Your stored preference is kept. Removing the profile assignment restores it, or you can choose a different personal combination while the profile is assigned.

To include shortcuts in a reusable profile, open **Builder interface → Keyboard shortcuts → Manage**. Edit the shortcuts and click **Save** to return to the Builder Interface draft. Then save or overwrite the profile. Saving a profile does not assign it to users automatically. See [Builder Interface Customiser and Profiles](https://academy.bricksbuilder.io/builder/interface/builder-interface-customiser-profiles/#keyboard-shortcuts).

## Import and export

Click the import/export icon in the manager header.

- **Export** downloads your shortcut customizations as a JSON file, including shortcuts you have disabled. It does not export the full workspace layout or every inherited default.
- **Import** adds the file's customizations to your current shortcut settings. Click **Save** after a successful import to keep them.

If the file contains conflicting, reserved, unsupported, or profile-managed bindings, Bricks rejects the import without applying part of the file. Export and import a full Builder Interface profile when you want to share both the workspace layout and its shortcuts.

## Default shortcuts

These combinations are customizable in Bricks 2.5. Actions still require the relevant builder permissions and selection or editor context.

| Shortcut | Action |
| --- | --- |
| `CMD / CTRL + S` | Save changes |
| `CMD / CTRL + SHIFT + S` | Force save all data |
| `CMD / CTRL + K` | Open Command palette |
| `CMD / CTRL + .` | Toggle Style Manager |
| `CMD / CTRL + SHIFT + .` | Toggle Builder Browser |
| `CMD / CTRL + SHIFT + L` | Open Templates in the Builder Browser |
| `CMD / CTRL + P` | Toggle Preview |
| `CMD / CTRL + SHIFT + V` | View on frontend |
| `CMD / CTRL + B` | Go to the next breakpoint |
| `CMD / CTRL + SHIFT + E` | Open Elements and focus its search |
| `CMD / CTRL + SHIFT + C` | Open Components |
| `CMD / CTRL + SHIFT + X` | Toggle Structure |
| `CMD / CTRL + F` | Focus [Structure search](https://academy.bricksbuilder.io/builder/interface/structure-panel-search/) when outside a text field and there are elements to search |
| `CMD / CTRL + SHIFT + H` | Open History |
| `CMD / CTRL + SHIFT + F` | Search element controls |
| `CMD / CTRL + Z` | Undo a builder change |
| `CMD / CTRL + SHIFT + Z` | Redo a builder change |
| `CMD / CTRL + C` | Copy selected elements |
| `CMD / CTRL + V` | Paste copied elements |
| `CMD / CTRL + SHIFT + D` | Duplicate selected elements |
| `CMD / CTRL + Delete` | Delete selected elements and their children |
| `CMD / CTRL + ENTER` | Toggle classes for the selected element |
| `CMD / CTRL + SHIFT + P` | Wrap the selection in the configured wrapper element |
| `CMD / CTRL + SHIFT + ARROW LEFT` | Select the parent element |
| `CMD / CTRL + SHIFT + ARROW RIGHT` | Select the first child element |
| `CMD / CTRL + SHIFT + ARROW UP` | Select the previous element at the same level |
| `CMD / CTRL + SHIFT + ARROW DOWN` | Select the next element at the same level |
| `CMD / CTRL + ENTER` in the media picker | Insert the selected media |
| `CMD / CTRL + R` in a focused Code control | Run code, when code execution is allowed |

The same combination can serve different actions in separate contexts. For example, `CMD / CTRL + ENTER` inserts selected media while the media picker is open, and opens the classes UI when an element is selected on the canvas.

## Built-in interaction keys

These keys belong to focused controls, navigation, or direct manipulation and cannot be remapped. Expand **Built-in interaction keys** at the bottom of the manager to see the list.

| Keys | Behavior |
| --- | --- |
| `ESC` | Close or dismiss the current popup or editing state |
| `TAB` / `SHIFT + TAB` | Move keyboard focus |
| `ENTER` / `SPACE` | Activate a focused control |
| `ALT / OPTION + T` | Focus the builder toolbar, then use Tab to move through it |
| `CMD / CTRL + ALT + 1–9` | Open an element-control quick-access group |
| Number keys in Browser or Style Manager | Switch visible sections or tabs when focus is outside a text field |
| `CMD / CTRL + ENTER` in Command palette | Insert the element structure from the focused palette |
| `ENTER` / `SHIFT + ENTER` in Structure search | Select the next / previous match |
| `CMD / CTRL + G` / `CMD / CTRL + SHIFT + G` in Structure search | Select the next / previous match |
| `CMD / CTRL` while inserting | Insert outside the active parent element |
| `SHIFT` while editing on the canvas | Use the existing precision, selection, or direct-edit modifier for that action |

Arrow-key navigation, typing, and native editing shortcuts in text fields, rich-text editors, code editors, and picker lists remain owned by those interfaces.

While typing in a field or editing text inline, Undo and Redo use the text editor's history. Leave the field or finish inline editing to use these shortcuts for builder changes.

---

# Global Data Revisions

Source: https://academy.bricksbuilder.io/builder/interface/global-data-history/

*Browse and restore earlier versions of individual classes, components, variables, and other shared Bricks data.*

Global data revisions, available since Bricks 2.5, keep earlier versions of shared Builder items. Restore one component or class without replacing newer changes to the rest of your design system. It also lets you recover an item that was deleted.

Revisions are recorded by default. You do not need to enable experimental Drafts to use them.

## Open the revisions

Open **Manage > Global data revisions** in the Builder toolbar. The dialog lists these data types in its sidebar: **Theme styles**, **Classes**, **Variables**, **Colors**, **Components**, **Queries**, and **Query filters**. Type shortcuts 1 to 9 select a type, and Bricks remembers your last type and sort order.

<div className="screenshot screenshot--control-panel">

![The Manage panel with History / Revisions and Global data revisions listed below Theme styles and Page settings.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-settings-panel.webp)

</div>

You can also open the revisions of one data type from where you edit it. Each opens the dialog on that type:

- **Style manager**: the revisions icon on the selected **Theme styles**, **Classes**, **Variables**, or **Colors** item.
- **Class and variable editors**: the **Revisions** button.
- **Browser**: the revisions icon on **Components**, **Query manager**, or **Filter manager**. A component's own **Revisions** icon in the Browser, or on its row in the Components panel, opens that component directly.

![Style manager with the Classes type selected. A revisions icon appears beside Classes and a Revisions button sits under the selected class.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-style-manager-entry.webp)

![The Browser with Components selected. A revisions icon appears beside Components in the sidebar.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-browser-entry.webp)

## Browse an item's revisions

1. Select a data type in the sidebar.
2. Find an item with the search field, which also searches deleted items, or sort the list. Classes, variables, components, queries, and filters also have a categories column, as in their managers.
3. Select an item. Click it again to deselect it.

Theme styles open directly on the active style. Use the style switcher to pick another one. Colors are listed one by one, and each palette appears as a category. A color's revisions come from the revisions of its palette.

An item's revisions form a timeline of cards, newest first. The newest card opens with the item. Select a card to expand or collapse it, or use **Expand all** and **Collapse all** in the item header. The header shows the number of revisions and when the item last changed.

Each card shows the action, such as **Created**, **Changed**, or **Deleted**, along with tags and when and by whom the change was made. A **Current** tag marks the version the site uses now. Source tags such as **AI agent**, **WP-CLI**, **Import**, **Published draft**, or **From a draft** show where a change came from. A change made by hand in the Builder has no source tag. A **Restored** tag marks a revision created by a restore.

An open card lists its changes, one setting per row. Each row shows the setting name with its section underneath, then the old value, an arrow, and the new value. Empty values read **Not set**, colors appear as swatches, and multi-line values such as custom CSS appear as code blocks with the old value dimmed above the new one. The oldest card lists its values under **Oldest recorded version**, because it has no earlier version to compare with. Labels come from the matching Theme styles and settings controls.

![Revisions of the btn-primary class on a timeline. The newest card compares custom CSS as code blocks and the oldest card lists its values under Oldest recorded version.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-class-revisions.webp)

Components also show a rendered preview in each card, and internal component fields are left out of the changes. The preview uses the site's styles. It does not restore the global classes, fonts, or other resources that the component used at that earlier time. Use **Open in new tab** to inspect the preview separately.

![Testimonial card component revisions with a rendered preview and the text change in the newest card.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-component-revisions.webp)

Custom fonts, breakpoints, font favorites, pinned elements, and class locks are not included in global data revisions.

## Restore an item

Each card ends with its own restore button. The current revision has none.

1. Expand the revision you want to recover.
2. Review its values and component preview, if available.
3. Click **Restore this version**. For a color, the button says **Restore this palette version**. For a deleted item, it says **Bring back**.

If you have unsaved changes to that type of global data, the button reads **Save and restore** (or **Save and bring back**) and saves them first.

Restoring saves the selected item's earlier value and updates the Builder. Other items keep their current values. Each restore is recorded as another revision, so you can return to the previous value through the same dialog.

An item's only revision is its recorded starting point and is titled **Current version**.

### Recover deleted items

An item that was deleted or moved to the trash is listed only under **Deleted**, in its own box below the categories, and not in **All** or its category. Select the item and click **Bring back** to return it to use. The item then appears under **All** again. If you open the dialog on a deleted item, it starts in **Deleted**.

![Deleted classes list with old-banner selected. Its Deleted revision shows the removed name and color and a Bring back button.](https://academy.bricksbuilder.io/assets/builder/global-data-revisions/revisions-deleted-item.webp)

### Restore inside drafts and site versions

When you are editing [a draft](https://academy.bricksbuilder.io/builder/interface/drafts/) or [a site version](https://academy.bricksbuilder.io/builder/interface/site-versions/), the dialog shows a notice that the revisions are the live site's history. The newest revision is tagged **Live** instead of **Current**, and you can restore it into the draft, because a draft does not record its own saves and may hold something else. Restored changes follow the [shared-data rules](https://academy.bricksbuilder.io/builder/interface/drafts/#shared-data). Changes affecting live content stay held until publication. Restored items that do not affect live content are shared across the site immediately. A change held in a draft enters global data revisions when it is published.

Your account needs Builder access and the relevant resource permissions. Restoring a component containing executable code also requires code execution permission.

## Retention and storage

By default, each item keeps its latest **20 versions**, plus all versions recorded in the last **90 days**. An item can therefore have more than 20 revisions. These limits are separate from the number of WordPress revisions kept for a page. Developers can adjust them with [`bricks/global_history/keep_latest`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_latest/) and [`bricks/global_history/keep_days`](https://academy.bricksbuilder.io/developer/hooks/filters/bricks-global_history-keep_days/).

Under **Bricks > Settings > Builder > Global data revisions**, you can:

- Enable **Disable global data revisions** to stop recording new changes.
- View the storage used by recorded revisions.
- Use **Delete revisions** to remove the stored revisions. This leaves your current global data in place, but the deleted revisions can no longer be restored.

Revisions cannot recover versions that were never recorded. Keep site backups for a complete recovery of WordPress content, media, settings, and files.

## Undo history, revisions, and drafts

| Tool | Use it for |
| --- | --- |
| **History** in Manage > History / Revisions | Undo and redo steps from the current editing session. |
| [Revisions](https://academy.bricksbuilder.io/builder/interface/revisions/) | Recover earlier page or template elements and page settings. |
| **Global data revisions** | Recover one recorded shared item, including a deleted item. |
| [Drafts](https://academy.bricksbuilder.io/builder/interface/drafts/) and [site versions](https://academy.bricksbuilder.io/builder/interface/site-versions/) | Hold changes affecting visitors until you choose to publish them. |

For agent workflows, the `bricks/list-global-revisions` and `bricks/restore-global-revision` abilities provide the same per-item recovery. Pass `target: "active"` to `bricks/restore-global-revision` to bring a deleted item back into use. See [Bricks AI abilities and skills](https://academy.bricksbuilder.io/builder/features/ai-abilities-and-skills/).
