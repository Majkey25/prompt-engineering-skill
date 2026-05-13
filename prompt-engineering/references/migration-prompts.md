# Migration Prompts

Migration prompts must prevent silent behavior loss.

## Required migration instructions

Tell the target agent to:

1. Inventory current functionality before changing code.
2. Identify old stack, target stack, entrypoints, routes, components, API boundaries, data flow, environment variables, build scripts, and deployment assumptions from repository evidence.
3. Map old routes to new routes.
4. Map old screens to new screens.
5. Map old state management and data loading to the target stack.
6. Preserve current user-visible behavior unless the prompt explicitly changes it.
7. Preserve current visual design when required.
8. Minimize unrelated changes.
9. Migrate incrementally where possible.
10. Verify each migrated slice before moving to the next risky slice.
11. Keep compatibility shims only when justified.
12. Remove dead legacy paths only when verified unused or explicitly in scope.
13. Produce a final migration report.

## React Router to Next.js App Router

Add these details only when the user's task names this migration:

- Discover current React Router routes, layouts, loaders/actions if present, route params, nested routes, redirects, and error boundaries.
- Map routes to Next.js App Router folders and `page`, `layout`, `loading`, `error`, `not-found`, and route handler files where appropriate.
- Detect which components must be client components. Add `use client` only when needed.
- Preserve CSS, assets, layout, and visual behavior.
- Verify route navigation, direct URL load, refresh behavior, and not-found behavior.

## Legacy PHP to Laravel

Add these details only when the user's task names this migration:

- Inventory legacy routes, includes/templates, forms, sessions/auth, database queries, uploads, cron jobs, and public assets.
- Map legacy pages to Laravel routes, controllers, requests, views/components, middleware, models, and config.
- Preserve URLs where required or add explicit redirects.
- Preserve forms, validation behavior, sessions, auth state, and database behavior.
- Run the app locally if possible and verify the main screens and flows in browser.
- Do not modernize UI unless explicitly requested.

## Migration report format

Require final response:

1. Migration scope completed
2. Old to new mapping
3. Behavior preserved
4. Visual verification performed
5. Live verification performed
6. Known gaps or blockers
7. Follow-up risks
