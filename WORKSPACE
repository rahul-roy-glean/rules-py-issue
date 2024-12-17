workspace(name = "test_repo")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive", "http_file", "http_jar")

http_archive(
    name = "rules_python",
    sha256 = "be04b635c7be4604be1ef20542e9870af3c49778ce841ee2d92fcb42f9d9516a",
    strip_prefix = "rules_python-0.35.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.35.0/rules_python-0.35.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")

py_repositories()

python_register_toolchains(
    name = "python310",
    ignore_root_user_error = True,
    python_version = "3.10",
    register_coverage_tool = True,
)

load("@python310//:defs.bzl", "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

pip_parse(
    name = "pip",
    extra_pip_args = [
        "--retries",
        "10",
        "--verbose",
    ],
    python_interpreter_target = interpreter,
    requirements_darwin = "//:requirements.txt",
    requirements_lock = "//:requirements.txt",
)

load("@pip//:requirements.bzl", "install_deps")

install_deps()
