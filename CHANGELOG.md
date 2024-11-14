# CHANGELOG


## v0.8.0 (2024-11-14)

### Features

- Update Docker image build workflow annotations and improve log upload path
  ([`87a5d40`](https://github.com/MountainGod2/my_pkg/commit/87a5d408bba5b36c2d29b521fe25259673b3cc88))


## v0.7.0 (2024-11-13)

### Features

- Add id-token permission for Docker image build workflow
  ([`d993715`](https://github.com/MountainGod2/my_pkg/commit/d993715c96e72db5ce9c11ac9946d4c59e56924a))


## v0.6.0 (2024-11-13)

### Features

- Simplify Docker image build annotations and enhance provenance attestation step
  ([`5a1b680`](https://github.com/MountainGod2/my_pkg/commit/5a1b680eef369e295ebf2b859da5003570e22bc8))


## v0.5.0 (2024-11-13)

### Features

- Enhance Docker image build workflow with provenance attestation
  ([`8842b64`](https://github.com/MountainGod2/my_pkg/commit/8842b64d08687d8ab4eec7973511f925da006f24))


## v0.4.2 (2024-11-13)

### Bug Fixes

- Correct annotation format in Docker image build workflow
  ([`65a4222`](https://github.com/MountainGod2/my_pkg/commit/65a42224ce7142c21a1db498ef317aa6cd2aa07f))


## v0.4.1 (2024-11-13)

### Bug Fixes

- Update Docker workflow to correct image description annotation format
  ([`2f24669`](https://github.com/MountainGod2/my_pkg/commit/2f246698bf5ccf335096be49a40f54ff6be8b325))


## v0.4.0 (2024-11-13)

### Features

- Refactor Docker workflow to streamline builds, add nightly schedule, and support multi-platform
  architecture
  ([`26e3636`](https://github.com/MountainGod2/my_pkg/commit/26e363681d2f1c524d0e239ef8d4daaf896fad6c))


## v0.3.6 (2024-11-13)

### Bug Fixes

- Update Docker workflow to support multi-platform builds and refine artifact naming
  ([`45fdc69`](https://github.com/MountainGod2/my_pkg/commit/45fdc699a8a2dcee695a18c58d579be90ef781a1))


## v0.3.5 (2024-11-13)

### Bug Fixes

- Simplify Docker image build workflow by removing unnecessary comments and refining artifact names
  ([`16d19ed`](https://github.com/MountainGod2/my_pkg/commit/16d19edc86c3a8865ade9106719af1a0433a3733))


## v0.3.4 (2024-11-13)

### Bug Fixes

- Update Docker image build workflow to push by tag instead of digest
  ([`43bfabb`](https://github.com/MountainGod2/my_pkg/commit/43bfabb301d26432a5968267b35c34716b760981))


## v0.3.3 (2024-11-13)

### Bug Fixes

- Restore push-by-digest option in Docker image build outputs
  ([`4a4ad20`](https://github.com/MountainGod2/my_pkg/commit/4a4ad20ca17a0b2586ca2563f19bd5d9dc28b31b))


## v0.3.2 (2024-11-13)

### Bug Fixes

- Remove unsupported ARM architectures from Docker build workflow
  ([`cbdbbd0`](https://github.com/MountainGod2/my_pkg/commit/cbdbbd0d0d3a1aba9359de2684a8cbc4d0e5f668))


## v0.3.1 (2024-11-13)

### Bug Fixes

- Remove push-by-digest option from Docker image build outputs
  ([`92dc25e`](https://github.com/MountainGod2/my_pkg/commit/92dc25e596783442b9759923c9f5594aae9d61c4))


## v0.3.0 (2024-11-13)

### Features

- Enhance Docker build workflow for multi-platform support
  ([`bc4ab11`](https://github.com/MountainGod2/my_pkg/commit/bc4ab110960c1ee398c9697e5e30e075eca20337))


## v0.2.1 (2024-11-13)

### Bug Fixes

- Update docker-image-build.yml
  ([`195ef89`](https://github.com/MountainGod2/my_pkg/commit/195ef89898534f8e632b2e0fd639230731b99245))


## v0.2.0 (2024-11-11)

### Features

- Refactor greeting function and update main entry point
  ([`7617cf4`](https://github.com/MountainGod2/my_pkg/commit/7617cf4ba8b5dccec19fb660de046b52be675d13))

- Add main entry point and update greeting function to print message
  ([`ad41157`](https://github.com/MountainGod2/my_pkg/commit/ad41157aed653340f803ff3425286435172f4ece))


## v0.1.7 (2024-11-11)

### Bug Fixes

- Remove unused SHA type from Docker image build workflow
  ([`25945cb`](https://github.com/MountainGod2/my_pkg/commit/25945cb7f77c225d88b2eaf26767d28824e58efa))


## v0.1.6 (2024-11-11)

### Bug Fixes

- Update continuous deployment and Docker image build workflows to use GITHUB_TOKEN and DOCKER_PAT
  for authentication
  ([`1a56964`](https://github.com/MountainGod2/my_pkg/commit/1a5696422da04958ab8893062fc153cd19a98f4a))

- Update continuous deployment workflow to ensure correct branch checkout and use GH_PAT for
  authentication
  ([`f44015f`](https://github.com/MountainGod2/my_pkg/commit/f44015f1669a8ff48a9e0d12774b33749d493153))

- Update user email and name in continuous deployment workflow
  ([`2d47936`](https://github.com/MountainGod2/my_pkg/commit/2d479361adc8cb53d10e5d57978f4554b0782922))

- Update continuous deployment workflow to enhance authentication and permissions
  ([`eeffa83`](https://github.com/MountainGod2/my_pkg/commit/eeffa83c50954e87e934c25522e47512b183014d))

- Remove hardcoded committer name from continuous deployment workflow
  ([`27c18d6`](https://github.com/MountainGod2/my_pkg/commit/27c18d6e28eb1c3de08cc382453589dd820f5ddc))

- Update GitHub token in continuous deployment workflow and correct label format in Dockerfile
  ([`4622091`](https://github.com/MountainGod2/my_pkg/commit/462209183c29281aa64441bbf0fbb642e6e735f3))

- Remove pre-check job from Docker image build workflow and update checkout step to use GH_PAT
  ([`52112c7`](https://github.com/MountainGod2/my_pkg/commit/52112c71d0109bffbbd1d9730d3b4f617c5b94fb))

- Enhance Docker image build workflow with pre-checks and multi-platform support
  ([`fbf6e69`](https://github.com/MountainGod2/my_pkg/commit/fbf6e696eacb6cf3d6815ad5d5fac2fbfb7e6f6b))

- Update Docker image build workflow to use GITHUB_TOKEN for authentication
  ([`adf833f`](https://github.com/MountainGod2/my_pkg/commit/adf833f65977a8216b1e0f4ff24f9287c47a34dc))


## v0.1.5 (2024-11-10)

### Bug Fixes

- Update Docker image build workflow to use hardcoded registry URL
  ([`4876988`](https://github.com/MountainGod2/my_pkg/commit/48769888a31478bd0fc99d0ed600ded05cedd0a2))


## v0.1.4 (2024-11-10)

### Bug Fixes

- Update Docker image build workflow to use hardcoded registry URL
  ([`25fe4bf`](https://github.com/MountainGod2/my_pkg/commit/25fe4bfd45e32d9da79c80275bd2bf87b5559695))


## v0.1.3 (2024-11-10)

### Bug Fixes

- Move REGISTRY environment variable to the correct step in Docker image build workflow
  ([`9a2105c`](https://github.com/MountainGod2/my_pkg/commit/9a2105c4ddd39710284066d4c89dcee3aa2a86cb))


## v0.1.2 (2024-11-10)

### Bug Fixes

- Update Docker image build workflow to use environment variable for registry
  ([`76e9d68`](https://github.com/MountainGod2/my_pkg/commit/76e9d68d981a38d688b3dce3ca502bb96f4e86ed))


## v0.1.1 (2024-11-10)

### Bug Fixes

- Update GitHub Actions to use GITHUB_TOKEN for Docker login
  ([`d2f7ff6`](https://github.com/MountainGod2/my_pkg/commit/d2f7ff6ed74117841d0e898a276fc2ac57acac0c))


## v0.1.0 (2024-11-10)

### Features

- Initial commit of my_pkg
  ([`9c75e1f`](https://github.com/MountainGod2/my_pkg/commit/9c75e1fde3aacff1d2f42d017d4b75df2679375a))
