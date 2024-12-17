from absl.testing import absltest

from foo import foo_main


class FooTest(absltest.TestCase):

    def test_foo(self):
        foo_main()
