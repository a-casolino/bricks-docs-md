*Create, organize, and maintain CSS classes directly in Bricks with Global Class Manager.*

The Global Class Manager is the central place to maintain your reusable CSS classes in Bricks. It is different from the class selector on an element: the element panel is for assigning and editing classes while you work on a specific element; the Class Manager is for editing custom CSS, organizing, importing, exporting, locking, deleting, and reviewing the whole class library.

Use the Class Manager when your site has more than a few reusable classes or when you maintain a design system across pages, templates, and imported layouts.

For the element-level workflow of assigning and styling classes while editing an element, see [Global CSS Classes](https://academy.bricksbuilder.io/builder/styling/global-css-classes/).

## Accessing the class manager

To access the Class Manager, click the **Style Manager** icon in the builder toolbar. Then select the **Classes** tab.

![](https://academy.bricksbuilder.io/assets/bricks-2.2-style-manager-class-manager-scaled.png)

The Class Manager can be disabled under `Bricks > Settings > General > Disable global class manager`.

Access is also permission-based. A user may be able to use the builder without having permission to access the Class Manager, create classes, edit classes, delete classes, lock classes, or copy and paste class styles.

## What the Class Manager stores

A global class is a site-level record. It can contain:

- A class ID.
- A class name.
- Style settings.
- Breakpoint-specific custom CSS.
- Custom selectors and pseudo-state settings.
- A category.

Bricks also tracks lock state, trash/restore data, and import conflict metadata around those class records so the manager can protect classes and resolve imports safely.

Elements that use a class store a reference to the class. This is why class imports and conflicts matter: a class name is what you see, but Bricks also needs to keep element references mapped correctly.

## Class Manager vs element class selector

Use the element class selector when you want to:

- Add a class to the selected element.
- Remove a class from the selected element.
- Select the active class and edit its styles through element controls.
- Work with element-specific pseudo states and custom selectors.

Use the Class Manager when you want to:

- Create or rename classes without selecting a specific element.
- Edit custom CSS for one selected class.
- Organize classes into categories.
- Bulk rename or duplicate classes.
- Lock or unlock multiple classes.
- Move classes to trash, restore them, or delete them permanently.
- Export and import classes.
- Review usage, conflicts, and imported classes.

To generate names from element labels or review the classes used by one structure, use [Generate Classes](https://academy.bricksbuilder.io/builder/styling/generate-classes/) from the Structure panel's context menu.

## Create and edit classes

In the Class Manager, use the new-class input at the bottom of the class list to create a class.

You can also select one or more classes and use the editor column to:

- Rename one class.
- Bulk rename multiple classes with find/replace, prefix, or suffix.
- Duplicate classes with find/replace, prefix, or suffix.
- Assign selected classes to a category.
- Lock or unlock selected classes.

If you rename or duplicate a class, Bricks checks for duplicate class names and skips names that would conflict.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager.png)

## Edit custom CSS for a class

Starting in Bricks 2.4, you can edit a class's custom CSS directly in the Class Manager. You do not need to find an element that uses the class first.

Select one class to open its **Custom CSS** editor in the editor column. Use `%root%` to target the selected class:

```css
%root% {
  color: firebrick;
}
```

The breakpoint navigation above the editor lets you add CSS for each responsive breakpoint. An indicator shows which breakpoints contain a value. Changes appear in the canvas preview while you edit, and the indicator on the Class Manager save button shows that the class has unsaved changes.

![](https://academy.bricksbuilder.io/assets/global-class-manager-custom-css.webp)

Click the Class Manager save button to save the CSS with the class. When global class synchronization is enabled, custom CSS changes use the same conflict checks as other class changes.

Renaming or duplicating the class preserves its custom CSS. If the stored CSS contains the previous class root selector, Bricks updates that selector for the renamed or duplicated class. CSS written outside Bricks-managed class settings is not changed.

## Categories

Categories help you organize large class libraries. They do not change CSS output by themselves; they are an organizational layer in the builder.

You can:

- Create categories.
- Rename categories.
- Reorder categories.
- Filter the class list by category.
- Export categories with the classes that belong to them.

If a class has no category, or its stored category no longer exists, Bricks treats it as uncategorized.

## Search, sorting, and filters

Use the Class Manager header to reduce the class list before editing or exporting.

Available filters include:

- Text include/exclude filters.
- Alphabetical sorting.
- Used on this site.
- Unused on this site.
- Used on this page.
- Unused on this page.
- Has styles.
- Has no styles.
- Locked.
- Unlocked.

Usage filters are useful for cleanup, but review results carefully before deleting classes. A class can be unused on the current page and still be used elsewhere.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-subheader.png)

## Lock classes

Locking protects classes from accidental changes. A locked class can still exist in the class library and can still be assigned where permissions allow, but its styles and custom CSS cannot be edited until it is unlocked.

If a selection contains a locked class, Bricks also blocks rename and delete actions for that selection. Unlock the class before renaming it, moving it to trash, or deleting it permanently.

Use locks for foundational design-system classes such as layout wrappers, button bases, typography classes, or generated utility classes that should not be changed casually.

Locking is permission-based. Users without lock/unlock permission cannot change the lock state.

## Trash, restore, and permanent delete

Deleting a class with an ID from the active list moves it to trash. Trashed classes can be restored from the trash view. Classes with a missing ID use the separate [recovery workflow](#classes-with-missing-names-or-ids).

When a class is restored, Bricks attempts to restore it to its previous position. If a class with the same name already exists, Bricks may rename the restored class to avoid the name conflict.

Permanent delete removes the class from the trash. Use permanent delete only after verifying that the class should not be restored.

> **Note**
>
> Moving a class to trash is not the same as removing a class from one element. Removing a class from an element only removes that element's assignment. Moving a class to trash removes the class from the active class library.

## Classes with missing names or IDs

A global class needs a name for its CSS selector and an internal ID for Bricks to track it. Imported class data can be missing either value. Starting in Bricks 2.5, affected classes show a **Missing class name** or **Missing class ID** badge in the Class Manager list. Empty values and values containing only whitespace count as missing.

If both values are missing, the class shows **Missing class ID**. These badges identify incomplete class records; they do not validate every possible CSS class name or guarantee that an import will reject invalid data.

### Restore a missing class name

A class with an ID but no name can be renamed without replacing its existing class record.

1. Open **Style Manager > Classes**.
2. Click the class marked **Missing class name**.
3. In the editor column, choose **Rename**, enter a name in the **Name** field, and click **Rename**.
4. Save your class changes with the Class Manager save button.

Until the class has a name, custom CSS editing, categorizing, locking, duplicating, exporting the selection, and drag reordering are unavailable for it. If a selection includes a class with a missing name, the corresponding selection actions are unavailable too.

If you do not need the class, use **Move to trash** in the class-list toolbar instead. Existing locks still block renaming and moving a class to trash.

![Class Manager with a class marked Missing class name selected and the Name field and Rename button visible.](https://academy.bricksbuilder.io/assets/global-class-manager-missing-class-name.webp)

### Remove a class with a missing ID

Click a class marked **Missing class ID** to open its recovery panel. The panel explains why other actions are unavailable and provides a **Remove** button.

Click **Remove**, then save your class changes. This removes the record directly from the active class library. It does not move it to trash, so it cannot be restored from the trash view.

Classes with a missing ID must be selected individually. **Select all** skips them. If you still need the class, create a replacement with a name and assign it to the relevant elements.

## Exporting and importing classes

The Global Class Manager facilitates the exporting and importing of CSS classes, making it easier to maintain a consistent styling framework across various Bricks projects.

### Exporting classes

You have two options for exporting classes:

1. **Export all:** Click the export button at the top of the manager to export the current class library.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-export-all-1024x682.png)

2. **Export selected:** Select one or more classes and click the export-selected icon in the classes column.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-export-selected-1024x682.png)

Exports include category metadata for classes that belong to a category.

### Importing classes

In the import popup, drag and drop a JSON file containing exported classes.

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-import-1024x682.png)

![](https://academy.bricksbuilder.io/assets/bricks-classes-manager-import-file.png)

## Import conflicts

When importing classes, Bricks checks for conflicts by class ID and class name.

A conflict can happen when:

- The imported class has the same ID as a local class but different data.
- The imported class has the same name as a local class.
- A template or pasted layout references a class that already exists locally.

Depending on the global class import setting, Bricks can:

- Add new classes automatically and show only conflicts for review.
- Ask you to review new classes.
- Skip conflicting classes.
- Ask you to review both new and conflicting classes.
- Map imported class IDs to existing local class IDs so inserted elements keep a valid class reference.

When reviewing an import, you can accept, reject, rename, duplicate, categorize, lock, or mark conflicting classes to override local classes.

If you're importing global classes and need to handle **conflicts** or organize new classes before they are added to your project, check out the [Global Class Import Manager](https://academy.bricksbuilder.io/builder/styling/global-class-import-manager/). This feature, introduced in Bricks 1.12, provides a structured way to resolve conflicts and categorize imported classes, ensuring a smooth and controlled workflow.

## Template and paste imports

Templates, remote templates, copied elements, and converted layouts can bring global classes with them.

When Bricks inserts content that references imported classes, it must keep the element's class references valid. If the imported class is identical to an existing class, Bricks can map the imported class to the existing one. If the class differs, Bricks can route the class through the import review workflow.

This is why reviewing class imports matters: accepting a class can change the class library, while mapping a class can make the inserted content reuse an existing local class.

## Generated CSS lifecycle

Bricks does not output every class record on every page just because it exists in the Class Manager.

Global class CSS is generated for classes that are used by elements in the current rendered context. Bricks also generates class CSS per element type so element-specific controls can output the correct selectors for that class.

Starting in Bricks 2.4, the **Output global class CSS in Class Manager order** setting under [Bricks settings](https://academy.bricksbuilder.io/builder/setup/settings/#miscellaneous) can make generated global class CSS follow the class order shown in the Class Manager. This affects same-specificity class overrides. It does not make unused classes output CSS.

This has a few practical effects:

- An unused class can exist in the Class Manager without producing frontend CSS on a page.
- A class with no styles can be assigned but may not output useful CSS.
- A class can output different generated rules depending on the element types that use it.
- If a site uses external CSS files, class changes may require Bricks to regenerate CSS files.

## Conflict detection while saving

If global class synchronization/conflict checking is enabled, Bricks can detect when another user changed global classes after your builder session loaded.

The save flow can report:

- Classes added by another user.
- Classes modified by another user.
- Classes deleted or trashed by another user.
- True conflicts where both your session and another session changed the same class.

Resolve the notification before continuing. This protects shared class systems on teams.

## Recover an earlier class

Use [Global data revisions](https://academy.bricksbuilder.io/builder/interface/global-data-history/) to inspect recorded class changes or recover an earlier value, including after deletion. Select **Revisions** in the class editor, or open **Manage > Global data revisions** and select **Classes**. Restoring a recorded class changes that item, while other classes keep their current values. This is separate from restoring a class out of trash.

## Best practices

- Use clear class names that describe purpose, not only appearance.
- Keep foundational classes locked once they are stable.
- Use categories for large systems such as layout, typography, buttons, cards, utilities, and components.
- Avoid deleting classes based only on the current page's usage filter.
- Review imports before accepting them on client sites.
- Keep utility classes small and predictable.
- Avoid creating several classes that set the same property in conflicting ways.

## Troubleshooting

### A class is in the manager but has no visible effect

Check whether the class is assigned to an element, has styles, and is not overridden by element ID styles or custom CSS.

### I cannot edit a class

The class may be locked, your user role may not have the required permission, or the Class Manager may be disabled.

### I restored a class and its name changed

That can happen when a class with the same name already exists. Rename the restored class if you need a different convention.

### Imported content does not look like the source site

Check whether imported classes were accepted, mapped to local classes, or rejected. Also check whether required variables, color palettes, or theme styles were imported.