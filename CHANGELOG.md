# CHANGELOG


## v0.12.3 (2024-11-16)

### Bug Fixes

- Remove unnecessary branch trigger from Docker image build workflow
  ([`ae3143c`](https://github.com/MountainGod2/my_pkg/commit/ae3143c8baf9889f85fff08d2502a49888c36586))


## v0.12.2 (2024-11-16)

### Bug Fixes

- Update permissions in continuous deployment workflow
  ([`2af5b5d`](https://github.com/MountainGod2/my_pkg/commit/2af5b5d3bf177dca927122c70a6bc98a349d454d))

### Chores

- Remove merge_group trigger from continuous integration workflow
  ([`acd9ad9`](https://github.com/MountainGod2/my_pkg/commit/acd9ad9acd9504c7594ef04e2b7dd9fe356ef661))


## v0.12.1 (2024-11-16)

### Bug Fixes

- Update dependency versions in pyproject.toml for improved compatibility
  ([`9d6226e`](https://github.com/MountainGod2/my_pkg/commit/9d6226e68d30ff3a22c368186b115c9a3f91aac8))

### Chores

- **deps**: Lock file maintenance ([#11](https://github.com/MountainGod2/my_pkg/pull/11),
  [`cbc89bd`](https://github.com/MountainGod2/my_pkg/commit/cbc89bd3a4eced2a37e46c1436278519cffd7f6f))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.12.0 (2024-11-16)

### Chores

- **deps**: Remove schedule for lock file maintenance and Docker dependency grouping
  ([`4630356`](https://github.com/MountainGod2/my_pkg/commit/46303560a667aff170df80d98b36d1499a203739))

### Features

- Add merge_group trigger to continuous integration workflow
  ([`d29e972`](https://github.com/MountainGod2/my_pkg/commit/d29e972646132d61b34035a968fe8a21e26eee50))


## v0.11.8 (2024-11-16)

### Bug Fixes

- Add build provenance attestation step to continuous deployment workflow
  ([`19fa9d3`](https://github.com/MountainGod2/my_pkg/commit/19fa9d3756b980b57747c936f6931e54cac38ab4))

### Chores

- **deps**: Lock file maintenance ([#10](https://github.com/MountainGod2/my_pkg/pull/10),
  [`acbadcf`](https://github.com/MountainGod2/my_pkg/commit/acbadcf3fd3c68fa4ba05776038be18d23573d52))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.11.7 (2024-11-15)

### Bug Fixes

- Update Docker image build workflow permissions to include attestations
  ([`be31a20`](https://github.com/MountainGod2/my_pkg/commit/be31a2019d044f50487b48125c00b56c0b0baff6))


## v0.11.6 (2024-11-15)

### Bug Fixes

- Update Docker image build workflow to use lowercase repository name and add build provenance
  attestation
  ([`70abd2e`](https://github.com/MountainGod2/my_pkg/commit/70abd2e2551b34ca80fee75f05f2080484772c92))


## v0.11.5 (2024-11-15)

### Bug Fixes

- Update GitHub Actions workflows to use secrets directly and add publish step
  ([`dc04d0d`](https://github.com/MountainGod2/my_pkg/commit/dc04d0d8e59e37e752f36628a08d651d9705fc29))

### Chores

- **deps**: Lock file maintenance ([#9](https://github.com/MountainGod2/my_pkg/pull/9),
  [`3569d0d`](https://github.com/MountainGod2/my_pkg/commit/3569d0ddb1fdf579e2f839bb6788613fe99df4d6))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Lock file maintenance
  ([`b566d8a`](https://github.com/MountainGod2/my_pkg/commit/b566d8adf1f4fc192e4f247dc262b50d3f7f6d7a))


## v0.11.4 (2024-11-15)

### Bug Fixes

- Update GitHub Actions workflow to use GITHUB_TOKEN and add exempt labels
  ([`5911d27`](https://github.com/MountainGod2/my_pkg/commit/5911d27361b461b29075056bfaa34d2240cf8684))

### Chores

- **deps**: Lock file maintenance ([#8](https://github.com/MountainGod2/my_pkg/pull/8),
  [`bbd2106`](https://github.com/MountainGod2/my_pkg/commit/bbd210643dd089d10a794fe201f2bcdb2539bc5b))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>


## v0.11.3 (2024-11-15)

### Bug Fixes

- Convert repository name to lowercase for Docker image build and update related steps
  ([`ca3e86d`](https://github.com/MountainGod2/my_pkg/commit/ca3e86d40701071535ca40ba716437b909f373a8))


## v0.11.2 (2024-11-15)

### Bug Fixes

- Update permissions for Docker image build workflow and add testing step
  ([`8bc057e`](https://github.com/MountainGod2/my_pkg/commit/8bc057e534293c2a71043b4c8b2877df6f698230))

- Update build log handling in Docker image build workflow
  ([`73a4011`](https://github.com/MountainGod2/my_pkg/commit/73a4011d10ae851c20093580ec53e29e6017e816))


## v0.11.1 (2024-11-15)

### Bug Fixes

- Update permissions to allow writing contents in Docker image build workflow
  ([`3cfdce0`](https://github.com/MountainGod2/my_pkg/commit/3cfdce023901082410d5ed27279845d999617cdc))


## v0.11.0 (2024-11-15)

### Features

- Add steps to save and display Docker build logs
  ([`88bd152`](https://github.com/MountainGod2/my_pkg/commit/88bd152235b6dfabbc58dc755dd4f320d4bb1c7b))


## v0.10.1 (2024-11-15)

### Bug Fixes

- Update Docker image build workflow to use GITHUB_TOKEN instead of DOCKER_PAT
  ([`4fdf54b`](https://github.com/MountainGod2/my_pkg/commit/4fdf54b35d718e6e553506f267e219f74522b69d))


## v0.10.0 (2024-11-15)

### Features

- Remove id-token permission and adjust Docker image build tags
  ([`afe6925`](https://github.com/MountainGod2/my_pkg/commit/afe6925184cf833301d931b3a47a6b4f732a9976))


## v0.9.6 (2024-11-15)

### Bug Fixes

- Update semver pattern to conditionally enable for non-tag branches
  ([`ed7aac1`](https://github.com/MountainGod2/my_pkg/commit/ed7aac1ac954caa23e3ebc9b93177ba501779771))


## v0.9.5 (2024-11-15)

### Bug Fixes

- Adjust priority for SHA type in Docker image build workflow
  ([`bd5da17`](https://github.com/MountainGod2/my_pkg/commit/bd5da177ca50d9af9d34e0750158ed949d0c44c9))


## v0.9.4 (2024-11-15)

### Bug Fixes

- Remove annotations from Docker image build workflow
  ([`c5ea295`](https://github.com/MountainGod2/my_pkg/commit/c5ea295bb94b57ff00731c4e3199ce415d6d2fd7))


## v0.9.3 (2024-11-15)

### Bug Fixes

- Remove unnecessary labels from Docker image build workflow
  ([`ae51701`](https://github.com/MountainGod2/my_pkg/commit/ae51701452132cc7672a8fb534e0f274180ae57b))

- Remove unnecessary metadata labels from Dockerfile
  ([`3e45e93`](https://github.com/MountainGod2/my_pkg/commit/3e45e93c94ff0c5f5536b2a551cca4cb97b2409d))


## v0.9.2 (2024-11-14)

### Bug Fixes

- Add labels for Docker image metadata in workflow
  ([`6e8fbe6`](https://github.com/MountainGod2/my_pkg/commit/6e8fbe6dfe38f217107846b3982b35b66880c5f8))


## v0.9.1 (2024-11-14)

### Bug Fixes

- Update Dockerfile and workflow metadata for improved image labeling
  ([`bc7ff1d`](https://github.com/MountainGod2/my_pkg/commit/bc7ff1d713b1983204855b3353cabae7c5dc62f0))

### Chores

- **deps**: Update actions/upload-artifact action to v4
  ([#4](https://github.com/MountainGod2/my_pkg/pull/4),
  [`6ff9759`](https://github.com/MountainGod2/my_pkg/commit/6ff9759ef06b76b9f9b56a5b2e57eec82566e178))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Update dependency ubuntu to v24 ([#5](https://github.com/MountainGod2/my_pkg/pull/5),
  [`b144e30`](https://github.com/MountainGod2/my_pkg/commit/b144e305624eeb3e06878404e5d69d4364c443f4))

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

- **deps**: Lock file maintenance
  ([`2b84019`](https://github.com/MountainGod2/my_pkg/commit/2b840191f7e42b2a0e04577c1da68d7e86c43bce))

- Update package version to 0.9.0 in uv.lock
  ([`a1fe012`](https://github.com/MountainGod2/my_pkg/commit/a1fe012d378574c752dce358b73710afec4644d3))


## v0.9.0 (2024-11-14)

### Features

- Enhance Docker image build workflow with dynamic Open Container Initiative labels and annotations
  ([`2f7df93`](https://github.com/MountainGod2/my_pkg/commit/2f7df93c4ecd488d77b2a11d329b11a56e66c815))


## v0.8.1 (2024-11-14)

### Bug Fixes

- Update Docker image build workflow to include Open Container Initiative labels
  ([`1574e79`](https://github.com/MountainGod2/my_pkg/commit/1574e79081142154bd17a62dbd2eb83bbd2f8935))


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
