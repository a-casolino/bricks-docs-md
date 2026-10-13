*Review legacy global elements in Bricks, convert them to components, and understand why new reusable work should use Components instead.*

> **Note**
>
> **Global elements are deprecated since Bricks 2.0. Use Components for new reusable builder structures, and convert existing global elements as soon as possible.**

Global elements remain visible for sites that already use them, but they are now a legacy feature. New reusable work should be created as [Components](https://academy.bricksbuilder.io/builder/features/components/), not as global elements.

## Review existing global elements

To find existing global element instances:

1. Go to `Bricks > Settings > General`.
2. Scroll to **Global elements** under the **Convert** section.
3. Start the global-elements review to retrieve a list of global element instances.

From there, review the affected pages and templates before converting, unlinking, or deleting anything.

## Convert to components

Use the converter under `Bricks > Settings > General > Convert` to convert global elements to components.

Bricks can convert global elements individually or in bulk. Nestable global elements cannot always be converted directly to components; in those cases, unlink them manually in the builder or use the converter flow that unlinks nestable global elements.

After conversion, delete the remaining global elements from the builder's elements panel.

## When to use templates instead

If you need to reuse a larger section or layout pattern without linked shared editing, save it as a template and insert it where needed. For linked reusable structures, use Components.