
from firexapp.testing.config_base import FlowTestConfiguration, assert_is_good_run


class MyFooDefaultTest(FlowTestConfiguration):
    def initial_firex_options(self) -> list:
        return ["submit", "--chain", "foo,bar"]

    def assert_expected_firex_output(self, cmd_output, cmd_err):
        assert "defeat     No success!!!" in cmd_output

    def assert_expected_return_code(self, ret_value):
        assert_is_good_run(ret_value)


class DefineMyOwnSuccessTest(FlowTestConfiguration):
    def initial_firex_options(self) -> list:
        return ["submit", "--chain", "foo,bar", "--define_success", "not likely"]

    def assert_expected_firex_output(self, cmd_output, cmd_err):
        assert "defeat     No not likely" in cmd_output, "Good try... but no"

    def assert_expected_return_code(self, ret_value):
        assert_is_good_run(ret_value)
