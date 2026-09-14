# Day 19 — Docker Misconfiguration Scanner Report

## Checks implemented
1. **Unpinned `latest` tag** — `FROM python:latest` means the exact
   base image can change between builds without warning, causing
   "works on my machine" drift and silently pulling in unreviewed
   upstream changes (including possible new vulnerabilities).
2. **Missing `USER` instruction** — without it, the container process
   runs as root inside the container. If an attacker achieves code
   execution inside the container (e.g., via an app-layer vuln), root
   inside the container is a much shorter path to a full **container
   breakout** onto the host than a non-privileged user would be.
3. **`EXPOSE 22`** — baking an SSH server into an application
   container is almost never appropriate; it's an unnecessary attack
   surface and usually indicates SSH was added for debugging and never
   removed.

## Test run
`sample_dockerfile.txt` is an intentionally vulnerable example
(unpinned `latest`, no `USER`, exposes SSH) — the scanner correctly
flags all three issues. `sample_dockerfile_secure.txt` shows the fixed
version (pinned version tag, explicit non-root `USER`, no SSH) for
comparison — running the scanner against it should report no findings.

## Secure Dockerfile checklist (deliverable)
- [ ] Pin base images to a specific version tag, not `latest`.
- [ ] Create and switch to a non-root `USER` before the final `CMD`.
- [ ] Never `EXPOSE` or install SSH/remote-admin services in an app image.
- [ ] Use multi-stage builds so build tools/secrets don't ship in the final image.
- [ ] Run `COPY` with the narrowest scope needed (avoid `COPY . .` when a `.dockerignore` isn't in place).
- [ ] Scan images with a vulnerability scanner (e.g., Trivy) as part of CI.

*Deliverable: static analyzer log against both sample Dockerfiles + this checklist.*
