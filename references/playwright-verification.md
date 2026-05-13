# Playwright Verification

Use for UI, frontend, dashboard, browser, visual matching, pixel preservation, responsive layout, and Playwright requests.

## Default UI verification

- Use Playwright or Playwright Interactive if available.
- Start the app using existing scripts.
- Open the relevant route in a browser.
- Verify by interacting with the UI, not by staring at source code only.
- Check console errors.
- Check failed network requests when frontend talks to an API.
- Capture screenshots when visual output matters.

## Visual preservation

If the user asks to keep screens the same, preserve UI, match pixels, avoid visual regressions, or migrate without changing appearance:

1. Capture a baseline screenshot before changes if the original state can be run.
2. Capture a post-change screenshot after implementation.
3. Compare main screens manually and, if tooling exists, with visual diff tooling.
4. Check desktop and at least one narrow/mobile viewport when responsive behavior matters.
5. Do not redesign by taste.
6. Do not change spacing, colors, typography, layout, component hierarchy, animation, or responsive behavior unless required.
7. Report any unavoidable mismatch explicitly.

## Browser checks

The target agent should check:

- page load success
- visible main content
- route transitions
- form inputs and buttons affected by the change
- error states where relevant
- console errors and warnings that matter
- failed or unexpected network calls
- layout overflow, clipped content, and responsive breakage

## Playwright Interactive phrasing

Use this in generated prompts when relevant:

```text
Use Playwright Interactive if available. Navigate the app like a user. Capture screenshots before and after the change when possible. Inspect console and network errors. Do not finish until the changed flow and the main old flow are verified in the browser, or until you document the exact blocker.
```
