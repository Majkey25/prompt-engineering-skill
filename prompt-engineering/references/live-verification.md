# Live Verification

Live verification is the default quality gate. The target agent must test the real changed behavior when the environment allows it.

## General rule

Run the most relevant available verification path. Prefer real execution over theoretical confidence.

Continue while a clear, safe, available next step can increase confidence that the task is done.

## Project startup

- Use existing scripts before inventing commands.
- Check README, package files, Makefile, Docker config, CI config, and framework docs inside the repo.
- Start the dev server, backend server, preview build, CLI, or app only when safe in the environment.
- If startup needs secrets, external services, unavailable ports, missing dependencies, or unsupported OS features, state the exact blocker.

## Frontend

- Run the app or preview build when possible.
- Open the app in a browser if browser tools are available.
- Visit main routes and changed screens.
- Click through the main user flow affected by the change.
- Check browser console errors.
- Check network failures when API calls are part of the flow.
- Verify responsive breakpoints when UI layout is relevant.

## Backend/API

- Start the backend when possible.
- Verify changed endpoints through existing clients, HTTP requests, API docs, curl, test clients, or framework tooling.
- Check status codes, response shape, validation failures, auth/error paths, and logs where relevant.
- Verify old clients or routes still work when compatibility is required.

## CLI

- Run the actual command with a safe sample input.
- Verify exit code, stdout, stderr, output files, and error handling.
- Do not claim CLI behavior works if it was not executed.

## Build, lint, and typecheck

- Run existing build, lint, typecheck, format-check, and test commands when they exist and are relevant.
- Do not invent a toolchain.
- Do not hide failing output. Investigate or report exact blockers.
- If a command fails for pre-existing unrelated reasons, prove it is unrelated before moving on.

## Tests

- Use existing tests when relevant.
- Pytest is optional. Use it only if the project already uses pytest, the user explicitly requests it, or Python pytest infrastructure clearly exists.
- Do not add tests only to look rigorous.

## If live verification cannot run

The target agent must report:

- exact attempted command or action
- exact failure or missing dependency
- why it blocks verification
- what lower-confidence checks were still performed
- what the user or environment must provide to complete live verification
