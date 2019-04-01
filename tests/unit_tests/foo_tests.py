import unittest
from firex_bundle_foobar.foo_tasks import foo


class FooBarTests(unittest.TestCase):
    def test_i_do_not_know_what_success_is(self):
        self.assertEqual(foo(), "success!!!")

    def test_redefine_success(self):
        success = "getting through the day"
        self.assertEqual(foo(success), "success")
