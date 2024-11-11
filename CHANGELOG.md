# CHANGELOG


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
